"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest


try :
    import src
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper

from pyquickhelper import fLOG
from src.ensae_teaching_cs.tutoriel.construction_classique import *


class TestConstructionClassique(unittest.TestCase):
    
    def test_fonctino(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        
        assert recherche([2,3,45],3)==1
        assert recherche([2,3,45],4)==-1
        assert minindex([2,3,45,-1,5]) == (-1,3)

if __name__ == "__main__"  :
    unittest.main ()    
