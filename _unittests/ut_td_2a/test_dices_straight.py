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
from src.ensae_teaching_cs.td_2a import DiceStraight


class TestDicesStraight(unittest.TestCase):

    text = """
                        3
                        4
                        4 8 15 16 23 42
                        8 6 7 5 30 9
                        1 2 3 4 55 6
                        2 10 18 36 54 86
                        2
                        1 2 3 4 5 6
                        60 50 40 30 20 10
                        3
                        1 2 3 4 5 6
                        1 2 3 4 5 6
                        1 4 2 6 5 3
                        """.replace("                        ", "")

    def test_parsed(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        prob = DiceStraight.parse(TestDicesStraight.text)
        self.assertEqual(len(prob), 3)


if __name__ == "__main__":
    unittest.main()
