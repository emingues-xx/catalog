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

### API (backoffice-veiculos-api)
- **Tecnologia**: Node.js
- **Repositório**: https://github.com/emingues-xx/backoffice-veiculos-api.git
- **Responsabilidade**: API principal para todas operações administrativas do sistema
- **Funcionalidades**:
  - CRUD completo de anúncios de veículos
  - Gestão de usuários e vendedores
  - Controle de permissões baseado em roles (RBAC)
  - Auditoria completa de ações administrativas
  - Endpoints para dashboards e relatórios
  - Upload e gestão de imagens de veículos
  - Integração com sistemas externos
- **Documentação**: [Ver documentação detalhada](../components/backoffice-veiculos-api/index.md)

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
[backoffice-veiculos-api] → Operações CRUD, Validações, Autenticação
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

### Backend (API)
- **Runtime**: Node.js
- **Framework**: Express.js ou NestJS
- **Autenticação**: JWT (JSON Web Tokens)
- **Banco de Dados**: PostgreSQL/MySQL
- **ORM**: Prisma ou TypeORM
- **Validação**: Joi ou class-validator
- **Upload de Arquivos**: Multer
- **Documentação API**: Swagger/OpenAPI

### Ferramentas de Desenvolvimento
- **Controle de Versão**: Git/GitHub
- **CI/CD**: GitHub Actions
- **Containerização**: Docker
- **Monitoramento**: Logs estruturados e APM

## Guia de Navegação

### Documentação dos Componentes
- **[backoffice-veiculos-api](../components/backoffice-veiculos-api/index.md)**: Documentação completa da API principal
  - [Referência da API](../components/backoffice-veiculos-api/api-reference.md): Endpoints, parâmetros e exemplos
  - [Arquitetura](../components/backoffice-veiculos-api/architecture.md): Estrutura técnica e padrões utilizados
  - [Instalação e Configuração](../components/backoffice-veiculos-api/installation.md): Guia de setup e deploy

### Como Usar Esta Documentação
1. **Iniciantes**: Comece pela visão geral do sistema (esta página)
2. **Desenvolvedores**: Consulte a arquitetura e referência da API
3. **DevOps**: Veja o guia de instalação e configuração
4. **Product Owners**: Foque nas funcionalidades principais e perfis de acesso

## Time Responsável

**Squad Backoffice**: Responsável pelo desenvolvimento e manutenção do sistema administrativo interno.