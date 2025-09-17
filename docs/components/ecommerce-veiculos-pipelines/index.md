# ecommerce-veiculos-pipelines

![Build Status](https://img.shields.io/github/actions/workflow/status/emingues-xx/ecommerce-veiculos-pipelines/ci.yml?branch=main)
![Version](https://img.shields.io/github/v/release/emingues-xx/ecommerce-veiculos-pipelines)
![License](https://img.shields.io/github/license/emingues-xx/ecommerce-veiculos-pipelines)
![Tech Stack](https://img.shields.io/badge/GitHub_Actions-✓-green)
![Tech Stack](https://img.shields.io/badge/Claude_API-✓-blue)
![Tech Stack](https://img.shields.io/badge/Python-3.9+-yellow)

Workflows de CI/CD e automação inteligente de documentação para todo o domínio E-commerce de Veículos.

## Descrição

Repositório centralizado que contém workflows reutilizáveis de CI/CD e sistema de automação de documentação usando Claude API. Monitora mudanças em todos os componentes e atualiza automaticamente a documentação técnica usando inteligência artificial.

## Características Principais

- 🚀 **CI/CD Workflows**: Workflows reutilizáveis para todos os components
- 🤖 **Smart Documentation**: Automação de documentação usando Claude API
- 🔍 **Change Detection**: Monitora mudanças em todos os repositórios
- 📝 **Auto-PR Creation**: Cria PRs automáticos no catálogo
- 🔐 **Security Scanning**: Análise de vulnerabilidades automatizada
- 📊 **Quality Gates**: Validação de código e testes automatizados

## Responsabilidades

### Workflows de CI/CD
- **Build & Test**: Compilação e execução de testes automatizados
- **Security Scanning**: Análise de vulnerabilidades e dependências
- **Code Quality**: Linting, formatting e code coverage
- **Deployment**: Deploy automatizado para ambientes de dev/staging

### Automação de Documentação
- **Change Detection**: Monitora PRs em todos os repositories
- **AI Analysis**: Claude API analisa mudanças e atualiza documentação
- **Auto-PR Creation**: Cria PRs automáticos no catálogo
- **Quality Assurance**: Validação de links e consistência

### Quality Assurance
- **Test Automation**: Execução de testes unitários e integração
- **Performance Testing**: Testes de carga e performance
- **Code Coverage**: Relatórios de cobertura de testes
- **Dependency Management**: Atualização automática de dependências

## Tecnologias

- **CI/CD**: GitHub Actions
- **Languages**: Python 3.9+, Node.js, Bash
- **AI Integration**: Claude API (Anthropic)
- **Security**: Snyk, CodeQL, Dependency Review
- **Documentation**: MkDocs, Markdown
- **Secrets**: GitHub Secrets, Encrypted Variables

## Workflows Disponíveis

### Reusable Workflows
```yaml
# .github/workflows/
├── reusable-nodejs-ci.yml      # CI para projetos Node.js
├── reusable-security-scan.yml  # Security scanning
├── reusable-deploy.yml         # Deploy para ambientes
└── update-docs.yml             # Automação de documentação
```

### Documentation Automation
```yaml
# Trigger automático
on:
  pull_request:
    types: [closed]
    branches: [main]

# Detecta componente e mudanças
# Envia para Claude API
# Atualiza documentação
# Cria PR para review
```

## Componentes Monitorados

### Vitrine System
- **vitrine-veiculos-web**: Frontend React/Next.js
- **vitrine-veiculos-api**: API Node.js
- **vitrine-veiculos-bff**: Backend for Frontend

### Backoffice System  
- **backoffice-veiculos-web**: Frontend administrativo
- **backoffice-veiculos-api**: API administrativa
- **backoffice-veiculos-bff**: BFF administrativo

### Shared Libraries
- **ecommerce-veiculos-shared**: Biblioteca compartilhada
- **ecommerce-veiculos-ui-components**: Design system

## Automação de Documentação

### Workflow Inteligente
1. **PR Detection**: Monitora merges em todos os repos de components
2. **Change Analysis**: Analisa código, commits e metadados
3. **AI Processing**: Claude API gera atualizações contextuais
4. **Auto-Update**: Aplica mudanças na documentação técnica
5. **Quality Review**: Cria PR para review humano

### Tipos de Mudanças Detectadas
- **Nueva features**: `feat:` commits
- **API changes**: Alterações em arquivos `*.api.ts`
- **Dependencies**: Mudanças em `package.json`
- **Configuration**: Alterações em arquivos de config
- **Architecture**: Mudanças estruturais significativas

## Instalação

### Pré-requisitos
- GitHub CLI configurado
- Python 3.9+
- Node.js 18+
- Acesso ao repositório de catálogo

### Setup Local
```bash
# Clone do repositório
git clone https://github.com/emingues-xx/ecommerce-veiculos-pipelines.git
cd ecommerce-veiculos-pipelines

# Instalar dependências Python
pip install -r requirements.txt

# Instalar dependências Node.js
npm install

# Validar workflows
npm run lint:workflows
```

### Configuração de Secrets
```bash
# GitHub Repository Secrets necessários
ANTHROPIC_API_KEY=sk-ant-...           # Claude API key
GITHUB_TOKEN=${{ secrets.GITHUB_TOKEN }} # GitHub access (automático)
```

## Scripts Disponíveis

```bash
# Quality Assurance
npm run lint:workflows      # Linting dos workflows
npm run lint:yaml          # Linting YAML
npm run test:scripts        # Validação scripts Python

# Documentation
npm run docs:serve          # Servidor local docs
npm run docs:build          # Build documentação

# Automation
npm run validate:automation # Validar sistema de automação
```

## Como Usar

### 1. Para Novos Componentes
```yaml
# No repositório do componente, referencie o workflow:
name: CI/CD
on: [push, pull_request]

jobs:
  ci:
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-nodejs-ci.yml@main
    secrets: inherit
```

### 2. Para Automação de Docs
```bash
# A automação é transparente e automática
# Merge qualquer PR para main → documenta automaticamente
# Branch pattern: feature/{component-name}-{feature}
```

### 3. Para Custom Workflows
```bash
# Copie e adapte workflows da pasta .github/workflows/
# Mantenha padrões de naming e estrutura
```

## Monitoramento

### Métricas Coletadas
- **Workflows executados**: Total de execuções por dia/semana
- **Taxa de sucesso**: Porcentagem de workflows bem-sucedidos
- **Tempo de execução**: Métricas de performance
- **Documentation updates**: Atualizações automáticas criadas

### Dashboards
- **GitHub Actions**: Execuções e métricas nativas
- **Claude API Usage**: Consumo da API de IA
- **Quality Metrics**: Code coverage, security findings

## Troubleshooting

### Workflow Failures
```bash
# Check logs no GitHub Actions
# Verificar secrets configurados
# Validar permissões do GitHub token
```

### Documentation Automation Issues
```bash
# Component não detectado:
# - Verificar naming pattern da branch
# - Confirmar merge para main branch

# Claude API errors:
# - Check API key validity
# - Verificar rate limits
# - Validar formato do prompt
```

## Links Relacionados

- 🔧 [Automação de Documentação](automation.md)
- 📋 [Workflows Disponíveis](workflows.md)
- 📚 [Repositório GitHub](https://github.com/emingues-xx/ecommerce-veiculos-pipelines)
- 🎯 [Catálogo Backstage](https://github.com/emingues-xx/catalog)