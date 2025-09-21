$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Verificando hierarquia final..."

$newCollectionId = "5c78f84a-f721-47cc-a983-2eb05e6bf246"

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $documents = $response.data | Where-Object { $_.collectionId -eq $newCollectionId }
    Write-Host "Documentos na nova coleção: $($documents.Count)"
    
    Write-Host ""
    Write-Host "=== DOCUMENTOS SEM PAI (RAIZ) ==="
    foreach ($doc in $documents) {
        if (-not $doc.parentDocumentId) {
            Write-Host "📄 $($doc.title)"
        }
    }
    
    Write-Host ""
    Write-Host "=== HIERARQUIA COMPLETA ==="
    foreach ($doc in $documents) {
        if (-not $doc.parentDocumentId) {
            Write-Host "📁 $($doc.title)"
            $children = $documents | Where-Object { $_.parentDocumentId -eq $doc.id }
            foreach ($child in $children) {
                Write-Host "  └── $($child.title)"
                $grandchildren = $documents | Where-Object { $_.parentDocumentId -eq $child.id }
                foreach ($grandchild in $grandchildren) {
                    Write-Host "      └── $($grandchild.title)"
                }
            }
        }
    }
    
} else {
    Write-Host "❌ Erro: $($response.message)"
}
