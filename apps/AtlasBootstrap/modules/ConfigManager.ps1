function Get-AtlasConfig {

    $ConfigFile = Join-Path $PSScriptRoot "..\config\config.json"

    if (!(Test-Path $ConfigFile)) {

        Write-AtlasLog -Level ERROR -Message "Arquivo config.json não encontrado."

        throw "Arquivo config.json não encontrado."
    }

    Write-AtlasLog -Level INFO -Message "Arquivo de configuração carregado."

    return Get-Content $ConfigFile -Raw | ConvertFrom-Json
}