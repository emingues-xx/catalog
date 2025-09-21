# Estrutura Hierárquica do Outline

## 📁 Organização das Coleções

```
docs-KS6TJUuX5p (Coleção Pai)
├── main-collection (Documentação Principal)
│   └── docs/index.md
├── architecture-collection (Arquitetura)
│   ├── docs/architecture/overview.md
│   └── docs/architecture/adrs/index.md
├── systems-collection (Sistemas)
│   ├── docs/systems/vitrine-veiculos/index.md
│   ├── docs/systems/vitrine-veiculos/arquitetura.md
│   ├── docs/systems/vitrine-veiculos/feature-busca-veiculos.md
│   ├── docs/systems/backoffice-veiculos/index.md
│   ├── docs/systems/backoffice-veiculos/arquitetura.md
│   └── docs/systems/backoffice-veiculos/feature-cadastro-anuncio.md
├── components-collection (Componentes)
│   ├── docs/components/vitrine-veiculos-web/index.md
│   ├── docs/components/vitrine-veiculos-web/architecture.md
│   ├── docs/components/vitrine-veiculos-web/setup.md
│   ├── docs/components/vitrine-veiculos-api/index.md
│   ├── docs/components/vitrine-veiculos-api/api.md
│   ├── docs/components/vitrine-veiculos-bff/index.md
│   ├── docs/components/backoffice-veiculos-web/index.md
│   ├── docs/components/backoffice-veiculos-api/index.md
│   ├── docs/components/backoffice-veiculos-bff/index.md
│   ├── docs/components/ecommerce-veiculos-pipelines/index.md
│   ├── docs/components/ecommerce-veiculos-pipelines/automation.md
│   └── docs/components/ecommerce-veiculos-pipelines/workflows.md
└── guides-collection (Guias)
    └── docs/guides/contributing.md
```

## 🎯 Mapeamento de Documentos

### Documentação Principal
- **Coleção**: `main-collection`
- **Documentos**: 1
- **Tags**: overview, main

### Arquitetura
- **Coleção**: `architecture-collection`
- **Documentos**: 2
- **Tags**: architecture, overview, adr, decisions

### Sistemas
- **Coleção**: `systems-collection`
- **Documentos**: 6
- **Tags**: system, vitrine, backoffice, frontend, admin, architecture, feature, search, ads

### Componentes
- **Coleção**: `components-collection`
- **Documentos**: 12
- **Tags**: component, vitrine, backoffice, web, frontend, api, backend, bff, admin, architecture, setup, reference, pipelines, ci-cd, automation, workflows

### Guias
- **Coleção**: `guides-collection`
- **Documentos**: 1
- **Tags**: guide, contributing, development

## 🔄 Processo de Sincronização

1. **Verificação da Coleção Pai**: Confirma se `docs-KS6TJUuX5p` existe
2. **Criação de Sub-coleções**: Cria as 5 sub-coleções dentro da coleção pai
3. **Sincronização de Documentos**: Para cada arquivo `.md`:
   - Aplica mapeamento específico
   - Cria/atualiza na coleção correspondente
   - Adiciona metadados e tags

## 📋 Configuração Atual

- **Coleção Pai**: `docs-KS6TJUuX5p`
- **Sub-coleções**: 5 (main, architecture, systems, components, guides)
- **Total de Documentos**: 22
- **Estrutura**: Hierárquica com organização por categoria
