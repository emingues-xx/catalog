# Configuração do Backstage para APIs

## Problema

O Backstage está tentando ler definições de API de URLs externas usando o placeholder `$text`, mas esses hosts não estão na lista de hosts permitidos.

## Solução

Adicione os domínios permitidos na configuração do Backstage (`app-config.yaml` ou `app-config.production.yaml`):

```yaml
backend:
  reading:
    allow:
      - host: 'back-ie-dash-financeiro-dev.edtech.com.br'
      - host: 'back-ie-dash-financeiro-hmg.edtech.com.br'
      - host: 'back-ie-dash-financeiro-prod.edtech.com.br'
      # Adicione todos os outros hosts necessários
      - host: '*.edtech.com.br'  # Ou use wildcard para todos os subdomínios
```

### Lista de Hosts Necessários

Com base nas APIs do catálogo, os seguintes hosts precisam ser permitidos:

- `back-ie-*-dev.edtech.com.br` (todos os serviços IE em dev)
- `back-hub-*-dev.edtech.com.br` (todos os serviços Hub em dev)
- `back-dash-*-dev.edtech.com.br` (todos os dashboards em dev)
- `back-*-dev.edtech.com.br` (outros serviços em dev)
- `back-*-hmg.edtech.com.br` (serviços em homologação)
- `back-*-prod.edtech.com.br` (serviços em produção)

### Configuração Recomendada

Para permitir todos os subdomínios `.edtech.com.br`:

```yaml
backend:
  reading:
    allow:
      - host: '*.edtech.com.br'
```

**Nota de Segurança:** Usar wildcards pode ser menos seguro. Considere listar hosts específicos em ambientes de produção.

## Alternativa: Usar Definições Locais

Se preferir não permitir acesso externo, você pode:

1. Baixar as definições OpenAPI/Swagger localmente
2. Armazená-las no repositório
3. Referenciar os arquivos locais ao invés de URLs externas

Exemplo:
```yaml
spec:
  definition:
    $text: ./openapi-specs/api-ie-dash-financeiro.json
```
