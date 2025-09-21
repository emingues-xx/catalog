# Script para deletar todos os documentos atuais do Outline

$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Limpando documentos do Outline..."
Write-Host ""

try {
    # Listar todos os documentos
    $listBody = '{"id": ""}'
    $listResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $listBody
    
    if ($listResponse.ok) {
        $documents = $listResponse.data
        Write-Host "Encontrados $($documents.Count) documentos:"
        
        foreach ($doc in $documents) {
            Write-Host "  - $($doc.title) (ID: $($doc.id))"
        }
        
        Write-Host ""
        Write-Host "Deletando documentos..."
        
        foreach ($doc in $documents) {
            try {
                $deleteBody = @{
                    id = $doc.id
                } | ConvertTo-Json
                
                $deleteResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.delete" -Headers $headers -Method Post -Body $deleteBody
                
                if ($deleteResponse.ok) {
                    Write-Host "Documento '$($doc.title)' deletado com sucesso"
                } else {
                    Write-Host "Erro ao deletar documento '$($doc.title)': $($deleteResponse.error)"
                }
            } catch {
                Write-Host "Erro ao deletar documento '$($doc.title)': $($_.Exception.Message)"
            }
        }
        
        Write-Host ""
        Write-Host "Verificando documentos restantes..."
        
        # Listar documentos restantes
        $finalResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $listBody
        
        if ($finalResponse.ok) {
            $remainingDocuments = $finalResponse.data
            Write-Host "Documentos restantes: $($remainingDocuments.Count)"
            
            foreach ($doc in $remainingDocuments) {
                Write-Host "  - $($doc.title) (ID: $($doc.id))"
            }
        }
        
    } else {
        Write-Host "Erro ao listar documentos: $($listResponse.error)"
    }
    
} catch {
    Write-Host "Erro geral: $($_.Exception.Message)"
}

Write-Host ""
Write-Host "Limpeza de documentos concluída!"
Write-Host "Acesse o Outline: https://outline-production-47e1.up.railway.app"
