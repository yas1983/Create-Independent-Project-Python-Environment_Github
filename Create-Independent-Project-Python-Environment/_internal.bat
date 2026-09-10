@echo off
cd /d "%~dp0"

if exist "D:\Programs\anaconda\python.exe" (
  "D:\Programs\anaconda\python.exe" "%~dp0create_project.py"
  goto :eof
)

where python >nul 2>&1
if %errorlevel%==0 (
  python "%~dp0create_project.py"
  goto :eof
)

echo Python was not found. Install Python first. See Complete User Manual.md.
pause
