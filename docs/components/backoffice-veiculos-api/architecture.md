# Arquitetura - Backoffice Veículos API

## Status do Projeto

🚧 **EM DESENVOLVIMENTO** - Este componente está em fase inicial de desenvolvimento com estrutura básica implementada.

## Visão Geral

A `backoffice-veiculos-api` é uma API REST Node.js/TypeScript em desenvolvimento para gerenciar operações de backoffice relacionadas a veículos. A aplicação segue uma arquitetura em camadas, separando responsabilidades entre controllers, services e repositories.

## Estrutura Atual (Skeleton)

### Estrutura de Pastas Implementada

```
backoffice-veiculos-api/
├── src/
│   ├── controllers/     # ✅ Estrutura básica criada
│   ├── services/        # ✅ Estrutura básica criada
│   ├── models/          # ✅ Estrutura básica criada
│   ├── middleware/      # ✅ Estrutura básica criada
│   ├── routes/          # ✅ Estrutura básica criada
│   ├── utils/           # ✅ Estrutura básica criada
│   └── types/           # ✅ Estrutura básica criada
├── .github/             # ✅ GitHub Actions configurado
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
- GitHub Actions para CI/CD
- Sistema de avaliação automática de PRs

### 🚧 Em Desenvolvimento
- Endpoints básicos de CRUD
- Sistema de autenticação JWT
- Integração com MongoDB
- Middlewares de validação
- Documentação Swagger

### 📋 Planejado
- Sistema completo de anúncios
- Gestão de usuários
- Dashboard e métricas
- Upload de imagens
- Sistema de notificações

## Endpoints Planejados

### Autenticação
- `POST /api/auth/login` - Login de usuários
- `POST /api/auth/register` - Registro de usuários
- `POST /api/auth/refresh` - Renovação de token

### Anúncios
- `GET /api/announcements` - Lista anúncios
- `GET /api/announcements/:id` - Detalhes do anúncio
- `POST /api/announcements` - Criar anúncio
- `PUT /api/announcements/:id` - Atualizar anúncio
- `DELETE /api/announcements/:id` - Remover anúncio

### Usuários
- `GET /api/users` - Lista usuários
- `GET /api/users/:id` - Detalhes do usuário
- `POST /api/users` - Criar usuário
- `PUT /api/users/:id` - Atualizar usuário

### Dashboard
- `GET /api/dashboard/metrics` - Métricas gerais
- `GET /api/dashboard/sales` - Dados de vendas

### Health Check
- `GET /health` - Status da API

## Tecnologias Utilizadas

### ✅ Implementado
- **Runtime**: Node.js 18+
- **Linguagem**: TypeScript
- **Framework**: Express.js
- **Containerização**: Docker
- **Deploy**: Railway
- **CI/CD**: GitHub Actions

### 🚧 Em Configuração
- **Banco de Dados**: MongoDB
- **Autenticação**: JWT (jsonwebtoken)
- **Validação**: Joi ou class-validator
- **Documentação**: Swagger/OpenAPI

### 📋 Planejado
- **Cache**: Redis
- **Logs**: Winston ou Pino
- **Testes**: Jest
- **Monitoramento**: APM tools

## Arquitetura Planejada

### Fluxo de Dados

```
Cliente → Middleware → Router → Controller → Service → Repository → MongoDB
                                                                        ↓
Cliente ← Response ← Controller ← Service ← Repository ← MongoDB
```

### Camadas da Aplicação

1. **Controllers**: Recebem requisições HTTP e coordenam a resposta
2. **Services**: Contêm a lógica de negócio
3. **Repositories**: Gerenciam acesso aos dados
4. **Models**: Definem estruturas de dados
5. **Middleware**: Processam requisições (auth, validation, logs)

## GitHub Actions

### ✅ Configurado
- **Avaliação de PRs**: Sistema automático de avaliação
- **Secret**: `DF94AEC11B7255BA28B4934259186`
- **API URL**: `https://claude-webhook-production.up.railway.app/evaluate-pullrequest`

### 🚧 Em Desenvolvimento
- Testes automatizados
- Deploy automático
- Linting e formatação

## Configuração de Desenvolvimento

### Variáveis de Ambiente

```bash
# Database
MONGODB_URI=mongodb://localhost:27017/backoffice-veiculos

# JWT
JWT_SECRET=your-super-secret-jwt-key-min-32-chars
JWT_EXPIRES_IN=24h

# Server
PORT=3000
NODE_ENV=development

# CORS
CORS_ORIGIN=http://localhost:3001
```

### Scripts Disponíveis

```bash
npm run dev          # Desenvolvimento com hot reload
npm run build        # Build para produção
npm start            # Inicia servidor
npm test             # Executa testes
npm run lint         # ESLint
```

## Próximos Passos

### Fase 1 - Estrutura Base (Em Andamento)
- [ ] Implementar endpoints básicos
- [ ] Configurar autenticação JWT
- [ ] Integrar MongoDB
- [ ] Criar middlewares essenciais

### Fase 2 - Funcionalidades Core
- [ ] CRUD completo de anúncios
- [ ] Sistema de usuários
- [ ] Upload de imagens
- [ ] Validações robustas

### Fase 3 - Recursos Avançados
- [ ] Dashboard e métricas
- [ ] Sistema de notificações
- [ ] Cache Redis
- [ ] Monitoramento e logs

## Links Úteis

- [Repositório](https://github.com/emingues-xx/backoffice-veiculos-api)
- [Documentação da API](https://backoffice-veiculos-api.railway.app/api-docs) (Em desenvolvimento)
- [Railway Dashboard](https://railway.app)
- [GitHub Actions](https://github.com/emingues-xx/backoffice-veiculos-api/actions)