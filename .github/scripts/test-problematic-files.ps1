# Script para testar arquivos problemáticos
param(
    [string]$ApiUrl = "https://outline-production-cebc.up.railway.app",
    [string]$ApiToken = "ol_api_2yNCdA9PywEilrGBTTZswHV5hYemUhIRMTgi4A"
)

Write-Host "🧪 Teste - Arquivos Problemáticos" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Cyan

# Configurar variaveis de ambiente
$env:OUTLINE_API_URL = $ApiUrl
$env:OUTLINE_API_TOKEN = $ApiToken

Write-Host "Testando criação de documentos problemáticos..." -ForegroundColor Yellow

# Testar vitrine-veiculos (nível 2)
Write-Host "`n1. Testando vitrine-veiculos (nível 2)..." -ForegroundColor Green
try {
    $headers = @{
        'Authorization' = "Bearer $ApiToken"
        'Content-Type' = 'application/json'
        'Accept' = 'application/json'
    }
    
    # Ler conteúdo do arquivo
    $content = Get-Content "docs\systems\vitrine-veiculos\index.md" -Raw -Encoding UTF8
    
    $body = @{
        title = "Vitrine de Veículos - Teste"
        text = $content
        collectionId = "d236ae05-812e-426a-a125-75653888903e"
        publish = $true
    }
    
    $response = Invoke-RestMethod -Uri "$ApiUrl/api/documents.create" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 30
    
    Write-Host "✅ Sucesso: vitrine-veiculos criado" -ForegroundColor Green
    Write-Host "   ID: $($response.data.id)" -ForegroundColor White
    
    # Deletar o documento de teste
    $deleteBody = @{ id = $response.data.id }
    Invoke-RestMethod -Uri "$ApiUrl/api/documents.delete" -Headers $headers -Method Post -Body ($deleteBody | ConvertTo-Json) -TimeoutSec 10
    Write-Host "   🗑️ Documento de teste deletado" -ForegroundColor Yellow
    
} catch {
    Write-Host "❌ Erro: vitrine-veiculos - $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        $responseBody = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($responseBody)
        $responseText = $reader.ReadToEnd()
        Write-Host "   Resposta: $responseText" -ForegroundColor Red
    }
}

# Testar vitrine-veiculos-bff (nível 3)
Write-Host "`n2. Testando vitrine-veiculos-bff (nível 3)..." -ForegroundColor Green
try {
    # Ler conteúdo do arquivo
    $content = Get-Content "docs\components\vitrine-veiculos-bff\index.md" -Raw -Encoding UTF8
    
    $body = @{
        title = "Vitrine BFF - Teste"
        text = $content
        collectionId = "d236ae05-812e-426a-a125-75653888903e"
        publish = $true
    }
    
    $response = Invoke-RestMethod -Uri "$ApiUrl/api/documents.create" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 30
    
    Write-Host "✅ Sucesso: vitrine-veiculos-bff criado" -ForegroundColor Green
    Write-Host "   ID: $($response.data.id)" -ForegroundColor White
    
    # Deletar o documento de teste
    $deleteBody = @{ id = $response.data.id }
    Invoke-RestMethod -Uri "$ApiUrl/api/documents.delete" -Headers $headers -Method Post -Body ($deleteBody | ConvertTo-Json) -TimeoutSec 10
    Write-Host "   🗑️ Documento de teste deletado" -ForegroundColor Yellow
    
} catch {
    Write-Host "❌ Erro: vitrine-veiculos-bff - $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        $responseBody = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($responseBody)
        $responseText = $reader.ReadToEnd()
        Write-Host "   Resposta: $responseText" -ForegroundColor Red
    }
}

# Testar versão simplificada do vitrine-veiculos-bff
Write-Host "`n3. Testando versão simplificada do vitrine-veiculos-bff..." -ForegroundColor Green
try {
    $simpleContent = @"
# Vitrine BFF - Teste Simplificado

Backend for Frontend que otimiza dados da vitrine para o frontend web.

## Descrição

Camada intermediária entre o frontend da vitrine e a API core.

## Características

- Agregação de Dados
- Cache Otimizado  
- Payload Otimizado
"@
    
    $body = @{
        title = "Vitrine BFF - Teste Simplificado"
        text = $simpleContent
        collectionId = "d236ae05-812e-426a-a125-75653888903e"
        publish = $true
    }
    
    $response = Invoke-RestMethod -Uri "$ApiUrl/api/documents.create" -Headers $headers -Method Post -Body ($body | ConvertTo-Json) -TimeoutSec 30
    
    Write-Host "✅ Sucesso: versão simplificada criada" -ForegroundColor Green
    Write-Host "   ID: $($response.data.id)" -ForegroundColor White
    
    # Deletar o documento de teste
    $deleteBody = @{ id = $response.data.id }
    Invoke-RestMethod -Uri "$ApiUrl/api/documents.delete" -Headers $headers -Method Post -Body ($deleteBody | ConvertTo-Json) -TimeoutSec 10
    Write-Host "   🗑️ Documento de teste deletado" -ForegroundColor Yellow
    
} catch {
    Write-Host "❌ Erro: versão simplificada - $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`nTeste concluido!" -ForegroundColor Cyan
