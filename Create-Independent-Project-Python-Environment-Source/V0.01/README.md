# V0.01 源码

对应绿色版文件夹：`Create-Independent-Project-Python-Environment-Green`（文件夹名没有版本号，视为 V0.01）。

## 这一版做什么

窗口里填项目名、选保存位置，创建一个文件夹，并在里面生成独立的 `.venv`。

没有「双击 .py 用本环境」的勾，也没有启用/关闭开关。

## 文件

| 文件 | 作用 |
|------|------|
| `create_project.py` | 整个窗口程序。打包成绿色 exe 的就是这份。 |

先看 `create_project.py` 里的 `create_project()`（建文件夹和 `.venv`），再看 `open_window()`（界面）。
