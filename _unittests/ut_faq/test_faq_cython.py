"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import warnings
import platform
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor


class TestFaqCython(unittest.TestCase):

    primes_pyx = """
                    def primes(int kmax):
                        cdef int n, k, i
                        cdef int p[1000]
                        result = []
                        if kmax > 1000:
                            kmax = 1000
                        k = 0
                        n = 2
                        while k < kmax:
                            i = 0
                            while i < k and n % p[i] != 0:
                                i = i + 1
                            if i == k:
                                p[k] = n
                                k = k + 1
                                result.append(n)
                            n = n + 1
                        return result
    """.replace('                    ', '')

    def test_faq_cython_compile(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from ensae_teaching_cs.faq.faq_cython import compile_cython_single_script
        temp = get_temp_folder(__file__, "temp_cython_primes")
        newfile = os.path.join(temp, "primes.pyx")
        with open(newfile, "w") as f:
            f.write(TestFaqCython.primes_pyx)
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
