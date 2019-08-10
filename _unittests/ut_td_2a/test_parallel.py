"""
@brief      test log(time=1s)
"""
import unittest
import numpy
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.td_2a import ParallelThread


class TestParallel(unittest.TestCase):

    def test_parallel(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def inv(m):
            return numpy.linalg.inv(m)

        nps = [[numpy.random.random((5, 5))] for i in range(0, 1000)]  # pylint: disable=E1101
        mm = ParallelThread.parallel(inv, nps, 10)
        fLOG(len(mm))
        self.assertEqual(len(mm), 1000)


if __name__ == "__main__":
    unittest.main()
