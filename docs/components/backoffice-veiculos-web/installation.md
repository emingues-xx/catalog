# Instalação - Backoffice Veículos Web

## Pré-requisitos

- **Node.js**: 18+ (recomendado 20.x)
- **npm**: 9+ ou **yarn**: 1.22+
- **Git**: Para clonagem do repositório
- **Acesso ao BFF**: backoffice-veiculos-bff
- **Docker**: Opcional, para containerização

## Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/emingues-xx/vitrine-veiculos-web.git
cd vitrine-veiculos-web
```

### 2. Instale as dependências

```bash
npm install
# ou
yarn install
```

### 3. Configure as variáveis de ambiente

Copie o arquivo de exemplo e configure as variáveis:

```bash
cp .env.example .env.local
```

Edite o arquivo `.env.local` com suas configurações:

```bash
# API Backend
NEXT_PUBLIC_API_URL=https://backoffice-veiculos-bff.railway.app
NEXT_PUBLIC_API_VERSION=v1
NEXT_PUBLIC_API_TIMEOUT=30000

# Autenticação
NEXT_PUBLIC_JWT_SECRET=your-jwt-secret
NEXT_PUBLIC_TOKEN_KEY=backoffice_token
NEXT_PUBLIC_REFRESH_TOKEN_KEY=backoffice_refresh_token

# Configurações da Aplicação
NEXT_PUBLIC_APP_NAME=Backoffice Veículos
NEXT_PUBLIC_APP_VERSION=1.0.0
NEXT_PUBLIC_APP_ENV=development

# Upload de Arquivos
NEXT_PUBLIC_MAX_FILE_SIZE=10485760
NEXT_PUBLIC_ALLOWED_FILE_TYPES=image/jpeg,image/png,image/webp

# Analytics (opcional)
NEXT_PUBLIC_GA_TRACKING_ID=GA-XXXXXXXXX
NEXT_PUBLIC_HOTJAR_ID=XXXXXXXXX

# Recaptcha (opcional)
NEXT_PUBLIC_RECAPTCHA_SITE_KEY=your-recaptcha-site-key
```

### 4. Inicie o servidor de desenvolvimento

```bash
# Desenvolvimento com hot reload
npm run dev

# Desenvolvimento com debug
npm run dev:debug

# Desenvolvimento com análise de bundle
npm run dev:analyze
```

### 5. Verifique a instalação

```bash
# Acesse a aplicação
open http://localhost:3000

# Teste a conectividade com a API
curl http://localhost:3000/api/health
```

## Docker

### Build da imagem

```bash
docker build -t backoffice-veiculos-web .
```

### Executar container

```bash
docker run -p 3000:3000 \
  -e NEXT_PUBLIC_API_URL=https://backoffice-veiculos-bff.railway.app \
  -e NEXT_PUBLIC_JWT_SECRET=your-jwt-secret \
  backoffice-veiculos-web
```

### Docker Compose

Crie um arquivo `docker-compose.yml`:

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=https://backoffice-veiculos-bff.railway.app
      - NEXT_PUBLIC_JWT_SECRET=your-jwt-secret
      - NODE_ENV=production
    volumes:
      - ./public:/app/public
    restart: unless-stopped
```

Execute com:

```bash
docker-compose up -d
```

## Deploy

### Railway (Recomendado)

