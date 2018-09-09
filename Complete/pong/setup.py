import os
import cx_Freeze

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("pong.py")]

cx_Freeze.setup(
    name="Pong",
    options={"build_exe": {"packages":[],
                           "include_files":["pong.py","pong.png"]}},
    executables = executables

    )
