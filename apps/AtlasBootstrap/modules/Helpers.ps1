function Test-Program {

    param(
        [string]$Name
    )

    if (Get-Command $Name -ErrorAction SilentlyContinue) {
        Write-Host ("[OK] {0} encontrado." -f $Name)
    }
    else {
        Write-Host ("[ERRO] {0} não encontrado." -f $Name)
    }
}