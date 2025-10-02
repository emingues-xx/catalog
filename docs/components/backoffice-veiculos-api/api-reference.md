# API Reference - Backoffice Veículos API

## Visão Geral

A API de Backoffice de Veículos fornece endpoints para gerenciamento completo de veículos, incluindo cadastro, consulta, atualização e remoção de registros.

**Base URL:** `https://api.example.com/v1`

**Autenticação:** Todas as requisições requerem autenticação via Bearer Token no header `Authorization`.

```
Authorization: Bearer {seu_token_jwt}
```

---

## Endpoints

### 1. Listar Veículos

Retorna uma lista paginada de veículos cadastrados.

**Endpoint:** `GET /veiculos`

**Parâmetros de Query:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| page | integer | Não | Número da página (padrão: 1) |
| limit | integer | Não | Itens por página (padrão: 20, máx: 100) |
| marca | string | Não | Filtrar por marca |
| modelo | string | Não | Filtrar por modelo |
| ano | integer | Não | Filtrar por ano |
| status | string | Não | Filtrar por status (ativo, inativo, vendido) |

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.example.com/v1/veiculos?page=1&limit=10&marca=Toyota" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Exemplo de Resposta (200 OK):**

```json
{
  "data": [
    {
      "id": "uuid-1234-5678",
      "marca": "Toyota",
      "modelo": "Corolla",
      "ano": 2023,
      "cor": "Preto",
      "placa": "ABC-1234",
      "chassi": "9BWZZZ377VT004251",
      "km": 15000,
      "preco": 95000.00,
      "status": "ativo",
      "createdAt": "2024-01-15T10:30:00Z",
      "updatedAt": "2024-01-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 150,
    "totalPages": 15
  }
}
```

**Códigos de Status:**

- `200 OK` - Sucesso
- `401 Unauthorized` - Token inválido ou ausente
- `403 Forbidden` - Sem permissão para acessar
- `500 Internal Server Error` - Erro interno do servidor

---

### 2. Buscar Veículo por ID

Retorna os detalhes de um veículo específico.

**Endpoint:** `GET /veiculos/{id}`

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | string (UUID) | ID único do veículo |

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.example.com/v1/veiculos/uuid-1234-5678" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Exemplo de Resposta (200 OK):**

```json
{
  "id": "uuid-1234-5678",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2023,
  "cor": "Preto",
  "placa": "ABC-1234",
  "chassi": "9BWZZZ377VT004251",
  "km": 15000,
  "preco": 95000.00,
  "status": "ativo",
  "proprietarioId": "uuid-owner-123",
  "observacoes": "Veículo em excelente estado",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z"
}
```

**Códigos de Status:**

- `200 OK` - Sucesso
- `401 Unauthorized` - Token inválido ou ausente
- `404 Not Found` - Veículo não encontrado
- `500 Internal Server Error` - Erro interno do servidor

---

### 3. Criar Veículo

Cadastra um novo veículo no sistema.

**Endpoint:** `POST /veiculos`

**Body (JSON):**

```json
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2023,
  "cor": "Preto",
  "placa": "ABC-1234",
  "chassi": "9BWZZZ377VT004251",
  "km": 15000,
  "preco": 95000.00,
  "status": "ativo",
  "proprietarioId": "uuid-owner-123",
  "observacoes": "Veículo em excelente estado"
}
```

**Campos Obrigatórios:**

| Campo | Tipo | Descrição |
|-------|------|-----------|
| marca | string | Marca do veículo |
| modelo | string | Modelo do veículo |
| ano | integer | Ano de fabricação (entre 1900 e ano atual + 1) |
| placa | string | Placa do veículo (formato: ABC-1234 ou ABC1D23) |
| chassi | string | Número do chassi (17 caracteres) |
| km | integer | Quilometragem atual |
| preco | number | Preço do veículo |
| status | string | Status (ativo, inativo, vendido) |

**Exemplo de Requisição:**

```bash
curl -X POST "https://api.example.com/v1/veiculos" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2023,
    "cor": "Preto",
    "placa": "ABC-1234",
    "chassi": "9BWZZZ377VT004251",
    "km": 15000,
    "preco": 95000.00,
    "status": "ativo"
  }'
```

**Exemplo de Resposta (201 Created):**

