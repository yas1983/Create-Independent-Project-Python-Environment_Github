"""由隐藏的 _internal.bat 启动：起名并生成该项目自己的 Python 环境。"""

import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

不能用的符号 = '\\/:*?"<>|'
默认位置 = Path(r"D:\vibecoding\cursor\CursorProjects")
窗口标题 = "双击生成独立项目的 Python 环境"


def 创建项目(名称: str, 父文件夹: Path) -> Path:
    名称 = 名称.strip()
    if not 名称:
        raise ValueError("请填写项目名称。")
    if any(符号 in 名称 for 符号 in 不能用的符号):
        raise ValueError('名称里不要包含 \\ / : * ? " < > |')

    目标 = 父文件夹 / 名称
    if 目标.exists():
        raise ValueError(f"已经有这个文件夹了：\n{目标}")

    父文件夹.mkdir(parents=True, exist_ok=True)
    目标.mkdir()

    完成 = subprocess.run(
        [sys.executable, "-m", "venv", str(目标 / ".venv")],
        capture_output=True,
        text=True,
    )
    if 完成.returncode != 0:
        raise ValueError("项目环境生成失败：\n" + (完成.stderr or 完成.stdout or "未知错误"))
    return 目标


def 打开窗口() -> None:
    窗口 = tk.Tk()
    窗口.title(窗口标题)
    窗口.geometry("520x240")
    窗口.resizable(False, False)

    名称变量 = tk.StringVar()
    位置变量 = tk.StringVar(value=str(默认位置))
    状态变量 = tk.StringVar(value="填名称，点创建。不需要打开 Cursor，也不用打命令。")

    def 选择位置() -> None:
        选中 = filedialog.askdirectory(initialdir=位置变量.get() or str(默认位置))
        if 选中:
            位置变量.set(选中)

    def 点创建() -> None:
        状态变量.set("正在生成独立项目环境，请稍等…")
        窗口.update_idletasks()
        try:
            路径 = 创建项目(名称变量.get(), Path(位置变量.get()))
        except Exception as 错误:
            状态变量.set("没成功。")
            messagebox.showerror("没成功", str(错误))
            return
        状态变量.set("完成。")
        messagebox.showinfo(
            "完成",
            "独立 Python 项目环境已建好：\n"
            f"{路径}\n\n"
            "这个项目自己的环境在里面的 .venv 文件夹。\n"
            "以后在那个项目里运行，用：\n"
            ".venv\\Scripts\\python.exe",
        )

    内边 = {"padx": 16, "pady": 6}
    tk.Label(窗口, text="项目名称").grid(row=0, column=0, sticky="w", **内边)
    tk.Entry(窗口, textvariable=名称变量, width=44).grid(row=0, column=1, columnspan=2, **内边)

    tk.Label(窗口, text="放在哪个文件夹").grid(row=1, column=0, sticky="w", **内边)
    tk.Entry(窗口, textvariable=位置变量, width=36).grid(row=1, column=1, **内边)
    tk.Button(窗口, text="浏览…", command=选择位置).grid(row=1, column=2, **内边)

    tk.Button(窗口, text="创建项目", command=点创建, width=16).grid(
        row=2, column=1, sticky="w", padx=16, pady=12
    )
    tk.Label(窗口, textvariable=状态变量, wraplength=460, justify="left").grid(
        row=3, column=0, columnspan=3, sticky="w", **内边
    )

    窗口.mainloop()


if __name__ == "__main__":
    打开窗口()
