# API Reference - Backoffice Veículos BFF

## Visão Geral

Esta documentação descreve todos os endpoints disponíveis no Backend for Frontend (BFF) do sistema de backoffice de veículos. O BFF atua como uma camada intermediária que agrega e otimiza dados de múltiplas APIs backend para o frontend.

## Base URL

- **Desenvolvimento**: `http://localhost:3002`
- **Produção**: `https://backoffice-veiculos-bff.railway.app`

## Autenticação

O BFF utiliza autenticação baseada em JWT (JSON Web Tokens). Inclua o token no header `Authorization`:

```bash
Authorization: Bearer <your-jwt-token>
```

## Headers Padrão

```bash
Content-Type: application/json
Authorization: Bearer <token>
Accept: application/json
```

## Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| 200 | Sucesso |
| 201 | Criado com sucesso |
| 400 | Requisição inválida |
| 401 | Não autorizado |
| 403 | Acesso negado |
| 404 | Recurso não encontrado |
| 429 | Muitas requisições (Rate Limit) |
| 500 | Erro interno do servidor |
| 502 | Erro de gateway (API backend indisponível) |
| 503 | Serviço indisponível |

## Endpoints

### Dashboard

#### GET /api/dashboard/metrics
Retorna métricas consolidadas do dashboard.

**Headers:**
```bash
Authorization: Bearer <token>
```

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "totalAnuncios": 1250,
    "anunciosAtivos": 980,
    "anunciosVendidos": 270,
    "totalVendas": 1250000.00,
    "vendasMesAtual": 85000.00,
    "vendedoresAtivos": 45,
    "conversaoMedia": 0.12,
    "tempoMedioVenda": 15.5,
    "ultimaAtualizacao": "2024-01-15T10:30:00Z"
  }
}
```

#### GET /api/dashboard/sales
Retorna dados de vendas para gráficos e relatórios.

**Query Parameters:**
- `period` (string, opcional): Período dos dados (`day`, `week`, `month`, `year`)
- `startDate` (string, opcional): Data de início (ISO 8601)
- `endDate` (string, opcional): Data de fim (ISO 8601)

**Exemplo:**
```bash
GET /api/dashboard/sales?period=month&startDate=2024-01-01&endDate=2024-01-31
```

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "period": "month",
    "totalVendas": 125000.00,
    "vendasPorDia": [
      {
        "date": "2024-01-01",
        "vendas": 2500.00,
        "quantidade": 3
      },
      {
        "date": "2024-01-02",
        "vendas": 3200.00,
        "quantidade": 4
      }
    ],
    "vendasPorVendedor": [
      {
        "vendedorId": "vendedor_123",
        "nome": "João Silva",
        "vendas": 15000.00,
        "quantidade": 8
      }
    ]
  }
}
```

#### GET /api/dashboard/announcements
Retorna estatísticas de anúncios.

