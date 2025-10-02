# API Reference

## Base URL

```
http://localhost:3000/api/v1
```

## Authentication

Most endpoints require JWT Bearer token authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

Authentication tokens are obtained via the login endpoint and remain valid according to the configured expiration time.

---

## Users

### POST /users/register

Register a new user in the system.

**Authentication:** Not required

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe",
  "role": "seller"
}
```

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Valid email address |
| password | string | Yes | Minimum 6 characters |
| name | string | Yes | User full name (2-50 characters) |
| role | string | Yes | User role: `admin`, `manager`, or `seller` |

**Response (201):**

```json
{
  "success": true,
  "data": {
    "user": {
      "id": "507f1f77bcf86cd799439011",
      "email": "user@example.com",
      "name": "John Doe",
      "role": "seller"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

**Status Codes:**
- 201: User created successfully
- 400: Invalid input data
- 409: Email already exists

---

### POST /users/login

Authenticate a user and receive a JWT token.

**Authentication:** Not required

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | User email address |
| password | string | Yes | User password |

**Response (200):**

```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": "507f1f77bcf86cd799439011",
      "email": "user@example.com",
      "name": "John Doe",
      "role": "seller"
    }
  }
}
```

**Status Codes:**
- 200: Login successful
- 401: Invalid credentials
- 400: Invalid input data

---

### GET /users/profile

Get the authenticated user's profile.

**Authentication:** Required

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "seller",
    "isActive": true,
    "lastLogin": "2025-10-02T10:30:00.000Z",
    "createdAt": "2025-09-01T08:00:00.000Z"
  }
}
```

**Status Codes:**
- 200: Success
- 401: Unauthorized

---

### PUT /users/profile

Update the authenticated user's profile.

**Authentication:** Required

**Request Body:**

```json
{
  "email": "newemail@example.com",
  "name": "John Updated"
}
```

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | No | New email address |
| name | string | No | New name (2-50 characters) |

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "email": "newemail@example.com",
    "name": "John Updated",
    "role": "seller"
  }
}
```

**Status Codes:**
- 200: Update successful
- 400: Invalid input data
- 401: Unauthorized
- 409: Email already exists

---

### GET /users

Get all users (admin only).

**Authentication:** Required (Admin role)

**Response (200):**

```json
{
  "success": true,
  "data": [
    {
      "id": "507f1f77bcf86cd799439011",
      "email": "user@example.com",
      "name": "John Doe",
      "role": "seller",
      "isActive": true,
      "createdAt": "2025-09-01T08:00:00.000Z"
    }
  ]
}
```

**Status Codes:**
- 200: Success
- 401: Unauthorized
- 403: Forbidden (not admin)

---

### GET /users/:id

Get a specific user by ID (admin only).

**Authentication:** Required (Admin role)

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId (24 hex characters) |

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "seller",
    "isActive": true,
    "lastLogin": "2025-10-02T10:30:00.000Z",
    "createdAt": "2025-09-01T08:00:00.000Z"
  }
}
```

**Status Codes:**
- 200: Success
- 401: Unauthorized
- 403: Forbidden
- 404: User not found

---

### PUT /users/:id

Update a user by ID (admin only).

**Authentication:** Required (Admin role)

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Request Body:**

```json
{
  "email": "updated@example.com",
  "name": "Updated Name",
  "role": "manager",
  "isActive": false
}
```

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "email": "updated@example.com",
    "name": "Updated Name",
    "role": "manager",
    "isActive": false
  }
}
```

**Status Codes:**
- 200: Update successful
- 400: Invalid input
- 401: Unauthorized
- 403: Forbidden
- 404: User not found

---

### DELETE /users/:id

Delete a user by ID (admin only).

**Authentication:** Required (Admin role)

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Response (200):**

```json
{
  "success": true,
  "message": "User deleted successfully"
}
```

**Status Codes:**
- 200: Delete successful
- 401: Unauthorized
- 403: Forbidden
- 404: User not found

---

## Vehicles

### GET /vehicles

Get all vehicles with optional filters.

