"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
import numpy
from pyquickhelper.pycode import ExtTestCase


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

from src.ensae_teaching_cs.ml.gini import gini


class TestGini(ExtTestCase):

    def test_gini(self):
        Y = numpy.array([1, 1, 1, 1, 1, 1])
        g = gini(Y)
        self.assertEqual(g, 0.5)

        Y = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        g = gini(Y)
        self.assertEqual(g, 0.9)

        Y = numpy.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        g = gini(Y, X=numpy.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 11]))
        self.assertEqual(g, 0.7)


if __name__ == "__main__":
    unittest.main()
