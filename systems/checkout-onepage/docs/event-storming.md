# Event Storming - Checkout Onepage

## Visão Geral

Este documento apresenta o Event Storming do sistema Checkout Onepage, mapeando os eventos de domínio, comandos e agregados que compõem o fluxo de matrícula e pagamento.

## Eventos de Domínio

### Eventos de Produto e Precificação

```mermaid
graph LR
    A[ProdutoConsultado] --> B[PrecificacaoCalculada]
    B --> C[CupomAplicado]
    C --> D[OpcoesParcelamentoDisponibilizadas]
```

- **ProdutoConsultado**: Quando o usuário acessa o checkout e o produto é buscado
- **PrecificacaoCalculada**: Após calcular o preço do produto
- **CupomAplicado**: Quando um cupom é aplicado com sucesso
- **OpcoesParcelamentoDisponibilizadas**: Quando as opções de parcelamento são calculadas

### Eventos de Contato

```mermaid
graph LR
    A[DadosContatoPreenchidos] --> B[ContatoCriado]
    B --> C[DealCriado]
    C --> D[EventoContatoPublicado]
```

- **DadosContatoPreenchidos**: Usuário preenche formulário de contato
- **ContatoCriado**: Contato criado no HubSpot
- **DealCriado**: Deal (negócio) criado no HubSpot
- **EventoContatoPublicado**: Evento publicado na fila SQS

### Eventos de Matrícula

```mermaid
graph LR
    A[DadosMatriculaPreenchidos] --> B[PedidoCriado]
    B --> C[ClienteCriado]
    C --> D[AssociacoesAtualizadas]
    D --> E[DealAtualizado]
```

- **DadosMatriculaPreenchidos**: Usuário preenche dados acadêmicos
- **PedidoCriado**: Pedido criado no Gateway
- **ClienteCriado**: Cliente criado no Gateway
- **AssociacoesAtualizadas**: Associações entre pedido, cliente e produto atualizadas
- **DealAtualizado**: Deal atualizado no HubSpot com informações do pedido

### Eventos de Pagamento

```mermaid
graph LR
    A[MetodoPagamentoSelecionado] --> B[SessaoPagamentoCriada]
    B --> C[PagamentoIniciado]
    C --> D[PagamentoProcessado]
    D --> E{Resultado}
    E -->|Sucesso| F[PagamentoAprovado]
    E -->|Falha| G[PagamentoRecusado]
    F --> H[CompraConfirmada]
    H --> I[DealAtualizadoCompra]
    I --> J[EventoPagamentoPublicado]
```

- **MetodoPagamentoSelecionado**: Usuário seleciona método (cartão, PIX, boleto)
- **SessaoPagamentoCriada**: Sessão criada no Adyen
- **PagamentoIniciado**: Processamento iniciado no Adyen
- **PagamentoProcessado**: Adyen processa o pagamento
- **PagamentoAprovado**: Pagamento aprovado com sucesso
- **PagamentoRecusado**: Pagamento recusado
- **CompraConfirmada**: Compra confirmada no sistema
- **DealAtualizadoCompra**: Deal atualizado com status de compra finalizada
- **EventoPagamentoPublicado**: Evento publicado na fila SQS

### Eventos Assíncronos (Webhooks)

```mermaid
graph LR
    A[WebhookAdyenRecebido] --> B[NotificacaoPagamentoProcessada]
    B --> C[StatusPagamentoAtualizado]
    C --> D[DealAtualizadoStatus]
```

- **WebhookAdyenRecebido**: Webhook recebido do Adyen via SQS
- **NotificacaoPagamentoProcessada**: Notificação processada
- **StatusPagamentoAtualizado**: Status atualizado no Gateway
- **DealAtualizadoStatus**: Deal atualizado no HubSpot com novo status

## Diagrama Completo de Event Storming

