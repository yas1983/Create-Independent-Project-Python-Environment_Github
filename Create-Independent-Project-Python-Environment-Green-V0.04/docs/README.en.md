# Portable (green) edition V0.04

Double-click:

**Create Independent Project Python Environment.exe**

No installer. Unzip (or copy this folder) and run. You do **not** need Cursor, Git, or a `.lnk` shortcut.

Python must already be installed on the computer. This exe is only the window; it still asks the installed Python to create each project’s `.venv`. If Python is missing, a panel tells you to read **Complete User Manual.en.md** in the visible `docs` folder, then click **OK**.

At the top of this green folder, double-click the exe. English manuals sit in `docs`; Chinese manuals sit in `说明`. Nothing is set hidden.

Windows may say the app is unrecognized (unsigned). Choose **More info** → **Run anyway** if you trust this file.

## Language

At the top of the create window, pick **中文** or **English**. The default is Chinese.

Chinese creates at the top level:

- `本项目环境.exe` (double-click this)
- `说明.txt`
- `使用手册.md`

Scripts are in `工具`. Window text is Chinese.

English creates at the top level:

- `Project Environment.exe`
- `Read me.txt`
- `User Manual.md`

Scripts are in `tools`. Window text is English.

Language is fixed when the project is created. To use the other language, create a new project with that choice.

## What is new in V0.04 compared with V0.03

- Reads Windows 11 `UserChoiceLatest` for the real `.py` default.
- New projects keep the panel exe, a short note, and the manual at the top; scripts go in `工具` / `tools`.

## What is still here from V0.03

Each new project folder gets one panel. After creating a project, double-click the panel exe above.

At the top: a checkbox. Ticked = this project’s `.py` files use this folder’s `.venv`. That changes **VSCode.py for the whole computer** (you confirm the first time). A project that is not ticked still goes through the opener, which then runs the backed-up original command. Restore turns the hook off for every project. If this PC does not open `.py` files with VS Code, ticking is refused and the switch stays off.

Below that: install and remove libraries (numpy, matplotlib, pandas, openpyxl, pygame, requests, flask, pillow, or paste other names). The list shows libraries you asked for. Helper libraries they need are installed too, but not listed separately.

There are no `.bat` switch files in the project folder.

When you create a project, the create-window box is **off** unless you tick it. Change it later in the panel exe.

Put your `.py` files next to `.venv`, not inside it. New files and files pasted from elsewhere follow the same rule.

For daily use, the top of this green folder only needs:

- `Create Independent Project Python Environment.exe`
- `README.md` (points to `说明` and `docs`)
- the `说明` folder (Chinese manuals; nothing is hidden)
- the `docs` folder (English manuals; nothing is hidden)

Source and the design plan live next to this folder, in `Create-Independent-Project-Python-Environment-Source` (`V0.04` for this build). Do not put source files in the green folder.

Do not upload `wscript.exe`.
