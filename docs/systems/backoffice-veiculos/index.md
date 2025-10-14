# Sistema Backoffice de Veículos

🚧 **EM DESENVOLVIMENTO** - O **Backoffice de Veículos** é o sistema interno para cadastro de anúncios, dashboard administrativo e acompanhamento de vendas.

## Visão Geral

Sistema administrativo em desenvolvimento que permitirá aos operadores e vendedores gerenciar anúncios de veículos, acompanhar métricas de vendas e administrar a plataforma de forma eficiente. O sistema é composto por uma arquitetura modular com três componentes principais: API backend, BFF (Backend for Frontend) e interface web.

## Propósito e Objetivos

O sistema **backoffice-veiculos** foi desenvolvido para:

- **Centralizar a gestão de anúncios**: Fornecer uma plataforma unificada para cadastro, edição e moderação de anúncios de veículos
- **Otimizar processos administrativos**: Automatizar tarefas repetitivas e agilizar operações do dia a dia
- **Prover visibilidade de negócio**: Oferecer dashboards e relatórios para tomada de decisão estratégica
- **Garantir controle e segurança**: Implementar controles de acesso, auditoria e permissões granulares
- **Facilitar integrações**: Servir como hub central para integração com sistemas externos (CRM, pagamentos, analytics)

## Componentes do Sistema

### 1. API Backend (backoffice-veiculos-api)
- **Tipo**: Service
- **Repositório**: https://github.com/emingues-xx/backoffice-veiculos-api
- **Tecnologia**: Node.js/TypeScript
- **Responsabilidade**: API RESTful para operações administrativas de veículos
- **Funcionalidades**:
  - CRUD completo de anúncios de veículos
  - Gestão de usuários e vendedores
  - Acompanhamento de vendas e métricas
  - Autenticação JWT e controle de permissões
  - Upload e gerenciamento de imagens
  - Integração com sistemas externos
- **Deploy**: Railway
- **Documentação**: [Ver documentação detalhada](../components/backoffice-veiculos-api/index.md)

### 2. BFF - Backend for Frontend (backoffice-veiculos-bff)
- **Tipo**: Service
- **Repositório**: https://github.com/emingues-xx/backoffice-veiculos-bff
- **Tecnologia**: Node.js/TypeScript
- **Responsabilidade**: Camada intermediária que orquestra chamadas entre o frontend e serviços backend
- **Funcionalidades**:
  - Agregação de dados de múltiplas APIs
  - Transformação de dados para formato otimizado do frontend
  - Cache Redis para melhor performance
  - Rate limiting e throttling
  - Endpoints customizados para necessidades da aplicação web
  - Tratamento de erros e fallbacks
- **Deploy**: Railway
- **Documentação**: [Ver documentação detalhada](../components/backoffice-veiculos-bff/index.md)

### 3. Frontend Web (backoffice-veiculos-web)
- **Tipo**: Website
- **Repositório**: https://github.com/emingues-xx/vitrine-veiculos-web
- **Tecnologia**: React/Next.js/TypeScript
- **Responsabilidade**: Interface web do sistema administrativo de veículos
- **Funcionalidades**:
  - Interface responsiva e intuitiva para gestão de anúncios
  - Dashboard com métricas e indicadores de vendas
  - Formulários de cadastro e edição de veículos
  - Sistema de upload e gerenciamento de imagens
  - Controle de usuários e permissões
  - Relatórios e visualizações de dados
- **Deploy**: Railway
- **Documentação**: [Ver documentação detalhada](../components/backoffice-veiculos-web/index.md)

## Funcionalidades Principais

### 🚧 Dashboard Executivo (Em Desenvolvimento)
Visão consolidada das principais métricas do negócio:
- Anúncios ativos vs inativos
- Volume de vendas por período
- Performance por vendedor
- Métricas de conversão
- Gráficos e indicadores visuais

### 🚧 Gestão de Anúncios (Em Desenvolvimento)
Sistema completo para administração de veículos:
- Cadastro de novos anúncios
- Edição de informações
- Upload e gestão de imagens
- Controle de status (ativo/inativo/vendido)
- Filtros e busca avançada

### 🚧 Consulta de Vendas (Em Desenvolvimento)
Sistema de acompanhamento e análise de vendas:
- **Relatórios de Vendas**: Visualização de vendas por período, vendedor e categoria
- **Métricas de Performance**: Taxa de conversão, tempo médio de venda, ticket médio
- **Análise de Tendências**: Gráficos de evolução de vendas ao longo do tempo
- **Comparativos**: Performance entre vendedores e períodos
- **Filtros Avançados**: Por data, vendedor, marca, modelo, faixa de preço
- **Exportação de Dados**: Relatórios em PDF, Excel e CSV
- **Dashboard de Vendas**: Visão executiva com KPIs principais

### 🚧 Controle de Usuários (Em Desenvolvimento)
Administração de acessos e permissões:
- Cadastro de vendedores
- Definição de perfis de acesso
- Controle de permissões por funcionalidade
- Auditoria de ações dos usuários

## Perfis de Acesso

### 🚧 Administrador (Em Desenvolvimento)
- Acesso completo ao sistema
- Gestão de usuários e permissões
- Visualização de todos os relatórios
- Configurações do sistema
- **Consulta de Vendas**: Acesso a todos os dados de vendas e relatórios

### 🚧 Gerente de Vendas (Em Desenvolvimento)
- Dashboard de vendas
- Relatórios de performance
- Gestão de equipe
- Aprovação de anúncios
- **Consulta de Vendas**: 
  - Relatórios de vendas da equipe
  - Comparativos de performance
  - Análise de tendências
  - Métricas de conversão

