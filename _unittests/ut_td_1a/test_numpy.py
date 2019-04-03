"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
import numpy
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.td_1a.numpys import numpy_matrix2list


class TestTd1aNumpy(unittest.TestCase):

    def test_numpy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mat = [[0, 1], [1, 9]]
        arr = numpy.array(mat)
        mat2 = numpy_matrix2list(arr)
        self.assertEqual(mat, mat2)


if __name__ == "__main__":
    unittest.main()
