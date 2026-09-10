$ErrorActionPreference = 'Stop'
$exe = Join-Path $env:LOCALAPPDATA 'IndependentPythonEnv\OpenPyInProject.exe'
if (-not (Test-Path $exe)) {
    throw "Opener not found: $exe"
}

# 用项目环境打开 — code points only, so PowerShell 5 does not misread UTF-8 Chinese.
$menuName = -join @(
    [char]0x7528, [char]0x9879, [char]0x76EE, [char]0x73AF,
    [char]0x5883, [char]0x6253, [char]0x5F00
)

$icon = 'D:\Programs\Microsoft VS Code\Code.exe'
$command = '"' + $exe + '" "%1"'

function Set-ShellVerb($relativeKey) {
    $k = [Microsoft.Win32.Registry]::CurrentUser.CreateSubKey($relativeKey)
    $k.SetValue('', $menuName)
    $k.SetValue('MUIVerb', $menuName)
    $k.SetValue('Icon', $icon)
    $c = $k.CreateSubKey('command')
    $c.SetValue('', $command)
    $c.Close()
    $k.Close()
}

Set-ShellVerb 'Software\Classes\VSCode.py\shell\OpenWithProjectEnv'
Set-ShellVerb 'Software\Classes\Cursor.py\shell\OpenWithProjectEnv'
Set-ShellVerb 'Software\Classes\Python.File\shell\OpenWithProjectEnv'
Set-ShellVerb 'Software\Classes\SystemFileAssociations\.py\shell\OpenWithProjectEnv'

$star = [Microsoft.Win32.Registry]::CurrentUser.CreateSubKey('Software\Classes\*\shell\OpenWithProjectEnv')
$star.SetValue('', $menuName)
$star.SetValue('MUIVerb', $menuName)
$star.SetValue('Icon', $icon)
$star.SetValue('AppliesTo', 'System.FileExtension:=".py"')
$starCmd = $star.CreateSubKey('command')
$starCmd.SetValue('', $command)
$starCmd.Close()
$star.Close()

$app = [Microsoft.Win32.Registry]::CurrentUser.CreateSubKey('Software\Classes\Applications\OpenPyInProject.exe')
$app.SetValue('FriendlyAppName', $menuName)
$appOpen = $app.CreateSubKey('shell\open\command')
$appOpen.SetValue('', $command)
$appOpen.Close()
$types = $app.CreateSubKey('SupportedTypes')
$types.SetValue('.py', '')
$types.Close()
$app.Close()

$progids = [Microsoft.Win32.Registry]::CurrentUser.CreateSubKey('Software\Classes\.py\OpenWithProgids')
$progids.SetValue('IndependentPythonEnv.py', [byte[]]@(), [Microsoft.Win32.RegistryValueKind]::None)
$progids.Close()

$envProg = [Microsoft.Win32.Registry]::CurrentUser.CreateSubKey('Software\Classes\IndependentPythonEnv.py')
$envProg.SetValue('', $menuName)
$envOpen = $envProg.CreateSubKey('shell\open\command')
$envOpen.SetValue('', $command)
$envOpen.Close()
$envProg.Close()

$sendTo = Join-Path $env:APPDATA 'Microsoft\Windows\SendTo'
$lnkPath = Join-Path $sendTo ($menuName + '.lnk')
$shell = New-Object -ComObject WScript.Shell
Get-ChildItem -LiteralPath $sendTo -Filter *.lnk -ErrorAction SilentlyContinue | ForEach-Object {
    try {
        $existing = $shell.CreateShortcut($_.FullName)
        if ($existing.TargetPath -and ($existing.TargetPath -ieq $exe)) {
            Remove-Item -LiteralPath $_.FullName -Force
        }
    } catch {}
}
$lnk = $shell.CreateShortcut($lnkPath)
$lnk.TargetPath = $exe
$lnk.WindowStyle = 7
$lnk.IconLocation = $icon
$lnk.Description = $menuName
$lnk.Save()

Write-Host 'menu installed'
Write-Host "exe=$exe"
Write-Host "sendto=$lnkPath"
