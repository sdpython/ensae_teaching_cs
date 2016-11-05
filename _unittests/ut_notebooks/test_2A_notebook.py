#-*- coding: utf-8 -*-
"""
@brief      test log(time=23s)
"""

import sys
import os
import unittest
import warnings

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


class TestNotebookRunner2a_ (unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    def test_notebook_runner_2a(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if is_travis_or_appveyor() == "appveyor":
            # too long for appveyor
            return
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a, unittest_raise_exception_notebook
        temp = get_temp_folder(__file__, "temp_notebook2a_")
        keepnote = ls_notebooks("2a")
        assert len(keepnote) > 0

        def filter(i, n):
            if not sys.platform.startswith("win") and "_convert" in n:
                return False
            if "git_" not in n and "python_r" not in n and "csharp" not in n:
                return True
            if is_travis_or_appveyor() and "notebook_convert.ipynb" in n:
                # this one requires pandoc
                return False
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
