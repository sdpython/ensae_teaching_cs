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

    def test_parsed_and_solve_triplet(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        probs = DiceStraight.parse(TestDicesStraight.text)
        exps = [[(0, 1), (1, 2)],
                [],
                [(3, 2), (2, 3), (0, 4)]]
        intervals = [[(1, 6)], [(1, 6)], [(1, 10), (15, 16), (54, 55)]]
        self.assertEqual(len(probs), 3)
        for prob, exp, einter in zip(probs, exps, intervals):
            fLOG(prob)
            # intervals
            inter = prob.find_intervals()
            fLOG("[intervales]", inter)
            self.assertEqual(inter, einter)
            # solution 1
            mul = prob.longest_path_length_graph(fLOG=fLOG)
            self.assertEqual(mul, exp)
            self.assertLesser(len(mul), len(prob))
            # solution 2
            mx = prob.longest_path_length_flow(fLOG=fLOG)
            fLOG("[max_flow]", mx)
            self.assertEqual(mx, len(exp) if len(exp) > 1 else 0)

    def test_parsed_and_solve_small(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        this = os.path.dirname(__file__)
        name = os.path.join(this, "data", "A-small-practice.in")
        probs = DiceStraight.parse(name)
        self.assertEqual(len(probs), 100)
        for i, prob in enumerate(probs):
            intervals = prob.find_intervals()
            fLOG("prob {0}: nb={1} I={2}".format(i, len(prob), intervals))
            # solution 2
            mx = prob.longest_path_length_flow(fLOG=fLOG)
            fLOG("[max_flow]", mx)
            self.assertLesser(mx, len(prob))
            if i >= 5:
                # Too long.
                break


if __name__ == "__main__":
    unittest.main()
