"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
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


class TestDiff(unittest.TestCase):

    def test_diff(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        seq1 = "ab ab abc abcd abc".split()
        seq2 = "ab ab abc abc abc adb".split()
        diff = SequenceMatcher(a=seq1, b=seq2)
        nb = 0
        for opcode in diff.get_opcodes():
            fLOG(opcode)
            nb += 1
        self.assertEqual(nb, 4)

        if __name__ == "__main__":
            from src.ensae_teaching_cs.helpers.pygame_helper import wait_event
            import pygame
            pygame.init()
            h = 20
            font = pygame.font.Font("freesansbold.ttf", h)
            font_small = pygame.font.Font("freesansbold.ttf", 3 * h // 4)
            size = 500, 500
            white = 255, 255, 255
            screen = pygame.display.set_mode(size)
            screen.fill(white)

            pos = 0
            for opcode in diff.get_opcodes():
                if opcode[0] == "delete":
                    color = (200, 0, 0)
                    for i in range(opcode[1], opcode[2]):
                        text = seq1[i]
                        text = font_small.render(text, True, color)
                        screen.blit(text, (10, h * pos + h // 6))
                        pos += 1
                else:
                    color = (0, 0, 0) if opcode[0] == "equal" else (0, 120, 0)
                    for i in range(opcode[3], opcode[4]):
                        text = seq2[i]
                        text = font.render(text, True, color)
                        screen.blit(text, (10, h * pos))
                        pos += 1
            pygame.display.flip()
            wait_event(pygame)


if __name__ == "__main__":
    unittest.main()
