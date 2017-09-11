#-*- coding: utf-8 -*-
"""
@brief      test log(time=18s)
"""

import sys
import os
import unittest
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


class TestNotebookRunner2aAlgo(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner_2a_algo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if is_travis_or_appveyor() == "appveyor":
            # too long for appveyor
            return
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from src.ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_algo")
        keepnote = ls_notebooks("td2a_algo")
        shutil.copy(simple_database(), temp)

        def filter(i, n):
            if "SNCF" in n:
                return False
            return True

        def clean_function_1a_upgraded(code):
            code = clean_function_1a(code)
            rep = "[1000, 2000, 5000, 10000, 12000, 15000, 17000, 20000]"
            by = "[1000, 2000]"
            code = code.replace(rep, by)
            rep = "[10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]"
            by = "[10, 20, 50, 100, 200]"
            code = code.replace(rep, by)
            return code

        if is_travis_or_appveyor() == "travis":
            # execution does not stop
            return

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          clean_function=clean_function_1a_upgraded,
                          dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
