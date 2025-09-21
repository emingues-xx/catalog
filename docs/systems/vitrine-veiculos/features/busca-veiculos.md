# Feature: Busca de Veículos

Sistema avançado de busca e filtros para localização de veículos na vitrine.

## Descrição

A funcionalidade de busca permite que usuários encontrem veículos específicos através de múltiplos critérios de filtros, proporcionando uma experiência de navegação eficiente e personalizada.

## Funcionalidades

### Busca por Texto Livre
- Campo de busca principal para marcas, modelos ou palavras-chave
- Sugestões automáticas durante digitação
- Correção automática de termos

### Filtros Avançados

#### Filtros Básicos
- **Marca**: Lista de todas as marcas disponíveis
- **Modelo**: Modelos baseados na marca selecionada
- **Ano**: Slider com range de anos (mín/máx)
- **Preço**: Range de valores com formatação monetária

#### Filtros Técnicos
- **Combustível**: Flex, Gasolina, Álcool, Diesel, Elétrico, Híbrido
- **Transmissão**: Manual, Automática, CVT
- **Quilometragem**: Range de KM rodados
- **Cor**: Cores mais comuns dos veículos

#### Filtros de Localização
- **Estado**: Lista de UFs
- **Cidade**: Cidades baseadas no estado
- **Raio**: Distância em KM a partir de uma localização

### Ordenação
- Menor preço
- Maior preço  
- Menor quilometragem
- Ano mais recente
- Ano mais antigo
- Mais relevante

## Implementação Técnica

### Frontend (React)
```typescript
interface FiltrosVeiculo {
  marca?: string;
  modelo?: string;
  anoMin?: number;
  anoMax?: number;
  precoMin?: number;
  precoMax?: number;
  combustivel?: string[];
  estado?: string;
  cidade?: string;
}
```

### API Endpoints
- `GET /api/veiculos/search` - Busca com filtros
- `GET /api/marcas` - Lista de marcas
- `GET /api/modelos/:marca` - Modelos por marca
- `GET /api/cidades/:estado` - Cidades por estado

### Performance
- Cache de 5 minutos para listas estáticas (marcas, modelos)
- Debounce de 300ms na busca por texto
- Lazy loading dos resultados (20 por página)
- Índices otimizados no banco de dados

## Regras de Negócio

1. **Resultados**: Máximo 20 veículos por página
2. **Cache**: Filtros estáticos cacheados por 5 minutos  
3. **Ordenação padrão**: Mais relevante baseado em views e atualizações
4. **Limite geográfico**: Busca limitada ao território nacional

## Melhorias Futuras

- [ ] Busca por reconhecimento de voz
- [ ] Filtro por características específicas (ar condicionado, direção hidráulica)
- [ ] Comparação entre veículos
- [ ] Histórico de buscas do usuário
- [ ] Recomendações baseadas em comportamento