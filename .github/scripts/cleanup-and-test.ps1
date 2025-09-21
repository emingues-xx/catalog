$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Limpando todos os documentos..."

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $documents = $response.data
    Write-Host "Encontrados $($documents.Count) documentos para deletar"
    
    $deletedCount = 0
    foreach ($doc in $documents) {
        $deleteBody = @{
            id = $doc.id
            permanent = $true
        } | ConvertTo-Json
        
        try {
            $deleteResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.delete" -Headers $headers -Method Post -Body $deleteBody
            if ($deleteResponse.ok) {
                Write-Host "✅ Deletado: $($doc.title)"
                $deletedCount++
            } else {
                Write-Host "❌ Erro ao deletar: $($doc.title) - $($deleteResponse.message)"
            }
        } catch {
            Write-Host "❌ Erro ao deletar: $($doc.title) - $($_.Exception.Message)"
        }
    }
    
    Write-Host ""
    Write-Host "📊 Resumo da limpeza:"
    Write-Host "✅ Documentos deletados: $deletedCount"
    Write-Host "❌ Erros: $($documents.Count - $deletedCount)"
    
} else {
    Write-Host "❌ Erro ao listar documentos: $($response.message)"
}

Write-Host ""
Write-Host "Limpeza concluída!"
Write-Host "Agora faça um commit para testar a sincronização completa."
