"""Green edition V0.02: name a folder, create that project's Python environment, optional per-project .py switch."""

import os
import shutil
import subprocess
import sys
import winreg
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

FORBIDDEN = '\\/:*?"<>|'
DEFAULT_PARENT = Path(r"D:\vibecoding\cursor\CursorProjects")
APP_VERSION = "V0.02"
WINDOW_TITLE = "Create Independent Project Python Environment " + APP_VERSION
MARKER_NAME = "use_project_env.on"
ENABLE_BAT_NAME = "启用：双击用本环境.bat"
DISABLE_BAT_NAME = "关闭：双击用系统 Python.bat"
APPDATA_DIR = Path(os.environ.get("LOCALAPPDATA", "")) / "IndependentPythonEnv"
OPENER_NAME = "OpenPyInProject.exe"
VSCODE_SETTINGS = """{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.terminal.executeInFileDir": true,
  "terminal.integrated.cwd": "${workspaceFolder}"
}
"""


def tool_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(getattr(sys, "_MEIPASS", Path(sys.executable).parent))
    return Path(__file__).resolve().parent


def resolve_python() -> str:
    """venv needs a real python.exe, not this program when it is packed as .exe."""
    if not getattr(sys, "frozen", False):
        return sys.executable

    anaconda = Path(r"D:\Programs\anaconda\python.exe")
    if anaconda.is_file():
        return str(anaconda)

    which = shutil.which("python")
    if which:
        path = Path(which)
        if path.is_file() and "windowsapps" not in str(path).lower():
            return str(path)

    py_launcher = shutil.which("py")
    if py_launcher:
        return py_launcher

    raise ValueError(
        "Python was not found on this computer.\n"
        "Install Python first (see Complete User Manual.md), then try again."
    )


def compile_opener(dest: Path) -> None:
    src = tool_dir() / "open_py_in_project.cs"
    if not src.is_file():
        raise ValueError("Missing open_py_in_project.cs; cannot build the opener.")
    ps = (
        "$src = Get-Content -Raw -LiteralPath "
        + _ps_quote(str(src))
        + "; Add-Type -TypeDefinition $src -ReferencedAssemblies @('System.dll','System.Windows.Forms.dll','System.Drawing.dll') "
        "-OutputAssembly "
        + _ps_quote(str(dest))
        + " -OutputType WindowsApplication -ErrorAction Stop"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0 or not dest.is_file():
        raise ValueError(
            "Could not build the opener:\n" + (result.stderr or result.stdout or "Unknown error")
        )


def _ps_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def ensure_opener() -> Path:
    APPDATA_DIR.mkdir(parents=True, exist_ok=True)
    dest = APPDATA_DIR / OPENER_NAME
    bundled = tool_dir() / OPENER_NAME
    if bundled.is_file():
        shutil.copy2(bundled, dest)
        return dest
    if dest.is_file():
        return dest
    compile_opener(dest)
    return dest


def wrap_double_click(opener: Path) -> None:
    command = f'"{opener}" "%1"'
    for progid in ("VSCode.py",):
        command_key = rf"Software\Classes\{progid}\shell\open\command"
        try:
            existing = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, command_key, 0, winreg.KEY_READ | winreg.KEY_SET_VALUE
            )
        except FileNotFoundError:
            continue
        try:
            current, _ = winreg.QueryValueEx(existing, None)
            if OPENER_NAME.lower() in str(current).lower():
                continue
            backup = winreg.CreateKey(
                winreg.HKEY_CURRENT_USER, rf"Software\IndependentPythonEnv\Backup\{progid}"
            )
            try:
                winreg.SetValueEx(backup, "open_command", 0, winreg.REG_SZ, str(current))
            finally:
                winreg.CloseKey(backup)
            winreg.SetValueEx(existing, None, 0, winreg.REG_SZ, command)
        finally:
            winreg.CloseKey(existing)


def write_install_hook(opener: Path) -> None:
    cmd = APPDATA_DIR / "install_hook.cmd"
    cmd.write_text(
        "@echo off\r\n"
        f'if exist "{opener}" (\r\n'
        f'  rem hook already installed by the green tool\r\n'
        f")\r\n",
        encoding="ascii",
        newline="",
    )


def write_project_helpers(dest: Path, enabled: bool) -> None:
    vscode = dest / ".vscode"
    vscode.mkdir(exist_ok=True)
    (vscode / "settings.json").write_text(VSCODE_SETTINGS, encoding="utf-8")

    marker = dest / MARKER_NAME
    if enabled:
        marker.write_text("", encoding="ascii")
    elif marker.exists():
        marker.unlink()

    enable_body = (
        "@echo off\r\n"
        "cd /d \"%~dp0\"\r\n"
        f'type nul > "%~dp0{MARKER_NAME}"\r\n'
        "echo This project will use its own environment when you double-click .py files.\r\n"
        "pause\r\n"
    )
    disable_body = (
        "@echo off\r\n"
        "cd /d \"%~dp0\"\r\n"
        f'if exist "%~dp0{MARKER_NAME}" del /f /q "%~dp0{MARKER_NAME}"\r\n'
        "echo This project will use the system Python when you double-click .py files.\r\n"
        "pause\r\n"
    )
    (dest / ENABLE_BAT_NAME).write_text(enable_body, encoding="ascii")
    (dest / DISABLE_BAT_NAME).write_text(disable_body, encoding="ascii")


