# API Reference - Backoffice Veículos API

## Visão Geral

API RESTful para gerenciamento de veículos no sistema de backoffice. Fornece endpoints para operações CRUD completas de veículos, consultas avançadas e gestão de documentação.

**Base URL:** `https://api.exemplo.com/v1`

**Autenticação:** Bearer Token (JWT)

Todas as requisições devem incluir o header:
```
Authorization: Bearer {token}
```

---

## Endpoints

### 1. Listar Veículos

Retorna uma lista paginada de veículos cadastrados.

**Endpoint:** `GET /vehicles`

**Autenticação:** Obrigatória

**Parâmetros de Query:**

| Parâmetro | Tipo | Obrigatório | Descrição | Padrão |
|-----------|------|-------------|-----------|---------|
| page | integer | Não | Número da página | 1 |
| limit | integer | Não | Itens por página (máx: 100) | 20 |
| status | string | Não | Filtrar por status: `active`, `inactive`, `maintenance` | - |
| brand | string | Não | Filtrar por marca | - |
| model | string | Não | Filtrar por modelo | - |
| year_min | integer | Não | Ano mínimo de fabricação | - |
| year_max | integer | Não | Ano máximo de fabricação | - |
| sort_by | string | Não | Campo para ordenação: `created_at`, `updated_at`, `brand`, `model` | created_at |
| sort_order | string | Não | Ordem: `asc`, `desc` | desc |

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.exemplo.com/v1/vehicles?page=1&limit=10&status=active&brand=Toyota" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**

```json
{
  "success": true,
  "data": {
    "vehicles": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "plate": "ABC-1234",
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2022,
        "color": "Prata",
        "status": "active",
        "mileage": 15000,
        "fuel_type": "flex",
        "chassis": "9BWZZZ377VT004251",
        "renavam": "00123456789",
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-20T14:45:00Z"
      }
    ],
    "pagination": {
      "current_page": 1,
      "total_pages": 5,
      "total_items": 47,
      "items_per_page": 10
    }
  }
}
```

**Códigos de Status:**

- `200` - Sucesso
- `401` - Não autenticado
- `403` - Sem permissão
- `500` - Erro interno do servidor

---

### 2. Buscar Veículo por ID

Retorna os detalhes completos de um veículo específico.

**Endpoint:** `GET /vehicles/{id}`

**Autenticação:** Obrigatória

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | UUID | ID do veículo |

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.exemplo.com/v1/vehicles/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**

```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "plate": "ABC-1234",
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "color": "Prata",
    "status": "active",
    "mileage": 15000,
    "fuel_type": "flex",
    "chassis": "9BWZZZ377VT004251",
    "renavam": "00123456789",
    "purchase_date": "2022-03-15",
    "purchase_price": 95000.00,
    "current_value": 85000.00,
    "insurance": {
      "company": "Seguradora XYZ",
      "policy_number": "POL-123456",
      "expiry_date": "2025-03-15"
    },
    "maintenance_history": [
      {
        "date": "2024-01-10",
        "type": "Revisão",
        "description": "Troca de óleo e filtros",
        "cost": 450.00
      }
    ],
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-20T14:45:00Z"
  }
}
```

**Códigos de Status:**

- `200` - Sucesso
- `401` - Não autenticado
- `403` - Sem permissão
- `404` - Veículo não encontrado
- `500` - Erro interno do servidor

---

### 3. Criar Veículo

Cadastra um novo veículo no sistema.

**Endpoint:** `POST /vehicles`

**Autenticação:** Obrigatória

**Corpo da Requisição:**

```json
{
  "plate": "ABC-1234",
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2022,
  "color": "Prata",
  "status": "active",
  "mileage": 15000,
  "fuel_type": "flex",
  "chassis": "9BWZZZ377VT004251",
  "renavam": "00123456789",
  "purchase_date": "2022-03-15",
  "purchase_price": 95000.00,
  "current_value": 85000.00,
  "insurance": {
    "company": "Seguradora XYZ",
    "policy_number": "POL-123456",
    "expiry_date": "2025-03-15"
  }
}
```

