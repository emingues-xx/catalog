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
                'default_collection_id': '5c78f84a-f721-47cc-a983-2eb05e6bf246',  # Coleção "Docs"
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

    def _get_document_info(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """Obtém informações de um documento pelo ID"""
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
                    if doc.get('id') == doc_id:
                        return doc
            
            return None
        except Exception as e:
            print(f"❌ Erro ao obter informações do documento '{doc_id}': {e}")
            return None

    def _create_parent_document(self, title: str, collection_id: str) -> Optional[str]:
        """Cria um documento pai vazio quando necessário"""
        try:
            # Conteúdo vazio para documento pai
            empty_content = f"# {title}\n\n*Documento pai criado automaticamente*"
            
            data = {
                'title': title,
                'text': empty_content,
                'publish': True,
                'collectionId': collection_id
            }
            
            response = requests.post(f'{self.api_url}/api/documents.create', headers=self.headers, json=data)
            
            if response.status_code in [200, 201]:
                doc_id = response.json().get('data', {}).get('id')
                print(f"✅ Documento pai '{title}' criado com sucesso (ID: {doc_id})")
                
                # Tornar readonly
                try:
                    readonly_data = {
                        'id': doc_id,
                        'readonly': True
                    }
                    readonly_response = requests.post(f'{self.api_url}/api/documents.update', headers=self.headers, json=readonly_data)
                    if readonly_response.status_code in [200, 201]:
                        print(f"✅ Documento pai '{title}' configurado como readonly")
                except Exception as e:
                    print(f"⚠️ Erro ao configurar readonly para '{title}': {e}")
                
                return doc_id
            else:
                print(f"❌ Erro ao criar documento pai '{title}': {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Erro ao criar documento pai '{title}': {e}")
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
                    print(f"⚠️ Documento pai '{parent_document_title}' não encontrado. Criando documento pai vazio.")
                    parent_document_id = self._create_parent_document(parent_document_title, collection_id)
            
            if doc_id:
                # Verificar se o documento está na coleção correta
                doc_info = self._get_document_info(doc_id)
                if doc_info and doc_info.get('collectionId') != collection_id:
                    print(f"🔄 Migrando documento '{title}' para nova coleção")
                    # Forçar migração para nova coleção
                    data = {
                        'id': doc_id,
                        'text': enhanced_content,
                        'readonly': True,
                        'collectionId': collection_id
                    }
                    
                    # Adicionar parentId se especificado
                    if parent_document_id:
                        data['parentDocumentId'] = parent_document_id
                        print(f"👨‍👩‍👧‍👦 Associando ao pai: {parent_document_title}")
                    
                    response = requests.post(f'{self.api_url}/api/documents.update', headers=self.headers, json=data)
                    
                    if response.status_code in [200, 201]:
                        print(f"✅ Documento '{title}' migrado para nova coleção com sucesso")
                        return True
                    else:
                        print(f"❌ Erro ao migrar documento '{title}': {response.status_code} - {response.text}")
                        return False
                else:
                    # Atualizar documento existente na coleção correta
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
    
    def _delete_all_documents_hierarchically(self) -> bool:
        """Deleta todos os documentos em ordem hierárquica (do maior nível para o menor)"""
        try:
            print("🗑️ Iniciando limpeza hierárquica de documentos...")
            
            # Listar todos os documentos
            test_data = {"id": ""}
            response = requests.post(
                f'{self.api_url}/api/documents.list',
                headers=self.headers,
                json=test_data,
                timeout=10
            )
            
            if response.status_code != 200:
                print(f"❌ Erro ao listar documentos: {response.status_code}")
                return False
            
            data = response.json()
            all_documents = data.get('data', [])
            
            if not all_documents:
                print("✅ Nenhum documento encontrado para deletar")
                return True
            
            print(f"📄 Encontrados {len(all_documents)} documentos para deletar")
            
            # Organizar documentos por nível hierárquico
            documents_by_level = {}
            for doc in all_documents:
                title = doc.get('title', '')
                level = self._get_document_level_by_title(title)
                
                if level not in documents_by_level:
                    documents_by_level[level] = []
                documents_by_level[level].append(doc)
            
            print(f"📊 Documentos organizados por nível para deleção:")
            for level in sorted(documents_by_level.keys(), reverse=True):
                print(f"  Nível {level}: {len(documents_by_level[level])} documentos")
            
            deleted_count = 0
            
            # Deletar por níveis (do maior para o menor)
            for level in sorted(documents_by_level.keys(), reverse=True):
                print(f"\n🗑️ Deletando Nível {level} ({len(documents_by_level[level])} documentos)...")
                
                for doc in documents_by_level[level]:
                    doc_id = doc.get('id')
                    doc_title = doc.get('title', 'Sem título')
                    
                    delete_data = {
                        'id': doc_id,
                        'permanent': True
                    }
                    
                    try:
                        delete_response = requests.post(
                            f'{self.api_url}/api/documents.delete',
                            headers=self.headers,
                            json=delete_data,
                            timeout=10
                        )
                        
                        if delete_response.status_code in [200, 201]:
                            print(f"✅ Deletado: {doc_title} (Nível {level})")
                            deleted_count += 1
                        else:
                            print(f"❌ Erro ao deletar {doc_title}: {delete_response.status_code} - {delete_response.text}")
                            
                    except Exception as e:
                        print(f"❌ Erro ao deletar {doc_title}: {e}")
            
            print(f"\n📊 Limpeza hierárquica concluída: {deleted_count} documentos deletados")
            return True
            
        except Exception as e:
            print(f"❌ Erro na limpeza hierárquica: {e}")
            return False

    def _get_document_level_by_title(self, title: str) -> int:
        """Determina o nível hierárquico do documento baseado no título"""
        # Nível 0: Documento raiz
        if title == "E-commerce de Veículos - Documentação":
            return 0
        
        # Nível 1: Documentos principais
        if title in ["Sistemas", "Componentes", "Arquitetura", "Guias"]:
            return 1
        
        # Nível 2: Sistemas e componentes específicos
        if title in ["Vitrine de Veículos", "Backoffice de Veículos", "Vitrine Web", "Vitrine API", 
                    "Vitrine BFF", "Backoffice Web", "Backoffice API", "Backoffice BFF", 
                    "Pipelines E-commerce", "Sobre ADRs", "ADRs", "Guia de Contribuição", "Contributing"]:
            return 2
        
        # Nível 3: Features, Arquitetura, Setup, etc.
        if title in ["Features", "Arquitetura", "Setup", "API Reference", "API", "Architecture",
                    "Automação - Pipelines", "Workflows - Pipelines"]:
            return 3
        
        # Nível 4: Funcionalidades específicas
        if title in ["Busca de Veículos", "Cadastro de Anúncios"]:
            return 4
        
        # Default: nível 2
        return 2

    def _get_document_level(self, file_path: str) -> int:
        """Determina o nível hierárquico do documento baseado no caminho"""
        path_parts = file_path.split('/')
        
        # docs/index.md = nível 0 (raiz)
        if file_path == "docs/index.md":
            return 0
        
        # docs/systems/index.md, docs/components/index.md, etc. = nível 1
        if len(path_parts) == 3 and path_parts[2] == "index.md":
            return 1
        
        # docs/systems/vitrine-veiculos/index.md = nível 2
        if len(path_parts) == 4 and path_parts[3] == "index.md":
            return 2
        
        # docs/systems/vitrine-veiculos/features.md, arquitetura.md = nível 3
        if len(path_parts) == 4 and path_parts[3] in ["features.md", "arquitetura.md", "setup.md", "api-reference.md", "automation.md", "workflows.md"]:
            return 3
        
        # docs/systems/vitrine-veiculos/feature-busca-veiculos.md = nível 4
        if len(path_parts) == 4 and path_parts[3].startswith("feature-"):
            return 4
        
        # docs/components/vitrine-veiculos-web/arquitetura.md, setup.md = nível 3
        if len(path_parts) == 5 and path_parts[4] in ["arquitetura.md", "setup.md", "api-reference.md", "automation.md", "workflows.md"]:
            return 3
        
        # docs/architecture/overview.md = nível 1
        if file_path == "docs/architecture/overview.md":
            return 1
        
        # docs/architecture/sobre-adrs.md, docs/architecture/adrs/index.md = nível 2
        if path_parts[1] == "architecture" and len(path_parts) >= 3:
            return 2
        
        # docs/guides/index.md = nível 1
        if file_path == "docs/guides/index.md":
            return 1
        
        # docs/guides/contributing.md, docs/guides/guia-contribuicao.md = nível 2
        if path_parts[1] == "guides" and len(path_parts) == 3:
            return 2
        
        # Default: nível 2
        return 2

    def sync_documents(self):
        """Sincroniza todos os documentos do diretório docs/ respeitando a hierarquia"""
        print("🚀 Iniciando sincronização hierárquica com Outline...")
        
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
        
        # Processar todos os arquivos .md
        md_files = list(docs_dir.rglob('*.md'))
        print(f"📄 Encontrados {len(md_files)} arquivos .md para processar")
        
        # Organizar arquivos por nível hierárquico
        files_by_level = {}
        for md_file in md_files:
            file_path = str(md_file.relative_to(docs_dir.parent))
            level = self._get_document_level(file_path)
            
            if level not in files_by_level:
                files_by_level[level] = []
            files_by_level[level].append((file_path, md_file))
        
        print(f"📊 Documentos organizados por nível:")
        for level in sorted(files_by_level.keys()):
            print(f"  Nível {level}: {len(files_by_level[level])} documentos")
        
        success_count = 0
        error_count = 0
        
        # Processar por níveis (do menor para o maior)
        for level in sorted(files_by_level.keys()):
            print(f"\n🔄 Processando Nível {level} ({len(files_by_level[level])} documentos)...")
            
            for file_path, md_file in files_by_level[level]:
                try:
                    print(f"📝 Processando: {file_path} (Nível {level})")
                    
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if self._create_or_update_document(file_path, content):
                        success_count += 1
                    else:
                        error_count += 1
                        
                except Exception as e:
                    print(f"❌ Erro ao processar arquivo '{file_path}': {e}")
                    error_count += 1
        
        print(f"\n📊 Resumo da sincronização hierárquica:")
        print(f"✅ Documentos sincronizados com sucesso: {success_count}")
        print(f"❌ Documentos com erro: {error_count}")
        
        return error_count == 0

def main():
    """Função principal"""
    try:
        syncer = OutlineSyncWorking()
        
        # Verificar se deve limpar antes da sincronização
        clean_before_sync = os.getenv('CLEAN_BEFORE_SYNC', 'false').lower() == 'true'
        
        if clean_before_sync:
            print("🧹 Modo de limpeza ativado. Deletando documentos existentes...")
            if not syncer._delete_all_documents_hierarchically():
                print("⚠️ Erro na limpeza, mas continuando com a sincronização...")
        
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
