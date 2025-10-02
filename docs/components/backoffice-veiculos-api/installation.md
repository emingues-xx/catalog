# Installation

## Prerequisites

- Node.js 18+ and npm/yarn
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
# or
yarn install
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
DB_USER=your_db_user
DB_PASSWORD=your_db_password

# Authentication (if applicable)
JWT_SECRET=your_secret_key
JWT_EXPIRES_IN=24h

# API Keys (if applicable)
API_KEY=your_api_key
```

### 4. Database Setup

Run migrations to create the database schema:

```bash
npm run migrate
# or
yarn migrate
```

Seed initial data (optional):

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
npm start
# or
yarn build
yarn start
```

## Verification

### Health Check

```bash
curl http://localhost:3000/health
```

Expected response:
```json
{
  "status": "ok",
  "timestamp": "2025-10-02T00:00:00.000Z"
}
```

### Test API Endpoints

```bash
# List vehicles
curl http://localhost:3000/api/vehicles

# Get specific vehicle
curl http://localhost:3000/api/vehicles/{id}
```

### Run Tests

```bash
npm test
# or
yarn test
```

## Troubleshooting

- **Database connection error**: Verify database credentials in `.env` and ensure the database service is running
- **Port already in use**: Change the `PORT` value in `.env`
- **Missing dependencies**: Delete `node_modules` and run `npm install` again
