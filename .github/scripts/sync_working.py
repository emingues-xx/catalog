#!/usr/bin/env python3
"""
Script de sincronização para Outline
Sincroniza documentos locais com Outline seguindo hierarquia definida no mapping
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
        self.api_url = os.getenv('OUTLINE_API_URL', 'https://outline-production-cebc.up.railway.app')
        self.api_token = os.getenv('OUTLINE_API_TOKEN', 'ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A')
        
        if not self.api_token:
            raise ValueError("OUTLINE_API_TOKEN deve estar definido")
        
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Carregar configuração de mapeamento
        self.mapping_config = self._load_mapping_config()
        
        # Cache para armazenar IDs do Outline para cada ID do mapeamento
        self.mapping_id_to_outline_id = {}
        
    def _load_mapping_config(self) -> Dict[str, Any]:
        """Carrega a configuração de mapeamento do arquivo YAML"""
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
            raise FileNotFoundError("Arquivo outline-mapping.yaml não encontrado")
        
        print(f"📄 Carregando mapeamento de: {mapping_file}")
        
        with open(mapping_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def _test_api_connection(self) -> bool:
        """Testa a conexão com a API"""
        try:
            print("🔗 Testando conexão com Outline API...")
            
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
                    default_collection_id = self.mapping_config.get('default_collection_id')
                    collection_exists = any(c['id'] == default_collection_id for c in collections)
                    if collection_exists:
                        print(f"✅ Coleção padrão encontrada: {default_collection_id}")
                    else:
                        print(f"⚠️  Coleção padrão não encontrada: {default_collection_id}")
                    
                    return True
                else:
                    print(f"❌ Erro ao acessar coleções: {collections_response.status_code}")
                    return False
            else:
                print(f"❌ Erro na conexão: {response.status_code}")
                print(f"Resposta: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao testar conexão: {e}")
            return False
    
    def _get_document_by_mapping_id(self, mapping_id: str) -> Optional[Dict]:
        """Busca um documento no Outline pelo ID do mapeamento"""
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
                
                # Buscar pelo ID do mapeamento no cache
                if mapping_id in self.mapping_id_to_outline_id:
                    outline_id = self.mapping_id_to_outline_id[mapping_id]
                    for doc in documents:
                        if doc['id'] == outline_id:
                            return doc
                
                return None
            else:
                print(f"❌ Erro ao buscar documentos: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Erro ao buscar documento {mapping_id}: {e}")
            return None
    
    def _get_document_parent_id(self, mapping_id: str) -> Optional[str]:
        """Obtém o ID do documento pai no Outline"""
        doc_config = self._get_document_config(mapping_id)
        if not doc_config or not doc_config.get('parent_id'):
            return None
        
        parent_mapping_id = doc_config['parent_id']
        
        # Se o pai já foi criado, retornar seu ID do Outline
        if parent_mapping_id in self.mapping_id_to_outline_id:
            return self.mapping_id_to_outline_id[parent_mapping_id]
        
        return None
    
    def _get_document_config(self, mapping_id: str) -> Optional[Dict]:
        """Obtém a configuração de um documento pelo ID do mapeamento"""
        for doc in self.mapping_config.get('documents', []):
            if doc.get('id') == mapping_id:
                return doc
        return None
    
    def _read_file_content(self, file_path: str) -> str:
        """Lê o conteúdo de um arquivo"""
        try:
            # Tentar diferentes caminhos
            possible_paths = [
                Path(file_path),
                Path.cwd() / file_path,
                Path(__file__).parent.parent.parent / file_path
            ]
            
            for path in possible_paths:
                if path.exists():
                    with open(path, 'r', encoding='utf-8') as f:
                        return f.read()
            
            print(f"⚠️  Arquivo não encontrado: {file_path}")
            return f"# Documento não encontrado\n\nArquivo: {file_path}\n\nEste arquivo não foi encontrado no sistema de arquivos."
            
        except Exception as e:
            print(f"❌ Erro ao ler arquivo {file_path}: {e}")
            return f"# Erro ao carregar documento\n\nErro: {e}\n\nArquivo: {file_path}"
    
    def _create_document(self, doc_config: Dict) -> Optional[str]:
        """Cria um novo documento no Outline"""
        try:
            mapping_id = doc_config['id']
            title = doc_config['title']
            file_path = doc_config['file_path']
            collection_id = doc_config.get('collection_id', self.mapping_config.get('default_collection_id'))
            parent_id = self._get_document_parent_id(mapping_id)
            
            print(f"📝 Criando documento: {mapping_id} - {title}")
            if parent_id:
                print(f"   📁 Pai: {parent_id}")
            
            # Ler conteúdo do arquivo
            content = self._read_file_content(file_path)
            
            # Preparar dados para criação
            data = {
                'title': title,
                'text': content,
                'collectionId': collection_id,
                'publish': True
            }
            
            if parent_id:
                data['parentDocumentId'] = parent_id
            
            # Criar documento
            response = requests.post(
                f'{self.api_url}/api/documents.create',
                headers=self.headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                outline_id = result['data']['id']
                
                # Armazenar no cache
                self.mapping_id_to_outline_id[mapping_id] = outline_id
                
                print(f"✅ Documento criado: {title} (ID: {outline_id})")
                return outline_id
            else:
                print(f"❌ Erro ao criar documento {title}: {response.status_code}")
                print(f"Resposta: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Erro ao criar documento {doc_config.get('id', 'unknown')}: {e}")
            return None
    
    def _update_document(self, doc_config: Dict, outline_doc: Dict) -> bool:
        """Atualiza um documento existente no Outline"""
        try:
            mapping_id = doc_config['id']
            title = doc_config['title']
            file_path = doc_config['file_path']
            outline_id = outline_doc['id']
            
            print(f"🔄 Atualizando documento: {mapping_id} - {title}")
            
            # Ler conteúdo do arquivo
            content = self._read_file_content(file_path)
            
            # Preparar dados para atualização
            data = {
                'id': outline_id,
                'title': title,
                'text': content,
                'append': False
            }
            
            # Atualizar documento
            response = requests.post(
                f'{self.api_url}/api/documents.update',
                headers=self.headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                print(f"✅ Documento atualizado: {title}")
                return True
            else:
                print(f"❌ Erro ao atualizar documento {title}: {response.status_code}")
                print(f"Resposta: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao atualizar documento {doc_config.get('id', 'unknown')}: {e}")
            return False
    
    def _sync_document(self, doc_config: Dict) -> bool:
        """Sincroniza um documento individual"""
        mapping_id = doc_config['id']
        title = doc_config['title']
        
        # Verificar se o documento já existe
        existing_doc = self._get_document_by_mapping_id(mapping_id)
        
        if existing_doc:
            # Documento existe, atualizar
            return self._update_document(doc_config, existing_doc)
        else:
            # Documento não existe, criar
            outline_id = self._create_document(doc_config)
            return outline_id is not None
    
    def _get_documents_by_level(self, level: int) -> List[Dict]:
        """Obtém todos os documentos de um nível específico"""
        return [doc for doc in self.mapping_config.get('documents', []) if doc.get('level') == level]
    
    def _get_max_level(self) -> int:
        """Obtém o nível máximo dos documentos"""
        max_level = 0
        for doc in self.mapping_config.get('documents', []):
            level = doc.get('level', 0)
            if level > max_level:
                max_level = level
        return max_level
    
    def sync_all_documents(self) -> bool:
        """Sincroniza todos os documentos seguindo a hierarquia"""
        print("🚀 Iniciando sincronização de documentos...")
        
        # Testar conexão primeiro
        if not self._test_api_connection():
            print("❌ Falha na conexão com a API. Abortando sincronização.")
            return False
        
        print("\n📊 Estatísticas do mapeamento:")
        total_docs = len(self.mapping_config.get('documents', []))
        print(f"   Total de documentos: {total_docs}")
        
        max_level = self._get_max_level()
        print(f"   Níveis: 0 a {max_level}")
        
        # Sincronizar por níveis (do menor para o maior)
        success_count = 0
        error_count = 0
        
        for level in range(max_level + 1):
            level_docs = self._get_documents_by_level(level)
            if not level_docs:
                continue
            
            print(f"\n📁 Processando nível {level} ({len(level_docs)} documentos):")
            
            for doc_config in level_docs:
                mapping_id = doc_config['id']
                title = doc_config['title']
                
                print(f"   🔄 {mapping_id}: {title}")
                
                if self._sync_document(doc_config):
                    success_count += 1
                else:
                    error_count += 1
        
        print(f"\n📈 Resumo da sincronização:")
        print(f"   ✅ Sucessos: {success_count}")
        print(f"   ❌ Erros: {error_count}")
        print(f"   📊 Total: {success_count + error_count}")
        
        return error_count == 0

def main():
    """Função principal"""
    try:
        print("🎯 Outline Sync - Sincronização de Documentos")
        print("=" * 50)
        
        sync = OutlineSync()
        success = sync.sync_all_documents()
        
        if success:
            print("\n🎉 Sincronização concluída com sucesso!")
            sys.exit(0)
        else:
            print("\n💥 Sincronização concluída com erros!")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n💥 Erro fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()