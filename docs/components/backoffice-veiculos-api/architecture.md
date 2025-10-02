# Arquitetura - backoffice-veiculos-api

## Visão Geral

A `backoffice-veiculos-api` é uma API REST backend responsável pelo gerenciamento de veículos no sistema de backoffice. A API fornece endpoints para operações CRUD (Create, Read, Update, Delete) de veículos, permitindo consultas, cadastros e atualizações de informações relacionadas.

## Endpoints Principais

### Veículos

- `GET /api/v1/veiculos` - Lista todos os veículos com suporte a paginação e filtros
- `GET /api/v1/veiculos/:id` - Busca um veículo específico por ID
- `POST /api/v1/veiculos` - Cria um novo veículo
- `PUT /api/v1/veiculos/:id` - Atualiza um veículo existente
- `DELETE /api/v1/veiculos/:id` - Remove um veículo
- `GET /api/v1/veiculos/search` - Busca veículos por critérios específicos

### Health Check

- `GET /health` - Verifica o status da API e suas dependências

## Estrutura de Pastas

```
backoffice-veiculos-api/
├── src/
│   ├── controllers/      # Controladores das requisições HTTP
│   ├── services/         # Lógica de negócio
│   ├── models/           # Modelos de dados e schemas
│   ├── routes/           # Definição de rotas
│   ├── middlewares/      # Middlewares (auth, validação, etc)
│   ├── config/           # Configurações da aplicação
│   ├── utils/            # Utilitários e helpers
│   └── database/         # Conexão e migrations do banco de dados
├── tests/                # Testes unitários e de integração
├── docs/                 # Documentação adicional
└── package.json
```

## Fluxo de Dados

1. **Requisição HTTP** → Cliente envia requisição para a API
2. **Roteamento** → Sistema de rotas direciona para o controlador apropriado
3. **Middleware de Autenticação** → Valida token JWT e permissões
4. **Validação** → Middleware valida dados de entrada conforme schema definido
5. **Controlador** → Processa requisição e delega para a camada de serviço
6. **Serviço** → Executa lógica de negócio e interage com o banco de dados
7. **Modelo** → Mapeia e valida dados com o schema do banco
8. **Resposta HTTP** → Retorna resposta formatada (JSON) ao cliente

## Autenticação e Autorização

### Autenticação

- **Método:** JWT (JSON Web Token)
- **Header:** `Authorization: Bearer <token>`
- Tokens são validados em cada requisição através de middleware dedicado
- Tokens expiram após período configurado (geralmente 24h)

### Autorização

- **Baseada em Roles:** Diferentes níveis de acesso (admin, operador, viewer)
- **Permissões por Endpoint:**
  - `GET` endpoints: Requerem role mínima de `viewer`
  - `POST/PUT` endpoints: Requerem role mínima de `operador`
  - `DELETE` endpoints: Requerem role de `admin`

### Fluxo de Autenticação

1. Cliente autentica via endpoint de login (geralmente em API separada)
2. Recebe token JWT com claims (userId, roles, permissions)
3. Inclui token no header de todas as requisições subsequentes
4. API valida token e extrai informações do usuário
5. Middleware de autorização verifica se role possui permissão para o endpoint
