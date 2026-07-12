[CmdletBinding()]
param(
  [string]$Branch = $(if ($env:TRS_GITHUB_BRANCH) { $env:TRS_GITHUB_BRANCH } else { 'main' }),
  [switch]$DryRun,
  [switch]$SkipLaunch,
  [switch]$NonInteractive,
  [string]$LocalSource = $(if ($env:TRS_LOCAL_SOURCE) { $env:TRS_LOCAL_SOURCE } else { '' })
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$RepoOwner = 'oleg3479881328-code'
$RepoName = 'Project-Execution-OS'
$ProjectRelativePath = 'projects\tiktok-research-sorter'
$LocalAppData = if ($env:LOCALAPPDATA) { $env:LOCALAPPDATA } else { Join-Path $HOME 'AppData\Local' }
$WorkRoot = Join-Path $LocalAppData 'TikTokResearchSorterDev'
$SourceRoot = Join-Path $WorkRoot 'source'
$PreviousRoot = Join-Path $WorkRoot 'previous'
$CandidateRoot = Join-Path $WorkRoot ("candidate-" + [Guid]::NewGuid().ToString('N'))
$ChromeProfileRoot = Join-Path $WorkRoot 'chrome-profile'
$LogPath = Join-Path $WorkRoot 'launcher.log'
$TempRoot = Join-Path $env:TEMP ("TikTokResearchSorter-" + [Guid]::NewGuid().ToString('N'))
$TranscriptStarted = $false

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
      throw 'Node.js 20+ не найден, а winget недоступен. Установите Node.js LTS и запустите ярлык снова.'
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
    (Join-Path $LocalAppData 'Google\Chrome\Application\chrome.exe')
  ) | Where-Object { $_ -and (Test-Path $_) }

  $chrome = $candidates | Select-Object -First 1
  if (-not $chrome) {
    throw 'Google Chrome не найден. Установите Chrome и запустите ярлык снова.'
  }
  return $chrome
}

function Stop-DedicatedChrome {
  Get-CimInstance Win32_Process -Filter "Name='chrome.exe'" -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -and $_.CommandLine.Contains($ChromeProfileRoot) } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
  Start-Sleep -Milliseconds 700
}

if ($DryRun) {
  Write-Step 'СУХОЙ ПРОГОН (DryRun). Реальные операции выполняться не будут.'
  Write-Host "  Branch:         $Branch" -ForegroundColor Gray
  Write-Host "  WorkRoot:       $WorkRoot" -ForegroundColor Gray
  Write-Host "  SourceRoot:     $SourceRoot" -ForegroundColor Gray
  Write-Host "  ChromeProfile:  $ChromeProfileRoot" -ForegroundColor Gray
  Write-Host "  SkipLaunch:     $SkipLaunch" -ForegroundColor Gray
  Write-Host "  LocalSource:    $(if ($LocalSource) { $LocalSource } else { '(не указан — будет загрузка с GitHub)' })" -ForegroundColor Gray
  Write-Host "`nDryRun завершён. Никаких файлов и папок не создано." -ForegroundColor Green
  exit 0
}

