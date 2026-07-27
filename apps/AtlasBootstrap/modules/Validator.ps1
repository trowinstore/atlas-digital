function Test-AtlasEnvironment {

    Write-Host ""
    Write-Host "Verificando ambiente..."
    Write-Host ""

    Test-Program "git"
    Test-Program "code"

    Write-Host ""
}