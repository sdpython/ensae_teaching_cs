"""
@brief      test log(time=20s)
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

try:
    import jyquickhelper as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "jyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import jyquickhelper as skip__

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, add_missing_development_version


class TestNotebookRunner2a_2_enonce(unittest.TestCase):

    def setUp(self):
        fLOG("add missing dependencing")
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_2_enonce")
        keepnote = ls_notebooks("td2a")

        if is_travis_or_appveyor() in ('travis', 'appveyor'):
            warnings.warn(
                "travis or appveyor, unable to test TestNotebookRunner2a_2_enonce.test_notebook_runner")
            return

        fold = os.path.dirname(keepnote[0])
        for png in os.listdir(fold):
            if ".png" not in png:
                continue
            fLOG("copy", png)
            shutil.copy(os.path.join(fold, png), temp)
        self.assertTrue(len(keepnote) > 0)

        execute_notebooks(temp, keepnote, lambda i, n: "_2" in n and
                          "enonce" in n and
                          "_2D" not in n and
                          "_2B" not in n,
                          fLOG=fLOG, clean_function=clean_function_1a,
                          dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
