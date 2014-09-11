import os, sys
path = os.path.abspath(os.path.dirname(__file__))
for p in ["pyensae", "pyquickhelper", "ensae_teaching_cs", "pymyinstall", "pyrsslocal", "pymmails", "pysqllike"] :
    pa = os.path.normpath(os.path.join(path, "..",p, "src"))
    sys.path.append(pa)
