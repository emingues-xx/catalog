#!/usr/bin/env python3
"""
Script para testar conectividade com a API do Outline
"""

import os
import requests
import json

def test_outline_connectivity():
    """Testa a conectividade com a API do Outline"""
    
    # Configurações
    api_url = os.getenv('OUTLINE_API_URL', 'https://outline-production-cebc.up.railway.app')
    api_token = os.getenv('OUTLINE_API_TOKEN', 'ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A')
    
    print("🔍 Testando conectividade com Outline...")
    print(f"📡 URL: {api_url}")
    print(f"🔑 Token: {api_token[:20]}...")
    print()
    
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    # Teste 1: Verificar se a API está acessível
    print("1️⃣ Testando acesso à API...")
    try:
        response = requests.get(f"{api_url}/api/auth.info", headers=headers, timeout=10)
        if response.status_code == 200:
            print("✅ API acessível - Status 200")
            auth_info = response.json()
            print(f"   👤 Usuário: {auth_info.get('data', {}).get('user', {}).get('name', 'N/A')}")
        else:
            print(f"❌ Erro na API - Status: {response.status_code}")
            print(f"   📄 Resposta: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return False
    
    # Teste 2: Listar coleções
    print("\n2️⃣ Testando listagem de coleções...")
    try:
        response = requests.get(f"{api_url}/api/collections.list", headers=headers, timeout=10)
        if response.status_code == 200:
            collections = response.json()
            print("✅ Coleções listadas com sucesso")
            print(f"   📁 Total de coleções: {len(collections.get('data', []))}")
            
            for collection in collections.get('data', []):
                print(f"   📂 {collection.get('name', 'N/A')} (ID: {collection.get('id', 'N/A')})")
        else:
            print(f"❌ Erro ao listar coleções - Status: {response.status_code}")
            print(f"   📄 Resposta: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return False
    
    # Teste 3: Listar documentos
    print("\n3️⃣ Testando listagem de documentos...")
    try:
        response = requests.get(f"{api_url}/api/documents.list", headers=headers, timeout=10)
        if response.status_code == 200:
            documents = response.json()
            print("✅ Documentos listados com sucesso")
            print(f"   📄 Total de documentos: {len(documents.get('data', []))}")
            
            for doc in documents.get('data', [])[:5]:  # Mostrar apenas os primeiros 5
                print(f"   📝 {doc.get('title', 'N/A')} (ID: {doc.get('id', 'N/A')})")
            
            if len(documents.get('data', [])) > 5:
                print(f"   ... e mais {len(documents.get('data', [])) - 5} documentos")
        else:
            print(f"❌ Erro ao listar documentos - Status: {response.status_code}")
            print(f"   📄 Resposta: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return False
    
    print("\n🎉 Todos os testes passaram! A configuração está correta.")
    return True

if __name__ == "__main__":
    success = test_outline_connectivity()
    if not success:
        print("\n❌ Alguns testes falharam. Verifique a configuração.")
        exit(1)
