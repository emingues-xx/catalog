# Sistema Backoffice de Veículos

O **Backoffice de Veículos** é o sistema interno para cadastro de anúncios, dashboard administrativo e acompanhamento de vendas.

## Visão Geral

Sistema administrativo que permite aos operadores e vendedores gerenciar anúncios de veículos, acompanhar métricas de vendas e administrar a plataforma de forma eficiente.

## Componentes

### Frontend (backoffice-veiculos-web)
- **Tecnologia**: React/Next.js
- **Responsabilidade**: Interface administrativa
- **Funcionalidades**:
  - Dashboard executivo
  - Cadastro de anúncios
  - Gestão de usuários
  - Relatórios e métricas

### API (backoffice-veiculos-api)  
- **Tecnologia**: Node.js
- **Responsabilidade**: API para operações administrativas
- **Funcionalidades**:
  - CRUD de anúncios
  - Gestão de usuários
  - Controle de permissões
  - Auditoria de ações

### BFF (backoffice-veiculos-bff)
- **Tecnologia**: Node.js  
- **Responsabilidade**: Backend for Frontend administrativo
- **Funcionalidades**:
  - Agregação de dashboards
  - Relatórios consolidados
  - Cache de métricas

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

## Integrações

- **Sistema de Pagamentos**: Para controle financeiro
- **CRM**: Sincronização de leads e vendas  
- **Sistema de Notificações**: E-mail e push notifications
- **Analytics**: Integração com ferramentas de BI

## Time Responsável

**Squad Backoffice**: Responsável pelo desenvolvimento e manutenção do sistema administrativo interno.