**Authentication:** Not required

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| brand | string | Filter by brand |
| vehicleModel | string | Filter by model |
| yearMin | number | Minimum year (1900+) |
| yearMax | number | Maximum year |
| priceMin | number | Minimum price |
| priceMax | number | Maximum price |
| fuelType | string | `gasoline`, `ethanol`, `diesel`, `electric`, `hybrid` |
| transmission | string | `manual`, `automatic` |
| category | string | `car`, `motorcycle`, `truck`, `van` |
| condition | string | `new`, `used` |
| city | string | Filter by city |
| state | string | Filter by state |
| status | string | `active`, `sold`, `inactive`, `pending` |
| isFeatured | boolean | Filter featured vehicles |
| page | number | Page number (default: 1) |
| limit | number | Results per page (1-100, default: 10) |
| sortBy | string | Field to sort by (default: createdAt) |
| sortOrder | string | `asc` or `desc` (default: desc) |

**Example Request:**

```
GET /vehicles?brand=Toyota&priceMin=20000&priceMax=50000&page=1&limit=10
```

**Response (200):**

```json
{
  "success": true,
  "data": {
    "vehicles": [
      {
        "id": "507f1f77bcf86cd799439011",
        "brand": "Toyota",
        "vehicleModel": "Corolla",
        "year": 2023,
        "mileage": 15000,
        "price": 85000,
        "fuelType": "hybrid",
        "transmission": "automatic",
        "color": "Silver",
        "doors": 4,
        "category": "car",
        "condition": "used",
        "description": "Excellent condition, single owner",
        "images": [
          "https://example.com/image1.jpg",
          "https://example.com/image2.jpg"
        ],
        "features": ["Air conditioning", "Leather seats", "Navigation"],
        "location": {
          "city": "São Paulo",
          "state": "SP",
          "zipCode": "01234-567"
        },
        "seller": {
          "id": "507f191e810c19729de860ea",
          "name": "John Dealer",
          "phone": "(11) 99999-9999",
          "email": "dealer@example.com"
        },
        "status": "active",
        "isFeatured": true,
        "views": 125,
        "createdAt": "2025-09-15T10:00:00.000Z",
        "updatedAt": "2025-10-01T14:30:00.000Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "totalPages": 5,
      "totalResults": 48
    }
  }
}
```

**Status Codes:**
- 200: Success
- 400: Invalid query parameters

---

### GET /vehicles/stats

Get vehicle statistics.

**Authentication:** Not required

**Response (200):**

```json
{
  "success": true,
  "data": {
    "totalVehicles": 150,
    "activeVehicles": 98,
    "soldVehicles": 42,
    "inactiveVehicles": 10,
    "totalViews": 12450,
    "averagePrice": 65000,
    "topBrands": [
      { "brand": "Toyota", "count": 25 },
      { "brand": "Honda", "count": 20 },
      { "brand": "Ford", "count": 18 }
    ],
    "topCities": [
      { "city": "São Paulo", "count": 45 },
      { "city": "Rio de Janeiro", "count": 30 }
    ]
  }
}
```

**Status Codes:**
- 200: Success

---

### GET /vehicles/:id

Get a specific vehicle by ID.