1. **Conecte o repositório**:
   - Acesse [Railway](https://railway.app)
   - Conecte sua conta GitHub
   - Selecione o repositório `vitrine-veiculos-web`

2. **Configure as variáveis de ambiente**:
   ```bash
   NEXT_PUBLIC_API_URL=https://backoffice-veiculos-bff.railway.app
   NEXT_PUBLIC_JWT_SECRET=your-production-jwt-secret
   NODE_ENV=production
   ```

3. **Deploy automático**: A cada push na branch `main`

### Vercel

1. **Instale o Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Configure e deploy**:
   ```bash
   vercel --prod
   ```

### Netlify

1. **Conecte o repositório** no Netlify
2. **Configure as variáveis de ambiente**
3. **Configure o build command**: `npm run build`
4. **Configure o publish directory**: `.next`

## Build de Produção

### Build Local

```bash
# Build para produção
npm run build

# Iniciar servidor de produção
npm start

# Build com análise de bundle
npm run build:analyze
```

### Build no CI/CD

```bash
# Instalar dependências
npm ci

# Build
npm run build

# Testes
npm run test

# Lint
npm run lint
```

## Testes

### Executar Testes

```bash
# Todos os testes
npm test

# Testes com coverage
npm run test:coverage

# Testes em modo watch
npm run test:watch

# Testes E2E
npm run test:e2e

# Testes de acessibilidade
npm run test:a11y
```

### Configuração de Testes

Crie um arquivo `.env.test`:

```bash
NEXT_PUBLIC_API_URL=http://localhost:3002
NEXT_PUBLIC_JWT_SECRET=test-jwt-secret
NODE_ENV=test
```

## Scripts Disponíveis

```bash
# Desenvolvimento
npm run dev          # Inicia servidor de desenvolvimento
npm run dev:debug    # Inicia com debugger
npm run dev:analyze  # Inicia com análise de bundle

# Produção
npm start            # Inicia servidor de produção
npm run build        # Build para produção
npm run build:analyze # Build com análise de bundle

# Testes
npm test             # Executa testes
npm run test:watch   # Testes em modo watch
npm run test:coverage # Testes com coverage
npm run test:e2e     # Testes E2E
npm run test:a11y    # Testes de acessibilidade

# Qualidade de código
npm run lint         # ESLint
npm run lint:fix     # ESLint com auto-fix
npm run format       # Prettier
npm run type-check   # Verificação de tipos TypeScript

# Análise
npm run analyze      # Análise de bundle
npm run lighthouse   # Teste de performance
npm run bundle-analyzer # Analisador de bundle

# Docker
npm run docker:build # Build da imagem Docker
npm run docker:run   # Executa container
```

## Estrutura do Projeto

```
src/
├── components/          # Componentes reutilizáveis
│   ├── ui/             # Componentes de interface
│   ├── forms/          # Formulários
│   ├── charts/         # Gráficos e visualizações
│   ├── layout/         # Layout e navegação
│   └── common/         # Componentes comuns
├── pages/              # Páginas da aplicação
│   ├── api/            # API routes (Next.js)
│   ├── dashboard/      # Dashboard principal
│   ├── anuncios/       # Gestão de anúncios
│   ├── usuarios/       # Gestão de usuários
│   ├── relatorios/     # Relatórios
│   └── auth/           # Autenticação
├── services/           # Serviços de API
├── hooks/              # Custom hooks
├── store/              # Gerenciamento de estado
├── utils/              # Utilitários
├── types/              # Definições TypeScript
├── styles/             # Estilos globais
└── public/             # Arquivos estáticos
```

## Configuração de Desenvolvimento

### VS Code

Instale as extensões recomendadas:

```json
{
  "recommendations": [
    "bradlc.vscode-tailwindcss",
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "ms-vscode.vscode-typescript-next"
  ]
}
```

### Configuração do ESLint

```json
{
  "extends": [
    "next/core-web-vitals",
    "@typescript-eslint/recommended",
    "prettier"
  ],
  "rules": {
    "prefer-const": "error",
    "no-unused-vars": "warn"
  }
}
```

## Troubleshooting

### Problemas Comuns

1. **Erro de build**:
   ```bash
   # Limpe o cache
   rm -rf .next
   npm run build
   ```

2. **Erro de API**:
   - Verifique se o BFF está rodando
   - Confirme a URL da API no `.env.local`
   - Teste a conectividade

3. **Erro de autenticação**:
   - Verifique o JWT_SECRET
   - Confirme se os tokens estão sendo enviados corretamente

4. **Erro de performance**:
   ```bash
   # Analise o bundle
   npm run analyze
   
   # Teste de performance
   npm run lighthouse
   ```

### Logs

```bash
# Ver logs em tempo real
npm run dev

# Logs do Docker
docker-compose logs -f web

# Logs do Railway
railway logs
```

## Links Úteis

- [Repositório](https://github.com/emingues-xx/vitrine-veiculos-web)
- [Documentação da API](https://backoffice-veiculos-bff.railway.app/api-docs)
- [Railway Dashboard](https://railway.app)
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev)