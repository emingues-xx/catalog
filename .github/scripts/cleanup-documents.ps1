# Limpar todos os documentos do Outline

$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Limpando todos os documentos do Outline..."

try {
    # Listar todos os documentos
    $body = '{"id": ""}'
    $response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body
    
    if ($response.ok) {
        $documents = $response.data
        Write-Host "Encontrados $($documents.Count) documentos para deletar"
        
        foreach ($doc in $documents) {
            try {
                $deleteBody = @{
                    id = $doc.id
                    permanent = $true
                } | ConvertTo-Json
                
                $deleteResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.delete" -Headers $headers -Method Post -Body $deleteBody
                
                if ($deleteResponse.ok) {
                    Write-Host "✅ Documento '$($doc.title)' deletado com sucesso"
                } else {
                    Write-Host "❌ Erro ao deletar documento '$($doc.title)': $($deleteResponse.message)"
                }
            } catch {
                Write-Host "❌ Erro ao deletar documento '$($doc.title)': $($_.Exception.Message)"
            }
        }
    } else {
        Write-Host "❌ Erro ao listar documentos: $($response.message)"
    }
} catch {
    Write-Host "❌ Erro geral: $($_.Exception.Message)"
}

Write-Host ""
Write-Host "Limpeza concluída!"
Write-Host "Acesse o Outline: https://outline-production-47e1.up.railway.app"