**Authentication:** Not required

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "brand": "Toyota",
    "vehicleModel": "Corolla",
    "year": 2023,
    "mileage": 15000,
    "price": 85000,
    "fuelType": "hybrid",
    "transmission": "automatic",
    "color": "Silver",
    "doors": 4,
    "category": "car",
    "condition": "used",
    "description": "Excellent condition, single owner",
    "images": ["https://example.com/image1.jpg"],
    "features": ["Air conditioning", "Leather seats"],
    "location": {
      "city": "São Paulo",
      "state": "SP",
      "zipCode": "01234-567"
    },
    "seller": {
      "id": "507f191e810c19729de860ea",
      "name": "John Dealer",
      "phone": "(11) 99999-9999",
      "email": "dealer@example.com"
    },
    "status": "active",
    "isFeatured": true,
    "views": 125,
    "createdAt": "2025-09-15T10:00:00.000Z",
    "updatedAt": "2025-10-01T14:30:00.000Z"
  }
}
```

**Status Codes:**
- 200: Success
- 404: Vehicle not found

---

### POST /vehicles

Create a new vehicle listing.

**Authentication:** Required (Admin, Manager, or Seller roles)

**Request Body:**

```json
{
  "brand": "Toyota",
  "vehicleModel": "Corolla",
  "year": 2023,
  "mileage": 15000,
  "price": 85000,
  "fuelType": "hybrid",
  "transmission": "automatic",
  "color": "Silver",
  "doors": 4,
  "category": "car",
  "condition": "used",
  "description": "Excellent condition, single owner",
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg"
  ],
  "features": ["Air conditioning", "Leather seats", "Navigation"],
  "location": {
    "city": "São Paulo",
    "state": "SP",
    "zipCode": "01234-567"
  },
  "seller": {
    "id": "507f191e810c19729de860ea",
    "name": "John Dealer",
    "phone": "(11) 99999-9999",
    "email": "dealer@example.com"
  },
  "isFeatured": false
}
```

**Parameters:**

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| brand | string | Yes | 2-50 characters |
| vehicleModel | string | Yes | 2-50 characters |
| year | number | Yes | 1900 to current year + 1 |
| mileage | number | Yes | >= 0 |
| price | number | Yes | >= 0 |
| fuelType | string | Yes | `gasoline`, `ethanol`, `diesel`, `electric`, `hybrid` |
| transmission | string | Yes | `manual`, `automatic` |
| color | string | Yes | 2-30 characters |
| doors | number | Yes | 2-6 |
| category | string | Yes | `car`, `motorcycle`, `truck`, `van` |
| condition | string | Yes | `new`, `used` |
| description | string | Yes | 10-2000 characters |
| images | array | Yes | 1-10 valid URIs |
| features | array | No | Max 20 items, each max 100 characters |
| location | object | Yes | city, state, zipCode (format: 12345-678) |
| seller | object | Yes | id, name, phone (format: (11) 99999-9999), email |
| isFeatured | boolean | No | Default: false |

**Response (201):**

```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "brand": "Toyota",
    "vehicleModel": "Corolla",
    "status": "active",
    "createdAt": "2025-10-02T15:30:00.000Z"
  }
}
```

**Status Codes:**
- 201: Vehicle created successfully
- 400: Invalid input data
- 401: Unauthorized
- 403: Forbidden

---

### PUT /vehicles/:id

Update a vehicle listing.

**Authentication:** Required

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Request Body:** (All fields are optional)

```json
{
  "price": 80000,
  "mileage": 16000,
  "status": "sold",
  "description": "Updated description"
}
```

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "price": 80000,
    "mileage": 16000,
    "status": "sold",
    "updatedAt": "2025-10-02T16:00:00.000Z"
  }
}
```

**Status Codes:**
- 200: Update successful
- 400: Invalid input data
- 401: Unauthorized
- 404: Vehicle not found

---

### DELETE /vehicles/:id

Delete a vehicle listing.

**Authentication:** Required

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Response (200):**

```json
{
  "success": true,
  "message": "Vehicle deleted successfully"
}
```

**Status Codes:**
- 200: Delete successful
- 401: Unauthorized
- 404: Vehicle not found

---

### PATCH /vehicles/:id/featured

Toggle featured status of a vehicle (admin only).

