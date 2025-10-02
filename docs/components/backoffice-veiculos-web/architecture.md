# Arquitetura - Backoffice Veículos Web

## Visão Geral

O **backoffice-veiculos-web** é uma aplicação frontend desenvolvida para gerenciamento de veículos no backoffice. A aplicação utiliza tecnologias modernas de desenvolvimento web para proporcionar uma interface intuitiva e responsiva.

## Stack Tecnológico

- **Framework:** React.js
- **Linguagem:** TypeScript
- **Gerenciamento de Estado:** Redux / Context API
- **Roteamento:** React Router
- **Estilização:** CSS Modules / Styled Components
- **Build Tool:** Webpack / Vite
- **Gerenciador de Pacotes:** npm / yarn

## Estrutura de Componentes

```
src/
├── components/          # Componentes reutilizáveis
│   ├── common/         # Componentes genéricos (Button, Input, Modal)
│   ├── layout/         # Componentes de layout (Header, Sidebar, Footer)
│   └── features/       # Componentes específicos de funcionalidades
├── pages/              # Páginas da aplicação
│   ├── Dashboard/
│   ├── Vehicles/
│   ├── Users/
│   └── Reports/
├── services/           # Serviços de comunicação com APIs
├── store/              # Configuração do gerenciamento de estado
│   ├── actions/
│   ├── reducers/
│   └── selectors/
├── hooks/              # Custom hooks
├── utils/              # Funções utilitárias
├── styles/             # Estilos globais e temas
└── types/              # Definições de tipos TypeScript
```

## Fluxo de Dados e Estado

### Gerenciamento de Estado

- **Estado Local:** Utilizado em componentes específicos através de `useState` e `useReducer`
- **Estado Global:** Gerenciado via Redux para dados compartilhados entre múltiplos componentes
- **Cache de Dados:** Implementado para otimizar requisições e melhorar performance

### Fluxo de Dados

1. **Requisição Iniciada:** Componente dispara ação
2. **Action Dispatcher:** Redux action é disparada
3. **API Service:** Serviço realiza chamada HTTP
4. **Response Handler:** Resposta é processada
5. **State Update:** Estado global é atualizado
6. **Component Re-render:** Componentes subscritos são re-renderizados

## Integração com APIs

### BFF (Backend for Frontend)

A aplicação se comunica exclusivamente com o **backoffice-veiculos-bff**, que atua como camada intermediária:

- **Base URL:** Configurada via variável de ambiente `REACT_APP_API_URL`
- **Autenticação:** JWT tokens armazenados em localStorage/sessionStorage
- **Interceptors:** Axios interceptors para tratamento de erros e refresh tokens
- **Error Handling:** Tratamento centralizado de erros com feedback ao usuário

### Endpoints Principais

```typescript
/api/vehicles       # CRUD de veículos
/api/users          # Gerenciamento de usuários
/api/reports        # Geração de relatórios
/api/auth           # Autenticação e autorização
```

## Build e Deploy

### Processo de Build

```bash
# Instalação de dependências
npm install

# Build de produção
npm run build

# Output: pasta 'build/' ou 'dist/' com arquivos estáticos otimizados
```

### Configuração de Ambiente

Variáveis de ambiente são gerenciadas através de arquivos `.env`:

```
REACT_APP_API_URL=https://api.example.com
REACT_APP_ENV=production
REACT_APP_VERSION=1.0.0
```

### Pipeline de Deploy

1. **Build:** Geração de bundle otimizado
2. **Testes:** Execução de testes unitários e e2e
3. **Análise:** Verificação de qualidade de código
4. **Deploy:** Upload para servidor de hospedagem (S3, Nginx, CDN)
5. **Validação:** Smoke tests em ambiente de produção

### Estratégia de Deploy

- **Ambientes:** Development, Staging, Production
- **CI/CD:** Integração contínua via GitHub Actions / Jenkins
- **Rollback:** Capacidade de reverter para versão anterior em caso de falhas
- **Cache Busting:** Versionamento de assets para invalidar cache do navegador

## Segurança

- **XSS Protection:** Sanitização de inputs
- **CSRF Protection:** Tokens CSRF em requisições mutáveis
- **Autenticação:** JWT com refresh token
- **HTTPS:** Comunicação criptografada obrigatória em produção

## Performance

- **Code Splitting:** Divisão de código por rotas
- **Lazy Loading:** Carregamento sob demanda de componentes
- **Memoization:** Uso de React.memo e useMemo
- **Bundle Optimization:** Minificação e tree shaking
