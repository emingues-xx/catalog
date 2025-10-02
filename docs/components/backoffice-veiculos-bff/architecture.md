# Arquitetura - Backoffice Veículos BFF

## Visão Geral

O **backoffice-veiculos-bff** (Backend For Frontend) atua como camada intermediária entre o frontend do backoffice de veículos e os serviços de backend. Ele orquestra chamadas a múltiplas APIs, agrega dados e fornece endpoints otimizados para as necessidades específicas da interface do usuário.

## Estrutura de Pastas

```
backoffice-veiculos-bff/
├── src/
│   ├── controllers/     # Controladores HTTP
│   ├── services/        # Lógica de negócio e orquestração
│   ├── routes/          # Definição de rotas
│   ├── middlewares/     # Middlewares (auth, validação, etc)
│   ├── models/          # Modelos de dados
│   ├── utils/           # Utilitários e helpers
│   └── config/          # Configurações da aplicação
├── tests/               # Testes unitários e integração
└── docs/                # Documentação adicional
```

## Componentes Principais

### Controllers
Responsáveis por receber requisições HTTP, validar entrada e retornar respostas adequadas ao frontend.

### Services
Contêm a lógica de negócio, orquestram chamadas para APIs externas (como backoffice-veiculos-api) e agregam/transformam dados.

### Middlewares
- **Autenticação/Autorização**: Validação de tokens e permissões
- **Validação**: Validação de schemas de request
- **Error Handling**: Tratamento centralizado de erros

### Routes
Definem os endpoints disponíveis e mapeiam para os respectivos controllers.

## Fluxo de Dados

```
Frontend (UI)
    ↓
    → [BFF] Controllers
         ↓
    → [BFF] Services (orquestração)
         ↓
    → APIs Backend (backoffice-veiculos-api, etc)
         ↓
    ← Agregação de Dados
         ↓
    ← Resposta Formatada para Frontend
```

### Exemplo de Fluxo
1. Frontend solicita lista de veículos com detalhes de usuário
2. Controller recebe requisição e valida parâmetros
3. Service orquestra chamadas paralelas:
   - API de veículos para dados básicos
   - API de usuários para informações do proprietário
4. Service agrega e formata os dados
5. Controller retorna resposta otimizada para o frontend

## Integrações

- **backoffice-veiculos-api**: API principal para operações de veículos
- **Serviços de Autenticação**: Validação de usuários e permissões
- **Outros microserviços**: Conforme necessário para agregação de dados
