$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Testando migração para nova coleção..."

$newCollectionId = "5c78f84a-f721-47cc-a983-2eb05e6bf246"
$oldCollectionId = "e581b5ff-6e58-45ae-ac32-ac40bd83d8f7"

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $documents = $response.data
    Write-Host "Total de documentos: $($documents.Count)"
    
    $inNewCollection = 0
    $inOldCollection = 0
    
    foreach ($doc in $documents) {
        if ($doc.collectionId -eq $newCollectionId) {
            $inNewCollection++
            Write-Host "✅ $($doc.title) - Nova coleção"
        } elseif ($doc.collectionId -eq $oldCollectionId) {
            $inOldCollection++
            Write-Host "🔄 $($doc.title) - Coleção antiga"
        } else {
            Write-Host "❓ $($doc.title) - Outra coleção ($($doc.collectionId))"
        }
    }
    
    Write-Host ""
    Write-Host "📊 Resumo:"
    Write-Host "✅ Na nova coleção: $inNewCollection"
    Write-Host "🔄 Na coleção antiga: $inOldCollection"
    
} else {
    Write-Host "❌ Erro ao listar documentos: $($response.message)"
}

Write-Host ""
Write-Host "Teste concluído!"