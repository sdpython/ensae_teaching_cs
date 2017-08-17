"""
@brief      test log(time=50s)

notebook test
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
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a


class TestNotebookRunner2a_2_enonce_2D (unittest.TestCase):

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        # this notebook describes how to distribute the work with multiple processors
        # it requires to start multiple clusters first (a command line)
        # and to stop them afterwards
        # it still needs to be implemented
        # we skip !
        warnings.warn(
            "TODO: implement a unit test testing the distribution on multiple processors")
        return

        temp = get_temp_folder(__file__, "temp_notebook2a_2_enonce_2D")
        keepnote = ls_notebooks("td2a")
        execute_notebooks(temp, keepnote, lambda i, n: "_2" in n and
                          "enonce" in n and
                          "_2D" in n,
                          fLOG=fLOG, clean_function=clean_function_1a,
                          dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
