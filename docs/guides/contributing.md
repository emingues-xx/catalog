# Guia de Contribuição

Como contribuir com a documentação e desenvolvimento do E-commerce de Veículos.

## Estrutura da Documentação

### Organização
```
docs/
├── index.md                    # Página inicial
├── systems/                    # Documentação por sistema
│   ├── vitrine-veiculos/       # Sistema Vitrine
│   └── backoffice-veiculos/    # Sistema Backoffice
├── architecture/               # Arquitetura geral
│   ├── overview.md             # Visão geral
│   └── adrs/                   # Architecture Decision Records
└── guides/                     # Guias e tutoriais
```

### Padrões de Escrita

#### Tom e Linguagem
- **Tom técnico mas acessível**: Explique conceitos complexos de forma clara
- **Português brasileiro**: Use a norma culta, evite gírias
- **Presente do indicativo**: "O sistema processa" ao invés de "processará"
- **Voz ativa**: "A API retorna dados" ao invés de "dados são retornados"

#### Formatação
- **Títulos**: Use hierarquia clara (H1 > H2 > H3)
- **Código**: Sempre com syntax highlighting apropriado
- **Links**: Descritivos, evite "clique aqui"
- **Listas**: Use bullet points para enumerações
- **Tabelas**: Para dados estruturados

### Templates

#### Documentação de Sistema
```markdown
# Sistema [Nome]

## Visão Geral
Descrição em 2-3 parágrafos do propósito e escopo.

## Componentes
Lista dos componentes principais com tecnologias.

## Funcionalidades
### Funcionalidade Principal 1
Descrição detalhada...

## Arquitetura
Visão técnica de alto nível.

## Time Responsável
Squad/time responsável.
```

#### Documentação de Feature
```markdown
# Feature: [Nome da Feature]

## Descrição
O que a feature faz em 1-2 parágrafos.

## Funcionalidades
Lista detalhada das funcionalidades.

## Implementação Técnica
Detalhes técnicos relevantes.

## Regras de Negócio
Validações e restrições.

## Melhorias Futuras
Roadmap e próximos passos.
```

## Contribuindo com Código

### Fluxo de Trabalho

#### 1. Setup Local
```bash
# Clone do repositório
git clone https://github.com/emingues-xx/catalog.git
cd catalog

# Instalação do MkDocs
pip install mkdocs-material
pip install mkdocs-techdocs-core

# Servidor local
mkdocs serve
```

#### 2. Branch Strategy
```bash
# Criar branch para mudança
git checkout -b docs/nome-da-alteracao

# Fazer alterações
# ...

# Commit com convenção
git commit -m "docs: adiciona documentação da feature X"

# Push e PR
git push origin docs/nome-da-alteracao
```

### Convenções de Commit

Siga o padrão [Conventional Commits](https://conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]
[optional footer]
```

**Tipos principais**:
- `docs`: Mudanças na documentação
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `refactor`: Refatoração sem mudança de behavior
- `style`: Mudanças de formatação
- `test`: Adição ou correção de testes

**Exemplos**:
```
docs: adiciona documentação da API de veículos
docs(vitrine): atualiza arquitetura do sistema
feat(backoffice): implementa autenticação JWT
fix(api): corrige validação de CPF
```

## Review Process

### Criando Pull Request

#### Checklist
- [ ] Documentação atualizada
- [ ] Markdown válido (sem erros de lint)
- [ ] Links funcionais
- [ ] Imagens otimizadas (< 500KB)
- [ ] Spell check executado
- [ ] Preview local testado

#### Template de PR
```markdown
## Tipo de Mudança
- [ ] Documentação nova
- [ ] Atualização de documentação existente
- [ ] Correção de bugs na documentação
- [ ] Melhoria de estrutura/organização

## Descrição
Descreva resumidamente as mudanças.

## Checklist
- [ ] Testado localmente com `mkdocs serve`
- [ ] Links verificados
- [ ] Seguiu padrões de escrita
- [ ] Revisão ortográfica feita
```

### Processo de Review

#### Reviewers
- **Tech Writers**: Foco em clareza e estrutura
- **Tech Leads**: Foco em precisão técnica  
- **Product Owners**: Foco em alinhamento com negócio

#### Critérios de Aprovação
- ✅ Conteúdo tecnicamente correto
- ✅ Linguagem clara e acessível
- ✅ Estrutura bem organizada
- ✅ Links e referências válidas
- ✅ Exemplos funcionais

## Ferramentas

### Desenvolvimento Local
```bash
# MkDocs com live reload
mkdocs serve

# Build para produção
mkdocs build

# Lint de markdown
markdownlint docs/

# Spell check
cspell "docs/**/*.md"
```

### Extensões Recomendadas (VSCode)
- **Markdown All in One**: Preview e shortcuts
- **markdownlint**: Linting de markdown
- **Code Spell Checker**: Verificação ortográfica
- **Markdown Preview Enhanced**: Preview avançado

## Padrões Específicos

### Documentação de API
```markdown
## Endpoint GET /api/veiculos

### Request
\`\`\`http
GET /api/veiculos?marca=honda&modelo=civic
Authorization: Bearer <token>
\`\`\`

### Response
\`\`\`json
{
  "data": [...],
  "total": 150,
  "page": 1
}
\`\`\`

### Parâmetros
| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| marca | string | Não | Filtro por marca |
```

### Diagramas
Use Mermaid para diagramas simples:

```markdown
\`\`\`mermaid
graph TD
    A[Frontend] --> B[BFF]
    B --> C[API]
    C --> D[Database]
\`\`\`
```

## Contato

### Dúvidas e Sugestões
- **Slack**: #ecommerce-docs
- **E-mail**: tech-docs@empresa.com
- **Issues**: GitHub Issues neste repositório

### Office Hours
- **Terças**: 14h-15h (Tech Writing)
- **Quintas**: 10h-11h (Architecture Review)