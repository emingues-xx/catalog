# Arquitetura - backoffice-veiculos-bff

## Visão Geral

O `backoffice-veiculos-bff` é um Backend for Frontend (BFF) que atua como camada intermediária entre o backoffice de veículos e os serviços de backend. Este componente é responsável por agregar, transformar e otimizar dados para o consumo do frontend.

## Estrutura de Pastas

```
backoffice-veiculos-bff/
├── src/
│   ├── controllers/     # Controladores das rotas HTTP
│   ├── services/        # Lógica de negócio e integração
│   ├── models/          # Modelos de dados e DTOs
│   ├── routes/          # Definição de rotas da API
│   ├── middleware/      # Middlewares (auth, validation, etc)
│   └── config/          # Configurações da aplicação
├── tests/               # Testes unitários e integração
└── docs/                # Documentação adicional
```

## Componentes Principais

### Controllers
Responsáveis por receber requisições HTTP, validar entrada e retornar respostas apropriadas.

### Services
Contêm a lógica de negócio, incluindo:
- Integração com APIs de backend
- Agregação de dados de múltiplas fontes
- Transformação de dados para o formato do frontend

### Middleware
Camadas de processamento para:
- Autenticação e autorização
- Validação de requisições
- Tratamento de erros
- Logging

## Fluxo de Dados

```
Frontend (Backoffice)
       ↓
   [API Gateway]
       ↓
 backoffice-veiculos-bff
       ↓
  ┌────┴────┐
  ↓         ↓
Serviço A  Serviço B
  (API)     (API)
```

1. **Requisição**: Frontend envia requisição ao BFF
2. **Processamento**: BFF processa e faz chamadas aos serviços necessários
3. **Agregação**: Dados de múltiplos serviços são agregados e transformados
4. **Resposta**: BFF retorna dados otimizados para o frontend
