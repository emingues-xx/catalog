# Sincronização com Backstage TechDocs

Este diretório contém scripts para sincronizar a documentação dos componentes com o Backstage TechDocs.

## 📋 Problema Resolvido

**❌ Situação anterior:**
- Nem todas as docs estavam no TechDocs (Backstage)
- Componentes sem documentação no Backstage
- Exemplo: `backoffice-veiculos-api` tem docs em `docs\components\backoffice-veiculos-api\` mas não estava no Backstage

**✅ Solução implementada:**
- Scripts para sincronizar automaticamente todos os componentes com documentação
- Integração com Backstage API
- Criação automática de entidades TechDocs

## 🚀 Como Usar

### 1. Configuração Inicial

```bash
# Configurar variáveis de ambiente
export BACKSTAGE_URL="http://localhost:7007"
export BACKSTAGE_TOKEN="seu-token-aqui"
```

### 2. Execução via PowerShell (Recomendado)

```powershell
# Executar sincronização
.\sync-backstage.ps1

# Ou com parâmetros customizados
.\sync-backstage.ps1 -BackstageUrl "https://backstage.company.com" -BackstageToken "seu-token"
```

### 3. Execução via Python

```bash
# Executar diretamente
python .github/scripts/sync_to_backstage.py
```

## 📁 Estrutura dos Arquivos

```
.github/scripts/
├── sync_to_backstage.py      # Script principal Python
├── sync-backstage.ps1        # Script PowerShell wrapper
├── backstage-config.yaml     # Configuração dos componentes
└── README-Backstage.md       # Este arquivo
```

## 🔧 Componentes Sincronizados

O script sincroniza automaticamente todos os componentes que têm documentação:

### ✅ Componentes de Vitrine
- `vitrine-veiculos-web` - Componente web da vitrine
- `vitrine-veiculos-api` - API da vitrine
- `vitrine-veiculos-bff` - BFF da vitrine

### ✅ Componentes de Backoffice
- `backoffice-veiculos-web` - Componente web do backoffice
- `backoffice-veiculos-api` - API do backoffice
- `backoffice-veiculos-bff` - BFF do backoffice

### ✅ Componentes de Infraestrutura
- `ecommerce-veiculos-pipelines` - Pipelines de CI/CD

## 📊 Resultados

Após a execução, o script gera:

1. **Log detalhado** no console
2. **Arquivo de resultados** (`backstage-sync-results.json`)
3. **Status de cada componente** (sucesso/falha)

### Exemplo de Saída

```
🚀 Sincronizando documentação com Backstage TechDocs...
============================================================
📋 Configurações:
   Backstage URL: http://localhost:7007
   Docs Directory: docs/components
   Token: eyJhbGciO...

🔍 Verificando componentes com documentação...
   ✅ vitrine-veiculos-web - Tem documentação
   ✅ vitrine-veiculos-api - Tem documentação
   ✅ backoffice-veiculos-api - Tem documentação
   ...

📊 Componentes encontrados: 7

🚀 Executando sincronização...
✅ Entidade TechDocs criada para vitrine-veiculos-web
✅ Entidade TechDocs criada para vitrine-veiculos-api
✅ Entidade TechDocs criada para backoffice-veiculos-api
...

🎉 Sincronização concluída com sucesso!
```

## 🔍 Verificação

Após a sincronização, verifique:

1. **Backstage UI**: Acesse `http://localhost:7007` e confirme que os componentes aparecem
2. **Documentação**: Clique em cada componente e verifique se a documentação está sendo exibida
3. **Metadados**: Confirme que os metadados (owner, type, lifecycle) estão corretos

## ⚙️ Configuração Avançada

### Personalizar Componentes

Edite o arquivo `backstage-config.yaml` para:

- Alterar owners dos componentes
- Modificar tipos (frontend, backend, infrastructure)
- Ajustar lifecycle (production, development, deprecated)
- Adicionar tags personalizadas

### Adicionar Novos Componentes

1. Crie a documentação em `docs/components/novo-componente/`
2. Adicione um arquivo `index.md` com a documentação
3. Execute o script de sincronização
4. O componente será automaticamente detectado e sincronizado

## 🐛 Troubleshooting

### Erro de Conexão

```
❌ Erro ao conectar com Backstage: Connection refused
```

**Solução**: Verifique se o Backstage está rodando e a URL está correta.

### Erro de Autenticação

```
❌ Erro ao obter componentes: 401
```

**Solução**: Verifique se o token está correto e tem as permissões necessárias.

### Componente Não Aparece

```
⚠️ Componente existe mas não tem documentação
```

**Solução**: Verifique se o arquivo `index.md` existe no diretório do componente.

## 📚 Referências

- [Backstage TechDocs](https://backstage.io/docs/features/techdocs/)
- [Backstage API](https://backstage.io/docs/reference/)
- [TechDocs Configuration](https://backstage.io/docs/features/techdocs/configuration/)

## 🤝 Contribuição

Para adicionar novos componentes ou melhorar a sincronização:

1. Edite o arquivo `sync_to_backstage.py`
2. Teste com um componente específico
3. Execute o script completo
4. Verifique os resultados no Backstage
5. Faça commit das alterações
