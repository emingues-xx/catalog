# API Documentation - vitrine-veiculos-api

Documentação completa dos endpoints da API de veículos da vitrine.

## Base URL

```
Development: http://localhost:3001
Production:  https://api-vitrine.veiculos.com
```

## Autenticação

A API da vitrine é pública e não requer autenticação para consultas. Rate limiting é aplicado por IP.

## Headers Padrão

```http
Content-Type: application/json
Accept: application/json
User-Agent: vitrine-web/1.0.0
```

## Rate Limiting

- **Limite**: 100 requests por minuto por IP
- **Headers de resposta**:
  - `X-RateLimit-Limit`: Limite máximo
  - `X-RateLimit-Remaining`: Requests restantes
  - `X-RateLimit-Reset`: Timestamp do reset

## Endpoints

### Veículos

#### Listar Veículos
Lista veículos com suporte a filtros e paginação.

```http
GET /api/vehicles
```

**Query Parameters:**
| Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
|-----------|------|-------------|-----------|---------|
| page | number | Não | Página (padrão: 1) | `?page=2` |
| limit | number | Não | Items por página (máx: 50) | `?limit=20` |
| brand | string | Não | Filtro por marca | `?brand=honda` |
| model | string | Não | Filtro por modelo | `?model=civic` |
| yearMin | number | Não | Ano mínimo | `?yearMin=2020` |
| yearMax | number | Não | Ano máximo | `?yearMax=2023` |
| priceMin | number | Não | Preço mínimo | `?priceMin=50000` |
| priceMax | number | Não | Preço máximo | `?priceMax=100000` |
| fuel | string | Não | Tipo combustível | `?fuel=flex` |
| state | string | Não | Estado (UF) | `?state=SP` |
| city | string | Não | Cidade | `?city=São Paulo` |
| sort | string | Não | Ordenação | `?sort=price_asc` |

**Valores de `sort`:**
- `price_asc`: Menor preço
- `price_desc`: Maior preço
- `year_desc`: Mais novo
- `year_asc`: Mais antigo
- `mileage_asc`: Menor quilometragem
- `created_desc`: Mais recente (padrão)

**Response:**
```json
{
  "data": [
    {
      "id": "uuid-v4",
      "brand": "Honda",
      "model": "Civic",
      "version": "LX CVT",
      "year": 2023,
      "modelYear": 2023,
      "price": 125000,
      "mileage": 15000,
      "fuel": "flex",
      "transmission": "automatic",
      "color": "Prata",
      "doors": 4,
      "location": {
        "state": "SP",
        "city": "São Paulo",
        "neighborhood": "Vila Madalena"
      },
      "images": [
        {
          "url": "https://cdn.example.com/image1.jpg",
          "alt": "Honda Civic 2023 - Vista frontal",
          "isPrimary": true
        }
      ],
      "seller": {
        "name": "Concessionária Premium",
        "type": "dealer",
        "phone": "(11) 99999-9999"
      },
      "features": ["Ar condicionado", "Direção elétrica", "Vidros elétricos"],
      "createdAt": "2023-12-01T10:30:00Z",
      "updatedAt": "2023-12-01T10:30:00Z"
    }
  ],
  "pagination": {
    "current": 1,
    "total": 150,
    "pages": 8,
    "perPage": 20,
    "hasNext": true,
    "hasPrev": false
  },
  "filters": {
    "applied": {
      "brand": "honda",
      "state": "SP"
    },
    "available": {
      "brands": ["Honda", "Toyota", "Volkswagen"],
      "priceRange": { "min": 25000, "max": 350000 },
      "yearRange": { "min": 2010, "max": 2024 }
    }
  }
}
```

#### Buscar Veículos
Busca por texto livre nos campos do veículo.

```http
GET /api/vehicles/search
```

**Query Parameters:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| q | string | Sim | Termo de busca |
| page | number | Não | Página |
| limit | number | Não | Items por página |

**Exemplo:**
```http
GET /api/vehicles/search?q=honda civic prata&page=1&limit=10
```

**Response:**
```json
{
  "data": [
    {
      "id": "uuid-v4",
      "brand": "Honda",
      "model": "Civic",
      "highlight": {
        "brand": "<mark>Honda</mark>",
        "model": "<mark>Civic</mark>",
        "color": "<mark>Prata</mark>"
      },
      "score": 0.95,
      // ... outros campos do veículo
    }
  ],
  "query": {
    "original": "honda civic prata",
    "processed": ["honda", "civic", "prata"],
    "suggestions": ["honda civic", "civic prata", "honda prata"]
  },
  "pagination": { /* ... */ }
}
```

#### Detalhes do Veículo
Retorna informações completas de um veículo específico.

```http
GET /api/vehicles/:id
```