def create_project(name: str, parent: Path, enabled: bool) -> Path:
    name = name.strip()
    if not name:
        raise ValueError("Please enter a project name.")
    if any(ch in name for ch in FORBIDDEN):
        raise ValueError('Do not use these characters in the name: \\ / : * ? " < > |')

    dest = parent / name
    if dest.exists():
        raise ValueError(f"A folder with this name already exists:\n{dest}")

    parent.mkdir(parents=True, exist_ok=True)
    dest.mkdir()

    python = resolve_python()
    cmd = [python, "-m", "venv", str(dest / ".venv")]
    if Path(python).name.lower() == "py.exe":
        cmd = [python, "-3", "-m", "venv", str(dest / ".venv")]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise ValueError(
            "Could not create the project environment:\n"
            + (result.stderr or result.stdout or "Unknown error")
        )

    write_project_helpers(dest, enabled)
    opener = ensure_opener()
    wrap_double_click(opener)
    write_install_hook(opener)
    return dest


def open_window() -> None:
    window = tk.Tk()
    window.title(WINDOW_TITLE)
    window.geometry("620x300")
    window.resizable(False, False)

    name_var = tk.StringVar()
    place_var = tk.StringVar(value=str(DEFAULT_PARENT))
    enabled_var = tk.BooleanVar(value=False)
    status_var = tk.StringVar(
        value="Enter a name and click Create. No command line needed."
    )

    def browse() -> None:
        chosen = filedialog.askdirectory(initialdir=place_var.get() or str(DEFAULT_PARENT))
        if chosen:
            place_var.set(chosen)

    def on_create() -> None:
        status_var.set("Creating an independent project environment. Please wait…")
        window.update_idletasks()
        try:
            path = create_project(name_var.get(), Path(place_var.get()), enabled_var.get())
        except Exception as err:
            status_var.set("Did not succeed.")
            messagebox.showerror("Did not succeed", str(err))
            return
        status_var.set("Done.")
        if enabled_var.get():
            extra = (
                "Double-click .py files in this folder will use this project's environment.\n"
                "You can turn this off later with:\n"
                "关闭：双击用系统 Python.bat"
            )
        else:
            extra = (
                "Double-click .py files still uses the system Python.\n"
                "Turn it on later with:\n"
                "启用：双击用本环境.bat"
            )
        messagebox.showinfo(
            "Done",
            "Independent Python project environment created:\n"
            f"{path}\n\n"
            "This project's own environment is the .venv folder inside it.\n"
            "Put your .py files next to .venv, not inside it.\n\n"
            + extra,
        )

    pad = {"padx": 16, "pady": 6}
    tk.Label(window, text="Project name").grid(row=0, column=0, sticky="w", **pad)
    tk.Entry(window, textvariable=name_var, width=48).grid(
        row=0, column=1, columnspan=2, **pad
    )

    tk.Label(window, text="Save in folder").grid(row=1, column=0, sticky="w", **pad)
    tk.Entry(window, textvariable=place_var, width=40).grid(row=1, column=1, **pad)
    tk.Button(window, text="Browse…", command=browse).grid(row=1, column=2, **pad)

    tk.Checkbutton(
        window,
        text="In this project, double-click .py files use this project's environment",
        variable=enabled_var,
        wraplength=500,
        justify="left",
        anchor="w",
    ).grid(row=2, column=0, columnspan=3, sticky="w", padx=16, pady=4)

    tk.Button(window, text="Create project", command=on_create, width=16).grid(
        row=3, column=1, sticky="w", padx=16, pady=8
    )
    tk.Label(window, textvariable=status_var, wraplength=560, justify="left").grid(
        row=4, column=0, columnspan=3, sticky="w", **pad
    )

    window.mainloop()


def warn_if_python_missing() -> bool:
    """When packed as exe, stop at a dialog if Python is not installed. True = continue."""
    if not getattr(sys, "frozen", False):
        return True
    try:
        resolve_python()
        return True
    except ValueError:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(
            "Python not found",
            "Python is not installed on this computer.\n\n"
            "Please open Complete User Manual.md in this same folder "
            "and follow the steps to install Python.\n\n"
            "Click OK, then install it yourself. "
            "Run this program again after Python is ready.",
        )
        root.destroy()
        return False


if __name__ == "__main__":
    if warn_if_python_missing():
        open_window()