```mermaid
graph TB
    subgraph "Jornada do Usuário"
        U1[Usuário acessa checkout]
        U2[Usuário preenche contato]
        U3[Usuário preenche matrícula]
        U4[Usuário seleciona pagamento]
        U5[Usuário finaliza compra]
    end
    
    subgraph "Eventos de Domínio"
        E1[ProdutoConsultado]
        E2[PrecificacaoCalculada]
        E3[ContatoCriado]
        E4[DealCriado]
        E5[PedidoCriado]
        E6[SessaoPagamentoCriada]
        E7[PagamentoAprovado]
        E8[CompraConfirmada]
    end
    
    subgraph "Comandos"
        C1[ConsultarProduto]
        C2[CriarContato]
        C3[CriarMatricula]
        C4[CriarSessaoPagamento]
        C5[ProcessarPagamento]
        C6[ConfirmarCompra]
    end
    
    subgraph "Agregados"
        A1[Produto]
        A2[Contato]
        A3[Pedido]
        A4[Pagamento]
        A5[Deal]
    end
    
    U1 --> C1
    C1 --> E1
    E1 --> A1
    A1 --> E2
    
    U2 --> C2
    C2 --> E3
    E3 --> A2
    A2 --> E4
    E4 --> A5
    
    U3 --> C3
    C3 --> E5
    E5 --> A3
    
    U4 --> C4
    C4 --> E6
    E6 --> A4
    
    U5 --> C5
    C5 --> E7
    E7 --> C6
    C6 --> E8
    E8 --> A5
    
    style E1 fill:#e1f5ff
    style E2 fill:#e1f5ff
    style E3 fill:#e1f5ff
    style E4 fill:#e1f5ff
    style E5 fill:#e1f5ff
    style E6 fill:#e1f5ff
    style E7 fill:#e1f5ff
    style E8 fill:#e1f5ff
    
    style C1 fill:#fff4e1
    style C2 fill:#fff4e1
    style C3 fill:#fff4e1
    style C4 fill:#fff4e1
    style C5 fill:#fff4e1
    style C6 fill:#fff4e1
    
    style A1 fill:#f0f0f0
    style A2 fill:#f0f0f0
    style A3 fill:#f0f0f0
    style A4 fill:#f0f0f0
    style A5 fill:#f0f0f0
```

## Fluxo Temporal de Eventos

```mermaid
sequenceDiagram
    participant U as Usuário
    participant FE as Frontend
    participant BFF as BFF
    participant Pricing as Precificação
    participant Gateway as Gateway
    participant Adyen as Adyen
    participant HubSpot as HubSpot
    participant SQS as SQS

    Note over U,SQS: Fase 1: Consulta de Produto
    U->>FE: Acessa checkout
    FE->>BFF: ConsultarProduto
    BFF->>Pricing: Busca precificação
    Pricing-->>BFF: PrecificacaoCalculada
    BFF-->>FE: ProdutoConsultado
    FE-->>U: Exibe produto

    Note over U,SQS: Fase 2: Cadastro de Contato
    U->>FE: Preenche contato
    FE->>BFF: CriarContato
    BFF->>HubSpot: Cria contato
    HubSpot-->>BFF: ContatoCriado
    BFF->>HubSpot: Cria deal
    HubSpot-->>BFF: DealCriado
    BFF->>SQS: Publica evento
    BFF-->>FE: Sucesso
    FE-->>U: Avança

    Note over U,SQS: Fase 3: Matrícula
    U->>FE: Preenche matrícula
    FE->>BFF: CriarMatricula
    BFF->>Gateway: Cria pedido
    Gateway-->>BFF: PedidoCriado
    BFF->>HubSpot: Atualiza deal
    BFF-->>FE: Sucesso
    FE-->>U: Avança

    Note over U,SQS: Fase 4: Pagamento
    U->>FE: Seleciona método
    FE->>BFF: CriarSessaoPagamento
    BFF->>Gateway: Cria sessão
    Gateway->>Adyen: Inicializa sessão
    Adyen-->>Gateway: SessaoPagamentoCriada
    Gateway-->>BFF: Sessão criada
    BFF-->>FE: Dados da sessão
    FE->>Adyen: Processa pagamento
    Adyen-->>FE: PagamentoAprovado
    FE->>BFF: ConfirmarCompra
    BFF->>Gateway: Confirma
    Gateway-->>BFF: CompraConfirmada
    BFF->>HubSpot: Atualiza deal
    BFF->>SQS: Publica evento
    BFF-->>FE: Sucesso
    FE-->>U: Compra finalizada

    Note over Adyen,SQS: Processamento Assíncrono
    Adyen->>SQS: Webhook recebido
    SQS->>Gateway: Processa notificação
    Gateway->>HubSpot: Atualiza status
```

