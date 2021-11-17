"""
@brief      test log(time=10s)

"""
import os
import unittest
from pyquickhelper.pycode import (
    get_temp_folder, is_travis_or_appveyor, ExtTestCase)
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.special.puzzle_2 import pygame_simulation, Puzzle2
from ensae_teaching_cs.helpers.video_helper import make_video


class TestPuzzle2(ExtTestCase):

    def test_image_video_puzzle_2_resolution(self):
        p = Puzzle2()
        p.solution()
        res = str(p)
        self.assertIn("BY-YR-RG-GB", res)

    def test_image_video_puzzle_2(self):
        temp = get_temp_folder(__file__, "temp_image_video_2")

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
        self.assertGreater(len(files), 8)
        png = [os.path.join(temp, _)
               for _ in files if os.path.splitext(_)[-1] == ".png"]
        self.assertGreater(len(png), 1)
        out = os.path.join(temp, "puzzle_2.avi")
        v = make_video(png, out, size=(750, 500), format="XVID", fps=4)
        self.assertNotEmpty(v)


if __name__ == "__main__":
    unittest.main()
