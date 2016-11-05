#-*- coding: utf-8 -*-
"""
@brief      test log(time=1800s)
"""

import sys
import os
import unittest
import warnings
import shutil

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
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, add_missing_development_version


class TestLongNotebookRunner2aML(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_long_notebook_runner_2a_ml(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if is_travis_or_appveyor() == "appveyor":
            # too long for appveyor
            return
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a, unittest_raise_exception_notebook
        from src.ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_eco")
        keepnote = ls_notebooks("td2a_ml")
        assert len(keepnote) > 0
        shutil.copy(simple_database(), temp)

        def filter(i, n):
            if "deep_python" in n:
                return True
            return False

        if is_travis_or_appveyor() == "travis":
            warnings.warn("execution does not stop")
            return

        res = execute_notebooks(temp, keepnote,
                                filter,
                                fLOG=fLOG,
                                clean_function=clean_function_1a)
        unittest_raise_exception_notebook(res, fLOG)


if __name__ == "__main__":
    unittest.main()
