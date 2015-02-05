#-*- coding: utf-8 -*-
"""
@brief      test log(time=27s)
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

try :
    import pyensae
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyensae", "src")))
    if path not in sys.path : sys.path.append (path)
    import pyensae

try :
    import pymmails
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pymmails", "src")))
    if path not in sys.path : sys.path.append (path)
    import pymmails

from pyquickhelper import fLOG, get_temp_folder
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a


class TestNotebookRunnerExpose1(unittest.TestCase):

    def test_notebook_runner_expose1(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebookexpose1_")
        keepnote = ls_notebooks("expose")
        assert len(keepnote)>0
        res = execute_notebooks(temp, keepnote,
                lambda i,n : "velib" not in n and "paris_parcours" not in n \
                    and "ml_table_mortalite" not in n,
                fLOG=fLOG,
                clean_function = clean_function_1a)
        assert len(res) > 0
        fails = [ (os.path.split(k)[-1],v) for k,v in sorted(res.items()) if not v[0] ]
        for f in fails: fLOG(f)
        if len(fails) > 0 : raise fails[0][1][1]

if __name__ == "__main__"  :
    unittest.main ()