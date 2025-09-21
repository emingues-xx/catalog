$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Verificando hierarquia dos documentos..."

$newCollectionId = "5c78f84a-f721-47cc-a983-2eb05e6bf246"

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $documents = $response.data | Where-Object { $_.collectionId -eq $newCollectionId }
    Write-Host "Documentos na nova coleção: $($documents.Count)"
    
    Write-Host ""
    Write-Host "=== DOCUMENTOS SEM PAI ==="
    foreach ($doc in $documents) {
        if (-not $doc.parentDocumentId) {
            Write-Host "📄 $($doc.title) (ID: $($doc.id))"
        }
    }
    
    Write-Host ""
    Write-Host "=== DOCUMENTOS COM PAI ==="
    foreach ($doc in $documents) {
        if ($doc.parentDocumentId) {
            $parent = $documents | Where-Object { $_.id -eq $doc.parentDocumentId }
            $parentTitle = if ($parent) { $parent.title } else { "Pai não encontrado" }
            Write-Host "👶 $($doc.title) -> Pai: $parentTitle"
        }
    }
    
    Write-Host ""
    Write-Host "=== DOCUMENTOS PAIS ==="
    foreach ($doc in $documents) {
        $children = $documents | Where-Object { $_.parentDocumentId -eq $doc.id }
        if ($children.Count -gt 0) {
            Write-Host "👨‍👩‍👧‍👦 $($doc.title) tem $($children.Count) filhos:"
            foreach ($child in $children) {
                Write-Host "  - $($child.title)"
            }
        }
    }
    
} else {
    Write-Host "❌ Erro: $($response.message)"
}
