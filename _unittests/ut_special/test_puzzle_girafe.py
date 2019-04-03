"""
@brief      test log(time=10s)

"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from ensae_teaching_cs.special.puzzle_girafe import pygame_simulation, PuzzleGirafe
from ensae_teaching_cs.helpers.video_helper import make_video


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
        import pygame
        if is_travis_or_appveyor() == "circleci":
            # os.environ["SDL_VIDEODRIVER"] = "x11"
            flags = pygame.NOFRAME
        else:
            flags = 0

        pygame_simulation(pygame, fLOG=fLOG, folder=temp,
                          delay=200 if __name__ == "__main__" else 2,
                          flags=flags)
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
