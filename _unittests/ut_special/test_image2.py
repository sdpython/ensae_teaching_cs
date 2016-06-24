"""
@brief      test log(time=200s)

"""
import os
import sys
import unittest
import math
import warnings


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
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from src.ensae_teaching_cs.special.image.image_synthese_base import Vecteur, Couleur, Source, Repere
from src.ensae_teaching_cs.special.image.image_synthese_sphere import Sphere
from src.ensae_teaching_cs.special.image.image_synthese_phong import ScenePhong
from src.ensae_teaching_cs.special.image.image_synthese_facette import Rectangle
from src.ensae_teaching_cs.special.image.image_synthese_facette_image import RectangleImage, SphereReflet


class TestImageSyntheseImage(unittest.TestCase):

    def test_scene_image(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_scene_bette")
        image = os.path.join(temp, "..", "data", "bette_davis.png")

        s = ScenePhong(Repere(), math.pi / 1.5, 400, 200)

        s.ajoute_source(Source(Vecteur(0, 8, 8), Couleur(0.4, 0.4, 0.4)))
        s.ajoute_source(Source(Vecteur(10, 0, 0), Couleur(0.4, 0.4, 0.4)))
        s.ajoute_source(Source(Vecteur(8, 8, 4.5), Couleur(0.4, 0.4, 0.4)))
        s.ajoute_objet(Sphere(Vecteur(3, -4, 7), 1, Couleur(1, 0, 0)))
        s.ajoute_objet(SphereReflet(Vecteur(0, -400, 12),
                                    396, Couleur(0.5, 0.5, 0.5), 0.5))

        s.ajoute_source(Source(Vecteur(7, 2, 8), Couleur(0.2, 0.2, 0.2)))
        s.ajoute_source(Source(Vecteur(12.5, 3, 5), Couleur(0.2, 0.2, 0.2)))
        s.ajoute_source(Source(Vecteur(-12.5, 1, 6), Couleur(0.2, 0.2, 0.2)))
        
        s.ajoute_objet(Rectangle(Vecteur(-12.4, 0.99, 5.9), Vecteur(-12.6, 0.99, 5.9),
                                 Vecteur(-12.6, 0.99, 6.1), None, Couleur(0, 0, 0)))

        if is_travis_or_appveyor() == "travis":
            warnings.warn("pygame is not available")
            return

        import pygame

        s.ajoute_objet(RectangleImage(Vecteur(8, -3.5, 9), Vecteur(2, -3.5, 8),
                                      Vecteur(2, 3.8, 8), None, image, invertx=True, pygame=pygame))

        from src.ensae_teaching_cs.helpers.pygame_helper import wait_event

        screen = pygame.display.set_mode(s.dim)
        screen.fill((255, 255, 255))
        s.construit_image(screen, pygame=pygame, fLOG=fLOG)

        pygame.image.save(screen, os.path.join(temp, "scene_bette.png"))

        if __name__ == "__main__":
            wait_event(pygame)


if __name__ == "__main__":
    unittest.main()
