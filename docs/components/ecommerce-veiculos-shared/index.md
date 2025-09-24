# E-commerce Veículos - Shared Library

Biblioteca compartilhada com tipos TypeScript, utilitários e funções comuns para o domínio de e-commerce de veículos.

## Visão Geral

Esta biblioteca centraliza código comum usado por todos os componentes do domínio, garantindo consistência e reutilização.

## Funcionalidades

### Tipos TypeScript
- Interfaces para veículos, anúncios e usuários
- Tipos para APIs e responses
- Enums para status e categorias

### Utilitários
- Funções de validação
- Helpers para formatação
- Utilitários de data e hora

### Constantes
- Configurações compartilhadas
- URLs e endpoints
- Mensagens de erro padronizadas

## Uso

```typescript
import { Vehicle, VehicleStatus } from '@ecommerce-veiculos/shared';
import { formatPrice, validateEmail } from '@ecommerce-veiculos/shared/utils';
```

## Estrutura

```
src/
├── types/          # Tipos TypeScript
├── utils/          # Funções utilitárias
├── constants/      # Constantes compartilhadas
└── validators/     # Funções de validação
```

## Dependências

Esta biblioteca é usada por todos os outros componentes do domínio:
- Vitrine de Veículos (API, BFF, Web)
- Backoffice de Veículos (API, BFF, Web)
- Pipelines e automações