**Campos Obrigatórios:**

- `plate` (string): Placa do veículo (formato brasileiro)
- `brand` (string): Marca do veículo
- `model` (string): Modelo do veículo
- `year` (integer): Ano de fabricação
- `chassis` (string): Número do chassis
- `renavam` (string): Número do RENAVAM

**Campos Opcionais:**

- `color` (string): Cor do veículo
- `status` (string): Status inicial (padrão: `active`)
- `mileage` (integer): Quilometragem atual
- `fuel_type` (string): Tipo de combustível
- `purchase_date` (date): Data de aquisição
- `purchase_price` (decimal): Preço de aquisição
- `current_value` (decimal): Valor atual
- `insurance` (object): Dados do seguro

**Exemplo de Requisição:**

```bash
curl -X POST "https://api.exemplo.com/v1/vehicles" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "plate": "ABC-1234",
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "chassis": "9BWZZZ377VT004251",
    "renavam": "00123456789"
  }'
```

**Resposta de Sucesso (201 Created):**

```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "plate": "ABC-1234",
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "status": "active",
    "chassis": "9BWZZZ377VT004251",
    "renavam": "00123456789",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
  },
  "message": "Veículo criado com sucesso"
}
```

**Códigos de Status:**

- `201` - Criado com sucesso
- `400` - Dados inválidos
- `401` - Não autenticado
- `403` - Sem permissão
- `409` - Veículo já cadastrado (placa duplicada)
- `500` - Erro interno do servidor

---

### 4. Atualizar Veículo

Atualiza os dados de um veículo existente.

**Endpoint:** `PUT /vehicles/{id}`

**Autenticação:** Obrigatória

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | UUID | ID do veículo |

**Corpo da Requisição:**

```json
{
  "color": "Preto",
  "status": "maintenance",
  "mileage": 18500,
  "current_value": 82000.00
}
```

**Exemplo de Requisição:**

```bash
curl -X PUT "https://api.exemplo.com/v1/vehicles/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "mileage": 18500,
    "status": "maintenance"
  }'
```

**Resposta de Sucesso (200 OK):**

```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "plate": "ABC-1234",
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "color": "Prata",
    "status": "maintenance",
    "mileage": 18500,
    "updated_at": "2024-01-25T16:20:00Z"
  },
  "message": "Veículo atualizado com sucesso"
}
```

**Códigos de Status:**

- `200` - Atualizado com sucesso
- `400` - Dados inválidos
- `401` - Não autenticado
- `403` - Sem permissão
- `404` - Veículo não encontrado
- `500` - Erro interno do servidor

---

### 5. Atualizar Parcialmente Veículo

Atualiza apenas campos específicos de um veículo.

**Endpoint:** `PATCH /vehicles/{id}`

**Autenticação:** Obrigatória

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | UUID | ID do veículo |

**Exemplo de Requisição:**

```bash
curl -X PATCH "https://api.exemplo.com/v1/vehicles/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "status": "active"
  }'
```

**Resposta de Sucesso (200 OK):**

```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "status": "active",
    "updated_at": "2024-01-26T09:15:00Z"
  },
  "message": "Veículo atualizado com sucesso"
}
```

**Códigos de Status:**

- `200` - Atualizado com sucesso
- `400` - Dados inválidos
- `401` - Não autenticado
- `403` - Sem permissão
- `404` - Veículo não encontrado
- `500` - Erro interno do servidor

---

### 6. Deletar Veículo

Remove um veículo do sistema (soft delete).

**Endpoint:** `DELETE /vehicles/{id}`

**Autenticação:** Obrigatória

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | UUID | ID do veículo |

**Parâmetros de Query:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| permanent | boolean | Não | Se `true`, deleta permanentemente | false |

**Exemplo de Requisição:**

