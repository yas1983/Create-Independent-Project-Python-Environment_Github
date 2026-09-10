"""Started by hidden _internal.bat or the portable .exe: name a folder and create that project's Python environment."""

import shutil
import subprocess
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

FORBIDDEN = '\\/:*?"<>|'
DEFAULT_PARENT = Path(r"D:\vibecoding\cursor\CursorProjects")
WINDOW_TITLE = "Create Independent Project Python Environment"


def resolve_python() -> str:
    """venv needs a real python.exe, not this program when it is packed as .exe."""
    if not getattr(sys, "frozen", False):
        return sys.executable

    anaconda = Path(r"D:\Programs\anaconda\python.exe")
    if anaconda.is_file():
        return str(anaconda)

    which = shutil.which("python")
    if which:
        path = Path(which)
        if path.is_file() and "windowsapps" not in str(path).lower():
            return str(path)

    py_launcher = shutil.which("py")
    if py_launcher:
        return py_launcher

    raise ValueError(
        "Python was not found on this computer.\n"
        "Install Python first (see Complete User Manual.md), then try again."
    )


def create_project(name: str, parent: Path) -> Path:
    name = name.strip()
    if not name:
        raise ValueError("Please enter a project name.")
    if any(ch in name for ch in FORBIDDEN):
        raise ValueError('Do not use these characters in the name: \\ / : * ? " < > |')

    dest = parent / name
    if dest.exists():
        raise ValueError(f"A folder with this name already exists:\n{dest}")

    parent.mkdir(parents=True, exist_ok=True)
    dest.mkdir()

    python = resolve_python()
    cmd = [python, "-m", "venv", str(dest / ".venv")]
    if Path(python).name.lower() == "py.exe":
        cmd = [python, "-3", "-m", "venv", str(dest / ".venv")]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise ValueError(
            "Could not create the project environment:\n"
            + (result.stderr or result.stdout or "Unknown error")
        )
    return dest


def open_window() -> None:
    window = tk.Tk()
    window.title(WINDOW_TITLE)
    window.geometry("560x250")
    window.resizable(False, False)

    name_var = tk.StringVar()
    place_var = tk.StringVar(value=str(DEFAULT_PARENT))
    status_var = tk.StringVar(
        value="Enter a name and click Create. No command line needed."
    )

    def browse() -> None:
        chosen = filedialog.askdirectory(initialdir=place_var.get() or str(DEFAULT_PARENT))
        if chosen:
            place_var.set(chosen)

    def on_create() -> None:
        status_var.set("Creating an independent project environment. Please wait…")
        window.update_idletasks()
        try:
            path = create_project(name_var.get(), Path(place_var.get()))
        except Exception as err:
            status_var.set("Did not succeed.")
            messagebox.showerror("Did not succeed", str(err))
            return
        status_var.set("Done.")
        messagebox.showinfo(
            "Done",
            "Independent Python project environment created:\n"
            f"{path}\n\n"
            "This project's own environment is the .venv folder inside it.\n"
            "Later, run files with:\n"
            ".venv\\Scripts\\python.exe",
        )

    pad = {"padx": 16, "pady": 6}
    tk.Label(window, text="Project name").grid(row=0, column=0, sticky="w", **pad)
    tk.Entry(window, textvariable=name_var, width=44).grid(
        row=0, column=1, columnspan=2, **pad
    )

    tk.Label(window, text="Save in folder").grid(row=1, column=0, sticky="w", **pad)
    tk.Entry(window, textvariable=place_var, width=36).grid(row=1, column=1, **pad)
    tk.Button(window, text="Browse…", command=browse).grid(row=1, column=2, **pad)

    tk.Button(window, text="Create project", command=on_create, width=16).grid(
        row=2, column=1, sticky="w", padx=16, pady=12
    )
    tk.Label(window, textvariable=status_var, wraplength=500, justify="left").grid(
        row=3, column=0, columnspan=3, sticky="w", **pad
    )

    window.mainloop()


def warn_if_python_missing() -> bool:
    """When packed as exe, stop at a dialog if Python is not installed. True = continue."""
    if not getattr(sys, "frozen", False):
        return True
    try:
        resolve_python()
        return True
    except ValueError:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(
            "Python not found",
            "Python is not installed on this computer.\n\n"
            "Please open Complete User Manual.md in this same folder "
            "and follow the steps to install Python.\n\n"
            "Click OK, then install it yourself. "
            "Run this program again after Python is ready.",
        )
        root.destroy()
        return False


if __name__ == "__main__":
    if warn_if_python_missing():
        open_window()
