# Arquitetura - Backoffice de Veículos

## Status do Projeto

🚧 **EM DESENVOLVIMENTO** - Esta documentação descreve a arquitetura planejada para o sistema de backoffice de veículos.

## Visão Geral

O sistema de backoffice de veículos é uma solução baseada em arquitetura moderna de aplicações web em desenvolvimento, projetada para gerenciar o cadastro, manutenção e operações relacionadas a veículos. A arquitetura segue os princípios de separação de responsabilidades, baixo acoplamento e alta coesão, garantindo escalabilidade, manutenibilidade e resiliência através de uma arquitetura frontend-backend desacoplada.

## Componentes do Sistema

O sistema é composto por três componentes principais que trabalham de forma integrada:

### 1. backoffice-veiculos-api (API Backend)

API RESTful Node.js/TypeScript responsável pelas operações de backend, gerenciamento de dados e regras de negócio.

**Repositório:** https://github.com/emingues-xx/backoffice-veiculos-api

**Tipo:** Service

**Tecnologias:** Node.js, TypeScript, Express.js, MongoDB

**Responsabilidades:**
- CRUD completo de anúncios de veículos
- Gestão de usuários e vendedores
- Acompanhamento de vendas e métricas
- Autenticação JWT e controle de permissões
- Upload e gerenciamento de imagens
- Integração com sistemas externos

### 2. backoffice-veiculos-bff (Backend For Frontend)

Backend For Frontend Node.js/TypeScript responsável por agregar dados, otimizar requisições e fornecer APIs específicas para o frontend.

**Repositório:** https://github.com/emingues-xx/backoffice-veiculos-bff

**Tipo:** Service

**Tecnologias:** Node.js, TypeScript, Express.js, Redis

**Responsabilidades:**
- Agregação de dados de múltiplas APIs
- Transformação de dados para formato otimizado do frontend
- Cache Redis para melhor performance
- Rate limiting e throttling
- Endpoints customizados para necessidades da aplicação web
- Tratamento de erros e fallbacks

### 3. backoffice-veiculos-web (Frontend Web)

Interface web React/Next.js/TypeScript responsável pela interação do usuário com o sistema.

**Repositório:** https://github.com/emingues-xx/vitrine-veiculos-web

**Tipo:** Website

**Tecnologias:** React, Next.js, TypeScript

**Responsabilidades:**
- Interface responsiva e intuitiva para gestão de anúncios
- Dashboard com métricas e indicadores de vendas
- Formulários de cadastro e edição de veículos
- Sistema de upload e gerenciamento de imagens
- Controle de usuários e permissões
- Relatórios e visualizações de dados

## Diagrama de Arquitetura

### Visão Geral do Sistema (Atual)

