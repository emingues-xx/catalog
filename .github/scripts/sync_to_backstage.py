#!/usr/bin/env python3
"""
Script para sincronizar documentação com Backstage TechDocs
"""

import os
import yaml
import requests
import json
from pathlib import Path
from typing import Dict, List, Optional

class BackstageTechDocsSync:
    def __init__(self, backstage_url: str, token: str):
        self.backstage_url = backstage_url.rstrip('/')
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
    
    def get_components(self) -> List[Dict]:
        """Obtém todos os componentes do Backstage"""
        try:
            response = requests.get(
                f'{self.backstage_url}/api/catalog/entities',
                headers=self.headers,
                params={'filter': 'kind=component'}
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Erro ao obter componentes: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Erro ao conectar com Backstage: {e}")
            return []
    
    def get_component_docs(self, component_name: str) -> List[Dict]:
        """Obtém documentação de um componente específico"""
        try:
            response = requests.get(
                f'{self.backstage_url}/api/techdocs/entity/{component_name}/docs',
                headers=self.headers
            )
            if response.status_code == 200:
                return response.json()
            else:
                return []
        except Exception as e:
            print(f"❌ Erro ao obter docs do componente {component_name}: {e}")
            return []
    
    def create_techdocs_entity(self, component_name: str, docs_path: str) -> bool:
        """Cria entidade TechDocs para um componente"""
        try:
            # Ler o arquivo de documentação
            docs_file = Path(docs_path) / "index.md"
            if not docs_file.exists():
                print(f"❌ Arquivo de documentação não encontrado: {docs_file}")
                return False
            
            # Criar entidade TechDocs
            entity_data = {
                'apiVersion': 'backstage.io/v1alpha1',
                'kind': 'Component',
                'metadata': {
                    'name': component_name,
                    'annotations': {
                        'backstage.io/techdocs-ref': f'dir:./{docs_path}'
                    }
                },
                'spec': {
                    'type': 'service',
                    'lifecycle': 'production',
                    'owner': 'platform-team'
                }
            }
            
            response = requests.post(
                f'{self.backstage_url}/api/catalog/entities',
                headers=self.headers,
                json=entity_data
            )
            
            if response.status_code in [200, 201]:
                print(f"✅ Entidade TechDocs criada para {component_name}")
                return True
            else:
                print(f"❌ Erro ao criar entidade TechDocs para {component_name}: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Erro ao criar entidade TechDocs para {component_name}: {e}")
            return False
    
    def sync_component_docs(self, component_name: str, docs_path: str) -> bool:
        """Sincroniza documentação de um componente"""
        try:
            # Verificar se o componente já existe
            components = self.get_components()
            existing_component = None
            
            for comp in components:
                if comp.get('metadata', {}).get('name') == component_name:
                    existing_component = comp
                    break
            
            if existing_component:
                print(f"📋 Componente {component_name} já existe no Backstage")
                # Verificar se tem documentação
                docs = self.get_component_docs(component_name)
                if docs:
                    print(f"✅ Componente {component_name} já tem documentação")
                    return True
                else:
                    print(f"⚠️ Componente {component_name} existe mas não tem documentação")
            else:
                print(f"📝 Criando componente {component_name} no Backstage")
            
            # Criar/atualizar entidade TechDocs
            return self.create_techdocs_entity(component_name, docs_path)
            
        except Exception as e:
            print(f"❌ Erro ao sincronizar componente {component_name}: {e}")
            return False
    
    def sync_all_components(self, docs_dir: str = "docs/components") -> Dict[str, bool]:
        """Sincroniza todos os componentes com documentação"""
        results = {}
        
        print("🚀 Iniciando sincronização com Backstage TechDocs...")
        print("=" * 60)
        
        # Verificar se o diretório existe
        if not os.path.exists(docs_dir):
            print(f"❌ Diretório de documentação não encontrado: {docs_dir}")
            return results
        
        # Listar todos os componentes com documentação
        for item in os.listdir(docs_dir):
            component_path = os.path.join(docs_dir, item)
            if os.path.isdir(component_path) and item != "index.md":
                # Verificar se tem documentação
                index_file = os.path.join(component_path, "index.md")
                if os.path.exists(index_file):
                    print(f"📁 Processando componente: {item}")
                    success = self.sync_component_docs(item, component_path)
                    results[item] = success
                else:
                    print(f"⚠️ Componente {item} não tem documentação (index.md)")
                    results[item] = False
        
        print("\n" + "=" * 60)
        print("📊 RESUMO DA SINCRONIZAÇÃO:")
        print("=" * 60)
        
        successful = sum(1 for success in results.values() if success)
        total = len(results)
        
        print(f"✅ Componentes sincronizados com sucesso: {successful}/{total}")
        
        for component, success in results.items():
            status = "✅" if success else "❌"
            print(f"   {status} {component}")
        
        if successful == total:
            print("\n🎉 Todos os componentes foram sincronizados com sucesso!")
        else:
            print(f"\n⚠️ {total - successful} componentes tiveram problemas na sincronização.")
        
        return results

def main():
    # Configurações do Backstage
    BACKSTAGE_URL = os.getenv('BACKSTAGE_URL', 'http://localhost:7007')
    BACKSTAGE_TOKEN = os.getenv('BACKSTAGE_TOKEN', '')
    
    if not BACKSTAGE_TOKEN:
        print("❌ BACKSTAGE_TOKEN não configurado")
        print("Configure a variável de ambiente BACKSTAGE_TOKEN")
        return
    
    # Inicializar sincronizador
    sync = BackstageTechDocsSync(BACKSTAGE_URL, BACKSTAGE_TOKEN)
    
    # Sincronizar todos os componentes
    results = sync.sync_all_components()
    
    # Salvar resultados
    with open('backstage-sync-results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Resultados salvos em: backstage-sync-results.json")

if __name__ == "__main__":
    main()
