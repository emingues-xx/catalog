# Workflows CI/CD - ecommerce-veiculos-pipelines

Documentação completa dos workflows de CI/CD reutilizáveis para o E-commerce de Veículos.

## Visão Geral

Os workflows estão organizados para serem reutilizáveis entre todos os componentes do sistema, promovendo consistência e reduzindo duplicação de código.

## Estrutura dos Workflows

```
.github/workflows/
├── reusable-nodejs-ci.yml          # CI Node.js reutilizável
├── reusable-security-scan.yml      # Security scanning
├── reusable-deploy.yml             # Deploy para ambientes
├── update-docs.yml                 # Automação de documentação
└── component-specific/
    ├── web-app-ci.yml              # CI específico para web apps
    ├── api-ci.yml                  # CI específico para APIs
    └── library-ci.yml              # CI específico para libraries
```

## Workflow Principal: Node.js CI

### reusable-nodejs-ci.yml

Workflow reutilizável para projetos Node.js com TypeScript.

```yaml
name: Node.js CI (Reusable)

on:
  workflow_call:
    inputs:
      node-version:
        required: false
        type: string
        default: '18'
      package-manager:
        required: false
        type: string
        default: 'npm'
      run-tests:
        required: false
        type: boolean
        default: true
      run-e2e:
        required: false
        type: boolean
        default: false

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ inputs.node-version }}
          cache: ${{ inputs.package-manager }}
          
      - name: Install dependencies
        run: |
          if [ "${{ inputs.package-manager }}" = "yarn" ]; then
            yarn install --frozen-lockfile
          else
            npm ci
          fi
          
      - name: Lint
        run: |
          if [ "${{ inputs.package-manager }}" = "yarn" ]; then
            yarn lint
          else
            npm run lint
          fi
          
      - name: Type check
        run: |
          if [ "${{ inputs.package-manager }}" = "yarn" ]; then
            yarn type-check
          else
            npm run type-check
          fi
          
      - name: Build
        run: |
          if [ "${{ inputs.package-manager }}" = "yarn" ]; then
            yarn build
          else
            npm run build
          fi
          
      - name: Test
        if: ${{ inputs.run-tests }}
        run: |
          if [ "${{ inputs.package-manager }}" = "yarn" ]; then
            yarn test:ci
          else
            npm run test:ci
          fi
          
      - name: E2E Tests
        if: ${{ inputs.run-e2e }}
        run: |
          if [ "${{ inputs.package-manager }}" = "yarn" ]; then
            yarn test:e2e
          else
            npm run test:e2e
          fi
```

## Security Scanning Workflow

### reusable-security-scan.yml

```yaml
name: Security Scan (Reusable)

on:
  workflow_call:
    inputs:
      language:
        required: true
        type: string

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: ${{ inputs.language }}
          
      - name: Autobuild
        uses: github/codeql-action/autobuild@v2
        
      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2
        
      - name: Dependency Review
        uses: actions/dependency-review-action@v3
        
      - name: Snyk Security Scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

## Deploy Workflow

### reusable-deploy.yml

```yaml
name: Deploy (Reusable)

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
      component-name:
        required: true
        type: string
    secrets:
      AWS_ACCESS_KEY_ID:
        required: true
      AWS_SECRET_ACCESS_KEY:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
          
      - name: Login to Amazon ECR
        uses: aws-actions/amazon-ecr-login@v1
        
      - name: Build and push Docker image
        run: |
          docker build -t ${{ inputs.component-name }}:${{ github.sha }} .
          docker tag ${{ inputs.component-name }}:${{ github.sha }} \
            123456789.dkr.ecr.us-east-1.amazonaws.com/${{ inputs.component-name }}:${{ github.sha }}
          docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/${{ inputs.component-name }}:${{ github.sha }}
          
      - name: Deploy to EKS
        run: |
          aws eks update-kubeconfig --name ecommerce-${{ inputs.environment }}-cluster
          kubectl set image deployment/${{ inputs.component-name }} \
            ${{ inputs.component-name }}=123456789.dkr.ecr.us-east-1.amazonaws.com/${{ inputs.component-name }}:${{ github.sha }}
```

## Workflows Específicos por Tipo

### Web Applications (React/Next.js)

```yaml
name: Web App CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  ci:
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-nodejs-ci.yml@main
    with:
      node-version: '18'
      package-manager: 'npm'
      run-tests: true
      run-e2e: true
      
  security:
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-security-scan.yml@main
    with:
      language: 'javascript'
      
  deploy-dev:
    if: github.ref == 'refs/heads/develop'
    needs: [ci, security]
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-deploy.yml@main
    with:
      environment: 'development'
      component-name: ${{ github.event.repository.name }}
    secrets: inherit
