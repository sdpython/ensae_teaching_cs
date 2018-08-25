# -*- coding: utf-8 -*-
"""
@brief      test log(time=23s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_appveyor, skipif_travis, add_missing_development_version

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


class TestNotebookRunner2a_(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    @skipif_appveyor("too long for appveyor")
    @skipif_travis("execution does not stop")
    def test_notebook_runner_2a(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_")
        keepnote = ls_notebooks("2a")

        def filter(i, n):
            if "seance_5" in n:
                return False
            if "bayesian_with_python" in n:
                return False
            if "cffi" in n:
                return False
            return "git_" not in n and "python_r" not in n and "csharp" not in n

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
