"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
import re


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
    import pyquickhelper
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
    import pyquickhelper

from pyquickhelper import fLOG
from src.ensae_teaching_cs.faq.faq_jupyter import jupyter_open_notebook


class TestFaqIPython(unittest.TestCase):

    def test_faq_ipython(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nbfile = os.path.abspath(os.path.dirname(__file__))
        nbfile = os.path.join(
            nbfile, "..", "..", "_doc", "notebooks", "1a", "code_liste_tuple.ipynb")
        assert os.path.exists(nbfile)

        if __name__ == "__main__" and "travis" not in sys.executable.lower():
            s = jupyter_open_notebook(nbfile, fLOG=fLOG)
            fLOG(s)


if __name__ == "__main__":
    unittest.main()