**Response:**
```json
{
  "data": {
    "id": "uuid-v4",
    "brand": "Honda",
    "model": "Civic",
    "version": "LX CVT",
    "year": 2023,
    "modelYear": 2023,
    "price": 125000,
    "mileage": 15000,
    "fuel": "flex",
    "transmission": "automatic",
    "engine": {
      "displacement": "2.0",
      "power": "155 cv",
      "torque": "192 Nm"
    },
    "specifications": {
      "doors": 4,
      "seats": 5,
      "trunkCapacity": "519 litros",
      "fuelTank": "50 litros",
      "weight": "1.320 kg"
    },
    "equipment": {
      "safety": ["ABS", "Airbag", "Controle de estabilidade"],
      "comfort": ["Ar condicionado", "Direção elétrica", "Vidros elétricos"],
      "technology": ["Central multimídia", "Bluetooth", "USB"]
    },
    "images": [
      {
        "url": "https://cdn.example.com/image1.jpg",
        "alt": "Honda Civic 2023 - Vista frontal",
        "isPrimary": true,
        "order": 1
      }
    ],
    "location": {
      "state": "SP",
      "city": "São Paulo",
      "neighborhood": "Vila Madalena",
      "coordinates": {
        "lat": -23.5505,
        "lng": -46.6333
      }
    },
    "seller": {
      "id": "seller-uuid",
      "name": "Concessionária Premium",
      "type": "dealer",
      "phone": "(11) 99999-9999",
      "whatsapp": "(11) 99999-9999",
      "email": "contato@premium.com",
      "rating": 4.8,
      "reviewsCount": 245
    },
    "history": {
      "owners": 1,
      "accidents": 0,
      "maintenance": {
        "isUpToDate": true,
        "lastService": "2023-11-15"
      }
    },
    "financing": {
      "available": true,
      "downPayment": 25000,
      "installments": [
        { "months": 24, "amount": 4500 },
        { "months": 36, "amount": 3200 },
        { "months": 48, "amount": 2600 }
      ]
    },
    "createdAt": "2023-12-01T10:30:00Z",
    "updatedAt": "2023-12-01T10:30:00Z",
    "viewsCount": 1520
  },
  "related": [
    {
      "id": "related-uuid-1",
      "brand": "Honda",
      "model": "Civic",
      "price": 115000,
      "year": 2022,
      "image": "https://cdn.example.com/thumb1.jpg"
    }
  ]
}
```

#### Sugestões de Busca
Retorna sugestões baseadas em busca parcial.

```http
GET /api/vehicles/suggestions
```

**Query Parameters:**
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| q | string | Sim | Termo parcial |
| limit | number | Não | Máximo de sugestões (padrão: 10) |

**Response:**
```json
{
  "suggestions": [
    {
      "text": "Honda Civic",
      "type": "brand_model",
      "count": 245
    },
    {
      "text": "Honda Accord",
      "type": "brand_model", 
      "count": 89
    },
    {
      "text": "Honda CR-V",
      "type": "brand_model",
      "count": 156
    }
  ]
}
```

### Filtros e Metadados

#### Marcas Disponíveis
```http
GET /api/brands
```

**Response:**
```json
{
  "data": [
    {
      "name": "Honda",
      "slug": "honda",
      "count": 1250,
      "logo": "https://cdn.example.com/logos/honda.png"
    },
    {
      "name": "Toyota", 
      "slug": "toyota",
      "count": 2100,
      "logo": "https://cdn.example.com/logos/toyota.png"
    }
  ]
}
```

#### Modelos por Marca
```http
GET /api/models/:brand
```

**Response:**
```json
{
  "data": [
    {
      "name": "Civic",
      "slug": "civic",
      "count": 245,
      "priceRange": { "min": 85000, "max": 165000 },
      "yearRange": { "min": 2018, "max": 2024 }
    },
    {
      "name": "Accord",
      "slug": "accord", 
      "count": 89,
      "priceRange": { "min": 120000, "max": 220000 },
      "yearRange": { "min": 2019, "max": 2024 }
    }
  ]
}
```

## Error Responses

### Formato Padrão
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request parameters",
    "details": [
      {
        "field": "price_min", 
        "message": "Must be a positive number"
      }
    ],
    "timestamp": "2023-12-01T10:30:00Z",
    "requestId": "req-uuid-v4"
  }
}
```

### Códigos de Erro
| Código | Status | Descrição |
|--------|--------|-----------|
| `VALIDATION_ERROR` | 400 | Parâmetros inválidos |
| `VEHICLE_NOT_FOUND` | 404 | Veículo não encontrado |
| `RATE_LIMIT_EXCEEDED` | 429 | Limite de requisições excedido |
| `INTERNAL_ERROR` | 500 | Erro interno do servidor |

## Paginação

### Padrão
- **Página padrão**: 1
- **Items por página**: 20 (máximo: 50)
- **Header `Link`**: Inclui links prev/next quando aplicável

### Response Headers
```http
X-Total-Count: 1250
X-Page-Count: 63
Link: <https://api.example.com/vehicles?page=2>; rel="next", 
      <https://api.example.com/vehicles?page=63>; rel="last"
```

## Cache

### Cache Headers
```http
Cache-Control: public, max-age=300
ETag: "hash-do-conteudo"
Last-Modified: Fri, 01 Dec 2023 10:30:00 GMT
```

### Invalidação
Cache é invalidado automaticamente quando:
- Novos veículos são adicionados
- Veículos existentes são atualizados
- Preços são alterados

## WebSocket (Opcional)

Para updates em tempo real:

```javascript
const ws = new WebSocket('ws://localhost:3001/ws');

ws.on('message', (data) => {
  const event = JSON.parse(data);
  // event.type: 'vehicle_added', 'vehicle_updated', 'price_changed'
});
```