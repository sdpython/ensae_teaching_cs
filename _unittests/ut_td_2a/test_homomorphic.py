"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
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
    import src
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
from src.ensae_teaching_cs.td_2a.homomorphic import HomomorphicInt


class TestHomomorphic(ExtTestCase):

    def test_homorphic_int_0(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        for x in range(0, 34):
            i = HomomorphicInt(x, 5, 7)
            c = i.crypt_add()
            d = c.decrypt_add()
            self.assertEqual(i.V, d.V)
            c = i.crypt_mult()
            d = c.decrypt_mult()
            self.assertEqual(i.V, d.V)

    def test_homorphic_int(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        i = HomomorphicInt(3)
        j = HomomorphicInt(4)
        self.assertEqual((i * j).V, 12)
        self.assertEqual((i + j).V, 7)
        k = i.inv()
        self.assertEqual((k * i).V, 1)
        self.assertEqual((j - i).V, 1)
        self.assertEqual((i - j).V, i.N - 1)
        i = HomomorphicInt(5, 10)
        self.assertRaise(lambda: i.inv(), ZeroDivisionError)

        i = HomomorphicInt(3)
        c = i.crypt_mult()
        dc = c.decrypt_mult()
        self.assertEqual(i.V, dc.V)
        c = i.crypt_add()
        dc = c.decrypt_add()
        self.assertEqual(i.V, dc.V)

        # Multiplication
        c1 = HomomorphicInt(3, 5, 7)
        c2 = c1.new_int(4)
        c12 = c1 * c2
        cc1 = c1.crypt_mult()
        cc2 = c2.crypt_mult()
        cc12 = c12.crypt_mult()
        cc = cc2 * cc1
        self.assertEqual(cc12.V, cc.V)
        dc = cc.decrypt_mult()
        self.assertEqual(12, dc.V)

        # Multiplication
        c1 = HomomorphicInt(3)
        c2 = c1.new_int(4)
        c12 = c1 * c2
        cc1 = c1.crypt_mult()
        cc2 = c2.crypt_mult()
        cc12 = c12.crypt_mult()
        cc = cc2 * cc1
        self.assertEqual(cc12.V, cc.V)
        dc = cc.decrypt_mult()
        self.assertEqual(12, dc.V)

        # Addition
        c1 = HomomorphicInt(3, 5, 7)
        c2 = c1.new_int(4)
        c12 = c1 + c2
        cc1 = c1.crypt_add()
        cc2 = c2.crypt_add()
        cc12 = c12.crypt_add()
        cc = cc2 + cc1
        self.assertEqual(cc12.V, cc.V)
        dc = cc.decrypt_add()
        self.assertEqual(7, dc.V)

        # Addition
        c1 = HomomorphicInt(3)
        c2 = c1.new_int(4)
        c12 = c1 + c2
        cc1 = c1.crypt_add()
        cc2 = c2.crypt_add()
        cc12 = c12.crypt_add()
        cc = cc2 + cc1
        self.assertEqual(cc12.V, cc.V)
        dc = cc.decrypt_add()
        self.assertEqual(7, dc.V)

        # Soustraction
        c1 = HomomorphicInt(3, 5, 7)
        c2 = c1.new_int(4)
        c12 = c2 - c1
        cc1 = c1.crypt_add()
        cc2 = c2.crypt_add()
        cc12 = c12.crypt_add()
        cc = cc2 - cc1
        self.assertEqual(cc12.V, cc.V)
        dc = cc.decrypt_add()
        self.assertEqual(1, dc.V)


if __name__ == "__main__":
    unittest.main()
