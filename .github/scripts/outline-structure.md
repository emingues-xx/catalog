# Estrutura Hierárquica do Outline

## 📁 Organização das Coleções

A documentação é organizada em uma estrutura hierárquica automática baseada no caminho dos arquivos:

```
docs (Coleção Raiz)
├── Arquitetura
│   ├── docs/architecture/overview.md
│   └── docs/architecture/adrs/index.md
├── Sistemas
│   ├── Sistema Vitrine Veículos
│   │   ├── docs/systems/vitrine-veiculos/index.md
│   │   ├── docs/systems/vitrine-veiculos/arquitetura.md
│   │   └── docs/systems/vitrine-veiculos/feature-busca-veiculos.md
│   └── Sistema Backoffice Veículos
│       ├── docs/systems/backoffice-veiculos/index.md
│       ├── docs/systems/backoffice-veiculos/arquitetura.md
│       └── docs/systems/backoffice-veiculos/feature-cadastro-anuncio.md
├── Componentes
│   ├── Componente Vitrine Veículos Web
│   │   ├── docs/components/vitrine-veiculos-web/index.md
│   │   ├── docs/components/vitrine-veiculos-web/architecture.md
│   │   └── docs/components/vitrine-veiculos-web/setup.md
│   ├── Componente Vitrine Veículos Api
│   │   ├── docs/components/vitrine-veiculos-api/index.md
│   │   └── docs/components/vitrine-veiculos-api/api.md
│   ├── Componente Vitrine Veículos Bff
│   │   └── docs/components/vitrine-veiculos-bff/index.md
│   └── Componente Ecommerce Veículos Pipelines
│       ├── docs/components/ecommerce-veiculos-pipelines/index.md
│       ├── docs/components/ecommerce-veiculos-pipelines/automation.md
│       └── docs/components/ecommerce-veiculos-pipelines/workflows.md
└── Guias
    └── docs/guides/contributing.md
```

## 🎯 Mapeamento Automático de Documentos

### Regras de Hierarquia

O sistema cria automaticamente a hierarquia baseada no caminho do arquivo:

- **`docs/index.md`** → Coleção: `docs`
- **`docs/architecture/*`** → Coleção: `docs >> Arquitetura`
- **`docs/systems/sistema-name/*`** → Coleção: `docs >> Sistemas >> Sistema Sistema Name`
- **`docs/components/component-name/*`** → Coleção: `docs >> Componentes >> Componente Component Name`
- **`docs/guides/*`** → Coleção: `docs >> Guias`

### Exemplos de Mapeamento

| Arquivo | Hierarquia | Coleção Final |
|---------|------------|---------------|
| `docs/index.md` | `docs` | `docs` |
| `docs/architecture/overview.md` | `docs >> Arquitetura` | `Arquitetura` |
| `docs/systems/vitrine-veiculos/index.md` | `docs >> Sistemas >> Sistema Vitrine Veículos` | `Sistema Vitrine Veículos` |
| `docs/components/vitrine-veiculos-web/architecture.md` | `docs >> Componentes >> Componente Vitrine Veículos Web` | `Componente Vitrine Veículos Web` |
| `docs/guides/contributing.md` | `docs >> Guias` | `Guias` |

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
