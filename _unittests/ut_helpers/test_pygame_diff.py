"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import random
import warnings
from difflib import SequenceMatcher


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
    import pyquickhelper.loghelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from src.ensae_teaching_cs.helpers.pygame_helper import build_diff_image, get_pygame_screen_font


class TestDiff(unittest.TestCase):

    def test_diff(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        seq1 = "ab ab2 abc3 abcd abc4".split()
        seq2 = "ab ab2 abc3 abc4 abc adb".split()
        diff = SequenceMatcher(a=seq1, b=seq2)
        nb = 0
        for opcode in diff.get_opcodes():
            fLOG(opcode)
            nb += 1
        self.assertEqual(nb, 4)

        h = 20
        size = 500, 500
        white = 255, 255, 255

        if is_travis_or_appveyor() == "travis":
            warnings.warn("pygame is not available")
            return
        pygame, screen, fonts = get_pygame_screen_font(h, size)

        from src.ensae_teaching_cs.helpers.pygame_helper import wait_event

        bars = [random.randint(10, 500) / 500.0 for s in seq2]
        screen.fill(white)
        build_diff_image(pygame, screen, h=h, maxw=size[1], seq1=seq1, seq2=seq2, diff=diff,
                         fonts=fonts, bars=bars)
        pygame.display.flip()
        temp = get_temp_folder(__file__, "temp_video_diff")

        for i in range(0, 21):
            screen.fill(white)
            build_diff_image(pygame, screen, h=h, maxw=size[0], seq1=seq1, seq2=seq2, diff=diff,
                             fonts=fonts, bars=bars, progress=i / 20.0, prev_bars=None)
            pygame.time.wait(60)
            pygame.display.flip()
            pygame.image.save(screen, os.path.join(temp, "diff%d.png" % i))

        if __name__ == "__main__":

            from src.ensae_teaching_cs.helpers.video_helper import make_video
            png = [os.path.join(temp, _)
                   for _ in os.listdir(temp) if ".png" in _]
            out = os.path.join(temp, "diff.avi")
            make_video(png, out, size=(350, 250), format="XVID", fps=5)

            wait_event(pygame)

    def test_diff_full(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        seq1 = "zab zab2 zabc3 zabcd zabc4".split()
        seq2 = "ab ab2 abc3 abc4 abc adb".split()
        diff = SequenceMatcher(a=seq1, b=seq2)

        h = 20
        size = 500, 500
        white = 255, 255, 255

        pygame, screen, fonts = get_pygame_screen_font(h, size)

        from src.ensae_teaching_cs.helpers.pygame_helper import wait_event

        bars = [random.randint(10, 500) / 500.0 for s in seq2]
        screen.fill(white)
        build_diff_image(pygame, screen, h=h, maxw=size[1], seq1=seq1, seq2=seq2, diff=diff,
                         fonts=fonts, bars=bars)
        pygame.display.flip()
        temp = get_temp_folder(__file__, "temp_video_diff_full")

        for i in range(0, 21):
            screen.fill(white)
            build_diff_image(pygame, screen, h=h, maxw=size[0], seq1=seq1, seq2=seq2, diff=diff,
                             fonts=fonts, bars=bars, progress=i / 20.0, prev_bars=None)
            pygame.time.wait(60)
            pygame.display.flip()
            pygame.image.save(screen, os.path.join(temp, "diff%d.png" % i))

        if __name__ == "__main__":

            from src.ensae_teaching_cs.helpers.video_helper import make_video
            png = [os.path.join(temp, _)
                   for _ in os.listdir(temp) if ".png" in _]
            out = os.path.join(temp, "diff.avi")
            make_video(png, out, size=(350, 250), format="XVID", fps=5)

            wait_event(pygame)

if __name__ == "__main__":
    unittest.main()
