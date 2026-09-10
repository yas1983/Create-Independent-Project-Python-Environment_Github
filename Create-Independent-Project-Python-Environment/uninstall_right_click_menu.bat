@echo off
reg delete "HKCU\Software\Classes\Python.File\shell\OpenWithProjectEnv" /f >nul 2>&1
reg delete "HKCU\Software\Classes\VSCode.py\shell\OpenWithProjectEnv" /f >nul 2>&1
reg delete "HKCU\Software\Classes\Cursor.py\shell\OpenWithProjectEnv" /f >nul 2>&1
reg delete "HKCU\Software\Classes\SystemFileAssociations\.py\shell\OpenWithProjectEnv" /f >nul 2>&1
reg delete "HKCU\Software\Classes\*\shell\OpenWithProjectEnv" /f >nul 2>&1
reg delete "HKCU\Software\Classes\Applications\OpenPyInProject.exe" /f >nul 2>&1
reg delete "HKCU\Software\Classes\IndependentPythonEnv.py" /f >nul 2>&1
del /f /q "%APPDATA%\Microsoft\Windows\SendTo\用项目环境打开.lnk" >nul 2>&1
echo Removed the right-click menu "用项目环境打开".
echo The opener file is still in AppData if you want to delete it by hand:
echo %LOCALAPPDATA%\IndependentPythonEnv\OpenPyInProject.exe
pause
