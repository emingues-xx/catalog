# Installation

## Prerequisites

- Node.js >= 18.x
- npm or yarn
- PostgreSQL/MySQL database (check `package.json` for specific database driver)
- Git

## Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/emingues-xx/backoffice-veiculos-api.git
cd backoffice-veiculos-api
```

2. **Install dependencies:**
```bash
npm install
# or
yarn install
```

3. **Configure environment variables:**

Create a `.env` file in the root directory:
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/backoffice_veiculos
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=backoffice_veiculos

# API
PORT=3000
NODE_ENV=development

# Authentication (if applicable)
JWT_SECRET=your_jwt_secret_key
JWT_EXPIRES_IN=1d

# Other configurations
API_PREFIX=/api
LOG_LEVEL=debug
```

4. **Run database migrations:**
```bash
npm run migrate
# or
npm run db:migrate
```

5. **Seed database (optional):**
```bash
npm run seed
```

## Running the API

### Development mode:
```bash
npm run dev
# or
yarn dev
```

### Production mode:
```bash
npm run build
npm start
```

The API will be available at `http://localhost:3000` (or the PORT specified in your `.env`).

## Verify Installation

Test the API health endpoint:
```bash
curl http://localhost:3000/health
# or
curl http://localhost:3000/api/health
```

Expected response:
```json
{
  "status": "ok",
  "timestamp": "2025-10-02T..."
}
```

Test a basic endpoint:
```bash
# List vehicles
curl http://localhost:3000/api/veiculos

# Get specific vehicle (if authentication not required)
curl http://localhost:3000/api/veiculos/1
```

## Troubleshooting

- **Database connection errors:** Verify DATABASE_URL and database credentials in `.env`
- **Port already in use:** Change PORT in `.env` file
- **Dependencies errors:** Delete `node_modules` and run `npm install` again
