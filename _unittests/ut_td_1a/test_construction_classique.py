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
from src.ensae_teaching_cs.td_1a.construction_classique import recherche, minindex, text2mat, compte, integrale, vect2mat, mat2vect, recherche_dichotomique, mat2text, triindex, construit_matrice_carree


class TestConstructionClassique(unittest.TestCase):

    def test_fonction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        assert recherche([2, 3, 45], 3) == 1
        assert recherche([2, 3, 45], 4) == -1
        assert minindex([2, 3, 45, -1, 5]) == (-1, 3)
        li = range(0, 100, 2)
        assert recherche_dichotomique(li, 48) == 24
        assert recherche_dichotomique(li, 49) == -1
        s = "case11;case12;case13|case21;case22;case23"
        mat = text2mat(s, "|", ";")
        t = mat2text(mat, "|", ";")
        assert t == s
        tab = ["zero", "un", "deux"]
        r = triindex(tab)
        assert r == [('deux', 2), ('un', 1), ('zero', 0)]
        li = ["un", "deux", "un", "trois"]
        r = compte(li)
        assert r == {'trois': 1, 'deux': 1, 'un': 2}
        mat = [[0, 1, 2], [3, 4, 5]]
        r = mat2vect(mat)
        assert r == [0, 1, 2, 3, 4, 5]
        m = vect2mat(r, 3)
        assert m == mat
        x2 = integrale(lambda x: x, 0, 2, 1000)
        assert x2 == 2

    def test_matrice_carre(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        mat = construit_matrice_carree(10)
        assert len(mat) == 10
        assert len(mat[0]) == 10

if __name__ == "__main__":
    unittest.main()
