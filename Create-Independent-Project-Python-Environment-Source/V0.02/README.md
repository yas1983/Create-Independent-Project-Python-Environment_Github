# V0.02 源码

对应绿色版文件夹：`Create-Independent-Project-Python-Environment-Green-V0.02`。

## 这一版比 V0.01 多了什么

- 生成窗口多一个勾：这个项目里双击 `.py` 是否用本项目的 `.venv`
- 每个项目里有「启用：双击用本环境.bat」和「关闭：双击用系统 Python.bat」
- 写入 `.vscode/settings.json`
- 开门程序：双击 `.py` 时看这个项目开没开开关

没有右键「用项目环境打开」。

## 文件

| 文件 | 作用 |
|------|------|
| `create_project.py` | 窗口、建 `.venv`、勾选、往项目里写开关和 settings |
| `open_py_in_project.cs` | 开门程序。双击 `.py` 时往上找 `.venv`，再看有没有 `use_project_env.on` |

## 建议阅读顺序

1. `create_project.py`：`write_project_helpers()`（项目里写下什么）、`create_project()`（勾了会怎样）
2. `open_py_in_project.cs`：`FindProjectFolder`、`use_project_env.on`、怎样打开 VS Code
