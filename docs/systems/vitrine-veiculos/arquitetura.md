# Arquitetura - Sistema Vitrine de Veículos

Visão técnica da arquitetura do sistema de vitrine pública.

## Visão Geral

O sistema segue uma arquitetura em camadas com separação clara de responsabilidades, otimizada para alta performance e escalabilidade na consulta pública de veículos.

## Componentes

### Frontend (vitrine-veiculos-web)
**Tecnologia**: React 18 + Next.js 14 + TypeScript

**Responsabilidades**:
- Renderização da interface de usuário
- Gerenciamento de estado local
- Otimizações de performance (SSR/SSG)
- SEO e meta tags dinâmicas

**Características**:
- Server Side Rendering para páginas de listagem
- Static Site Generation para páginas de detalhes
- Image optimization automática
- Code splitting por rotas

### BFF (vitrine-veiculos-bff)
**Tecnologia**: Node.js + Express + TypeScript

**Responsabilidades**:
- Agregação de dados de múltiplas APIs
- Transformação de dados para o frontend  
- Cache inteligente de consultas
- Rate limiting e throttling

**Endpoints principais**:
- `/api/veiculos` - Listagem com filtros
- `/api/veiculos/:id` - Detalhes do veículo
- `/api/search/suggestions` - Sugestões de busca
- `/api/filters/options` - Opções de filtros

### API Core (vitrine-veiculos-api)
**Tecnologia**: Node.js + Fastify + TypeScript

**Responsabilidades**:
- Lógica de negócio de consultas
- Acesso ao banco de dados
- Validação de dados
- Logging e monitoramento

## Fluxo de Dados

```
Usuário → Frontend → BFF → API Core → Database
                 ↙        ↙
              Cache    Cache
```

1. **Usuário** faz requisição no navegador
2. **Frontend** processa a requisição e chama o BFF
3. **BFF** verifica cache, se miss, chama API Core
4. **API Core** consulta banco de dados e retorna dados
5. **BFF** cacheia resultado e responde ao Frontend
6. **Frontend** renderiza dados para o usuário

## Estratégia de Cache

### Frontend (Browser)
- **Service Workers**: Cache de assets estáticos
- **LocalStorage**: Preferências do usuário
- **SessionStorage**: Estado temporário de filtros

### BFF (Redis)
- **Listagens**: 5 minutos TTL
- **Detalhes**: 15 minutos TTL  
- **Filtros**: 1 hora TTL
- **Busca**: 10 minutos TTL

### API Core (Database)
- **Query cache**: Índices otimizados
- **Connection pooling**: Reutilização de conexões

## Banco de Dados

### Estrutura Principal
- **veiculos**: Dados principais dos veículos
- **marcas**: Marcas disponíveis
- **modelos**: Modelos por marca
- **imagens**: Galeria de fotos
- **localizacao**: Estados e cidades

### Índices Otimizados
- Marca + Modelo + Ano
- Preço + Ano + Estado
- Geolocalização (lat/lng)
- Texto completo (marca, modelo, descrição)

## Performance

### Métricas Alvo
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Time to Interactive**: < 3.0s
- **Cumulative Layout Shift**: < 0.1

### Otimizações
- CDN para assets estáticos
- Image optimization e lazy loading
- Critical CSS inline
- Preload de recursos críticos
- Bundle splitting por rotas

## Monitoramento

- **APM**: New Relic para performance
- **Logs**: Winston + ELK Stack
- **Métricas**: Prometheus + Grafana
- **Uptime**: Pingdom para disponibilidade

## Segurança

- Rate limiting por IP
- Sanitização de inputs
- Headers de segurança (CSP, HSTS)
- CORS configurado apropriadamente
- Validação de schemas com Joi