# Arquitetura - Backoffice Veículos BFF

## Status do Projeto

🚧 **EM DESENVOLVIMENTO** - Este componente está em fase inicial de desenvolvimento com estrutura básica implementada.

## Visão Geral

O `backoffice-veiculos-bff` é um Backend for Frontend (BFF) Node.js/TypeScript em desenvolvimento que atua como camada intermediária entre o frontend do backoffice de veículos e os serviços de backend. Este componente é responsável por agregar, transformar e otimizar dados para o consumo do frontend.

## Estrutura Atual (Skeleton)

### Estrutura de Pastas Implementada

```
backoffice-veiculos-bff/
├── src/
│   ├── controllers/     # ✅ Estrutura básica criada
│   ├── services/        # ✅ Estrutura básica criada
│   ├── models/          # ✅ Estrutura básica criada
│   ├── routes/          # ✅ Estrutura básica criada
│   ├── middleware/      # ✅ Estrutura básica criada
│   ├── config/          # ✅ Estrutura básica criada
│   └── utils/           # ✅ Estrutura básica criada
├── tests/               # 🚧 Estrutura básica
├── docs/                # 🚧 Documentação em desenvolvimento
├── Dockerfile           # ✅ Configurado
├── package.json         # ✅ Dependências básicas
└── tsconfig.json        # ✅ Configuração TypeScript
```

## Funcionalidades Implementadas

### ✅ Estrutura Base
- Configuração inicial do projeto Node.js/TypeScript
- Estrutura de pastas organizada
- Configuração de Docker
- Deploy no Railway

### 🚧 Em Desenvolvimento
- Endpoints básicos de agregação
- Integração com APIs backend
- Sistema de cache Redis
- Middlewares de autenticação

### 📋 Planejado
- Agregação de dados de múltiplas APIs
- Transformação de dados para frontend
- Rate limiting e throttling
- Sistema de cache inteligente

## Arquitetura Planejada

### Fluxo de Dados

```
Frontend (Backoffice Web)
       ↓
   [API Gateway]
       ↓
 backoffice-veiculos-bff
       ↓
  ┌────┴────┐
  ↓         ↓
backoffice-veiculos-api  (Outras APIs)
  (MongoDB)              (Serviços externos)
```

### Camadas da Aplicação

1. **Controllers**: Recebem requisições HTTP do frontend
2. **Services**: Orquestram chamadas para APIs backend
3. **Cache Layer**: Gerencia cache Redis para performance
4. **Middleware**: Autenticação, validação e logs
5. **Utils**: Funções auxiliares e helpers

## Endpoints Planejados

### Dashboard
- `GET /api/dashboard/metrics` - Métricas consolidadas
- `GET /api/dashboard/sales` - Dados de vendas agregados
- `GET /api/dashboard/announcements` - Estatísticas de anúncios

### Anúncios
- `GET /api/announcements` - Lista com filtros e paginação
- `POST /api/announcements` - Criação via API backend
- `PUT /api/announcements/:id` - Atualização via API backend
- `DELETE /api/announcements/:id` - Remoção via API backend

### Usuários
- `GET /api/users` - Lista de usuários
- `GET /api/users/:id` - Detalhes do usuário
- `POST /api/users` - Criação de usuário
- `PUT /api/users/:id` - Atualização de usuário

### Cache
- `GET /api/cache/stats` - Estatísticas do cache
- `DELETE /api/cache/clear` - Limpar cache

### Health Check
- `GET /health` - Status do BFF
- `GET /health/detailed` - Status detalhado com dependências

## Tecnologias Utilizadas

### ✅ Implementado
- **Runtime**: Node.js 18+
- **Linguagem**: TypeScript
- **Framework**: Express.js
- **Containerização**: Docker
- **Deploy**: Railway

### 🚧 Em Configuração
- **Cache**: Redis
- **Autenticação**: JWT
- **Validação**: Joi ou class-validator
- **HTTP Client**: Axios

### 📋 Planejado
- **Rate Limiting**: express-rate-limit
- **Logs**: Winston ou Pino
- **Monitoramento**: APM tools
- **Documentação**: Swagger/OpenAPI

## Integração com APIs Backend

### APIs Principais
- **backoffice-veiculos-api**: API principal de anúncios e usuários
- **auth-service**: Serviço de autenticação (futuro)
- **notification-service**: Serviços de notificação (futuro)

### Padrões de Integração
- **Circuit Breaker**: Para resiliência
- **Retry Logic**: Para falhas temporárias
- **Timeout**: Para evitar travamentos
- **Fallback**: Dados em cache quando APIs falham

## Sistema de Cache

### Estratégia de Cache
- **Cache de Dados**: Métricas e listagens frequentes
- **TTL Configurável**: Diferentes tempos para diferentes tipos de dados
- **Invalidation**: Limpeza automática e manual
- **Fallback**: Dados em cache quando APIs estão indisponíveis

### Tipos de Cache
- **Dashboard Metrics**: TTL 5 minutos
- **Lista de Anúncios**: TTL 3 minutos
- **Dados de Usuário**: TTL 10 minutos
- **Configurações**: TTL 1 hora

## Configuração de Desenvolvimento

### Variáveis de Ambiente

```bash
# Serviços Backend
BACKOFFICE_API_URL=https://backoffice-veiculos-api.railway.app
AUTH_SERVICE_URL=https://auth-service.railway.app

# Cache Redis
REDIS_URL=redis://localhost:6379
CACHE_TTL=300
CACHE_PREFIX=backoffice_bff

# Autenticação
JWT_SECRET=your-jwt-secret
JWT_EXPIRES_IN=24h

# Server
PORT=3002
NODE_ENV=development
```

### Scripts Disponíveis

```bash
npm run dev          # Desenvolvimento com hot reload
npm run build        # Build para produção
npm start            # Inicia servidor
npm test             # Executa testes
npm run cache:clear  # Limpa cache Redis
```

## Próximos Passos

### Fase 1 - Estrutura Base (Em Andamento)
- [ ] Implementar endpoints básicos
- [ ] Configurar integração com API backend
- [ ] Implementar sistema de cache Redis
- [ ] Criar middlewares essenciais

### Fase 2 - Agregação de Dados
- [ ] Implementar agregação de métricas
- [ ] Criar endpoints de dashboard
- [ ] Implementar transformação de dados
- [ ] Adicionar rate limiting

### Fase 3 - Recursos Avançados
- [ ] Sistema de fallback
- [ ] Monitoramento e métricas
- [ ] Documentação Swagger
- [ ] Testes de integração

## Monitoramento e Observabilidade

### Métricas Planejadas
- **Latência**: Tempo de resposta das requisições
- **Throughput**: Requisições por segundo
- **Cache Hit Rate**: Taxa de acerto do cache
- **Error Rate**: Taxa de erros por endpoint
- **Backend Response Time**: Tempo de resposta das APIs

### Logs
- Requisições HTTP com timestamps
- Erros e exceções detalhadas
- Performance de chamadas para APIs backend
- Auditoria de operações sensíveis

## Links Úteis

- [Repositório](https://github.com/emingues-xx/backoffice-veiculos-bff)
- [Documentação da API](./api-reference.md)
- [Railway Dashboard](https://railway.app)
- [Redis Documentation](https://redis.io/docs)