```json
{
  "id": "uuid-1234-5678",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2023,
  "cor": "Preto",
  "placa": "ABC-1234",
  "chassi": "9BWZZZ377VT004251",
  "km": 15000,
  "preco": 95000.00,
  "status": "ativo",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z"
}
```

**Códigos de Status:**

- `201 Created` - Veículo criado com sucesso
- `400 Bad Request` - Dados inválidos ou faltando campos obrigatórios
- `401 Unauthorized` - Token inválido ou ausente
- `409 Conflict` - Placa ou chassi já cadastrados
- `500 Internal Server Error` - Erro interno do servidor

---

### 4. Atualizar Veículo

Atualiza os dados de um veículo existente.

**Endpoint:** `PUT /veiculos/{id}`

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | string (UUID) | ID único do veículo |

**Body (JSON):** Todos os campos são opcionais

```json
{
  "marca": "Toyota",
  "modelo": "Corolla XEI",
  "ano": 2023,
  "cor": "Prata",
  "km": 16500,
  "preco": 93000.00,
  "status": "ativo",
  "observacoes": "Preço atualizado"
}
```

**Exemplo de Requisição:**

```bash
curl -X PUT "https://api.example.com/v1/veiculos/uuid-1234-5678" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "km": 16500,
    "preco": 93000.00
  }'
```

**Exemplo de Resposta (200 OK):**

```json
{
  "id": "uuid-1234-5678",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2023,
  "cor": "Preto",
  "placa": "ABC-1234",
  "chassi": "9BWZZZ377VT004251",
  "km": 16500,
  "preco": 93000.00,
  "status": "ativo",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-16T14:20:00Z"
}
```

**Códigos de Status:**

- `200 OK` - Veículo atualizado com sucesso
- `400 Bad Request` - Dados inválidos
- `401 Unauthorized` - Token inválido ou ausente
- `404 Not Found` - Veículo não encontrado
- `500 Internal Server Error` - Erro interno do servidor

---

### 5. Atualizar Parcialmente Veículo

Atualiza apenas campos específicos de um veículo.

**Endpoint:** `PATCH /veiculos/{id}`

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | string (UUID) | ID único do veículo |

**Body (JSON):** Apenas campos que deseja atualizar

```json
{
  "status": "vendido",
  "observacoes": "Vendido em 16/01/2024"
}
```

**Exemplo de Requisição:**

```bash
curl -X PATCH "https://api.example.com/v1/veiculos/uuid-1234-5678" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "status": "vendido"
  }'
```

**Exemplo de Resposta (200 OK):**

```json
{
  "id": "uuid-1234-5678",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2023,
  "cor": "Preto",
  "placa": "ABC-1234",
  "chassi": "9BWZZZ377VT004251",
  "km": 16500,
  "preco": 93000.00,
  "status": "vendido",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-16T15:45:00Z"
}
```

**Códigos de Status:**

- `200 OK` - Veículo atualizado com sucesso
- `400 Bad Request` - Dados inválidos
- `401 Unauthorized` - Token inválido ou ausente
- `404 Not Found` - Veículo não encontrado
- `500 Internal Server Error` - Erro interno do servidor

---

### 6. Deletar Veículo

Remove um veículo do sistema (soft delete).

**Endpoint:** `DELETE /veiculos/{id}`

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| id | string (UUID) | ID único do veículo |

**Exemplo de Requisição:**

```bash
curl -X DELETE "https://api.example.com/v1/veiculos/uuid-1234-5678" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Exemplo de Resposta (204 No Content):**

```
(sem corpo de resposta)
```

**Códigos de Status:**

- `204 No Content` - Veículo deletado com sucesso
- `401 Unauthorized` - Token inválido ou ausente
- `404 Not Found` - Veículo não encontrado
- `500 Internal Server Error` - Erro interno do servidor

---

### 7. Buscar Veículo por Placa

Busca um veículo específico pela placa.

**Endpoint:** `GET /veiculos/placa/{placa}`

**Parâmetros de Path:**

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| placa | string | Placa do veículo (ABC-1234 ou ABC1D23) |

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.example.com/v1/veiculos/placa/ABC-1234" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Exemplo de Resposta (200 OK):**

```json
{
  "id": "uuid-1234-5678",
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2023,
  "cor": "Preto",
  "placa": "ABC-1234",
  "chassi": "9BWZZZ377VT004251",
  "km": 15000,
  "preco": 95000.00,
  "status": "ativo",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z"
}
```

**Códigos de Status:**

- `200 OK` - Sucesso
- `401 Unauthorized` - Token inválido ou ausente
- `404 Not Found` - Veículo não encontrado
- `500 Internal Server Error` - Erro interno do servidor

---

### 8. Estatísticas de Veículos

Retorna estatísticas gerais sobre os veículos cadastrados.

**Endpoint:** `GET /veiculos/stats`

**Exemplo de Requisição:**

```bash
curl -X GET "https://api.example.com/v1/veiculos/stats" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Exemplo de Resposta (200 OK):**

