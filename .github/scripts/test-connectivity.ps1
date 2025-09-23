# Script para testar conectividade com a API do Outline
param(
    [string]$ApiUrl = "https://outline-production-cebc.up.railway.app",
    [string]$ApiToken = "ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"
)

Write-Host "Testando conectividade com Outline..." -ForegroundColor Cyan
Write-Host "URL: $ApiUrl" -ForegroundColor Yellow
Write-Host "Token: $($ApiToken.Substring(0, 20))..." -ForegroundColor Yellow
Write-Host ""

$headers = @{
    'Authorization' = "Bearer $ApiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

# Teste 1: Verificar se a API está acessível
Write-Host "1. Testando acesso à API..." -ForegroundColor Green
try {
    $response = Invoke-RestMethod -Uri "$ApiUrl/auth.info" -Headers $headers -Method Get -TimeoutSec 10
    Write-Host "SUCCESS: API acessível - Status 200" -ForegroundColor Green
    Write-Host "   Usuário: $($response.data.user.name)" -ForegroundColor White
} catch {
    Write-Host "ERROR: Erro na API: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        Write-Host "   Status: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
    }
    exit 1
}

# Teste 2: Listar coleções
Write-Host ""
Write-Host "2. Testando listagem de coleções..." -ForegroundColor Green
try {
    $response = Invoke-RestMethod -Uri "$ApiUrl/collections.list" -Headers $headers -Method Get -TimeoutSec 10
    Write-Host "SUCCESS: Coleções listadas com sucesso" -ForegroundColor Green
    Write-Host "   Total de coleções: $($response.data.Count)" -ForegroundColor White
    
    foreach ($collection in $response.data) {
        Write-Host "   - $($collection.name) (ID: $($collection.id))" -ForegroundColor White
    }
} catch {
    Write-Host "ERROR: Erro ao listar coleções: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        Write-Host "   Status: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
    }
    exit 1
}

# Teste 3: Listar documentos
Write-Host ""
Write-Host "3. Testando listagem de documentos..." -ForegroundColor Green
try {
    $response = Invoke-RestMethod -Uri "$ApiUrl/documents.list" -Headers $headers -Method Get -TimeoutSec 10
    Write-Host "SUCCESS: Documentos listados com sucesso" -ForegroundColor Green
    Write-Host "   Total de documentos: $($response.data.Count)" -ForegroundColor White
    
    $count = 0
    foreach ($doc in $response.data) {
        if ($count -lt 5) {
            Write-Host "   - $($doc.title) (ID: $($doc.id))" -ForegroundColor White
            $count++
        }
    }
    
    if ($response.data.Count -gt 5) {
        Write-Host "   ... e mais $($response.data.Count - 5) documentos" -ForegroundColor White
    }
} catch {
    Write-Host "ERROR: Erro ao listar documentos: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        Write-Host "   Status: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
    }
    exit 1
}

Write-Host ""
Write-Host "SUCCESS: Todos os testes passaram! A configuração está correta." -ForegroundColor Green
