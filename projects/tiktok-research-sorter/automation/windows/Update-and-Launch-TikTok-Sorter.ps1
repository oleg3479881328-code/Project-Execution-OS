[CmdletBinding()]
param(
  [string]$Branch = $(if ($env:TRS_GITHUB_BRANCH) { $env:TRS_GITHUB_BRANCH } else { 'agent/tiktok-research-sorter-mvp' }),

  # Testability flags
  [switch]$DryRun,
  [switch]$SkipLaunch,
  [string]$LocalSource = $(if ($env:TRS_LOCAL_SOURCE) { $env:TRS_LOCAL_SOURCE } else { '' })
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$RepoOwner = 'oleg3479881328-code'
$RepoName = 'Project-Execution-OS'
$ProjectRelativePath = 'projects\tiktok-research-sorter'
$WorkRoot = Join-Path $env:LOCALAPPDATA 'TikTokResearchSorterDev'
$SourceRoot = Join-Path $WorkRoot 'source'
$ChromeProfileRoot = Join-Path $WorkRoot 'chrome-profile'
$LogPath = Join-Path $WorkRoot 'launcher.log'
$TempRoot = Join-Path $env:TEMP ("TikTokResearchSorter-" + [Guid]::NewGuid().ToString('N'))

New-Item -ItemType Directory -Force -Path $WorkRoot | Out-Null
Start-Transcript -Path $LogPath -Append | Out-Null

function Write-Step([string]$Message) {
  Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Refresh-ProcessPath {
  $machine = [Environment]::GetEnvironmentVariable('Path', 'Machine')
  $user = [Environment]::GetEnvironmentVariable('Path', 'User')
  $env:Path = "$machine;$user"
}

function Ensure-Node {
  $nodeCommand = Get-Command node.exe -ErrorAction SilentlyContinue
  $major = 0
  if ($nodeCommand) {
    $versionText = (& node.exe --version).TrimStart('v')
    $major = [int]($versionText.Split('.')[0])
  }

  if (-not $nodeCommand -or $major -lt 20) {
    Write-Step 'Устанавливаю Node.js LTS (нужно только один раз)'
    $winget = Get-Command winget.exe -ErrorAction SilentlyContinue
    if (-not $winget) {
      throw 'Node.js 20+ не найден, а winget недоступен. Установите Node.js LTS с nodejs.org и запустите ярлык снова.'
    }
    & winget.exe install --id OpenJS.NodeJS.LTS -e --accept-package-agreements --accept-source-agreements
    if ($LASTEXITCODE -ne 0) {
      throw "winget не смог установить Node.js. Код: $LASTEXITCODE"
    }
    Refresh-ProcessPath
  }

  if (-not (Get-Command node.exe -ErrorAction SilentlyContinue)) {
    throw 'Node.js установлен, но ещё не появился в PATH. Перезагрузите Windows и запустите ярлык снова.'
  }
}

function Find-Chrome {
  $candidates = @(
    (Join-Path $env:ProgramFiles 'Google\Chrome\Application\chrome.exe'),
    (Join-Path ${env:ProgramFiles(x86)} 'Google\Chrome\Application\chrome.exe'),
    (Join-Path $env:LOCALAPPDATA 'Google\Chrome\Application\chrome.exe')
  ) | Where-Object { $_ -and (Test-Path $_) }

  $chrome = $candidates | Select-Object -First 1
  if (-not $chrome) {
    throw 'Google Chrome не найден. Установите Chrome и запустите ярлык снова.'
  }
  return $chrome
}

try {
  # ---- Dry-Run: только показать, что будет сделано ----
  if ($DryRun) {
    Write-Step "СУХОЙ ПРОГОН (DryRun). Реальные операции выполняться не будут."
    Write-Host "  Branch:         $Branch" -ForegroundColor Gray
    Write-Host "  WorkRoot:       $WorkRoot" -ForegroundColor Gray
    Write-Host "  SourceRoot:     $SourceRoot" -ForegroundColor Gray
    Write-Host "  ChromeProfile:  $ChromeProfileRoot" -ForegroundColor Gray
    Write-Host "  SkipLaunch:     $SkipLaunch" -ForegroundColor Gray
    Write-Host "  LocalSource:    $(if ($LocalSource) { $LocalSource } else { '(не указан — будет загрузка с GitHub)' })" -ForegroundColor Gray
    Write-Host "`nDryRun завершён. Никаких изменений не внесено." -ForegroundColor Green
    return
  }

  # ---- Получение исходников ----
  if ($LocalSource) {
    Write-Step "Использую локальный источник: $LocalSource"
    $projectSource = Get-Item -Path $LocalSource -ErrorAction Stop
    if (-not (Test-Path (Join-Path $projectSource.FullName 'package.json'))) {
      throw "Локальный источник не содержит package.json: $LocalSource"
    }
  } else {
    Write-Step "Проверяю обновления из GitHub: $Branch"
    New-Item -ItemType Directory -Force -Path $TempRoot | Out-Null
    $archivePath = Join-Path $TempRoot 'source.zip'
    $extractRoot = Join-Path $TempRoot 'extracted'
    $archiveUrl = "https://codeload.github.com/$RepoOwner/$RepoName/zip/refs/heads/$Branch"
    Invoke-WebRequest -Uri $archiveUrl -OutFile $archivePath -UseBasicParsing
    Expand-Archive -Path $archivePath -DestinationPath $extractRoot -Force

    $projectSource = Get-ChildItem -Path $extractRoot -Directory -Recurse |
      Where-Object { $_.FullName.EndsWith($ProjectRelativePath, [StringComparison]::OrdinalIgnoreCase) } |
      Select-Object -First 1
    if (-not $projectSource) {
      throw "В скачанном архиве не найден $ProjectRelativePath"
    }
  }

  Write-Step 'Обновляю локальную рабочую копию'
  New-Item -ItemType Directory -Force -Path $SourceRoot | Out-Null
  & robocopy.exe $projectSource.FullName $SourceRoot /MIR /XD node_modules .output .wxt /XF launcher.log /NFL /NDL /NJH /NJS /NP | Out-Null
  if ($LASTEXITCODE -gt 7) {
    throw "robocopy завершился с ошибкой $LASTEXITCODE"
  }

  Ensure-Node
  Push-Location $SourceRoot
  try {
    $lockPath = Join-Path $SourceRoot 'package-lock.json'
    $hashPath = Join-Path $WorkRoot 'package-lock.sha256'
    if (-not (Test-Path $lockPath)) {
      Write-Step 'Создаю lock-файл и устанавливаю зависимости'
      & npm.cmd install --no-audit --no-fund
      if ($LASTEXITCODE -ne 0) { throw "npm install завершился с ошибкой $LASTEXITCODE" }
    }

    $currentHash = (Get-FileHash $lockPath -Algorithm SHA256).Hash
    $storedHash = if (Test-Path $hashPath) { (Get-Content $hashPath -Raw).Trim() } else { '' }

    if (-not (Test-Path (Join-Path $SourceRoot 'node_modules')) -or $currentHash -ne $storedHash) {
      Write-Step 'Устанавливаю или обновляю зависимости'
      & npm.cmd ci --no-audit --no-fund
      if ($LASTEXITCODE -ne 0) { throw "npm ci завершился с ошибкой $LASTEXITCODE" }
      Set-Content -Path $hashPath -Value $currentHash -Encoding ASCII
    } else {
      Write-Step 'Зависимости не изменились'
    }

    Write-Step 'Собираю последнюю версию расширения'
    & npm.cmd run build
    if ($LASTEXITCODE -ne 0) { throw "npm run build завершился с ошибкой $LASTEXITCODE" }
  }
  finally {
    Pop-Location
  }

  $extensionRoot = Join-Path $SourceRoot '.output\chrome-mv3'
  $manifestPath = Join-Path $extensionRoot 'manifest.json'
  if (-not (Test-Path $manifestPath)) {
    throw "Сборка завершена, но manifest.json не найден: $manifestPath"
  }

  # ---- Launch (пропускается если SkipLaunch) ----
  if (-not $SkipLaunch) {
    $chromePath = Find-Chrome
    Write-Step 'Перезапускаю отдельное окно Chrome с новой версией'
    Get-CimInstance Win32_Process -Filter "Name='chrome.exe'" -ErrorAction SilentlyContinue |
      Where-Object { $_.CommandLine -and $_.CommandLine.Contains($ChromeProfileRoot) } |
      ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
    Start-Sleep -Milliseconds 700

    New-Item -ItemType Directory -Force -Path $ChromeProfileRoot | Out-Null
    $arguments = @(
      "--user-data-dir=`"$ChromeProfileRoot`"",
      "--disable-extensions-except=`"$extensionRoot`"",
      "--load-extension=`"$extensionRoot`"",
      '--no-first-run',
      '--no-default-browser-check',
      'https://www.tiktok.com/'
    )
    Start-Process -FilePath $chromePath -ArgumentList $arguments

    Write-Host "`nГотово. Открыт отдельный Chrome с последней версией TikTok Research Sorter." -ForegroundColor Green
    Write-Host "При первом запуске войдите в TikTok и закрепите значок расширения. Этот профиль сохранится." -ForegroundColor Yellow
  } else {
    Write-Step "SkipLaunch — Chrome не запущен."
    Write-Host "Сборка готова: $extensionRoot" -ForegroundColor Green
  }
}
catch {
  Write-Host "`nОШИБКА: $($_.Exception.Message)" -ForegroundColor Red
  Write-Host "Журнал: $LogPath" -ForegroundColor Yellow
  Read-Host 'Нажмите Enter, чтобы закрыть окно'
  exit 1
}
finally {
  if (Test-Path $TempRoot) { Remove-Item $TempRoot -Recurse -Force -ErrorAction SilentlyContinue }
  Stop-Transcript -ErrorAction SilentlyContinue | Out-Null
}
