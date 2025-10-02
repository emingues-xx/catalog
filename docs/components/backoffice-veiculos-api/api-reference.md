# API Reference - Backoffice Veículos API

## Visão Geral

Esta documentação detalha todos os endpoints disponíveis na API de Backoffice de Veículos.

**Base URL:** `https://api.example.com/v1`

**Autenticação:** Todas as requisições requerem um token JWT no header `Authorization: Bearer {token}`

---

## Endpoints

### Veículos

#### 1. Listar Veículos

```http
GET /veiculos
```

**Descrição:** Retorna uma lista paginada de veículos cadastrados.

**Parâmetros de Query:**
- `page` (integer, opcional): Número da página (padrão: 1)
- `limit` (integer, opcional): Itens por página (padrão: 20, máx: 100)
- `status` (string, opcional): Filtrar por status (`ativo`, `inativo`, `manutencao`)
- `placa` (string, opcional): Buscar por placa

**Headers:**
```
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Exemplo de Requisição:**
```bash
curl -X GET "https://api.example.com/v1/veiculos?page=1&limit=20&status=ativo" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**
```json
{
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "placa": "ABC-1234",
      "modelo": "Fiat Uno",
      "ano": 2020,
      "cor": "Branco",
      "status": "ativo",
      "km_atual": 45000,
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-20T14:45:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "total_pages": 8
  }
}
```

**Códigos de Status:**
- `200 OK`: Requisição bem-sucedida
- `401 Unauthorized`: Token inválido ou ausente
- `400 Bad Request`: Parâmetros inválidos

---

#### 2. Buscar Veículo por ID

```http
GET /veiculos/{id}
```

**Descrição:** Retorna os detalhes de um veículo específico.

**Parâmetros de Path:**
- `id` (uuid, obrigatório): ID único do veículo

**Headers:**
```
Authorization: Bearer {jwt_token}
```

**Exemplo de Requisição:**
```bash
curl -X GET "https://api.example.com/v1/veiculos/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "placa": "ABC-1234",
  "modelo": "Fiat Uno",
  "ano": 2020,
  "cor": "Branco",
  "status": "ativo",
  "km_atual": 45000,
  "chassi": "9BWZZZ377VT004251",
  "renavam": "12345678901",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-20T14:45:00Z"
}
```

**Códigos de Status:**
- `200 OK`: Veículo encontrado
- `404 Not Found`: Veículo não existe
- `401 Unauthorized`: Token inválido

---

#### 3. Criar Novo Veículo

```http
POST /veiculos
```

**Descrição:** Cadastra um novo veículo no sistema.

**Headers:**
```
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "placa": "XYZ-5678",
  "modelo": "Volkswagen Gol",
  "ano": 2022,
  "cor": "Prata",
  "chassi": "9BWAA05U08P042579",
  "renavam": "98765432109",
  "km_atual": 15000,
  "status": "ativo"
}
```

**Campos Obrigatórios:**
- `placa` (string): Placa do veículo (formato: ABC-1234)
- `modelo` (string): Modelo do veículo
- `ano` (integer): Ano de fabricação
- `chassi` (string): Número do chassi
- `renavam` (string): Número do RENAVAM

**Campos Opcionais:**
- `cor` (string): Cor do veículo
- `km_atual` (integer): Quilometragem atual (padrão: 0)
- `status` (string): Status inicial (padrão: "ativo")

**Exemplo de Requisição:**
```bash
curl -X POST "https://api.example.com/v1/veiculos" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "placa": "XYZ-5678",
    "modelo": "Volkswagen Gol",
    "ano": 2022,
    "cor": "Prata",
    "chassi": "9BWAA05U08P042579",
    "renavam": "98765432109",
    "km_atual": 15000
  }'
```

**Resposta de Sucesso (201 Created):**
```json
{
  "id": "660e9511-f39c-52e5-b827-557766551111",
  "placa": "XYZ-5678",
  "modelo": "Volkswagen Gol",
  "ano": 2022,
  "cor": "Prata",
  "status": "ativo",
  "km_atual": 15000,
  "chassi": "9BWAA05U08P042579",
  "renavam": "98765432109",
  "created_at": "2024-02-01T09:15:00Z",
  "updated_at": "2024-02-01T09:15:00Z"
}
```

