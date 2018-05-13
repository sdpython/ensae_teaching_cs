"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

from src.ensae_teaching_cs.td_2a import DiceStraight


class TestDicesStraight(ExtTestCase):

    text = """
                        4
                        3
                        5287 5288 5289 5290 5291 5292
                        5287 5288 5289 5290 5291 5292
                        5294 5295 5296 5297 5298 5299
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

    def a_test_parsed_and_solve_triplet(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        probs = DiceStraight.parse(TestDicesStraight.text)
        exps = [[(0, 5287), (1, 5288)],
                [(0, 1), (1, 2), (2, 3)],
                [],
                [(3, 2), (2, 3), (0, 4)]]
        intervals = [[(5287, 5292), (5294, 5299)],
                     [(1, 6)], [(1, 6)],
                     [(1, 10), (15, 16), (54, 55)]]
        self.assertEqual(len(probs), 4)
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
            mx = prob.longest_path_length_flow(fLOG=fLOG, verbose=True)
            fLOG("[max_flow]", mx)
            self.assertEqual(mx, len(exp) if len(exp) > 1 else 0)

    def b_test_parsed_and_solve_small(self):
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
            mx = None
            if i < 5:
                # solution 2
                fLOG("prob {0}: nb={1} I={2}".format(i, len(prob), intervals))
                mx = prob.longest_path_length_flow(fLOG=fLOG)
                fLOG("[max_flow]", mx)
                self.assertLesser(mx, len(prob))
            if len(prob) < 8:
                if mx is None:
                    fLOG("prob {0}: nb={1} I={2}".format(
                        i, len(prob), intervals))
                    mx = prob.longest_path_length_flow()
                s2 = prob.longest_path_length_graph()
                if mx != len(s2):
                    raise Exception("{0} != {1}\n{2}".format(mx, s2, prob))


if __name__ == "__main__":
    unittest.main()
