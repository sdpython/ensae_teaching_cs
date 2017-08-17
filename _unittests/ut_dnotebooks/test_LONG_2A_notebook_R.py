#-*- coding: utf-8 -*-
"""
@brief      test log(time=93s)
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


class TestNotebookRunner2a_long (unittest.TestCase):

    def setUp(self):
        from pyquickhelper.pycode import add_missing_development_version
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=__name__ == "__main__")

    def test_notebook_runner_2a_long(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            # skip travis and R
            warnings.warn(
                "travis, unable to test TestNotebookRunner2a_long.test_notebook_runner_2a_long")
            return

        if "R_HOME" not in os.environ or not os.path.exists(os.environ["R_HOME"]):
            paths = [r"C:\Program Files\R\R-3.2.4revised",
                     r"C:\Program Files\R\R-3.2.4",
                     r"C:\Program Files\R\R-3.2.3",
                     r"C:\Program Files\R\R-3.2.2"]
            for path in paths:
                if os.path.exists(path):
                    os.environ["R_HOME"] = path
                    break
        if "R_HOME" not in os.environ:
            warnings.warn("No installed R")
            return

        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        from src.ensae_teaching_cs.automation.notebook_test_helper import clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_long_")
        keepnote = ls_notebooks("2a")
        execute_notebooks(temp, keepnote, (lambda i, n: "python_r" in n), fLOG=fLOG,
                          clean_function=clean_function_1a, dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
