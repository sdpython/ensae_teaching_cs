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
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from src.ensae_teaching_cs.special.puzzle_girafe import pygame_simulation, PuzzleGirafe
from src.ensae_teaching_cs.helpers.video_helper import make_video


class TestPuzzleGirafe(unittest.TestCase):

    def test_image_video_puzzle_girafe_resolution(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        p = PuzzleGirafe()
        p.solution()
        res = str(p)
        self.assertIn(
            "1 : haut orange - bas bleu clair - bas bleu fonce - haut violet -  orientation 0 numero 1", res)

    def test_image_video_puzzle_girafe(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_image_video_girafe")

        if is_travis_or_appveyor() in ("travis",):
            # pygame.error: No available video device
            return
        if is_travis_or_appveyor() == "circleci":
            os.environ["SDL_VIDEODRIVER"] = "x11"

        import pygame
        pygame_simulation(pygame, fLOG=fLOG, folder=temp,
                          delay=200 if __name__ == "__main__" else 2)
        files = os.listdir(temp)
        assert len(files) > 9
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        assert len(png) > 0
        out = os.path.join(temp, "puzzle_girafe.avi")
        v = make_video(png, out, size=(500, 500), format="XVID", fps=4)
        assert v is not None


if __name__ == "__main__":
    unittest.main()
