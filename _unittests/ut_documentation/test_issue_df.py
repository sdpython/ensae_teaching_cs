"""
@brief      test log(time=93s)
@author     Xavier Dupre
"""

import sys
import os
import unittest
import pandas


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
    import pyquickhelper as skip____
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
    import pyquickhelper as skip____


from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyquickhelper.helpgen import rst2html


class TestIssueDf(unittest.TestCase):

    def test_notebook_cov(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fold = os.path.dirname(__file__)
        name = "notebook.ensae_teaching_cs.txt"
        dff = os.path.join(fold, name)
        if os.path.exists(dff):
            df = pandas.read_csv(dff, sep="\t", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
