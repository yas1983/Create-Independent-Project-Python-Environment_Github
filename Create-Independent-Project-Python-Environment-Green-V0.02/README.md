# Portable (green) edition V0.02

Double-click:

**Create Independent Project Python Environment.exe**

No installer. Unzip (or copy this folder) and run. You do **not** need Cursor, Git, or a `.lnk` shortcut.

Python must already be installed on the computer. This exe is only the window; it still asks the installed Python to create each project’s `.venv`. If Python is missing, a panel tells you to read **Complete User Manual.md**, then click **OK**.

Windows may say the app is unrecognized (unsigned). Choose **More info** → **Run anyway** if you trust this file.

## What is new in V0.02

Each project can choose whether double-clicking `.py` files uses **this project’s** environment (`.venv`) or the computer’s default Python.

- When you create a project, the box is **off** unless you tick it.
- Later you can turn it on or off inside that project folder:
  - `启用：双击用本环境.bat`
  - `关闭：双击用系统 Python.bat`

Put your `.py` files next to `.venv`, not inside it. New files and files pasted from elsewhere follow the same rule.

This folder is the green build. Older copies without a version number are **V0.01**.

For daily use, this folder only needs three files:

- `Create Independent Project Python Environment.exe`
- `README.md`
- `Complete User Manual.md`

Source and the design plan live next to this folder, in `Create-Independent-Project-Python-Environment-Source` (`V0.02` for this build). Do not put source files in the green folder.

Do not upload `wscript.exe`.