```

### APIs (Node.js/Express)

```yaml
name: API CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  ci:
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-nodejs-ci.yml@main
    with:
      node-version: '18'
      package-manager: 'npm'
      run-tests: true
      run-e2e: false
      
  security:
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-security-scan.yml@main
    with:
      language: 'javascript'
      
  integration-tests:
    needs: ci
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Run integration tests
        run: npm run test:integration
```

### Libraries

```yaml
name: Library CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  ci:
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-nodejs-ci.yml@main
    with:
      node-version: '18'
      package-manager: 'npm'
      run-tests: true
      run-e2e: false
      
  publish:
    if: github.ref == 'refs/heads/main'
    needs: ci
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'
          registry-url: 'https://registry.npmjs.org'
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Publish to NPM
        run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

## Como Usar os Workflows

### 1. Referenciando Workflow Reutilizável

```yaml
# No repositório do componente (.github/workflows/ci.yml)
name: CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  ci:
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-nodejs-ci.yml@main
    with:
      node-version: '18'
      package-manager: 'npm'
      run-tests: true
    secrets: inherit
```

### 2. Customizando para Necessidades Específicas

```yaml
# Workflow customizado baseado no reutilizável
jobs:
  ci:
    uses: emingues-xx/ecommerce-veiculos-pipelines/.github/workflows/reusable-nodejs-ci.yml@main
    with:
      node-version: '16'  # Versão específica
      package-manager: 'yarn'  # Package manager diferente
      run-tests: false  # Pular testes se necessário
      
  custom-step:
    needs: ci
    runs-on: ubuntu-latest
    steps:
      - name: Custom deployment logic
        run: echo "Custom step"
```

## Convenções e Padrões

### Naming Convention
- **Workflows reutilizáveis**: `reusable-{purpose}.yml`
- **Workflows específicos**: `{component-type}-ci.yml`
- **Jobs**: Nomes descritivos em inglês
- **Steps**: Nomes claros e concisos

### Secrets Management
```yaml
# Secrets organizacionais
ANTHROPIC_API_KEY      # Claude API para automação de docs
AWS_ACCESS_KEY_ID      # Deploy AWS
AWS_SECRET_ACCESS_KEY  # Deploy AWS
SNYK_TOKEN            # Security scanning
NPM_TOKEN             # Publish libraries

# Secrets específicos por repositório
DATABASE_URL          # Para testes de integração
API_KEY              # Para testes E2E
```

### Environment Variables
```yaml
# Variáveis globais
ENVIRONMENT: ${{ github.ref == 'refs/heads/main' && 'production' || 'development' }}
COMPONENT_NAME: ${{ github.event.repository.name }}
VERSION: ${{ github.sha }}
```

## Troubleshooting

### Problemas Comuns

#### Workflow não encontrado
```bash
# Erro: workflow not found
# Solução: Verificar se o workflow existe na branch main
# do repositório ecommerce-veiculos-pipelines
```

#### Secrets não disponíveis
```bash
# Erro: secret not found
# Solução: Configurar secrets no nível da organização
# ou passá-los explicitamente
```

#### Testes falhando
```bash
# Verificar se scripts estão definidos no package.json:
# - test:ci
# - lint
# - type-check
# - build
```

### Debugging

```yaml
# Adicionar debug steps
- name: Debug
  run: |
    echo "Repository: ${{ github.repository }}"
    echo "Branch: ${{ github.ref }}"
    echo "Event: ${{ github.event_name }}"
    env
```

## Monitoramento e Métricas

### Métricas dos Workflows
- **Success Rate**: Taxa de sucesso por workflow
- **Duration**: Tempo médio de execução
- **Failure Rate**: Taxa de falhas e causas
- **Resource Usage**: Uso de runners e tempo

### Dashboards
- **GitHub Actions Insights**: Métricas nativas do GitHub
- **Custom Dashboard**: Métricas específicas do domínio
- **Security Dashboard**: Vulnerabilidades encontradas

## Roadmap

### Próximas Funcionalidades
- [ ] **Workflow para Mobile**: CI/CD para React Native
- [ ] **Performance Testing**: Testes de performance automatizados
- [ ] **Visual Regression**: Testes de regressão visual
- [ ] **Auto-scaling**: Deploy com auto-scaling baseado em métricas
- [ ] **Multi-environment**: Deploy paralelo para múltiplos ambientes