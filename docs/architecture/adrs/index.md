# Architecture Decision Records (ADRs)

Esta seção contém os Architecture Decision Records (ADRs) do domínio E-commerce de Veículos.

## O que são ADRs?

Architecture Decision Records são documentos que capturam decisões arquiteturais importantes junto com seu contexto e consequências. Cada ADR representa uma decisão significativa que afeta a estrutura, comportamento ou propriedades não-funcionais do sistema.

## Formato dos ADRs

Seguimos o template padrão de ADRs com as seguintes seções:

- **Status**: Proposed, Accepted, Deprecated, Superseded
- **Context**: Situação que força uma decisão
- **Decision**: A decisão arquitetural escolhida  
- **Consequences**: Resultado da decisão, positivas e negativas

## Lista de ADRs

### Status: Accepted ✅

- [ADR-001: Separação de Sistemas Vitrine e Backoffice](adr-001-separacao-sistemas.md)
- [ADR-002: Uso de BFF (Backend for Frontend)](adr-002-bff-pattern.md)
- [ADR-003: Banco de Dados Compartilhado](adr-003-shared-database.md)
- [ADR-004: Stack Node.js + TypeScript](adr-004-nodejs-typescript.md)
- [ADR-005: Cache Strategy com Redis](adr-005-cache-redis.md)

### Status: Proposed 🤔

- [ADR-006: Migração para Microserviços](adr-006-microservices.md)
- [ADR-007: Event-Driven Architecture](adr-007-event-driven.md)

### Status: Deprecated ❌

- [ADR-008: API Gateway Centralizado](adr-008-api-gateway.md) *(Superseded by ADR-002)*

## Como Contribuir

### Criando um Novo ADR

1. **Numeração**: Use o próximo número sequencial (ADR-XXX)
2. **Template**: Copie o template base abaixo
3. **Discussão**: Abra uma discussão antes de implementar
4. **Review**: ADRs devem ser revisados pela equipe de arquitetura

### Template ADR

```markdown
# ADR-XXX: Título da Decisão

## Status

Proposed / Accepted / Deprecated / Superseded by ADR-XXX

## Context

Descreva o contexto e as forças que influenciam a decisão.
- Restrições técnicas
- Requisitos de negócio  
- Limitações de tempo/recursos
- Decisões arquiteturais anteriores

## Decision

Descreva a decisão e justificativa completa.
- O que será implementado
- Como será implementado
- Por que esta abordagem foi escolhida
- Alternativas consideradas

## Consequences

### Positive
- Benefícios da decisão
- Problemas que resolve
- Melhorias que traz

### Negative  
- Trade-offs aceitos
- Complexidade adicionada
- Riscos introduzidos

### Neutral
- Mudanças necessárias
- Impacto em outras decisões
```

## Guidelines

### Quando Criar um ADR

Crie ADRs para decisões que:
- Afetam múltiplos sistemas ou equipes
- Têm impacto significativo na arquitetura
- São difíceis de reverter
- Geram debates técnicos na equipe
- Estabelecem padrões ou convenções

### Características de um Bom ADR

- **Conciso**: Informação necessária, sem excesso
- **Específico**: Decisão clara e acionável
- **Contextualizado**: Explica o "porquê" da decisão
- **Honesto**: Reconhece trade-offs e limitações
- **Versionado**: Rastreável no Git

## Processo de Review

1. **Draft**: Autor cria PR com ADR em status "Proposed"
2. **Discussion**: Equipe discute via comments no PR
3. **Refinement**: Autor incorpora feedback
4. **Approval**: Tech leads aprovam a decisão
5. **Merge**: ADR vira status "Accepted" e é mergeado

## Ferramentas

- **ADR Tools**: [adr-tools](https://github.com/npryce/adr-tools) para automação
- **Templates**: Modelos padronizados no repositório
- **Linting**: Validação automática de formato