try {
  New-Item -ItemType Directory -Force -Path $WorkRoot | Out-Null
  try {
    Start-Transcript -Path $LogPath -Append | Out-Null
    $TranscriptStarted = $true
  } catch {
    Write-Warning "Не удалось запустить журнал: $($_.Exception.Message)"
  }

  New-Item -ItemType Directory -Force -Path $CandidateRoot | Out-Null

  if ($LocalSource) {
    Write-Step "Использую локальный источник: $LocalSource"
    $projectSource = Get-Item -LiteralPath $LocalSource -ErrorAction Stop
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

  Write-Step 'Готовлю изолированную кандидатную сборку'
  & robocopy.exe $projectSource.FullName $CandidateRoot /MIR /XD node_modules .output .wxt /XF launcher.log /NFL /NDL /NJH /NJS /NP | Out-Null
  $robocopyCode = $LASTEXITCODE
  if ($robocopyCode -gt 7) {
    throw "robocopy завершился с ошибкой $robocopyCode"
  }

  Ensure-Node
  Push-Location $CandidateRoot
  try {
    $lockPath = Join-Path $CandidateRoot 'package-lock.json'
    if (-not (Test-Path $lockPath)) {
      throw 'В проекте отсутствует package-lock.json. Обновление остановлено до воспроизводимой сборки.'
    }

    Write-Step 'Устанавливаю зависимости из lock-файла'
    & npm.cmd ci --no-audit --no-fund
    if ($LASTEXITCODE -ne 0) { throw "npm ci завершился с ошибкой $LASTEXITCODE" }

    Write-Step 'Проверяю TypeScript'
    & npm.cmd run check
    if ($LASTEXITCODE -ne 0) { throw "npm run check завершился с ошибкой $LASTEXITCODE" }

    Write-Step 'Запускаю тесты'
    & npm.cmd test
    if ($LASTEXITCODE -ne 0) { throw "npm test завершился с ошибкой $LASTEXITCODE" }

    Write-Step 'Собираю расширение'
    & npm.cmd run build
    if ($LASTEXITCODE -ne 0) { throw "npm run build завершился с ошибкой $LASTEXITCODE" }
  }
  finally {
    Pop-Location
  }

  $candidateExtensionRoot = Join-Path $CandidateRoot '.output\chrome-mv3'
  $candidateManifestPath = Join-Path $candidateExtensionRoot 'manifest.json'
  if (-not (Test-Path $candidateManifestPath)) {
    throw "Сборка завершена, но manifest.json не найден: $candidateManifestPath"
  }
  $null = Get-Content $candidateManifestPath -Raw | ConvertFrom-Json

  if (-not $SkipLaunch) {
    Write-Step 'Закрываю только специальное окно Chrome'
    Stop-DedicatedChrome
  }

  Write-Step 'Переключаюсь на проверенную сборку'
  if (Test-Path $PreviousRoot) {
    Remove-Item $PreviousRoot -Recurse -Force
  }

  $movedCurrent = $false
  try {
    if (Test-Path $SourceRoot) {
      Move-Item -LiteralPath $SourceRoot -Destination $PreviousRoot
      $movedCurrent = $true
    }
    Move-Item -LiteralPath $CandidateRoot -Destination $SourceRoot
  } catch {
    if (-not (Test-Path $SourceRoot) -and $movedCurrent -and (Test-Path $PreviousRoot)) {
      Move-Item -LiteralPath $PreviousRoot -Destination $SourceRoot -ErrorAction SilentlyContinue
    }
    throw
  }

  $extensionRoot = Join-Path $SourceRoot '.output\chrome-mv3'

  if ($SkipLaunch) {
    Write-Step 'SkipLaunch — Chrome не запущен.'
    Write-Host "Проверенная сборка готова: $extensionRoot" -ForegroundColor Green
  } else {
    $chromePath = Find-Chrome
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
    Write-Host "`nГотово. Открыт отдельный Chrome с проверенной версией TikTok Research Sorter." -ForegroundColor Green
    Write-Host 'Предыдущая рабочая версия сохранена в папке previous для отката.' -ForegroundColor Yellow
  }
}
catch {
  Write-Host "`nОШИБКА: $($_.Exception.Message)" -ForegroundColor Red
  Write-Host "Рабочая версия не заменена. Журнал: $LogPath" -ForegroundColor Yellow
  if (-not $NonInteractive -and -not $env:CI) {
    Read-Host 'Нажмите Enter, чтобы закрыть окно'
  }
  exit 1
}
finally {
  if (Test-Path $TempRoot) { Remove-Item $TempRoot -Recurse -Force -ErrorAction SilentlyContinue }
  if (Test-Path $CandidateRoot) { Remove-Item $CandidateRoot -Recurse -Force -ErrorAction SilentlyContinue }
  if ($TranscriptStarted) { Stop-Transcript -ErrorAction SilentlyContinue | Out-Null }
}
