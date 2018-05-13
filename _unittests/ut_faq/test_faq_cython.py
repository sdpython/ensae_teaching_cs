"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import shutil
import warnings
import platform
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor

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


class TestFaqCython(unittest.TestCase):

    def test_faq_cython_compile(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.ensae_teaching_cs.faq.faq_cython import compile_cython_single_script
        temp = get_temp_folder(__file__, "temp_cython_primes")
        primes = os.path.join(temp, "..", "primes.pyx")
        shutil.copy(primes, temp)
        newfile = os.path.join(temp, "primes.pyx")
        cwd = os.getcwd()

        if is_travis_or_appveyor() == "travis":
            # the unit test does not end on travis
            warnings.warn("test_faq_cython_compile not test on travis")
            return

        compile_cython_single_script(newfile, fLOG=fLOG, skip_warn=False)

        # we checked it worked
        res = platform.architecture()
        if sys.platform.startswith("win"):
            ext = "win_amd64" if res[0] == "64bit" else "win32"
            name = "primes.cp%d%d-%s.pyd" % (
                sys.version_info[0], sys.version_info[1], ext)
        else:
            ext = "x86_64-linux-gnu" if res[0] == "64bit" else "x86-linux-gnu"
            name = "primes.cpython-%d%dm-%s.so" % (
                sys.version_info[0], sys.version_info[1], ext)
        fname = os.path.join(temp, name)
        fLOG(fname)
        if not os.path.exists(fname):
            raise FileNotFoundError("Not found: '{0}'. Found:\n{1}".format(
                fname, "\n".join(os.listdir(temp))))

        sys.path.append(temp)
        import primes
        del sys.path[-1]

        p = primes.primes(100)
        fLOG(p)
        self.assertEqual(p, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                             61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
                             139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                             211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
                             281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                             367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                             443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521,
                             523, 541])

        fLOG(os.getcwd())
        self.assertEqual(cwd, os.getcwd())


if __name__ == "__main__":
    unittest.main()
