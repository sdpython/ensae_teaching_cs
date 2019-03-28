"""
@brief      test log(time=10s)
"""
import unittest
import time
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.special.hermionne import solution, affiche_solution
from ensae_teaching_cs.special.hermionne_classes import solution as solution_classe


class TestHermionne(ExtTestCase):

    def test_solution1(self):
        begin = time.perf_counter()
        for i in range(0, 100):
            res = solution()
        dur = time.perf_counter() - begin
        mes = affiche_solution(res)
        self.assertEqual(res, [0, 1, 3, 0, 0, 1, 2])
        self.assertGreater(dur, 0)
        self.assertNotEmpty(res)

    def test_solution2(self):
        begin = time.perf_counter()
        for i in range(0, 100):
            res = solution_classe()
        dur = time.perf_counter() - begin
        self.assertEqual(
            str(res), "poison, vin, avancer, poison, poison, vin, reculer")
        self.assertGreater(dur, 0)


if __name__ == "__main__":
    unittest.main()
