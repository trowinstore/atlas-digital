# ==========================================
# Inicialização
# ==========================================

$Root = Split-Path -Parent $PSScriptRoot

# ==========================================
# Carregamento de módulos
# ==========================================

. "$Root\modules\Banner.ps1"
. "$Root\modules\Helpers.ps1"
. "$Root\modules\Logger.ps1"
. "$Root\modules\ConfigManager.ps1"
. "$Root\modules\Validator.ps1"

# ==========================================
# Execução
# ==========================================

Write-AtlasLog -Level INFO -Message "AtlasBootstrap iniciado."

$Config = Get-AtlasConfig


Show-AtlasBanner -Config $Config
Test-AtlasEnvironment

Write-AtlasLog -Level INFO -Message "Validação do ambiente concluída."