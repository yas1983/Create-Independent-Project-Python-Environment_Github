# 双击生成独立项目的 Python 环境

英文名：**Double-Click to Create an Independent Project Python Environment**

---

## Complete User Manual（完整使用手册）

**这只是一个小工具，不能替你安装 Python。**

如果你的电脑里还没有 Python，双击之后不会出现窗口，或者黑色窗口提示找不到 Python。请先按下面把 Python 装好，再回来用这个工具。

### 去哪里下载

请只用官网，不要用来路不明的「Python 加速包 / 绿色版」：

- 官网总入口：<https://www.python.org/downloads/>
- Windows 直接页：<https://www.python.org/downloads/windows/>

点黄色的 **Download Python** 即可。那是官方安装包。

已经用 Anaconda / Miniconda 装过 Python 的人，**不必再装一份**。这个工具会优先使用 `D:\Programs\anaconda\python.exe`。

### 装什么版本

- **建议：Python 3.11 或 3.12**（Windows 官方安装包，稳定、好装）
- **可以用：3.10、3.11、3.12、3.13**
- **不要：Python 2.x**（太旧，这个工具不能用）

装 64-bit（安装器名字里通常有 `amd64`）即可，现在常见电脑都是这种。

### 安装时必须勾选 / 注意

官方 Windows 安装器打开后：

1. **务必勾选** `Add python.exe to PATH`（把 Python 加入系统路径）。不勾的话，双击这个工具经常会说找不到 Python。
2. 点 **Install Now** 就可以。
3. 装完如果最后一页有 **Disable path length limit**（解除路径长度限制），建议点一下，以后少出怪问题。
4. 装完可点 Close。一般**不用重启电脑**；若双击仍找不到，关完所有窗口再试一次，或重启一次。

官方安装包已经自带这个工具需要的东西，你**不用再单独下载**：

| 需要有的 | 说明 |
|----------|------|
| Python 本体 | 能运行 `.py` 文件 |
| pip | 官方安装包自带，这个小工具暂时用不到，但以后装别的包会用到 |
| venv | 官方安装包自带，用来给每个项目生成独立环境 |
| tkinter（窗口） | 官方安装包自带，用来弹出填写名称的窗口。依赖 Tcl/Tk，也已打在官方安装包里 |
| Windows 10 或更新 | 你现在的系统可以 |

### 不需要为了这个工具去装的

这些**不是**这个小工具的前提。没装也能用（除非你做别的项目需要）：

- Cursor / VS Code 等编辑器
- Git
- Node.js、Java、Docker
- Visual Studio、C++ 编译器
- 额外的 Python 扩展库（Flask、Playwright 等）——那是别的项目的事

可选、不是必须：Anaconda。你已经装过的话，继续用即可。

### 怎么确认电脑里已经有 Python（不会命令行也可以）

任选一种：

- 开始菜单搜索 **Python**，能看到 Python 3.x，一般就是装上了。
- 开始菜单搜索 **命令提示符** 或 **PowerShell**，输入 `python --version` 回车。出现 `Python 3.11` 这类字样就对了。如果提示不是内部或外部命令，多半是没勾选 PATH，请卸载后重装并勾选 `Add python.exe to PATH`。

确认有 Python 之后，再双击文件夹里的快捷方式 **`双击生成独立项目的Python环境.lnk`**（白底、淡 Python 标志、前面一根魔杖）。请只点这个快捷方式。

快捷方式**不再记下你这台电脑的项目路径**。它先调用 Windows 自带的程序，再运行同一文件夹里的 `open.vbs`。别人下载整个文件夹（或 GitHub 压缩包）后，只要文件还在一起，一般可以直接双击，不用再改路径。

若文件来自网络，Windows 可能拦截第一次双击：右键快捷方式或压缩包 → 属性 → 勾选 **解除锁定** → 确定。

内部文件 `_internal.bat`、`open.vbs`、`python_wand.ico` 已隐藏。它们必须和快捷方式、`create_project.py` 留在同一文件夹；拷走时请拷整个文件夹。若资源管理器开了「隐藏的项目」，请不要双击这些隐藏文件。

