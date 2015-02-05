#-*- coding: utf-8 -*-
"""
@brief      test log(time=90s)

notebook test
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
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks


class TestNotebookRunner1a_enonce_12 (unittest.TestCase):

    @staticmethod
    def clean_function(code):
        code = code.replace('run_cmd("exemple.xlsx"', 'skip_run_cmd("exemple.xlsx"')

        skip = ['df["difference"] = ...',
                "df.plot (...)",
                ]
        for s in skip:
            if s in code:
                return ""
        return code

    def test_notebook_runner_enonce_12(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_enonce_12")
        keepnote = ls_notebooks("td1a")
        assert len(keepnote)>0
        res = execute_notebooks(temp, keepnote,
                lambda i,n : "cenonce_session_12" in n,
                fLOG=fLOG,
                clean_function = TestNotebookRunner1a_enonce_12.clean_function)
        assert len(res) > 0
        fails = [ (os.path.split(k)[-1],v) for k,v in sorted(res.items()) if not v[0] ]
        for f in fails: fLOG(f)
        if len(fails) > 0 : raise fails[0][1][1]

if __name__ == "__main__"  :
    unittest.main ()