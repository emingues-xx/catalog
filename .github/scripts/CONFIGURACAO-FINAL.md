# ✅ Configuração Final - Outline Sync

## 🔗 Sua Instância do Outline

**URL da Instância**: https://outline-production-cebc.up.railway.app  
**Token de API**: ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A

## 🔐 Secrets do GitHub

Configure os seguintes secrets no seu repositório GitHub:

### 1. OUTLINE_API_URL
```
Name: OUTLINE_API_URL
Value: https://outline-production-cebc.up.railway.app
```

### 2. OUTLINE_API_TOKEN
```
Name: OUTLINE_API_TOKEN
Value: ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A
```

## ✅ Validação Realizada

- ✅ **Conectividade**: API acessível e funcionando
- ✅ **Autenticação**: Token válido e com permissões adequadas
- ✅ **Endpoints**: Corrigidos (removido prefixo `/api`)
- ✅ **Arquivos**: 30 arquivos .md encontrados no diretório `docs/`
- ✅ **Mapeamento**: Arquivo `outline-mapping.yaml` configurado
- ✅ **Scripts**: Atualizados com nova URL e token

## 🚀 Como Usar

### 1. Teste Local (PowerShell)
```powershell
# Testar conectividade
.\github\scripts\test-connectivity.ps1

# Validar configuração
powershell -ExecutionPolicy Bypass -File .github\scripts\test-sync.ps1
```

### 2. Sincronização via GitHub Actions
- Faça push de qualquer alteração nos arquivos `.md` do diretório `docs/`
- O GitHub Action executará automaticamente a sincronização
- Verifique os logs em **Actions** > **Sync Documentation to Outline**

### 3. Sincronização Manual (se tiver Python)
```bash
# Definir variáveis de ambiente
export OUTLINE_API_URL="https://outline-production-cebc.up.railway.app"
export OUTLINE_API_TOKEN="ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"

# Executar sincronização
python .github/scripts/sync_working.py
```

## 📋 Estrutura de Documentos

A sincronização criará a seguinte estrutura hierárquica no Outline:

```
E-commerce de Veículos - Documentação
├── Arquitetura
│   ├── Sobre ADRs
│   └── ADRs
├── Sistemas
│   ├── Vitrine de Veículos
│   │   ├── Features
│   │   │   └── Busca de Veículos
│   │   └── Arquitetura
│   └── Backoffice de Veículos
│       ├── Features
│       │   └── Cadastro de Anúncios
│       └── Arquitetura
├── Componentes
│   ├── Vitrine Web
│   │   ├── Arquitetura
│   │   └── Setup
│   ├── Vitrine API
│   │   └── API Reference
│   ├── Vitrine BFF
│   ├── Backoffice Web
│   ├── Backoffice API
│   ├── Backoffice BFF
│   └── Pipelines E-commerce
│       ├── Automação - Pipelines
│       └── Workflows - Pipelines
└── Guias
    ├── Contributing
    └── Guia de Contribuição
```

## 🔧 Troubleshooting

### Erro 404 (Not Found)
- Verifique se a URL está correta: `https://outline-production-cebc.up.railway.app`
- **NÃO** inclua `/api` no final da URL

### Erro 401 (Unauthorized)
- Verifique se o token está correto: `ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A`
- Confirme se o token tem as permissões necessárias

### Erro de Conectividade
- Execute o teste: `.\github\scripts\test-connectivity.ps1`
- Verifique se a instância do Outline está acessível

## 📞 Suporte

Se encontrar problemas:
1. Execute os scripts de teste
2. Verifique os logs do GitHub Actions
3. Confirme se os secrets estão configurados corretamente
4. Verifique se a instância do Outline está funcionando

---

**✅ Configuração concluída com sucesso!**
