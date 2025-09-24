# MongoDB Database

Banco de dados MongoDB para armazenamento de dados do e-commerce de veículos.

## Visão Geral

O MongoDB é o banco de dados principal do sistema de e-commerce de veículos, responsável por armazenar todos os dados relacionados a veículos, anúncios, usuários e transações.

## Configuração

### Conexão
- **Host**: `mongodb://localhost:27017` (desenvolvimento)
- **Database**: `ecommerce_veiculos`
- **Autenticação**: Configurada via variáveis de ambiente

### Variáveis de Ambiente
```bash
MONGODB_URI=mongodb://localhost:27017/ecommerce_veiculos
MONGODB_USER=admin
MONGODB_PASSWORD=password
```

## Estrutura de Dados

### Coleções Principais

#### `vehicles`
```javascript
{
  _id: ObjectId,
  brand: String,
  model: String,
  year: Number,
  price: Number,
  mileage: Number,
  fuelType: String,
  transmission: String,
  color: String,
  images: [String],
  features: [String],
  status: String, // available, sold, reserved
  createdAt: Date,
  updatedAt: Date
}
```

#### `announcements`
```javascript
{
  _id: ObjectId,
  vehicleId: ObjectId,
  sellerId: ObjectId,
  title: String,
  description: String,
  price: Number,
  status: String, // active, inactive, sold
  publishedAt: Date,
  expiresAt: Date,
  views: Number,
  createdAt: Date,
  updatedAt: Date
}
```

#### `users`
```javascript
{
  _id: ObjectId,
  name: String,
  email: String,
  phone: String,
  role: String, // admin, seller, buyer
  isActive: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

#### `sales`
```javascript
{
  _id: ObjectId,
  announcementId: ObjectId,
  buyerId: ObjectId,
  sellerId: ObjectId,
  vehicleId: ObjectId,
  price: Number,
  status: String, // pending, completed, cancelled
  paymentMethod: String,
  createdAt: Date,
  completedAt: Date
}
```

## Índices

### Índices de Performance
```javascript
// Vehicles
db.vehicles.createIndex({ "brand": 1, "model": 1 })
db.vehicles.createIndex({ "price": 1 })
db.vehicles.createIndex({ "year": 1 })
db.vehicles.createIndex({ "status": 1 })

// Announcements
db.announcements.createIndex({ "status": 1, "publishedAt": -1 })
db.announcements.createIndex({ "sellerId": 1 })
db.announcements.createIndex({ "vehicleId": 1 })

// Users
db.users.createIndex({ "email": 1 }, { unique: true })
db.users.createIndex({ "role": 1 })

// Sales
db.sales.createIndex({ "buyerId": 1 })
db.sales.createIndex({ "sellerId": 1 })
db.sales.createIndex({ "status": 1 })
```

## Operações Comuns

### Consultas de Veículos
```javascript
// Buscar veículos por marca e modelo
db.vehicles.find({
  brand: "Toyota",
  model: "Corolla",
  status: "available"
})

// Buscar veículos por faixa de preço
db.vehicles.find({
  price: { $gte: 30000, $lte: 50000 },
  status: "available"
}).sort({ price: 1 })
```

### Consultas de Anúncios
```javascript
// Anúncios ativos ordenados por data
db.announcements.find({
  status: "active"
}).sort({ publishedAt: -1 })

// Anúncios de um vendedor
db.announcements.find({
  sellerId: ObjectId("..."),
  status: "active"
})
```

## Backup e Restore

### Backup
```bash
mongodump --uri="mongodb://localhost:27017/ecommerce_veiculos" --out=/backup/
```

### Restore
```bash
mongorestore --uri="mongodb://localhost:27017/ecommerce_veiculos" /backup/ecommerce_veiculos/
```

## Monitoramento

### Métricas Importantes
- **Conexões ativas**: Número de conexões simultâneas
- **Operações por segundo**: QPS de leitura e escrita
- **Tamanho do banco**: Espaço utilizado
- **Índices**: Eficiência dos índices

### Logs
- **Slow queries**: Consultas que demoram mais de 100ms
- **Erros de conexão**: Falhas na conexão
- **Operações de escrita**: Logs de inserção/atualização

## Segurança

### Autenticação
- Usuário e senha configurados via variáveis de ambiente
- Acesso restrito por IP em produção
- SSL/TLS habilitado para conexões remotas

### Autorização
- Roles específicos para diferentes tipos de usuário
- Controle de acesso baseado em coleções
- Auditoria de operações sensíveis

## Dependências

### Componentes que usam este banco:
- **backoffice-veiculos-api**: CRUD de anúncios e usuários
- **vitrine-veiculos-api**: Consultas públicas de veículos
- **backoffice-veiculos-bff**: Agregação de dados para frontend
- **vitrine-veiculos-bff**: Agregação de dados para vitrine

## Troubleshooting

### Problemas Comuns
1. **Conexão recusada**: Verificar se o MongoDB está rodando
2. **Timeout**: Verificar configurações de timeout
3. **Índices lentos**: Analisar e otimizar consultas
4. **Espaço em disco**: Monitorar crescimento do banco

### Comandos Úteis
```javascript
// Verificar status
db.serverStatus()

// Verificar conexões
db.serverStatus().connections

// Verificar operações
db.serverStatus().opcounters

// Verificar índices
db.vehicles.getIndexes()
```
