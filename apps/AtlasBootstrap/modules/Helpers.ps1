function Test-Program {

    param(
        [Parameter(Mandatory)]
        [string]$Name
    )

    return [bool](Get-Command $Name -ErrorAction SilentlyContinue)

}