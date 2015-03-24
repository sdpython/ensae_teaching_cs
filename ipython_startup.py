import os
import sys
path = os.path.abspath(os.path.dirname(__file__))
for p in ["pyensae", "pyquickhelper", "ensae_teaching_cs",
          "pymyinstall", "pyrsslocal", "pymmails", "pysqllike",
          "code_beatrix", "actuariat_python"]:
    pa = os.path.normpath(os.path.join(path, "..", p, "src"))
    sys.path.append(pa)
