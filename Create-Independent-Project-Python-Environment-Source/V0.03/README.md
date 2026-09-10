# V0.03 源码

对应绿色版文件夹：`Create-Independent-Project-Python-Environment-Green-V0.03`。  
这是当前锁定版本。装库窗口的改动（加宽、只列你装过的库、删除按钮在右边）都写在这一版里，没有另开新号。

## 这一版比 V0.02 多了什么

每个新项目文件夹里多一个装库窗口：

- 双击 `维护本项目的库.bat` 打开
- 上面勾常用库（numpy、matplotlib、pandas、openpyxl、pygame、requests、flask、pillow）
- 中间输入框：自己粘贴库名
- 常用库和已安装的库横排显示
- 下面只列出你装过的库（它们需要的小库不单独列），可勾选后点右边「删除勾选的库」

装库规则：只信这个项目的 `.venv`；没装完、没能用，不算已安装；关掉窗口会停掉当前安装；pip / setuptools / wheel 不能删。

V0.02 的按项目双击开关、启用/关闭、开门程序都还在。没有右键「用项目环境打开」。

## 文件

| 文件 | 作用 |
|------|------|
| `create_project.py` | 窗口、建 `.venv`、写入开关、把装库窗口拷进新项目 |
| `维护本项目的库.py` | 装库窗口。生成时复制到项目文件夹，和 `.venv` 放在一起 |
| `open_py_in_project.cs` | 开门程序。双击 `.py` 时往上找 `.venv`，再看有没有 `use_project_env.on` |

## 建议阅读顺序

1. `create_project.py`：`write_library_manager()`、`write_project_helpers()`
2. `维护本项目的库.py`：常用勾选、输入框、进度、已安装列表
3. `open_py_in_project.cs`：和 V0.02 相同思路
