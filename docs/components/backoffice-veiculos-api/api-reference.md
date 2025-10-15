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

### Métricas de Vendas

#### `GET /metricas/vendas/total`
Retorna o valor total consolidado de vendas no período especificado.

**Query Parameters:**
- `data_inicio` (string, opcional): Data inicial no formato ISO 8601 (YYYY-MM-DD)
- `data_fim` (string, opcional): Data final no formato ISO 8601 (YYYY-MM-DD)

**Resposta de Sucesso (200 OK):**
```json
{
  "total_vendas": 1250000.00,
  "moeda": "BRL",
  "periodo": {
    "inicio": "2024-01-01",
    "fim": "2024-03-31"
  },
  "atualizado_em": "2024-03-25T23:00:00Z"
}
```

**Códigos de Status:**
- `200` - Sucesso
- `400` - Parâmetros de data inválidos
- `401` - Não autenticado
- `500` - Erro interno

---

#### `GET /metricas/vendas/por-dia`
Retorna a quantidade de vendas realizadas em cada dia do período.

**Query Parameters:**
- `data_inicio` (string, opcional): Data inicial no formato ISO 8601 (YYYY-MM-DD)
- `data_fim` (string, opcional): Data final no formato ISO 8601 (YYYY-MM-DD)

**Resposta de Sucesso (200 OK):**
```json
{
  "dados": [
    {
      "data": "2024-03-01",
      "quantidade": 15,
      "valor_total": 42500.00
    },
    {
      "data": "2024-03-02",
      "quantidade": 18,
      "valor_total": 51300.00
    }
  ],
  "periodo": {
    "inicio": "2024-03-01",
    "fim": "2024-03-31"
  },
  "total_periodo": 450,
  "atualizado_em": "2024-03-25T23:00:00Z"
}
```

**Códigos de Status:**
- `200` - Sucesso
- `400` - Parâmetros de data inválidos
- `401` - Não autenticado
- `500` - Erro interno

---

#### `GET /metricas/vendas/ticket-medio`
Retorna o valor médio de cada venda no período.

**Query Parameters:**
- `data_inicio` (string, opcional): Data inicial no formato ISO 8601 (YYYY-MM-DD)
- `data_fim` (string, opcional): Data final no formato ISO 8601 (YYYY-MM-DD)

**Resposta de Sucesso (200 OK):**
```json
{
  "ticket_medio": 35700.00,
  "moeda": "BRL",
  "total_vendas": 450,
  "valor_total": 16065000.00,
  "periodo": {
    "inicio": "2024-01-01",
    "fim": "2024-03-31"
  },
  "precisao": "100%",
  "atualizado_em": "2024-03-25T23:00:00Z"
}
```

**Códigos de Status:**
- `200` - Sucesso
- `400` - Parâmetros de data inválidos
- `401` - Não autenticado
- `500` - Erro interno

---

#### `GET /metricas/vendas/taxa-conversao`
Retorna a taxa de conversão de leads em vendas.

**Query Parameters:**
- `data_inicio` (string, opcional): Data inicial no formato ISO 8601 (YYYY-MM-DD)
- `data_fim` (string, opcional): Data final no formato ISO 8601 (YYYY-MM-DD)

**Resposta de Sucesso (200 OK):**
```json
{
  "taxa_conversao": 12.5,
  "unidade": "percentual",
  "total_leads": 3600,
  "vendas_concluidas": 450,
  "periodo": {
    "inicio": "2024-01-01",
    "fim": "2024-03-31"
  },
  "atualizado_em": "2024-03-25T23:00:00Z"
}
```

**Códigos de Status:**
- `200` - Sucesso
- `400` - Parâmetros de data inválidos
- `401` - Não autenticado
- `500` - Erro interno

---

#### `GET /metricas/vendas/tempo-medio`
Retorna o tempo médio entre criação do lead e fechamento da venda.

**Query Parameters:**
- `data_inicio` (string, opcional): Data inicial no formato ISO 8601 (YYYY-MM-DD)
- `data_fim` (string, opcional): Data final no formato ISO 8601 (YYYY-MM-DD)

**Resposta de Sucesso (200 OK):**
```json
{
  "tempo_medio_dias": 7.5,
  "tempo_medio_horas": 180.0,
  "unidade": "dias",
  "total_vendas_analisadas": 450,
  "periodo": {
    "inicio": "2024-01-01",
    "fim": "2024-03-31"
  },
  "distribuicao": {
    "0_3_dias": 120,
    "4_7_dias": 180,
    "8_14_dias": 110,
    "mais_14_dias": 40
  },
  "atualizado_em": "2024-03-25T23:00:00Z"
}
```

**Códigos de Status:**
- `200` - Sucesso
- `400` - Parâmetros de data inválidos
- `401` - Não autenticado
- `500` - Erro interno

---

#### `GET /metricas/vendas/consolidado`
Retorna todas as métricas consolidadas em uma única requisição.

**Query Parameters:**
- `data_inicio` (string, opcional): Data inicial no formato ISO 8601 (YYYY-MM-DD)
- `data_fim` (string, opcional): Data final no formato ISO 8601 (YYYY-MM-DD)

**Resposta de Sucesso (200 OK):**
```json
{
  "periodo": {
    "inicio": "2024-01-01",
    "fim": "2024-03-31"
  },
  "total_vendas": 16065000.00,
  "quantidade_vendas": 450,
  "ticket_medio": 35700.00,
  "taxa_conversao": 12.5,
  "tempo_medio_vendas": 7.5,
  "vendas_por_dia": [
    {
      "data": "2024-03-01",
      "quantidade": 15,
      "valor_total": 42500.00
    }
  ],
  "performance_cache": {
    "cache_hit": true,
    "tempo_resposta_ms": 45
  },
  "atualizado_em": "2024-03-25T23:00:00Z"
}
```

**Códigos de Status:**
- `200` - Sucesso
- `400` - Parâmetros de data inválidos
- `401` - Não autenticado
- `500` - Erro interno

**Notas:**
- Este endpoint é otimizado com cache Redis
- Tempo de resposta típico: < 100ms
- Recomendado para dashboards que necessitam de todas as métricas

---

#### `GET /metricas/vendas/health`
Health check do sistema de métricas.

**Resposta de Sucesso (200 OK):**
```json
{
  "status": "healthy",
  "servicos": {
    "database": "operational",
    "cache": "operational",
    "job_atualizacao": "operational"
  },
  "ultima_atualizacao": "2024-03-25T23:00:00Z",
  "proxima_atualizacao": "2024-03-26T23:00:00Z",
  "metricas_disponiveis": 5,
  "tempo_resposta_medio_ms": 650
}
```

**Códigos de Status:**
- `200` - Sistema saudável
- `503` - Sistema com problemas

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
