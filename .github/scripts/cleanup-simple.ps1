$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Limpando documentos..."

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $documents = $response.data
    Write-Host "Total: $($documents.Count) documentos"
    
    $deleted = 0
    foreach ($doc in $documents) {
        $deleteBody = @{
            id = $doc.id
            permanent = $true
        } | ConvertTo-Json
        
        try {
            $deleteResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.delete" -Headers $headers -Method Post -Body $deleteBody
            if ($deleteResponse.ok) {
                Write-Host "✅ $($doc.title)"
                $deleted++
            } else {
                Write-Host "❌ $($doc.title)"
            }
        } catch {
            Write-Host "❌ $($doc.title)"
        }
    }
    
    Write-Host "Deletados: $deleted"
} else {
    Write-Host "Erro ao listar"
}

Write-Host "Limpeza concluida!"
