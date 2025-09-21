# Exemplo de Configuração - Secrets do GitHub

## 🔐 Configuração dos Secrets

Para configurar os secrets necessários no GitHub:

### 1. Acesse as Configurações do Repositório

1. Vá para o seu repositório no GitHub
2. Clique em **Settings** (Configurações)
3. No menu lateral, clique em **Secrets and variables** > **Actions**

### 2. Adicione os Secrets

Clique em **New repository secret** e adicione:

#### OUTLINE_API_URL
```
Name: OUTLINE_API_URL
Value: https://your-outline-instance.com/api
```

**Exemplo**: `https://docs.minhaempresa.com/api`

#### OUTLINE_API_TOKEN
```
Name: OUTLINE_API_TOKEN
Value: your-api-token-here
```

**Como obter o token**:
1. Acesse sua instância do Outline
2. Vá para **Settings** > **API Tokens**
3. Clique em **Create Token**
4. Dê um nome descritivo (ex: "GitHub Sync")
5. Selecione as permissões necessárias:
   - ✅ Read documents
   - ✅ Write documents
   - ✅ Read collections
   - ✅ Write collections
6. Copie o token gerado

### 3. Verificar Configuração

Após adicionar os secrets, você pode verificar se estão configurados corretamente:

1. Volte para **Secrets and variables** > **Actions**
2. Você deve ver os dois secrets listados:
   - `OUTLINE_API_URL`
   - `OUTLINE_API_TOKEN`

## 🧪 Teste da Configuração

Para testar se a configuração está funcionando:

1. Faça uma pequena alteração em qualquer arquivo `.md` no diretório `docs/`
2. Crie um PR e faça merge para `main`
3. Vá para **Actions** no GitHub e verifique se o workflow foi executado
4. Se tudo estiver correto, você verá:
   - ✅ Workflow executado com sucesso
   - 📝 Documentos sincronizados no Outline

## ⚠️ Troubleshooting

### Erro 401 (Unauthorized)
- Verifique se o `OUTLINE_API_TOKEN` está correto
- Confirme se o token tem as permissões necessárias

### Erro 404 (Not Found)
- Verifique se o `OUTLINE_API_URL` está correto
- Confirme se a instância do Outline está acessível

### Erro de Conexão
- Verifique se a URL da API está acessível
- Confirme se não há firewall bloqueando a conexão

## 📋 Checklist de Configuração

- [ ] Instância do Outline configurada e acessível
- [ ] Token de API criado com permissões adequadas
- [ ] Secret `OUTLINE_API_URL` configurado no GitHub
- [ ] Secret `OUTLINE_API_TOKEN` configurado no GitHub
- [ ] Arquivo `outline-mapping.yaml` configurado com IDs corretos
- [ ] Teste realizado com sucesso

## 🔄 Próximos Passos

Após configurar os secrets:

1. **Personalize o mapeamento**: Edite `outline-mapping.yaml` conforme suas necessidades
2. **Teste a sincronização**: Faça uma alteração na documentação e verifique o resultado
3. **Monitore os logs**: Acompanhe a execução do workflow em **Actions**
4. **Ajuste conforme necessário**: Modifique tags, títulos e descrições conforme sua preferência
