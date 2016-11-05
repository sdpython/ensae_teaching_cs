"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
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
from src.ensae_teaching_cs.td_1a import edit_distance


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
        s2 = "***   H ***   H/  ***  H  ***  H/   *** H   *** H/   *** H   *** H/  ***  H  ***  H/ ***   H ***   H/ ***   H ***   H/  ***  H  ***  H/   *** H   *** H/   *** H   *** H/  ***  H  ***  H/ ***   H ***   H"
        d, p = edit_distance(s1, s2)
        fLOG(d, p)


if __name__ == "__main__":
    unittest.main()