### 🚧 Vendedor (Em Desenvolvimento)
- Cadastro de anúncios próprios
- Acompanhamento de vendas pessoais
- Edição de anúncios ativos
- Chat com potenciais compradores
- **Consulta de Vendas**:
  - Vendas pessoais
  - Histórico de vendas
  - Métricas individuais
  - Relatórios de performance pessoal

### 🚧 Operador (Em Desenvolvimento)
- Moderação de anúncios
- Suporte a usuários
- Relatórios operacionais
- Gestão de conteúdo
- **Consulta de Vendas**: Acesso limitado a relatórios operacionais

## Segurança

- **Autenticação**: JWT com refresh tokens
- **Autorização**: Controle baseado em roles (RBAC)
- **Auditoria**: Log de todas as ações administrativas
- **Sessões**: Controle de sessões ativas por usuário

## Fluxo de Dados e Integrações

### Fluxo Principal
```
[Usuário Administrativo]
       ↓
[backoffice-veiculos-web] → Interface do usuário
       ↓
[backoffice-veiculos-bff] → Orquestração e agregação de dados
       ↓
[APIs Backend] → Operações CRUD, Validações, Autenticação
       ↓
[Banco de Dados] → Persistência de dados
       ↓
[Sistemas Externos] → Integrações com terceiros
```

### Integrações

- **Sistema de Pagamentos**: Para controle financeiro e acompanhamento de transações
- **CRM**: Sincronização automática de leads e vendas
- **Sistema de Notificações**: Envio de e-mails e push notifications para usuários
- **Analytics**: Integração com ferramentas de BI para análise de dados
- **Storage (S3/Cloud)**: Armazenamento de imagens e documentos

## Tecnologias e Frameworks

### 🚧 Frontend Web (backoffice-veiculos-web) - Em Desenvolvimento
- **Runtime**: Node.js 18+
- **Framework**: React/Next.js
- **Linguagem**: TypeScript
- **Gerenciamento de Estado**: Redux Toolkit ou Zustand
- **UI Components**: Material-UI, Ant Design ou Chakra UI
- **Comunicação HTTP**: Axios
- **Roteamento**: React Router
- **Formulários**: React Hook Form
- **Gráficos**: Chart.js, Recharts ou D3.js
- **Deploy**: Railway

### 🚧 BFF (backoffice-veiculos-bff) - Em Desenvolvimento
- **Runtime**: Node.js 18+
- **Framework**: Express.js
- **Linguagem**: TypeScript
- **Autenticação**: JWT (JSON Web Tokens)
- **Validação**: Joi ou class-validator
- **Cache**: Redis
- **Documentação API**: Swagger/OpenAPI
- **Deploy**: Railway

### 🚧 API Backend (backoffice-veiculos-api) - Em Desenvolvimento
- **Runtime**: Node.js 18+
- **Framework**: Express.js
- **Linguagem**: TypeScript
- **Banco de Dados**: MongoDB
- **Autenticação**: JWT
- **Containerização**: Docker
- **Deploy**: Railway
- **CI/CD**: GitHub Actions com avaliação automática de PRs

### Infraestrutura Compartilhada
- **Banco de Dados**: MongoDB
- **Storage**: Railway ou AWS S3 para imagens
- **Cache**: Redis
- **Mensageria**: Futuro - RabbitMQ ou Kafka

### Ferramentas de Desenvolvimento
- **Controle de Versão**: Git/GitHub
- **CI/CD**: GitHub Actions
- **Containerização**: Docker
- **Monitoramento**: Logs estruturados
- **Testes**: Jest, React Testing Library
- **Deploy**: Railway

## Guia de Navegação

### Documentação dos Componentes

#### 1. API Backend
- **[backoffice-veiculos-api](../components/backoffice-veiculos-api/index.md)**: Documentação completa da API
  - [Arquitetura](../components/backoffice-veiculos-api/architecture.md): Estrutura técnica e padrões utilizados
  - [Instalação e Configuração](../components/backoffice-veiculos-api/installation.md): Guia de setup e deploy
  - [Referência da API](../components/backoffice-veiculos-api/api-reference.md): Documentação completa dos endpoints

#### 2. BFF - Backend for Frontend
- **[backoffice-veiculos-bff](../components/backoffice-veiculos-bff/index.md)**: Documentação completa do BFF
  - [Arquitetura](../components/backoffice-veiculos-bff/architecture.md): Estrutura técnica e padrões utilizados
  - [Instalação e Configuração](../components/backoffice-veiculos-bff/installation.md): Guia de setup e deploy
  - [Referência da API](../components/backoffice-veiculos-bff/api-reference.md): Documentação completa dos endpoints

#### 3. Frontend Web
- **[backoffice-veiculos-web](../components/backoffice-veiculos-web/index.md)**: Documentação completa da aplicação web
  - [Arquitetura](../components/backoffice-veiculos-web/architecture.md): Estrutura de componentes e fluxo de dados
  - [Instalação e Configuração](../components/backoffice-veiculos-web/installation.md): Guia de setup e desenvolvimento
  - [Guia do Usuário](../components/backoffice-veiculos-web/user-guide.md): Como usar a interface

### Como Usar Esta Documentação
1. **Iniciantes**: Comece pela visão geral do sistema (esta página)
2. **Desenvolvedores Frontend**: Consulte a documentação do backoffice-veiculos-web
3. **Desenvolvedores Backend**: Consulte a documentação do backoffice-veiculos-api e backoffice-veiculos-bff
4. **DevOps**: Veja os guias de instalação e configuração de todos os componentes
5. **Product Owners**: Foque nas funcionalidades principais, perfis de acesso e consulta de vendas
6. **Analistas de Negócio**: Consulte a seção de consulta de vendas e relatórios

## Time Responsável

**Squad Backoffice**: Responsável pelo desenvolvimento e manutenção do sistema administrativo interno.