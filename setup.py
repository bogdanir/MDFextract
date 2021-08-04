from distutils.core import setup
import os
import sys
import py2exe

# sys.setrecursionlimit(15000)
sys.path.append('C:\\Users\\irimescub\\Downloads')


includes = ['os', 'sys', 'mdfreader', 'webbrowser', 'pandas', 'tkinter', 'lxml._elementpath']
excludes = []
packages = []
dll_excludes = []

#os.environ['$env:TCL_LIBRARY'] = r'C:\Program Files\Python27\tcl\tcl8.5'
#os.environ['$env:TK_LIBRARY'] = r'C:\Program Files\Python27\tcl\tk8.5'

Base = None
if sys.platform == "win32":
    Base = "Win32GUI"
script_file = 'C:\\Users\\irimescub\\PycharmProjects\\MDFextractALL\\FolderMDFReader_ExtractALL.py'
setup(options = {"py2exe": {"compressed": 0,
                          "skip_archive": 1,
                          "optimize": 0,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "dist_dir": ".",
                          "xref": False,
                          "ascii": False,
                          "custom_boot_script": '',
                            }
                 },
      console = [{'script': script_file}])
