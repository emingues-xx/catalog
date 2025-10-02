# Arquitetura - Backoffice de Veículos

## Visão Geral

O sistema de backoffice de veículos é uma solução baseada em arquitetura moderna de aplicações web, projetada para gerenciar o cadastro, manutenção e operações relacionadas a veículos. A arquitetura segue os princípios de separação de responsabilidades, baixo acoplamento e alta coesão, garantindo escalabilidade, manutenibilidade e resiliência através de uma arquitetura frontend-backend desacoplada.

## Componentes do Sistema

O sistema é composto por dois componentes principais que trabalham de forma integrada:

### backoffice-veiculos-bff (Backend For Frontend)

Backend For Frontend responsável por fornecer APIs REST otimizadas para o frontend, agregando dados, aplicando regras de negócio e gerenciando integrações com sistemas externos.

**Repositório:** https://github.com/emingues-xx/backoffice-veiculos-bff.git

**Tipo:** Application (BFF)

**Responsabilidades:**
- Gerenciamento do ciclo de vida de veículos
- Validação de regras de negócio
- Exposição de endpoints REST otimizados para o frontend
- Agregação de dados de múltiplas fontes
- Integração com banco de dados e serviços externos
- Autenticação e autorização de usuários
- Transformação de dados para o formato do frontend

### backoffice-veiculos-web

Interface web responsável pela interação do usuário com o sistema, fornecendo uma experiência moderna e responsiva para gestão de veículos.

**Repositório:** https://github.com/emingues-xx/backoffice-veiculos-web.git

**Tipo:** Web Frontend

**Responsabilidades:**
- Interface de usuário responsiva e moderna
- Formulários de cadastro e edição de veículos
- Visualização de listagens e detalhes
- Validação de dados no cliente
- Gestão de estado da aplicação
- Comunicação com o BFF via REST API
- Experiência do usuário (UX) otimizada

## Diagrama de Arquitetura

### Visão Geral do Sistema

```
┌──────────────────────────────────────────────────────────────────┐
│                         Usuários Finais                          │
│              (Gestores de Frota, Operadores)                     │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            │ HTTPS
                            │
┌───────────────────────────▼──────────────────────────────────────┐
│                   backoffice-veiculos-web                        │
│                      (Web Frontend)                              │
│  ┌────────────────────────────────────────────────────────┐     │
│  │  UI Components Layer                                    │     │
│  │  - Pages (Listagem, Cadastro, Edição, Detalhes)        │     │
│  │  - Components (Forms, Tables, Modals, Cards)           │     │
│  │  - Layouts (Dashboard, Auth)                           │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  State Management                                       │     │
│  │  - Redux/Context API/Zustand                           │     │
│  │  - Global State, User Session, Cache                   │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  API Client Layer                                       │     │
│  │  - Axios/Fetch                                         │     │
│  │  - Request/Response Interceptors                       │     │
│  │  - Error Handling, Retry Logic                         │     │
│  └────────────────────────┬───────────────────────────────┘     │
└───────────────────────────┼──────────────────────────────────────┘
                            │
                            │ REST API (JSON)
                            │
┌───────────────────────────▼──────────────────────────────────────┐
│                   API Gateway / Load Balancer                    │
│                   (NGINX / AWS ALB / Kong)                       │
│  - Rate Limiting                                                 │
│  - SSL Termination                                               │
│  - Request Routing                                               │
└───────────────────────────┬──────────────────────────────────────┘
                            │
                            │
┌───────────────────────────▼──────────────────────────────────────┐
│                   backoffice-veiculos-bff                        │
│                     (Backend For Frontend)                       │
│  ┌────────────────────────────────────────────────────────┐     │
│  │  Controllers Layer                                      │     │
│  │  - VeiculosController (CRUD endpoints)                 │     │
│  │  - ManutencaoController (Manutenção de veículos)       │     │
│  │  - RelatoriosController (Relatórios e dashboards)      │     │
│  │  - AuthController (Autenticação e autorização)         │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  Middleware Layer                                       │     │
│  │  - Authentication (JWT Validation)                     │     │
│  │  - Authorization (RBAC)                                │     │
│  │  - Request Validation                                  │     │
│  │  - Logging & Tracing                                   │     │
│  │  - Error Handling                                      │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  Business Logic Layer (Services)                       │     │
│  │  - VeiculosService (Lógica de negócio de veículos)    │     │
│  │  - ValidationService (Validações complexas)            │     │
│  │  - IntegrationService (Integrações externas)           │     │
│  │  - NotificationService (Notificações)                  │     │
│  │  - ReportService (Geração de relatórios)               │     │
│  └────────────────────────┬───────────────────────────────┘     │
│                           │                                      │
│  ┌────────────────────────▼───────────────────────────────┐     │
│  │  Data Access Layer                                      │     │
│  │  - VeiculosRepository                                  │     │
│  │  - ManutencaoRepository                                │     │
│  │  - ORM/Query Builder (TypeORM/Prisma/Sequelize)       │     │
│  │  - Database Migrations                                 │     │
│  └────────────────────────┬───────────────────────────────┘     │
└───────────────────────────┼──────────────────────────────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
┌─────────▼────────┐  ┌─────▼──────┐  ┌──────▼─────────┐
│   Database       │  │   Cache    │  │  Message Queue │
│  (PostgreSQL)    │  │  (Redis)   │  │  (RabbitMQ/    │
│                  │  │            │  │   AWS SQS)     │
│  - veiculos      │  │  - Session │  │                │
│  - manutencoes   │  │  - Data    │  │  - Events      │
│  - usuarios      │  │  - Queries │  │  - Async Jobs  │
└──────────────────┘  └────────────┘  └────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│                      Serviços Externos                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   DETRAN     │  │   RENAVAM    │  │  Sistema de  │          │
│  │     API      │  │     API      │  │   Frotas     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└──────────────────────────────────────────────────────────────────┘
```

