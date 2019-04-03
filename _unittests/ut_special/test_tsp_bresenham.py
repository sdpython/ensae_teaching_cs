"""
@brief      test log(time=10s)

"""
import unittest
import random
from ensae_teaching_cs.special.tsp_bresenham import draw_line, draw_ellipse


class TestTspBresenham(unittest.TestCase):

    def test_bresenham(self):
        x, y = 500, 500
        for n in range(0, 10):
            x1 = random.randint(0, x - 1)
            y1 = random.randint(0, y - 1)
            x2 = random.randint(0, x - 1)
            y2 = random.randint(0, y - 1)
            ligne1 = draw_line(x1, y1, x2, y2)
            ligne2 = draw_line(x2, y2, x1, y1)
            ligne2.reverse()
            self.assertEqual(len(ligne1), len(ligne2))
            draw_line(x2, y1, x1, y2)
            draw_line(x1, y2, x2, y1)

    def test_bresenham_ellipses(self):
        x, y = 500, 500
        for n in range(0, 10):
            x1 = random.randint(0, x - 1)
            y1 = random.randint(0, y - 1)
            xa = random.randint(50, 100)
            xb = random.randint(50, 100)
            draw_ellipse(x1, y1, xa, xb)


if __name__ == "__main__":
    unittest.main()
