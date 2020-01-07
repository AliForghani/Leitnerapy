import sys
import os
from random import randrange, uniform
from cx_Freeze import setup, Executable
import tkinter
import pandas


PYTHON_INSTALL_DIR=os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


build_exe_options = {"include_msvcr": True, "packages": ["tkinter",'numpy.core._methods', 'numpy.lib.format', "pandas"]}


#build_exe_options = {
#"include_msvcr": True   #skip error msvcr100.dll missing}

base =None

if sys.platform=='win32':
	base = "Win32GUI"

setup( name = "Any Name", options={"build_exe": build_exe_options },version = "3.1", description = "Any Description you like", executables = [Executable("Words.py", base = base,icon="W.ico")])