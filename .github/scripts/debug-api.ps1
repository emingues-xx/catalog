# Script para debugar a API do Outline
param(
    [string]$ApiUrl = "https://outline-production-cebc.up.railway.app",
    [string]$ApiToken = "ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"
)

$headers = @{
    'Authorization' = "Bearer $ApiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Debugando API do Outline..." -ForegroundColor Cyan
Write-Host "URL: $ApiUrl" -ForegroundColor Yellow
Write-Host ""

# Teste 1: GET vs POST
Write-Host "1. Testando GET vs POST para documents.list..." -ForegroundColor Green

# Teste GET
Write-Host "   Testando GET..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$ApiUrl/documents.list" -Headers $headers -Method Get -TimeoutSec 10
    Write-Host "   SUCCESS: GET funcionou" -ForegroundColor Green
} catch {
    Write-Host "   ERROR: GET falhou - $($_.Exception.Message)" -ForegroundColor Red
}

# Teste POST com dados vazios
Write-Host "   Testando POST com dados vazios..." -ForegroundColor Yellow
try {
    $body = @{}
    $response = Invoke-RestMethod -Uri "$ApiUrl/documents.list" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 10
    Write-Host "   SUCCESS: POST com dados vazios funcionou" -ForegroundColor Green
} catch {
    Write-Host "   ERROR: POST com dados vazios falhou - $($_.Exception.Message)" -ForegroundColor Red
}

# Teste POST com id vazio
Write-Host "   Testando POST com id vazio..." -ForegroundColor Yellow
try {
    $body = @{ id = "" }
    $response = Invoke-RestMethod -Uri "$ApiUrl/documents.list" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 10
    Write-Host "   SUCCESS: POST com id vazio funcionou" -ForegroundColor Green
} catch {
    Write-Host "   ERROR: POST com id vazio falhou - $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""

# Teste 2: Verificar se precisa de collectionId
Write-Host "2. Testando com collectionId..." -ForegroundColor Green
try {
    $body = @{ collectionId = "" }
    $response = Invoke-RestMethod -Uri "$ApiUrl/documents.list" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 10
    Write-Host "   SUCCESS: POST com collectionId vazio funcionou" -ForegroundColor Green
} catch {
    Write-Host "   ERROR: POST com collectionId vazio falhou - $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""

# Teste 3: Verificar se precisa de parâmetros específicos
Write-Host "3. Testando com parâmetros específicos..." -ForegroundColor Green
try {
    $body = @{ 
        id = ""
        collectionId = ""
        limit = 10
    }
    $response = Invoke-RestMethod -Uri "$ApiUrl/documents.list" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 10
    Write-Host "   SUCCESS: POST com parâmetros específicos funcionou" -ForegroundColor Green
    Write-Host "   Documentos encontrados: $($response.data.Count)" -ForegroundColor White
} catch {
    Write-Host "   ERROR: POST com parâmetros específicos falhou - $($_.Exception.Message)" -ForegroundColor Red
}
