# Teste de documentos públicos e readonly

$apiUrl = "https://outline-production-47e1.up.railway.app"
$apiToken = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"

$headers = @{
    'Authorization' = "Bearer $apiToken"
    'Content-Type' = 'application/json'
    'Accept' = 'application/json'
}

Write-Host "Teste de documentos públicos e readonly"

# Teste 1: Criar documento público
Write-Host "`n1. Criando documento público..."
try {
    $testData = @{
        title = "Teste Público - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
        text = "Este é um documento público de teste"
        publish = $true
        collectionId = "fdc96e70-5b1d-4de5-abca-09fc9749b543"
    } | ConvertTo-Json
    
    $response = Invoke-RestMethod -Uri "$apiUrl/api/documents.create" -Headers $headers -Method Post -Body $testData
    $docId = $response.data.id
    Write-Host "Documento público criado: $docId"
    
    # Teste 2: Configurar como readonly
    Write-Host "`n2. Configurando como readonly..."
    try {
        $readonlyData = @{
            id = $docId
            readonly = $true
        } | ConvertTo-Json
        
        $readonlyResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.update" -Headers $headers -Method Post -Body $readonlyData
        Write-Host "Documento configurado como readonly"
        
    } catch {
        Write-Host "ERRO ao configurar readonly: $($_.Exception.Message)"
    }
    
    # Teste 3: Verificar se aparece na listagem
    Write-Host "`n3. Verificando se aparece na listagem..."
    Start-Sleep -Seconds 2
    
    $data = '{"id": ""}'
    $response = Invoke-RestMethod -Uri "$apiUrl/api/documents.list" -Headers $headers -Method Post -Body $data
    $documents = $response.data
    
    $testDoc = $documents | Where-Object { $_.id -eq $docId }
    if ($testDoc) {
        Write-Host "OK - Documento encontrado na listagem"
        Write-Host "  Título: $($testDoc.title)"
        Write-Host "  Coleção: $($testDoc.collectionId)"
        Write-Host "  Público: $($testDoc.publishedAt)"
        Write-Host "  Readonly: $($testDoc.readonly)"
    } else {
        Write-Host "ERRO - Documento não encontrado na listagem"
    }
    
    # Teste 4: Deletar documento de teste
    Write-Host "`n4. Removendo documento de teste..."
    $deleteData = @{ id = $docId } | ConvertTo-Json
    $deleteResponse = Invoke-RestMethod -Uri "$apiUrl/api/documents.delete" -Headers $headers -Method Post -Body $deleteData
    Write-Host "Documento removido"
    
} catch {
    Write-Host "ERRO: $($_.Exception.Message)"
}

Write-Host "`nTeste finalizado!"
