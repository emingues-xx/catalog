# Resources do Backstage

Este diretório contém as definições de Resources (recursos externos) do sistema.

## 📋 O que são Resources no Backstage?

Resources são entidades que representam recursos externos utilizados pelas aplicações, como:
- **Databases** (MySQL, PostgreSQL, MongoDB, Redis, etc.)
- **SQS Queues** (Amazon Simple Queue Service)
- **API Gateways**
- **Outros recursos de infraestrutura**

## 🏗️ Estrutura de um Resource

### Database

```yaml
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: database-{nome}-{tipo}
  title: Database {Nome} {Tipo}
  description: |
    | Database | Tipo | Ambiente |
    | ------   | ---- | -------- |
    | {nome} | {tipo} | Production |
  tags:
  - database
  - {tipo}
spec:
  type: database
  lifecycle: production
  owner: group:{time}
  system: {sistema}
```

### SQS Queue

```yaml
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: sqs-{nome-queue}
  title: SQS {Nome Queue}
  description: |
    | Queue | Tipo | Ambiente |
    | ------ | ---- | -------- |
    | {nome-queue} | SQS Standard | Production |
  tags:
  - sqs
  - queue
spec:
  type: sqs-queue
  lifecycle: production
  owner: group:{time}
  system: {sistema}
```

## 📁 Estrutura de Diretórios

```
resources/
  ├── database/
  │   ├── database-back-pedidos-mysql.yaml
  │   ├── database-back-pagamentos-mysql.yaml
  │   └── ...
  └── sqs/
      ├── sqs-hubspot-create-contact-deal-hub.yaml
      ├── sqs-bank-slip-installments-hub.yaml
      └── ...
```

## 🔗 Relação com Componentes

Os Resources são referenciados nas Aplicações através do campo `dependsOn`:

```yaml
spec:
  dependsOn:
    - component:back-hub-pedidos
    - resource:database-back-pedidos-mysql
    - resource:sqs-hubspot-create-contact-deal-hub
```

## 📝 Convenções de Nomenclatura

### Databases
- Nome: `database-{nome-servico}-{tipo}`
- Exemplo: `database-back-pedidos-mysql`, `database-back-pagamentos-mysql`

### SQS Queues
- Nome: `sqs-{nome-queue}`
- Exemplo: `sqs-hubspot-create-contact-deal-hub`, `sqs-bank-slip-installments-hub`

## ✅ Checklist para Criar um Resource

### Database:
- [ ] Nome segue o padrão `database-{nome}-{tipo}`
- [ ] Tem descrição com tabela de informações
- [ ] Tem tags relevantes (database, tipo, domínio)
- [ ] Tem annotations com tipo e ORM (se aplicável)
- [ ] `owner` e `system` estão corretos

### SQS Queue:
- [ ] Nome segue o padrão `sqs-{nome-queue}`
- [ ] Tem descrição com tabela de informações
- [ ] Tem tags relevantes (sqs, queue, domínio)
- [ ] `owner` e `system` estão corretos

## 📊 Resources Disponíveis

### Databases
- `database-back-pedidos-mysql` - Database de Pedidos
- `database-back-pagamentos-mysql` - Database de Pagamentos
- `database-back-contratos-mysql` - Database de Contratos
- `database-back-clientes-mysql` - Database de Clientes
- `database-back-promocoes-mysql` - Database de Promoções

### SQS Queues
- `sqs-hubspot-create-contact-deal-hub` - Fila para criação de contatos/negócios no Hubspot
- `sqs-bank-slip-installments-hub` - Fila para parcelas de boleto
- `sqs-credit-card-installments-hub` - Fila para parcelas de cartão
- `sqs-annual-adjustment-hub` - Fila para ajustes anuais
- `sqs-enrollment-integration-ie` - Fila para integração de matrículas
