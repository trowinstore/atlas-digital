function Show-AtlasBanner {

    param(
        $Config
    )

    Clear-Host

    Write-Host ""
    Write-Host "===================================================="
    Write-Host ""
    Write-Host "              ATLAS FRAMEWORK"
    Write-Host ""
    Write-Host "            Bootstrap v$($Config.Project.Version)"
    Write-Host ""
    Write-Host "===================================================="
    Write-Host ""
    Write-Host $Config.Project.Name
    Write-Host ""
}


