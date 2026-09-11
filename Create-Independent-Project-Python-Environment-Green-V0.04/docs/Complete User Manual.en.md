# Create an Independent Project Python Environment

**Portable / green edition V0.04:** in the green pack, double-click `Create Independent Project Python Environment.exe` at the top level. English manuals sit in the visible `docs` folder; Chinese manuals sit in `说明`. No `.lnk` shortcut and no extra `.bat` for the end user.

Chinese name: **双击生成独立项目的 Python 环境（绿色版 V0.04）**

Also in the green pack’s `docs` folder:

- `Complete User Manual.en.md` — this file
- `README.en.md`

Chinese manuals are in `说明`.

---

## Complete User Manual

**This is only a helper tool. It cannot install Python for you.**

If Python is not installed, double-clicking the `.exe` opens a small panel: it tells you to read this manual, install Python yourself, then click **OK**. The main window does not open. After Python is installed, double-click the `.exe` again.

### Where to download

Use the official site only. Do not use random “portable / cracked Python” packages:

- Main downloads: <https://www.python.org/downloads/>
- Windows: <https://www.python.org/downloads/windows/>

Click the yellow **Download Python** button.

If you already installed Python with Anaconda / Miniconda, **do not install another copy**. Make sure `python` or `py` is on PATH (or use the Anaconda Prompt). This tool does not hard-code a drive-letter path.

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

Then go back to the top of the green pack and double-click **`Create Independent Project Python Environment.exe`**.

Windows may block a file that came from the internet. If the first double-click is refused: right-click the `.exe` or the ZIP → Properties → tick **Unblock** → OK. Or choose **More info** → **Run anyway**.

You may copy this whole folder anywhere on this computer. It does **not** need to sit next to new projects or their `.venv`. See “How this folder relates to new projects” below.

---

## How to use this tool

### What this is

For people who are not comfortable with the command line: double-click the `.exe`, enter a name, and it will:

1. Create a new project folder
2. Create an **independent** Python environment (`.venv`) inside that folder only
3. Leave a library window in that folder so you can add or remove packages
4. Leave a per-project switch (whether **this project** uses `.venv`). Changing double-click is computer-wide; you confirm the first time.

### Language: Chinese or English

At the top of the create window, pick **中文** or **English** before you click Create.

| Choice | Panel exe in the new project | Panel text |
|--------|------------------------------|------------|
| 中文 | `本项目环境.exe` | Chinese |
| English | `Project Environment.exe` | English |

That choice is stored in the project as `ui_lang.txt`. Later windows in that project follow it. To use the other language, create a new project with that option.

### How this folder relates to new projects

These are two separate things:

| | This folder (the green tool) | The project you just created |
|--|-----------------------------|------------------------------|
| What is inside | Top level: `.exe` (click this) and the index README; Chinese manuals in `说明`, English in `docs` | Your project files + `.venv` (that project’s toolbox / environment) |
| Where it lives | Copy the whole folder anywhere (Desktop, D: drive, etc.) | The location you chose in the window |
| After you use it | You can close or move it; already-created projects keep working | The environment already lives inside the new project |

There is **no** rule that the green tool folder must sit in the same directory as the new project, and **no** rule that it must sit next to `.venv`. The `工具` / `tools` folder inside a new project is for the program’s own files; you do not need to open it. Double-click the panel exe at the top. If you are reading this manual inside a project, click that top-level exe.

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

## V0.04: this project’s panel

After a project is created, double-click **本项目环境.exe** (Chinese) or **Project Environment.exe** (English) at the **top** of that project folder. A short note and the user manual sit next to it. Scripts live in `工具` / `tools`; you do not need to open that folder.

- Top checkbox: ticked = this project’s double-click `.py` uses this folder’s `.venv`; unticked = this project no longer asks for that environment. The first time the computer’s open command would change, you will be asked. Unticking only turns this project off; it does not restore the whole computer.
- **Restore double-click for .py**: reads the backup and restores the previous open command (whole computer, not only this project).
- Below: tick common libraries, or paste names from PyPI into the box (spaces or commas).
- Common list: numpy, matplotlib, pandas, openpyxl, pygame, requests, flask, pillow.
- The bottom list shows libraries you asked for. Helper libraries they need are installed too, but not listed separately.
- An install that did not finish does not appear.
- Closing the window stops the current install.
- `pip` / `setuptools` / `wheel` cannot be deleted.
- Do not double-click the panel `.py` in `工具` / `tools` if you only want the window; that file is the program. Use the `.exe` at the top of the folder.

This window never installs into the computer’s system Python.

Older projects made before this panel do not get it automatically. Create a new project with the current V0.04 tool.

---

## V0.02: per-project double-click switch

The enable file (`use_project_env.on`) belongs to **one project**. Once double-click is wrapped, that hook is computer-wide.

In the create window there is a box (off by default):

**In this project, double-click .py files use this project's environment**

| When you created this project | Double-click a `.py` in this folder |
|-------------------------------|-------------------------------------|
| Box ticked, and you confirmed changing how `.py` files open | This project uses its `.venv` (double-click first goes through the opener) |
| Box left off, or you cancelled a new-hook confirm | This create does **not** add a **new** hook. If a leftover opener command is found, OK clears it then creates; Cancel does not create. If a previous confirm already wrapped this computer, double-click still goes through the opener, which then runs the backed-up original command |
| File is not inside any enabled independent-environment folder | The opener runs the backup first; then VS Code / Notepad if the backup is missing |

Project A and project B each have their own switch. Unticking only turns that one project off.

### If you left the box off and later change your mind

You do not need to recreate the folder. Open the panel exe and tick the box at the top. If this would be the first change to the computer’s open command, you will be asked again.

Other projects’ switches are not changed. To restore the whole computer’s previous double-click method, use **Restore double-click for .py**.

### What the tool installs in the background

Windows cannot change double-click for only one folder. **Only after you tick the environment box and confirm**, a small opener is stored under your user AppData, and this key is changed:

`HKCU\Software\Classes\VSCode.py\shell\open\command`

The previous open command is backed up. The opener only looks at **that project’s** enable file (`use_project_env.on`). If the project is not enabled, double-click still goes through the opener: this project will not force `.venv`, but the whole computer’s open command is restored only with **Restore double-click for .py**. Creating a project with the box off does **not** add a new hook. If a leftover opener command is found, OK clears it; Cancel does not create.

VS Code must be installed for double-click-to-edit. If VS Code is missing, the opener tries the backed-up command; if that also fails, it opens the file in Notepad so the file is not stuck. You can also use the terminal command in “After it succeeds”.