```
┌──────────────────────────────────────────────────────────────────┐
│                         Usuários Finais                          │
│              (Administradores, Vendedores, Operadores)           │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            │ HTTPS
                            │
┌───────────────────────────▼──────────────────────────────────────┐
│                   backoffice-veiculos-web                        │
│                      (React/Next.js)                             │
│  ┌────────────────────────────────────────────────────────┐     │
│  │  UI Components Layer                                    │     │
│  │  - Dashboard (Métricas, Gráficos)                      │     │
│  │  - Anúncios (Listagem, Cadastro, Edição)               │     │
│  │  - Vendas (Consulta, Relatórios)                       │     │
│  │  - Usuários (Gestão, Permissões)                       │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  State Management                                       │     │
│  │  - Redux Toolkit/Zustand                               │     │
│  │  - Global State, User Session                          │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  API Client Layer                                       │     │
│  │  - Axios                                               │     │
│  │  - Request/Response Interceptors                       │     │
│  │  - Error Handling, Retry Logic                         │     │
│  └────────────────────────┬───────────────────────────────┘     │
└───────────────────────────┼──────────────────────────────────────┘
                            │
                            │ REST API (JSON)
                            │
┌───────────────────────────▼──────────────────────────────────────┐
│                   backoffice-veiculos-bff                        │
│                     (Backend For Frontend)                       │
│  ┌────────────────────────────────────────────────────────┐     │
│  │  Controllers Layer                                      │     │
│  │  - DashboardController (Métricas, KPIs)                │     │
│  │  - AnunciosController (CRUD de anúncios)               │     │
│  │  - VendasController (Consulta de vendas)               │     │
│  │  - UsuariosController (Gestão de usuários)             │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  Middleware Layer                                       │     │
│  │  - Authentication (JWT Validation)                     │     │
│  │  - Authorization (RBAC)                                │     │
│  │  - Request Validation                                  │     │
│  │  - Error Handling                                      │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  Business Logic Layer (Services)                       │     │
│  │  - DashboardService (Agregação de métricas)            │     │
│  │  - AnunciosService (Lógica de anúncios)                │     │
│  │  - VendasService (Análise de vendas)                   │     │
│  │  - CacheService (Gerenciamento de cache)               │     │
│  └────────────────────────┬───────────────────────────────┘     │
└───────────────────────────┼──────────────────────────────────────┘
                            │
                            │ REST API (JSON)
                            │
┌───────────────────────────▼──────────────────────────────────────┐
│                   backoffice-veiculos-api                        │
│                        (API Backend)                             │
│  ┌────────────────────────────────────────────────────────┐     │
│  │  Controllers Layer                                      │     │
│  │  - AnunciosController (CRUD endpoints)                 │     │
│  │  - VendasController (Gestão de vendas)                 │     │
│  │  - UsuariosController (Gestão de usuários)             │     │
│  │  - AuthController (Autenticação)                       │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  Business Logic Layer (Services)                       │     │
│  │  - AnunciosService (Regras de negócio)                 │     │
│  │  - VendasService (Processamento de vendas)             │     │
│  │  - UsuariosService (Gestão de usuários)                │     │
│  │  - AuthService (Autenticação e autorização)            │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  Data Access Layer                                      │     │
│  │  - AnunciosRepository                                  │     │
│  │  - VendasRepository                                    │     │
│  │  - UsuariosRepository                                  │     │
│  │  - MongoDB Driver                                      │     │
│  └────────────────────────┬───────────────────────────────┘     │
└───────────────────────────┼──────────────────────────────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
┌─────────▼────────┐  ┌─────▼──────┐  ┌──────▼─────────┐
│   Database       │  │   Cache    │  │   Storage      │
│   (MongoDB)      │  │  (Redis)   │  │  (Railway/S3)  │
│                  │  │            │  │                │
│  - anuncios      │  │  - Session │  │  - Images      │
│  - vendas        │  │  - Data    │  │  - Documents   │
│  - usuarios      │  │  - Queries │  │  - Backups     │
└──────────────────┘  └────────────┘  └────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│                      Deploy & CI/CD                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Railway    │  │ GitHub Actions│  │   Docker     │          │
│  │   (Deploy)   │  │   (CI/CD)     │  │ (Container)  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└──────────────────────────────────────────────────────────────────┘
```

## Fluxo de Dados