## Agregados e Entidades

### Agregado: Produto
- **Raiz**: Produto
- **Eventos**: ProdutoConsultado, PrecificacaoCalculada
- **Comandos**: ConsultarProduto

### Agregado: Contato
- **Raiz**: Contato
- **Eventos**: ContatoCriado, DadosContatoPreenchidos
- **Comandos**: CriarContato

### Agregado: Pedido
- **Raiz**: Pedido
- **Eventos**: PedidoCriado, ClienteCriado, AssociacoesAtualizadas
- **Comandos**: CriarMatricula, CriarPedido

### Agregado: Pagamento
- **Raiz**: Pagamento
- **Eventos**: SessaoPagamentoCriada, PagamentoIniciado, PagamentoAprovado, PagamentoRecusado
- **Comandos**: CriarSessaoPagamento, ProcessarPagamento, ConfirmarCompra

### Agregado: Deal (Negócio)
- **Raiz**: Deal
- **Eventos**: DealCriado, DealAtualizado, DealAtualizadoCompra
- **Comandos**: CriarDeal, AtualizarDeal

## Bounded Contexts

```mermaid
graph TB
    subgraph "Bounded Context: Vendas"
        BC1[Checkout Onepage]
        BC2[Precificação]
        BC3[Matrícula]
    end
    
    subgraph "Bounded Context: Pagamentos"
        BC4[Gateway Pagamento]
        BC5[Integração Adyen]
    end
    
    subgraph "Bounded Context: CRM"
        BC6[HubSpot Integration]
        BC7[HubSpot CRM]
    end
    
    BC1 --> BC2
    BC1 --> BC3
    BC1 --> BC4
    BC4 --> BC5
    BC1 --> BC6
    BC6 --> BC7
    
    style BC1 fill:#e1f5ff
    style BC2 fill:#e1f5ff
    style BC3 fill:#e1f5ff
    style BC4 fill:#fff4e1
    style BC5 fill:#fff4e1
    style BC6 fill:#f0f0f0
    style BC7 fill:#f0f0f0
```

## Regras de Negócio

### Precificação
- Deve calcular preço base do produto
- Deve aplicar cupom se fornecido
- Deve calcular opções de parcelamento
- Deve validar instalações disponíveis

### Contato
- Deve validar dados obrigatórios
- Deve criar contato no HubSpot
- Deve criar deal associado
- Deve publicar evento na fila SQS

### Matrícula
- Deve validar dados acadêmicos
- Deve criar pedido no Gateway
- Deve criar cliente no Gateway
- Deve atualizar deal no HubSpot

### Pagamento
- Deve criar sessão no Adyen
- Deve processar pagamento via SDK
- Deve confirmar compra após aprovação
- Deve atualizar deal com status final
- Deve publicar evento na fila SQS

## Eventos de Integração

### Eventos Publicados (SQS)
- `contact.created` - Contato criado
- `deal.created` - Deal criado
- `payment.processed` - Pagamento processado
- `purchase.confirmed` - Compra confirmada

### Eventos Consumidos (SQS)
- `adyen.webhook.notification` - Webhook do Adyen
- `payment.status.updated` - Status de pagamento atualizado

## Considerações de Design

### Event Sourcing
Alguns eventos críticos são persistidos para auditoria e rastreamento:
- Criação de contatos
- Criação de pedidos
- Processamento de pagamentos
- Confirmação de compras

### CQRS
O sistema utiliza separação entre comandos (write) e queries (read):
- **Commands**: CriarContato, CriarMatricula, ProcessarPagamento
- **Queries**: ConsultarProduto, BuscarPrecificacao

### Saga Pattern
O fluxo de checkout implementa um padrão de saga distribuída:
1. Criar Contato → Criar Deal
2. Criar Pedido → Criar Cliente
3. Criar Sessão → Processar Pagamento → Confirmar Compra

Cada etapa pode ser compensada em caso de falha.
