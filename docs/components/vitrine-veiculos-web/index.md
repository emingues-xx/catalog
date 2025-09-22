# vitrine-veiculos-web

![Build Status](https://img.shields.io/github/actions/workflow/status/emingues-xx/vitrine-veiculos-web/ci.yml?branch=main)
![Version](https://img.shields.io/github/v/release/emingues-xx/vitrine-veiculos-web)
![License](https://img.shields.io/github/license/emingues-xx/vitrine-veiculos-web)
![Tech Stack](https://img.shields.io/badge/React-18-blue)
![Tech Stack](https://img.shields.io/badge/Next.js-14-black)
![Tech Stack](https://img.shields.io/badge/TypeScript-5-blue)

Frontend da vitrine pública de veículos - interface React/Next.js otimizada para SEO e performance.

## Descrição

Aplicação web responsiva que oferece a experiência pública de navegação, busca e visualização de veículos disponíveis para venda. Construída com foco em performance, SEO e experiência do usuário.

## Características Principais

- 🚀 **Performance**: SSR/SSG com Next.js para carregamento rápido  
- 🔍 **SEO Otimizado**: Meta tags dinâmicas e estrutura semântica  
- 📱 **Responsivo**: Design adaptável para mobile, tablet e desktop
- ♿ **Acessível**: WCAG 2.1 AA compliance
- 🎨 **Design System**: Componentes reutilizáveis e consistentes

## Tecnologias

- **Framework**: Next.js 14 (App Router)
- **Linguagem**: TypeScript 5
- **Styling**: Styled Components + CSS Modules
- **State Management**: Zustand
- **HTTP Client**: Axios
- **Testing**: Jest + React Testing Library
- **Linting**: ESLint + Prettier

## Instalação

### Pré-requisitos
- Node.js 18+ 
- npm 9+ ou yarn 1.22+

### Setup Rápido
```bash
# Clone do repositório
git clone https://github.com/emingues-xx/vitrine-veiculos-web.git
cd vitrine-veiculos-web

# Instalação de dependências  
npm install

# Configuração do ambiente
cp .env.example .env.local
# Edite .env.local com suas configurações

# Servidor de desenvolvimento
npm run dev

# Acesse http://localhost:3000
```

## Scripts Disponíveis

```bash
npm run dev          # Servidor de desenvolvimento
npm run build        # Build para produção
npm run start        # Servidor de produção
npm run test         # Execução de testes
npm run test:watch   # Testes em modo watch
npm run lint         # Linting do código
npm run type-check   # Verificação de tipos TypeScript
```

## Estrutura do Projeto

```
src/
├── app/                 # App Router (Next.js 14)
│   ├── (pages)/        # Grupos de rotas
│   ├── globals.css     # Estilos globais
│   └── layout.tsx      # Layout raiz
├── components/         # Componentes React
│   ├── ui/            # Componentes base (botões, inputs)
│   └── features/      # Componentes específicos de features
├── hooks/             # Custom hooks
├── lib/               # Utilitários e configurações
├── stores/            # Stores do Zustand
├── types/             # Definições TypeScript
└── utils/             # Funções utilitárias
```

## Configuração

### Variáveis de Ambiente

```bash
# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:3001
NEXT_PUBLIC_BFF_URL=http://localhost:3002

# Analytics
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX

# Feature Flags
NEXT_PUBLIC_ENABLE_ANALYTICS=true
NEXT_PUBLIC_ENABLE_PWA=true
```

## Performance

### Métricas Alvo
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s  
- **Time to Interactive**: < 3.0s
- **Cumulative Layout Shift**: < 0.1

### Otimizações Implementadas
- Image optimization automática (Next.js)
- Code splitting por rotas
- Bundle analysis com @next/bundle-analyzer
- Service Worker para cache (PWA)
- Critical CSS inline

## Deploy

### Vercel (Recomendado)
```bash
# Deploy automático via GitHub
# Configure as environment variables no dashboard
```

### Docker
```bash
# Build da imagem
docker build -t vitrine-veiculos-web .

# Execução
docker run -p 3000:3000 vitrine-veiculos-web
```

## Links Relacionados

- 🏗️ [Arquitetura](architecture.md)
- 🔧 [Setup Detalhado](setup.md)
- 📚 [Repositório GitHub](https://github.com/emingues-xx/vitrine-veiculos-web)
- 🎯 [Vitrine BFF](../vitrine-veiculos-bff/index.md)
- 📊 [Vitrine API](../vitrine-veiculos-api/index.md)