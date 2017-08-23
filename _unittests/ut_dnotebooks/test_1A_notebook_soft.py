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
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version


class TestNotebookRunner1a_soft(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper", "mlstatpy"],
                                        __file__, hide=True)

    def test_notebook_runner_enonce_soft(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_soft")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        keepnote = ls_notebooks("td1a_soft")
        execute_notebooks(temp, keepnote,
                          lambda i, n: True,
                          fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
