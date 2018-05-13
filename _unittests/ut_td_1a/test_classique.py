"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
from datetime import datetime
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

from src.ensae_teaching_cs.td_1a.classiques import racine_carree, commentaire_accentues, dix_entiers_carre
from src.ensae_teaching_cs.td_1a.classiques import repetition_a_eviter, str2date


class TestClassiques (unittest.TestCase):

    def test_fonction1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        a = racine_carree(2)
        self.assertEqual(a, 2 ** 0.5)

    def test_commentaire_accentues(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        commentaire_accentues()

    def test_dix_entiers_carre(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        r = dix_entiers_carre()
        self.assertEqual(r, 385)

    def test_repetition_a_eviter(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        r = repetition_a_eviter([0, 1, 1, 2])
        self.assertEqual(r, 0.5)

    def test_str2date(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        s = str2date("9/8/2017")
        self.assertEqual(s, datetime(2017, 8, 9))


if __name__ == "__main__":
    unittest.main()
