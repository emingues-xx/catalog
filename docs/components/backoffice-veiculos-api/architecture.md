# Arquitetura - backoffice-veiculos-api

## Visão Geral

A `backoffice-veiculos-api` é uma API backend desenvolvida para gerenciar operações de veículos no sistema de backoffice. A arquitetura segue princípios RESTful e é construída para ser escalável, mantível e segura.

## Endpoints Principais

### Veículos
- `GET /api/veiculos` - Lista todos os veículos
- `GET /api/veiculos/:id` - Busca veículo por ID
- `POST /api/veiculos` - Cria novo veículo
- `PUT /api/veiculos/:id` - Atualiza veículo existente
- `DELETE /api/veiculos/:id` - Remove veículo

### Consultas
- `GET /api/veiculos/search` - Busca veículos com filtros
- `GET /api/veiculos/placa/:placa` - Busca por placa
- `GET /api/veiculos/status/:status` - Filtra por status

### Gestão
- `GET /api/health` - Health check da API
- `GET /api/metrics` - Métricas da aplicação

## Estrutura de Pastas

```
backoffice-veiculos-api/
├── src/
│   ├── controllers/        # Controladores da API
│   ├── models/             # Modelos de dados
│   ├── routes/             # Definição de rotas
│   ├── services/           # Lógica de negócio
│   ├── middlewares/        # Middlewares (auth, validação, etc)
│   ├── config/             # Configurações da aplicação
│   ├── utils/              # Utilitários e helpers
│   └── database/           # Conexão e migrations
├── tests/                  # Testes automatizados
├── docs/                   # Documentação adicional
└── scripts/                # Scripts auxiliares
```

## Fluxo de Dados

```
Cliente
  ↓
[Autenticação Middleware]
  ↓
[Validação Middleware]
  ↓
Routes
  ↓
Controllers
  ↓
Services (Lógica de Negócio)
  ↓
Models (ORM/Database)
  ↓
Banco de Dados
```

### Detalhamento do Fluxo

1. **Request**: Cliente envia requisição HTTP
2. **Autenticação**: Middleware valida token de acesso
3. **Validação**: Middleware valida dados de entrada
4. **Roteamento**: Sistema direciona para controller apropriado
5. **Processamento**: Controller delega para service
6. **Persistência**: Service interage com models/database
7. **Response**: Resposta formatada retorna ao cliente

## Autenticação e Autorização

### Autenticação

- **Método**: JWT (JSON Web Tokens)
- **Header**: `Authorization: Bearer <token>`
- **Expiração**: Tokens expiram após período configurável
- **Refresh**: Suporte a refresh tokens para renovação

### Autorização

- **Níveis de Acesso**:
  - `admin`: Acesso completo (CRUD)
  - `operator`: Leitura e edição
  - `viewer`: Apenas leitura

- **Controle por Endpoint**:
  - Middlewares de autorização verificam permissões
  - Recursos protegidos por roles específicas
  - Auditoria de acessos e modificações

### Segurança

- Validação de entrada em todos os endpoints
- Rate limiting para prevenir abuso
- CORS configurado adequadamente
- Logs de auditoria para ações críticas
- Sanitização de dados para prevenir SQL injection
