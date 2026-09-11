# 绿色版 V0.04

双击：

**Create Independent Project Python Environment.exe**

不用安装。解压（或复制本文件夹）后直接运行。不需要 Cursor、Git，也不需要 `.lnk` 快捷方式。

电脑上需要先装好 Python。这个 exe 只是窗口；真正建每个项目的 `.venv`，还是请已安装的 Python 去做。如果没有 Python，会弹出说明，请先看「说明」文件夹里的 **Complete User Manual.zh.md**，再点确定。

绿色包第一层请双击 exe。中文说明书在看得见的「说明」文件夹，英文在 `docs`。没有设成隐藏。

Windows 可能提示无法识别（未签名）。如果信任这个文件，选「更多信息」→「仍要运行」。

## 语言

生成窗口最上面有一项：**中文** 或 **English**。默认中文。

选中文后，新项目最外层是：

- `本项目环境.exe`（请双击这个）
- `说明.txt`
- `使用手册.md`

脚本在 `工具` 里。窗口文字是中文。

选 English 后，新项目最外层是：

- `Project Environment.exe`
- `Read me.txt`
- `User Manual.md`

脚本在 `tools` 里。窗口文字是英文。

语言在创建时定下来。以后要换语言，请用对应语言再生成一个新项目。

## V0.04 比 V0.03 多了什么

- 认 Windows 11 默认打开方式（`UserChoiceLatest`）。
- 新项目第一层只留面板 exe、说明、手册；脚本在 `工具` / `tools`。

## 从 V0.03 起还带着的能力

每个新项目文件夹里有一块板。生成成功后，双击上面的那个 exe。

最上面一个勾：勾上 = 这个项目双击 `.py` 走本项目 `.venv`。这会改**整台电脑**的 VSCode.py（第一次会确认）。没勾的项目会改走备份里原来的打开方式。恢复按钮拆掉整机挂钩。本机若不是 VS Code 打开 `.py`，勾选会被拒绝。

下面：装库、删库（numpy、matplotlib、pandas、openpyxl、pygame、requests、flask、pillow，或自己粘贴库名）。列表只显示你要的库。它们需要的小库也会装上，但不单独列。

项目文件夹里不再放启用/关闭/装库那三个 `.bat`。

生成窗口里那个环境勾，默认不勾。以后要改，打开项目里的这块板。

请把 `.py` 放在 `.venv` 旁边，不要放进去。本文件夹新建的、从别处粘过来的，规则一样。

日常使用，本绿色文件夹第一层只需要：

- `Create Independent Project Python Environment.exe`
- `README.md`（入口，指向「说明」和 `docs`）
- `说明` 文件夹（中文手册，没有隐藏）
- `docs` 文件夹（英文手册，没有隐藏）

源码和方案在旁边的 `Create-Independent-Project-Python-Environment-Source`（本版看 `V0.04`）。不要把源码放进绿色文件夹。

不要上传 `wscript.exe`。
