# E-commerce Veículos - UI Components

Design system e biblioteca de componentes React compartilhados para o domínio de e-commerce de veículos.

## Visão Geral

Esta biblioteca fornece componentes de interface reutilizáveis, garantindo consistência visual e de experiência em todos os sistemas do domínio.

## Componentes Disponíveis

### Layout
- **Container**: Wrapper responsivo para conteúdo
- **Grid**: Sistema de grid flexível
- **Card**: Cartões para exibição de conteúdo

### Formulários
- **Input**: Campos de entrada padronizados
- **Select**: Seletores com busca
- **Button**: Botões com variantes e estados
- **Form**: Wrapper para formulários

### Exibição
- **VehicleCard**: Cartão específico para veículos
- **PriceDisplay**: Exibição formatada de preços
- **ImageGallery**: Galeria de imagens
- **Badge**: Badges para status e categorias

### Navegação
- **Breadcrumb**: Navegação hierárquica
- **Pagination**: Paginação de listas
- **Tabs**: Navegação por abas

## Design System

### Cores
- **Primárias**: Azul corporativo
- **Secundárias**: Cinza e branco
- **Estados**: Sucesso, erro, aviso, info

### Tipografia
- **Fontes**: Inter (principal), Roboto (secundária)
- **Tamanhos**: Escala modular
- **Pesos**: Regular, Medium, Semibold, Bold

### Espaçamento
- **Grid**: 8px base
- **Margens**: 4px, 8px, 16px, 24px, 32px
- **Padding**: Consistente com grid

## Uso

```typescript
import { 
  VehicleCard, 
  Button, 
  Input,
  Container 
} from '@ecommerce-veiculos/ui-components';
```

## Storybook

Documentação interativa dos componentes disponível em:
- **Desenvolvimento**: http://localhost:6006
- **Produção**: [URL do Storybook]

## Contribuição

Para adicionar novos componentes:
1. Crie o componente em `src/components/`
2. Adicione stories em `src/stories/`
3. Documente no Storybook
4. Atualize esta documentação
