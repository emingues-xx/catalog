# 🔄 Atualização do GitHub Actions - Deleção e Sincronização

## ✅ Status: Script Atualizado com Funcionalidade de Deleção

O script do GitHub Actions foi atualizado para deletar todos os documentos existentes antes de criar novos, garantindo uma sincronização limpa e evitando conflitos.

## 🔧 Mudanças Implementadas

### 1. **Nova Função de Deleção**

#### `_delete_all_documents()`
```python
def _delete_all_documents(self) -> bool:
    """Deleta todos os documentos da collection"""
    # Busca todos os documentos
    # Deleta cada documento individualmente
    # Retorna estatísticas de sucesso/erro
```

**Funcionalidades:**
- ✅ Busca todos os documentos existentes
- ✅ Deleta cada documento individualmente
- ✅ Exibe progresso detalhado
- ✅ Retorna estatísticas de sucesso/erro
- ✅ Tratamento de erros robusto

### 2. **Controle de Deleção**

#### Variável de Ambiente: `CLEAN_BEFORE_SYNC`
```python
clean_before_sync = os.getenv('CLEAN_BEFORE_SYNC', 'true').lower() == 'true'
```

**Valores:**
- **`true`** (padrão): Deleta todos os documentos antes de criar novos
- **`false`**: Mantém documentos existentes e apenas atualiza

### 3. **Fluxo Atualizado**

#### Processo de Sincronização:
1. **🔗 Teste de Conexão**: Verifica conectividade com Outline API
2. **🧹 Limpeza** (se `CLEAN_BEFORE_SYNC=true`): Deleta todos os documentos existentes
3. **📝 Criação**: Cria novos documentos seguindo a hierarquia
4. **📊 Relatório**: Exibe estatísticas finais

## 📋 Configuração do GitHub Actions

### Workflow Atualizado: `.github/workflows/sync-docs-to-outline.yml`

```yaml
env:
  OUTLINE_API_URL: ${{ secrets.OUTLINE_API_URL }}
  OUTLINE_API_TOKEN: ${{ secrets.OUTLINE_API_TOKEN }}
  GITHUB_REPOSITORY: ${{ github.repository }}
  GITHUB_SHA: ${{ github.sha }}
  CLEAN_BEFORE_SYNC: ${{ vars.CLEAN_BEFORE_SYNC || 'true' }}
```

### Variáveis de Ambiente:

| **Variável** | **Descrição** | **Padrão** |
|--------------|---------------|------------|
| `OUTLINE_API_URL` | URL da API do Outline | Obrigatório |
| `OUTLINE_API_TOKEN` | Token de autenticação | Obrigatório |
| `CLEAN_BEFORE_SYNC` | Deletar antes de sincronizar | `true` |

## 🎯 Benefícios da Atualização

### 1. **Sincronização Limpa**
- ✅ Remove documentos obsoletos
- ✅ Evita conflitos de títulos
- ✅ Garante hierarquia correta
- ✅ Elimina documentos duplicados

### 2. **Controle Flexível**
- ✅ Opção de manter documentos existentes
- ✅ Configurável via variável de ambiente
- ✅ Controle por repositório ou execução

### 3. **Logs Detalhados**
- ✅ Progresso da deleção
- ✅ Estatísticas de sucesso/erro
- ✅ Identificação de problemas
- ✅ Rastreabilidade completa

### 4. **Robustez**
- ✅ Tratamento de erros
- ✅ Continuação mesmo com falhas parciais
- ✅ Timeout configurado
- ✅ Validação de respostas

## 📊 Exemplo de Execução

### Logs de Saída:
```
🚀 Iniciando sincronização de documentos...
🔗 Testando conexão com Outline API...
✅ Conexão com API OK - 0 documentos encontrados

🧹 Limpando documentos existentes...
🗑️  Deletando todos os documentos existentes...
📋 Encontrados 5 documentos para deletar
   ✅ Deletado: Documento 1
   ✅ Deletado: Documento 2
   ✅ Deletado: Documento 3
   ✅ Deletado: Documento 4
   ✅ Deletado: Documento 5
📊 Resumo da deleção:
   ✅ Deletados: 5
   ❌ Erros: 0
   📋 Total: 5

📝 Iniciando criação de novos documentos...
📊 Estatísticas do mapeamento:
   Total de documentos: 28
   Níveis: 0 a 4

📁 Processando nível 0 (1 documentos):
   🔄 doc-root: E-commerce de Veículos
   ✅ Documento criado: E-commerce de Veículos (ID: abc123)

📁 Processando nível 1 (4 documentos):
   🔄 doc-systems: Sistemas
   ✅ Documento criado: Sistemas (ID: def456)
   ...

📈 Resumo da sincronização:
   ✅ Sucessos: 28
   ❌ Erros: 0
   📊 Total: 28

🎉 Sincronização concluída com sucesso!
```

## 🧪 Script de Teste

### Arquivo: `.github/scripts/test-delete-and-sync.ps1`

**Funcionalidades:**
- ✅ Testa conectividade
- ✅ Verifica documentos antes da execução
- ✅ Executa sincronização
- ✅ Verifica documentos após execução
- ✅ Exibe comparação de resultados

**Uso:**
```powershell
# Teste com deleção (padrão)
.\test-delete-and-sync.ps1

# Teste sem deleção
.\test-delete-and-sync.ps1 -CleanBeforeSync "false"
```

## ⚙️ Configuração no GitHub

### 1. **Secrets (Obrigatórios)**
```
OUTLINE_API_URL: https://outline-production-cebc.up.railway.app
OUTLINE_API_TOKEN: ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A
```

### 2. **Variables (Opcionais)**
```
CLEAN_BEFORE_SYNC: true  # ou false
```

### 3. **Configuração por Repositório**
- **Settings** > **Secrets and variables** > **Actions**
- **Repository secrets**: `OUTLINE_API_URL`, `OUTLINE_API_TOKEN`
- **Repository variables**: `CLEAN_BEFORE_SYNC`

## 🔍 Monitoramento

### 1. **Logs do GitHub Actions**
- Acesse: **Actions** > **Sync Documentation to Outline**
- Verifique logs de deleção e criação
- Identifique erros ou problemas

### 2. **Outline Dashboard**
- Acesse: https://outline-production-cebc.up.railway.app
- Verifique se documentos foram deletados/criados
- Confirme hierarquia correta

## 🎉 Resultado

**✅ Script atualizado com funcionalidade de deleção**
**✅ Controle flexível via variável de ambiente**
**✅ Logs detalhados e robustez**
**✅ Teste automatizado disponível**

---

**🎯 Agora o GitHub Actions deleta todos os documentos antes de criar novos, garantindo uma sincronização limpa e sem conflitos!**
