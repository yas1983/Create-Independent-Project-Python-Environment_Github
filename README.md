# Create Independent Project Python Environment

**当前版本 / Current release：V0.04**

一个给 Windows 用的绿色小工具：点几下就能给每个 Python 小项目搭好**独立虚拟环境**，少打命令行，少反复折腾环境。

A portable Windows tool that sets up a **separate `.venv` per project** with a few clicks—less command-line typing, less environment hassle.

---

## 为什么做它 / Why I built this

学 Python 做项目时，总要反复：

- 建虚拟环境、切环境  
- 记 `pip install` 包名、怕拼错  
- 在 VS Code 里对不上该用哪个 Python  

作为初学者，我想有一个**省事的外壳**：把「建环境 + 装库 +（可选）双击 `.py` 走本项目」收成窗口和按钮，把心力留给写代码，而不是记命令。

I kept redoing venv setup and `pip install` for every small project. This is my first app—a simple shell so I can focus on code instead of the terminal.

---

## 现在能做什么 / What V0.04 does

### 1. 一键建项目环境

双击绿色 exe → 填项目名、保存位置 → 自动创建文件夹、`.venv`、VS Code 工作区设置（终端指向本项目 `.venv`）。

### 2. 中英文界面

生成窗口可选中文 / English；语言写入项目的 `ui_lang.txt`，面板文字和文件名跟着走。

### 3. 项目环境面板（装库 / 删库）

每个项目里有 **「本项目环境」** 面板（或英文 `Project Environment.exe`）：

- 勾选常用库，或粘贴库名  
- 安装前会弹出确认（提醒核对拼写）  
- 只往**本项目 `.venv`** 里 `pip install`，不动系统 Python  

### 4. 可选：双击 `.py` 用本项目环境（整机挂钩，须确认）

- **默认不勾**——不会悄悄改电脑。  
- 勾选并**第一次确认**后，才会改本机 `VSCode.py` 的打开方式（整台电脑生效；Windows 无法只改某一个文件夹）。  
- 原打开方式会**备份**；面板里可 **「恢复本机双击 .py」** 读回备份。  
- 支持 Windows 11「设置 → 默认应用」里的 `.py` 关联（只读 `UserChoiceLatest`，不写注册表里的 UserChoice）。  
- 未启用的项目：双击仍会经过开门程序，但会走**备份里的原打开方式**，不会硬塞进 VS Code。

### 5. 绿色包结构（V0.04）

| 位置 | 内容 |
|------|------|
| 根目录 | `Create Independent Project Python Environment.exe`、入口 `README.md` |
| **说明** | 中文手册（开屏、功能、Complete User Manual） |
| **docs** | English manuals |
| 新建项目内 | 面板 exe、说明、手册；脚本在 **工具** / **tools**（不隐藏） |

---

## 下载与使用 / Download & run

1. 打开文件夹 **[Create-Independent-Project-Python-Environment-Green-V0.04](Create-Independent-Project-Python-Environment-Green-V0.04/)**  
2. 双击 **`Create Independent Project Python Environment.exe`**（不要用 `.lnk` 快捷方式）  
3. 电脑需已安装 Python；若没有，按 **说明** / **docs** 里的 Complete User Manual 安装后再试  
4. Windows 可能提示「无法识别」→ 更多信息 → 仍要运行  

更细的按钮说明见绿色包内 **说明/开屏手册.md** 与 **产品功能手册.md**。

---

## 仓库里还有什么 / Repo layout

| 文件夹 | 说明 |
|--------|------|
| `Create-Independent-Project-Python-Environment-Green-V0.04/` | **当前推荐**绿色可执行版 |
| `Create-Independent-Project-Python-Environment-Green-V0.03/` 等 | 旧版绿色包（保留对照） |
| `Create-Independent-Project-Python-Environment-Source/` | 源码（按 V0.01、V0.02… 分版本） |

---

## 不会做的事 / Out of scope

- 不替你在后台偷偷改注册表、环境变量或启动项（改双击必须勾选 + 确认）  
- 不上传、不收集你的项目内容  
- 不能做到「只给某一个文件夹改 Windows 双击关联」（系统限制）  

---

## 版本

- **V0.04**（2026-09-11）：Win11 默认打开方式检测、绿色包 **说明** + **docs** 分语言、挂钩须确认且可恢复、预编译助手 exe、不隐藏文件。  
- 更早版本见各 `Green-V0.0X` 文件夹。

---

Made by **yas** — first app, built to make Python project setup less painful for beginners.
