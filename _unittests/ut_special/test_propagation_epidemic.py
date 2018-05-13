"""
@brief      test log(time=10s)
"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


from src.ensae_teaching_cs.special.propagation_epidemic import numerical_simulation, pygame_simulation
from src.ensae_teaching_cs.helpers.video_helper import make_video


class TestEpidemicPropagation(unittest.TestCase):

    def test_simulation_epidemic(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = numerical_simulation(fLOG=fLOG, iter=10)
        fLOG(res)

    def test_image_video_epidemic(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_image_video_epidemic")

        if is_travis_or_appveyor() in ("travis",):
            # pygame.error: No available video device
            return
        import pygame
        if is_travis_or_appveyor() == "circleci":
            # os.environ["SDL_VIDEODRIVER"] = "x11"
            flags = pygame.NOFRAME
        else:
            flags = 0

        pygame_simulation(pygame, fLOG=fLOG, iter=10, folder=temp, flags=flags)
        files = os.listdir(temp)
        self.assertTrue(len(files) > 9)
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        self.assertTrue(len(png) > 0)
        out = os.path.join(temp, "epidemic.avi")

        v = make_video(png, out, size=(300, 300), format="XVID")
        self.assertTrue(v is not None)


if __name__ == "__main__":
    unittest.main()
