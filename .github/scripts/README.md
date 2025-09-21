# Sincronização de Documentação com Outline

Este diretório contém scripts e configurações para sincronizar automaticamente a documentação do repositório com o Outline.

## 📋 Pré-requisitos

1. **Instância do Outline**: Você precisa ter uma instância do Outline configurada
2. **Token de API**: Um token de API válido do Outline
3. **Secrets do GitHub**: Configurar os secrets necessários no repositório

## 🔧 Configuração

### 1. Configurar Secrets no GitHub

Vá para **Settings > Secrets and variables > Actions** no seu repositório e adicione:

- `OUTLINE_API_URL`: URL da API do seu Outline (ex: `https://your-outline.com/api`)
- `OUTLINE_API_TOKEN`: Token de API do Outline

### 2. Configurar o Arquivo de Mapeamento

Edite o arquivo `outline-mapping.yaml` na raiz do projeto para:

- Definir os IDs das coleções no Outline
- Mapear documentos específicos para títulos, tags e descrições
- Configurar coleções e suas propriedades

### 3. Personalizar o Mapeamento

```yaml
# Exemplo de mapeamento personalizado
documents:
  "docs/systems/vitrine-veiculos/index.md":
    title: "Sistema Vitrine de Veículos"
    collection_id: "systems-collection"
    tags: ["system", "vitrine", "frontend"]
    description: "Documentação do sistema de vitrine de veículos"
```

## 🚀 Como Funciona

### Trigger do Workflow

O workflow é executado automaticamente quando:

- Um PR é mergeado para a branch `main`
- Há mudanças nos arquivos do diretório `docs/`
- O arquivo `outline-mapping.yaml` é modificado
- O próprio workflow é atualizado

### Processo de Sincronização

1. **Detecção de Mudanças**: Verifica se houve alterações na documentação
2. **Criação de Coleções**: Garante que todas as coleções necessárias existam
3. **Processamento de Documentos**: Para cada arquivo `.md`:
   - Lê o conteúdo do arquivo
   - Aplica o mapeamento configurado
   - Busca se o documento já existe no Outline
   - Cria ou atualiza o documento
4. **Relatório**: Exibe resumo da sincronização

### Metadados Adicionados

O script adiciona automaticamente:

- **Cabeçalho**: Informações sobre o repositório e commit
- **Rodapé**: Tags e link para o arquivo original
- **Tags**: Baseadas na configuração do mapeamento

## 📁 Estrutura de Arquivos

```
.github/
├── workflows/
│   └── sync-docs-to-outline.yml    # Workflow do GitHub Actions
└── scripts/
    ├── sync_to_outline.py          # Script principal de sincronização
    └── README.md                   # Este arquivo

outline-mapping.yaml                # Configuração de mapeamento
```

## 🔍 Troubleshooting

### Erro de Autenticação

```
❌ Erro ao buscar documento: 401 Unauthorized
```

**Solução**: Verifique se o `OUTLINE_API_TOKEN` está correto e tem as permissões necessárias.

### Erro de URL da API

```
❌ Erro ao buscar documento: Connection refused
```

**Solução**: Verifique se o `OUTLINE_API_URL` está correto e acessível.

### Documentos Não Sincronizados

**Possíveis causas**:
- Arquivo não está no diretório `docs/`
- Arquivo não tem extensão `.md`
- Erro de codificação (use UTF-8)

### Coleções Não Criadas

**Solução**: Verifique se o token tem permissão para criar coleções e se os IDs estão corretos.

## 🎯 Exemplos de Uso

### Mapeamento Simples

```yaml
documents:
  "docs/index.md":
    title: "Documentação Principal"
    collection_id: "main-docs"
    tags: ["overview", "main"]
```

### Mapeamento Avançado

```yaml
documents:
  "docs/systems/vitrine-veiculos/arquitetura.md":
    title: "Arquitetura - Vitrine de Veículos"
    collection_id: "architecture-collection"
    tags: ["system", "vitrine", "architecture", "technical"]
    description: "Documentação detalhada da arquitetura do sistema de vitrine"
```

## 📝 Logs e Monitoramento

O workflow gera logs detalhados que podem ser visualizados em:

**GitHub Actions > Sync Documentation to Outline > sync-to-outline**

Os logs incluem:
- ✅ Documentos sincronizados com sucesso
- ❌ Erros de sincronização
- 📊 Resumo final da operação

## 🔄 Atualizações

Para atualizar a configuração:

1. Modifique o arquivo `outline-mapping.yaml`
2. Faça commit das mudanças
3. O workflow será executado automaticamente no próximo merge para `main`
