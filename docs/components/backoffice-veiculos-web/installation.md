# Installation Guide

## Prerequisites

- Node.js >= 18.x
- npm >= 9.x or yarn >= 1.22.x
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/emingues-xx/backoffice-veiculos-web.git
cd backoffice-veiculos-web
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

## Environment Configuration

Create a `.env` file in the project root:

```env
VITE_API_URL=http://localhost:3000
VITE_BFF_URL=http://localhost:4000
```

Available environment variables:
- `VITE_API_URL`: Backend API endpoint
- `VITE_BFF_URL`: BFF (Backend for Frontend) endpoint

## Running in Development

Start the development server:

```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:5173`

## Production Build

Build the application for production:

```bash
npm run build
# or
yarn build
```

The production-ready files will be generated in the `dist/` directory.

## Installation Verification

1. Ensure the development server starts without errors
2. Access `http://localhost:5173` in your browser
3. Check browser console for any errors
4. Verify API connectivity in the Network tab

## Troubleshooting

- Clear `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Clear cache: `npm run clean` (if available)
- Check Node.js version: `node --version`
