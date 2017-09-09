#-*- coding: utf-8 -*-
"""
@brief      test log(time=51s)
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
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version


class TestNotebookRunner1a_correction (unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    def test_notebook_runner_correction_1_7(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook1a_correction_1_7")
        keepnote = ls_notebooks("td1a")

        cp = os.path.join(temp, "..", "data", "seance4_excel.txt")
        shutil.copy(cp, temp)
        cp = os.path.join(temp, "..", "data", "seance4_excel.xlsx")
        shutil.copy(cp, temp)

        execute_notebooks(temp, keepnote,
                          lambda i, n: "_12" not in n and
                          "session6." not in n and
                          "session8." not in n and
                          "session9." not in n and
                          "session_10." not in n and
                          "session_11." not in n and
                          "deviner" not in n and
                          "correction" in n,
                          fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
