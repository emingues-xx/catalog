# Deployment - Backoffice Veículos API

## Visão Geral

Este documento descreve o processo de deployment da API do Backoffice de Veículos na plataforma Railway.

## Plataforma de Deploy

**Plataforma:** Railway
**Região:** us-east-1
**Runtime:** Node.js 18 LTS
**Build System:** Docker

## Pré-requisitos

### Variáveis de Ambiente

As seguintes variáveis de ambiente devem estar configuradas no Railway:

#### Banco de Dados
```bash
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/backoffice-veiculos
DB_NAME=backoffice-veiculos
```

#### Cache
```bash
REDIS_URL=redis://user:password@redis-host:6379
REDIS_TTL=3600
```

#### Autenticação
```bash
JWT_SECRET=your-super-secret-jwt-key
JWT_EXPIRATION=24h
```

#### API Configuration
```bash
NODE_ENV=production
PORT=3000
API_VERSION=v1
BASE_URL=https://backoffice-veiculos-api.railway.app
```

#### Integração com Sistemas Legados
```bash
LEGACY_SYSTEM_API_URL=https://legacy-api.internal.com
LEGACY_SYSTEM_API_KEY=your-legacy-api-key
```

#### Monitoramento
```bash
PROMETHEUS_ENABLED=true
PROMETHEUS_PORT=9090
LOG_LEVEL=info
```

#### Jobs
```bash
JOB_ATUALIZACAO_METRICAS_ENABLED=true
JOB_ATUALIZACAO_METRICAS_CRON=0 23 * * *
```

#### Alertas
```bash
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
ALERT_EMAIL=alerts@backoffice-veiculos.com
```

## Dockerfile

O projeto utiliza o seguinte Dockerfile otimizado para produção:

```dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app

# Copiar arquivos de dependências
COPY package*.json ./
COPY tsconfig.json ./

# Instalar dependências
RUN npm ci --only=production

# Copiar código fonte
COPY src ./src

# Build do projeto
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app

# Copiar dependências e build do stage anterior
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./

# Expor porta
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

# Usuário não-root para segurança
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
USER nodejs

# Comando de inicialização
CMD ["node", "dist/server.js"]
```

## Processo de Deployment

### 1. Deploy Automático via GitHub

O Railway está configurado para fazer deploy automático quando há push na branch `main`:

```yaml
# railway.json
{
  "build": {
    "builder": "DOCKERFILE",
    "dockerfilePath": "Dockerfile"
  },
  "deploy": {
    "numReplicas": 1,
    "sleepApplication": false,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### 2. Deploy Manual via Railway CLI

```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Login no Railway
railway login

# Linkar ao projeto
railway link

# Deploy manual
railway up
```

### 3. Pipeline CI/CD

O projeto utiliza GitHub Actions para CI/CD:

```yaml
name: Deploy to Railway

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm test
      - run: npm run lint

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - uses: railway/deploy-action@v1
        with:
          railway_token: ${{ secrets.RAILWAY_TOKEN }}
```

## Configurações de Produção

### Recursos Alocados

- **CPU**: 2 vCPUs
- **Memória**: 4 GB RAM
- **Disco**: 10 GB SSD
- **Replicas**: 1 (com auto-scaling planejado)

### Limites e Quotas

```javascript
// src/config/rate-limit.ts
export const rateLimitConfig = {
  windowMs: 60 * 60 * 1000, // 1 hora
  max: 1000, // limite de requisições
  message: 'Limite de requisições excedido',
  standardHeaders: true,
  legacyHeaders: false,
}
```

### Health Checks

Endpoint de health check disponível em `/health`:

```typescript
// src/routes/health.ts
app.get('/health', (req, res) => {
  const health = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    services: {
      database: checkDatabaseHealth(),
      cache: checkCacheHealth(),
      jobs: checkJobsHealth(),
    }
  }

  const isHealthy = Object.values(health.services).every(s => s === 'operational')
  res.status(isHealthy ? 200 : 503).json(health)
})
```

## Monitoramento

### Prometheus Metrics

Métricas expostas em `/metrics`:

```
http_requests_total
http_request_duration_ms
api_response_time_ms
cache_hit_rate
job_execution_duration_ms
database_query_duration_ms
```

### Grafana Dashboards

Dashboards configurados:
- API Performance
- Cache Performance
- Job Execution Status
- Database Queries
- Error Rates

### Alertas

Alertas configurados via Alertmanager:

1. **API Down**: API não responde por mais de 5 minutos
2. **High Error Rate**: Taxa de erro > 5% em 10 minutos
3. **Slow Response Time**: Tempo de resposta médio > 2s
4. **Cache Miss Rate High**: Taxa de cache miss > 30%
5. **Job Failure**: Job de atualização de métricas falha
6. **Database Connection Issues**: Problemas de conexão com MongoDB

## Rollback

### Rollback Automático

O Railway mantém os últimos 10 deployments. Para fazer rollback:

1. Acessar Railway Dashboard
2. Ir em "Deployments"
3. Selecionar deployment anterior
4. Clicar em "Redeploy"

### Rollback via CLI

```bash
# Listar deployments
railway deployments list

# Fazer rollback para deployment específico
railway rollback <deployment-id>
```

## Logs

### Visualização de Logs

```bash
# Logs em tempo real
railway logs

# Logs filtrados
railway logs --filter "ERROR"

# Logs de um serviço específico
railway logs --service api
```

### Logs Estruturados

A aplicação utiliza Winston para logs estruturados:

```typescript
import winston from 'winston'

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
})
```

## Backup e Recuperação

### Backup do MongoDB

Backups automáticos diários configurados no MongoDB Atlas:
- **Frequência**: Diária às 2:00 AM UTC
- **Retenção**: 7 dias
- **Snapshot On-Demand**: Disponível a qualquer momento

### Backup de Variáveis de Ambiente

```bash
# Exportar variáveis de ambiente
railway variables > .env.backup

# Restaurar variáveis de ambiente
railway variables set < .env.backup
```

## Segurança

### Proteções Implementadas

1. **Helmet.js**: Headers de segurança HTTP
2. **Rate Limiting**: Prevenção de DDoS
3. **CORS**: Configuração restrita de origens
4. **JWT**: Tokens seguros com expiração
5. **Input Validation**: Validação de todos os inputs
6. **SQL Injection Prevention**: Queries parametrizadas
7. **XSS Prevention**: Sanitização de inputs

### SSL/TLS

O Railway fornece certificados SSL/TLS automáticos via Let's Encrypt.

## Troubleshooting

### Problemas Comuns

#### API não inicia
```bash
# Verificar logs
railway logs

# Verificar variáveis de ambiente
railway variables

# Verificar build
railway build logs
```

#### Performance degradada
```bash
# Verificar métricas no Grafana
# Verificar cache Redis
redis-cli INFO stats

# Verificar queries lentas no MongoDB
db.currentOp({ "active": true, "secs_running": { "$gt": 3 } })
```

#### Job de atualização não executa
```bash
# Verificar logs do job
railway logs --filter "AtualizacaoMetricasJob"

# Verificar variáveis de ambiente do job
railway variables | grep JOB_
```

## Contatos de Suporte

- **Equipe de DevOps**: devops@backoffice-veiculos.com
- **Squad Backoffice**: squad-backoffice@backoffice-veiculos.com
- **Oncall**: +55 11 99999-9999

## Referências

- [Railway Docs](https://docs.railway.app/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Node.js Production Best Practices](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)
- [Prometheus Monitoring](https://prometheus.io/docs/introduction/overview/)