```json
{
  "total": 150,
  "porStatus": {
    "ativo": 120,
    "inativo": 15,
    "vendido": 15
  },
  "porMarca": {
    "Toyota": 45,
    "Honda": 30,
    "Volkswagen": 25,
    "Outros": 50
  },
  "mediaPreco": 87500.00,
  "mediaKm": 35000
}
```

**Códigos de Status:**

- `200 OK` - Sucesso
- `401 Unauthorized` - Token inválido ou ausente
- `500 Internal Server Error` - Erro interno do servidor

---

## Modelos de Dados

### Veículo

```typescript
{
  id: string;              // UUID único
  marca: string;           // Marca do veículo
  modelo: string;          // Modelo do veículo
  ano: number;             // Ano de fabricação
  cor: string;             // Cor do veículo
  placa: string;           // Placa (ABC-1234 ou ABC1D23)
  chassi: string;          // Número do chassi (17 caracteres)
  km: number;              // Quilometragem
  preco: number;           // Preço (decimal)
  status: string;          // Status: "ativo" | "inativo" | "vendido"
  proprietarioId?: string; // UUID do proprietário (opcional)
  observacoes?: string;    // Observações adicionais (opcional)
  createdAt: string;       // Data de criação (ISO 8601)
  updatedAt: string;       // Data de atualização (ISO 8601)
}
```

---

## Tratamento de Erros

Todos os erros seguem o padrão:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Descrição legível do erro",
    "details": {
      "field": "campo_com_erro",
      "reason": "Motivo específico"
    }
  }
}
```

### Códigos de Erro Comuns

| Código | Status HTTP | Descrição |
|--------|-------------|-----------|
| INVALID_TOKEN | 401 | Token JWT inválido ou expirado |
| MISSING_TOKEN | 401 | Token não fornecido |
| INSUFFICIENT_PERMISSIONS | 403 | Usuário sem permissões necessárias |
| RESOURCE_NOT_FOUND | 404 | Recurso não encontrado |
| VALIDATION_ERROR | 400 | Erro de validação nos dados |
| DUPLICATE_PLATE | 409 | Placa já cadastrada |
| DUPLICATE_CHASSI | 409 | Chassi já cadastrado |
| INTERNAL_ERROR | 500 | Erro interno do servidor |

---

## Rate Limiting

A API possui limites de taxa para prevenir abuso:

- **100 requisições por minuto** por token
- **10.000 requisições por dia** por token

Headers de resposta incluem informações sobre o rate limit:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642259400
```

Quando o limite é excedido, a API retorna:

**Status:** `429 Too Many Requests`

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Limite de requisições excedido. Tente novamente em 60 segundos."
  }
}
```

---

## Versionamento

A API utiliza versionamento via URL. A versão atual é `v1`.

Exemplo: `https://api.example.com/v1/veiculos`

Mudanças breaking resultarão em uma nova versão (v2, v3, etc.). Versões antigas serão mantidas por no mínimo 12 meses após o lançamento de uma nova versão.

---

## Ambientes

| Ambiente | Base URL | Descrição |
|----------|----------|-----------|
| Produção | `https://api.example.com/v1` | Ambiente de produção |
| Staging | `https://api-staging.example.com/v1` | Ambiente de testes |
| Desenvolvimento | `https://api-dev.example.com/v1` | Ambiente de desenvolvimento |

---

## Suporte

Para dúvidas ou problemas com a API, entre em contato:

- **Email:** api-support@example.com
- **Documentação:** https://docs.example.com
- **Status da API:** https://status.example.com
