"""
@brief      test log(time=4s)
"""

import sys, os, unittest, re


try :
    import src
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    import src

try :
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import pyquickhelper

from pyquickhelper import fLOG
from src.ensae_teaching_cs.mypython.custom_magics import CustomMagics



class TestCustomMagic (unittest.TestCase):
    
    def test_voice(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        return
        if sys.platform.startswith("win"):
            cm = CustomMagics()
            cm.SPEAK("fr-FR", "hello")
            
    def test_cs(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        if sys.platform.startswith("win"):
            cm = CustomMagics()
            code = "public static double SquareX(double x) {return x*x ; }"
            f = cm.CS("SquareX", code)
            x = f (2.0)
            assert x == 4
        
        

if __name__ == "__main__"  :
    unittest.main ()    
