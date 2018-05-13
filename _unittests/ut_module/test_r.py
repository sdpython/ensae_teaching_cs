"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG


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


from src.ensae_teaching_cs.faq.faq_jupyter import r_and_notebook


class TestR (unittest.TestCase):

    def test_r(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "R_HOME" not in os.environ:
            warnings.warn("R is not installed")
            return

        assert r_and_notebook()


if __name__ == "__main__":
    unittest.main()
