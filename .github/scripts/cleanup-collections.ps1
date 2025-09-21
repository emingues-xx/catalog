# Script para deletar todas as coleções atuais do Outline (exceto a raiz)

$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Limpando coleções do Outline..."
Write-Host ""

try {
    # Listar todas as coleções
    $listBody = '{"id": ""}'
    $listResponse = Invoke-RestMethod -Uri "$apiUrl/api/collections.list" -Headers $headers -Method Post -Body $listBody
    
    if ($listResponse.ok) {
        $collections = $listResponse.data
        Write-Host "Encontradas $($collections.Count) coleções:"
        
        foreach ($col in $collections) {
            Write-Host "  - $($col.name) (ID: $($col.id), Parent: $($col.parentId))"
        }
        
        Write-Host ""
        Write-Host "Deletando coleções (exceto a raiz)..."
        
        foreach ($col in $collections) {
            # Pular a coleção raiz
            if ($col.id -eq "e581b5ff-6e58-45ae-ac32-ac40bd83d8f7") {
                Write-Host "Mantendo coleção raiz: $($col.name)"
                continue
            }
            
            try {
                $deleteBody = @{
                    id = $col.id
                } | ConvertTo-Json
                
                $deleteResponse = Invoke-RestMethod -Uri "$apiUrl/api/collections.delete" -Headers $headers -Method Post -Body $deleteBody
                
                if ($deleteResponse.ok) {
                    Write-Host "Coleção '$($col.name)' deletada com sucesso"
                } else {
                    Write-Host "Erro ao deletar coleção '$($col.name)': $($deleteResponse.error)"
                }
            } catch {
                Write-Host "Erro ao deletar coleção '$($col.name)': $($_.Exception.Message)"
            }
        }
        
        Write-Host ""
        Write-Host "Verificando coleções restantes..."
        
        # Listar coleções restantes
        $finalResponse = Invoke-RestMethod -Uri "$apiUrl/api/collections.list" -Headers $headers -Method Post -Body $listBody
        
        if ($finalResponse.ok) {
            $remainingCollections = $finalResponse.data
            Write-Host "Coleções restantes: $($remainingCollections.Count)"
            
            foreach ($col in $remainingCollections) {
                Write-Host "  - $($col.name) (ID: $($col.id))"
            }
        }
        
    } else {
        Write-Host "Erro ao listar coleções: $($listResponse.error)"
    }
    
} catch {
    Write-Host "Erro geral: $($_.Exception.Message)"
}

Write-Host ""
Write-Host "Limpeza concluída!"
Write-Host "Acesse o Outline: https://outline-production-47e1.up.railway.app"
