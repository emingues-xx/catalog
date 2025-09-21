#!/usr/bin/env python3
"""
Script para sincronizar documentação do diretório docs/ com o Outline
"""

import os
import sys
import yaml
import requests
import json
from pathlib import Path
from typing import Dict, List, Optional, Any

class OutlineSync:
    def __init__(self):
        self.api_url = os.getenv('OUTLINE_API_URL')
        self.api_token = os.getenv('OUTLINE_API_TOKEN')
        self.github_repo = os.getenv('GITHUB_REPOSITORY', '')
        self.github_sha = os.getenv('GITHUB_SHA', '')
        
        if not self.api_url or not self.api_token:
            raise ValueError("OUTLINE_API_URL e OUTLINE_API_TOKEN devem estar definidos")
        
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
        
        # Carregar configuração de mapeamento
        self.mapping_config = self._load_mapping_config()
        
    def _load_mapping_config(self) -> Dict[str, Any]:
        """Carrega a configuração de mapeamento do arquivo YAML"""
        mapping_file = Path('outline-mapping.yaml')
        if not mapping_file.exists():
            print("⚠️ Arquivo outline-mapping.yaml não encontrado, usando configuração padrão")
            return self._get_default_mapping()
        
        with open(mapping_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def _get_default_mapping(self) -> Dict[str, Any]:
        """Retorna configuração padrão caso o arquivo de mapeamento não exista"""
        return {
            'config': {
                'default_collection_id': 'default-collection',
                'default_tags': ['backstage', 'documentation']
            },
            'documents': {},
            'collections': {}
        }
    
    def _get_document_mapping(self, file_path: str) -> Dict[str, Any]:
        """Obtém o mapeamento específico para um documento"""
        return self.mapping_config.get('documents', {}).get(file_path, {})
    
    def _get_collection_id(self, file_path: str) -> str:
        """Obtém o ID da coleção para um documento"""
        mapping = self._get_document_mapping(file_path)
        return mapping.get('collection_id', self.mapping_config['config']['default_collection_id'])
    
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
    
    def _search_document(self, title: str) -> Optional[str]:
        """Busca um documento existente no Outline pelo título"""
        try:
            response = requests.get(
                f'{self.api_url}/documents.search',
                headers=self.headers,
                params={'query': title}
            )
            
            if response.status_code == 200:
                results = response.json().get('data', [])
                for doc in results:
                    if doc.get('title') == title:
                        return doc.get('id')
            
            return None
        except Exception as e:
            print(f"❌ Erro ao buscar documento '{title}': {e}")
            return None
    
    def _create_collection(self, collection_id: str, name: str, description: str = "", color: str = "#3B82F6") -> bool:
        """Cria uma coleção no Outline se ela não existir"""
        try:
            # Verificar se a coleção já existe
            response = requests.get(f'{self.api_url}/collections.list', headers=self.headers)
            if response.status_code == 200:
                collections = response.json().get('data', [])
                for collection in collections:
                    if collection.get('id') == collection_id:
                        print(f"✅ Coleção '{name}' já existe")
                        return True
            
            # Para sub-coleções, usar a coleção pai como parent
            parent_collection_id = self.mapping_config['config']['default_collection_id']
            
            # Criar nova coleção
            data = {
                'name': name,
                'description': description,
                'color': color,
                'private': False
            }
            
            # Se não for a coleção pai, adicionar como sub-coleção
            if collection_id != parent_collection_id:
                data['parentId'] = parent_collection_id
            
            response = requests.post(f'{self.api_url}/collections.create', headers=self.headers, json=data)
            
            if response.status_code in [200, 201]:
                print(f"✅ Coleção '{name}' criada com sucesso")
                return True
            else:
                print(f"❌ Erro ao criar coleção '{name}': {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao criar coleção '{name}': {e}")
            return False
    
    def _create_or_update_document(self, file_path: str, content: str) -> bool:
        """Cria ou atualiza um documento no Outline"""
        try:
            file_name = Path(file_path).name
            title = self._get_document_title(file_path, file_name)
            collection_id = self._get_collection_id(file_path)
            tags = self._get_document_tags(file_path)
            description = self._get_document_description(file_path)
            
            # Adicionar metadados ao conteúdo
            enhanced_content = self._enhance_content(content, file_path, tags)
            
            # Buscar documento existente
            doc_id = self._search_document(title)
            
            if doc_id:
                # Atualizar documento existente
                data = {
                    'id': doc_id,
                    'text': enhanced_content
                }
                
                response = requests.post(f'{self.api_url}/documents.update', headers=self.headers, json=data)
                
                if response.status_code in [200, 201]:
                    print(f"✅ Documento '{title}' atualizado com sucesso")
                    return True
                else:
                    print(f"❌ Erro ao atualizar documento '{title}': {response.text}")
                    return False
            else:
                # Criar novo documento
                data = {
                    'title': title,
                    'text': enhanced_content,
                    'collectionId': collection_id,
                    'publish': True
                }
                
                response = requests.post(f'{self.api_url}/documents.create', headers=self.headers, json=data)
                
                if response.status_code in [200, 201]:
                    print(f"✅ Documento '{title}' criado com sucesso")
                    return True
                else:
                    print(f"❌ Erro ao criar documento '{title}': {response.text}")
                    return False
                    
        except Exception as e:
            print(f"❌ Erro ao processar documento '{file_path}': {e}")
            return False
    
    def _enhance_content(self, content: str, file_path: str, tags: List[str]) -> str:
        """Adiciona metadados e informações extras ao conteúdo"""
        # Adicionar cabeçalho com informações do repositório
        header = f"""---
*Documento sincronizado automaticamente do repositório [{self.github_repo}](https://github.com/{self.github_repo})*
*Última atualização: commit {self.github_sha[:8]}*
*Arquivo original: `{file_path}`*

---

"""
        
        # Adicionar rodapé com tags
        footer = f"""

---

**Tags:** {', '.join([f'`{tag}`' for tag in tags])}
**Fonte:** [{self.github_repo}](https://github.com/{self.github_repo}/blob/main/{file_path})
"""
        
        return header + content + footer
    
    def _ensure_collections_exist(self):
        """Garante que todas as coleções necessárias existam"""
        # Primeiro, verificar se a coleção pai existe
        parent_collection_id = self.mapping_config['config']['default_collection_id']
        if not self._verify_collection_exists(parent_collection_id):
            print(f"❌ Coleção pai '{parent_collection_id}' não encontrada. Verifique se ela existe no Outline.")
            return False
        
        # Depois, criar as sub-coleções
        collections = self.mapping_config.get('collections', {})
        
        for collection_id, collection_info in collections.items():
            name = collection_info.get('name', collection_id)
            description = collection_info.get('description', '')
            color = collection_info.get('color', '#3B82F6')
            
            self._create_collection(collection_id, name, description, color)
        
        return True
    
    def _verify_collection_exists(self, collection_id: str) -> bool:
        """Verifica se a coleção existe no Outline"""
        try:
            response = requests.get(f'{self.api_url}/collections.list', headers=self.headers)
            if response.status_code == 200:
                collections = response.json().get('data', [])
                for collection in collections:
                    if collection.get('id') == collection_id:
                        print(f"✅ Coleção '{collection_id}' encontrada")
                        return True
                print(f"❌ Coleção '{collection_id}' não encontrada")
                return False
            else:
                print(f"❌ Erro ao verificar coleções: {response.text}")
                return False
        except Exception as e:
            print(f"❌ Erro ao verificar coleção '{collection_id}': {e}")
            return False
    
    def sync_documents(self):
        """Sincroniza todos os documentos do diretório docs/"""
        print("🚀 Iniciando sincronização com Outline...")
        
        # Garantir que as coleções existam
        if not self._ensure_collections_exist():
            print("❌ Falha na verificação/criação de coleções. Abortando sincronização.")
            return False
        
        docs_dir = Path('docs')
        if not docs_dir.exists():
            print("❌ Diretório 'docs' não encontrado")
            return False
        
        success_count = 0
        error_count = 0
        
        # Processar todos os arquivos .md
        for md_file in docs_dir.rglob('*.md'):
            file_path = str(md_file.relative_to(Path.cwd()))
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if self._create_or_update_document(file_path, content):
                    success_count += 1
                else:
                    error_count += 1
                    
            except Exception as e:
                print(f"❌ Erro ao ler arquivo '{file_path}': {e}")
                error_count += 1
        
        print(f"\n📊 Resumo da sincronização:")
        print(f"✅ Documentos sincronizados com sucesso: {success_count}")
        print(f"❌ Documentos com erro: {error_count}")
        
        return error_count == 0

def main():
    """Função principal"""
    try:
        syncer = OutlineSync()
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