若把整个文件夹拷到别的位置，只要文件还在一起，一般**不必**重新做快捷方式。

本文件夹可以拷到这台电脑的任意位置，**不必**和新项目、也不必和项目里的 `.venv` 放在一起。详见下面「和新建项目是什么关系」。

---

## Complete User Manual (English)

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

Then double-click the shortcut **`双击生成独立项目的Python环境.lnk`** (white background, faded Python logo, wand in front). Click only this shortcut.

The launcher file `_internal.bat` and the icon file `python_wand.ico` are hidden so the folder does not show two icons. They must stay with the shortcut and `create_project.py`. Copy the whole folder if you move it. If Explorer shows hidden items, do not double-click those hidden files.

If you move the whole folder, the shortcut may still point to the old path. Delete the old `.lnk` or recreate it in the new location.

You may copy this whole folder anywhere on this computer. It does **not** need to sit next to new projects or their `.venv`. See “How this folder relates to new projects” below.

---

## 中文（这个工具怎么用）

### 这是什么

给不太会用命令行的人用：双击快捷方式 `双击生成独立项目的Python环境.lnk`，弹出窗口，起个名字，就会自动：

1. 新建一个项目文件夹
2. 在里面生成**只属于这个项目**的 Python 环境（`.venv`）

### 和新建项目是什么关系

这是两套东西，各过各的：

| | 你现在看的这个文件夹（开工按钮） | 你新建出来的那个项目 |
|--|----------------------------------|----------------------|
| 里面是什么 | 快捷方式 `.lnk`（请点这个）、隐藏的 `_internal.bat`、`create_project.py`、本说明书 | 项目自己的文件 + `.venv`（工具库 / 项目环境） |
| 放哪 | 整夹可以粘贴到系统任意位置（桌面、D 盘等） | 窗口里你填的「放在哪个文件夹」 |
| 用完之后 | 可以关掉、搬走，不影响已经建好的项目 | 环境已经生在新项目里面了 |

**没有**「这个工具文件夹必须和新建项目放同一层目录」这种要求，也**没有**「必须挨着 `.venv`」这种要求。

唯一要守的：这个工具文件夹**内部**，隐藏的 `_internal.bat` 和 `create_project.py` 必须在一起（建议连快捷方式和 `Complete User Manual.md` 一起拷）。不要单独拷走 bat。

拷到**另一台没装 Python 的电脑**会打不开，那是完整使用手册里说的事，和目录结构无关。

### 必须注意

- **请只双击快捷方式。** 真正干活的是隐藏文件 `_internal.bat`，必须和 `create_project.py` 放在同一个文件夹里。不要把 `_internal.bat` 单独拖到桌面去点。
- 若要放到桌面使用：请拷贝整个「双击生成独立项目的Python环境」文件夹（含快捷方式、`Complete User Manual.md`），再双击里面的 `.lnk`。
- 每创建一个项目，都会得到**自己的一份**环境。不要把别的项目里的 `.venv` 拷过来用。
- 项目名称不要包含这些符号：`\ / : * ? " < > |`
- 如果目标位置已经有同名文件夹，不会覆盖，会提示失败。
- 生成环境可能需要几秒，窗口提示「请稍等」时不要重复点击。

### 创建成功之后

在新项目的终端里，用这个项目自己的环境运行文件，例如：

```powershell
.\.venv\Scripts\python.exe 某个文件.py
```

---

## English (how to use this tool)

### What this is

For people who are not comfortable with the command line: double-click `双击生成独立项目的Python环境.lnk`, enter a name, and it will:

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
- To use this from the Desktop: copy the whole folder `双击生成独立项目的Python环境` (including the shortcut and `Complete User Manual.md`), then double-click the `.lnk` inside it.
- Each new project gets **its own** `.venv`. Do not copy `.venv` from another project.
- Do not use these characters in the project name: `\ / : * ? " < > |`
- If a folder with the same name already exists, nothing is overwritten; you will see an error.
- Creating the environment can take a few seconds. Do not click Create repeatedly while it says to wait.

### After it succeeds

In a terminal opened in the new project folder:

```powershell
.\.venv\Scripts\python.exe some_file.py
```
