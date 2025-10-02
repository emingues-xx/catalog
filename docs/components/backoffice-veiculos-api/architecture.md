# Arquitetura - backoffice-veiculos-api

## Visão Geral

A `backoffice-veiculos-api` é uma API REST desenvolvida para gerenciar operações de backoffice relacionadas a veículos. A arquitetura segue os princípios de separação de responsabilidades e design orientado a serviços.

## Endpoints Principais

### Veículos
- `GET /api/veiculos` - Lista todos os veículos
- `GET /api/veiculos/:id` - Busca veículo específico
- `POST /api/veiculos` - Cria novo veículo
- `PUT /api/veiculos/:id` - Atualiza veículo existente
- `DELETE /api/veiculos/:id` - Remove veículo

### Categorias
- `GET /api/categorias` - Lista categorias de veículos
- `POST /api/categorias` - Cria nova categoria

### Relatórios
- `GET /api/relatorios/veiculos` - Relatórios gerenciais de veículos
- `GET /api/relatorios/estatisticas` - Estatísticas consolidadas

## Estrutura de Pastas

```
backoffice-veiculos-api/
├── src/
│   ├── controllers/       # Controladores de requisições
│   ├── services/          # Lógica de negócio
│   ├── models/            # Modelos de dados
│   ├── routes/            # Definição de rotas
│   ├── middleware/        # Middlewares (auth, validação)
│   ├── config/            # Configurações da aplicação
│   ├── utils/             # Funções utilitárias
│   └── database/          # Conexão e migrations
├── tests/                 # Testes unitários e integração
└── docs/                  # Documentação adicional
```

## Fluxo de Dados

1. **Requisição HTTP** → Cliente envia requisição para a API
2. **Middleware de Autenticação** → Valida token JWT
3. **Roteamento** → Direciona para o controller apropriado
4. **Controller** → Recebe requisição e delega para service
5. **Service** → Executa lógica de negócio
6. **Model/Repository** → Interage com banco de dados
7. **Resposta** → Retorna dados formatados ao cliente

### Diagrama de Fluxo
```
Cliente → API Gateway → Auth Middleware → Routes → Controllers → Services → Models → Database
                                                                      ↓
                                                                  Response
```

## Autenticação e Autorização

### Autenticação
- Utiliza **JWT (JSON Web Token)** para autenticação
- Tokens são gerados no login e validados em cada requisição
- Expiração configurável (padrão: 24 horas)

### Autorização
- **Roles baseadas em permissões:**
  - `admin` - Acesso completo a todas as operações
  - `manager` - Leitura e criação de veículos
  - `viewer` - Apenas leitura

### Headers Obrigatórios
```
Authorization: Bearer <token>
Content-Type: application/json
```

### Middleware de Segurança
- Rate limiting para prevenir abuso
- CORS configurado para domínios autorizados
- Validação de entrada para prevenir injeção
- Sanitização de dados sensíveis nos logs
