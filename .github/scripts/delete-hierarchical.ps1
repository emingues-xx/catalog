$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Deletando documentos em ordem hierárquica..."

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $allDocuments = $response.data
    Write-Host "Total de documentos: $($allDocuments.Count)"
    
    # Função para deletar um documento
    function Delete-Document {
        param($docId, $docTitle)
        $deleteBody = @{
            id = $docId
            permanent = $true
        } | ConvertTo-Json
        
        try {
            $deleteResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.delete" -Headers $headers -Method Post -Body $deleteBody
            if ($deleteResponse.ok) {
                Write-Host "✅ Deletado: $docTitle"
                return $true
            } else {
                Write-Host "❌ Erro ao deletar: $docTitle - $($deleteResponse.message)"
                return $false
            }
        } catch {
            Write-Host "❌ Erro ao deletar: $docTitle - $($_.Exception.Message)"
            return $false
        }
    }
    
    # Função para encontrar documentos sem filhos
    function Get-LeafDocuments {
        param($documents)
        $leafDocs = @()
        foreach ($doc in $documents) {
            $hasChildren = $false
            foreach ($otherDoc in $documents) {
                if ($otherDoc.parentDocumentId -eq $doc.id) {
                    $hasChildren = $true
                    break
                }
            }
            if (-not $hasChildren) {
                $leafDocs += $doc
            }
        }
        return $leafDocs
    }
    
    $deletedCount = 0
    $maxIterations = 10  # Prevenir loop infinito
    $iteration = 0
    
    while ($allDocuments.Count -gt 0 -and $iteration -lt $maxIterations) {
        $iteration++
        Write-Host ""
        Write-Host "Iteração $iteration - Documentos restantes: $($allDocuments.Count)"
        
        # Encontrar documentos sem filhos (folhas)
        $leafDocs = Get-LeafDocuments $allDocuments
        Write-Host "Documentos sem filhos encontrados: $($leafDocs.Count)"
        
        if ($leafDocs.Count -eq 0) {
            Write-Host "⚠️ Nenhum documento sem filhos encontrado. Deletando todos os restantes..."
            # Se não há folhas, deletar todos os restantes
            foreach ($doc in $allDocuments) {
                if (Delete-Document $doc.id $doc.title) {
                    $deletedCount++
                }
            }
            break
        }
        
        # Deletar documentos sem filhos
        foreach ($doc in $leafDocs) {
            if (Delete-Document $doc.id $doc.title) {
                $deletedCount++
                # Remover da lista
                $allDocuments = $allDocuments | Where-Object { $_.id -ne $doc.id }
            }
        }
    }
    
    Write-Host ""
    Write-Host "📊 Resumo da limpeza hierárquica:"
    Write-Host "✅ Documentos deletados: $deletedCount"
    Write-Host "🔄 Iterações realizadas: $iteration"
    
} else {
    Write-Host "❌ Erro ao listar documentos: $($response.message)"
}

Write-Host ""
Write-Host "Limpeza hierárquica concluída!"
