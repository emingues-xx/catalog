# Catálogo Backstage - E-commerce de Veículos

Este repositório contém a definição completa do catálogo Backstage para o domínio de E-commerce de Veículos, incluindo documentação técnica centralizada com TechDocs.

## 🏗️ Estrutura do Catálogo

### Entidades Backstage
- **`catalog-info.yaml`**: Arquivo raiz que registra todas as entidades
- **`domains/`**: Definições de domínios de negócio
- **`systems/`**: Sistemas que compõem cada domínio  
- **`apis/`**: Definições das APIs REST
- **`components/`**: Componentes (repositórios) que implementam os sistemas
- **`owners/`**: Definições de grupos e times responsáveis

### Documentação TechDocs
- **`docs/`**: Documentação técnica completa (MkDocs)
- **`mkdocs.yml`**: Configuração do site de documentação


## Domínios

### E-commerce de Veículos
Domínio que concentra as capacidades de venda, catálogo e gestão de anúncios de veículos.

**Sistemas:**
- **Vitrine de Veículos**: Sistema responsável pela vitrine (catálogo público), busca e exibição de veículos
- **Backoffice de Veículos**: Sistema interno para cadastro de anúncios, dashboard e acompanhamento de vendas

## 📊 Visão Geral das Entidades

### 🏢 Domínio: E-commerce de Veículos
| Entidade | Tipo | Owner | Descrição |
|----------|------|-------|-----------|
| **ecommerce-veiculos** | Domain | tribe-ecommerce | Domínio completo de e-commerce |

### 🎯 Sistemas (2)
| Sistema | Owner | Componentes | APIs |
|---------|-------|-------------|------|
| **vitrine-veiculos** | squad-vitrine | 3 components | 2 APIs |
| **backoffice-veiculos** | squad-backoffice | 3 components | 2 APIs |

### 🔧 Componentes (9)
#### Sistema Vitrine de Veículos
- **vitrine-veiculos-web**: Frontend React/Next.js para vitrine pública
- **vitrine-veiculos-api**: API Node.js para consultas e filtros  
- **vitrine-veiculos-bff**: Backend for Frontend otimizado

#### Sistema Backoffice de Veículos  
- **backoffice-veiculos-web**: Frontend administrativo React/Next.js
- **backoffice-veiculos-api**: API Node.js para CRUD e vendas
- **backoffice-veiculos-bff**: Backend for Frontend administrativo

#### Bibliotecas Compartilhadas
- **ecommerce-veiculos-shared**: Tipos TypeScript e utilitários
- **ecommerce-veiculos-ui-components**: Design system React  
- **ecommerce-veiculos-pipelines**: CI/CD workflows e automação de documentação

### 🌐 APIs (4)
- **vitrine-veiculos-api**: REST API pública para consultas
- **vitrine-veiculos-bff-api**: BFF otimizada para frontend
- **backoffice-veiculos-api**: API administrativa para CRUD
- **backoffice-veiculos-bff-api**: BFF para painel administrativo

## Organização

- **Tribo E-commerce**: Grupo responsável pelo domínio completo
  - **Squad Vitrine**: Time responsável pela vitrine de veículos
  - **Squad Backoffice**: Time responsável pelo backoffice de veículos

## Repositórios do Sistema

O ecossistema é composto por 9 repositórios organizados por função:
- **3 repositórios** para vitrine (web, api, bff)
- **3 repositórios** para backoffice (web, api, bff)  
- **3 repositórios** para bibliotecas compartilhadas (shared, ui-components, pipelines)

## Documentação (TechDocs)

A documentação técnica está centralizada neste repositório usando MkDocs/TechDocs:

### Visualizar Localmente
```bash
# Instalar dependências
pip install mkdocs-material mkdocs-techdocs-core

# Servidor local
mkdocs serve

# Acesse http://localhost:8000
```

### Estrutura da Documentação
- **`docs/systems/`**: Documentação detalhada de cada sistema
- **`docs/components/`**: Documentação específica de cada componente
- **`docs/architecture/`**: Visão geral e ADRs (Architecture Decision Records)  
- **`docs/guides/`**: Guias de contribuição e desenvolvimento

### Contribuindo
Veja o [Guia de Contribuição](docs/guides/contributing.md) para detalhes sobre como contribuir com a documentação.

## ✅ Status de Validação

### Compatibilidade Backstage
- ✅ **Entidades**: 17 entidades definidas (1 Domain, 2 Systems, 9 Components, 4 APIs, 1 Location) 
- ✅ **Relationships**: Dependências e ownership corretos
- ✅ **TechDocs**: Configurado nos Systems com metadata apropriado
- ✅ **GitHub Integration**: Annotations para todos os components

### Estrutura de Documentação  
- ✅ **MkDocs**: Build validado sem erros
- ✅ **Navegação**: Estrutura hierárquica por sistemas e componentes
- ✅ **Content**: Documentação completa de arquitetura, APIs e setup
- ✅ **ADRs**: Espaço preparado para Architecture Decision Records

### Automação
- ✅ **Pipelines CI/CD**: Workflows reutilizáveis centralizados
- ✅ **Documentation AI**: Automação inteligente via Claude API
- ✅ **Quality Gates**: Validação automática de código e segurança

## 🚀 Próximos Passos

1. **Importar no Backstage**: Adicionar URL do `catalog-info.yaml` 
2. **Configurar TechDocs**: Habilitar plugin no Backstage
3. **Setup CI/CD**: Configurar workflows nos repositórios dos componentes
4. **Configurar Secrets**: Adicionar `ANTHROPIC_API_KEY` para automação
5. **Desenvolvimento**: Começar implementação dos componentes
