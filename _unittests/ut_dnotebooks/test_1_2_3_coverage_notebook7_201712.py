#-*- coding: utf-8 -*-
"""
@brief      test log(time=13s)
"""

import sys
import os
import unittest


try:
    import src.ensae_teaching_cs as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src.ensae_teaching_cs as skip__

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
from pyquickhelper.pycode import add_missing_development_version


class TestNotebook1237Coverage201712(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def a_test_notebook_runner(self, name, folder, valid=None, copy_files=None, modules=None):
        from src.ensae_teaching_cs.automation.notebook_test_helper import a_test_notebook_runner
        return a_test_notebook_runner(__file__, name, folder, valid=valid,
                                      copy_files=copy_files, modules=modules, fLOG=fLOG)

    def test_notebook_dimensions_reduction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner(
            "dimensions_reduction", "notebook_eleves/2017-2018")

    def test_notebook_git_notebook(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("git_notebook", "2a")

    def test_notebook_td2a_bigdata_memory(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("td2a_bigdata_memory", "td2a")

    def test_notebook_td1a_pyramide_bigarre(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("bigarree", "td1a")


if __name__ == "__main__":
    unittest.main()
