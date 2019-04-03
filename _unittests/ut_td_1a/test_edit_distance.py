"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.td_1a import edit_distance


class TestEditDistance(unittest.TestCase):

    def test_edit_distance(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        d, p = edit_distance("distance", "dizstnce")
        self.assertEqual(d, 2)
        self.assertEqual(p, [(-1, -1), (0, 0), (1, 1), (1, 2),
                             (2, 3), (3, 4), (4, 4), (5, 5), (6, 6), (7, 7)])

    def test_edit_distance_bug(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        s1 = ""
        s2 = "*"
        d, p = edit_distance(s1, s2)
        fLOG(d, p)

        s1 = ""
        s2 = ("***   H ***   H/  ***  H  ***  H/   *** H   *** H/   *** H   *** H/  ***  H  ***  H/ ***   H ***" +
              "   H/ ***   H ***   H/  ***  H  ***  H/   *** H   *** H/   *** H   *** H/  ***  H  ***  H/ ***   H ***   H")
        d, p = edit_distance(s1, s2)
        fLOG(d, p)


if __name__ == "__main__":
    unittest.main()
