"""
@brief      test log(time=93s)
"""
import unittest
import numpy as np
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
