function Test-AtlasEnvironment {

    Write-Host ""
    Write-Host "Verificando ambiente..."
    Write-Host ""

    $Programs = @(
        "git",
        "code"
    )

    foreach ($Program in $Programs) {

        if (Test-Program $Program) {

            Write-Host "[OK] $Program encontrado."
            Write-AtlasLog -Level INFO -Message "Programa '$Program' encontrado."

        }
        else {

            Write-Host "[ERRO] $Program não encontrado."
            Write-AtlasLog -Level ERROR -Message "Programa '$Program' não encontrado."

        }

    }

    Write-Host ""
}