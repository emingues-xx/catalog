# Sistema Vitrine de Veículos

A **Vitrine de Veículos** é o sistema responsável pela experiência pública dos usuários, oferecendo catálogo, busca e exibição de veículos disponíveis para venda.

## Visão Geral

O sistema permite que usuários naveguem, pesquisem e visualizem detalhes dos veículos disponíveis em nossa plataforma de forma intuitiva e eficiente.

## Componentes

### Frontend (vitrine-veiculos-web)
- **Tecnologia**: React/Next.js
- **Responsabilidade**: Interface de usuário da vitrine pública
- **Funcionalidades**:
  - Listagem de veículos
  - Filtros de busca
  - Detalhes do veículo
  - Galeria de imagens 

### API (vitrine-veiculos-api)  
- **Tecnologia**: Node.js
- **Responsabilidade**: API para consultas públicas
- **Funcionalidades**:
  - Endpoints de listagem
  - Sistema de filtros
  - Busca por critérios
  - Cache de dados   

### BFF (vitrine-veiculos-bff)
- **Tecnologia**: Node.js  
- **Responsabilidade**: Backend for Frontend otimizado
- **Funcionalidades**:
  - Agregação de dados
  - Otimização para frontend
  - Transformação de dados

## Funcionalidades

### Catálogo de Veículos
Exibição organizada dos veículos disponíveis com informações essenciais como preço, marca, modelo, ano e localização.

### Sistema de Busca e Filtros
Interface intuitiva para filtrar veículos por:
- Marca e modelo
- Faixa de preço
- Ano de fabricação
- Tipo de combustível
- Localização

### Detalhes do Veículo
Página dedicada com informações completas:
- Especificações técnicas
- Galeria de fotos
- Histórico do veículo
- Informações do vendedor

## Arquitetura

O sistema segue uma arquitetura de três camadas:

1. **Frontend**: Interface React otimizada para performance
2. **BFF**: Camada de agregação e otimização 
3. **API**: Serviços de dados e regras de negócio

## Time Responsável

**Squad Vitrine**: Responsável pelo desenvolvimento e manutenção do sistema de vitrine pública.