### 1. Cadastro de Anúncio (Atual)

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Usuário preenche formulário de cadastro de anúncio          │
│    backoffice-veiculos-web                                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ POST /api/anuncios
                         │ { marca, modelo, ano, preco, ... }
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 2. backoffice-veiculos-bff                                      │
│                                                                 │
│    2.1. Authentication Middleware                               │
│         - Valida JWT token                                     │
│         - Verifica permissões (RBAC)                           │
│                                                                 │
│    2.2. Request Validation Middleware                          │
│         - Valida schema da requisição                          │
│         - Sanitiza inputs                                      │
│                                                                 │
│    2.3. AnunciosController.create()                            │
│         - Recebe requisição                                    │
│         - Delega para service                                  │
│                                                                 │
│    2.4. AnunciosService.cadastrarAnuncio()                     │
│         - Valida regras de negócio                             │
│         - Chama API backend                                    │
│                                                                 │
│    2.5. Cache                                                  │
│         - Invalida cache de listagem                           │
│         - Armazena novo anúncio em cache                       │
│                                                                 │
│    2.6. Response                                               │
│         - Status: 201 Created                                  │
│         - Body: { id, marca, modelo, ... }                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ POST /api/anuncios
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 3. backoffice-veiculos-api                                      │
│                                                                 │
│    3.1. Authentication Middleware                               │
│         - Valida JWT token                                     │
│                                                                 │
│    3.2. AnunciosController.create()                            │
│                                                                 │
│    3.3. AnunciosService.cadastrarAnuncio()                     │
│         - Valida regras de negócio:                            │
│           * Dados obrigatórios                                 │
│           * Formato de dados                                   │
│                                                                 │
│    3.4. AnunciosRepository.save()                              │
│         - Persiste no MongoDB                                  │
│         - Retorna anúncio criado com ID                        │
│                                                                 │
│    3.5. Response                                               │
│         - Status: 201 Created                                  │
│         - Body: { id, marca, modelo, ... }                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 4. backoffice-veiculos-web                                      │
│    - Atualiza estado da aplicação                              │
│    - Exibe mensagem de sucesso                                 │
│    - Redireciona para página de detalhes                       │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Consulta de Vendas (Atual)

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Usuário acessa página de vendas                             │
│    backoffice-veiculos-web                                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ GET /api/vendas
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 2. backoffice-veiculos-bff                                      │
│                                                                 │
│    2.1. Authentication & Authorization                          │
│                                                                 │
│    2.2. VendasController.list()                                │
│                                                                 │
│    2.3. VendasService.listarVendas()                           │
│         - Gera cache key baseada nos parâmetros                │
│                                                                 │
│    2.4. Verificação em Cache (Redis)                           │
│         ┌─────────────────────────────────────────┐            │
│         │ Cache HIT?                              │            │
│         │                                         │            │
│         │ SIM:                        NÃO:        │            │
│         │ - Retorna dados do cache    - Chama API │           │
│         │ - Resposta rápida (<10ms)   - Backend   │           │
│         │                             - Popula cache│           │
│         │                             - Retorna dados│          │
│         └─────────────────────────────────────────┘            │
│                                                                 │
│    2.5. Response                                               │
│         - Status: 200 OK                                       │
│         - Body: {                                              │
│             data: [vendas...],                                 │
│             pagination: { page, limit, total }                 │
│           }                                                    │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ GET /api/vendas
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 3. backoffice-veiculos-api                                      │
│                                                                 │
│    3.1. Authentication Middleware                               │
│                                                                 │
│    3.2. VendasController.list()                                │
│                                                                 │
│    3.3. VendasService.listarVendas()                           │
│                                                                 │
│    3.4. VendasRepository.findAll()                             │
│         - Query no MongoDB                                     │
│         - Paginação aplicada                                   │
│         - Filtros e ordenação                                  │
│                                                                 │
│    3.5. Response                                               │
│         - Status: 200 OK                                       │
│         - Body: {                                              │
│             data: [vendas...],                                 │
│             pagination: { page, limit, total }                 │
│           }                                                    │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 4. backoffice-veiculos-web                                      │
│    - Atualiza estado com dados recebidos                       │
│    - Renderiza lista de vendas                                 │
│    - Exibe informações: modelo, comprador, vendedor, valor     │
└─────────────────────────────────────────────────────────────────┘
```

### 3. Atualização de Veículo

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Usuário edita dados do veículo                              │
│    backoffice-veiculos-web                                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ PUT /api/veiculos/:id
                         │ { marca, modelo, ano, ... }
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 2. backoffice-veiculos-bff                                      │
│                                                                 │
│    2.1. Authentication & Authorization                          │
│         - Valida token                                         │
│         - Verifica se usuário pode editar                      │
│                                                                 │
│    2.2. Request Validation                                     │
│         - Valida dados enviados                                │
│                                                                 │
│    2.3. VeiculosController.update()                            │
│                                                                 │
│    2.4. VeiculosService.atualizarVeiculo()                     │
│         - Busca veículo existente                              │
│         - Valida se existe (404 se não)                        │
│         - Aplica regras de negócio:                            │
│           * Campos editáveis                                   │
│           * Validações de domínio                              │
│           * Log de auditoria                                   │
│                                                                 │
│    2.5. VeiculosRepository.update()                            │
│         - Atualiza no banco de dados                           │
│         - Retorna veículo atualizado                           │
│                                                                 │
│    2.6. Cache Invalidation                                     │
│         - Invalida cache do veículo específico                 │
│         - Invalida cache de listagens                          │
│                                                                 │
│    2.7. Event Publishing                                       │
│         - Publica evento: VeiculoAtualizado                    │
│         - Inclui dados antes/depois (audit trail)              │
│                                                                 │
│    2.8. Response                                               │
│         - Status: 200 OK                                       │
│         - Body: veículo atualizado                             │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 3. backoffice-veiculos-web                                      │
│    - Atualiza estado local                                     │
│    - Exibe mensagem de sucesso                                 │
│    - Atualiza UI com novos dados                               │
└─────────────────────────────────────────────────────────────────┘
```

