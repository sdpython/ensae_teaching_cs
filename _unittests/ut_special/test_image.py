"""
@brief      test log(time=200s)
"""
import os
import unittest
import math
import numpy
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from ensae_teaching_cs.special.image.image_synthese_base import (
    Vecteur, Couleur, Pixel, Rayon, Source, Repere)
from ensae_teaching_cs.special.image.image_synthese_sphere import Sphere
from ensae_teaching_cs.special.image.image_synthese_scene import Scene


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

    def common_test_scene(self, use_pygame):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, f"temp_scene{use_pygame!r}")

        s = Scene(Repere(), math.pi / 1.5, 400, 300)
        s.ajoute_source(Source(Vecteur(0, 10, 10), Couleur(1, 1, 1)))
        s.ajoute_source(Source(Vecteur(10, 10, 5), Couleur(0.5, 0.5, 0.5)))
        s.ajoute_objet(Sphere(Vecteur(0, 0, 12), 3, Couleur(1, 0, 0)))
        s.ajoute_objet(Sphere(Vecteur(0, -400, 12),
                              396, Couleur(0.5, 0.5, 0.5)))
        fLOG(s)

        if not use_pygame:
            pygame = None
        else:
            import pygame

        from ensae_teaching_cs.helpers.pygame_helper import wait_event

        if pygame is not None:
            screen = pygame.display.set_mode(s.dim)
            screen.fill((255, 255, 255))
        else:
            screen = numpy.zeros(s.dim + (3, ), dtype=numpy.uint8)
        s.construit_image(screen, pygame=pygame, fLOG=fLOG)

        if pygame is None:
            from PIL import Image
            print(screen.shape)
            im = Image.fromarray(numpy.transpose(
                screen, (1, 0, 2)), mode='RGB')
            im.save(os.path.join(temp, "scene.png"))
        else:
            pygame.image.save(screen, os.path.join(temp, "scene2.png"))
            if __name__ == "__main__":
                wait_event(pygame)

    def test_scene(self):
        self.common_test_scene(False)
        if not is_travis_or_appveyor():
            self.common_test_scene(True)


if __name__ == "__main__":
    unittest.main()
