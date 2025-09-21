# Estrutura Hierárquica do Outline

## 📁 Organização das Coleções

A documentação é organizada em uma estrutura hierárquica automática baseada no caminho dos arquivos, seguindo o padrão estabelecido:

```
Docs (Coleção Raiz)
├── Arquitetura
│   ├── docs/architecture/overview.md
│   └── docs/architecture/adrs/index.md
├── Sistemas
│   ├── Vitrine de Veículos
│   │   ├── docs/systems/vitrine-veiculos/index.md
│   │   ├── Arquitetura
│   │   │   └── docs/systems/vitrine-veiculos/arquitetura.md
│   │   └── Features
│   │       └── Busca de Veículos
│   │           └── docs/systems/vitrine-veiculos/feature-busca-veiculos.md
│   └── Backoffice de Veículos
│       ├── docs/systems/backoffice-veiculos/index.md
│       ├── Arquitetura
│       │   └── docs/systems/backoffice-veiculos/arquitetura.md
│       └── Features
│           └── Cadastro de Anúncios
│               └── docs/systems/backoffice-veiculos/feature-cadastro-anuncio.md
├── Componentes
│   ├── Vitrine Veículos Web
│   │   ├── docs/components/vitrine-veiculos-web/index.md
│   │   ├── Arquitetura
│   │   │   └── docs/components/vitrine-veiculos-web/architecture.md
│   │   └── Setup
│   │       └── docs/components/vitrine-veiculos-web/setup.md
│   ├── Vitrine Veículos Api
│   │   ├── docs/components/vitrine-veiculos-api/index.md
│   │   └── API
│   │       └── docs/components/vitrine-veiculos-api/api.md
│   └── Ecommerce Veículos Pipelines
│       ├── docs/components/ecommerce-veiculos-pipelines/index.md
│       ├── Automação
│       │   └── docs/components/ecommerce-veiculos-pipelines/automation.md
│       └── Workflows
│           └── docs/components/ecommerce-veiculos-pipelines/workflows.md
└── Guias
    └── Contribuindo
        └── docs/guides/contributing.md
```

## 🎯 Mapeamento Automático de Documentos

### Regras de Hierarquia

O sistema cria automaticamente a hierarquia baseada no caminho do arquivo, seguindo o padrão estabelecido:

- **`docs/index.md`** → Coleção: `Docs`
- **`docs/architecture/*`** → Coleção: `Docs >> Arquitetura`
- **`docs/systems/sistema-name/*`** → Coleção: `Docs >> Sistemas >> Sistema Name`
- **`docs/components/component-name/*`** → Coleção: `Docs >> Componentes >> Component Name`
- **`docs/guides/*`** → Coleção: `Docs >> Guias`

### Exemplos de Mapeamento

| Arquivo | Hierarquia | Coleção Final |
|---------|------------|---------------|
| `docs/index.md` | `Docs` | `Docs` |
| `docs/architecture/overview.md` | `Docs >> Arquitetura` | `Arquitetura` |
| `docs/systems/vitrine-veiculos/index.md` | `Docs >> Sistemas >> Vitrine de Veículos` | `Vitrine de Veículos` |
| `docs/systems/vitrine-veiculos/arquitetura.md` | `Docs >> Sistemas >> Vitrine de Veículos >> Arquitetura` | `Arquitetura` |
| `docs/systems/vitrine-veiculos/feature-busca-veiculos.md` | `Docs >> Sistemas >> Vitrine de Veículos >> Features >> Busca de Veículos` | `Busca de Veículos` |
| `docs/components/vitrine-veiculos-web/architecture.md` | `Docs >> Componentes >> Vitrine Veículos Web >> Arquitetura` | `Arquitetura` |
| `docs/guides/contributing.md` | `Docs >> Guias >> Contribuindo` | `Contribuindo` |

## 🔄 Processo de Sincronização

1. **Análise do Caminho**: Para cada arquivo `.md`, determina a hierarquia baseada no caminho
2. **Criação de Coleções**: Cria automaticamente a hierarquia de coleções necessária
3. **Sincronização de Documentos**: Para cada arquivo `.md`:
   - Determina a coleção final na hierarquia
   - Cria/atualiza o documento na coleção correta
   - Configura como público e readonly
   - Adiciona metadados e tags

## 📋 Configuração Atual

- **Coleção Raiz**: `docs` (criada automaticamente)
- **Hierarquia Automática**: Baseada no caminho dos arquivos
- **Total de Documentos**: 19
- **Estrutura**: Hierárquica automática com organização por categoria e sistema/componente
- **Características**: Documentos públicos e readonly
