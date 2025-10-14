# API Reference - Backoffice Veículos API

## Status do Projeto

🚧 **EM DESENVOLVIMENTO** - Esta documentação descreve os endpoints planejados para a API.

## Base URL
```
https://backoffice-veiculos-api.railway.app/api/v1
```

## Autenticação

Todas as requisições requerem autenticação via Bearer Token no header:
```
Authorization: Bearer {token}
```

---

## Endpoints

### Veículos

#### `GET /veiculos`
Lista todos os veículos cadastrados.

**Query Parameters:**
- `page` (number, opcional): Número da página (default: 1)
- `limit` (number, opcional): Itens por página (default: 20, max: 100)
- `status` (string, opcional): Filtrar por status (`ativo`, `inativo`, `manutencao`)
- `tipo` (string, opcional): Filtrar por tipo de veículo

**Resposta de Sucesso (200 OK):**
```json
{
  "data": [
    {
      "id": "uuid-123",
      "placa": "ABC-1234",
      "modelo": "Fiat Uno",
      "ano": 2020,
      "status": "ativo",
      "tipo": "passeio",
      "km_atual": 45000,
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-03-20T14:45:00Z"
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
- `200` - Sucesso
- `401` - Não autenticado
- `403` - Sem permissão
- `500` - Erro interno

---

#### `GET /veiculos/{id}`
Obtém detalhes de um veículo específico.

**Path Parameters:**
- `id` (string, obrigatório): ID do veículo

**Resposta de Sucesso (200 OK):**
```json
{
  "id": "uuid-123",
  "placa": "ABC-1234",
  "modelo": "Fiat Uno",
  "marca": "Fiat",
  "ano": 2020,
  "status": "ativo",
  "tipo": "passeio",
  "km_atual": 45000,
  "cor": "branco",
  "chassi": "9BWZZZ377VT004251",
  "renavam": "00123456789",
  "proprietario_id": "uuid-456",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-03-20T14:45:00Z"
}
```

**Códigos de Status:**
- `200` - Sucesso
- `401` - Não autenticado
- `404` - Veículo não encontrado
- `500` - Erro interno

---

#### `POST /veiculos`
Cadastra um novo veículo.

**Body (JSON):**
```json
{
  "placa": "XYZ-9876",
  "modelo": "Honda Civic",
  "marca": "Honda",
  "ano": 2023,
  "tipo": "passeio",
  "km_atual": 0,
  "cor": "prata",
  "chassi": "9BWZZZ377VT004252",
  "renavam": "00987654321",
  "proprietario_id": "uuid-789"
}
```

**Campos Obrigatórios:**
- `placa`
- `modelo`
- `marca`
- `ano`
- `tipo`

**Resposta de Sucesso (201 Created):**
```json
{
  "id": "uuid-789",
  "placa": "XYZ-9876",
  "modelo": "Honda Civic",
  "marca": "Honda",
  "ano": 2023,
  "status": "ativo",
  "tipo": "passeio",
  "km_atual": 0,
  "cor": "prata",
  "chassi": "9BWZZZ377VT004252",
  "renavam": "00987654321",
  "proprietario_id": "uuid-789",
  "created_at": "2024-03-25T09:15:00Z",
  "updated_at": "2024-03-25T09:15:00Z"
}
```

**Códigos de Status:**
- `201` - Criado com sucesso
- `400` - Dados inválidos
- `401` - Não autenticado
- `409` - Placa já cadastrada
- `500` - Erro interno

---

#### `PUT /veiculos/{id}`
Atualiza dados de um veículo existente.

**Path Parameters:**
- `id` (string, obrigatório): ID do veículo

**Body (JSON):**
```json
{
  "km_atual": 47500,
  "status": "manutencao",
  "cor": "preto"
}
```

**Campos Atualizáveis:**
- `km_atual`
- `status`
- `cor`
- `proprietario_id`

**Resposta de Sucesso (200 OK):**
```json
{
  "id": "uuid-123",
  "placa": "ABC-1234",
  "modelo": "Fiat Uno",
  "marca": "Fiat",
  "ano": 2020,
  "status": "manutencao",
  "tipo": "passeio",
  "km_atual": 47500,
  "cor": "preto",
  "chassi": "9BWZZZ377VT004251",
  "renavam": "00123456789",
  "proprietario_id": "uuid-456",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-03-25T16:20:00Z"
}
```

**Códigos de Status:**
- `200` - Atualizado com sucesso
- `400` - Dados inválidos
- `401` - Não autenticado
- `404` - Veículo não encontrado
- `500` - Erro interno

---

#### `DELETE /veiculos/{id}`
Remove um veículo do sistema.

**Path Parameters:**
- `id` (string, obrigatório): ID do veículo

**Resposta de Sucesso (204 No Content):**
Sem corpo de resposta.

**Códigos de Status:**
- `204` - Removido com sucesso
- `401` - Não autenticado
- `404` - Veículo não encontrado
- `409` - Veículo possui dependências (manutenções ativas)
- `500` - Erro interno

---

### Manutenções

#### `GET /veiculos/{veiculo_id}/manutencoes`
Lista manutenções de um veículo.

**Path Parameters:**
- `veiculo_id` (string, obrigatório): ID do veículo

**Query Parameters:**
- `status` (string, opcional): Filtrar por status (`agendada`, `em_andamento`, `concluida`)
- `data_inicio` (date, opcional): Filtrar por data inicial (ISO 8601)
- `data_fim` (date, opcional): Filtrar por data final (ISO 8601)

**Resposta de Sucesso (200 OK):**
```json
{
  "data": [
    {
      "id": "uuid-mnt-001",
      "veiculo_id": "uuid-123",
      "tipo": "preventiva",
      "descricao": "Troca de óleo e filtros",
      "status": "concluida",
      "data_agendada": "2024-03-10T08:00:00Z",
      "data_conclusao": "2024-03-10T10:30:00Z",
      "km_manutencao": 45000,
      "custo": 350.00,
      "oficina": "Auto Center XYZ",
      "created_at": "2024-03-01T14:00:00Z"
    }
  ]
}
```

**Códigos de Status:**
- `200` - Sucesso
- `401` - Não autenticado
- `404` - Veículo não encontrado
- `500` - Erro interno

---

#### `POST /veiculos/{veiculo_id}/manutencoes`
Agenda uma nova manutenção.

**Path Parameters:**
- `veiculo_id` (string, obrigatório): ID do veículo

**Body (JSON):**
```json
{
  "tipo": "corretiva",
  "descricao": "Reparo no sistema de freios",
  "data_agendada": "2024-03-30T09:00:00Z",
  "oficina": "Oficina do João",
  "custo_estimado": 800.00
}
```

**Campos Obrigatórios:**
- `tipo` (valores: `preventiva`, `corretiva`, `revisao`)
- `descricao`
- `data_agendada`

**Resposta de Sucesso (201 Created):**
```json
{
  "id": "uuid-mnt-002",
  "veiculo_id": "uuid-123",
  "tipo": "corretiva",
  "descricao": "Reparo no sistema de freios",
  "status": "agendada",
  "data_agendada": "2024-03-30T09:00:00Z",
  "oficina": "Oficina do João",
  "custo_estimado": 800.00,
  "created_at": "2024-03-25T11:45:00Z"
}
```

**Códigos de Status:**
- `201` - Criado com sucesso
- `400` - Dados inválidos
- `401` - Não autenticado
- `404` - Veículo não encontrado
- `500` - Erro interno

---

#### `PATCH /manutencoes/{id}/status`
Atualiza status de uma manutenção.

**Path Parameters:**
- `id` (string, obrigatório): ID da manutenção

**Body (JSON):**
```json
{
  "status": "em_andamento",
  "observacoes": "Iniciado reparo dos freios dianteiros"
}
```

**Status Permitidos:**
- `agendada`
- `em_andamento`
- `concluida`
- `cancelada`

**Resposta de Sucesso (200 OK):**
```json
{
  "id": "uuid-mnt-002",
  "status": "em_andamento",
  "updated_at": "2024-03-30T09:15:00Z",
  "observacoes": "Iniciado reparo dos freios dianteiros"
}
```

**Códigos de Status:**
- `200` - Atualizado com sucesso
- `400` - Status inválido
- `401` - Não autenticado
- `404` - Manutenção não encontrada
- `500` - Erro interno

---

### Relatórios

#### `GET /relatorios/veiculos`
Gera relatório consolidado de veículos.

**Query Parameters:**
- `formato` (string, opcional): Formato do relatório (`json`, `pdf`, `xlsx`) - default: `json`
- `status` (string, opcional): Filtrar por status
- `data_inicio` (date, opcional): Período inicial
- `data_fim` (date, opcional): Período final

**Resposta de Sucesso (200 OK):**
```json
{
  "resumo": {
    "total_veiculos": 150,
    "veiculos_ativos": 120,
    "veiculos_manutencao": 15,
    "veiculos_inativos": 15
  },
  "por_tipo": {
    "passeio": 80,
    "utilitario": 45,
    "caminhao": 25
  },
  "manutencoes": {
    "total_mes": 42,
    "custo_total": 35600.00,
    "custo_medio": 847.62
  },
  "gerado_em": "2024-03-25T16:30:00Z"
}
```

**Códigos de Status:**
- `200` - Sucesso
- `401` - Não autenticado
- `403` - Sem permissão para relatórios
- `500` - Erro interno

---

## Códigos de Erro

### Formato Padrão de Erro
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos fornecidos",
    "details": [
      {
        "field": "placa",
        "message": "Formato de placa inválido"
      }
    ]
  }
}
```

### Códigos Comuns
- `UNAUTHORIZED` - Token inválido ou ausente
- `FORBIDDEN` - Sem permissão para recurso
- `NOT_FOUND` - Recurso não encontrado
- `VALIDATION_ERROR` - Dados inválidos
- `DUPLICATE_ENTRY` - Registro já existe
- `CONFLICT` - Operação conflitante
- `INTERNAL_ERROR` - Erro interno do servidor

---

## Rate Limiting

- **Limite:** 1000 requisições por hora por token
- **Headers de resposta:**
  ```
  X-RateLimit-Limit: 1000
  X-RateLimit-Remaining: 985
  X-RateLimit-Reset: 1711377600
  ```

**Resposta quando limite excedido (429 Too Many Requests):**
```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Limite de requisições excedido",
    "retry_after": 3600
  }
}
```

---

## Versionamento

A API utiliza versionamento via URL (`/v1/`). Mudanças não retrocompatíveis resultarão em nova versão.

## Suporte

Para dúvidas ou problemas, contate: api-support@backoffice-veiculos.com
