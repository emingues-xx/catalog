# Script para testar a configuração final
param(
    [string]$ApiUrl = "https://outline-production-cebc.up.railway.app",
    [string]$ApiToken = "ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"
)

$headers = @{
    'Authorization' = "Bearer $ApiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Testando configuração final..." -ForegroundColor Cyan
Write-Host "URL: $ApiUrl" -ForegroundColor Yellow
Write-Host "Token: $($ApiToken.Substring(0, 20))..." -ForegroundColor Yellow
Write-Host ""

# Teste 1: collections.list (como no curl que funciona)
Write-Host "1. Testando collections.list (como no curl)..." -ForegroundColor Green
try {
    $body = @{ id = "" }
    $response = Invoke-RestMethod -Uri "$ApiUrl/api/collections.list" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 10
    Write-Host "SUCCESS: collections.list funcionou" -ForegroundColor Green
    Write-Host "   Coleções encontradas: $($response.data.Count)" -ForegroundColor White
    
    foreach ($collection in $response.data) {
        Write-Host "   - $($collection.name) (ID: $($collection.id))" -ForegroundColor White
    }
} catch {
    Write-Host "ERROR: collections.list falhou - $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        Write-Host "   Status: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
    }
    exit 1
}

Write-Host ""

# Teste 2: documents.list
Write-Host "2. Testando documents.list..." -ForegroundColor Green
try {
    $body = @{ id = "" }
    $response = Invoke-RestMethod -Uri "$ApiUrl/api/documents.list" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 10
    Write-Host "SUCCESS: documents.list funcionou" -ForegroundColor Green
    Write-Host "   Documentos encontrados: $($response.data.Count)" -ForegroundColor White
    
    $count = 0
    foreach ($doc in $response.data) {
        if ($count -lt 3) {
            Write-Host "   - $($doc.title) (ID: $($doc.id))" -ForegroundColor White
            $count++
        }
    }
    
    if ($response.data.Count -gt 3) {
        Write-Host "   ... e mais $($response.data.Count - 3) documentos" -ForegroundColor White
    }
} catch {
    Write-Host "ERROR: documents.list falhou - $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        Write-Host "   Status: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
    }
    exit 1
}

Write-Host ""
Write-Host "SUCCESS: Configuração final validada!" -ForegroundColor Green
Write-Host "O script sync_working.py deve funcionar agora." -ForegroundColor Yellow
