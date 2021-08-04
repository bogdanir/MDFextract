import sys
# sys.setrecursionlimit(10000)
from cx_Freeze import setup, Executable
import os
import tkinter

sys.path.append('C:\\Users\\irimescub\\Downloads')
# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []
packages = ["Tkinter", 'scipy', 'scipy_path']

build_exe_options = {"includes": ['os', 'sys', 'mdfreader', 'webbrowser', 'pandas', 'tkinter', 'lxml._elementpath', 'os', 'xlsxwriter'],
                     "excludes": [''],
                     "include_files": []
                     }

base = None

if sys.platform == "win32":
   base = "Win32GUI"

setup(name="SRAHelperTool",
      version="1.0",
      description="SRA Helper",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="SRA Helper TOOL.py", base=base)])
