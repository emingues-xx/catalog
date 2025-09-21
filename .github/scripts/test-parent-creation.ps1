# Testar criação de documento pai vazio

$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Testando criação de documento pai vazio..."

# Testar criação de documento pai "Sistemas"
$parentTitle = "Sistemas"
$collectionId = "e581b5ff-6e58-45ae-ac32-ac40bd83d8f7"
$emptyContent = "# $parentTitle`n`n*Documento pai criado automaticamente*"

$data = @{
    title = $parentTitle
    text = $emptyContent
    publish = $true
    collectionId = $collectionId
} | ConvertTo-Json

try {
    Write-Host "Criando documento pai: $parentTitle"
    $response = Invoke-RestMethod -Uri "$apiUrl/api/documents.create" -Headers $headers -Method Post -Body $data
    
    if ($response.ok) {
        $docId = $response.data.id
        Write-Host "✅ Documento pai '$parentTitle' criado com sucesso (ID: $docId)"
        
        # Tornar readonly
        $readonlyData = @{
            id = $docId
            readonly = $true
        } | ConvertTo-Json
        
        $readonlyResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.update" -Headers $headers -Method Post -Body $readonlyData
        
        if ($readonlyResponse.ok) {
            Write-Host "✅ Documento pai '$parentTitle' configurado como readonly"
        } else {
            Write-Host "⚠️ Erro ao configurar readonly: $($readonlyResponse.message)"
        }
    } else {
        Write-Host "❌ Erro ao criar documento pai: $($response.message)"
    }
} catch {
    Write-Host "❌ Erro: $($_.Exception.Message)"
}

Write-Host ""
Write-Host "Teste concluído!"
Write-Host "Acesse o Outline: https://outline-production-47e1.up.railway.app"
