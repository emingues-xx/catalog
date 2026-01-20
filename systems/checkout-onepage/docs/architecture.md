# Arquitetura do Sistema Checkout Onepage

## Visão Geral

O Checkout Onepage é uma solução frontend que integra múltiplos serviços para proporcionar uma experiência fluida de matrícula e pagamento para instituições de ensino. O sistema gerencia todo o fluxo desde a seleção do produto até a finalização do pagamento.

## Diagrama de Arquitetura

```mermaid
graph TB
    subgraph "Frontend Layer"
        FE[Frontend Next.js<br/>checkout-onepage-hub-vendas-frontend]
    end
    
    subgraph "BFF Layer"
        BFF[BFF Sales<br/>back-hub-bff-sales]
    end
    
    subgraph "Backend Services"
        PRICING[Precificação<br/>precificacao-hub-vendas-backend]
        GATEWAY[Gateway Pagamento<br/>gateway-pagamento-hub-vendas-backend]
        HUBSPOT_INT[HubSpot Integration<br/>hubspot-integration-hub-vendas-backend]
        ADYEN_INT[Adyen Integration<br/>integracao-adyen-hub-vendas-backend]
    end
    
    subgraph "External Services"
        ADYEN[Adyen Payment Gateway]
        HUBSPOT[HubSpot CRM]
        AWS_SQS[AWS SQS]
    end
    
    subgraph "AWS Infrastructure"
        SSM[AWS SSM<br/>Parameter Store]
    end
    
    FE -->|API Proxy| BFF
    BFF -->|Product Pricing| PRICING
    BFF -->|Payment Session| GATEWAY
    BFF -->|Contact/Deal| HUBSPOT_INT
    BFF -->|Events| AWS_SQS
    
    GATEWAY -->|Payment Processing| ADYEN_INT
    ADYEN_INT -->|Payment API| ADYEN
    HUBSPOT_INT -->|CRM API| HUBSPOT
    
    ADYEN -->|Webhooks| AWS_SQS
    AWS_SQS -->|Events| GATEWAY
    AWS_SQS -->|Events| HUBSPOT_INT
    
    FE -->|Config| SSM
    
    style FE fill:#e1f5ff
    style BFF fill:#fff4e1
    style PRICING fill:#f0f0f0
    style GATEWAY fill:#f0f0f0
    style HUBSPOT_INT fill:#f0f0f0
    style ADYEN_INT fill:#f0f0f0
    style ADYEN fill:#ffe1f5
    style HUBSPOT fill:#ffe1f5
    style AWS_SQS fill:#ffe1f5
    style SSM fill:#ffe1f5
```

## Fluxo de Dados Detalhado

```mermaid
sequenceDiagram
    participant User as Usuário
    participant FE as Frontend Next.js
    participant BFF as BFF Sales
    participant Pricing as Precificação
    participant Gateway as Gateway Pagamento
    participant Adyen as Adyen Gateway
    participant HubSpot as HubSpot Integration
    participant SQS as AWS SQS
    participant HubSpotCRM as HubSpot CRM

    User->>FE: Acessa checkout com productId
    FE->>BFF: GET /product/checkout-onepage/{id}/pricing
    BFF->>Pricing: Busca precificação do produto
    Pricing-->>BFF: Retorna preço e opções de parcelamento
    BFF-->>FE: Dados do produto e precificação
    FE-->>User: Exibe produto e preços

    User->>FE: Preenche dados de contato
    FE->>BFF: POST /contact-deal
    BFF->>HubSpot: Cria contato e deal
    BFF->>SQS: Publica evento de contato criado
    HubSpot-->>BFF: Contato e deal criados
    BFF-->>FE: Sucesso
    FE-->>User: Avança para matrícula

    User->>FE: Preenche dados de matrícula
    FE->>BFF: POST /enrollment
    BFF->>Gateway: Cria pedido/cliente
    Gateway-->>BFF: Pedido criado
    BFF->>HubSpot: Atualiza deal com pedido
    BFF-->>FE: Matrícula criada
    FE-->>User: Avança para pagamento

    User->>FE: Seleciona método de pagamento
    FE->>BFF: POST /payments/sessions
    BFF->>Gateway: Cria sessão de pagamento
    Gateway->>Adyen: Inicializa sessão
    Adyen-->>Gateway: Session data
    Gateway-->>BFF: Dados da sessão
    BFF-->>FE: Session data
    FE->>Adyen: Processa pagamento (SDK)
    Adyen-->>FE: Resultado do pagamento
    FE->>BFF: POST /payments/confirm
    BFF->>Gateway: Confirma pagamento
    BFF->>HubSpot: Atualiza deal (compra finalizada)
    BFF->>SQS: Publica evento de pagamento
    BFF-->>FE: Pagamento confirmado
    FE-->>User: Redireciona para tela de obrigado

    Note over Adyen,SQS: Webhooks assíncronos
    Adyen->>SQS: Webhook de notificação
    SQS->>Gateway: Processa notificação
    Gateway->>HubSpot: Atualiza status do pagamento
```

