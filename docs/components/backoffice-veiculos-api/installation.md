# Installation Guide

## Prerequisites

- **Node.js**: >= 18.x
- **npm** or **yarn**
- **Database**: PostgreSQL 14+ or MySQL 8+
- **Git**

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/emingues-xx/backoffice-veiculos-api.git
cd backoffice-veiculos-api
```

### 2. Install Dependencies

```bash
npm install
# or
yarn install
```

### 3. Environment Configuration

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Configure the following environment variables:

```env
# Server
PORT=3000
NODE_ENV=development

# Database
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=backoffice_veiculos
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password

# JWT
JWT_SECRET=your_jwt_secret_key
JWT_EXPIRES_IN=24h

# API
API_PREFIX=/api/v1
```

### 4. Database Setup

Run migrations to create database schema:

```bash
npm run migration:run
# or
yarn migration:run
```

(Optional) Seed initial data:

```bash
npm run seed
# or
yarn seed
```

## Running the API

### Development Mode

```bash
npm run dev
# or
yarn dev
```

The API will be available at `http://localhost:3000`

### Production Mode

```bash
npm run build
npm run start:prod
# or
yarn build
yarn start:prod
```

## Verify Installation

### Health Check

```bash
curl http://localhost:3000/health
```

Expected response:
```json
{
  "status": "ok",
  "timestamp": "2025-10-02T10:00:00.000Z"
}
```

### API Documentation

Access Swagger documentation at:
```
http://localhost:3000/api/docs
```

### Test Endpoint

```bash
curl http://localhost:3000/api/v1/veiculos
```

## Troubleshooting

- **Database connection error**: Verify database credentials and ensure the database server is running
- **Port already in use**: Change the `PORT` in `.env` file
- **Migration errors**: Check database user permissions and schema access