### 4. Integração com Serviços Externos (DETRAN)

```
┌─────────────────────────────────────────────────────────────────┐
│ Validação de Placa via DETRAN                                  │
└─────────────────────────────────────────────────────────────────┘

backoffice-veiculos-bff
        │
        │ IntegrationService.validarPlaca(placa)
        │
        ├─→ 1. Verifica cache (placa já validada?)
        │       │
        │       └─→ Cache HIT: retorna resultado
        │
        └─→ 2. Cache MISS: chama API DETRAN
                │
                ├─→ HTTP Client com:
                │   - Timeout: 5 segundos
                │   - Retry: 3 tentativas
                │   - Circuit Breaker
                │
                ├─→ Response OK:
                │   - Armazena em cache (TTL: 24h)
                │   - Retorna dados validados
                │
                └─→ Response Error:
                    - Log do erro
                    - Fallback: permite cadastro com flag "pendente_validacao"
                    - Retry assíncrono via queue
```

## Padrões Arquiteturais

### 1. BFF Pattern (Backend For Frontend)

O sistema utiliza o padrão BFF, onde o `backoffice-veiculos-bff` é responsável por:
- Agregar dados de múltiplas fontes
- Transformar dados no formato ideal para o frontend
- Reduzir número de chamadas de rede do cliente
- Aplicar lógica específica para o contexto web

**Vantagens:**
- Otimização de performance (menos round-trips)
- Melhor experiência de desenvolvimento frontend
- Evolução independente de frontend e backend
- Redução de acoplamento

### 2. Layered Architecture

**Frontend (backoffice-veiculos-web):**
- **Presentation Layer:** Componentes React/Vue/Angular
- **State Management Layer:** Redux/Vuex/Context API
- **API Client Layer:** Axios/Fetch com interceptors
- **Routing Layer:** React Router/Vue Router

**Backend (backoffice-veiculos-bff):**
- **Controllers Layer:** Recebe requisições HTTP, valida entrada e delega para camada de serviço
- **Middleware Layer:** Autenticação, autorização, validação, logging
- **Business Logic Layer:** Implementa regras de negócio e orquestração
- **Data Access Layer:** Abstração de acesso a dados e persistência
- **Cross-Cutting Concerns:** Logging, autenticação, autorização, tratamento de erros

### 3. Domain-Driven Design (DDD)

Aplicado no BFF para modelagem de domínio rica:

**Entities:**
- **Veiculo:** Entidade principal com identidade única
- **Manutencao:** Histórico de manutenções do veículo
- **Usuario:** Usuários do sistema

**Value Objects:**
- **Placa:** Validação de formato, normalização
- **Chassi:** Validação e unicidade
- **Renavam:** Número de registro único

**Aggregates:**
- **Veiculo Aggregate:** Veículo como aggregate root, contendo manutenções e documentos

**Repositories:**
- Interface para acesso a dados, isolando lógica de persistência

**Domain Services:**
- **ValidationService:** Validações complexas de domínio
- **IntegrationService:** Integrações com APIs externas

### 4. Repository Pattern

Abstração da camada de dados para:
- Facilitar testes unitários (mock de repositories)
- Permitir mudanças de infraestrutura sem impacto no domínio
- Centralizar queries e operações de banco

```typescript
interface VeiculosRepository {
  findById(id: string): Promise<Veiculo | null>;
  findAll(filters: VeiculoFilters): Promise<Veiculo[]>;
  save(veiculo: Veiculo): Promise<Veiculo>;
  update(id: string, data: Partial<Veiculo>): Promise<Veiculo>;
  delete(id: string): Promise<void>;
}
```

### 5. Dependency Injection

Utilização de containers de injeção de dependência (NestJS, TypeDI, InversifyJS):
- Desacoplamento de componentes
- Facilita testes (injeção de mocks)
- Gerenciamento de ciclo de vida de objetos
- Configuração centralizada

### 6. API Gateway Pattern

Camada de entrada única para o sistema:
- Roteamento de requisições
- Rate limiting e throttling
- SSL/TLS termination
- Load balancing
- Autenticação inicial

### 7. Cache-Aside Pattern

Estratégia de cache implementada no BFF:
- Consulta cache primeiro
- Se miss, busca do banco e popula cache
- Invalidação seletiva em operações de escrita
- TTL configurável por tipo de dado

### 8. Circuit Breaker Pattern

