#-*- coding: utf-8 -*-
"""
@brief      test log(time=20s)

notebook test
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, unittest_raise_exception_notebook


class TestNotebookRunner1a_correction_11 (unittest.TestCase):

    @staticmethod
    def clean_function(code):
        code = code.replace(
            'run_cmd("exemple.xlsx"',
            'skip_run_cmd("exemple.xlsx"')

        skip = []
        for s in skip:
            if s in code:
                return ""
        return code

    def test_notebook_runner_correction_11(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_correction_11")
        keepnote = ls_notebooks("td1a")
        assert len(keepnote) > 0
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "correction_session_11" in n,
                                fLOG=fLOG,
                                clean_function=TestNotebookRunner1a_correction_11.clean_function)
        unittest_raise_exception_notebook(res, fLOG)

if __name__ == "__main__":
    unittest.main()
