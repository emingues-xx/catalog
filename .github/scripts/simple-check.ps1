$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $documents = $response.data
    Write-Host "Total: $($documents.Count) documentos"
    
    $newCollectionId = "5c78f84a-f721-47cc-a983-2eb05e6bf246"
    $oldCollectionId = "e581b5ff-6e58-45ae-ac32-ac40bd83d8f7"
    
    $inNew = 0
    $inOld = 0
    
    foreach ($doc in $documents) {
        if ($doc.collectionId -eq $newCollectionId) {
            $inNew++
        } elseif ($doc.collectionId -eq $oldCollectionId) {
            $inOld++
        }
    }
    
    Write-Host "Nova coleção: $inNew"
    Write-Host "Coleção antiga: $inOld"
} else {
    Write-Host "Erro ao listar documentos"
}