**Códigos de Status:**
- `201 Created`: Veículo criado com sucesso
- `400 Bad Request`: Dados inválidos ou incompletos
- `409 Conflict`: Placa ou chassi já cadastrado
- `401 Unauthorized`: Token inválido

---

#### 4. Atualizar Veículo

```http
PUT /veiculos/{id}
```

**Descrição:** Atualiza os dados de um veículo existente.

**Parâmetros de Path:**
- `id` (uuid, obrigatório): ID do veículo

**Headers:**
```
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "km_atual": 47500,
  "status": "manutencao",
  "cor": "Branco Pérola"
}
```

**Campos Atualizáveis:**
- `km_atual` (integer)
- `status` (string): "ativo", "inativo", "manutencao"
- `cor` (string)

**Exemplo de Requisição:**
```bash
curl -X PUT "https://api.example.com/v1/veiculos/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "km_atual": 47500,
    "status": "manutencao"
  }'
```

**Resposta de Sucesso (200 OK):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "placa": "ABC-1234",
  "modelo": "Fiat Uno",
  "ano": 2020,
  "cor": "Branco Pérola",
  "status": "manutencao",
  "km_atual": 47500,
  "chassi": "9BWZZZ377VT004251",
  "renavam": "12345678901",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-02-05T16:20:00Z"
}
```

**Códigos de Status:**
- `200 OK`: Veículo atualizado com sucesso
- `404 Not Found`: Veículo não encontrado
- `400 Bad Request`: Dados inválidos
- `401 Unauthorized`: Token inválido

---

#### 5. Deletar Veículo

```http
DELETE /veiculos/{id}
```

**Descrição:** Remove um veículo do sistema (soft delete).

**Parâmetros de Path:**
- `id` (uuid, obrigatório): ID do veículo

**Headers:**
```
Authorization: Bearer {jwt_token}
```

**Exemplo de Requisição:**
```bash
curl -X DELETE "https://api.example.com/v1/veiculos/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (204 No Content):**
```
(sem corpo de resposta)
```

**Códigos de Status:**
- `204 No Content`: Veículo deletado com sucesso
- `404 Not Found`: Veículo não encontrado
- `401 Unauthorized`: Token inválido

---

### Manutenções

#### 6. Listar Manutenções de um Veículo

```http
GET /veiculos/{id}/manutencoes
```

**Descrição:** Retorna histórico de manutenções de um veículo.

**Parâmetros de Path:**
- `id` (uuid, obrigatório): ID do veículo

**Parâmetros de Query:**
- `page` (integer, opcional): Número da página
- `limit` (integer, opcional): Itens por página

**Headers:**
```
Authorization: Bearer {jwt_token}
```

**Exemplo de Requisição:**
```bash
curl -X GET "https://api.example.com/v1/veiculos/550e8400-e29b-41d4-a716-446655440000/manutencoes" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**
```json
{
  "data": [
    {
      "id": "770f9622-g40d-63f6-c938-668877662222",
      "veiculo_id": "550e8400-e29b-41d4-a716-446655440000",
      "tipo": "preventiva",
      "descricao": "Troca de óleo e filtros",
      "valor": 350.00,
      "km_realizada": 45000,
      "data_manutencao": "2024-01-20T08:00:00Z",
      "oficina": "Auto Center Silva",
      "created_at": "2024-01-20T14:45:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 5,
    "total_pages": 1
  }
}
```

**Códigos de Status:**
- `200 OK`: Lista retornada com sucesso
- `404 Not Found`: Veículo não encontrado
- `401 Unauthorized`: Token inválido

---

#### 7. Registrar Nova Manutenção

```http
POST /veiculos/{id}/manutencoes
```

**Descrição:** Registra uma nova manutenção para o veículo.

**Parâmetros de Path:**
- `id` (uuid, obrigatório): ID do veículo

**Headers:**
```
Authorization: Bearer {jwt_token}
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "tipo": "corretiva",
  "descricao": "Substituição de pastilhas de freio",
  "valor": 580.00,
  "km_realizada": 47500,
  "data_manutencao": "2024-02-05T10:00:00Z",
  "oficina": "Freios & Cia"
}
```

**Campos Obrigatórios:**
- `tipo` (string): "preventiva" ou "corretiva"
- `descricao` (string): Descrição da manutenção
- `valor` (number): Valor da manutenção
- `km_realizada` (integer): Quilometragem no momento da manutenção
- `data_manutencao` (datetime): Data/hora da manutenção

**Campos Opcionais:**
- `oficina` (string): Nome da oficina

**Exemplo de Requisição:**
```bash
curl -X POST "https://api.example.com/v1/veiculos/550e8400-e29b-41d4-a716-446655440000/manutencoes" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "tipo": "corretiva",
    "descricao": "Substituição de pastilhas de freio",
    "valor": 580.00,
    "km_realizada": 47500,
    "data_manutencao": "2024-02-05T10:00:00Z",
    "oficina": "Freios & Cia"
  }'
