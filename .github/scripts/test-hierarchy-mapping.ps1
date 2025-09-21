# Testar mapeamento de hierarquia

Write-Host "Verificando mapeamento de hierarquia..."

# Simular a estrutura esperada
$expectedHierarchy = @{
    "E-commerce de Veículos - Documentação" = @()
    "Sistemas" = @("Vitrine de Veículos", "Backoffice de Veículos")
    "Vitrine de Veículos" = @("Busca de Veículos", "Arquitetura - Vitrine de Veículos")
    "Backoffice de Veículos" = @("Arquitetura - Backoffice de Veículos", "Cadastro de Anúncios")
    "Arquitetura" = @("Sobre ADRs")
    "Componentes" = @("Vitrine Web", "Vitrine API", "Vitrine BFF", "Backoffice Web", "Backoffice API", "Backoffice BFF", "Pipelines E-commerce")
    "Vitrine Web" = @("Arquitetura", "Setup")
    "Vitrine API" = @("API Reference")
    "Pipelines E-commerce" = @("Automação - Pipelines", "Workflows - Pipelines")
    "Guias" = @("Guia de Contribuição")
}

Write-Host ""
Write-Host "=== ESTRUTURA ESPERADA ==="
foreach ($parent in $expectedHierarchy.Keys) {
    Write-Host "📁 $parent"
    foreach ($child in $expectedHierarchy[$parent]) {
        Write-Host "  └── $child"
    }
}

Write-Host ""
Write-Host "=== ORDEM DE DELEÇÃO ESPERADA ==="
Write-Host "1. Documentos sem filhos (folhas):"
$leaves = @()
foreach ($parent in $expectedHierarchy.Keys) {
    foreach ($child in $expectedHierarchy[$parent]) {
        if (-not $expectedHierarchy.ContainsKey($child)) {
            $leaves += $child
        }
    }
}
$leaves | Sort-Object | ForEach-Object { Write-Host "  - $_" }

Write-Host ""
Write-Host "2. Documentos pais (após filhos deletados):"
$parents = $expectedHierarchy.Keys | Sort-Object
$parents | ForEach-Object { Write-Host "  - $_" }

Write-Host ""
Write-Host "Mapeamento verificado!"
