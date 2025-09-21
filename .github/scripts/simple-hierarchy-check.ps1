$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

$newCollectionId = "5c78f84a-f721-47cc-a983-2eb05e6bf246"

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $documents = $response.data | Where-Object { $_.collectionId -eq $newCollectionId }
    Write-Host "Documentos na nova coleção: $($documents.Count)"
    
    Write-Host ""
    Write-Host "Documentos sem pai (raiz):"
    foreach ($doc in $documents) {
        if (-not $doc.parentDocumentId) {
            Write-Host "- $($doc.title)"
        }
    }
    
    Write-Host ""
    Write-Host "Documentos com pai:"
    foreach ($doc in $documents) {
        if ($doc.parentDocumentId) {
            $parent = $documents | Where-Object { $_.id -eq $doc.parentDocumentId }
            $parentTitle = if ($parent) { $parent.title } else { "Pai não encontrado" }
            Write-Host "- $($doc.title) -> $parentTitle"
        }
    }
} else {
    Write-Host "Erro ao listar documentos"
}
