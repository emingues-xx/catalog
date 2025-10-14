# Instalação - Backoffice Veículos API

## Pré-requisitos

- **Node.js**: 18+ (recomendado 20.x)
- **npm**: 9+ ou **yarn**: 1.22+
- **MongoDB**: 6.0+ (local ou Atlas)
- **Git**: Para clonagem do repositório
- **Docker**: Opcional, para containerização

## Instalação Local

### 1. Clone o repositório

```bash
git clone https://github.com/emingues-xx/backoffice-veiculos-api.git
cd backoffice-veiculos-api
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
cp env.example .env
```

Edite o arquivo `.env` com suas configurações:

```bash
# Database
MONGODB_URI=mongodb://localhost:27017/backoffice-veiculos

# JWT Authentication
JWT_SECRET=your-super-secret-jwt-key-min-32-chars
JWT_EXPIRES_IN=24h
JWT_REFRESH_EXPIRES_IN=7d

# Server Configuration
PORT=3000
NODE_ENV=development
HOST=localhost

# CORS
CORS_ORIGIN=http://localhost:3001,http://localhost:3000

# File Upload
MAX_FILE_SIZE=10485760
UPLOAD_PATH=./uploads

# Email (opcional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

# Logs
LOG_LEVEL=info
LOG_FILE=./logs/app.log

# Rate Limiting
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100
```

### 4. Configure o MongoDB

#### Opção 1: MongoDB Local

```bash
# Instalar MongoDB (Ubuntu/Debian)
sudo apt-get install mongodb

# Iniciar o serviço
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

#### Opção 2: MongoDB Atlas (Cloud)

1. Crie uma conta no [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Crie um cluster gratuito
3. Configure o usuário e senha
4. Obtenha a string de conexão
5. Atualize `MONGODB_URI` no `.env`

### 5. Execute as migrações e seeders (se necessário)

```bash
# Executar migrações
npm run migrate

# Popular banco com dados de exemplo
npm run seed
```

### 6. Inicie o servidor

```bash
# Desenvolvimento com hot reload
npm run dev

# Desenvolvimento com debug
npm run dev:debug

# Produção
npm start
```

### 7. Verifique a instalação

```bash
# Teste a API
curl http://localhost:3000/health

# Acesse a documentação Swagger
open http://localhost:3000/api-docs
```

## Docker

### Build da imagem

```bash
docker build -t backoffice-veiculos-api .
```

### Executar container

```bash
docker run -p 3000:3000 \
  -e MONGODB_URI=mongodb://host.docker.internal:27017/backoffice-veiculos \
  -e JWT_SECRET=your-jwt-secret \
  -e NODE_ENV=production \
  backoffice-veiculos-api
```

### Docker Compose (Recomendado)

Crie um arquivo `docker-compose.yml`:

```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "3000:3000"
    environment:
      - MONGODB_URI=mongodb://mongo:27017/backoffice-veiculos
      - JWT_SECRET=your-super-secret-jwt-key
      - NODE_ENV=production
      - CORS_ORIGIN=http://localhost:3001
    depends_on:
      - mongo
    volumes:
      - ./uploads:/app/uploads
      - ./logs:/app/logs
    restart: unless-stopped
  
  mongo:
    image: mongo:7.0
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
      - ./mongo-init.js:/docker-entrypoint-initdb.d/mongo-init.js:ro
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=password
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped

volumes:
  mongo_data:
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
   - Selecione o repositório `backoffice-veiculos-api`

2. **Configure as variáveis de ambiente**:
   ```bash
   MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/backoffice-veiculos
   JWT_SECRET=your-production-jwt-secret-min-32-chars
   NODE_ENV=production
   PORT=3000
   CORS_ORIGIN=https://your-frontend-domain.com
   ```

3. **Deploy automático**: A cada push na branch `main`

### Heroku

1. **Instale o Heroku CLI**
2. **Configure o app**:
   ```bash
   heroku create backoffice-veiculos-api
   heroku addons:create mongolab:sandbox
   heroku config:set JWT_SECRET=your-production-secret
   heroku config:set NODE_ENV=production
   ```

3. **Deploy**:
   ```bash
   git push heroku main
   ```

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

# Testes E2E
npm run test:e2e
```

### Configuração de Testes

Crie um arquivo `.env.test`:

```bash
MONGODB_URI=mongodb://localhost:27017/backoffice-veiculos-test
JWT_SECRET=test-jwt-secret
NODE_ENV=test
PORT=3001
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

# Banco de dados
npm run migrate      # Executa migrações
npm run seed         # Popula banco com dados
npm run db:reset     # Reseta banco de dados

# Docker
npm run docker:build # Build da imagem Docker
npm run docker:run   # Executa container
```

## GitHub Actions

O repositório inclui workflows automatizados para:

### Avaliação de Pull Requests
- **Secret**: `DF94AEC11B7255BA28B4934259186`
- **API URL**: `https://claude-webhook-production.up.railway.app/evaluate-pullrequest`

### Configuração
1. Vá em **Settings** → **Secrets and variables** → **Actions**
2. Adicione o secret `WEBHOOK_SECRET`
3. Configure `EVALUATION_API_URL` (opcional)

## Troubleshooting

### Problemas Comuns

1. **Erro de conexão com MongoDB**:
   ```bash
   # Verifique se o MongoDB está rodando
   sudo systemctl status mongodb
   
   # Teste a conexão
   mongosh mongodb://localhost:27017/backoffice-veiculos
   ```

2. **Erro de JWT Secret**:
   - Certifique-se que o JWT_SECRET tem pelo menos 32 caracteres
   - Use um gerador de senhas seguras

3. **Erro de CORS**:
   - Verifique se a URL do frontend está em CORS_ORIGIN
   - Para desenvolvimento, use `http://localhost:3001`

4. **Erro de porta em uso**:
   ```bash
   # Encontre o processo usando a porta
   lsof -i :3000
   
   # Mate o processo
   kill -9 <PID>
   ```

### Logs

```bash
# Ver logs em tempo real
npm run dev

# Logs do Docker
docker-compose logs -f api

# Logs do Railway
railway logs
```

## Links Úteis

- [Repositório](https://github.com/emingues-xx/backoffice-veiculos-api)
- [Documentação da API](https://backoffice-veiculos-api.railway.app/api-docs)
- [Exemplos de CURL](https://github.com/emingues-xx/backoffice-veiculos-api/blob/main/API_CURL_EXAMPLES.md)
- [Railway Dashboard](https://railway.app)
- [MongoDB Atlas](https://www.mongodb.com/atlas)