## Componentes Principais

### Frontend (Next.js)
- **Framework**: Next.js 15.2.4
- **Linguagem**: TypeScript
- **UI**: Material UI v7 + Styled Components
- **State Management**: React Context + TanStack React Query
- **Formulários**: React Hook Form + Zod
- **Payment SDK**: Adyen Web SDK

### BFF (Backend For Frontend)
- **Framework**: NestJS
- **Função**: Orquestração de chamadas para múltiplos serviços
- **Endpoints Principais**:
  - `/product/checkout-onepage/{id}/pricing` - Precificação
  - `/contact-deal` - Criação de contato e deal
  - `/enrollment` - Processamento de matrícula
  - `/payments/sessions` - Criação de sessão de pagamento
  - `/payments/confirm` - Confirmação de pagamento

### Serviços Backend

#### Precificação
- Calcula preços do produto
- Aplica cupons e descontos
- Retorna opções de parcelamento

#### Gateway de Pagamento
- Gerencia pedidos e clientes
- Integra com Adyen
- Processa webhooks de pagamento

#### HubSpot Integration
- Cria e atualiza contatos
- Gerencia deals (negócios)
- Sincroniza estágios de pedido

#### Adyen Integration
- Processa pagamentos
- Gerencia sessões de pagamento
- Processa notificações assíncronas

## Fluxo de Jornada do Usuário

```mermaid
stateDiagram-v2
    [*] --> SelecaoProduto: Acesso ao checkout
    SelecaoProduto --> CadastroContato: Produto carregado
    CadastroContato --> Matricula: Contato criado
    Matricula --> Pagamento: Matrícula processada
    Pagamento --> ProcessandoPagamento: Método selecionado
    ProcessandoPagamento --> PagamentoConfirmado: Pagamento aprovado
    ProcessandoPagamento --> PagamentoRecusado: Pagamento recusado
    PagamentoConfirmado --> CompraFinalizada: Redirecionamento
    PagamentoRecusado --> Pagamento: Retry
    CompraFinalizada --> [*]
```

## Tecnologias e Integrações

### Frontend
- Next.js 15.2.4
- TypeScript
- Material UI v7
- Styled Components
- TanStack React Query
- React Hook Form + Zod
- Adyen Web SDK
- AWS SDK (SSM)

### Backend
- NestJS
- AWS SQS
- AWS SSM Parameter Store

### Integrações Externas
- **Adyen**: Gateway de pagamento (cartão, PIX, boleto)
- **HubSpot**: CRM para gestão de contatos e deals
- **AWS SQS**: Fila de mensagens para eventos assíncronos
- **AWS SSM**: Armazenamento de parâmetros de configuração

## Padrões Arquiteturais

### BFF Pattern
O Backend For Frontend (BFF) atua como uma camada de orquestração, agregando chamadas para múltiplos serviços backend e fornecendo uma API unificada otimizada para o frontend.

### Event-Driven Architecture
Eventos assíncronos são publicados via SQS para processamento posterior, permitindo desacoplamento entre serviços.

### API Proxy Pattern
O frontend utiliza um proxy API route do Next.js para fazer chamadas ao BFF, centralizando configuração e headers.

## Segurança

- Headers de correlação (`x-correlation-id`) para rastreamento
- Validação de headers obrigatórios (`ie-id`)
- Integração segura com Adyen via SDK oficial
- Parâmetros sensíveis armazenados no AWS SSM

## Monitoramento

- Datadog APM para rastreamento de performance
- Datadog Logs para análise de logs
- Correlation IDs para rastreamento de requisições
- Logging estruturado em todos os serviços
