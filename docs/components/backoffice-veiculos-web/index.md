# Backoffice Veículos Web

## Visão Geral

Aplicação frontend web Node.js/TypeScript do sistema de backoffice de veículos, responsável pela interface de usuário administrativa e interação com os serviços de gestão de veículos. A aplicação fornece uma interface moderna e responsiva para operações administrativas.

## Propósito

Fornecer uma interface web intuitiva e responsiva para operações de gerenciamento de veículos no backoffice, permitindo aos usuários realizar:
- Cadastros e edição de anúncios de veículos
- Consultas e visualização de informações detalhadas
- Gestão de usuários e permissões
- Acompanhamento de vendas e métricas
- Dashboard executivo com indicadores de negócio

## Funcionalidades Principais

### Dashboard Administrativo
- Visão geral das métricas de vendas
- Gráficos e indicadores de performance
- Relatórios de anúncios ativos/inativos
- Estatísticas por vendedor e período

### Gestão de Anúncios
- Interface de cadastro de novos anúncios
- Edição e atualização de informações
- Upload e gerenciamento de imagens
- Controle de status (ativo/inativo/vendido)
- Filtros e busca avançada

### Gestão de Usuários
- Cadastro de vendedores e operadores
- Controle de permissões e roles
- Auditoria de ações dos usuários
- Gerenciamento de perfis

### Relatórios e Analytics
- Relatórios de vendas por período
- Análise de performance de anúncios
- Métricas de conversão
- Exportação de dados

## Tecnologias Utilizadas

- **Runtime**: Node.js
- **Linguagem**: TypeScript
- **Framework Frontend**: React/Next.js
- **Gerenciamento de Estado**: Redux Toolkit ou Zustand
- **Estilização**: Tailwind CSS ou Styled Components
- **UI Components**: Material-UI, Ant Design ou Chakra UI
- **Build Tool**: Vite ou Webpack
- **Roteamento**: React Router
- **Formulários**: React Hook Form
- **Gráficos**: Chart.js, Recharts ou D3.js
- **Testes**: Jest, React Testing Library
- **Containerização**: Docker
- **Deploy**: Railway

## Arquitetura Frontend

### Estrutura de Componentes

```
src/
├── components/          # Componentes reutilizáveis
│   ├── ui/             # Componentes de interface
│   ├── forms/          # Formulários
│   ├── charts/         # Gráficos e visualizações
│   └── layout/         # Layout e navegação
├── pages/              # Páginas da aplicação
│   ├── dashboard/      # Dashboard principal
│   ├── anuncios/       # Gestão de anúncios
│   ├── usuarios/       # Gestão de usuários
│   └── relatorios/     # Relatórios
├── services/           # Serviços de API
├── hooks/              # Custom hooks
├── store/              # Gerenciamento de estado
├── utils/              # Utilitários
└── types/              # Definições TypeScript
```

### Fluxo de Dados

1. **Interface do Usuário**: Componentes React capturam interações
2. **Estado Global**: Redux/Zustand gerencia estado da aplicação
3. **Serviços**: Camada de serviços faz requisições para o BFF
4. **BFF**: Backend for Frontend processa e agrega dados
5. **APIs**: Serviços backend executam operações de negócio

## Perfis de Usuário

### Administrador
- Acesso completo ao sistema
- Gestão de usuários e permissões
- Visualização de todos os relatórios
- Configurações do sistema

### Gerente de Vendas
- Dashboard de vendas
- Relatórios de performance
- Gestão de equipe
- Aprovação de anúncios

### Vendedor
- Cadastro de anúncios próprios
- Acompanhamento de vendas pessoais
- Edição de anúncios ativos

### Operador
- Moderação de anúncios
- Suporte a usuários
- Relatórios operacionais

## Configuração e Deploy

### Variáveis de Ambiente

```bash
# API Backend
NEXT_PUBLIC_API_URL=https://backoffice-veiculos-bff.railway.app
NEXT_PUBLIC_API_VERSION=v1

# Autenticação
NEXT_PUBLIC_JWT_SECRET=your-jwt-secret
NEXT_PUBLIC_TOKEN_KEY=backoffice_token

# Configurações
NEXT_PUBLIC_APP_NAME=Backoffice Veículos
NEXT_PUBLIC_APP_VERSION=1.0.0
NODE_ENV=production
```

### Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## Links Úteis

- [Repositório](https://github.com/emingues-xx/vitrine-veiculos-web)
- [Documentação da API](https://backoffice-veiculos-bff.railway.app/api-docs)
- [Deploy no Railway](https://railway.app)
- [Guia de Desenvolvimento](./installation.md)
- [Arquitetura](./architecture.md)
- [Guia do Usuário](./user-guide.md)
