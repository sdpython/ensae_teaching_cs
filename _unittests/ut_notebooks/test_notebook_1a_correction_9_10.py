#-*- coding: utf-8 -*-
"""
@brief      test log(time=9s)
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
    import pyquickhelper as skip____
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
    import pyquickhelper as skip____

try:
    import pyensae as skip___
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae as skip___

try:
    import pymmails as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymmails",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymmails as skip__


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a, unittest_raise_exception_notebook


class TestNotebookRunner1a_correction (unittest.TestCase):

    def test_notebook_runner_correction_9_10(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_correction_9_10")
        keepnote = ls_notebooks("td1a")
        assert len(keepnote) > 0
        if is_travis_or_appveyor() == "travis":
            warnings.warn("too long")
            return
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "_12" not in n and
                                "session1." not in n and
                                "session2." not in n and
                                "session3." not in n and
                                "session4." not in n and
                                "session5." not in n and
                                "session6." not in n and
                                "session7." not in n and
                                "session8." not in n and
                                "session_11." not in n and
                                "correction" in n,
                                fLOG=fLOG,
                                clean_function=clean_function_1a)
        unittest_raise_exception_notebook(res, fLOG)


if __name__ == "__main__":
    unittest.main()
