# Create an Independent Project Python Environment

Chinese name: **双击生成独立项目的 Python 环境**

---

## Complete User Manual

**This is only a helper tool. It cannot install Python for you.**

If Python is not installed, double-clicking will not show the window, or a black console will say Python was not found. Install Python first, then come back.

### Where to download

Use the official site only. Do not use random “portable / cracked Python” packages:

- Main downloads: <https://www.python.org/downloads/>
- Windows: <https://www.python.org/downloads/windows/>

Click the yellow **Download Python** button.

If you already installed Python with Anaconda / Miniconda, **do not install another copy**. This tool looks for `D:\Programs\anaconda\python.exe` first.

### Which version

- **Recommended: Python 3.11 or 3.12** (official Windows installer)
- **OK: 3.10, 3.11, 3.12, 3.13**
- **Do not use Python 2.x**

Install the 64-bit build (`amd64` in the filename) on a typical PC.

### During setup

1. **Check `Add python.exe to PATH`.** If you skip this, the tool often cannot find Python.
2. Click **Install Now**.
3. If the last page offers **Disable path length limit**, click it.
4. Restart is usually not required; if the tool still cannot find Python, close everything and try again, or reboot once.

The official installer already includes everything this tool needs. You do **not** download these separately:

| Required | Why |
|----------|-----|
| Python itself | Runs `.py` files |
| pip | Bundled; not used by this tool yet, useful later |
| venv | Bundled; creates each project’s independent environment |
| tkinter (Tcl/Tk) | Bundled; shows the name window |
| Windows 10 or newer | Supported |

### Not required for this tool

You do **not** need Cursor, VS Code, Git, Node.js, Java, Docker, Visual Studio, a C++ compiler, or extra Python libraries (Flask, Playwright, and so on) just to use this helper.

Anaconda is optional if you already have it.

### How to check that Python is installed

- Search **Python** in the Start menu and look for Python 3.x, or
- Open Command Prompt or PowerShell and run `python --version`. You should see `Python 3.11` (or similar). If Windows says it is not recognized, reinstall and tick **Add python.exe to PATH**.

Then double-click the shortcut **`Create Independent Project Python Environment.lnk`** (white background, faded Python logo, wand in front). Click only this shortcut.

The shortcut does **not** store your PC’s project folder path. It starts Windows’ own `wscript.exe`, then runs `open.vbs` in the **same folder**. After someone downloads this folder (or a GitHub ZIP) and keeps the files together, they can double-click the shortcut without editing paths.

Windows may block a file that came from the internet. If the first double-click is refused: right-click the shortcut or the ZIP → Properties → tick **Unblock** → OK.

The launcher `_internal.bat`, helper `open.vbs`, and icon `python_wand.ico` are hidden. They must stay with the shortcut and `create_project.py`. Copy the whole folder if you move it. If Explorer shows hidden items, do not double-click those hidden files.

If you move the whole folder, keep all files together. You should **not** need to rebuild the shortcut just because the folder moved.

You may copy this whole folder anywhere on this computer. It does **not** need to sit next to new projects or their `.venv`. See “How this folder relates to new projects” below.

---

## How to use this tool

### What this is

For people who are not comfortable with the command line: double-click `Create Independent Project Python Environment.lnk`, enter a name, and it will:

1. Create a new project folder
2. Create an **independent** Python environment (`.venv`) inside that folder only

### How this folder relates to new projects

These are two separate things:

| | This folder (the start button) | The project you just created |
|--|-------------------------------|------------------------------|
| What is inside | Shortcut `.lnk` (click this), hidden `_internal.bat`, `create_project.py`, `Complete User Manual.md` | Your project files + `.venv` (that project’s toolbox / environment) |
| Where it lives | Copy the whole folder anywhere (Desktop, D: drive, etc.) | The location you chose in the window |
| After you use it | You can close or move it; already-created projects keep working | The environment already lives inside the new project |

There is **no** rule that this tool folder must sit in the same directory as the new project, and **no** rule that it must sit next to `.venv`.

The only rule: **inside this tool folder**, keep hidden `_internal.bat` and `create_project.py` together (copy the shortcut and `Complete User Manual.md` with them). Do not copy the `.bat` to the Desktop by itself.

Copying the folder to **another PC with no Python** will fail. That is explained in the complete user manual, not a folder-layout issue.

### Important

- **Click only the shortcut.** The real launcher is hidden `_internal.bat` and must stay with `create_project.py`. Do not drag `_internal.bat` to the Desktop and click it.
- To use this from the Desktop: copy the whole folder `Create-Independent-Project-Python-Environment` (including the shortcut and `Complete User Manual.md`), then double-click the `.lnk` inside it.
- Each new project gets **its own** `.venv`. Do not copy `.venv` from another project.
- Do not use these characters in the project name: `\ / : * ? " < > |`
- If a folder with the same name already exists, nothing is overwritten; you will see an error.
- Creating the environment can take a few seconds. Do not click Create repeatedly while it says to wait.

### After it succeeds

In a terminal opened in the new project folder:

```powershell
.\.venv\Scripts\python.exe some_file.py
```
