# Configuração do Outline para Sincronização

## 🔗 Informações da Instância

**URL da Instância**: https://outline-production-cebc.up.railway.app  
**Coleção Principal**: d236ae05-812e-426a-a125-75653888903e  
**URL da Coleção**: https://outline-production-cebc.up.railway.app/collection/d236ae05-812e-426a-a125-75653888903e/recent

## 🔐 Secrets Necessários no GitHub

Configure os seguintes secrets no seu repositório GitHub:

### 1. OUTLINE_API_TOKEN
```
Name: OUTLINE_API_TOKEN
Value: ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A
```

### 2. OUTLINE_API_URL
```
Name: OUTLINE_API_URL
Value: https://outline-production-cebc.up.railway.app
```

**Nota**: A URL da API é: `https://outline-production-cebc.up.railway.app` (os endpoints usam o prefixo `/api`)

## 🎯 Como Obter o Token de API

1. Acesse sua instância do Outline: https://outline-production-cebc.up.railway.app
2. Faça login com sua conta
3. Vá para **Settings** (Configurações)
4. Clique em **API Tokens**
5. Clique em **Create Token**
6. Configure o token:
   - **Name**: `GitHub Sync`
   - **Permissions**:
     - ✅ Read documents
     - ✅ Write documents
     - ✅ Read collections
     - ✅ Write collections
7. Clique em **Create Token**
8. Copie o token gerado e cole no secret `OUTLINE_API_TOKEN`

## ✅ Verificação da Configuração

Após configurar os secrets, você pode testar:

1. **Teste Manual**: Execute o script localmente:
   ```bash
   cd .github/scripts
   python sync_to_outline.py
   ```

2. **Teste via GitHub Actions**: 
   - Faça uma pequena alteração em qualquer arquivo `.md` no diretório `docs/`
   - Crie um PR e faça merge para `main`
   - Verifique a execução em **Actions** > **Sync Documentation to Outline**

## 📋 Checklist de Configuração

- [ ] Instância do Outline acessível
- [ ] Token de API criado com permissões adequadas
- [ ] Secret `OUTLINE_API_URL` configurado: `https://outline-production-cebc.up.railway.app`
- [ ] Secret `OUTLINE_API_TOKEN` configurado com o token real
- [ ] Arquivo `outline-mapping.yaml` configurado com ID correto: `d236ae05-812e-426a-a125-75653888903e`
- [ ] Teste realizado com sucesso

## 🚨 Troubleshooting

### Erro 401 (Unauthorized)
- Verifique se o token está correto
- Confirme se o token tem as permissões necessárias

### Erro 404 (Collection Not Found)
- Verifique se o ID da coleção `docs-KS6TJUuX5p` está correto
- Confirme se você tem acesso à coleção

### Erro de Conexão
- Verifique se a URL da API está acessível
- Teste a conectividade: `curl https://outline-production-47e1.up.railway.app/api`

## 📊 Estrutura dos Documentos no Outline

Os documentos serão organizados em uma estrutura hierárquica:

### Coleção Pai
- **ID**: `fdc96e70-5b1d-4de5-abca-09fc9749b543`
- **Nome**: Docs
- **URL**: https://outline-production-47e1.up.railway.app/collection/fdc96e70-5b1d-4de5-abca-09fc9749b543

### Sub-coleções (criadas automaticamente)
- **Documentação Principal** (`main-collection`)
- **Arquitetura** (`architecture-collection`) 
- **Sistemas** (`systems-collection`)
- **Componentes** (`components-collection`)
- **Guias** (`guides-collection`)

### Características dos Documentos
- **Títulos personalizados** baseados no mapeamento
- **Tags organizadas** por categoria (system, component, architecture, etc.)
- **Metadados enriquecidos** com links para o repositório
- **Estrutura hierárquica** mantida através das sub-coleções

## 🔄 Próximos Passos

1. Configure os secrets conforme instruções acima
2. Teste a sincronização
3. Monitore os logs do GitHub Actions
4. Ajuste tags e títulos conforme necessário no `outline-mapping.yaml`
