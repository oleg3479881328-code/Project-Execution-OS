[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$packageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$installRoot = Join-Path $env:LOCALAPPDATA 'TikTokResearchSorterLauncher'
$desktop = [Environment]::GetFolderPath('Desktop')
$shortcutPath = Join-Path $desktop 'TikTok Sorter — обновить и запустить.lnk'

New-Item -ItemType Directory -Force -Path $installRoot | Out-Null
Copy-Item (Join-Path $packageRoot 'Update-and-Launch-TikTok-Sorter.ps1') $installRoot -Force
Copy-Item (Join-Path $packageRoot 'Update-and-Launch-TikTok-Sorter.cmd') $installRoot -Force

$target = Join-Path $installRoot 'Update-and-Launch-TikTok-Sorter.cmd'
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $target
$shortcut.WorkingDirectory = $installRoot
$shortcut.Description = 'Обновить TikTok Research Sorter из GitHub и открыть отдельный Chrome'
$shortcut.Save()

Write-Host 'Ярлык создан на рабочем столе:' -ForegroundColor Green
Write-Host $shortcutPath -ForegroundColor Cyan
Write-Host 'Сейчас выполняется первый запуск. Он может занять несколько минут.' -ForegroundColor Yellow
& $target
