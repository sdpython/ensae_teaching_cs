"""
@brief      test log(time=10s)

"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from ensae_teaching_cs.special.voisinage_evolution import pygame_simulation
from ensae_teaching_cs.helpers.video_helper import make_video


class TestSimulationVoisinage(unittest.TestCase):

    def test_image_video_epidemic(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_image_video_voisinage")

        if is_travis_or_appveyor() in ("travis",):
            # pygame.error: No available video device
            return
        import pygame
        if is_travis_or_appveyor() == "circleci":
            # os.environ["SDL_VIDEODRIVER"] = "x11"
            flags = pygame.NOFRAME
        else:
            flags = 0

        pygame_simulation(pygame, fLOG=fLOG, folder=temp,
                          max_iter=150 if __name__ == "__main__" else 10,
                          flags=flags)
        files = os.listdir(temp)
        assert len(files) > 9
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        assert len(png) > 0
        out = os.path.join(temp, "voisinage.avi")
        v = make_video(png, out, size=(500, 500), format="XVID")
        assert v is not None


if __name__ == "__main__":
    unittest.main()
