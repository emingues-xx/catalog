# Instalação - Backoffice Veículos BFF

## Pré-requisitos

- **Node.js**: 18+ (recomendado 20.x)
- **npm**: 9+ ou **yarn**: 1.22+
- **Redis**: 6.0+ (para cache)
- **Acesso às APIs backend**: backoffice-veiculos-api
- **Git**: Para clonagem do repositório
- **Docker**: Opcional, para containerização

## Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/emingues-xx/backoffice-veiculos-bff.git
cd backoffice-veiculos-bff
```

### 2. Instale as dependências

```bash
npm install
# ou
yarn install
```

### 3. Configure as variáveis de ambiente

Copie o arquivo de exemplo e configure as variáveis:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```bash
# Serviços Backend
BACKOFFICE_API_URL=https://backoffice-veiculos-api.railway.app
AUTH_SERVICE_URL=https://auth-service.railway.app
VITRINE_API_URL=https://vitrine-veiculos-api.railway.app

# Server Configuration
PORT=3002
NODE_ENV=development
HOST=localhost

# Cache Redis
REDIS_URL=redis://localhost:6379
CACHE_TTL=300
CACHE_PREFIX=backoffice_bff

# Autenticação
JWT_SECRET=your-jwt-secret
JWT_EXPIRES_IN=24h
API_KEY_SECRET=your-api-key-secret

# Rate Limiting
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100

# Logs
LOG_LEVEL=info
LOG_FILE=./logs/bff.log

# Timeouts
REQUEST_TIMEOUT=30000
CONNECTION_TIMEOUT=5000
```

### 4. Configure o Redis

#### Opção 1: Redis Local

```bash
# Instalar Redis (Ubuntu/Debian)
sudo apt-get install redis-server

# Iniciar o serviço
sudo systemctl start redis-server
sudo systemctl enable redis-server

# Testar conexão
redis-cli ping
```

#### Opção 2: Redis Cloud

1. Crie uma conta no [Redis Cloud](https://redis.com/redis-enterprise-cloud/overview/)
2. Crie uma instância gratuita
3. Obtenha a string de conexão
4. Atualize `REDIS_URL` no `.env`

### 5. Inicie o servidor

```bash
# Desenvolvimento com hot reload
npm run dev

# Desenvolvimento com debug
npm run dev:debug

# Produção
npm start
```

### 6. Verifique a instalação

```bash
# Teste o BFF
curl http://localhost:3002/health

# Teste endpoint de dashboard
curl http://localhost:3002/api/dashboard/metrics
```

## Docker

### Build da imagem

```bash
docker build -t backoffice-veiculos-bff .
```

### Executar container

```bash
docker run -p 3002:3002 \
  -e BACKOFFICE_API_URL=https://backoffice-veiculos-api.railway.app \
  -e REDIS_URL=redis://host.docker.internal:6379 \
  -e JWT_SECRET=your-jwt-secret \
  backoffice-veiculos-bff
```

### Docker Compose

Crie um arquivo `docker-compose.yml`:

```yaml
version: '3.8'
services:
  bff:
    build: .
    ports:
      - "3002:3002"
    environment:
      - BACKOFFICE_API_URL=https://backoffice-veiculos-api.railway.app
      - REDIS_URL=redis://redis:6379
      - JWT_SECRET=your-jwt-secret
      - NODE_ENV=production
    depends_on:
      - redis
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped

volumes:
  redis_data:
```

Execute com:

```bash
docker-compose up -d
```

## Deploy

### Railway (Recomendado)

1. **Conecte o repositório**:
   - Acesse [Railway](https://railway.app)
   - Conecte sua conta GitHub
   - Selecione o repositório `backoffice-veiculos-bff`

2. **Configure as variáveis de ambiente**:
   ```bash
   BACKOFFICE_API_URL=https://backoffice-veiculos-api.railway.app
   REDIS_URL=redis://redis:6379
   JWT_SECRET=your-production-jwt-secret
   NODE_ENV=production
   PORT=3002
   ```

3. **Adicione Redis**:
   - No Railway, adicione o serviço Redis
   - Configure a variável `REDIS_URL` automaticamente

4. **Deploy automático**: A cada push na branch `main`

### Vercel

1. **Instale o Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Configure e deploy**:
   ```bash
   vercel --prod
   ```

## Testes

### Executar Testes

```bash
# Todos os testes
npm test

# Testes com coverage
npm run test:coverage

# Testes em modo watch
npm run test:watch

# Testes de integração
npm run test:integration
```

### Configuração de Testes

Crie um arquivo `.env.test`:

```bash
BACKOFFICE_API_URL=http://localhost:3000
REDIS_URL=redis://localhost:6379
JWT_SECRET=test-jwt-secret
NODE_ENV=test
PORT=3003
```

## Scripts Disponíveis

```bash
# Desenvolvimento
npm run dev          # Inicia com nodemon
npm run dev:debug    # Inicia com debugger

# Produção
npm start            # Inicia servidor
npm run build        # Compila TypeScript

# Testes
npm test             # Executa testes
npm run test:watch   # Testes em modo watch
npm run test:coverage # Testes com coverage

# Qualidade de código
npm run lint         # ESLint
npm run lint:fix     # ESLint com auto-fix
npm run format       # Prettier

# Cache
npm run cache:clear  # Limpa cache Redis
npm run cache:stats  # Estatísticas do cache

# Docker
npm run docker:build # Build da imagem Docker
npm run docker:run   # Executa container
```

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

### Cache
- `GET /api/cache/stats` - Estatísticas do cache
- `DELETE /api/cache/clear` - Limpar cache

## Monitoramento

### Métricas Importantes
- **Latência**: Tempo de resposta das requisições
- **Throughput**: Número de requisições por segundo
- **Cache Hit Rate**: Taxa de acerto do cache
- **Error Rate**: Taxa de erros por endpoint
- **Backend Response Time**: Tempo de resposta dos serviços backend

### Health Checks

```bash
# Health check básico
curl http://localhost:3002/health

# Health check detalhado
curl http://localhost:3002/health/detailed

# Status do cache
curl http://localhost:3002/api/cache/stats
```

## Troubleshooting

### Problemas Comuns

1. **Erro de conexão com Redis**:
   ```bash
   # Verifique se o Redis está rodando
   sudo systemctl status redis-server
   
   # Teste a conexão
   redis-cli ping
   ```

2. **Erro de conexão com APIs backend**:
   - Verifique se as URLs estão corretas
   - Teste a conectividade com as APIs
   - Verifique se as APIs estão rodando

3. **Erro de cache**:
   - Verifique se o Redis está acessível
   - Limpe o cache se necessário: `npm run cache:clear`

4. **Erro de timeout**:
   - Aumente os valores de timeout no `.env`
   - Verifique a performance das APIs backend

### Logs

```bash
# Ver logs em tempo real
npm run dev

# Logs do Docker
docker-compose logs -f bff

# Logs do Railway
railway logs
```

## Links Úteis

- [Repositório](https://github.com/emingues-xx/backoffice-veiculos-bff)
- [Documentação da API](https://backoffice-veiculos-bff.railway.app/api-docs)
- [Railway Dashboard](https://railway.app)
- [Redis Cloud](https://redis.com/redis-enterprise-cloud/overview/)