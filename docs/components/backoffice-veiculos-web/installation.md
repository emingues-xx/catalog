# Installation

## Prerequisites

- Node.js >= 16.x
- npm >= 8.x or yarn >= 1.22.x
- Git

## Installation Steps

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

Create a `.env` file in the root directory:

```env
REACT_APP_API_URL=http://localhost:3000
REACT_APP_BFF_URL=http://localhost:4000
REACT_APP_ENV=development
```

Adjust the values according to your environment.

## Running in Development

Start the development server:

```bash
npm start
# or
yarn start
```

The application will be available at `http://localhost:3000`

## Building for Production

Generate the production build:

```bash
npm run build
# or
yarn build
```

The optimized files will be generated in the `build/` directory.

## Installation Verification

After starting the development server, verify that:

1. The application loads without errors in the browser
2. The console shows no critical errors
3. The API connection is working (check network tab)
4. Static assets are loading correctly

To test the production build locally:

```bash
npx serve -s build
```
