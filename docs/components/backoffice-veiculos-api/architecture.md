# Arquitetura - Backoffice Veículos API

## Visão Geral

API REST desenvolvida para gerenciar o backoffice de veículos, fornecendo endpoints para operações CRUD e consultas relacionadas ao cadastro e gestão de veículos.

## Estrutura de Pastas

```
backoffice-veiculos-api/
├── src/
│   ├── controllers/     # Controladores das rotas
│   ├── models/          # Modelos de dados
│   ├── services/        # Lógica de negócio
│   ├── routes/          # Definição de rotas
│   ├── middlewares/     # Middlewares de autenticação e validação
│   ├── config/          # Configurações da aplicação
│   └── utils/           # Utilitários e helpers
├── tests/               # Testes automatizados
└── docs/                # Documentação adicional
```

## Componentes Principais

### Controllers
Responsáveis por receber as requisições HTTP, validar os dados de entrada e delegar a execução para os services.

### Services
Contêm a lógica de negócio da aplicação, realizando operações sobre os dados de veículos e integrações necessárias.

### Models
Definem a estrutura dos dados e mapeamento com o banco de dados.

### Middlewares
- **Autenticação**: Validação de tokens e permissões
- **Validação**: Verificação de dados de entrada
- **Error Handling**: Tratamento centralizado de erros

## Fluxo de Dados

1. **Requisição**: Cliente envia requisição HTTP para a API
2. **Middleware**: Autenticação e validação dos dados
3. **Controller**: Recebe a requisição e extrai os parâmetros
4. **Service**: Executa a lógica de negócio
5. **Model**: Acessa/persiste dados no banco
6. **Resposta**: Retorna resultado ao cliente em formato JSON
