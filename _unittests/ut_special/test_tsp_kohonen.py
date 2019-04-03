"""
@brief      test log(time=10s)

"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from ensae_teaching_cs.special.tsp_kohonen import pygame_simulation
from ensae_teaching_cs.helpers.video_helper import make_video


class TestTspKohonen(unittest.TestCase):

    def test_image_video_kohonen(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_image_video_tsp_kohonen")

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
                          nb=200 if __name__ == "__main__" else 20,
                          size=(400, 250), flags=flags)
        files = os.listdir(temp)
        assert len(files) > 9
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        assert len(png) > 0
        out = os.path.join(temp, "tsp_kohonen.avi")
        v = make_video(png, out, size=(200, 125), format="XVID", fps=20)
        assert v is not None


if __name__ == "__main__":
    unittest.main()
