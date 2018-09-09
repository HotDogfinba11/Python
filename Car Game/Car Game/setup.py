import os
import cx_Freeze

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("cargame.pyw")]

cx_Freeze.setup(
    name="Prime Generator",
    options={"build_exe": {"packages":[],
                           "include_files":["start.wav","crash.wav","click.wav","car.png"]}},
    executables = executables

    )
