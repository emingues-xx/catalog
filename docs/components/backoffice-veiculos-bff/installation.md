# Installation

## Prerequisites

- Node.js 18.x or higher
- npm or yarn package manager
- Git
- Access to the repository: https://github.com/emingues-xx/backoffice-veiculos-bff.git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/emingues-xx/backoffice-veiculos-bff.git
cd backoffice-veiculos-bff
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the Application

### Development Mode
```bash
npm run dev
```

### Production Mode
```bash
npm run build
npm start
```

## Installation Verification

1. Check if the application is running:
```bash
curl http://localhost:3000/health
```

2. Expected response:
```json
{
  "status": "ok"
}
```

3. View application logs to confirm successful startup
