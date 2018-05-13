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

from src.ensae_teaching_cs.td_1a.numpys import numpy_matrix2list


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