**Query Parameters:**
- `status` (string, opcional): Status dos anúncios (`active`, `sold`, `inactive`)
- `category` (string, opcional): Categoria do veículo

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "totalAnuncios": 1250,
    "anunciosPorStatus": {
      "active": 980,
      "sold": 270,
      "inactive": 0
    },
    "anunciosPorCategoria": {
      "carros": 800,
      "motos": 300,
      "caminhoes": 150
    },
    "anunciosPorMarca": [
      {
        "marca": "Honda",
        "quantidade": 250
      },
      {
        "marca": "Toyota",
        "quantidade": 200
      }
    ]
  }
}
```

### Anúncios

#### GET /api/announcements
Lista anúncios com filtros e paginação.

**Query Parameters:**
- `page` (number, opcional): Número da página (padrão: 1)
- `limit` (number, opcional): Itens por página (padrão: 20, máximo: 100)
- `status` (string, opcional): Status do anúncio (`active`, `sold`, `inactive`)
- `marca` (string, opcional): Marca do veículo
- `modelo` (string, opcional): Modelo do veículo
- `precoMin` (number, opcional): Preço mínimo
- `precoMax` (number, opcional): Preço máximo
- `anoMin` (number, opcional): Ano mínimo
- `anoMax` (number, opcional): Ano máximo
- `search` (string, opcional): Busca por texto
- `sortBy` (string, opcional): Campo para ordenação (`createdAt`, `preco`, `ano`)
- `sortOrder` (string, opcional): Ordem (`asc`, `desc`)

**Exemplo:**
```bash
GET /api/announcements?page=1&limit=20&status=active&marca=Honda&precoMin=50000&sortBy=preco&sortOrder=asc
```

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "announcements": [
      {
        "id": "ann_123",
        "titulo": "Honda Civic 2020",
        "preco": 85000.00,
        "marca": "Honda",
        "modelo": "Civic",
        "ano": 2020,
        "quilometragem": 45000,
        "status": "active",
        "imagens": [
          "https://storage.com/images/ann_123_1.jpg"
        ],
        "vendedor": {
          "id": "vendedor_123",
          "nome": "João Silva",
          "telefone": "+5511999999999"
        },
        "createdAt": "2024-01-10T14:30:00Z",
        "updatedAt": "2024-01-15T09:15:00Z"
      }
    ],
    "pagination": {
      "currentPage": 1,
      "totalPages": 25,
      "totalItems": 500,
      "itemsPerPage": 20,
      "hasNext": true,
      "hasPrev": false
    },
    "filters": {
      "applied": {
        "status": "active",
        "marca": "Honda",
        "precoMin": 50000
      },
      "available": {
        "marcas": ["Honda", "Toyota", "Ford"],
        "modelos": ["Civic", "Corolla", "Focus"],
        "anos": [2018, 2019, 2020, 2021, 2022]
      }
    }
  }
}
```

#### GET /api/announcements/:id
Retorna detalhes de um anúncio específico.

**Parâmetros:**
- `id` (string): ID do anúncio

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "id": "ann_123",
    "titulo": "Honda Civic 2020",
    "descricao": "Veículo em excelente estado, único dono...",
    "preco": 85000.00,
    "marca": "Honda",
    "modelo": "Civic",
    "ano": 2020,
    "quilometragem": 45000,
    "combustivel": "Flex",
    "cambio": "Automático",
    "cor": "Prata",
    "status": "active",
    "imagens": [
      "https://storage.com/images/ann_123_1.jpg",
      "https://storage.com/images/ann_123_2.jpg"
    ],
    "vendedor": {
      "id": "vendedor_123",
      "nome": "João Silva",
      "email": "joao@exemplo.com",
      "telefone": "+5511999999999"
    },
    "estatisticas": {
      "visualizacoes": 1250,
      "contatos": 45,
      "favoritos": 12
    },
    "createdAt": "2024-01-10T14:30:00Z",
    "updatedAt": "2024-01-15T09:15:00Z"
  }
}
```

#### POST /api/announcements
Cria um novo anúncio.

**Body:**
```json
{
  "titulo": "Honda Civic 2020",
  "descricao": "Veículo em excelente estado, único dono...",
  "preco": 85000.00,
  "marca": "Honda",
  "modelo": "Civic",
  "ano": 2020,
  "quilometragem": 45000,
  "combustivel": "Flex",
  "cambio": "Automático",
  "cor": "Prata",
  "imagens": [
    "https://storage.com/images/ann_123_1.jpg"
  ]
}
```

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "id": "ann_123",
    "titulo": "Honda Civic 2020",
    "status": "active",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

#### PUT /api/announcements/:id
Atualiza um anúncio existente.

**Parâmetros:**
- `id` (string): ID do anúncio

**Body:**
```json
{
  "titulo": "Honda Civic 2020 - Atualizado",
  "preco": 82000.00,
  "descricao": "Preço reduzido! Veículo em excelente estado..."
}
```

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "id": "ann_123",
    "titulo": "Honda Civic 2020 - Atualizado",
    "preco": 82000.00,
    "updatedAt": "2024-01-15T11:00:00Z"
  }
}
```

#### DELETE /api/announcements/:id
Remove um anúncio.

**Parâmetros:**
- `id` (string): ID do anúncio

**Resposta:**
```json
{
  "status": "success",
  "message": "Anúncio removido com sucesso"
}
```

#### PUT /api/announcements/:id/status
Atualiza o status de um anúncio.

**Parâmetros:**
- `id` (string): ID do anúncio

