"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import random
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

    def get_pygame_screen_font(self, h, size):
        import pygame
        pygame.init()
        font = pygame.font.Font("freesansbold.ttf", h)
        font_small = pygame.font.Font("freesansbold.ttf", 3 * h // 4)
        screen = pygame.display.set_mode(size)
        font = pygame.font.Font("freesansbold.ttf", h)
        font_small = pygame.font.Font("freesansbold.ttf", 3 * h // 4)
        font_half = pygame.font.Font("freesansbold.ttf", 5 * h // 6)
        return pygame, screen, dict(font=font, font_half=font_half, font_small=font_small)

    def build_image(self, pygame, screen, h, seq1=None, seq2=None, diff=None,
                    fonts=None, bars=None):
        font = fonts.get('font', None)
        font_small = fonts.get('font_small', None)
        font_half = fonts.get('font_half', None)
        if font is None:
            raise ValueError("font cannot be None")
        if font_small is None:
            raise ValueError("font_small cannot be None")
        if font_half is None:
            raise ValueError("font_half cannot be None")
        if seq2 is None:
            raise ValueError("seq2 cannot be None")

        set_seq1 = {} if seq1 is None else set(seq1)
        set_seq2 = set(seq2)
        width = h // 3
        color_bar = (240, 240, 0)
        pos = 0
        if diff is not None:
            for opcode in diff.get_opcodes():
                if opcode[0] == "delete":
                    for i in range(opcode[1], opcode[2]):
                        text = seq1[i]
                        if text not in set_seq2:
                            color = (200, 0, 0)
                            text = font_small.render(text, True, color)
                            screen.blit(text, (10, h * pos + h // 6))
                            pos += 1
                        else:
                            # we skip, it is going to be display by the other
                            # part of the loop
                            passs
                elif opcode[0] == "equal":
                    color = (0, 0, 0)
                    for i in range(opcode[3], opcode[4]):
                        if bars is not None:
                            y = h * pos + (h - width) // 2 + width
                            pygame.draw.line(
                                screen, color_bar, (0, y), (bars[i], y), width)
                        text = seq2[i]
                        text = font.render(text, True, color)
                        screen.blit(text, (10, h * pos))
                        pos += 1
                else:
                    for i in range(opcode[3], opcode[4]):
                        if bars is not None:
                            y = h * pos + (h - width) // 2 + width
                            pygame.draw.line(
                                screen, color_bar, (0, y), (bars[i], y), width)
                        text = seq2[i]
                        if text in set_seq1:
                            color = (0, 120, 0)
                            text = font.render(text, True, color)
                            screen.blit(text, (10, h * pos))
                            pos += 1
                        else:
                            color = (0, 120, 120)
                            text = font.render(text, True, color)
                            screen.blit(text, (10, h * pos))
                            pos += 1
        else:
            color = (0, 0, 0)
            for i in range(0, len(seq2)):
                text = seq2[i]
                text = font.render(text, True, color)
                screen.blit(text, (10, h * pos))
                pos += 1

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
            h = 20
            size = 500, 500
            white = 255, 255, 255

            pygame, screen, fonts = self.get_pygame_screen_font(h, size)

            from src.ensae_teaching_cs.helpers.pygame_helper import wait_event

            bars = [random.randint(10, 500) for s in seq2]
            screen.fill(white)
            self.build_image(pygame, screen, h=h, seq1=seq1, seq2=seq2, diff=diff,
                             fonts=fonts, bars=bars)
            pygame.display.flip()
            wait_event(pygame)


if __name__ == "__main__":
    unittest.main()
