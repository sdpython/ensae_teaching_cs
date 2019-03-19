"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
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

from src.ensae_teaching_cs.faq.faq_gpu import pyopencl_status


class TestFaqGPU(ExtTestCase):

    def test_pyopencl_status(self):
        res = pyopencl_status()
        self.assertNotEmpty(res)
        self.assertIn('===', res)


if __name__ == "__main__":
    unittest.main()