**Body:**
```json
{
  "status": "sold"
}
```

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "id": "ann_123",
    "status": "sold",
    "updatedAt": "2024-01-15T12:00:00Z"
  }
}
```

### Usuários

#### GET /api/users
Lista usuários do sistema.

**Query Parameters:**
- `page` (number, opcional): Número da página
- `limit` (number, opcional): Itens por página
- `role` (string, opcional): Papel do usuário (`admin`, `manager`, `seller`, `operator`)
- `status` (string, opcional): Status do usuário (`active`, `inactive`)

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "users": [
      {
        "id": "user_123",
        "nome": "João Silva",
        "email": "joao@exemplo.com",
        "role": "seller",
        "status": "active",
        "telefone": "+5511999999999",
        "createdAt": "2024-01-01T10:00:00Z",
        "lastLogin": "2024-01-15T09:30:00Z"
      }
    ],
    "pagination": {
      "currentPage": 1,
      "totalPages": 5,
      "totalItems": 100,
      "itemsPerPage": 20
    }
  }
}
```

#### GET /api/users/:id
Retorna detalhes de um usuário específico.

**Parâmetros:**
- `id` (string): ID do usuário

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "id": "user_123",
    "nome": "João Silva",
    "email": "joao@exemplo.com",
    "role": "seller",
    "status": "active",
    "telefone": "+5511999999999",
    "endereco": {
      "rua": "Rua das Flores, 123",
      "cidade": "São Paulo",
      "estado": "SP",
      "cep": "01234-567"
    },
    "estatisticas": {
      "totalAnuncios": 25,
      "anunciosAtivos": 15,
      "totalVendas": 125000.00,
      "ultimaVenda": "2024-01-10T14:30:00Z"
    },
    "createdAt": "2024-01-01T10:00:00Z",
    "lastLogin": "2024-01-15T09:30:00Z"
  }
}
```

#### POST /api/users
Cria um novo usuário.

**Body:**
```json
{
  "nome": "Maria Santos",
  "email": "maria@exemplo.com",
  "password": "senha123",
  "role": "seller",
  "telefone": "+5511888888888"
}
```

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "id": "user_456",
    "nome": "Maria Santos",
    "email": "maria@exemplo.com",
    "role": "seller",
    "status": "active",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

#### PUT /api/users/:id
Atualiza um usuário existente.

**Parâmetros:**
- `id` (string): ID do usuário

**Body:**
```json
{
  "nome": "Maria Santos Silva",
  "telefone": "+5511888888889",
  "role": "manager"
}
```

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "id": "user_456",
    "nome": "Maria Santos Silva",
    "role": "manager",
    "updatedAt": "2024-01-15T11:00:00Z"
  }
}
```

### Cache

#### GET /api/cache/stats
Retorna estatísticas do cache Redis.

**Resposta:**
```json
{
  "status": "success",
  "data": {
    "hitRate": 0.85,
    "missRate": 0.15,
    "totalKeys": 1250,
    "memoryUsage": "45.2MB",
    "uptime": "7d 12h 30m",
    "topKeys": [
      {
        "key": "dashboard:metrics",
        "hits": 1250,
        "ttl": 300
      },
      {
        "key": "announcements:list:page_1",
        "hits": 890,
        "ttl": 180
      }
    ]
  }
}
```

#### DELETE /api/cache/clear
Limpa todo o cache.

**Resposta:**
```json
{
  "status": "success",
  "message": "Cache limpo com sucesso"
}
```

#### DELETE /api/cache/clear/:pattern
Limpa cache por padrão.

**Parâmetros:**
- `pattern` (string): Padrão das chaves a serem removidas

**Exemplo:**
```bash
DELETE /api/cache/clear/dashboard:*
```

**Resposta:**
```json
{
  "status": "success",
  "message": "Cache limpo para o padrão: dashboard:*"
}
```

### Health Check

#### GET /health
Verifica a saúde do serviço BFF.

**Resposta:**
```json
{
  "status": "ok",
  "timestamp": "2024-01-15T10:30:00Z",
  "uptime": "7d 12h 30m",
  "version": "1.0.0",
  "environment": "production"
}
```

