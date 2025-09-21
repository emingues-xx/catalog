#!/usr/bin/env python3
"""
Script de sincronização que funciona com a API do Outline
Versão simplificada que usa apenas a coleção existente
"""

import os
import sys
import yaml
import requests
import json
from pathlib import Path
from typing import Dict, List, Optional, Any

class OutlineSyncWorking:
    def __init__(self):
        self.api_url = "https://outline-production-47e1.up.railway.app"
        self.api_token = os.getenv('OUTLINE_API_TOKEN', 'ol_api_tekTu1JQZ5x6DryFECHKN6mXfdB8weVcAjKJxN')
        
        if not self.api_token:
            raise ValueError("OUTLINE_API_TOKEN deve estar definido")
        
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Carregar configuração de mapeamento
        self.mapping_config = self._load_mapping_config()
        
    def _load_mapping_config(self) -> Dict[str, Any]:
        """Carrega a configuração de mapeamento do arquivo YAML"""
        # Tentar diferentes caminhos para o arquivo de mapeamento
        possible_paths = [
            Path('outline-mapping.yaml'),
            Path.cwd() / 'outline-mapping.yaml',
            Path(__file__).parent.parent.parent / 'outline-mapping.yaml'
        ]
        
        mapping_file = None
        for path in possible_paths:
            if path.exists():
                mapping_file = path
                break
        
        if not mapping_file:
            print("⚠️ Arquivo outline-mapping.yaml não encontrado, usando configuração padrão")
            return self._get_default_mapping()
        
        with open(mapping_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def _get_default_mapping(self) -> Dict[str, Any]:
        """Retorna configuração padrão caso o arquivo de mapeamento não exista"""
        return {
            'config': {
                'default_collection_id': 'e581b5ff-6e58-45ae-ac32-ac40bd83d8f7',  # Coleção "Docs"
                'default_tags': ['backstage', 'documentation']
            },
            'documents': {},
            'collections': {}
        }
    
    def _get_document_mapping(self, file_path: str) -> Dict[str, Any]:
        """Obtém o mapeamento específico para um documento"""
        return self.mapping_config.get('documents', {}).get(file_path, {})
    
    def _get_document_parent(self, file_path: str) -> Optional[str]:
        """Obtém o documento pai baseado no mapeamento YAML"""
        mapping = self._get_document_mapping(file_path)
        
        if not mapping:
            return None
        
        return mapping.get('parent_document')
    
    def _get_document_title(self, file_path: str, file_name: str) -> str:
        """Obtém o título do documento no Outline"""
        mapping = self._get_document_mapping(file_path)
        if 'title' in mapping:
            return mapping['title']
        
        # Gerar título baseado no nome do arquivo
        title = file_name.replace('.md', '').replace('_', ' ').replace('-', ' ')
        return title.title()
    
    def _get_document_tags(self, file_path: str) -> List[str]:
        """Obtém as tags do documento"""
        mapping = self._get_document_mapping(file_path)
        default_tags = self.mapping_config['config'].get('default_tags', [])
        return mapping.get('tags', default_tags)
    
    def _get_document_description(self, file_path: str) -> str:
        """Obtém a descrição do documento"""
        mapping = self._get_document_mapping(file_path)
        return mapping.get('description', '')
    
    def _test_api_connection(self) -> bool:
        """Testa a conexão com a API"""
        try:
            # Testar com documents.list
            test_data = {"id": ""}
            response = requests.post(
                f'{self.api_url}/api/documents.list',
                headers=self.headers,
                json=test_data,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                documents = data.get('data', [])
                print(f"✅ Conexão com API OK - {len(documents)} documentos encontrados")
                
                # Testar collections.list também
                collections_response = requests.post(
                    f'{self.api_url}/api/collections.list',
                    headers=self.headers,
                    json=test_data,
                    timeout=10
                )
                
                if collections_response.status_code == 200:
                    collections_data = collections_response.json()
                    collections = collections_data.get('data', [])
                    print(f"✅ Coleções acessíveis - {len(collections)} coleções encontradas")
                    
                    # Verificar se a coleção padrão existe
                    default_collection_id = self.mapping_config['config']['default_collection_id']
                    collection_exists = any(col.get('id') == default_collection_id for col in collections)
                    
                    if collection_exists:
                        print(f"✅ Coleção padrão encontrada: {default_collection_id}")
                    else:
                        print(f"⚠️ Coleção padrão não encontrada: {default_collection_id}")
                        print("Coleções disponíveis:")
                        for col in collections:
                            print(f"  - {col.get('id')}: {col.get('name')}")
                
                return True
            else:
                print(f"❌ Erro na API: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Erro de conexão: {e}")
            return False
    
    
    
    def _search_document(self, title: str) -> Optional[str]:
        """Busca um documento existente no Outline pelo título"""
        try:
            test_data = {"id": ""}
            response = requests.post(
                f'{self.api_url}/api/documents.list',
                headers=self.headers,
                json=test_data,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                documents = data.get('data', [])
                for doc in documents:
                    if doc.get('title') == title:
                        return doc.get('id')
            
            return None
        except Exception as e:
            print(f"❌ Erro ao buscar documento '{title}': {e}")
            return None
    
    def _create_or_update_document(self, file_path: str, content: str) -> bool:
        """Cria ou atualiza um documento no Outline"""
        try:
            file_name = Path(file_path).name
            title = self._get_document_title(file_path, file_name)
            tags = self._get_document_tags(file_path)
            description = self._get_document_description(file_path)
            
            # Adicionar metadados ao conteúdo
            enhanced_content = self._enhance_content(content, file_path, tags)
            
            # Obter coleção e documento pai
            mapping = self._get_document_mapping(file_path)
            collection_id = mapping.get('collection_id', self.mapping_config['config']['default_collection_id'])
            parent_document_title = self._get_document_parent(file_path)
            
            print(f"📄 Processando documento: '{title}'")
            print(f"📁 Coleção: {collection_id}")
            if parent_document_title:
                print(f"👨‍👩‍👧‍👦 Documento pai: '{parent_document_title}'")
            
            # Buscar documento existente
            doc_id = self._search_document(title)
            
            # Buscar ID do documento pai se especificado
            parent_document_id = None
            if parent_document_title:
                parent_document_id = self._search_document(parent_document_title)
                if not parent_document_id:
                    print(f"⚠️ Documento pai '{parent_document_title}' não encontrado. Criando documento sem pai.")
            
            if doc_id:
                # Atualizar documento existente
                data = {
                    'id': doc_id,
                    'text': enhanced_content,
                    'readonly': True,
                    'collectionId': collection_id
                }
                
                # Adicionar parentId se especificado
                if parent_document_id:
                    data['parentDocumentId'] = parent_document_id
                
                response = requests.post(f'{self.api_url}/api/documents.update', headers=self.headers, json=data)
                
                if response.status_code in [200, 201]:
                    print(f"✅ Documento '{title}' atualizado com sucesso (readonly)")
                    return True
                else:
                    print(f"❌ Erro ao atualizar documento '{title}': {response.status_code} - {response.text}")
                    return False
            else:
                # Criar novo documento público e readonly
                data = {
                    'title': title,
                    'text': enhanced_content,
                    'publish': True,
                    'collectionId': collection_id
                }
                
                # Adicionar parentId se especificado
                if parent_document_id:
                    data['parentDocumentId'] = parent_document_id
                
                response = requests.post(f'{self.api_url}/api/documents.create', headers=self.headers, json=data)
                
                if response.status_code in [200, 201]:
                    doc_id = response.json().get('data', {}).get('id')
                    print(f"✅ Documento '{title}' criado com sucesso (ID: {doc_id})")
                    
                    # Tentar tornar o documento readonly
                    try:
                        readonly_data = {
                            'id': doc_id,
                            'readonly': True
                        }
                        readonly_response = requests.post(f'{self.api_url}/api/documents.update', headers=self.headers, json=readonly_data)
                        if readonly_response.status_code in [200, 201]:
                            print(f"✅ Documento '{title}' configurado como readonly")
                        else:
                            print(f"⚠️ Não foi possível configurar readonly para '{title}': {readonly_response.status_code}")
                    except Exception as e:
                        print(f"⚠️ Erro ao configurar readonly para '{title}': {e}")
                    
                    return True
                else:
                    print(f"❌ Erro ao criar documento '{title}': {response.status_code} - {response.text}")
                    return False
                
        except Exception as e:
            print(f"❌ Erro ao processar documento '{file_path}': {e}")
            return False
    
    def _enhance_content(self, content: str, file_path: str, tags: List[str]) -> str:
        """Adiciona metadados e informações extras ao conteúdo"""
        github_repo = os.getenv('GITHUB_REPOSITORY', '')
        github_sha = os.getenv('GITHUB_SHA', '')
        
        # Adicionar cabeçalho com informações do repositório
        header = f"""---
*Documento sincronizado automaticamente do repositório [{github_repo}](https://github.com/{github_repo})*
*Última atualização: commit {github_sha[:8] if github_sha else 'N/A'}*
*Arquivo original: `{file_path}`*

---

"""
        
        # Adicionar rodapé com tags
        footer = f"""

---

**Tags:** {', '.join([f'`{tag}`' for tag in tags])}
**Fonte:** [{github_repo}](https://github.com/{github_repo}/blob/main/{file_path})
"""
        
        return header + content + footer
    
    def sync_documents(self):
        """Sincroniza todos os documentos do diretório docs/"""
        print("🚀 Iniciando sincronização com Outline...")
        
        # Testar conexão com API
        if not self._test_api_connection():
            print("❌ Falha na conexão com a API. Abortando sincronização.")
            return False
        
        # Tentar diferentes caminhos para o diretório docs
        possible_docs_paths = [
            Path('docs'),
            Path.cwd() / 'docs',
            Path(__file__).parent.parent.parent / 'docs'
        ]
        
        docs_dir = None
        for path in possible_docs_paths:
            if path.exists():
                docs_dir = path
                break
        
        if not docs_dir:
            print("❌ Diretório 'docs' não encontrado")
            return False
        
        print(f"📁 Usando diretório docs: {docs_dir}")
        
        success_count = 0
        error_count = 0
        
        # Processar todos os arquivos .md
        md_files = list(docs_dir.rglob('*.md'))
        print(f"📄 Encontrados {len(md_files)} arquivos .md para processar")
        
        for md_file in md_files:
            try:
                # Usar caminho relativo ao diretório docs
                file_path = str(md_file.relative_to(docs_dir.parent))
                print(f"📝 Processando: {file_path}")
                
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if self._create_or_update_document(file_path, content):
                    success_count += 1
                else:
                    error_count += 1
                    
            except Exception as e:
                print(f"❌ Erro ao processar arquivo '{md_file}': {e}")
                error_count += 1
        
        print(f"\n📊 Resumo da sincronização:")
        print(f"✅ Documentos sincronizados com sucesso: {success_count}")
        print(f"❌ Documentos com erro: {error_count}")
        
        return error_count == 0

def main():
    """Função principal"""
    try:
        syncer = OutlineSyncWorking()
        success = syncer.sync_documents()
        
        if success:
            print("\n🎉 Sincronização concluída com sucesso!")
            sys.exit(0)
        else:
            print("\n💥 Sincronização concluída com erros!")
            sys.exit(1)
            
    except Exception as e:
        print(f"💥 Erro fatal: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
