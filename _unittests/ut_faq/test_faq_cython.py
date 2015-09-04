"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import re
import shutil
import warnings

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

try:
    import pyquickhelper
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper

from pyquickhelper import fLOG, get_temp_folder
from src.ensae_teaching_cs.faq.faq_cython import compile_cython_single_script


class TestFaqCython(unittest.TestCase):

    def test_faq_cython_compile(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_cython_primes")
        primes = os.path.join(temp, "..", "primes.pyx")
        shutil.copy(primes, temp)
        newfile = os.path.join(temp, "primes.pyx")
        cwd = os.getcwd()

        if "travis" in sys.executable:
            # the unit test does not end on travis
            warnings.warn("test_faq_cython_compile not test on travis")
            return

        compile_cython_single_script(newfile, fLOG=fLOG)

        # we checked it worked
        assert os.path.exists(os.path.join(temp, "primes.pyd"))

        sys.path.append(temp)
        import primes
        del sys.path[-1]

        p = primes.primes(100)
        fLOG(p)
        assert p == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                     61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
                     139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                     211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
                     281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                     367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                     443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521,
                     523, 541]

        fLOG(os.getcwd())
        assert cwd == os.getcwd()


if __name__ == "__main__":
    unittest.main()