Proteção contra falhas em cascata em integrações externas:
- Monitora falhas em chamadas externas
- Abre circuito após threshold de erros
- Half-open state para tentativas de recuperação
- Fallback strategies para degradação graceful

### 9. Event-Driven Architecture

Comunicação assíncrona via eventos:
- Desacoplamento temporal entre componentes
- Processamento assíncrono de operações pesadas
- Auditoria e rastreabilidade
- Integração com outros sistemas

**Eventos publicados:**
- `VeiculoCriado`
- `VeiculoAtualizado`
- `VeiculoRemovido`
- `ManutencaoAgendada`

### 10. CQRS (Command Query Responsibility Segregation)

Separação entre operações de leitura e escrita:
- Queries otimizadas para leitura (views materializadas, cache)
- Commands para operações de escrita com validação completa
- Escalabilidade independente
- Modelos de dados especializados

## Tecnologias Utilizadas

### Frontend (backoffice-veiculos-web) - Em Desenvolvimento

**Core:**
- **Framework:** React/Next.js
- **Linguagem:** TypeScript
- **Build Tool:** Vite/Webpack
- **Package Manager:** npm

**UI/UX:**
- **Component Library:** Material-UI, Ant Design ou Chakra UI
- **Styling:** Tailwind CSS ou Styled Components
- **Icons:** React Icons

**State Management:**
- **Global State:** Redux Toolkit ou Zustand
- **Form State:** React Hook Form

**Routing:**
- **Router:** React Router
- **Dynamic Routing:** Suporte a rotas dinâmicas

**Data Fetching:**
- **HTTP Client:** Axios

**Testing:**
- **Unit Tests:** Jest
- **Component Tests:** React Testing Library

**Code Quality:**
- **Linter:** ESLint
- **Formatter:** Prettier
- **Type Checking:** TypeScript Compiler

### BFF (backoffice-veiculos-bff) - Em Desenvolvimento

**Core:**
- **Linguagem:** Node.js 18+ / TypeScript
- **Framework:** Express.js
- **Runtime:** Node.js

**Cache:**
- **Redis** para cache de dados e sessões

**Validation:**
- **Schema Validation:** Joi ou class-validator

**Authentication & Authorization:**
- **JWT:** jsonwebtoken
- **RBAC:** Controle baseado em roles

**Testing:**
- **Unit Tests:** Jest
- **Integration Tests:** Supertest

**Code Quality:**
- **Linter:** ESLint
- **Formatter:** Prettier

### API Backend (backoffice-veiculos-api) - Em Desenvolvimento

**Core:**
- **Linguagem:** Node.js 18+ / TypeScript
- **Framework:** Express.js
- **Runtime:** Node.js

**Database:**
- **MongoDB** como banco principal
- **MongoDB Driver** para acesso aos dados

**Authentication & Authorization:**
- **JWT:** jsonwebtoken
- **Password Hashing:** bcrypt

**Testing:**
- **Unit Tests:** Jest

**Code Quality:**
- **Linter:** ESLint
- **Formatter:** Prettier

### Infraestrutura e Dados

**Banco de Dados:**
- **MongoDB** como banco principal
  - Documentos JSON
  - Índices para performance
  - Agregações para relatórios

**Cache:**
- **Redis**
  - Key-value storage
  - TTL configurável
  - Cache de sessões

**Storage:**
- **Railway** para deploy e storage
- **AWS S3** (futuro) para imagens

**Deploy:**
- **Railway** para deploy automático
- **Docker** para containerização
- **GitHub Actions** para CI/CD

### Observabilidade

**Logging:**
- **Framework:** Winston / Pino / Bunyan
- **Format:** JSON structured logging
- **Levels:** ERROR, WARN, INFO, DEBUG, TRACE
- **Centralization:**
  - ELK Stack (Elasticsearch, Logstash, Kibana)
  - Datadog
  - CloudWatch Logs
  - Grafana Loki

**Metrics:**
- **Collection:** Prometheus / StatsD
- **Visualization:** Grafana
- **Custom Metrics:** prom-client (Node.js)
- **Dashboards:** Grafana dashboards

**Distributed Tracing:**
- **OpenTelemetry** (padrão open-source)
- **Jaeger** (distributed tracing platform)
- **Zipkin** (alternativa)
- **Datadog APM** (commercial)

