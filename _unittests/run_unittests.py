"""
@file
@brief run all unit tests
"""

try :
    import src
    import pyquickhelper
except ImportError :
    import os, sys
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper

import unittest, os, io
from pyquickhelper import fLOG
from pyquickhelper.unittests.utils_tests import main 



if __name__ == "__main__" :
    fLOG(OutputPrint = True)
        
    runner  = unittest.TextTestRunner(verbosity=0, stream = io.StringIO ())
    path    = os.path.abspath(os.path.join(os.path.split(__file__) [0]))
    res     = main(runner, path_test = path, skip = -1)
    for r in res :
        k = str (r [1])
        if "errors=0" not in k or "failures=0" not in k :
            print ("*", r[1], r[0])

