# Sistema Backoffice de Veículos

O **Backoffice de Veículos** é o sistema interno para cadastro de anúncios, dashboard administrativo e acompanhamento de vendas.

## Visão Geral

Sistema administrativo que permite aos operadores e vendedores gerenciar anúncios de veículos, acompanhar métricas de vendas e administrar a plataforma de forma eficiente. O sistema é composto por uma arquitetura modular, centralizada em uma API que oferece funcionalidades completas de gestão e controle administrativo.

## Propósito e Objetivos

O sistema **backoffice-veiculos** foi desenvolvido para:

- **Centralizar a gestão de anúncios**: Fornecer uma plataforma unificada para cadastro, edição e moderação de anúncios de veículos
- **Otimizar processos administrativos**: Automatizar tarefas repetitivas e agilizar operações do dia a dia
- **Prover visibilidade de negócio**: Oferecer dashboards e relatórios para tomada de decisão estratégica
- **Garantir controle e segurança**: Implementar controles de acesso, auditoria e permissões granulares
- **Facilitar integrações**: Servir como hub central para integração com sistemas externos (CRM, pagamentos, analytics)

## Componentes do Sistema

### 1. BFF - Backend for Frontend (backoffice-veiculos-bff)
- **Tipo**: Application
- **Repositório**: https://github.com/emingues-xx/backoffice-veiculos-bff.git
- **Responsabilidade**: Camada intermediária que orquestra chamadas entre o frontend e serviços backend
- **Funcionalidades**:
  - Agregação de dados de múltiplas APIs
  - Transformação de dados para formato otimizado do frontend
  - Gerenciamento de sessão e autenticação
  - Cache de requisições para melhor performance
  - Manipulação de regras de negócio específicas da interface
  - Endpoints customizados para necessidades da aplicação web
- **Documentação**: [Ver documentação detalhada](../components/backoffice-veiculos-bff/index.md)

### 2. Frontend Web (backoffice-veiculos-web)
- **Tipo**: Web Frontend
- **Repositório**: https://github.com/emingues-xx/backoffice-veiculos-web.git
- **Responsabilidade**: Interface web do sistema administrativo de veículos
- **Funcionalidades**:
  - Interface responsiva e intuitiva para gestão de anúncios
  - Dashboard com métricas e indicadores de vendas
  - Formulários de cadastro e edição de veículos
  - Sistema de upload e gerenciamento de imagens
  - Controle de usuários e permissões
  - Relatórios e visualizações de dados
- **Documentação**: [Ver documentação detalhada](../components/backoffice-veiculos-web/index.md)

## Funcionalidades Principais

### Dashboard Executivo
Visão consolidada das principais métricas do negócio:
- Anúncios ativos vs inativos
- Volume de vendas por período
- Performance por vendedor
- Métricas de conversão

### Gestão de Anúncios
Sistema completo para administração de veículos:
- Cadastro de novos anúncios
- Edição de informações
- Upload e gestão de imagens
- Controle de status (ativo/inativo/vendido)

### Controle de Usuários
Administração de acessos e permissões:
- Cadastro de vendedores
- Definição de perfis de acesso
- Controle de permissões por funcionalidade
- Auditoria de ações dos usuários

## Perfis de Acesso

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
- Chat com potenciais compradores

### Operador
- Moderação de anúncios
- Suporte a usuários
- Relatórios operacionais
- Gestão de conteúdo

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

### Frontend Web (backoffice-veiculos-web)
- **Framework**: React ou Next.js
- **Linguagem**: TypeScript/JavaScript
- **Gerenciamento de Estado**: Redux, Context API ou Zustand
- **UI Components**: Material-UI, Ant Design ou biblioteca customizada
- **Comunicação HTTP**: Axios ou Fetch API
- **Roteamento**: React Router
- **Formulários**: React Hook Form ou Formik
- **Gráficos**: Chart.js ou Recharts

### BFF (backoffice-veiculos-bff)
- **Runtime**: Node.js
- **Framework**: Express.js ou NestJS
- **Linguagem**: TypeScript/JavaScript
- **Autenticação**: JWT (JSON Web Tokens)
- **Validação**: Joi ou class-validator
- **Cache**: Redis
- **Documentação API**: Swagger/OpenAPI

### Infraestrutura Compartilhada
- **Banco de Dados**: PostgreSQL/MySQL
- **Storage**: AWS S3 ou similar para imagens
- **Mensageria**: RabbitMQ ou Kafka (se aplicável)

### Ferramentas de Desenvolvimento
- **Controle de Versão**: Git/GitHub
- **CI/CD**: GitHub Actions
- **Containerização**: Docker
- **Monitoramento**: Logs estruturados e APM
- **Testes**: Jest, React Testing Library

## Guia de Navegação

### Documentação dos Componentes

#### 1. Frontend Web
- **[backoffice-veiculos-web](../components/backoffice-veiculos-web/index.md)**: Documentação completa da aplicação web
  - [Arquitetura](../components/backoffice-veiculos-web/architecture.md): Estrutura de componentes e fluxo de dados
  - [Instalação e Configuração](../components/backoffice-veiculos-web/installation.md): Guia de setup e desenvolvimento
  - [Guia do Usuário](../components/backoffice-veiculos-web/user-guide.md): Como usar a interface

#### 2. BFF - Backend for Frontend
- **[backoffice-veiculos-bff](../components/backoffice-veiculos-bff/index.md)**: Documentação completa do BFF
  - [Arquitetura](../components/backoffice-veiculos-bff/architecture.md): Estrutura técnica e padrões utilizados
  - [Instalação e Configuração](../components/backoffice-veiculos-bff/installation.md): Guia de setup e deploy

### Como Usar Esta Documentação
1. **Iniciantes**: Comece pela visão geral do sistema (esta página)
2. **Desenvolvedores Frontend**: Consulte a documentação do backoffice-veiculos-web
3. **Desenvolvedores Backend**: Consulte a documentação do backoffice-veiculos-bff
4. **DevOps**: Veja os guias de instalação e configuração de ambos os componentes
5. **Product Owners**: Foque nas funcionalidades principais e perfis de acesso

## Time Responsável

**Squad Backoffice**: Responsável pelo desenvolvimento e manutenção do sistema administrativo interno.