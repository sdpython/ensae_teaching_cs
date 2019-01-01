"""
@brief      test log(time=10s)

"""
import os
import sys
import unittest
import time
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


class TestHermionne(unittest.TestCase):

    def test_solution1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.ensae_teaching_cs.special.hermionne import solution, affiche_solution
        begin = time.perf_counter()
        for i in range(0, 100):
            res = solution()
        dur = time.perf_counter() - begin
        mes = affiche_solution(res)
        fLOG("1", dur, mes)
        self.assertEqual(res, [0, 1, 3, 0, 0, 1, 2])

    def test_solution2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.ensae_teaching_cs.special.hermionne_classes import solution as solution_classe
        begin = time.perf_counter()
        for i in range(0, 100):
            res = solution_classe()
        dur = time.perf_counter() - begin
        fLOG("2", dur, res)
        self.assertEqual(
            str(res), "poison, vin, avancer, poison, poison, vin, reculer")


if __name__ == "__main__":
    unittest.main()
