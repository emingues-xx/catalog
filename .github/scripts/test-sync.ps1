# Script para testar sincronização com Outline
param(
    [string]$ApiUrl = "https://outline-production-cebc.up.railway.app",
    [string]$ApiToken = "ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"
)

Write-Host "Testando sincronização com Outline..." -ForegroundColor Cyan
Write-Host "URL: $ApiUrl" -ForegroundColor Yellow
Write-Host "Token: $($ApiToken.Substring(0, 20))..." -ForegroundColor Yellow
Write-Host ""

# Definir variáveis de ambiente
$env:OUTLINE_API_URL = $ApiUrl
$env:OUTLINE_API_TOKEN = $ApiToken

# Verificar se o arquivo de mapeamento existe
$mappingFile = "outline-mapping.yaml"
if (-not (Test-Path $mappingFile)) {
    Write-Host "ERROR: Arquivo $mappingFile não encontrado!" -ForegroundColor Red
    exit 1
}

Write-Host "Arquivo de mapeamento encontrado: $mappingFile" -ForegroundColor Green

# Verificar se o diretório docs existe
$docsDir = "docs"
if (-not (Test-Path $docsDir)) {
    Write-Host "ERROR: Diretório $docsDir não encontrado!" -ForegroundColor Red
    exit 1
}

Write-Host "Diretório de documentação encontrado: $docsDir" -ForegroundColor Green

# Contar arquivos .md
$mdFiles = Get-ChildItem -Path $docsDir -Recurse -Filter "*.md"
Write-Host "Arquivos .md encontrados: $($mdFiles.Count)" -ForegroundColor Green

# Listar alguns arquivos
Write-Host ""
Write-Host "Primeiros 5 arquivos:" -ForegroundColor Yellow
$count = 0
foreach ($file in $mdFiles) {
    if ($count -lt 5) {
        Write-Host "   - $($file.FullName)" -ForegroundColor White
        $count++
    }
}

if ($mdFiles.Count -gt 5) {
    Write-Host "   ... e mais $($mdFiles.Count - 5) arquivos" -ForegroundColor White
}

Write-Host ""
Write-Host "Configuração validada com sucesso!" -ForegroundColor Green
Write-Host "Para executar a sincronização, use:" -ForegroundColor Yellow
Write-Host "   python .github/scripts/sync_working.py" -ForegroundColor White
