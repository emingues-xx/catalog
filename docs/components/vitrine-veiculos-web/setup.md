# Setup - vitrine-veiculos-web

Guia completo de configuração do ambiente de desenvolvimento.

## Pré-requisitos

### Software Necessário
- **Node.js**: 18.17.0 ou superior
- **npm**: 9.0.0 ou superior (ou yarn 1.22+)
- **Git**: Para controle de versão
- **VSCode**: Editor recomendado

### Verificação de Versões
```bash
node --version   # v18.17.0+
npm --version    # 9.0.0+
git --version    # 2.30.0+
```

## Instalação

### 1. Clone do Repositório
```bash
# Via HTTPS
git clone https://github.com/emingues-xx/vitrine-veiculos-web.git

# Via SSH (recomendado)
git clone git@github.com:emingues-xx/vitrine-veiculos-web.git

cd vitrine-veiculos-web
```

### 2. Instalação de Dependências
```bash
# Usando npm
npm install

# Ou usando yarn
yarn install

# Verificar instalação
npm list --depth=0
```

### 3. Configuração de Ambiente

#### Arquivo .env.local
```bash
# Copiar exemplo
cp .env.example .env.local

# Editar variáveis
nano .env.local
```

#### Variáveis Obrigatórias
```bash
# URLs da API
NEXT_PUBLIC_API_URL=http://localhost:3001
NEXT_PUBLIC_BFF_URL=http://localhost:3002

# Configurações de desenvolvimento
NODE_ENV=development
NEXT_PUBLIC_APP_ENV=development
```

#### Variáveis Opcionais
```bash
# Analytics (desenvolvimento)
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX
NEXT_PUBLIC_ENABLE_ANALYTICS=false

# Feature Flags
NEXT_PUBLIC_ENABLE_PWA=true
NEXT_PUBLIC_ENABLE_DARK_MODE=true

# Debug
NEXT_PUBLIC_DEBUG_MODE=true
```

## Configuração do Editor

### VSCode Extensions
Instale as extensões recomendadas:

```json
{
  "recommendations": [
    "bradlc.vscode-tailwindcss",
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "ms-vscode.vscode-typescript-next",
    "styled-components.vscode-styled-components",
    "christian-kohler.path-intellisense",
    "ms-vscode.vscode-json"
  ]
}
```

### VSCode Settings
Configure o arquivo `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "typescript.preferences.importModuleSpecifier": "relative",
  "emmet.includeLanguages": {
    "typescript": "html",
    "typescriptreact": "html"
  }
}
```

## Configuração de Git

### Git Hooks
```bash
# Instalar husky (se não instalado automaticamente)
npm run prepare

# Verificar hooks
ls -la .husky/
```

### Conventional Commits
Configure o commitizen:
```bash
# Fazer commit interativo
npm run commit

# Ou usar convencional manualmente
git commit -m "feat: adiciona componente VehicleCard"
```

## Execução

### Servidor de Desenvolvimento
```bash
# Iniciar servidor
npm run dev

# Com debug detalhado
DEBUG=* npm run dev

# Especificar porta
PORT=3001 npm run dev
```

### Verificação de Saúde
Após iniciar, verifique:
- ✅ **URL**: http://localhost:3000
- ✅ **Hot Reload**: Funcional
- ✅ **TypeScript**: Sem erros
- ✅ **Console**: Sem warnings críticos

## Comandos de Desenvolvimento

### Linting e Formatação
```bash
# Executar ESLint
npm run lint

# Corrigir problemas automaticamente
npm run lint:fix

# Verificar formatação Prettier
npm run format:check

# Aplicar formatação
npm run format
```

### Verificação de Tipos
```bash
# TypeScript check
npm run type-check

# Em modo watch
npm run type-check:watch
```

### Testes
```bash
# Executar todos os testes
npm run test

# Testes em modo watch
npm run test:watch

# Testes com coverage
npm run test:coverage

# Testes E2E (requer build)
npm run build
npm run test:e2e
```

## Build e Deploy

### Build Local
```bash
# Build para produção
npm run build

# Analisar bundle
npm run analyze

# Testar build localmente
npm run start
```

### Configuração para Deploy

#### Vercel (Recomendado)
```bash
# Instalar Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Deploy para produção
vercel --prod
```

#### Docker
```bash
# Build da imagem
docker build -t vitrine-veiculos-web .

# Executar container
docker run -p 3000:3000 vitrine-veiculos-web
```

## Troubleshooting

### Problemas Comuns

#### Erro de Módulo não Encontrado
```bash
# Limpar cache e reinstalar
rm -rf node_modules package-lock.json
npm install
```

#### Problemas de TypeScript
```bash
# Restart do TypeScript server no VSCode
Ctrl/Cmd + Shift + P > "TypeScript: Restart TS Server"

# Verificar configuração
npx tsc --showConfig
```

#### Problemas de Performance
```bash
# Analisar bundle
npm run analyze

# Verificar dependências
npm run deps:check

# Limpar cache do Next.js
rm -rf .next
```

### Logs de Debug

#### Habilitar Debug
```bash
# Debug completo
DEBUG=* npm run dev

# Debug específico do Next.js
DEBUG=next:* npm run dev

# Debug de network requests
DEBUG=axios npm run dev
```

#### Logs no Browser
```javascript
// Habilitar logs detalhados
localStorage.setItem('debug', 'vitrine:*');
```

## Integração com Backend

### Configuração de Proxy
Durante desenvolvimento, configure proxy para evitar CORS:

```javascript
// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:3001/api/:path*'
      }
    ];
  }
};
```

### Mock de APIs
Para desenvolvimento independente:

```bash
# Iniciar servidor mock
npm run mock:server

# Usar MSW para intercept
npm run dev:mock
```

## Performance Monitoring

### Bundle Analysis
```bash
# Analisar tamanho do bundle
npm run analyze

# Verificar tree-shaking
npm run build 2>&1 | grep "First Load JS"
```

### Métricas de Performance
```bash
# Lighthouse CI
npm run lighthouse

# Web Vitals
npm run vitals
```

## Próximos Passos

1. ✅ Ambiente configurado
2. 🔄 Familiarizar-se com a estrutura
3. 📚 Ler documentação da [Arquitetura](architecture.md)
4. 🧪 Executar testes existentes
5. 🚀 Começar desenvolvimento!