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
from pyquickhelper.pycode import ExtTestCase
from src.ensae_teaching_cs.td_2a import DiceStraight


class TestDicesStraight(ExtTestCase):

    text = """
                        3
                        3
                        1 2 3 4 5 6
                        1 2 3 4 5 6
                        1 4 2 6 5 3
                        2
                        1 2 3 4 5 6
                        60 50 40 30 20 10
                        4
                        4 8 15 16 23 42
                        8 6 7 5 30 9
                        1 2 3 4 55 6
                        2 10 18 36 54 86
                        """.replace("                        ", "")

    def test_parsed_and_solve(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        probs = DiceStraight.parse(TestDicesStraight.text)
        exps = [[(0, 1), (1, 2)],
                [],
                [(3, 2), (2, 3), (0, 4)]]
        self.assertEqual(len(probs), 3)
        for prob, exp in zip(probs, exps):
            fLOG(prob)
            mul = prob.longest_path_length(fLOG=fLOG)
            self.assertEqual(mul, exp)

    def a_test_parsed_and_solve_small(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        this = os.path.dirname(__file__)
        name = os.path.join(this, "data", "A-small-practice.in")
        probs = DiceStraight.parse(name)
        self.assertEqual(len(probs), 100)
        for i, prob in enumerate(probs):
            fLOG("prob {0}: nb={1}".format(i, len(prob)))
            fLOG(prob)
            mul = prob.longest_path_length(fLOG=fLOG)
            fLOG("   path: {0}".format(mul))
            self.assertTrue(mul is not None)


if __name__ == "__main__":
    unittest.main()
