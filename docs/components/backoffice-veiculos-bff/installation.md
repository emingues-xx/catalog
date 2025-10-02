# Installation

## Prerequisites

- Node.js 18+ and npm/yarn
- Git
- Access to the repository: https://github.com/emingues-xx/backoffice-veiculos-bff.git

## Installation Commands

```bash
# Clone the repository
git clone https://github.com/emingues-xx/backoffice-veiculos-bff.git
cd backoffice-veiculos-bff

# Install dependencies
npm install
# or
yarn install
```

## How to Run

```bash
# Development mode
npm run dev
# or
yarn dev

# Production mode
npm start
# or
yarn start
```

## Installation Verification

1. Check if the application is running:
   ```bash
   curl http://localhost:3000/health
   ```

2. Verify the logs for any errors:
   ```bash
   npm run logs
   ```

3. Confirm all dependencies are installed:
   ```bash
   npm list
   ```
