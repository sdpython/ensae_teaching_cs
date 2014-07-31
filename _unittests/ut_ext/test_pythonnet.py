"""
@brief      test log(time=1s)
"""

import sys, os, unittest, re


try :
    import src
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    import src

from pyquickhelper import fLOG


class TestPythonnet(unittest.TestCase):
    
    def test_pythonnet (self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        if sys.platform.startswith("win"):
            from src.ensae_teaching_cs.pythonnet import clr
            from System import String
            s = String("example")
            x = s.Replace("e","j")
            assert "jxamplj" == x
            
            from System.Collections.Generic import Dictionary
            d = Dictionary[String, String]()
            d["un"] = "1"
            assert d.Count == 1
            
    def test_voice(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        if sys.platform.startswith("win"):
            from src.ensae_teaching_cs.pythonnet import vocal_synthesis
            vocal_synthesis("test unitaire")
        


if __name__ == "__main__"  :
    unittest.main ()    
