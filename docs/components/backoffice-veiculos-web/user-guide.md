# Guia do Usuário - Backoffice Veículos Web

## Visão Geral

O Backoffice Veículos Web é uma aplicação frontend para gerenciamento de veículos, permitindo cadastro, consulta, edição e exclusão de informações de veículos através de uma interface web intuitiva.

## Como Acessar

1. Abra seu navegador web
2. Acesse a URL da aplicação (fornecida pelo administrador)
3. Faça login com suas credenciais

## Funcionalidades Principais

### 1. Listagem de Veículos
- Visualize todos os veículos cadastrados em uma tabela
- Filtre veículos por marca, modelo, ano ou placa
- Ordene os resultados por diferentes campos
- Navegue entre páginas de resultados

### 2. Cadastro de Veículos
- Adicione novos veículos ao sistema
- Preencha informações como:
  - Placa
  - Marca
  - Modelo
  - Ano de fabricação
  - Cor
  - Quilometragem
  - Status

### 3. Edição de Veículos
- Atualize informações de veículos existentes
- Modifique dados cadastrais
- Altere status do veículo

### 4. Exclusão de Veículos
- Remove veículos do sistema
- Confirmação antes da exclusão

### 5. Busca e Filtros
- Pesquisa rápida por placa ou modelo
- Filtros avançados por múltiplos critérios
- Exportação de dados filtrados

## Guia Passo a Passo

### Cadastrar um Novo Veículo

1. Na página inicial, clique no botão **"Novo Veículo"** ou **"+"**
2. Preencha o formulário com os dados do veículo:
   - **Placa**: Digite a placa no formato ABC-1234
   - **Marca**: Selecione a marca do veículo
   - **Modelo**: Informe o modelo
   - **Ano**: Selecione o ano de fabricação
   - **Cor**: Escolha a cor
   - **Quilometragem**: Digite a quilometragem atual
   - **Status**: Selecione o status (Disponível, Em manutenção, Vendido, etc.)
3. Clique em **"Salvar"**
4. Uma mensagem de confirmação será exibida

### Consultar Veículos

1. Na página inicial, você verá a lista de todos os veículos
2. Use a barra de pesquisa para encontrar um veículo específico
3. Utilize os filtros laterais para refinar sua busca:
   - Selecione a marca desejada
   - Escolha o ano
   - Filtre por status
4. Os resultados são atualizados automaticamente

### Editar um Veículo

1. Na lista de veículos, localize o veículo que deseja editar
2. Clique no ícone de **"Editar"** (lápis) na linha do veículo
3. Modifique os campos necessários no formulário
4. Clique em **"Salvar"** para confirmar as alterações
5. Clique em **"Cancelar"** para descartar as mudanças

### Excluir um Veículo

1. Na lista de veículos, localize o veículo que deseja excluir
2. Clique no ícone de **"Excluir"** (lixeira) na linha do veículo
3. Confirme a exclusão na caixa de diálogo
4. O veículo será removido da lista

### Exportar Dados

1. Aplique os filtros desejados na lista de veículos
2. Clique no botão **"Exportar"**
3. Escolha o formato (CSV, Excel, PDF)
4. O arquivo será baixado automaticamente

## Exemplos Visuais

### Tela Principal
```
┌─────────────────────────────────────────────────────────┐
│ Backoffice Veículos                    [Novo Veículo]   │
├─────────────────────────────────────────────────────────┤
│ 🔍 Pesquisar: [_________________]  [Filtros ▼]          │
├─────────────────────────────────────────────────────────┤
│ Placa    │ Marca  │ Modelo    │ Ano  │ Status │ Ações  │
├──────────┼────────┼───────────┼──────┼────────┼────────┤
│ ABC-1234 │ Fiat   │ Uno       │ 2020 │ Disp.  │ ✏️ 🗑️  │
│ DEF-5678 │ VW     │ Gol       │ 2019 │ Manutenção│ ✏️ 🗑️│
│ GHI-9012 │ Ford   │ Fiesta    │ 2021 │ Disp.  │ ✏️ 🗑️  │
└─────────────────────────────────────────────────────────┘
```

### Formulário de Cadastro
```
┌─────────────────────────────────────┐
│ Cadastrar Novo Veículo              │
├─────────────────────────────────────┤
│ Placa: [___________]                │
│ Marca: [▼__________]                │
│ Modelo: [___________]               │
│ Ano: [▼____]                        │
│ Cor: [▼__________]                  │
│ Quilometragem: [___________] km     │
│ Status: [▼__________]               │
│                                     │
│        [Cancelar]  [Salvar]         │
└─────────────────────────────────────┘
```

## Solução de Problemas Comuns

### Problema: Não consigo fazer login
**Solução:**
- Verifique se suas credenciais estão corretas
- Confirme se o CAPS LOCK não está ativado
- Entre em contato com o administrador para resetar sua senha

### Problema: A lista de veículos não carrega
**Solução:**
- Verifique sua conexão com a internet
- Atualize a página (F5 ou Ctrl+R)
- Limpe o cache do navegador
- Tente acessar em modo anônimo/privado

### Problema: Não consigo salvar um veículo
**Solução:**
- Verifique se todos os campos obrigatórios (marcados com *) estão preenchidos
- Confirme se a placa está no formato correto (ABC-1234)
- Verifique se a placa já não está cadastrada no sistema
- Tente novamente após alguns segundos

### Problema: O filtro não está funcionando
**Solução:**
- Limpe todos os filtros e tente novamente
- Verifique se há dados que correspondem aos filtros aplicados
- Atualize a página

### Problema: Não consigo exportar dados
**Solução:**
- Verifique se há veículos na lista para exportar
- Desabilite bloqueadores de pop-up no navegador
- Tente usar outro navegador
- Verifique se há espaço disponível no seu computador

### Problema: A aplicação está lenta
**Solução:**
- Feche abas desnecessárias do navegador
- Limpe o cache do navegador
- Verifique sua conexão com a internet
- Use filtros para reduzir a quantidade de dados exibidos

## Dicas de Uso

- **Atalhos de teclado**: Use `Ctrl+F` para busca rápida na página
- **Navegação**: Use `Tab` para navegar entre campos do formulário
- **Atualização**: Pressione `F5` para atualizar a lista de veículos
- **Seleção múltipla**: Use `Ctrl+Click` para selecionar múltiplos veículos (quando disponível)

## Suporte

Em caso de dúvidas ou problemas não resolvidos:
- Entre em contato com o suporte técnico
- Envie um email para: suporte@exemplo.com
- Abra um chamado no sistema de tickets
- Consulte a documentação técnica completa

## Requisitos do Sistema

- **Navegadores suportados**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Resolução mínima**: 1280x720
- **Conexão**: Banda larga recomendada
