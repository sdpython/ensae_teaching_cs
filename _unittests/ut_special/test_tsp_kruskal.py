"""
@brief      test log(time=10s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, ExtTestCase
from ensae_teaching_cs.helpers.video_helper import make_video
from ensae_teaching_cs.special.tsp_kruskal import construit_ville, pygame_simulation, tsp_kruskal_algorithm
from ensae_teaching_cs.special.tsp_kruskal import equation_droite, evaluation_droite, intersection_segment


class TestTspKruskal(ExtTestCase):

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

    def test_equation_droite(self):
        res = equation_droite((0., 0.), (1., 1.))
        self.assertEqual(res, (1.0, -1.0, 0.0))
        ev = evaluation_droite(*res, (0., 1.))
        self.assertEqual(ev, -1.0)
        inter = intersection_segment((0., 0.), (1., 1.), (0., 1.), (1., 0.))
        self.assertTrue(inter)
        inter = intersection_segment((0., 0.), (1., 1.), (0., 1.), (0.1, 1.1))
        self.assertFalse(inter)

    def test_kruskal_pygame_simulation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_kruskal_pygame_simulation")

        if is_travis_or_appveyor() in ("travis",):
            # pygame.error: No available video device
            return
        import pygame
        if is_travis_or_appveyor() == "circleci":
            # os.environ["SDL_VIDEODRIVER"] = "x11"
            flags = pygame.NOFRAME
        else:
            flags = 0

        pygame.init()

        pygame_simulation(fLOG=fLOG, max_iter=10 if __name__ != "__main__" else 10000,
                          pygame=pygame, folder=temp, flags=flags)

        files = os.listdir(temp)
        self.assertGreater(len(files), 9)
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        self.assertGreater(len(png), 0)
        out = os.path.join(temp, "tsp_kruskal.avi")
        v = make_video(png, out, size=(800, 500), format="XVID", fps=20)
        self.assertNotEmpty(v)


if __name__ == "__main__":
    unittest.main()
