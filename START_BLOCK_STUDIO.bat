@echo off
setlocal
cd /d "%~dp0"
set "VENV=%CD%\.venv-block-studio"

if not exist "%VENV%\Scripts\python.exe" (
  echo Creating Block Studio environment...
  py -3 -m venv "%VENV%" 2>nul
  if errorlevel 1 python -m venv "%VENV%"
  if errorlevel 1 goto :error
)

echo Installing local Block Studio packages...
"%VENV%\Scripts\python.exe" -m pip install --disable-pip-version-check -e "%CD%\capabilities\media-probe" -e "%CD%\apps\block-studio"
if errorlevel 1 goto :error

echo Opening Project Execution OS Block Studio...
"%VENV%\Scripts\python.exe" -m peos_block_studio
if errorlevel 1 goto :error
exit /b 0

:error
echo.
echo Block Studio could not start. Check Python and ffprobe installation.
pause
exit /b 1
