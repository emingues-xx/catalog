# Installation

## Prerequisites

- Node.js >= 18.x
- npm >= 9.x or yarn >= 1.22.x
- Git

## Installation Commands

```bash
# Clone the repository
git clone https://github.com/emingues-xx/backoffice-veiculos-api.git

# Navigate to project directory
cd backoffice-veiculos-api

# Install dependencies
npm install
```

## How to Run

```bash
# Development mode
npm run dev

# Production mode
npm start
```

## Installation Verification

After installation, verify the setup:

```bash
# Check if the API is running
curl http://localhost:3000/health

# Or access in browser
# http://localhost:3000
```

Expected response: API should return a healthy status or welcome message.
