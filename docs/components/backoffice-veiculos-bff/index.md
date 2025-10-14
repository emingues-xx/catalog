# Backoffice Veículos BFF

## Visão Geral

O **backoffice-veiculos-bff** é uma aplicação BFF (Backend for Frontend) Node.js/TypeScript que atua como camada intermediária entre o frontend do backoffice de veículos e os serviços de backend. Ele fornece uma interface otimizada e adaptada às necessidades específicas da interface de usuário administrativa.

## Propósito

Este componente tem como objetivo:

- **Agregar dados**: Consolidar informações de múltiplos serviços backend em uma única interface
- **Otimizar performance**: Reduzir requisições e complexidade do frontend através de cache e agregação
- **Customizar endpoints**: Fornecer APIs específicas para necessidades do backoffice
- **Garantir segurança**: Implementar validação, autenticação e autorização centralizadas
- **Simplificar integração**: Abstrair complexidades dos serviços backend para o frontend

## Funcionalidades Principais

### Agregação de Dados
- Consolidação de dados de anúncios, usuários e vendas
- Transformação de dados para formato otimizado do frontend
- Cache inteligente para melhorar performance
- Paginação e filtros customizados

### Orquestração de Serviços
- Coordenação de chamadas para múltiplas APIs
- Tratamento de erros e fallbacks
- Retry automático para operações críticas
- Rate limiting e throttling

### Segurança e Autenticação
- Validação de tokens JWT
- Controle de permissões baseado em roles
- Sanitização de dados de entrada
- Logs de auditoria

### Otimizações para Frontend
- Endpoints específicos para dashboards
- Dados pré-processados para gráficos e relatórios
- Suporte a operações em lote
- WebSocket para atualizações em tempo real

## Tecnologias Utilizadas

- **Runtime**: Node.js
- **Linguagem**: TypeScript
- **Framework**: Express.js ou NestJS
- **Cache**: Redis
- **Autenticação**: JWT
- **Validação**: Joi ou class-validator
- **Documentação**: Swagger/OpenAPI
- **Containerização**: Docker
- **Deploy**: Railway

## Arquitetura

### Camadas da Aplicação

```
┌─────────────────────────────────────┐
│           Frontend Web              │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│            BFF Layer                │
│  ┌─────────────┐ ┌─────────────────┐│
│  │ Controllers │ │    Services     ││
│  └─────────────┘ └─────────────────┘│
│  ┌─────────────┐ ┌─────────────────┐│
│  │ Middleware  │ │   Cache Layer   ││
│  └─────────────┘ └─────────────────┘│
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│         Backend Services            │
│  ┌─────────────┐ ┌─────────────────┐│
│  │ API Service │ │  Auth Service   ││
│  └─────────────┘ └─────────────────┘│
└─────────────────────────────────────┘
```

### Fluxo de Dados

1. **Requisição do Frontend**: Interface web faz requisição para o BFF
2. **Validação**: BFF valida autenticação e autorização
3. **Cache Check**: Verifica se dados estão em cache
4. **Orquestração**: Coordena chamadas para serviços backend
5. **Agregação**: Combina e transforma dados recebidos
6. **Resposta**: Retorna dados otimizados para o frontend

## Endpoints Principais

### Dashboard
- `GET /api/dashboard/metrics` - Métricas consolidadas
- `GET /api/dashboard/sales` - Dados de vendas
- `GET /api/dashboard/announcements` - Estatísticas de anúncios

### Anúncios
- `GET /api/announcements` - Lista paginada com filtros
- `POST /api/announcements` - Criação de anúncio
- `PUT /api/announcements/:id` - Atualização
- `DELETE /api/announcements/:id` - Remoção

### Usuários
- `GET /api/users` - Lista de usuários
- `GET /api/users/:id` - Detalhes do usuário
- `PUT /api/users/:id` - Atualização de perfil

## Configuração

### Variáveis de Ambiente

```bash
# Serviços Backend
BACKOFFICE_API_URL=https://backoffice-veiculos-api.railway.app
AUTH_SERVICE_URL=https://auth-service.railway.app

# Cache
REDIS_URL=redis://localhost:6379
CACHE_TTL=300

# Autenticação
JWT_SECRET=your-jwt-secret
JWT_EXPIRES_IN=24h

# Logs
LOG_LEVEL=info
```

### Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

## Monitoramento

### Métricas Importantes
- **Latência**: Tempo de resposta das requisições
- **Throughput**: Número de requisições por segundo
- **Cache Hit Rate**: Taxa de acerto do cache
- **Error Rate**: Taxa de erros por endpoint

### Logs
- Requisições HTTP com timestamps
- Erros e exceções detalhadas
- Performance de chamadas para serviços backend
- Auditoria de operações sensíveis

## Links Úteis

- [Repositório](https://github.com/emingues-xx/backoffice-veiculos-bff)
- [Documentação da API](https://backoffice-veiculos-bff.railway.app/api-docs)
- [Deploy no Railway](https://railway.app)
