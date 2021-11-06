"""
@brief      test log(time=200s)
"""
import os
import unittest
import math
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from ensae_teaching_cs.special.image.image_synthese_base import (
    Vecteur, Couleur, Source, Repere)
from ensae_teaching_cs.special.image.image_synthese_sphere import Sphere
from ensae_teaching_cs.special.image.image_synthese_phong import ScenePhong
from ensae_teaching_cs.special.image.image_synthese_facette import Facette, Rectangle


class TestImageSynthese(unittest.TestCase):

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

        if is_travis_or_appveyor() == "travis":
            warnings.warn("pygame is not available")
            return

        import pygame
        screen = pygame.display.set_mode(s.dim)
        screen.fill((255, 255, 255))
        s.construit_image(screen, pygame=pygame, fLOG=fLOG)

        from ensae_teaching_cs.helpers.pygame_helper import wait_event
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

        if is_travis_or_appveyor() == "travis":
            warnings.warn("pygame is not available")
            return

        import pygame
        screen = pygame.display.set_mode(s.dim)
        screen.fill((255, 255, 255))
        s.construit_image(screen, pygame=pygame, fLOG=fLOG)

        from ensae_teaching_cs.helpers.pygame_helper import wait_event
        pygame.image.save(screen, os.path.join(temp, "scene_facette.png"))

        if __name__ == "__main__":
            wait_event(pygame)


if __name__ == "__main__":
    unittest.main()
