"""
@brief      test log(time=620s)

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


class TestNotebookRunner2a_3 (unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    def test_notebook_runner_enonce(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, unittest_raise_exception_notebook, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_3_enonce")
        keepnote = ls_notebooks("td2a")
        assert len(keepnote) > 0
        res = execute_notebooks(
            temp, keepnote, lambda i, n: "_3" in n and "enonce" in n,
            clean_function=clean_function_1a)
        unittest_raise_exception_notebook(res, fLOG)

    def test_notebook_runner_correction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, unittest_raise_exception_notebook, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_3_correction")
        keepnote = ls_notebooks("td2a")
        assert len(keepnote) > 0
        res = execute_notebooks(
            temp, keepnote, lambda i, n: "_3" in n and "correction" in n,
            clean_function=clean_function_1a)
        unittest_raise_exception_notebook(res, fLOG)

if __name__ == "__main__":
    unittest.main()
