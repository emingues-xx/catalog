# Testar nova coleção raiz

$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Testando nova coleção raiz..."

# Verificar se a nova coleção existe
$collectionId = "5c78f84a-f721-47cc-a983-2eb05e6bf246"

try {
    # Listar coleções
    $body = '{"id": ""}'
    $response = Invoke-RestMethod -Uri "$apiUrl/api/collections.list" -Headers $headers -Method Post -Body $body
    
    if ($response.ok) {
        $collections = $response.data
        Write-Host "Coleções encontradas: $($collections.Count)"
        
        $found = $false
        foreach ($col in $collections) {
            if ($col.id -eq $collectionId) {
                Write-Host "✅ Nova coleção encontrada: $($col.name) (ID: $($col.id))"
                $found = $true
                break
            }
        }
        
        if (-not $found) {
            Write-Host "❌ Nova coleção não encontrada: $collectionId"
            Write-Host "Coleções disponíveis:"
            foreach ($col in $collections) {
                Write-Host "  - $($col.name) (ID: $($col.id))"
            }
        }
    } else {
        Write-Host "❌ Erro ao listar coleções: $($response.message)"
    }
} catch {
    Write-Host "❌ Erro: $($_.Exception.Message)"
}

Write-Host ""
Write-Host "Teste concluído!"
