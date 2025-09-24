# Vitrine de Veículos - BFF

Backend for Frontend que otimiza dados da vitrine para o frontend web.

## Status do Projeto

- **Build Status**: [![Build Status](https://img.shields.io/github/actions/workflow/status/emingues-xx/vitrine-veiculos-bff/ci.yml?branch=main)](https://github.com/emingues-xx/vitrine-veiculos-bff/actions)
- **Versão**: [![Version](https://img.shields.io/github/v/release/emingues-xx/vitrine-veiculos-bff)](https://github.com/emingues-xx/vitrine-veiculos-bff/releases)
- **Licença**: [![License](https://img.shields.io/github/license/emingues-xx/vitrine-veiculos-bff)](https://github.com/emingues-xx/vitrine-veiculos-bff/blob/main/LICENSE)
- **Tecnologias**: Node.js 18, Express 4, TypeScript 5

## Descrição

Camada intermediária entre o frontend da vitrine e a API core, responsável por agregar, transformar e otimizar dados específicos para as necessidades da interface web. Implementa cache inteligente e reduz o número de requisições do frontend.

## Características Principais

- 🔄 **Agregação de Dados**: Combina múltiplas APIs em uma única resposta
- ⚡ **Cache Otimizado**: Redis com TTL específico por endpoint
- 📱 **Payload Otimizado**: Respostas customizadas para cada tela
- 🛡️ **Rate Limiting**: Proteção específica por tipo de cliente
- 📊 **Transformação**: Formatação de dados para UI

## Tecnologias

- **Runtime**: Node.js 18 LTS
- **Framework**: Express 4
- **Linguagem**: TypeScript 5
- **Cache**: Redis 7
- **HTTP Client**: Axios
- **Validation**: Joi
- **Testing**: Jest + Supertest

## Instalação

```bash
# Clone e instalação
git clone https://github.com/emingues-xx/vitrine-veiculos-bff.git
cd vitrine-veiculos-bff
npm install

# Configuração
cp .env.example .env
# Edite .env com suas configurações

# Desenvolvimento
npm run dev
```

## Principais Endpoints

### Frontend Otimizado
```http
GET /api/home/data              # Dados completos da homepage
GET /api/search/filters         # Filtros agregados para busca
GET /api/vehicle/:id/details    # Detalhes otimizados do veículo
GET /api/listings/optimized     # Listagem otimizada com metadados
```

## Links Relacionados

- 🏗️ [Arquitetura](architecture.md)
- 🔧 [Setup](setup.md)
- 📚 [Repositório GitHub](https://github.com/emingues-xx/vitrine-veiculos-bff)