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

echo 找不到 Python。请先安装 Python。
pause
