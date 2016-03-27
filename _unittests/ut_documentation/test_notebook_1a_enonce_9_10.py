#-*- coding: utf-8 -*-
"""
@brief      test log(time=17s)

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
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a, unittest_raise_exception_notebook


class TestNotebookRunner1a_enonce (unittest.TestCase):

    def test_notebook_runner_enonce_9_10(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_enonce_9_10")
        keepnote = ls_notebooks("td1a")
        assert len(keepnote) > 0
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "_12" not in n and
                                "cenonce_session1." not in n and
                                "cenonce_session2." not in n and
                                "cenonce_session3." not in n and
                                "cenonce_session4." not in n and
                                "cenonce_session5." not in n and
                                "cenonce_session6." not in n and
                                "cenonce_session7." not in n and
                                "cenonce_session8." not in n and
                                "cenonce_session_11." not in n and
                                "enonce" in n,
                                fLOG=fLOG,
                                clean_function=clean_function_1a)
        unittest_raise_exception_notebook(res, fLOG)

if __name__ == "__main__":
    unittest.main()