```bash
curl -X DELETE "https://api.exemplo.com/v1/vehicles/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**

```json
{
  "success": true,
  "message": "Veículo removido com sucesso"
}
```

**Códigos de Status:**

- `200` - Removido com sucesso
- `401` - Não autenticado
- `403` - Sem permissão
- `404` - Veículo não encontrado
- `500` - Erro interno do servidor

---

### 7. Adicionar Manutenção

Registra uma manutenção realizada no veículo.

**Endpoint:** `POST /vehicles/{id}/maintenance`

**Autenticação:** Obrigatória

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | UUID | ID do veículo |

**Corpo da Requisição:**

```json
{
  "date": "2024-01-20",
  "type": "Revisão",
  "description": "Troca de óleo e filtros",
  "cost": 450.00,
  "mileage": 20000,
  "workshop": "Oficina ABC Ltda",
  "next_maintenance_date": "2024-07-20",
  "next_maintenance_mileage": 30000
}
```

**Campos Obrigatórios:**

- `date` (date): Data da manutenção
- `type` (string): Tipo de manutenção
- `description` (string): Descrição da manutenção
- `cost` (decimal): Custo da manutenção

**Exemplo de Requisição:**

```bash
curl -X POST "https://api.exemplo.com/v1/vehicles/550e8400-e29b-41d4-a716-446655440000/maintenance" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-01-20",
    "type": "Revisão",
    "description": "Troca de óleo e filtros",
    "cost": 450.00
  }'
