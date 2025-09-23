# Script para testar diferentes endpoints da API do Outline
param(
    [string]$ApiUrl = "https://outline-production-cebc.up.railway.app",
    [string]$ApiToken = "ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"
)

$headers = @{
    'Authorization' = "Bearer $ApiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Testando diferentes endpoints..." -ForegroundColor Cyan
Write-Host ""

# Lista de endpoints para testar
$endpoints = @(
    "/api/auth.info",
    "/api/collections.list",
    "/api/documents.list",
    "/auth.info",
    "/collections.list",
    "/documents.list"
)

foreach ($endpoint in $endpoints) {
    $fullUrl = "$ApiUrl$endpoint"
    Write-Host "Testando: $fullUrl" -ForegroundColor Yellow
    
    try {
        $response = Invoke-RestMethod -Uri $fullUrl -Headers $headers -Method Get -TimeoutSec 5
        Write-Host "SUCCESS: $endpoint" -ForegroundColor Green
        if ($response.data) {
            Write-Host "   Dados recebidos: $($response.data.Count) itens" -ForegroundColor White
        }
    } catch {
        Write-Host "ERROR: $endpoint - $($_.Exception.Message)" -ForegroundColor Red
        if ($_.Exception.Response) {
            Write-Host "   Status: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
        }
    }
    Write-Host ""
}
