@echo off
setlocal
set "TARGET=%~dp0index.html"
if not exist "%TARGET%" (
  echo Could not find index.html next to this launcher.
  exit /b 1
)
start "" "%TARGET%"
