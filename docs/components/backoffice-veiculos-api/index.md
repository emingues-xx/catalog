# Backoffice Veículos API

## Visão Geral

API backend Node.js/TypeScript responsável por gerenciar operações administrativas relacionadas a veículos no sistema de backoffice. A API fornece endpoints RESTful para CRUD de anúncios, usuários e acompanhamento de vendas.

## Propósito

Fornecer endpoints para:
- Cadastro e gerenciamento de anúncios de veículos
- Gestão de usuários e vendedores
- Acompanhamento de vendas e métricas
- Operações administrativas do backoffice
- Integração com sistemas internos e externos

## Tecnologias Utilizadas

- **Runtime**: Node.js
- **Linguagem**: TypeScript
- **Framework**: Express.js ou NestJS
- **Banco de Dados**: MongoDB
- **Autenticação**: JWT (JSON Web Tokens)
- **Containerização**: Docker
- **Deploy**: Railway
- **CI/CD**: GitHub Actions com avaliação automática de PRs

## Funcionalidades Principais

### Gestão de Anúncios
- CRUD completo de anúncios de veículos
- Upload e gerenciamento de imagens
- Controle de status (ativo/inativo/vendido)
- Filtros e busca avançada

### Gestão de Usuários
- Cadastro e autenticação de vendedores
- Controle de permissões e roles
- Auditoria de ações dos usuários
- Gerenciamento de sessões

### Métricas de Vendas
- API RESTful para métricas de performance comercial
- Consolidação de dados de vendas em tempo real
- Filtros por período personalizáveis
- Cache Redis para otimização de performance
- Job de atualização diária automatizado
- Monitoramento e health checks

### Acompanhamento de Vendas
- Métricas de vendas por período
- Relatórios de performance
- Dashboard de indicadores
- Integração com sistemas de pagamento

## Arquitetura

A API segue uma arquitetura modular com:
- **Controllers**: Gerenciamento de rotas e requisições
- **Services**: Lógica de negócio
- **Models**: Definição de entidades e schemas
- **Middleware**: Autenticação, validação e logs
- **Utils**: Funções auxiliares e helpers

## GitHub Actions

O repositório inclui workflows automatizados para:
- **Avaliação de Pull Requests**: Sistema de avaliação automática usando webhook
- **CI/CD**: Testes automatizados e deploy
- **Qualidade de Código**: Linting e formatação

### Configuração do Webhook
- **Secret**: `DF94AEC11B7255BA28B4934259186`
- **API URL**: `https://claude-webhook-production.up.railway.app/evaluate-pullrequest`

## Estrutura do Projeto

```
src/
├── controllers/     # Controladores das rotas
├── services/        # Lógica de negócio
├── models/          # Modelos de dados
├── middleware/      # Middlewares customizados
├── routes/          # Definição de rotas
├── utils/           # Utilitários e helpers
└── types/           # Definições TypeScript
```

## Documentação da API

A API utiliza OpenAPI/Swagger para documentação automática dos endpoints. A documentação está disponível em:
- **Desenvolvimento**: `http://localhost:3000/api-docs`
- **Produção**: `https://backoffice-veiculos-api.railway.app/api-docs`

## Exemplos de Uso

### Autenticação
```bash
curl -X POST https://api.backoffice-veiculos.com/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "vendedor@exemplo.com", "password": "senha123"}'
```

### Criar Anúncio
```bash
curl -X POST https://api.backoffice-veiculos.com/anuncios \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Honda Civic 2020",
    "preco": 85000,
    "descricao": "Veículo em excelente estado",
    "marca": "Honda",
    "modelo": "Civic"
  }'
```

## Links Úteis

- [Repositório](https://github.com/emingues-xx/backoffice-veiculos-api)
- [Documentação da API](https://backoffice-veiculos-api.railway.app/api-docs)
- [Exemplos de CURL](https://github.com/emingues-xx/backoffice-veiculos-api/blob/main/API_CURL_EXAMPLES.md)
- [Deploy no Railway](https://railway.app)