**Application Performance Monitoring (APM):**
- **Datadog APM**
- **New Relic**
- **Dynatrace**
- **Elastic APM**

**Error Tracking:**
- **Sentry** (error tracking e monitoring)
- **Rollbar**
- **Bugsnag**

**Uptime Monitoring:**
- **UptimeRobot**
- **Pingdom**
- **StatusCake**
- **Datadog Synthetics**

## Considerações de Segurança

### 1. Autenticação e Autorização

**JWT (JSON Web Tokens):**
- **Access Token:** Curta duração (15 minutos)
- **Refresh Token:** Longa duração (7 dias), armazenado em httpOnly cookie
- **Token Rotation:** Renovação automática de tokens
- **Token Revocation:** Lista negra em Redis para tokens revogados
- **Claims:** userId, roles, permissions, iat, exp

**RBAC (Role-Based Access Control):**
```typescript
Roles:
  - ADMIN: Acesso completo ao sistema
  - GESTOR: Gestão de veículos e relatórios
  - OPERADOR: Visualização e edição limitada
  - LEITOR: Apenas visualização

Permissions:
  - veiculos:create
  - veiculos:read
  - veiculos:update
  - veiculos:delete
  - relatorios:generate
  - usuarios:manage
```

**Implementação:**
- Middleware de autenticação valida JWT em cada requisição
- Middleware de autorização verifica permissões por endpoint
- Decorators para proteção de rotas (NestJS: @Roles, @Permissions)

**Rate Limiting:**
- **Por IP:** 100 requisições/minuto
- **Por Usuário:** 500 requisições/minuto
- **Por Endpoint Sensível:** 10 requisições/minuto (ex: login, reset password)
- **Implementação:** Redis com sliding window counter

### 2. Segurança de Dados

**Criptografia em Repouso:**
- Dados sensíveis criptografados com AES-256
- Chaves gerenciadas via KMS (AWS KMS, Azure Key Vault, HashiCorp Vault)
- Campos criptografados: CPF, CNH, dados bancários
- Hash de senhas com bcrypt (cost factor: 12) ou argon2

