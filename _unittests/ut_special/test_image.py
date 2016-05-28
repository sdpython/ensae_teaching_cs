"""
@brief      test log(time=200s)

"""
import os
import sys
import unittest
import pygame
import math


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
from src.ensae_teaching_cs.special.image.image_synthese_base import Vecteur, Couleur, Pixel, Rayon, Source, Repere
from src.ensae_teaching_cs.special.image.image_synthese_sphere import Sphere
from src.ensae_teaching_cs.special.image.image_synthese_scene import Scene
from src.ensae_teaching_cs.special.image.image_synthese_phong import ScenePhong
from src.ensae_teaching_cs.special.image.image_synthese_facette import Facette, Rectangle
from src.ensae_teaching_cs.helpers.pygame_helper import wait_event


class TestImageSynthese(unittest.TestCase):

    def test_base(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        v = Vecteur(0, 1, 2)
        u = Vecteur(0, 1, 2)
        w = u + v
        fLOG(u, v, w)
        fLOG(w * 6)
        p = Pixel(5, 5)
        fLOG(p)
        c = Couleur(1, 1, 1)
        fLOG(c)
        r = Rayon(u, w, p, c)
        fLOG(r)
        s = Source(v, c)
        fLOG(s)

    def test_sphere(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        s = Sphere(Vecteur(0, 0, 0), 5, Couleur(0, 1, 0))
        r = Rayon(Vecteur(10, 0, 0), Vecteur(1, 0, 0),
                  Pixel(0, 0), Couleur(0, 0, 0))
        fLOG(s)
        fLOG(r)
        p = s.intersection(r)
        fLOG(p)

    def test_scene(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_scene")

        s = Scene(Repere(), math.pi / 1.5, 400, 300)
        s.ajoute_source(Source(Vecteur(0, 10, 10), Couleur(1, 1, 1)))
        s.ajoute_source(Source(Vecteur(10, 10, 5), Couleur(0.5, 0.5, 0.5)))
        s.ajoute_objet(Sphere(Vecteur(0, 0, 12), 3, Couleur(1, 0, 0)))
        s.ajoute_objet(Sphere(Vecteur(0, -400, 12),
                              396, Couleur(0.5, 0.5, 0.5)))
        fLOG(s)

        screen = pygame.display.set_mode(s.dim)
        screen.fill((255, 255, 255))
        s.construit_image(screen, fLOG=fLOG)

        pygame.image.save(screen, os.path.join(temp, "scene.png"))

        if __name__ == "__main__":
            wait_event(pygame)

    def test_scene_phong(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_scene_phong")

        s = ScenePhong(Repere(), math.pi / 1.5, 400, 300)

        s.ajoute_source(Source(Vecteur(0, 10, 10), Couleur(1, 1, 1)))
        s.ajoute_source(Source(Vecteur(10, 10, 5), Couleur(0.5, 0.5, 0.5)))
        s.ajoute_objet(Sphere(Vecteur(0, 0, 12), 3, Couleur(1, 0, 0)))
        s.ajoute_objet(Sphere(Vecteur(0, -400, 12),
                              396, Couleur(0.5, 0.5, 0.5)))

        screen = pygame.display.set_mode(s.dim)
        screen.fill((255, 255, 255))
        s.construit_image(screen, fLOG=fLOG)

        pygame.image.save(screen, os.path.join(temp, "scene_phong.png"))

        if __name__ == "__main__":
            wait_event(pygame)

    def test_scene_facette(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_scene_facette")

        s = ScenePhong(Repere(), math.pi / 1.5, 400, 300)

        s.ajoute_source(Source(Vecteur(0, 8, 8), Couleur(0.6, 0.6, 0.6)))
        s.ajoute_source(Source(Vecteur(10, 0, 0), Couleur(0.6, 0.6, 0.6)))
        s.ajoute_source(Source(Vecteur(8, 8, 4.5), Couleur(0.6, 0.6, 0.6)))
        s.ajoute_objet(Sphere(Vecteur(1, 0, 5), 1, Couleur(1, 0, 0)))
        s.ajoute_objet(Sphere(Vecteur(0, -400, 12),
                              396, Couleur(0.5, 0.5, 0.5)))
        s.ajoute_objet(Facette(Vecteur(0, -2.5, 6), Vecteur(-2, -2.5, 3),
                               Vecteur(1, -3.5, 4.5), Couleur(0.2, 0.8, 0)))
        s.ajoute_objet(Rectangle(Vecteur(0, -2.5, 6), Vecteur(-2, -2.5, 3),
                                 Vecteur(-2, 2.8, 3.5), None, Couleur(0, 0, 1)))

        screen = pygame.display.set_mode(s.dim)
        screen.fill((255, 255, 255))
        s.construit_image(screen, fLOG=fLOG)

        pygame.image.save(screen, os.path.join(temp, "scene_facette.png"))

        if __name__ == "__main__":
            wait_event(pygame)


if __name__ == "__main__":
    unittest.main()
