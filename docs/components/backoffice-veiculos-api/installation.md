# Installation

## Prerequisites

- Node.js 18+ and npm
- PostgreSQL 14+ or MySQL 8+
- Git

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/emingues-xx/backoffice-veiculos-api.git
cd backoffice-veiculos-api
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Environment Configuration

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Configure the following variables:

```env
# Server
PORT=3000
NODE_ENV=development

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=backoffice_veiculos
DB_USER=your_user
DB_PASSWORD=your_password

# Authentication
JWT_SECRET=your_secret_key
JWT_EXPIRES_IN=24h

# API Settings
API_PREFIX=/api/v1
```

### 4. Database Setup

Run migrations:

```bash
npm run migrate
```

Seed initial data (optional):

```bash
npm run seed
```

## Running the API

### Development Mode

```bash
npm run dev
```

### Production Mode

```bash
npm run build
npm start
```

The API will be available at `http://localhost:3000`

## Verification

### Health Check

```bash
curl http://localhost:3000/api/v1/health
```

Expected response:
```json
{
  "status": "ok",
  "timestamp": "2025-10-02T10:00:00.000Z"
}
```

### Test Endpoints

List vehicles:
```bash
curl http://localhost:3000/api/v1/veiculos
```

### Run Tests

```bash
npm test
```

## Troubleshooting

- **Port already in use**: Change `PORT` in `.env`
- **Database connection failed**: Verify database credentials and ensure the database server is running
- **Migration errors**: Check database permissions and ensure the database exists
