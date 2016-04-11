"""
@brief      test log(time=10s)

"""
import os
import sys
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
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.special.tsp_kruskal import construit_ville, pygame_simulation, tsp_kruskal_algorithm


class TestTspKruskal(unittest.TestCase):

    def test_kruskal(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb_ville = 700
        x, y = 800, 500
        villes = construit_ville(nb_ville, x, y)
        neurones = tsp_kruskal_algorithm(villes, fLOG=fLOG, max_iter=10)
        self.assertEqual(len(villes), len(neurones))

    def test_kruskal_pygame_simulation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_kruskal_pygame_simulation")

        import pygame
        pygame.init()

        pygame_simulation(fLOG=fLOG, max_iter=10 if __name__ != "__main__" else 10000,
                          pygame=pygame, folder=temp)


if __name__ == "__main__":
    unittest.main()