**Criptografia em Trânsito:**
- TLS 1.3 obrigatório em produção
- Certificados válidos (Let's Encrypt, CA confiável)
- HSTS (HTTP Strict Transport Security) habilitado
- Upgrade automático de HTTP para HTTPS

**Proteção contra Injeções:**
- **SQL Injection:** Uso de prepared statements via ORM
- **NoSQL Injection:** Validação e sanitização de queries
- **Command Injection:** Sanitização de inputs para comandos shell
- **LDAP Injection:** Escape de caracteres especiais

**Proteção XSS (Cross-Site Scripting):**
- Sanitização de inputs no frontend e backend
- Content Security Policy (CSP) configurado
- Escape de HTML em templates
- httpOnly cookies para tokens

**Proteção CSRF (Cross-Site Request Forgery):**
- CSRF tokens em formulários
- SameSite cookie attribute
- Validação de Origin/Referer headers

### 3. Segurança de API

**CORS (Cross-Origin Resource Sharing):**
```typescript
CORS Configuration:
  - origin: ['https://backoffice.example.com']
  - methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']
  - allowedHeaders: ['Content-Type', 'Authorization']
  - credentials: true
  - maxAge: 86400
```

**Security Headers (Helmet.js):**
```typescript
Headers aplicados:
  - X-Content-Type-Options: nosniff
  - X-Frame-Options: DENY
  - X-XSS-Protection: 1; mode=block
  - Strict-Transport-Security: max-age=31536000; includeSubDomains
  - Content-Security-Policy: default-src 'self'
  - Referrer-Policy: strict-origin-when-cross-origin
```

**Input Validation:**
- Validação de schema em todas as requisições (Joi, Zod, class-validator)
- Whitelist de campos permitidos
- Validação de tipos, formatos e ranges
- Rejeição de dados malformados (400 Bad Request)

**API Rate Limiting:**
- Implementação com Redis + sliding window
- Headers de resposta:
  - X-RateLimit-Limit
  - X-RateLimit-Remaining
  - X-RateLimit-Reset
- Resposta 429 (Too Many Requests) quando excedido

**DDoS Protection:**
- Rate limiting agressivo
- API Gateway com WAF (Web Application Firewall)
- CloudFlare / AWS Shield
- IP blacklisting automático

### 4. Compliance e Auditoria

**LGPD (Lei Geral de Proteção de Dados):**
- Consentimento explícito para coleta de dados
- Direito de acesso, correção e exclusão de dados
- Anonimização de dados pessoais em logs e backups
- Data retention policies configuráveis
- Relatórios de dados pessoais por titular

**Auditoria de Operações:**
```typescript
Audit Log Schema:
  - timestamp: Data/hora da operação
  - userId: ID do usuário
  - action: CREATE | UPDATE | DELETE | READ
  - resource: veiculos, usuarios, etc
  - resourceId: ID do recurso afetado
  - changes: Dados antes/depois (diff)
  - ip: IP de origem
  - userAgent: User agent do cliente
```

**Retenção de Logs:**
- Logs de auditoria: 7 anos (conformidade legal)
- Logs de aplicação: 90 dias
- Logs de acesso: 1 ano
- Arquivamento em cold storage após período ativo

**Backup e Recuperação:**
- Backups diários automatizados
- Retenção: 30 dias (daily), 12 semanas (weekly), 12 meses (monthly)
- Backup criptografado (AES-256)
- Testes de restore mensais
- RTO (Recovery Time Objective): 4 horas
- RPO (Recovery Point Objective): 24 horas

### 5. Segurança de Dependências

**Vulnerability Scanning:**
- `npm audit` em CI/CD pipeline
- Snyk / Dependabot para detecção de vulnerabilidades
- Renovate bot para atualização automática de dependências
- Bloqueio de merge com vulnerabilidades críticas

**Supply Chain Security:**
- Verificação de checksums de pacotes
- Uso de lock files (package-lock.json, yarn.lock)
- Audit de pacotes antes de adicionar
- Preferência por pacotes com boa manutenção

### 6. Segurança de Infraestrutura

**Network Security:**
- VPC (Virtual Private Cloud) isolada
- Security Groups / Network ACLs
- Banco de dados em subnet privada (sem acesso público)
- Bastion host para acesso administrativo

**Secrets Management:**
- Secrets armazenados em vault (AWS Secrets Manager, HashiCorp Vault)
- Nunca commitar secrets no código
- Rotação automática de secrets (senhas de BD, API keys)
- Variáveis de ambiente para configuração

**Container Security:**
- Base images oficiais e atualizadas
- Scan de vulnerabilidades em images (Trivy, Clair)
- Non-root user em containers
- Read-only filesystem quando possível
- Resource limits (CPU, memória)

## Considerações de Performance

### Otimizações
- **Cache em múltiplas camadas:**
  - Cache de aplicação (Redis)
  - Cache de queries (ORM)
  - Cache HTTP (CDN)

- **Indexação de banco de dados:**
  - Índices em colunas frequentemente consultadas
  - Índices compostos para queries complexas
  - Análise periódica de query plans

- **Paginação:**
  - Cursor-based pagination para grandes volumes
  - Limite máximo de resultados por página

- **Lazy Loading:**
  - Carregamento sob demanda de relacionamentos
  - Eager loading configurável

### Escalabilidade
- **Horizontal Scaling:** Múltiplas instâncias da API atrás de load balancer
- **Database Read Replicas:** Réplicas de leitura para distribuir carga
- **Connection Pooling:** Pool de conexões configurado adequadamente
- **Async Processing:** Operações pesadas processadas via filas

### Monitoramento de Performance
- SLO de 99.9% de disponibilidade
- Latência P95 < 500ms
- Latência P99 < 1000ms
- Alertas automáticos para degradação

## Estratégias de Deploy

### CI/CD Pipeline

```
Code Push → Git Repository
              ↓
          Webhook Trigger
              ↓
      ┌───────────────────┐
      │   CI Pipeline     │
      │  - Lint           │
      │  - Unit Tests     │
      │  - Build          │
      │  - Security Scan  │
      └────────┬──────────┘
               ↓
      ┌───────────────────┐
      │  Docker Build     │
      │  - Build Image    │
      │  - Push to Registry│
      └────────┬──────────┘
               ↓
      ┌───────────────────┐
      │ CD Pipeline       │
      │  - Deploy to Dev  │
      │  - Integration Tests│
      │  - Deploy to Staging│
      │  - E2E Tests      │
      │  - Deploy to Prod │
      └───────────────────┘
```

### Ambientes

#### Desenvolvimento (Dev)
- Deploy automático em cada push para branch de desenvolvimento
- Dados de teste sintéticos
- Configurações de debug habilitadas

#### Staging
- Espelho do ambiente de produção
- Deploy automático após aprovação em Dev
- Testes de integração e E2E
- Dados anonimizados de produção

#### Produção
- Deploy manual ou automatizado após aprovação
- Blue-Green Deployment ou Canary Release
- Rollback automático em caso de falhas
- Monitoramento intensivo pós-deploy

### Estratégias de Deploy

#### Blue-Green Deployment
- Dois ambientes idênticos (Blue e Green)
- Deploy no ambiente inativo
- Switch de tráfego após validação
- Rollback instantâneo em caso de problemas

#### Canary Release
- Deploy gradual para percentual de usuários
- Monitoramento de métricas durante rollout
- Aumento progressivo de tráfego
- Rollback automático se métricas degradarem

### Containerização
- **Docker:** Containers para aplicação
- **Kubernetes:** Orquestração de containers
- **Helm:** Gerenciamento de deployments
- **Docker Compose:** Ambiente local

## Monitoramento e Observabilidade

### Métricas de Negócio
- Total de veículos cadastrados
- Veículos ativos vs inativos
- Taxa de criação de veículos por período
- Erros de validação mais comuns

### Métricas Técnicas
- Request rate (req/s)
- Error rate (%)
- Response time (P50, P95, P99)
- CPU e memória utilizados
- Database connection pool usage
- Cache hit/miss ratio

### Logging
- **Structured Logging:** JSON format
- **Log Levels:** ERROR, WARN, INFO, DEBUG
- **Correlation IDs:** Rastreamento de requisições
- **Centralização:** ELK Stack / Datadog / CloudWatch

### Alertas
- **Disponibilidade:** Downtime > 1 minuto
- **Performance:** Latência P95 > 1s
- **Erros:** Error rate > 5%
- **Infraestrutura:** CPU > 80%, Memória > 85%
- **Segurança:** Tentativas de acesso não autorizadas

### Dashboards
- **Visão Operacional:** Status dos serviços, latência, erros
- **Visão de Negócio:** KPIs, métricas de uso
- **Visão de Infraestrutura:** Recursos, custos
- **SLA Dashboard:** Disponibilidade, tempo de resposta

## Estratégias de Resiliência

### Circuit Breaker
- Proteção contra falhas em cascata
- Timeout configurável por operação
- Fallback strategies

### Retry Policies
- Exponential backoff
- Jitter para evitar thundering herd
- Limite máximo de tentativas

### Health Checks
- Liveness probe: Serviço está rodando
- Readiness probe: Serviço está pronto para receber tráfego
- Dependency checks: Banco de dados, cache, filas

### Graceful Shutdown
- Drenagem de conexões ativas
- Finalização de requisições em andamento
- Timeout máximo de shutdown

## Status Atual do Desenvolvimento

### 🚧 Componentes em Desenvolvimento

#### backoffice-veiculos-api
- **Status:** Estrutura básica implementada
- **Funcionalidades:** CRUD de anúncios, autenticação JWT, gestão de usuários
- **Tecnologias:** Node.js, TypeScript, Express.js, MongoDB
- **Deploy:** Railway
- **Próximos passos:** Implementação completa de vendas e relatórios

#### backoffice-veiculos-bff
- **Status:** Estrutura básica implementada
- **Funcionalidades:** Agregação de dados, cache Redis, endpoints otimizados
- **Tecnologias:** Node.js, TypeScript, Express.js, Redis
- **Deploy:** Railway
- **Próximos passos:** Implementação de métricas e dashboards

#### backoffice-veiculos-web
- **Status:** Interface básica implementada
- **Funcionalidades:** Listagem de vendas, navegação, autenticação
- **Tecnologias:** React, Next.js, TypeScript
- **Deploy:** Railway
- **Próximos passos:** Dashboard completo, formulários de cadastro, relatórios

### ✅ Funcionalidades Implementadas
- Listagem básica de vendas
- Autenticação JWT
- Navegação entre páginas
- Estrutura de componentes

### 🚧 Funcionalidades em Desenvolvimento
- Dashboard com métricas
- Cadastro de anúncios
- Relatórios de vendas
- Gestão de usuários
- Upload de imagens

### 📋 Próximas Implementações
- Filtros avançados de vendas
- Exportação de relatórios
- Notificações em tempo real
- Analytics avançado
- Mobile responsiveness