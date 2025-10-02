# Guia do Usuário - Backoffice Veículos Web

## Visão Geral

O Backoffice Veículos Web é uma aplicação frontend para gerenciamento de veículos. Esta interface permite que usuários administrativos realizem operações de cadastro, consulta, edição e exclusão de veículos de forma intuitiva.

## Como Acessar

1. Acesse a URL da aplicação através do seu navegador
2. Faça login com suas credenciais de acesso
3. Após autenticação, você será direcionado para o painel principal

## Funcionalidades Principais

### 1. Dashboard
- Visualização de estatísticas gerais de veículos
- Resumo de veículos ativos/inativos
- Indicadores de performance

### 2. Listagem de Veículos
- Visualize todos os veículos cadastrados
- Utilize filtros para busca avançada (placa, modelo, marca, ano)
- Ordene resultados por diferentes critérios
- Paginação para navegação eficiente

### 3. Cadastro de Veículos
- Adicione novos veículos ao sistema
- Preencha informações obrigatórias: placa, modelo, marca, ano
- Adicione informações complementares: cor, quilometragem, status

### 4. Edição de Veículos
- Atualize dados de veículos existentes
- Modifique status (ativo/inativo)
- Altere informações cadastrais

### 5. Exclusão de Veículos
- Remova veículos do sistema
- Confirmação de exclusão para evitar ações acidentais

## Guia Passo a Passo

### Cadastrar um Novo Veículo

1. No menu lateral, clique em **"Veículos"**
2. Clique no botão **"+ Novo Veículo"** no canto superior direito
3. Preencha o formulário com as informações:
   - **Placa** (obrigatório): ex: ABC-1234
   - **Marca** (obrigatório): ex: Toyota
   - **Modelo** (obrigatório): ex: Corolla
   - **Ano** (obrigatório): ex: 2023
   - **Cor**: ex: Preto
   - **Quilometragem**: ex: 15000
   - **Status**: Ativo/Inativo
4. Clique em **"Salvar"**
5. Verifique a mensagem de confirmação

### Buscar um Veículo

1. Acesse a página **"Veículos"**
2. Utilize a barra de busca no topo da lista
3. Digite placa, modelo ou marca
4. Ou utilize os filtros avançados:
   - Selecione marca no dropdown
   - Defina intervalo de ano
   - Escolha status (ativo/inativo)
5. Clique em **"Filtrar"**

### Editar um Veículo

1. Na listagem, localize o veículo desejado
2. Clique no ícone de **lápis/edição** na linha do veículo
3. Modifique os campos necessários
4. Clique em **"Atualizar"**
5. Confirme a atualização

### Excluir um Veículo

1. Na listagem, localize o veículo
2. Clique no ícone de **lixeira/exclusão**
3. Confirme a exclusão no modal de confirmação
4. O veículo será removido da listagem

## Exemplos Visuais

### Interface de Listagem
```
┌─────────────────────────────────────────────────────┐
│  Veículos                        [+ Novo Veículo]   │
├─────────────────────────────────────────────────────┤
│  Buscar: [___________]  Filtros: [Marca▼] [Ano▼]   │
├──────┬────────┬────────┬──────┬────────┬───────────┤
│ Placa│ Marca  │ Modelo │ Ano  │ Status │ Ações     │
├──────┼────────┼────────┼──────┼────────┼───────────┤
│ABC123│ Toyota │ Corolla│ 2023 │ Ativo  │ [✏️] [🗑️] │
│DEF456│ Honda  │ Civic  │ 2022 │ Ativo  │ [✏️] [🗑️] │
└──────┴────────┴────────┴──────┴────────┴───────────┘
```

### Formulário de Cadastro
```
┌─────────────────────────────────────┐
│  Novo Veículo                       │
├─────────────────────────────────────┤
│  Placa *:     [_____________]       │
│  Marca *:     [_____________]       │
│  Modelo *:    [_____________]       │
│  Ano *:       [_____________]       │
│  Cor:         [_____________]       │
│  Km:          [_____________]       │
│  Status:      (•) Ativo  ( ) Inativo│
│                                     │
│         [Cancelar]  [Salvar]        │
└─────────────────────────────────────┘
```

## Solução de Problemas Comuns

### Não consigo fazer login
- **Problema**: Credenciais inválidas
- **Solução**: Verifique usuário e senha. Contate o administrador para resetar senha se necessário

### Veículo não aparece na listagem
- **Problema**: Filtros ativos podem estar ocultando o resultado
- **Solução**: Clique em "Limpar Filtros" e tente novamente

### Erro ao salvar veículo
- **Problema**: Campos obrigatórios não preenchidos ou formato inválido
- **Solução**: Verifique se todos os campos com (*) estão preenchidos corretamente. Placa deve seguir padrão brasileiro (ABC-1234)

### Página carrega lentamente
- **Problema**: Grande volume de dados ou conexão lenta
- **Solução**: Utilize filtros para reduzir o volume de dados carregados. Verifique sua conexão de internet

### Botões não respondem
- **Problema**: Sessão expirada ou erro de carregamento
- **Solução**: Recarregue a página (F5) ou faça login novamente

### Mensagem "Erro ao comunicar com servidor"
- **Problema**: API indisponível ou problemas de rede
- **Solução**: Aguarde alguns minutos e tente novamente. Se persistir, contate o suporte técnico

## Dicas de Uso

- **Atalhos de teclado**: Use Tab para navegar entre campos dos formulários
- **Exportação**: Utilize o botão "Exportar" para baixar a lista de veículos em Excel/CSV
- **Atualizações**: A listagem é atualizada automaticamente a cada ação
- **Validações**: O sistema valida automaticamente formatos de placa e dados obrigatórios

## Suporte

Para suporte técnico ou dúvidas adicionais:
- Abra uma issue no repositório: https://github.com/emingues-xx/backoffice-veiculos-web/issues
- Contate a equipe de desenvolvimento
- Consulte a documentação técnica para desenvolvedores
