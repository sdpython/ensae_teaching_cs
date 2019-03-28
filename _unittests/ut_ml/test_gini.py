"""
@brief      test log(time=2s)
"""
import unittest
import numpy
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.ml.gini import gini


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
