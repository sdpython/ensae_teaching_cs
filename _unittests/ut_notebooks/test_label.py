"""
@brief      test log(time=1s)
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


class TestLabel(unittest.TestCase):

    def test_label_bom(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.dirname(__file__))
        fhel = os.path.join(
            fold,
            "..",
            "..",
            "_doc",
            "sphinxdoc",
            "build3",
            "html",
            "specials",
            "algorithm_culture.html")
        fhel = os.path.normpath(fhel)
        if os.path.exists(fhel):
            with open(fhel, "r", encoding="utf8") as f:
                content = f.read()
            self.assertTrue(".. _l-algoculture:</p>" not in content)
        else:
            fLOG("unable to test", fhel)


if __name__ == "__main__":
    unittest.main()
