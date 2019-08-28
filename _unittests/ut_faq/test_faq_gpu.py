"""
@brief      test log(time=7s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase, skipif_circleci
from ensae_teaching_cs.faq.faq_gpu import pyopencl_status


class TestFaqGPU(ExtTestCase):

    @skipif_circleci("Received 'segmentation fault' signal")
    def test_pyopencl_status(self):
        res = pyopencl_status()
        self.assertNotEmpty(res)
        self.assertTrue("===" in res or "pyopencl is not available due" in res)


if __name__ == "__main__":
    unittest.main()
