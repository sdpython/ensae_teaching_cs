"""
@brief      test log(time=40s)
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


class TestNotebookEleves(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def get_replacements(self):
        return {"https://archive.ics.uci.edu/ml/machine-learning-databases/00222/":
                "http://www.xavierdupre.fr/enseignement/complements/"}

    def test_notebook_runner_eleves(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        temp = get_temp_folder(__file__, "temp_notebook_eleves")
        keepnote = ls_notebooks("notebook_eleves/2016-2017")
        self.assertTrue(len(keepnote) > 0)
        execute_notebooks(temp, keepnote, (lambda i, n: True), fLOG=fLOG,
                          replacements=self.get_replacements(), dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
