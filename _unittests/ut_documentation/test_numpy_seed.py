"""
@brief      test log(time=93s)
@author     Xavier Dupre
"""

import sys
import os
import unittest
import numpy as np


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


class TestShpinxGallery(unittest.TestCase):

    def test_numpy_random(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        np.random.seed(42)


if __name__ == "__main__":
    unittest.main()
