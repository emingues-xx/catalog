$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Deletando documentos hierarquicamente..."

$body = '{"id": ""}'
$response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $body

if ($response.ok) {
    $docs = $response.data
    Write-Host "Total: $($docs.Count) documentos"
    
    $deleted = 0
    $maxRounds = 5
    
    for ($round = 1; $round -le $maxRounds; $round++) {
        Write-Host "Round $round"
        
        $toDelete = @()
        foreach ($doc in $docs) {
            $hasChildren = $false
            foreach ($other in $docs) {
                if ($other.parentDocumentId -eq $doc.id) {
                    $hasChildren = $true
                    break
                }
            }
            if (-not $hasChildren) {
                $toDelete += $doc
            }
        }
        
        if ($toDelete.Count -eq 0) {
            Write-Host "Nenhum documento sem filhos. Deletando restantes..."
            $toDelete = $docs
        }
        
        foreach ($doc in $toDelete) {
            $deleteBody = @{
                id = $doc.id
                permanent = $true
            } | ConvertTo-Json
            
            try {
                $deleteResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.delete" -Headers $headers -Method Post -Body $deleteBody
                if ($deleteResponse.ok) {
                    Write-Host "✅ $($doc.title)"
                    $deleted++
                    $docs = $docs | Where-Object { $_.id -ne $doc.id }
                } else {
                    Write-Host "❌ $($doc.title)"
                }
            } catch {
                Write-Host "❌ $($doc.title)"
            }
        }
        
        if ($docs.Count -eq 0) {
            break
        }
    }
    
    Write-Host "Deletados: $deleted"
} else {
    Write-Host "Erro ao listar"
}

Write-Host "Concluido!"