**Authentication:** Required (Admin role)

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "isFeatured": true
  }
}
```

**Status Codes:**
- 200: Success
- 401: Unauthorized
- 403: Forbidden
- 404: Vehicle not found

---

## Sales

### POST /sales

Create a new sale.

**Authentication:** Required (Admin, Manager, or Seller roles)

**Request Body:**

```json
{
  "vehicleId": "507f1f77bcf86cd799439011",
  "buyer": {
    "name": "Jane Smith",
    "email": "jane@example.com",
    "phone": "(11) 98888-8888",
    "document": "123.456.789-00"
  },
  "salePrice": 80000,
  "paymentMethod": "financing",
  "notes": "Customer approved for 48-month financing"
}
```

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| vehicleId | string | Yes | MongoDB ObjectId of the vehicle |
| buyer.name | string | Yes | Buyer full name (2-50 characters) |
| buyer.email | string | Yes | Buyer email address |
| buyer.phone | string | Yes | Format: (11) 99999-9999 |
| buyer.document | string | Yes | CPF format: 123.456.789-00 |
| salePrice | number | Yes | Sale price (>= 0) |
| paymentMethod | string | Yes | `cash`, `financing`, `trade-in` |
| notes | string | No | Additional notes (max 1000 characters) |

**Response (201):**

```json
{
  "success": true,
  "data": {
    "id": "507f191e810c19729de860ea",
    "vehicleId": "507f1f77bcf86cd799439011",
    "vehicle": {
      "brand": "Toyota",
      "vehicleModel": "Corolla",
      "year": 2023,
      "price": 85000
    },
    "buyer": {
      "name": "Jane Smith",
      "email": "jane@example.com",
      "phone": "(11) 98888-8888",
      "document": "123.456.789-00"
    },
    "seller": {
      "id": "507f1f77bcf86cd799439012",
      "name": "John Doe",
      "email": "john@example.com"
    },
    "salePrice": 80000,
    "commission": 4000,
    "status": "pending",
    "paymentMethod": "financing",
    "notes": "Customer approved for 48-month financing",
    "saleDate": "2025-10-02T16:30:00.000Z",
    "createdAt": "2025-10-02T16:30:00.000Z"
  }
}
```

**Status Codes:**
- 201: Sale created successfully
- 400: Invalid input data
- 401: Unauthorized
- 403: Forbidden
- 404: Vehicle not found

---

### GET /sales

Get all sales with optional filters.

**Authentication:** Required

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| sellerId | string | Filter by seller ID (MongoDB ObjectId) |
| status | string | `pending`, `completed`, `cancelled` |
| paymentMethod | string | `cash`, `financing`, `trade-in` |
| dateFrom | date | Filter sales from this date |
| dateTo | date | Filter sales until this date |
| page | number | Page number (default: 1) |
| limit | number | Results per page (1-100, default: 10) |
| sortBy | string | Field to sort by (default: saleDate) |
| sortOrder | string | `asc` or `desc` (default: desc) |

**Example Request:**

```
GET /sales?status=completed&dateFrom=2025-09-01&dateTo=2025-09-30&page=1&limit=20
```

**Response (200):**

```json
{
  "success": true,
  "data": {
    "sales": [
      {
        "id": "507f191e810c19729de860ea",
        "vehicleId": "507f1f77bcf86cd799439011",
        "vehicle": {
          "brand": "Toyota",
          "vehicleModel": "Corolla",
          "year": 2023,
          "price": 85000
        },
        "buyer": {
          "name": "Jane Smith",
          "email": "jane@example.com",
          "phone": "(11) 98888-8888",
          "document": "123.456.789-00"
        },
        "seller": {
          "id": "507f1f77bcf86cd799439012",
          "name": "John Doe",
          "email": "john@example.com"
        },
        "salePrice": 80000,
        "commission": 4000,
        "status": "completed",
        "paymentMethod": "financing",
        "saleDate": "2025-09-15T10:00:00.000Z",
        "createdAt": "2025-09-15T10:00:00.000Z",
        "updatedAt": "2025-09-20T14:30:00.000Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "totalPages": 3,
      "totalResults": 52
    }
  }
}
```

**Status Codes:**
- 200: Success
- 400: Invalid query parameters
- 401: Unauthorized

---

### GET /sales/stats

Get sales statistics.

**Authentication:** Required

**Response (200):**

```json
{
  "success": true,
  "data": {
    "totalSales": 150,
    "totalRevenue": 12500000,
    "totalCommission": 625000,
    "averageSalePrice": 83333,
    "salesByMonth": [
      {
        "month": "2025-09",
        "sales": 45,
        "revenue": 3800000
      },
      {
        "month": "2025-08",
        "sales": 52,
        "revenue": 4200000
      }
    ],
    "topSellers": [
      {
        "sellerId": "507f1f77bcf86cd799439012",
        "sellerName": "John Doe",
        "sales": 25,
        "revenue": 2100000
      },
      {
        "sellerId": "507f1f77bcf86cd799439013",
        "sellerName": "Jane Smith",
        "sales": 20,
        "revenue": 1750000
      }
    ],
    "salesByPaymentMethod": [
      {
        "method": "financing",
        "count": 85,
        "revenue": 7200000
      },
      {
        "method": "cash",
        "count": 45,
        "revenue": 3800000
      },
      {
        "method": "trade-in",
        "count": 20,
        "revenue": 1500000
      }
    ]
  }
}
```

**Status Codes:**
- 200: Success
- 401: Unauthorized

---

### GET /sales/my-sales

Get sales for the authenticated seller.

**Authentication:** Required

**Response (200):**

```json
{
  "success": true,
  "data": [
    {
      "id": "507f191e810c19729de860ea",
      "vehicleId": "507f1f77bcf86cd799439011",
      "vehicle": {
        "brand": "Toyota",
        "vehicleModel": "Corolla",
        "year": 2023,
        "price": 85000
      },
      "salePrice": 80000,
      "commission": 4000,
      "status": "completed",
      "saleDate": "2025-09-15T10:00:00.000Z"
    }
  ]
}
```

**Status Codes:**
- 200: Success
- 401: Unauthorized

---

### GET /sales/:id

Get a specific sale by ID.

**Authentication:** Required

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f191e810c19729de860ea",
    "vehicleId": "507f1f77bcf86cd799439011",
    "vehicle": {
      "brand": "Toyota",
      "vehicleModel": "Corolla",
      "year": 2023,
      "price": 85000
    },
    "buyer": {
      "name": "Jane Smith",
      "email": "jane@example.com",
      "phone": "(11) 98888-8888",
      "document": "123.456.789-00"
    },
    "seller": {
      "id": "507f1f77bcf86cd799439012",
      "name": "John Doe",
      "email": "john@example.com"
    },
    "salePrice": 80000,
    "commission": 4000,
    "status": "completed",
    "paymentMethod": "financing",
    "notes": "Customer approved for 48-month financing",
    "saleDate": "2025-09-15T10:00:00.000Z",
    "createdAt": "2025-09-15T10:00:00.000Z",
    "updatedAt": "2025-09-20T14:30:00.000Z"
  }
}
```

**Status Codes:**
- 200: Success
- 401: Unauthorized
- 404: Sale not found

---

### PUT /sales/:id

Update a sale.

**Authentication:** Required

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Request Body:** (All fields are optional)

```json
{
  "status": "completed",
  "salePrice": 82000,
  "notes": "Final price negotiated"
}
```

**Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "507f191e810c19729de860ea",
    "status": "completed",
    "salePrice": 82000,
    "notes": "Final price negotiated",
    "updatedAt": "2025-10-02T17:00:00.000Z"
  }
}
```

**Status Codes:**
- 200: Update successful
- 400: Invalid input data
- 401: Unauthorized
- 404: Sale not found

---

### DELETE /sales/:id

Delete a sale (admin only).

**Authentication:** Required (Admin role)

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | MongoDB ObjectId |

**Response (200):**

```json
{
  "success": true,
  "message": "Sale deleted successfully"
}
```

**Status Codes:**
- 200: Delete successful
- 401: Unauthorized
- 403: Forbidden
- 404: Sale not found

---

## Health Check

### GET /health

Check API health status.

**Authentication:** Not required

**Response (200):**

```json
{
  "success": true,
  "message": "API is running",
  "timestamp": "2025-10-02T17:30:00.000Z",
  "environment": "development"
}
```

**Status Codes:**
- 200: API is healthy

---

## Error Responses

All error responses follow this format:

```json
{
  "success": false,
  "error": "Error type",
  "message": "Detailed error message",
  "details": {}
}
```

### Common HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 201 | Resource created successfully |
| 400 | Bad request - Invalid input data |
| 401 | Unauthorized - Authentication required or token invalid |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not found - Resource does not exist |
| 409 | Conflict - Resource already exists |
| 429 | Too many requests - Rate limit exceeded |
| 500 | Internal server error |

---

## Rate Limiting

The API implements rate limiting to prevent abuse. Default limits:
- Window: Configurable (typically 15 minutes)
- Max requests: Configurable per window

When rate limit is exceeded, you'll receive:

```json
{
  "success": false,
  "error": "Too many requests",
  "message": "Rate limit exceeded. Please try again later."
}
```

**Status Code:** 429

---

## Additional Documentation

For interactive API documentation with request/response examples, visit:

```
http://localhost:3000/docs
```

This provides a Swagger UI interface for testing all endpoints.
