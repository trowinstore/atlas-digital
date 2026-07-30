function Start-AtlasWorkspace {

    Write-Host ""
    Write-Host "Preparando ambiente de trabalho..."
    Write-Host ""

    Write-AtlasLog -Level INFO -Message "Workspace iniciado."

    $Config = Get-AtlasConfig

    Write-Host ""
    Write-Host "===== DEBUG CONFIG ====="
    $Config | ConvertTo-Json -Depth 5
    Write-Host "========================"
    Write-Host ""

    foreach ($Application in $Config.Workspace.Applications) {

        Write-Host "[INFO] Abrindo $Application..."

        Start-Process $Application

        Write-AtlasLog -Level INFO -Message "Aplicação '$Application' iniciada."
    }

    foreach ($Website in $Config.Workspace.Websites) {

        Write-Host "[INFO] Abrindo $Website..."

        Start-Process $Website

        Write-AtlasLog -Level INFO -Message "Website '$Website' aberto."

}


}