# 🔧 Troubleshooting - Sincronização com Outline

## ❌ Erro: "Resource not found" (404)

### Possíveis Causas:

1. **URL da API Incorreta**
2. **Token de API Inválido ou Expirado**
3. **ID da Coleção Incorreto**
4. **Permissões Insuficientes**

## 🔍 Passos para Diagnóstico

### 1. Verificar a URL da API

A URL deve ser:
```
https://outline-production-cebc.up.railway.app
```

**❌ Incorreto:**
- `https://outline-production-cebc.up.railway.app/api` (com /api)
- `https://outline-production-cebc.up.railway.app/` (com barra final)

**✅ Correto:**
- `https://outline-production-cebc.up.railway.app` (sem prefixo /api)

### 2. Testar Conectividade

Execute o script de teste:

```bash
# Configure o token
export OUTLINE_API_TOKEN="seu-token-aqui"

# Execute o teste
python .github/scripts/test-outline-api.py
```

### 3. Verificar o Token de API

1. Acesse: https://outline-production-cebc.up.railway.app
2. Vá para **Settings** > **API Tokens**
3. Verifique se o token existe e está ativo
4. Confirme as permissões:
   - ✅ Read documents
   - ✅ Write documents
   - ✅ Read collections
   - ✅ Write collections

### 4. Verificar o ID da Coleção

Execute o script de validação:

```bash
python .github/scripts/validate-outline.py
```

Isso listará todas as coleções disponíveis e mostrará os IDs corretos.

## 🛠️ Soluções

### Solução 1: Corrigir a URL da API

No GitHub Secrets, configure:
```
OUTLINE_API_URL: https://outline-production-cebc.up.railway.app
```

### Solução 2: Atualizar o Token

1. Gere um novo token no Outline
2. Atualize o secret `OUTLINE_API_TOKEN` no GitHub
3. Teste novamente

### Solução 3: Corrigir o ID da Coleção

Se a coleção `docs-KS6TJUuX5p` não existir:

1. **Opção A**: Use um ID de coleção existente
2. **Opção B**: Crie uma nova coleção no Outline
3. **Opção C**: Use a coleção raiz (deixe vazio)

### Solução 4: Usar Coleção Raiz

Se você quiser usar a coleção raiz, modifique o `outline-mapping.yaml`:

```yaml
config:
  default_collection_id: ""  # Coleção raiz
```

## 🧪 Testes Manuais

### Teste 1: Conectividade Básica

```bash
curl -H "Authorization: Bearer SEU_TOKEN" \
     https://outline-production-47e1.up.railway.app/api/auth.info
```

### Teste 2: Listar Coleções

```bash
curl -H "Authorization: Bearer SEU_TOKEN" \
     https://outline-production-47e1.up.railway.app/api/collections.list
```

### Teste 3: Buscar Coleção Específica

```bash
curl -H "Authorization: Bearer SEU_TOKEN" \
     "https://outline-production-47e1.up.railway.app/api/collections.list?query=docs"
```

## 📋 Checklist de Verificação

- [ ] URL da API está correta (sem /api no final)
- [ ] Token de API está válido e ativo
- [ ] Token tem permissões de leitura e escrita
- [ ] ID da coleção existe no Outline
- [ ] Instância do Outline está acessível
- [ ] Secrets estão configurados no GitHub

## 🆘 Se Nada Funcionar

1. **Verifique os logs do GitHub Actions** para mais detalhes
2. **Teste localmente** com os scripts fornecidos
3. **Verifique se a instância do Outline está funcionando**
4. **Entre em contato com o administrador do Outline**

## 📞 Comandos de Emergência

### Reset Completo

```bash
# 1. Remover secrets
# 2. Gerar novo token
# 3. Configurar secrets novamente
# 4. Testar com script de validação
```

### Usar Coleção Raiz

```bash
# Modificar outline-mapping.yaml
# Alterar default_collection_id para ""
# Fazer commit e testar
```
