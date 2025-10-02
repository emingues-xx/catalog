# Installation

## Prerequisites

- Node.js 18+ and npm/yarn
- PostgreSQL 14+ or compatible database
- Git

## Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/emingues-xx/backoffice-veiculos-api.git
cd backoffice-veiculos-api
```

2. Install dependencies:
```bash
npm install
```

## Environment Configuration

Create a `.env` file in the project root:

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/backoffice_veiculos
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=backoffice_veiculos
DATABASE_USER=user
DATABASE_PASSWORD=password

# Server
PORT=3000
NODE_ENV=development

# API Keys (if applicable)
API_KEY=your_api_key_here
```

## Running the API

### Development mode:
```bash
npm run dev
```

### Production mode:
```bash
npm run build
npm start
```

## Installation Verification

Test the API health endpoint:

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

Test API endpoints:
```bash
# List vehicles
curl http://localhost:3000/api/veiculos

# Get specific vehicle
curl http://localhost:3000/api/veiculos/{id}
```

The API should be running at `http://localhost:3000`
