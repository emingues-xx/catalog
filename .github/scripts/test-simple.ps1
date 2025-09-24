# Script simples para testar sincronização
param(
    [string]$ApiUrl = "https://outline-production-cebc.up.railway.app",
    [string]$ApiToken = "ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"
)

Write-Host "Teste Local - Sincronizacao Outline" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

# Configurar variaveis de ambiente
$env:OUTLINE_API_URL = $ApiUrl
$env:OUTLINE_API_TOKEN = $ApiToken

Write-Host "Configurando variaveis de ambiente..." -ForegroundColor Yellow
Write-Host "   OUTLINE_API_URL: $ApiUrl" -ForegroundColor White
Write-Host "   OUTLINE_API_TOKEN: $($ApiToken.Substring(0, 20))..." -ForegroundColor White

# Verificar se Python esta disponivel
Write-Host "`nVerificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Python nao encontrado. Instale Python primeiro." -ForegroundColor Red
    exit 1
}

# Verificar arquivos necessarios
Write-Host "`nVerificando arquivos..." -ForegroundColor Yellow
if (Test-Path "outline-mapping.yaml") {
    Write-Host "outline-mapping.yaml: OK" -ForegroundColor Green
} else {
    Write-Host "outline-mapping.yaml: NAO ENCONTRADO" -ForegroundColor Red
    exit 1
}

if (Test-Path ".github\scripts\sync_working.py") {
    Write-Host "sync_working.py: OK" -ForegroundColor Green
} else {
    Write-Host "sync_working.py: NAO ENCONTRADO" -ForegroundColor Red
    exit 1
}

# Testar conectividade
Write-Host "`nTestando conectividade..." -ForegroundColor Yellow
try {
    $headers = @{
        'Authorization' = "Bearer $ApiToken"
        'Content-Type' = 'application/json'
        'Accept' = 'application/json'
    }
    
    $body = @{ id = "" }
    $response = Invoke-RestMethod -Uri "$ApiUrl/api/collections.list" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 10
    
    Write-Host "Conectividade OK - $($response.data.Count) colecoes encontradas" -ForegroundColor Green
    
    foreach ($collection in $response.data) {
        Write-Host "   - $($collection.name)" -ForegroundColor White
    }
} catch {
    Write-Host "Falha na conectividade: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Executar sincronizacao
Write-Host "`nExecutando sincronizacao..." -ForegroundColor Yellow
Write-Host "=============================================" -ForegroundColor Yellow

try {
    python .github\scripts\sync_working.py
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`nSincronizacao concluida com sucesso!" -ForegroundColor Green
    } else {
        Write-Host "`nSincronizacao falhou com codigo: $LASTEXITCODE" -ForegroundColor Red
    }
} catch {
    Write-Host "`nErro ao executar script: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`nTeste local concluido!" -ForegroundColor Cyan
