# Arquitetura - Backoffice Veículos API

## Visão Geral

A `backoffice-veiculos-api` é uma API REST construída para gerenciar operações de backoffice relacionadas a veículos. A aplicação segue uma arquitetura em camadas, separando responsabilidades entre controllers, services e repositories.

## Endpoints Principais

### Veículos
- `GET /api/veiculos` - Lista todos os veículos
- `GET /api/veiculos/:id` - Obtém detalhes de um veículo específico
- `POST /api/veiculos` - Cadastra um novo veículo
- `PUT /api/veiculos/:id` - Atualiza dados de um veículo
- `DELETE /api/veiculos/:id` - Remove um veículo

### Administração
- `GET /api/admin/dashboard` - Dados do dashboard administrativo
- `GET /api/admin/relatorios` - Geração de relatórios

### Health Check
- `GET /health` - Verifica o status da API

## Estrutura de Pastas

```
backoffice-veiculos-api/
├── src/
│   ├── controllers/     # Controladores das rotas
│   ├── services/        # Lógica de negócio
│   ├── repositories/    # Acesso a dados
│   ├── models/          # Modelos de dados
│   ├── middlewares/     # Middlewares (autenticação, validação)
│   ├── routes/          # Definição de rotas
│   ├── config/          # Configurações da aplicação
│   └── utils/           # Funções utilitárias
├── tests/               # Testes unitários e integração
├── docs/                # Documentação adicional
└── package.json
```

## Fluxo de Dados

1. **Request** → O cliente envia uma requisição HTTP
2. **Middleware** → Validação de autenticação e autorização
3. **Router** → Direciona para o controller apropriado
4. **Controller** → Recebe a requisição e valida parâmetros
5. **Service** → Executa a lógica de negócio
6. **Repository** → Realiza operações no banco de dados
7. **Response** → Retorna a resposta formatada ao cliente

```
Cliente → Middleware → Router → Controller → Service → Repository → Database
                                                                        ↓
Cliente ← Response ← Controller ← Service ← Repository ← Database
```

## Autenticação e Autorização

### Autenticação
- **Método:** JWT (JSON Web Tokens)
- **Endpoint de Login:** `POST /api/auth/login`
- **Token:** Enviado no header `Authorization: Bearer <token>`
- **Expiração:** Tokens expiram após 24 horas

### Autorização
- **Roles:** `ADMIN`, `OPERATOR`, `VIEWER`
- **ADMIN:** Acesso total às operações
- **OPERATOR:** Pode criar e editar veículos
- **VIEWER:** Apenas visualização de dados

### Middleware de Segurança
- Validação de token em todas as rotas protegidas
- Rate limiting para prevenir abuso
- CORS configurado para origens permitidas
- Validação de entrada para prevenir injeções

## Tecnologias

- **Framework:** Node.js com Express
- **Banco de Dados:** PostgreSQL
- **ORM:** Sequelize / TypeORM
- **Autenticação:** JWT (jsonwebtoken)
- **Validação:** Joi / Yup
