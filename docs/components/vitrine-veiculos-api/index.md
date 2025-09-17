# vitrine-veiculos-api

![Build Status](https://img.shields.io/github/actions/workflow/status/emingues-xx/vitrine-veiculos-api/ci.yml?branch=main)
![Version](https://img.shields.io/github/v/release/emingues-xx/vitrine-veiculos-api)
![License](https://img.shields.io/github/license/emingues-xx/vitrine-veiculos-api)
![Tech Stack](https://img.shields.io/badge/Node.js-18-green)
![Tech Stack](https://img.shields.io/badge/Fastify-4-blue)
![Tech Stack](https://img.shields.io/badge/TypeScript-5-blue)

API Node.js para consultas públicas, busca e filtros de veículos da vitrine.

## Descrição

API REST robusta e performática que fornece endpoints para consulta pública de veículos, sistema de busca avançada e filtros otimizados. Construída com foco em performance, cache inteligente e escalabilidade.

## Características Principais

- ⚡ **Alta Performance**: Fastify com otimizações para throughput
- 🔍 **Busca Avançada**: Full-text search com PostgreSQL e Elasticsearch
- 💾 **Cache Inteligente**: Redis com estratégias de invalidação
- 📊 **Rate Limiting**: Proteção contra abuse e DDoS
- 📈 **Monitoramento**: APM integrado e métricas detalhadas
- 🔒 **Segurança**: Validação rigorosa e sanitização de inputs

## Tecnologias

- **Runtime**: Node.js 18 LTS
- **Framework**: Fastify 4
- **Linguagem**: TypeScript 5
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **Search**: Elasticsearch 8 (opcional)
- **Validation**: Joi
- **Testing**: Jest + Supertest
- **Documentation**: Swagger/OpenAPI

## Instalação

### Pré-requisitos
- Node.js 18+
- PostgreSQL 15+
- Redis 7+
- npm 9+ ou yarn 1.22+

### Setup Rápido
```bash
# Clone do repositório
git clone https://github.com/emingues-xx/vitrine-veiculos-api.git
cd vitrine-veiculos-api

# Instalação de dependências
npm install

# Configuração do ambiente
cp .env.example .env
# Edite .env com suas configurações

# Setup do banco de dados
npm run db:migrate
npm run db:seed

# Servidor de desenvolvimento
npm run dev

# API disponível em http://localhost:3001
```

## Scripts Disponíveis

```bash
npm run dev          # Servidor de desenvolvimento com watch
npm run build        # Build TypeScript para produção
npm run start        # Servidor de produção
npm run test         # Execução de testes
npm run test:watch   # Testes em modo watch
npm run test:e2e     # Testes end-to-end
npm run lint         # Linting do código
npm run db:migrate   # Execução de migrations
npm run db:seed      # Seed do banco com dados de teste
```

## Principais Endpoints

### Veículos
```http
GET    /api/vehicles              # Listagem com filtros
GET    /api/vehicles/:id          # Detalhes de um veículo
GET    /api/vehicles/search       # Busca com texto livre
GET    /api/vehicles/suggestions  # Sugestões de busca
```

### Filtros e Metadados
```http
GET    /api/brands               # Lista de marcas
GET    /api/models/:brand        # Modelos por marca
GET    /api/locations/states     # Estados disponíveis
GET    /api/locations/cities/:state # Cidades por estado
```

### Utilitários
```http
GET    /health                   # Health check
GET    /metrics                  # Métricas Prometheus
GET    /docs                     # Documentação Swagger
```

## Configuração

### Variáveis de Ambiente

```bash
# Server Configuration
NODE_ENV=development
PORT=3001
HOST=0.0.0.0

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/vitrine_db
DATABASE_POOL_SIZE=10

# Redis Cache
REDIS_URL=redis://localhost:6379
REDIS_TTL_DEFAULT=300

# Search (Optional)
ELASTICSEARCH_URL=http://localhost:9200

# Rate Limiting
RATE_LIMIT_MAX=100
RATE_LIMIT_WINDOW=60000

# Monitoring
APM_SERVICE_NAME=vitrine-veiculos-api
APM_SERVER_URL=http://localhost:8200
```

## Estrutura do Projeto

```
src/
├── controllers/        # Route handlers
├── services/          # Business logic
├── repositories/      # Data access layer
├── models/           # Data models and types
├── middleware/       # Express/Fastify middleware
├── utils/            # Utility functions
├── config/           # Configuration files
├── migrations/       # Database migrations
├── seeds/            # Database seeds
└── tests/            # Test files
```

## Performance

### Benchmarks
- **Throughput**: 10,000+ req/s (single instance)
- **Latency**: p95 < 50ms para consultas simples
- **Memory**: ~150MB baseline

### Otimizações Implementadas
- Connection pooling otimizado
- Query optimization com índices estratégicos
- Response caching com Redis
- Compression automática (gzip/brotli)
- Keep-alive connections

## Cache Strategy

### Camadas de Cache
```
Application → Redis → Database
```

### TTL por Endpoint
- **Listagem de veículos**: 5 minutos
- **Detalhes do veículo**: 15 minutos
- **Marcas/Modelos**: 1 hora
- **Localizações**: 24 horas

## Monitoramento

### Health Checks
```http
GET /health
{
  "status": "healthy",
  "database": "connected",
  "redis": "connected",
  "uptime": 3600
}
```

### Métricas
- Request rate e latency
- Database connection pool
- Redis cache hit ratio
- Error rates por endpoint

## Deploy

### Docker
```bash
# Build da imagem
docker build -t vitrine-veiculos-api .

# Execução com docker-compose
docker-compose up -d
```

### Kubernetes
```bash
# Deploy usando manifests
kubectl apply -f k8s/

# Ou usando Helm
helm install vitrine-api ./charts/vitrine-api
```

## Links Relacionados

- 🏗️ [Arquitetura](architecture.md)
- 📋 [API Documentation](api.md)
- 🔧 [Setup Detalhado](setup.md)
- 📚 [Repositório GitHub](https://github.com/emingues-xx/vitrine-veiculos-api)
- 🎯 [Vitrine BFF](../vitrine-veiculos-bff/index.md)