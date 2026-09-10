"""维护本项目的库。列表只信这个项目 .venv 里 pip 的真实结果；没装完不算已安装。"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import threading
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

COMMON = (
    "numpy",
    "matplotlib",
    "pandas",
    "openpyxl",
    "pygame",
    "requests",
    "flask",
    "pillow",
)
IMPORT_NAME = {
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "pandas": "pandas",
    "openpyxl": "openpyxl",
    "pygame": "pygame",
    "requests": "requests",
    "flask": "flask",
    "pillow": "PIL",
}
SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
PROTECTED = {"pip", "setuptools", "wheel"}


def parse_typed_names(text: str) -> tuple[list[str], list[str]]:
    parts = text.replace(",", " ").replace("，", " ").replace(";", " ").split()
    good: list[str] = []
    skipped: list[str] = []
    seen: set[str] = set()
    for item in parts:
        key = item.lower()
        if not SAFE_NAME.fullmatch(item) or key in PROTECTED:
            skipped.append(item)
            continue
        if key in seen:
            continue
        seen.add(key)
        good.append(item)
    return good, skipped


CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0


def find_venv_python() -> Path | None:
    here = Path(__file__).resolve().parent
    for folder in (here, here.parent):
        py = folder / ".venv" / "Scripts" / "python.exe"
        if py.is_file():
            return py
    return None


def run_venv(py: Path, args: list[str], timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [str(py), *args],
        capture_output=True,
        text=True,
        timeout=timeout,
        creationflags=CREATE_NO_WINDOW,
    )


def pip_list(py: Path, not_required: bool = False) -> list[str]:
    args = ["-m", "pip", "list", "--format=json", "--disable-pip-version-check"]
    if not_required:
        args.append("--not-required")
    result = run_venv(py, args)
    if result.returncode != 0:
        return []
    try:
        rows = json.loads(result.stdout or "[]")
    except json.JSONDecodeError:
        return []
    names = [str(row.get("name", "")).lower() for row in rows if row.get("name")]
    names.sort()
    return names


def pip_list_shown(py: Path) -> list[str]:
    names = pip_list(py, not_required=True)
    return [name for name in names if name not in PROTECTED]


def fill_check_grid(parent: tk.Widget, names: list[str] | tuple[str, ...], vars_map: dict[str, tk.BooleanVar], columns: int = 4) -> None:
    for index, name in enumerate(names):
        row, col = divmod(index, columns)
        tk.Checkbutton(parent, text=name, variable=vars_map[name]).grid(
            row=row, column=col, sticky="w", padx=(0, 18), pady=2
        )


def can_import(py: Path, pip_name: str) -> bool:
    key = pip_name.lower()
    guesses = []
    if key in IMPORT_NAME:
        guesses.append(IMPORT_NAME[key])
    guesses.append(pip_name.replace("-", "_"))
    guesses.append(pip_name)
    seen: set[str] = set()
    for module in guesses:
        if module in seen or not module.isidentifier():
            continue
        seen.add(module)
        result = run_venv(py, ["-c", f"import {module}"])
        if result.returncode == 0:
            return True
    return False


class LibraryWindow:
    def __init__(self) -> None:
        self.py = find_venv_python()
        self.live = self.py is not None
        self.win = tk.Tk()
        self.win.title("维护本项目的库")
        self.win.geometry("820x620")
        self.win.minsize(760, 560)
        self.win.protocol("WM_DELETE_WINDOW", self.on_close)

        self.common_vars = {name: tk.BooleanVar(value=False) for name in COMMON}
        self.installed: list[str] = []
        self.installed_vars: dict[str, tk.BooleanVar] = {}
        self.busy = False
        self.cancel = False
        self.proc: subprocess.Popen[str] | None = None

        if self.live:
            tip = (
                "下面只列出你装过的库。安装时还会带上一些它们需要的小库，那些不单独列出来。"
                "没装完的不会写上去。"
            )
        else:
            tip = "找不到这个项目的 .venv，不能装库。请把本窗口放在项目文件夹里（和 .venv 旁边）。"

        pad = {"padx": 16, "pady": 6}
        tk.Label(self.win, text=tip, wraplength=780, justify="left", fg="#555555").pack(
            anchor="w", **pad
        )

        tk.Label(self.win, text="常用库（勾选后点安装）").pack(anchor="w", padx=16)
        common_box = tk.Frame(self.win)
        common_box.pack(anchor="w", padx=28, pady=4)
        fill_check_grid(common_box, COMMON, self.common_vars)

        tk.Label(self.win, text="上面没有的，把库名粘贴到这里（空格或逗号分开）").pack(
            anchor="w", padx=16, pady=(8, 0)
        )
        self.typed = tk.StringVar()
        self.typed_entry = tk.Entry(self.win, textvariable=self.typed, width=72)
        self.typed_entry.pack(anchor="w", padx=16, pady=4)

        self.install_btn = tk.Button(
            self.win, text="安装勾选的和输入的库", command=self.install_selected, width=22
        )
        self.install_btn.pack(anchor="w", padx=16, pady=8)

        ttk.Separator(self.win, orient="horizontal").pack(fill="x", padx=16, pady=4)
        tk.Label(self.win, text="进度").pack(anchor="w", padx=16, pady=(8, 0))
        mid = tk.Frame(self.win)
        mid.pack(fill="x", padx=16, pady=6)
        self.work = tk.StringVar(value="空闲。勾选库之后点安装，这里会显示正在装什么。")
        tk.Label(mid, textvariable=self.work, wraplength=780, justify="left").pack(anchor="w")
        self.bar = ttk.Progressbar(mid, mode="determinate", maximum=100, length=770)
        self.bar.pack(anchor="w", pady=(8, 0))
        self.percent = tk.StringVar(value="")
        tk.Label(mid, textvariable=self.percent, fg="#555555").pack(anchor="w")

        ttk.Separator(self.win, orient="horizontal").pack(fill="x", padx=16, pady=8)
        head = tk.Frame(self.win)
        head.pack(fill="x", padx=16, pady=(0, 4))
        tk.Label(head, text="本环境已安装的库（勾选后点右边删除）").pack(side="left")
        self.delete_btn = tk.Button(
            head, text="删除勾选的库", command=self.delete_selected, width=16
        )
        self.delete_btn.pack(side="right")

        list_wrap = tk.Frame(self.win)
        list_wrap.pack(fill="both", expand=True, padx=16, pady=4)
        self.canvas = tk.Canvas(list_wrap, height=180, highlightthickness=1)
        scroll = ttk.Scrollbar(list_wrap, orient="vertical", command=self.canvas.yview)
        self.inner = tk.Frame(self.canvas)
        self.inner.bind(
            "<Configure>",
            lambda _e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.canvas.configure(yscrollcommand=scroll.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.status = tk.StringVar(value="")
        tk.Label(self.win, textvariable=self.status, wraplength=780, justify="left").pack(
            anchor="w", padx=16, pady=(0, 12)
        )

        self.reload_installed()
        if not self.live:
            self.set_busy(True)

    def on_close(self) -> None:
        self.cancel = True
        if self.proc is not None and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=3)
            except Exception:
                self.proc.kill()
        self.win.destroy()

    def set_busy(self, busy: bool) -> None:
        self.busy = busy
        state = tk.DISABLED if busy else tk.NORMAL
        self.install_btn.configure(state=state)
        self.delete_btn.configure(state=state)
        self.typed_entry.configure(state=state)

    def reload_installed(self) -> None:
        if self.live and self.py is not None:
            self.installed = pip_list_shown(self.py)
        self.refresh_installed()

    def refresh_installed(self) -> None:
        for child in self.inner.winfo_children():
            child.destroy()
        self.installed_vars = {}
        if not self.installed:
            tk.Label(self.inner, text="（还没有你装的库）", fg="#777777").pack(anchor="w")
            return
        for name in self.installed:
            self.installed_vars[name] = tk.BooleanVar(value=False)
        fill_check_grid(self.inner, self.installed, self.installed_vars)

    def wait_proc(self, args: list[str]) -> int:
        if self.py is None:
            return 1
        self.proc = subprocess.Popen(
            [str(self.py), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            creationflags=CREATE_NO_WINDOW,
        )
        code = self.proc.wait()
        self.proc = None
        return code

    def install_one(self, name: str) -> bool:
        if self.cancel:
            return False
        if not self.live or self.py is None:
            return False
        self.wait_proc(["-m", "pip", "install", name, "--disable-pip-version-check"])
        if self.cancel:
            return False
        if self._really_installed(name):
            return True
        self.wait_proc(
            ["-m", "pip", "install", "--force-reinstall", name, "--disable-pip-version-check"]
        )
        if self.cancel:
            return False
        return self._really_installed(name)

    def _really_installed(self, name: str) -> bool:
        if self.py is None:
            return False
        if can_import(self.py, name):
            return True
        if name.lower() in IMPORT_NAME:
            return False
        return name.lower() in pip_list(self.py, not_required=False)

    def uninstall_one(self, name: str) -> bool:
        if self.cancel:
            return False
        if name.lower() in PROTECTED:
            return False
        if not self.live or self.py is None:
            return False
        self.wait_proc(["-m", "pip", "uninstall", "-y", name, "--disable-pip-version-check"])
        if self.cancel:
            return False
        return name.lower() not in pip_list(self.py)

    def install_selected(self) -> None:
        if self.busy:
            return
        if not self.live:
            messagebox.showerror("维护本项目的库", "找不到这个项目的 .venv，不能装库。")
            return
        have = {name.lower() for name in self.installed}
        pending: list[str] = []
        seen: set[str] = set()
        for name, var in self.common_vars.items():
            if var.get() and name.lower() not in have and name.lower() not in seen:
                pending.append(name)
                seen.add(name.lower())
        typed_raw = self.typed.get().strip()
        typed_names, skipped = parse_typed_names(typed_raw)
        for name in typed_names:
            if name.lower() not in have and name.lower() not in seen:
                pending.append(name)
                seen.add(name.lower())
        for var in self.common_vars.values():
            var.set(False)
        self.typed.set("")
        if skipped:
            messagebox.showinfo(
                "维护本项目的库",
                "这些名字不能用来安装，已跳过：\n" + "、".join(skipped),
            )
        if not pending:
            self.work.set("空闲。")
            self.status.set("没有新的库可加。请勾选上面的库，或在输入框粘贴库名。")
            return
        self._start_job(pending, adding=True)

    def delete_selected(self) -> None:
        if self.busy:
            return
        if not self.live:
            messagebox.showerror("维护本项目的库", "找不到这个项目的 .venv，不能删库。")
            return
        chosen = [name for name, var in self.installed_vars.items() if var.get()]
        blocked = [name for name in chosen if name.lower() in PROTECTED]
        chosen = [name for name in chosen if name.lower() not in PROTECTED]
        if blocked and not chosen:
            messagebox.showinfo("维护本项目的库", "pip / setuptools / wheel 是工具箱自己的，不能删。")
            return
        if not chosen:
            messagebox.showinfo("维护本项目的库", "请先勾选下面要删除的库。")
            return
        if not messagebox.askyesno("维护本项目的库", "确定删除这些库？\n" + "、".join(chosen)):
            return
        self._start_job(chosen, adding=False)

    def _start_job(self, names: list[str], adding: bool) -> None:
        self.cancel = False
        self.set_busy(True)
        self.bar["value"] = 0
        self.percent.set("0%")
        thread = threading.Thread(
            target=self._worker, args=(names, adding), daemon=True
        )
        thread.start()

    def _worker(self, names: list[str], adding: bool) -> None:
        total = len(names)
        ok_names: list[str] = []
        bad_names: list[str] = []
        verb = "安装" if adding else "删除"
        for index, name in enumerate(names):
            if self.cancel:
                break
            self.win.after(0, lambda n=name, i=index: self._show_progress(verb, n, i, total))
            passed = self.install_one(name) if adding else self.uninstall_one(name)
            if self.cancel:
                break
            if passed:
                ok_names.append(name)
            else:
                bad_names.append(name)
            if self.live:
                self.win.after(0, self.reload_installed)
        self.win.after(0, lambda: self._finish(verb, ok_names, bad_names))

    def _show_progress(self, verb: str, name: str, index: int, total: int) -> None:
        self.work.set(f"正在{verb} {name}（{index + 1}/{total}），请等待…")
        done = index / total * 100
        self.bar["value"] = done
        self.percent.set(f"{int(done)}%")

    def _finish(self, verb: str, ok_names: list[str], bad_names: list[str]) -> None:
        if self.live:
            self.reload_installed()
        if self.cancel:
            self.work.set("已停止。没装完的不会出现在下面。")
            self.status.set("刚才被关掉或中断。下面只显示已经真正完成的库。")
            self.set_busy(False)
            return
        self.bar["value"] = 100
        self.percent.set("100%")
        self.work.set("完成，请看下面的列表。")
        parts = []
        if ok_names:
            parts.append(f"{verb}成功：" + "、".join(ok_names))
        if bad_names:
            parts.append("没完成（可再试一次）：" + "、".join(bad_names))
        self.status.set(" ".join(parts) if parts else "没有变化。")
        self.set_busy(False)

    def run(self) -> None:
        self.win.mainloop()


if __name__ == "__main__":
    LibraryWindow().run()
