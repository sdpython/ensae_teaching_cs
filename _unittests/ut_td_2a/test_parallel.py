"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
import numpy
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

from src.ensae_teaching_cs.td_2a import ParallelThread


class TestParallel(unittest.TestCase):

    def test_parallel(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def inv(m):
            return numpy.linalg.inv(m)

        nps = [[numpy.random.random((5, 5))] for i in range(0, 1000)]
        mm = ParallelThread.parallel(inv, nps, 10)
        fLOG(len(mm))
        self.assertEqual(len(mm), 1000)


if __name__ == "__main__":
    unittest.main()
