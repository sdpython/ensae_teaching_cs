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
from src.ensae_teaching_cs.helpers.video_helper import make_video
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

        files = os.listdir(temp)
        assert len(files) > 9
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        assert len(png) > 0
        out = os.path.join(temp, "tsp_kruskal.avi")
        v = make_video(png, out, size=(800, 500), format="XVID", fps=20)
        assert v is not None

if __name__ == "__main__":
    unittest.main()
