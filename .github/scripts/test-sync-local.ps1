# Script para testar a sincronização localmente
param(
    [string]$ApiUrl = "https://outline-production-cebc.up.railway.app",
    [string]$ApiToken = "ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"
)

Write-Host "🧪 Teste Local - Sincronização Outline" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Cyan

# Verificar se Python está disponível
Write-Host "🔍 Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python não encontrado. Instalando..." -ForegroundColor Red
    
    # Tentar instalar Python via winget
    try {
        winget install Python.Python.3.11
        Write-Host "✅ Python instalado via winget" -ForegroundColor Green
    } catch {
        Write-Host "❌ Falha ao instalar Python. Instale manualmente." -ForegroundColor Red
        exit 1
    }
}

# Verificar se o arquivo de mapeamento existe
Write-Host "`n📄 Verificando arquivo de mapeamento..." -ForegroundColor Yellow
if (Test-Path "outline-mapping.yaml") {
    Write-Host "✅ outline-mapping.yaml encontrado" -ForegroundColor Green
} else {
    Write-Host "❌ outline-mapping.yaml não encontrado" -ForegroundColor Red
    exit 1
}

# Verificar se o script Python existe
Write-Host "`n🐍 Verificando script Python..." -ForegroundColor Yellow
if (Test-Path ".github\scripts\sync_working.py") {
    Write-Host "✅ sync_working.py encontrado" -ForegroundColor Green
} else {
    Write-Host "❌ sync_working.py não encontrado" -ForegroundColor Red
    exit 1
}

# Configurar variáveis de ambiente
Write-Host "`n🔧 Configurando variáveis de ambiente..." -ForegroundColor Yellow
$env:OUTLINE_API_URL = $ApiUrl
$env:OUTLINE_API_TOKEN = $ApiToken

Write-Host "   OUTLINE_API_URL: $ApiUrl" -ForegroundColor White
Write-Host "   OUTLINE_API_TOKEN: $($ApiToken.Substring(0, 20))..." -ForegroundColor White

# Testar conectividade primeiro
Write-Host "`n🔗 Testando conectividade..." -ForegroundColor Yellow
try {
    $headers = @{
        'Authorization' = "Bearer $ApiToken"
        'Content-Type' = 'application/json'
        'Accept' = 'application/json'
    }
    
    $body = @{ id = "" }
    $response = Invoke-RestMethod -Uri "$ApiUrl/api/collections.list" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 10
    
    Write-Host "✅ Conectividade OK - $($response.data.Count) coleções encontradas" -ForegroundColor Green
    
    foreach ($collection in $response.data) {
        Write-Host "   - $($collection.name) (ID: $($collection.id))" -ForegroundColor White
    }
} catch {
    Write-Host "❌ Falha na conectividade: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Executar o script Python
Write-Host "`n🚀 Executando sincronização..." -ForegroundColor Yellow
Write-Host "=" * 30 -ForegroundColor Yellow

try {
    python .github\scripts\sync_working.py
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n🎉 Sincronização concluída com sucesso!" -ForegroundColor Green
    } else {
        Write-Host "`n💥 Sincronização falhou com código: $LASTEXITCODE" -ForegroundColor Red
    }
} catch {
    Write-Host "`n💥 Erro ao executar script: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n📋 Teste local concluído!" -ForegroundColor Cyan
