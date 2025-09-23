# Script PowerShell para sincronizar documentação com Backstage TechDocs

param(
    [string]$BackstageUrl = "http://localhost:7007",
    [string]$BackstageToken = "",
    [string]$DocsDir = "docs/components"
)

Write-Host "🚀 Sincronizando documentação com Backstage TechDocs..." -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

# Verificar se o token foi fornecido
if (-not $BackstageToken) {
    $BackstageToken = $env:BACKSTAGE_TOKEN
    if (-not $BackstageToken) {
        Write-Host "❌ BACKSTAGE_TOKEN não configurado" -ForegroundColor Red
        Write-Host "Configure a variável de ambiente BACKSTAGE_TOKEN ou passe como parâmetro" -ForegroundColor Yellow
        Write-Host "Exemplo: .\sync-backstage.ps1 -BackstageToken 'seu-token-aqui'" -ForegroundColor Yellow
        exit 1
    }
}

# Verificar se o diretório de documentação existe
if (-not (Test-Path $DocsDir)) {
    Write-Host "❌ Diretório de documentação não encontrado: $DocsDir" -ForegroundColor Red
    exit 1
}

# Configurar variáveis de ambiente
$env:BACKSTAGE_URL = $BackstageUrl
$env:BACKSTAGE_TOKEN = $BackstageToken

Write-Host "📋 Configurações:" -ForegroundColor Yellow
Write-Host "   Backstage URL: $BackstageUrl" -ForegroundColor White
Write-Host "   Docs Directory: $DocsDir" -ForegroundColor White
Write-Host "   Token: $($BackstageToken.Substring(0, 10))..." -ForegroundColor White

Write-Host "`n🔍 Verificando componentes com documentação..." -ForegroundColor Yellow

# Listar componentes com documentação
$components = @()
Get-ChildItem -Path $DocsDir -Directory | ForEach-Object {
    $componentName = $_.Name
    $indexFile = Join-Path $_.FullName "index.md"
    
    if (Test-Path $indexFile) {
        $components += $componentName
        Write-Host "   ✅ $componentName - Tem documentação" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️ $componentName - Sem documentação (index.md)" -ForegroundColor Yellow
    }
}

Write-Host "`n📊 Componentes encontrados: $($components.Count)" -ForegroundColor Cyan

if ($components.Count -eq 0) {
    Write-Host "❌ Nenhum componente com documentação encontrado" -ForegroundColor Red
    exit 1
}

Write-Host "`n🚀 Executando sincronização..." -ForegroundColor Green

# Executar script Python
try {
    python .github/scripts/sync_to_backstage.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n🎉 Sincronização concluída com sucesso!" -ForegroundColor Green
    } else {
        Write-Host "`n❌ Erro na sincronização" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "`n❌ Erro ao executar script Python: $_" -ForegroundColor Red
    exit 1
}

Write-Host "`n📄 Verificando resultados..." -ForegroundColor Yellow

# Verificar arquivo de resultados
$resultsFile = "backstage-sync-results.json"
if (Test-Path $resultsFile) {
    $results = Get-Content $resultsFile | ConvertFrom-Json
    Write-Host "`n📊 Resultados da sincronização:" -ForegroundColor Cyan
    Write-Host "=" * 40 -ForegroundColor Cyan
    
    $successful = 0
    $total = 0
    
    foreach ($component in $results.PSObject.Properties) {
        $total++
        if ($component.Value) {
            $successful++
            Write-Host "   ✅ $($component.Name)" -ForegroundColor Green
        } else {
            Write-Host "   ❌ $($component.Name)" -ForegroundColor Red
        }
    }
    
    Write-Host "`n📈 Resumo:" -ForegroundColor Yellow
    Write-Host "   Total: $total" -ForegroundColor White
    Write-Host "   Sucesso: $successful" -ForegroundColor Green
    Write-Host "   Falhas: $($total - $successful)" -ForegroundColor Red
    
    if ($successful -eq $total) {
        Write-Host "`n🎉 Todos os componentes foram sincronizados com sucesso!" -ForegroundColor Green
    } else {
        Write-Host "`n⚠️ Alguns componentes tiveram problemas na sincronização." -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ Arquivo de resultados não encontrado" -ForegroundColor Red
}

Write-Host "`n🔗 Próximos passos:" -ForegroundColor Yellow
Write-Host "   1. Verifique os componentes no Backstage: $BackstageUrl" -ForegroundColor White
Write-Host "   2. Confirme que a documentação está sendo exibida corretamente" -ForegroundColor White
Write-Host "   3. Configure permissões e ownership dos componentes" -ForegroundColor White
Write-Host "   4. Adicione tags e metadados adicionais conforme necessário" -ForegroundColor White

Write-Host "`n✨ Sincronização concluída!" -ForegroundColor Green
