#!/usr/bin/env python3
"""
Script para testar os caminhos no ambiente do GitHub Actions
"""

import os
from pathlib import Path

def test_paths():
    print("🔍 Testando caminhos...")
    
    print(f"Current working directory: {Path.cwd()}")
    print(f"Script location: {Path(__file__).parent}")
    print(f"Repository root: {Path(__file__).parent.parent.parent}")
    
    # Testar diferentes caminhos para docs
    possible_docs_paths = [
        Path('docs'),
        Path.cwd() / 'docs',
        Path(__file__).parent.parent.parent / 'docs'
    ]
    
    print("\n📁 Testando caminhos para docs:")
    for path in possible_docs_paths:
        exists = path.exists()
        print(f"  {path}: {'✅' if exists else '❌'}")
        if exists:
            md_files = list(path.rglob('*.md'))
            print(f"    Arquivos .md encontrados: {len(md_files)}")
            for md_file in md_files[:3]:  # Mostrar apenas os primeiros 3
                try:
                    relative_path = str(md_file.relative_to(path.parent))
                    print(f"    - {relative_path}")
                except Exception as e:
                    print(f"    - {md_file} (erro: {e})")
    
    # Testar diferentes caminhos para outline-mapping.yaml
    possible_mapping_paths = [
        Path('outline-mapping.yaml'),
        Path.cwd() / 'outline-mapping.yaml',
        Path(__file__).parent.parent.parent / 'outline-mapping.yaml'
    ]
    
    print("\n📄 Testando caminhos para outline-mapping.yaml:")
    for path in possible_mapping_paths:
        exists = path.exists()
        print(f"  {path}: {'✅' if exists else '❌'}")

if __name__ == '__main__':
    test_paths()
