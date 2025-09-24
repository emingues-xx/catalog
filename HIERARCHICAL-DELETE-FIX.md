# 🔧 Correção - Deleção Hierárquica

## ❌ Problema Identificado

O script estava duplicando documentos ao invés de deletar corretamente, porque não estava respeitando a hierarquia na deleção.

## ✅ Solução Implementada

### 1. **Nova Função de Deleção Hierárquica**

#### `_delete_all_documents_hierarchically()`
```python
def _delete_all_documents_hierarchically(self) -> bool:
    """Deleta todos os documentos da collection obedecendo hierarquia (maior para menor nível)"""
```

**Funcionalidades:**
- ✅ Organiza documentos por nível
- ✅ Deleta do maior para o menor nível (4 → 3 → 2 → 1 → 0)
- ✅ Evita problemas com documentos filhos
- ✅ Mapeia documentos existentes com o mapeamento

### 2. **Determinação Inteligente de Níveis**

#### `_get_document_level_from_outline()`
```python
def _get_document_level_from_outline(self, doc: Dict) -> int:
    """Determina o nível de um documento do Outline baseado na hierarquia"""
```

**Estratégia:**
1. **Mapeamento Exato**: Busca o documento no `outline-mapping.yaml` pelo título
2. **Heurística Inteligente**: Se não encontrar, usa palavras-chave no título
3. **Estrutura de Parent**: Considera se o documento tem `parentDocumentId`

### 3. **Mapeamento de Níveis por Palavras-Chave**

| **Nível** | **Palavras-Chave** | **Exemplos** |
|-----------|-------------------|--------------|
| **4** | features, arquitetura, setup, api, workflows | "Busca de Veículos", "Arquitetura - Vitrine Web" |
| **3** | vitrine, backoffice, pipelines, shared, ui-components, mongodb | "Vitrine de Veículos", "MongoDB Database" |
| **2** | sistemas, componentes, arquitetura, guias, adrs, contribuindo | "Sistemas", "Componentes", "ADRs" |
| **1** | Outros com parent | Documentos filhos genéricos |
| **0** | Sem parent | Documento raiz |

## 🔄 Processo de Deleção

### Ordem de Deleção:
```
Nível 4: Documentos específicos (features, arquitetura, etc.)
    ↓
Nível 3: Componentes e sistemas (vitrine, backoffice, etc.)
    ↓
Nível 2: Seções principais (sistemas, componentes, etc.)
    ↓
Nível 1: Documentos filhos genéricos
    ↓
Nível 0: Documento raiz
```

### Exemplo de Execução:
```
📁 Deletando nível 4 (3 documentos):
   ✅ Deletado: Busca de Veículos
   ✅ Deletado: Cadastro de Anúncio
   ✅ Deletado: Arquitetura - Vitrine Web

📁 Deletando nível 3 (8 documentos):
   ✅ Deletado: Vitrine de Veículos
   ✅ Deletado: Backoffice de Veículos
   ✅ Deletado: MongoDB Database
   ...

📁 Deletando nível 2 (4 documentos):
   ✅ Deletado: Sistemas
   ✅ Deletado: Componentes
   ✅ Deletado: Arquitetura
   ✅ Deletado: Guias

📁 Deletando nível 1 (1 documentos):
   ✅ Deletado: Documento Filho

📁 Deletando nível 0 (1 documentos):
   ✅ Deletado: E-commerce de Veículos
```

## 🎯 Benefícios da Correção

### 1. **Eliminação de Duplicatas**
- ✅ Deleta todos os documentos existentes antes de criar novos
- ✅ Evita conflitos de títulos
- ✅ Garante sincronização limpa

### 2. **Respeito à Hierarquia**
- ✅ Deleta filhos antes dos pais
- ✅ Evita erros de referência
- ✅ Mantém integridade estrutural

### 3. **Mapeamento Inteligente**
- ✅ Identifica níveis corretamente
- ✅ Funciona mesmo com documentos não mapeados
- ✅ Heurística robusta para casos especiais

### 4. **Logs Detalhados**
- ✅ Mostra progresso por nível
- ✅ Identifica problemas específicos
- ✅ Estatísticas completas

## 🧪 Teste da Correção

### Script de Teste: `.github/scripts/test-hierarchical-delete.ps1`

**Funcionalidades:**
- ✅ Verifica documentos antes da execução
- ✅ Executa deleção hierárquica
- ✅ Verifica documentos após execução
- ✅ Mostra estrutura de parent/child

**Uso:**
```powershell
.\test-hierarchical-delete.ps1
```

### Verificação Manual:
1. **Antes**: Verificar documentos existentes no Outline
2. **Executar**: Fazer commit para triggerar GitHub Actions
3. **Depois**: Verificar se documentos foram deletados e recriados
4. **Validar**: Confirmar que não há duplicatas

## 📋 Configuração

### Variável de Ambiente:
```bash
CLEAN_BEFORE_SYNC=true  # Habilita deleção hierárquica
```

### GitHub Actions:
```yaml
env:
  CLEAN_BEFORE_SYNC: ${{ vars.CLEAN_BEFORE_SYNC || 'true' }}
```

## 🔍 Monitoramento

### Logs Esperados:
```
🧹 Limpando documentos existentes...
🗑️  Deletando todos os documentos existentes (hierarquicamente)...
📋 Encontrados X documentos para deletar

📁 Deletando nível 4 (X documentos):
   ✅ Deletado: [título]
   ...

📊 Resumo da deleção:
   ✅ Deletados: X
   ❌ Erros: 0
   📋 Total: X

📝 Iniciando criação de novos documentos...
```

### Verificação no Outline:
- ✅ Nenhum documento duplicado
- ✅ Hierarquia correta
- ✅ Todos os documentos do mapeamento presentes
- ✅ Estrutura de parent/child correta

## 🎉 Resultado

**✅ Deleção hierárquica implementada**
**✅ Eliminação de duplicatas**
**✅ Respeito à estrutura de documentos**
**✅ Mapeamento inteligente de níveis**

---

**🎯 Agora o script deleta corretamente todos os documentos obedecendo a hierarquia, eliminando duplicatas e garantindo sincronização limpa!**