```

**Resposta de Sucesso (201 Created):**

```json
{
  "success": true,
  "data": {
    "id": "650e8400-e29b-41d4-a716-446655440001",
    "vehicle_id": "550e8400-e29b-41d4-a716-446655440000",
    "date": "2024-01-20",
    "type": "Revisão",
    "description": "Troca de óleo e filtros",
    "cost": 450.00,
    "created_at": "2024-01-20T10:30:00Z"
  },
  "message": "Manutenção registrada com sucesso"
}
```

**Códigos de Status:**

- `201` - Criado com sucesso
- `400` - Dados inválidos
- `401` - Não autenticado
- `403` - Sem permissão
- `404` - Veículo não encontrado
- `500` - Erro interno do servidor

---

### 8. Listar Histórico de Manutenção

Retorna o histórico completo de manutenções de um veículo.

**Endpoint:** `GET /vehicles/{id}/maintenance`

**Autenticação:** Obrigatória

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | UUID | ID do veículo |

**Parâmetros de Query:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| start_date | date | Não | Data inicial do período | - |
| end_date | date | Não | Data final do período | - |
| type | string | Não | Filtrar por tipo de manutenção | - |

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.exemplo.com/v1/vehicles/550e8400-e29b-41d4-a716-446655440000/maintenance" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**

```json
{
  "success": true,
  "data": {
    "vehicle_id": "550e8400-e29b-41d4-a716-446655440000",
    "maintenance_history": [
      {
        "id": "650e8400-e29b-41d4-a716-446655440001",
        "date": "2024-01-20",
        "type": "Revisão",
        "description": "Troca de óleo e filtros",
        "cost": 450.00,
        "mileage": 20000,
        "workshop": "Oficina ABC Ltda"
      }
    ],
    "total_cost": 450.00,
    "total_records": 1
  }
}
```

**Códigos de Status:**

- `200` - Sucesso
- `401` - Não autenticado
- `403` - Sem permissão
- `404` - Veículo não encontrado
- `500` - Erro interno do servidor

---

### 9. Buscar por Placa

Busca um veículo pela placa.

**Endpoint:** `GET /vehicles/plate/{plate}`

**Autenticação:** Obrigatória

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| plate | string | Placa do veículo (sem hífens) |

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.exemplo.com/v1/vehicles/plate/ABC1234" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta:** Mesma estrutura do endpoint GET /vehicles/{id}

**Códigos de Status:**

- `200` - Sucesso
- `401` - Não autenticado
- `403` - Sem permissão
- `404` - Veículo não encontrado
- `500` - Erro interno do servidor

---

### 10. Relatório de Veículos

Gera relatório consolidado de veículos.

**Endpoint:** `GET /vehicles/reports/summary`

**Autenticação:** Obrigatória

**Parâmetros de Query:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| format | string | Não | Formato do relatório: `json`, `csv`, `pdf` | json |
| group_by | string | Não | Agrupar por: `brand`, `status`, `year` | - |

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.exemplo.com/v1/vehicles/reports/summary?group_by=status" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**

```json
{
  "success": true,
  "data": {
    "total_vehicles": 47,
    "by_status": {
      "active": 35,
      "maintenance": 8,
      "inactive": 4
    },
    "total_value": 3950000.00,
    "average_age": 3.2,
    "total_maintenance_cost": 125000.00,
    "generated_at": "2024-01-26T10:00:00Z"
  }
}
```

**Códigos de Status:**

- `200` - Sucesso
- `401` - Não autenticado
- `403` - Sem permissão
- `500` - Erro interno do servidor

---

## Modelos de Dados

### Vehicle

```json
{
  "id": "UUID",
  "plate": "string",
  "brand": "string",
  "model": "string",
  "year": "integer",
  "color": "string",
  "status": "enum[active, inactive, maintenance, sold]",
  "mileage": "integer",
  "fuel_type": "enum[gasoline, ethanol, flex, diesel, electric, hybrid]",
  "chassis": "string",
  "renavam": "string",
  "purchase_date": "date",
  "purchase_price": "decimal",
  "current_value": "decimal",
  "insurance": "Insurance",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Insurance

```json
{
  "company": "string",
  "policy_number": "string",
  "expiry_date": "date"
}
```

### Maintenance

```json
{
  "id": "UUID",
  "vehicle_id": "UUID",
  "date": "date",
  "type": "string",
  "description": "string",
  "cost": "decimal",
  "mileage": "integer",
  "workshop": "string",
  "next_maintenance_date": "date",
  "next_maintenance_mileage": "integer",
  "created_at": "datetime"
}
```

---

## Códigos de Erro

### Estrutura de Erro

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Mensagem descritiva do erro",
    "details": {}
  }
}
```

### Códigos Comuns

| Código | Status HTTP | Descrição |
|--------|-------------|-----------|
| UNAUTHORIZED | 401 | Token de autenticação ausente ou inválido |
| FORBIDDEN | 403 | Usuário sem permissão para a operação |
| NOT_FOUND | 404 | Recurso não encontrado |
| VALIDATION_ERROR | 400 | Dados de entrada inválidos |
| DUPLICATE_PLATE | 409 | Placa já cadastrada no sistema |
| INTERNAL_ERROR | 500 | Erro interno do servidor |

---

## Rate Limiting

- **Limite:** 1000 requisições por hora por token
- **Headers de resposta:**
  - `X-RateLimit-Limit`: Limite total
  - `X-RateLimit-Remaining`: Requisições restantes
  - `X-RateLimit-Reset`: Timestamp de reset do limite

**Resposta ao exceder o limite (429 Too Many Requests):**

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Limite de requisições excedido. Tente novamente em 15 minutos."
  }
}
```

---

## Versionamento

A API utiliza versionamento na URL. A versão atual é `v1`.

Versões anteriores serão mantidas por no mínimo 12 meses após a liberação de uma nova versão.

---

## Ambientes

| Ambiente | Base URL |
|----------|----------|
| Produção | `https://api.exemplo.com/v1` |
| Staging | `https://api-staging.exemplo.com/v1` |
| Desenvolvimento | `https://api-dev.exemplo.com/v1` |

---

## Suporte

Para questões ou problemas relacionados à API:

- **Email:** api-support@exemplo.com
- **Documentação:** https://docs.exemplo.com
- **Status da API:** https://status.exemplo.com
