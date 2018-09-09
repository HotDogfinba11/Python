import os
import cx_Freeze

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("Lesson.py")]

cx_Freeze.setup(
    name="Converter",
    options={"build_exe": {"packages":[],
                           "include_files":["lesson.py","array.py"]}},
    executables = executables

    )
