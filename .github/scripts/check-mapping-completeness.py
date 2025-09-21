#!/usr/bin/env python3
"""
Script para verificar se todos os arquivos .md do diretório docs/ estão mapeados no outline-mapping.yaml
"""

import os
import yaml
from pathlib import Path

def get_all_md_files(docs_dir):
    """Obtém todos os arquivos .md do diretório docs/"""
    md_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                # Converter para caminho relativo ao diretório docs
                rel_path = os.path.relpath(full_path, docs_dir)
                md_files.append(rel_path)
    return sorted(md_files)

def load_mapping_config():
    """Carrega o arquivo outline-mapping.yaml"""
    try:
        with open('outline-mapping.yaml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Erro ao carregar outline-mapping.yaml: {e}")
        return None

def main():
    print("🔍 Verificando completude do mapeamento...")
    
    # Obter todos os arquivos .md
    docs_dir = "docs"
    if not os.path.exists(docs_dir):
        print(f"❌ Diretório '{docs_dir}' não encontrado")
        return
    
    md_files = get_all_md_files(docs_dir)
    print(f"📄 Encontrados {len(md_files)} arquivos .md:")
    for file in md_files:
        print(f"  - {file}")
    
    # Carregar configuração de mapeamento
    config = load_mapping_config()
    if not config:
        return
    
    # Obter arquivos mapeados
    mapped_files = set(config.get('documents', {}).keys())
    print(f"\n📋 Encontrados {len(mapped_files)} arquivos mapeados:")
    for file in sorted(mapped_files):
        print(f"  - {file}")
    
    # Verificar diferenças
    md_files_set = set(md_files)
    
    missing_in_mapping = md_files_set - mapped_files
    extra_in_mapping = mapped_files - md_files_set
    
    print(f"\n📊 Resultado da verificação:")
    
    if missing_in_mapping:
        print(f"❌ {len(missing_in_mapping)} arquivos .md NÃO estão mapeados:")
        for file in sorted(missing_in_mapping):
            print(f"  - {file}")
    else:
        print("✅ Todos os arquivos .md estão mapeados")
    
    if extra_in_mapping:
        print(f"⚠️ {len(extra_in_mapping)} entradas no mapeamento NÃO correspondem a arquivos .md:")
        for file in sorted(extra_in_mapping):
            print(f"  - {file}")
    else:
        print("✅ Todas as entradas do mapeamento correspondem a arquivos .md")
    
    # Verificar duplicatas no mapeamento
    mapping_keys = list(config.get('documents', {}).keys())
    duplicates = [key for key in mapping_keys if mapping_keys.count(key) > 1]
    if duplicates:
        print(f"⚠️ {len(set(duplicates))} chaves duplicadas no mapeamento:")
        for key in set(duplicates):
            print(f"  - {key}")
    else:
        print("✅ Nenhuma chave duplicada no mapeamento")

if __name__ == "__main__":
    main()
