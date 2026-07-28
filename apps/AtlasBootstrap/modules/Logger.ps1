function Write-AtlasLog {

    param(
        [Parameter(Mandatory)]
        [ValidateSet("INFO","WARNING","ERROR")]
        [string]$Level,

        [Parameter(Mandatory)]
        [string]$Message
    )

    $LogFolder = Join-Path $PSScriptRoot "..\logs"

    if (!(Test-Path $LogFolder)) {
        New-Item -ItemType Directory -Path $LogFolder | Out-Null
    }

    $LogFile = Join-Path $LogFolder "Atlas.log"

    $Time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

    Add-Content -Path $LogFile -Value "$Time [$Level] $Message"
}