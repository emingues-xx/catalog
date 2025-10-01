# Arquitetura - backoffice-veiculos-api

## Visão Geral

API backend desenvolvida em Node.js/TypeScript para gestão de veículos. O sistema fornece endpoints REST para operações de backoffice relacionadas ao gerenciamento de veículos, com suporte a containerização Docker e CI/CD automatizado.

## Stack Tecnológica

- **Runtime:** Node.js
- **Linguagem:** TypeScript (71% do código)
- **Testes:** Jest
- **Containerização:** Docker
- **CI/CD:** GitHub Actions
- **Deployment:** Railway, Docker

## Estrutura de Pastas

```
backoffice-veiculos-api/
├── src/                      # Código-fonte principal da aplicação
├── workflows/                # Configurações GitHub Actions
├── tests/                    # Testes automatizados
├── Dockerfile                # Configuração do container
├── tsconfig.json             # Configuração TypeScript
├── package.json              # Dependências e scripts
└── env.example               # Template de variáveis de ambiente
```

## Componentes Principais

### 1. API REST
- Endpoints para gerenciamento de veículos
- Configuração CORS
- Middleware de autenticação e validação

### 2. Sistema de CI/CD
- GitHub Actions para avaliação automática de PRs
- Pipeline de testes automatizados
- Deploy automático para ambientes

### 3. Camada de Configuração
- Gerenciamento de variáveis de ambiente
- Configurações específicas por ambiente
- Suporte a múltiplas plataformas de deployment

## Fluxo de Dados

1. **Requisição HTTP** → Cliente envia requisição para API
2. **Middleware** → Validação, autenticação e CORS
3. **Controller** → Processa lógica de negócio
4. **Resposta** → Retorna dados formatados ao cliente

## Deployment

- **Desenvolvimento:** nodemon para hot-reload
- **Produção:** Container Docker ou Railway
- **CI/CD:** Automação via GitHub Actions
