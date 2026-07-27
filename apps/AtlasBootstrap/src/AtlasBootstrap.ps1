# ==========================================
# Atlas Framework
# AtlasBootstrap v1.0
# Arquivo Principal
# ==========================================

# Caminho da pasta do script
$Root = Split-Path -Parent $PSScriptRoot

# Carrega o módulo Banner
. "$Root\modules\Banner.ps1"

. "$Root\modules\Helpers.ps1"

. "$Root\modules\Validator.ps1"

# Exibe o banner
Show-AtlasBanner
Test-AtlasEnvironment