#### GET /health/detailed
Verifica a saúde detalhada do serviço e suas dependências.

**Resposta:**
```json
{
  "status": "ok",
  "timestamp": "2024-01-15T10:30:00Z",
  "services": {
    "backoffice-api": {
      "status": "ok",
      "responseTime": 45,
      "url": "https://backoffice-veiculos-api.railway.app"
    },
    "redis": {
      "status": "ok",
      "responseTime": 2,
      "memory": "45.2MB"
    }
  },
  "metrics": {
    "requestsPerMinute": 150,
    "averageResponseTime": 120,
    "errorRate": 0.02
  }
}
```

## Rate Limiting

O BFF implementa rate limiting para proteger contra abuso:

- **Limite padrão**: 100 requisições por 15 minutos por IP
- **Limite para autenticação**: 5 tentativas por minuto por IP
- **Headers de resposta**:
  ```
  X-RateLimit-Limit: 100
  X-RateLimit-Remaining: 95
  X-RateLimit-Reset: 1642248000
  ```

## Tratamento de Erros

### Formato de Erro Padrão

```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados de entrada inválidos",
    "details": [
      {
        "field": "preco",
        "message": "Preço deve ser um número positivo"
      }
    ]
  },
  "timestamp": "2024-01-15T10:30:00Z",
  "requestId": "req_123456"
}
```

### Códigos de Erro Comuns

| Código | Descrição |
|--------|-----------|
| `VALIDATION_ERROR` | Dados de entrada inválidos |
| `AUTHENTICATION_ERROR` | Token inválido ou expirado |
| `AUTHORIZATION_ERROR` | Usuário não tem permissão |
| `NOT_FOUND` | Recurso não encontrado |
| `DUPLICATE_ENTRY` | Recurso já existe |
| `BACKEND_ERROR` | Erro no serviço backend |
| `CACHE_ERROR` | Erro no cache Redis |
| `RATE_LIMIT_EXCEEDED` | Limite de requisições excedido |

## Webhooks

O BFF pode enviar webhooks para notificar sobre eventos importantes:

### Eventos Disponíveis

- `announcement.created` - Novo anúncio criado
- `announcement.updated` - Anúncio atualizado
- `announcement.sold` - Anúncio vendido
- `user.created` - Novo usuário criado
- `user.updated` - Usuário atualizado

### Configuração de Webhook

```json
{
  "url": "https://seu-servidor.com/webhook",
  "events": ["announcement.created", "announcement.sold"],
  "secret": "seu-webhook-secret"
}
```

## Exemplos de Uso

### JavaScript/TypeScript

```javascript
// Configuração base
const API_BASE = 'https://backoffice-veiculos-bff.railway.app';
const token = 'seu-jwt-token';

// Buscar anúncios
async function getAnnouncements(filters = {}) {
  const params = new URLSearchParams(filters);
  const response = await fetch(`${API_BASE}/api/announcements?${params}`, {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  });
  
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  
  return await response.json();
}

// Criar anúncio
async function createAnnouncement(announcementData) {
  const response = await fetch(`${API_BASE}/api/announcements`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(announcementData)
  });
  
  return await response.json();
}
```

### cURL

```bash
# Buscar métricas do dashboard
curl -X GET "https://backoffice-veiculos-bff.railway.app/api/dashboard/metrics" \
  -H "Authorization: Bearer seu-jwt-token" \
  -H "Content-Type: application/json"

# Criar novo anúncio
curl -X POST "https://backoffice-veiculos-bff.railway.app/api/announcements" \
  -H "Authorization: Bearer seu-jwt-token" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Honda Civic 2020",
    "preco": 85000.00,
    "marca": "Honda",
    "modelo": "Civic",
    "ano": 2020
  }'
```

## Changelog

### v1.0.0 (2024-01-15)
- Versão inicial da API
- Endpoints de dashboard, anúncios e usuários
- Sistema de cache Redis
- Rate limiting
- Health checks

## Suporte

Para dúvidas ou problemas com a API:

- **Documentação**: [Ver documentação completa](./index.md)
- **Issues**: [GitHub Issues](https://github.com/emingues-xx/backoffice-veiculos-bff/issues)
- **Email**: suporte@backoffice-veiculos.com
