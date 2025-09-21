# Testar limpeza e sincronização

Write-Host "Testando limpeza hierárquica e sincronização..."

# Definir variáveis de ambiente
$env:OUTLINE_API_TOKEN = "ol_api_1QaafZhDnPSgs9bzU4vV4LpydZ9A6hVYdcZuCK"
$env:GITHUB_REPOSITORY = "emingues-xx/catalog"
$env:GITHUB_SHA = "main"
$env:CLEAN_BEFORE_SYNC = "true"

# Executar o script Python
try {
    python .github\scripts\sync_working.py
    Write-Host ""
    Write-Host "✅ Teste concluído!"
    Write-Host "Acesse o Outline: https://outline-production-47e1.up.railway.app"
} catch {
    Write-Host "❌ Erro ao executar: $($_.Exception.Message)"
}
