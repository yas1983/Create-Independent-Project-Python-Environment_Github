# Create Independent Project Python Environment

**Current release: V0.04**  
<sub>当前版本：V0.04</sub>

A portable Windows tool: set up a **separate `.venv` per project** in a few clicks—less terminal typing, less environment hassle.  
<sub>Windows 绿色小工具：点几下给每个 Python 项目搭独立虚拟环境，少打命令行，少折腾环境。</sub>

---

## Why I built this
<sub>为什么做它</sub>

When learning Python I kept redoing the same chores:  
<sub>学 Python 做项目时，总要反复：</sub>

- Create and switch virtual environments  
  <sub>建虚拟环境、切环境</sub>
- Remember `pip install` names and worry about typos  
  <sub>记 `pip install` 包名、怕拼错</sub>
- Point VS Code at the wrong Python  
  <sub>在 VS Code 里对不上该用哪个 Python</sub>

As a beginner I wanted a **simple shell**—create env, install libs, and (optionally) open `.py` files through this project—so I can focus on code, not commands. This is my **first app**.  
<sub>作为菜鸟，我想有个省事的外壳：建环境、装库、（可选）双击 `.py` 走本项目，把心力留给写代码。这是我做的第一个小软件。</sub>

---

## What V0.04 does
<sub>V0.04 能做什么</sub>

### 1. One-click project environment
<sub>一键建项目环境</sub>

Double-click the green exe → enter name and folder → the tool creates the project folder, `.venv`, and VS Code settings (terminal uses this `.venv`).  
<sub>双击绿色 exe → 填项目名和位置 → 自动建文件夹、`.venv`、VS Code 工作区（终端指向本项目 `.venv`）。</sub>

### 2. Chinese / English UI
<sub>中英文界面</sub>

Pick 中文 or English in the create window; language is saved in `ui_lang.txt` and drives panel text and file names.  
<sub>生成窗口可选中文 / English；写入 `ui_lang.txt`，面板文字和文件名跟着走。</sub>

### 3. Project Environment panel (install / remove libraries)
<sub>项目环境面板（装库 / 删库）</sub>

Each project includes **本项目环境** (or **Project Environment.exe**):  
<sub>每个项目里有「本项目环境」面板（或英文 Project Environment.exe）：</sub>

- Tick common libraries or paste package names  
  <sub>勾选常用库，或粘贴库名</sub>
- Confirm before install (spell-check reminder)  
  <sub>安装前弹出确认（提醒核对拼写）</sub>
- `pip install` only into **this project's `.venv`**, not system Python  
  <sub>只往本项目 `.venv` 里 pip，不动系统 Python</sub>

### 4. Optional: double-click `.py` through this project (whole PC; must confirm)
<sub>可选：双击 `.py` 用本项目环境（整机挂钩，须确认）</sub>

- **Off by default**—nothing changes on your PC until you opt in.  
  <sub>**默认不勾**——不会悄悄改电脑。</sub>
- After you **check the box and confirm once**, the tool may change how `.py` opens via `VSCode.py` (whole computer; Windows cannot scope this to one folder only).  
  <sub>勾选并**第一次确认**后，才改本机 `VSCode.py` 打开方式（整机生效；Windows 无法只改某一个文件夹）。</sub>
- Original opener is **backed up**; use **Restore double-click for .py** in the panel to read it back.  
  <sub>原打开方式会**备份**；面板里「恢复本机双击 .py」可读回。</sub>
- Windows 11 “Default apps” for `.py` is detected read-only (`UserChoiceLatest`); the tool does not write `UserChoice`.  
  <sub>支持 Win11「设置 → 默认应用」里的 `.py` 关联（只读 UserChoiceLatest，不写 UserChoice）。</sub>
- Disabled projects still pass through the opener but fall back to the **backed-up command**, not forced VS Code.  
  <sub>未启用的项目仍经开门程序，但走**备份里的原打开方式**，不会硬塞进 VS Code。</sub>

### 5. Green package layout (V0.04)
<sub>绿色包结构（V0.04）</sub>

| Location | Contents |
|----------|----------|
| Root | `Create Independent Project Python Environment.exe`, entry `README.md` <br><sub>根目录：exe、入口 README</sub> |
| **说明** | Chinese manuals (quick start, features, Complete User Manual) <br><sub>中文手册</sub> |
| **docs** | English manuals <br><sub>英文手册</sub> |
| Inside new projects | Panel exe, readme, manual; scripts in **工具** / **tools** (not hidden) <br><sub>新项目：面板、说明、手册；脚本在 工具/tools，不隐藏</sub> |

---

## Download & run
<sub>下载与使用</sub>

1. Open **[Create-Independent-Project-Python-Environment-Green-V0.04](Create-Independent-Project-Python-Environment-Green-V0.04/)**  
   <sub>打开绿色版 V0.04 文件夹</sub>
2. Double-click **`Create Independent Project Python Environment.exe`** (not a `.lnk` shortcut)  
   <sub>双击 exe（不要用 .lnk 快捷方式）</sub>
3. Python must already be installed; if not, follow **Complete User Manual** in **说明** or **docs**  
   <sub>电脑需已装 Python；否则按 说明/docs 里的手册安装</sub>
4. If Windows warns “unrecognized app” → More info → Run anyway  
   <sub>若提示无法识别 → 更多信息 → 仍要运行</sub>

More detail: **说明/开屏手册.md** and **产品功能手册.md** inside the green folder.  
<sub>更细说明见绿色包内开屏手册与产品功能手册。</sub>

---

## Repo layout
<sub>仓库结构</sub>

| Folder | Note |
|--------|------|
| `Create-Independent-Project-Python-Environment-Green-V0.04/` | **Recommended** green build <br><sub>**当前推荐**绿色可执行版</sub> |
| `Create-Independent-Project-Python-Environment-Green-V0.03/` … | Older green builds <br><sub>旧版绿色包（对照用）</sub> |
| `Create-Independent-Project-Python-Environment-Source/` | Source by version (V0.01, V0.02, …) <br><sub>源码（按版本分文件夹）</sub> |

---

## Out of scope
<sub>不会做的事</sub>

- No silent changes to registry, env vars, or startup items (double-click changes require check + confirm).  
  <sub>不偷偷改注册表、环境变量、启动项（改双击须勾选 + 确认）。</sub>
- Does not upload or collect your project files.  
  <sub>不上传、不收集你的项目内容。</sub>
- Cannot make Windows associate `.py` with **only one folder** (OS limitation).  
  <sub>不能「只给某一个文件夹」改双击关联（系统限制）。</sub>

---

## Version history
<sub>版本</sub>

- **V0.04** (2026-09-11): Win11 default-app detection; green pack **说明** + **docs**; hook only after confirm with restore; prebuilt helper exes; no hidden files.  
  <sub>**V0.04**：Win11 默认打开检测；说明+docs 分语言；挂钩须确认可恢复；预编译助手；不隐藏文件。</sub>
- Earlier builds: see each `Green-V0.0X` folder.  
  <sub>更早版本见各 Green-V0.0X 文件夹。</sub>

---

Made by **yas** — first app, built to make Python project setup less painful for beginners.  
<sub>作者 yas — 第一个小软件，让 Python 项目环境少折腾一点。</sub>
