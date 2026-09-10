# Create an Independent Project Python Environment

**Portable / green edition V0.02:** double-click `Create Independent Project Python Environment.exe` in this folder. No `.lnk` shortcut and no extra `.bat` for the end user.

Chinese name: **双击生成独立项目的 Python 环境（绿色版 V0.02）**

---

## Complete User Manual

**This is only a helper tool. It cannot install Python for you.**

If Python is not installed, double-clicking the `.exe` opens a small panel: it tells you to read this manual, install Python yourself, then click **OK**. The main window does not open. After Python is installed, double-click the `.exe` again.

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
| pip | Bundled; useful later inside each project’s `.venv` |
| venv | Bundled; creates each project’s independent environment |
| tkinter (Tcl/Tk) | Bundled; shows the name window |
| Windows 10 or newer | Supported |

### Not required for this tool

You do **not** need Cursor, Git, Node.js, Java, Docker, Visual Studio, a C++ compiler, or extra Python libraries (Flask, Playwright, and so on) just to use this helper.

VS Code is optional to *create* a project. It is needed if you want double-click to **open** a `.py` file in the editor and then click Run.

Anaconda is optional if you already have it.

### How to check that Python is installed

- Search **Python** in the Start menu and look for Python 3.x, or
- Open Command Prompt or PowerShell and run `python --version`. You should see `Python 3.11` (or similar). If Windows says it is not recognized, reinstall and tick **Add python.exe to PATH**.

Then double-click **`Create Independent Project Python Environment.exe`** in this folder.

Windows may block a file that came from the internet. If the first double-click is refused: right-click the `.exe` or the ZIP → Properties → tick **Unblock** → OK. Or choose **More info** → **Run anyway**.

You may copy this whole folder anywhere on this computer. It does **not** need to sit next to new projects or their `.venv`. See “How this folder relates to new projects” below.

---

## How to use this tool

### What this is

For people who are not comfortable with the command line: double-click the `.exe`, enter a name, and it will:

1. Create a new project folder
2. Create an **independent** Python environment (`.venv`) inside that folder only
3. Leave a per-project switch for how `.py` files are double-clicked (see V0.02 below)

### How this folder relates to new projects

These are two separate things:

| | This folder (the green tool) | The project you just created |
|--|-----------------------------|------------------------------|
| What is inside | `.exe` (click this), `README.md`, `Complete User Manual.md` | Your project files + `.venv` (that project’s toolbox / environment) |
| Where it lives | Copy the whole folder anywhere (Desktop, D: drive, etc.) | The location you chose in the window |
| After you use it | You can close or move it; already-created projects keep working | The environment already lives inside the new project |

There is **no** rule that this tool folder must sit in the same directory as the new project, and **no** rule that it must sit next to `.venv`.

Copying the folder to **another PC with no Python** will fail. That is explained above, not a folder-layout issue.

### Important

- **Click the `.exe`.** This green edition does not use a `.lnk` shortcut.
- Each new project gets **its own** `.venv`. Do not copy `.venv` from another project.
- Put your `.py` files **next to** `.venv` (or in a subfolder of the project). Do not put them inside `.venv`.
- New `.py` files and files pasted from elsewhere follow the same rule.
- Do not use these characters in the project name: `\ / : * ? " < > |`
- If a folder with the same name already exists, nothing is overwritten; you will see an error.
- Creating the environment can take a few seconds. Do not click Create repeatedly while it says to wait.

### After it succeeds

In a terminal opened in the new project folder you can always run:

```powershell
.\.venv\Scripts\python.exe some_file.py
```

That uses this project’s environment even if the double-click switch is off.

---

## V0.02: per-project double-click switch

The switch belongs to **one project**, not the whole computer.

In the create window there is a box (off by default):

**In this project, double-click .py files use this project's environment**

| When you created this project | Double-click a `.py` in this folder |
|-------------------------------|-------------------------------------|
| Box ticked | Uses this project’s `.venv` |
| Box left off | Uses the computer’s default Python |
| File is not inside any independent-environment folder | Uses the computer’s default Python |

Project A and project B each have their own switch.

### If you left the box off and later change your mind

You do not need to recreate the folder. Inside the project, double-click:

- **启用：双击用本环境.bat** — from now on, double-click `.py` here uses this project’s environment
- **关闭：双击用系统 Python.bat** — this project goes back to the computer’s default Python

Other projects are not changed.

### What the tool installs in the background

Windows cannot change double-click for only one folder. The first time you create a project with this V0.02 tool, a small opener is stored under your user AppData. It only looks at **that project’s** enable file (`use_project_env.on`). If the project is not enabled, double-click still behaves like the system default.

VS Code must be installed for double-click-to-edit. If VS Code is missing, use the terminal command in “After it succeeds”.

---

## V0.02 说明（中文）

绿色版，双击本文件夹里的 **Create Independent Project Python Environment.exe**。不要用旧版的 `.lnk`。

生成窗口里有一项，默认不勾：

**在此项目中，双击 .py 时使用本项目的独立环境**

- 勾了：这个文件夹里的 `.py`（新建的或从别处粘进来的）双击后走本项目的 `.venv`
- 没勾：双击仍用电脑默认的 Python
- 程序文件放在 `.venv` 旁边，不要放进 `.venv`

当时没勾、后来要改，不用重建文件夹。在项目里双击：

- **启用：双击用本环境.bat**
- **关闭：双击用系统 Python.bat**

这不是全电脑总开关。作业 A 勾了、作业 B 没勾，互不影响。