```

**Resposta de Sucesso (201 Created):**
```json
{
  "id": "880g0733-h51e-74g7-d049-779988773333",
  "veiculo_id": "550e8400-e29b-41d4-a716-446655440000",
  "tipo": "corretiva",
  "descricao": "Substituição de pastilhas de freio",
  "valor": 580.00,
  "km_realizada": 47500,
  "data_manutencao": "2024-02-05T10:00:00Z",
  "oficina": "Freios & Cia",
  "created_at": "2024-02-05T16:20:00Z"
}
```

**Códigos de Status:**
- `201 Created`: Manutenção registrada com sucesso
- `404 Not Found`: Veículo não encontrado
- `400 Bad Request`: Dados inválidos
- `401 Unauthorized`: Token inválido

---

### Autenticação

#### 8. Login

```http
POST /auth/login
```

**Descrição:** Realiza autenticação e retorna token JWT.

**Headers:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "email": "usuario@example.com",
  "password": "senha123"
}
```

**Exemplo de Requisição:**
```bash
curl -X POST "https://api.example.com/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@example.com",
    "password": "senha123"
  }'
```

**Resposta de Sucesso (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "token_type": "Bearer",
  "expires_in": 3600,
  "user": {
    "id": "990h1844-i62f-85h8-e150-880099884444",
    "email": "usuario@example.com",
    "name": "João Silva"
  }
}
```

**Códigos de Status:**
- `200 OK`: Login bem-sucedido
- `401 Unauthorized`: Credenciais inválidas
- `400 Bad Request`: Dados incompletos

---

#### 9. Refresh Token

```http
POST /auth/refresh
```

**Descrição:** Renova o token de acesso.

**Headers:**
```
Authorization: Bearer {jwt_token}
```

**Exemplo de Requisição:**
```bash
curl -X POST "https://api.example.com/v1/auth/refresh" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Resposta de Sucesso (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.newtoken...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Códigos de Status:**
- `200 OK`: Token renovado
- `401 Unauthorized`: Token inválido ou expirado

---

## Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| `200 OK` | Requisição bem-sucedida |
| `201 Created` | Recurso criado com sucesso |
| `204 No Content` | Operação bem-sucedida sem retorno |
| `400 Bad Request` | Dados inválidos ou incompletos |
| `401 Unauthorized` | Autenticação necessária ou falhou |
| `403 Forbidden` | Sem permissão para acessar recurso |
| `404 Not Found` | Recurso não encontrado |
| `409 Conflict` | Conflito de dados (ex: duplicação) |
| `422 Unprocessable Entity` | Validação de dados falhou |
| `500 Internal Server Error` | Erro interno do servidor |

---

## Tratamento de Erros

Todas as respostas de erro seguem o padrão:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos fornecidos",
    "details": [
      {
        "field": "placa",
        "message": "Formato de placa inválido. Use ABC-1234"
      }
    ]
  }
}
```

---

## Rate Limiting

- **Limite:** 1000 requisições por hora por token
- **Headers de resposta:**
  - `X-RateLimit-Limit`: Limite total
  - `X-RateLimit-Remaining`: Requisições restantes
  - `X-RateLimit-Reset`: Timestamp de reset do limite

Quando o limite é excedido, retorna `429 Too Many Requests`.

---

## Versionamento

A API utiliza versionamento via URL. A versão atual é `v1`.

Mudanças breaking resultarão em nova versão (`v2`, etc).
