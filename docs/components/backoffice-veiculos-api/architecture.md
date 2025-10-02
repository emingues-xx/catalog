# Arquitetura - backoffice-veiculos-api

## Visão Geral

A **backoffice-veiculos-api** é uma API REST backend responsável pelo gerenciamento de veículos no sistema de backoffice. Desenvolvida para fornecer operações CRUD e funcionalidades relacionadas ao cadastro, consulta e manutenção de informações de veículos.

## Endpoints Principais

### Veículos
- `GET /api/veiculos` - Lista todos os veículos
- `GET /api/veiculos/{id}` - Consulta um veículo específico
- `POST /api/veiculos` - Cadastra um novo veículo
- `PUT /api/veiculos/{id}` - Atualiza dados de um veículo
- `DELETE /api/veiculos/{id}` - Remove um veículo do sistema

### Health Check
- `GET /health` - Verifica o status da API
- `GET /metrics` - Métricas de monitoramento

## Estrutura de Pastas

```
backoffice-veiculos-api/
├── src/
│   ├── controllers/       # Controladores das rotas
│   ├── services/          # Lógica de negócio
│   ├── models/            # Modelos de dados
│   ├── repositories/      # Camada de acesso a dados
│   ├── middlewares/       # Middlewares (auth, validação)
│   ├── config/            # Configurações da aplicação
│   └── utils/             # Utilitários e helpers
├── tests/                 # Testes unitários e integração
├── docs/                  # Documentação adicional
└── package.json
```

## Fluxo de Dados

```
Cliente HTTP → Controller → Service → Repository → Banco de Dados
                    ↓           ↓
                Validação   Lógica de Negócio
```

1. **Controller**: Recebe requisições HTTP, valida parâmetros e delega para o service
2. **Service**: Implementa regras de negócio e orquestra operações
3. **Repository**: Abstrai acesso ao banco de dados
4. **Model**: Define estrutura e validação de dados

## Autenticação e Autorização

### Autenticação
- **Tipo**: JWT (JSON Web Token)
- **Header**: `Authorization: Bearer <token>`
- **Validação**: Middleware de autenticação em todas as rotas protegidas

### Autorização
- **Controle de Acesso**: Baseado em roles/permissões
- **Níveis de Acesso**:
  - `ADMIN`: Acesso completo (CRUD)
  - `EDITOR`: Criação e edição
  - `VIEWER`: Apenas leitura

### Fluxo de Segurança
1. Cliente envia token JWT no header
2. Middleware valida token e extrai informações do usuário
3. Verifica permissões necessárias para a operação
4. Processa requisição ou retorna erro 401/403
