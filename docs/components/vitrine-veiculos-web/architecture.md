# Arquitetura - vitrine-veiculos-web

Arquitetura detalhada do frontend da vitrine de veículos.

## Visão Geral

Aplicação Next.js 14 otimizada para performance e SEO, seguindo princípios de component-driven development e state management eficiente.

## Arquitetura de Componentes

```mermaid
graph TD
    A[App Router] --> B[Layout]
    B --> C[Pages]
    C --> D[Feature Components]
    D --> E[UI Components]
    
    F[Stores] --> D
    G[Hooks] --> D
    H[Utils] --> D
    
    I[BFF API] --> F
    J[External APIs] --> F
```

## Stack Técnico

### Core Framework
- **Next.js 14**: App Router para roteamento moderno
- **React 18**: Concurrent features e Suspense
- **TypeScript 5**: Type safety completo

### Styling e UI
```mermaid
graph LR
    A[Design Tokens] --> B[Styled Components]
    A --> C[CSS Modules]
    B --> D[Theme Provider]
    C --> D
    D --> E[Components]
```

**Approach**:
- Design tokens centralizados
- Styled Components para componentes dinâmicos
- CSS Modules para estilos estáticos
- Theme switching (light/dark)

### State Management

```mermaid
graph TD
    A[Zustand Store] --> B[Slices]
    B --> C[Vehicle Slice]
    B --> D[Search Slice]
    B --> E[User Slice]
    
    F[React Query] --> G[Server State]
    G --> H[API Queries]
    G --> I[Cache Management]
```

**Estratégia**:
- **Zustand**: Estado global da aplicação
- **React Query**: Estado do servidor e cache
- **React Hook Form**: Estado de formulários
- **Local Storage**: Persistência de preferências

## Estrutura de Pastas

```
src/
├── app/
│   ├── (marketing)/           # Grupo: páginas marketing
│   │   ├── page.tsx          # Homepage
│   │   └── sobre/            # Página sobre
│   ├── veiculos/             # Área de veículos
│   │   ├── page.tsx          # Listagem
│   │   ├── [slug]/           # Detalhes do veículo
│   │   └── buscar/           # Busca avançada
│   ├── layout.tsx            # Layout raiz
│   └── globals.css           # Estilos globais
├── components/
│   ├── ui/                   # Componentes base
│   │   ├── Button/
│   │   ├── Input/
│   │   └── Modal/
│   └── features/             # Componentes de negócio
│       ├── VehicleCard/
│       ├── SearchFilters/
│       └── VehicleGallery/
├── hooks/                    # Custom hooks
├── stores/                   # Zustand stores
├── lib/                      # Configurações
└── types/                    # TypeScript types
```

## Routing Strategy

### App Router (Next.js 14)
```mermaid
graph TD
    A[/] --> B[Homepage]
    C[/veiculos] --> D[Vehicle List]
    E[/veiculos/[slug]] --> F[Vehicle Details]
    G[/buscar] --> H[Advanced Search]
    
    I[Middleware] --> J[Auth Check]
    I --> K[Geo Location]
    I --> L[A/B Testing]
```

**Características**:
- Server Components por padrão
- Client Components apenas quando necessário
- Streaming para carregamento progressivo
- Suspense boundaries para fallbacks

## Data Flow

```mermaid
sequenceDiagram
    participant U as User
    participant C as Component
    participant S as Store
    participant Q as React Query
    participant A as API
    
    U->>C: Interaction
    C->>S: Update State
    S->>Q: Trigger Query
    Q->>A: HTTP Request
    A-->>Q: Response
    Q-->>S: Update Cache
    S-->>C: Re-render
    C-->>U: Updated UI
```

## Performance Architecture

### Bundle Optimization
```mermaid
graph TD
    A[Source Code] --> B[Webpack]
    B --> C[Code Splitting]
    C --> D[Route Chunks]
    C --> E[Vendor Chunks]
    C --> F[Common Chunks]
    
    G[Tree Shaking] --> B
    H[Dead Code Elimination] --> B
```

### Loading Strategy
- **Critical CSS**: Inline para above-the-fold
- **Image Optimization**: Next.js Image component
- **Prefetching**: Automatic para links visíveis
- **Service Worker**: Cache de assets

### Caching Layers
```mermaid
graph LR
    A[Browser Cache] --> B[Service Worker]
    B --> C[React Query Cache]
    C --> D[Zustand Store]
    D --> E[Local Storage]
```

## Security

### Client-Side Security
- **Content Security Policy**: Configurado no Next.js
- **XSS Protection**: Sanitização automática do React
- **Input Validation**: Zod schemas
- **Environment Variables**: Segregação public/private

### API Security
```typescript
// Exemplo de interceptor Axios
axios.interceptors.request.use((config) => {
  // Rate limiting headers
  config.headers['X-RateLimit-User'] = getUserId();
  
  // CSRF protection
  config.headers['X-CSRF-Token'] = getCSRFToken();
  
  return config;
});
```

## Testing Architecture

```mermaid
graph TD
    A[Unit Tests] --> B[Jest]
    C[Component Tests] --> D[React Testing Library]
    E[Integration Tests] --> F[MSW]
    G[E2E Tests] --> H[Playwright]
    
    I[Test Utils] --> B
    I --> D
    I --> F
```

### Testing Strategy
- **Unit**: Lógica de negócio e utilitários
- **Component**: Comportamento dos componentes
- **Integration**: Fluxos completos com API mock
- **E2E**: Jornadas críticas do usuário

## Monitoring

### Client-Side Monitoring
```mermaid
graph TD
    A[Web Vitals] --> B[Performance API]
    C[Error Boundary] --> D[Sentry]
    E[Analytics] --> F[Google Analytics]
    G[User Behavior] --> H[Hotjar]
```

### Métricas Coletadas
- **Performance**: Core Web Vitals
- **Errors**: JavaScript errors e crashes
- **Usage**: Page views, interactions
- **Business**: Conversion funnels

## Deployment

### Build Process
```mermaid
graph LR
    A[Git Push] --> B[GitHub Actions]
    B --> C[Install Dependencies]
    C --> D[Type Check]
    D --> E[Lint & Test]
    E --> F[Build]
    F --> G[Deploy to Vercel]
```

### Environments
- **Development**: Local com hot reload
- **Staging**: Preview deployments (Vercel)
- **Production**: Main branch auto-deploy