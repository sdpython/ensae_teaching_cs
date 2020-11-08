"""
@brief      test log(time=3s)
"""
import unittest
import numpy
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.data import interpret_imagenet_results


class TestDataImageNet(ExtTestCase):

    def test_imagenet(self):
        rnd = numpy.random.rand(1000)
        mx = max(rnd)
        res = interpret_imagenet_results(rnd)
        self.assertEqual(len(res), 10)
        mx2 = max(res.values())
        self.assertEqual(mx, mx2)


if __name__ == "__main__":
    unittest.main()