## Fluxo de Dados

### 1. Cadastro de Veículo

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Usuário preenche formulário de cadastro                     │
│    backoffice-veiculos-web                                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ POST /api/veiculos
                         │ { placa, marca, modelo, ano, ... }
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 2. API Gateway                                                  │
│    - Validação de rate limiting                                │
│    - SSL/TLS termination                                       │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 3. backoffice-veiculos-bff                                      │
│                                                                 │
│    3.1. Authentication Middleware                               │
│         - Valida JWT token                                     │
│         - Verifica permissões (RBAC)                           │
│                                                                 │
│    3.2. Request Validation Middleware                          │
│         - Valida schema da requisição                          │
│         - Sanitiza inputs                                      │
│                                                                 │
│    3.3. VeiculosController.create()                            │
│         - Recebe requisição                                    │
│         - Delega para service                                  │
│                                                                 │
│    3.4. VeiculosService.cadastrarVeiculo()                     │
│         - Valida regras de negócio:                            │
│           * Placa única                                        │
│           * Dados obrigatórios                                 │
│           * Formato de dados                                   │
│         - Integra com serviços externos (DETRAN)               │
│         - Enriquece dados do veículo                           │
│                                                                 │
│    3.5. VeiculosRepository.save()                              │
│         - Persiste no banco de dados                           │
│         - Retorna veículo criado com ID                        │
│                                                                 │
│    3.6. Cache                                                  │
│         - Invalida cache de listagem                           │
│         - Armazena novo veículo em cache                       │
│                                                                 │
│    3.7. Event Publishing                                       │
│         - Publica evento: VeiculoCriado                        │
│         - Para processamento assíncrono                        │
│                                                                 │
│    3.8. Response                                               │
│         - Status: 201 Created                                  │
│         - Body: { id, placa, marca, ... }                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 4. backoffice-veiculos-web                                      │
│    - Atualiza estado da aplicação                              │
│    - Exibe mensagem de sucesso                                 │
│    - Redireciona para página de detalhes                       │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Consulta de Veículo

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Usuário acessa listagem de veículos                         │
│    backoffice-veiculos-web                                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         │ GET /api/veiculos?page=1&limit=20
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 2. backoffice-veiculos-bff                                      │
│                                                                 │
│    2.1. Authentication & Authorization                          │
│                                                                 │
│    2.2. VeiculosController.list()                              │
│                                                                 │
│    2.3. VeiculosService.listarVeiculos()                       │
│         - Gera cache key baseada nos parâmetros                │
│                                                                 │
│    2.4. Verificação em Cache (Redis)                           │
│         ┌─────────────────────────────────────────┐            │
│         │ Cache HIT?                              │            │
│         │                                         │            │
│         │ SIM:                        NÃO:        │            │
│         │ - Retorna dados do cache    - Consulta BD│           │
│         │ - Resposta rápida (<10ms)   - Repository │           │
│         │                             - Popula cache│           │
│         │                             - Retorna dados│          │
│         └─────────────────────────────────────────┘            │
│                                                                 │
│    2.5. VeiculosRepository.findAll()                           │
│         - Query otimizada com índices                          │
│         - Paginação aplicada                                   │
│         - Filtros e ordenação                                  │
│                                                                 │
│    2.6. Response                                               │
│         - Status: 200 OK                                       │
│         - Body: {                                              │
│             data: [...],                                       │
│             pagination: { page, limit, total }                 │
│           }                                                    │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 3. backoffice-veiculos-web                                      │
│    - Atualiza estado com dados recebidos                       │
│    - Renderiza tabela de veículos                              │
│    - Exibe paginação                                           │
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

