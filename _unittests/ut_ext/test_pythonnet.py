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

try :
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import pyquickhelper

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
            try:
                vocal_synthesis("test unitaire")
            except Exception as e :
                if "Audio device error encountered" in str(e):
                    # maybe the script is running on a virtual machine (no Audia device)
                    if os.environ["USERNAME"] == "ensaestudent":
                        # I would prefer to catch a proper exception
                        # it just exclude one user only used on remotre machines
                        return
                raise e





if __name__ == "__main__"  :
    unittest.main ()