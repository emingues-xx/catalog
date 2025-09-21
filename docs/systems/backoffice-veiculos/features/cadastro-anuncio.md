# Feature: Cadastro de Anúncios

Sistema de cadastro e gestão de anúncios de veículos para vendedores e operadores.

## Descrição

Funcionalidade que permite o cadastro completo de veículos na plataforma, incluindo informações técnicas, fotos, preço e detalhes de contato, com validações e aprovação automática ou manual.

## Fluxo de Cadastro

### 1. Informações Básicas
- **Tipo de veículo**: Carro, Moto, Caminhão, etc.
- **Marca e Modelo**: Seleção em cascata
- **Ano do veículo**: Ano de fabricação e modelo
- **Versão**: Versões específicas do modelo

### 2. Características Técnicas
- **Motor**: Cilindrada, potência
- **Combustível**: Flex, Gasolina, Diesel, etc.
- **Transmissão**: Manual, Automática, CVT
- **Direção**: Mecânica, Hidráulica, Elétrica
- **Quilometragem**: KM atual do veículo

### 3. Informações Comerciais
- **Preço**: Valor de venda
- **Condições**: À vista, financiado, troca
- **IPVA**: Situação do pagamento
- **Documentação**: Situação legal do veículo
- **Aceita troca**: Sim/Não

### 4. Localização
- **CEP**: Código postal
- **Estado e Cidade**: Preenchimento automático
- **Bairro**: Localização específica
- **Endereço**: Opcional para contato

### 5. Galeria de Fotos
- **Upload múltiplo**: Até 20 fotos
- **Formatos aceitos**: JPG, PNG, WEBP
- **Tamanho máximo**: 5MB por foto
- **Redimensionamento automático**: Para otimização

### 6. Descrição e Opcionais
- **Descrição**: Texto livre sobre o veículo
- **Opcionais**: Ar condicionado, som, bancos de couro, etc.
- **Observações**: Informações adicionais

## Validações

### Campos Obrigatórios
- Marca, modelo, ano, preço
- Pelo menos 3 fotos
- Quilometragem
- Localização (CEP)
- Telefone para contato

### Validações de Negócio
- **Ano**: Não pode ser superior ao ano atual + 1
- **Preço**: Deve ser maior que R$ 1.000
- **KM**: Coerente com o ano do veículo
- **Fotos**: Qualidade mínima exigida

### Validações Técnicas
- **Duplicação**: Verificação de anúncios similares
- **Marca/Modelo**: Validação contra base de dados FIPE
- **CEP**: Validação de existência
- **Telefone**: Formato válido

## Processo de Aprovação

### Aprovação Automática
Anúncios que atendem todos os critérios:
- ✅ Todas as validações passaram
- ✅ Vendedor com boa reputação
- ✅ Fotos de qualidade adequada
- ✅ Preço dentro da faixa FIPE

### Aprovação Manual
Anúncios que precisam de revisão:
- ⚠️ Preço muito abaixo/acima da tabela FIPE
- ⚠️ Vendedor novo na plataforma
- ⚠️ Fotos de baixa qualidade
- ⚠️ Descrição com possíveis problemas

### Processo de Revisão
1. **Fila de moderação**: Anúncios pendentes
2. **Análise**: Operador revisa informações
3. **Decisão**: Aprovação, correção ou rejeição
4. **Notificação**: Vendedor informado do status

## Interface de Usuário

### Wizard de Cadastro
Interface step-by-step para facilitar o processo:
- Progress bar mostrando etapas
- Salvamento automático do progresso
- Validação em tempo real
- Preview do anúncio antes da publicação

### Upload de Fotos
- Drag & drop interface
- Preview instantâneo
- Crop e rotação de imagens
- Indicação de foto principal

## Integrações

### Tabela FIPE
- **Consulta de preços**: Referência para validação
- **Sugestão de preço**: Baseado no ano e modelo
- **Atualização**: Dados atualizados mensalmente

### CEP API
- **Preenchimento automático**: Endereço por CEP
- **Validação**: Verificação de CEP válido

### Sistema de Notificações
- **E-mail**: Confirmação de cadastro
- **SMS**: Código de verificação (opcional)
- **Push**: Status de aprovação

## Métricas e Analytics

### Métricas de Conversão
- Taxa de conclusão do cadastro
- Tempo médio de preenchimento
- Abandono por etapa
- Taxa de aprovação automática vs manual

### Qualidade dos Dados
- Anúncios com informações completas
- Qualidade média das fotos
- Precisão das informações técnicas

## Melhorias Futuras

- [ ] Reconhecimento automático de placas em fotos
- [ ] Sugestão automática de opcionais por foto
- [ ] Integração com sistemas de vistoria
- [ ] Cadastro via mobile com geolocalização
- [ ] Template de anúncios para vendedores recorrentes