### Frontend (backoffice-veiculos-web)

**Core:**
- **Framework:** React 18+ / Vue 3+ / Angular 15+
- **Linguagem:** TypeScript 5+
- **Build Tool:** Vite / Webpack / esbuild
- **Package Manager:** npm / yarn / pnpm

**UI/UX:**
- **Component Library:** Material-UI / Ant Design / Chakra UI / Tailwind CSS
- **Styling:** CSS Modules / Styled Components / Emotion
- **Icons:** React Icons / Font Awesome / Material Icons

**State Management:**
- **Global State:** Redux Toolkit / Zustand / Jotai / Recoil
- **Server State:** React Query / SWR / Apollo Client
- **Form State:** React Hook Form / Formik

**Routing:**
- **Router:** React Router v6 / Vue Router / Angular Router
- **Dynamic Routing:** Suporte a rotas dinâmicas e lazy loading

**Data Fetching:**
- **HTTP Client:** Axios / Fetch API
- **GraphQL Client:** Apollo Client (se aplicável)

**Testing:**
- **Unit Tests:** Jest / Vitest
- **Component Tests:** React Testing Library / Vue Test Utils
- **E2E Tests:** Cypress / Playwright
- **Visual Regression:** Storybook + Chromatic

**Code Quality:**
- **Linter:** ESLint
- **Formatter:** Prettier
- **Type Checking:** TypeScript Compiler
- **Git Hooks:** Husky + lint-staged

### Backend (backoffice-veiculos-bff)

**Core:**
- **Linguagem:** Node.js 18+ / TypeScript 5+
- **Framework:** NestJS / Express.js / Fastify / Koa
- **Runtime:** Node.js / Bun / Deno

**Database:**
- **ORM/Query Builder:**
  - TypeORM (completo, com migrations e relations)
  - Prisma (type-safe, developer experience)
  - Sequelize (maduro, amplamente utilizado)
  - Drizzle ORM (performático, type-safe)
- **Migrations:** Gerenciamento via ORM ou Flyway
- **Seeding:** Scripts de dados iniciais

**Validation:**
- **Schema Validation:** Joi / Yup / Zod / class-validator
- **DTO Validation:** class-validator + class-transformer (NestJS)

**Authentication & Authorization:**
- **JWT:** jsonwebtoken / @nestjs/jwt
- **Password Hashing:** bcrypt / argon2
- **OAuth 2.0:** Passport.js strategies
- **RBAC:** Custom middleware / CASL

**Testing:**
- **Unit Tests:** Jest / Vitest
- **Integration Tests:** Supertest / Pactum
- **E2E Tests:** Jest + Supertest
- **Mocking:** jest.mock / Sinon
- **Coverage:** Istanbul / c8

**Code Quality:**
- **Linter:** ESLint
- **Formatter:** Prettier
- **Static Analysis:** SonarQube / ESLint plugins
- **Security Scan:** npm audit / Snyk

### Infraestrutura e Dados

**Banco de Dados Relacional:**
- **PostgreSQL 14+** (recomendado)
  - Suporte a JSON, índices avançados
  - Replicação e alta disponibilidade
  - Extensões: pg_trgm, uuid-ossp
- **Alternativas:** MySQL 8+, MariaDB

**Cache:**
- **Redis 7+**
  - Key-value storage
  - TTL configurável
  - Pub/Sub para eventos
  - Cluster para alta disponibilidade

**Message Queue:**
- **RabbitMQ** (message broker completo)
- **AWS SQS** (cloud-native)
- **Apache Kafka** (high-throughput, event streaming)
- **Redis Streams** (lightweight alternative)

**Search Engine (Opcional):**
- **Elasticsearch** para busca full-text avançada
- **Meilisearch** alternativa leve e rápida

### API Gateway & Load Balancer

- **NGINX** (reverse proxy, load balancer)
- **AWS Application Load Balancer**
- **Kong** (API Gateway completo)
- **Traefik** (cloud-native, com service discovery)

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