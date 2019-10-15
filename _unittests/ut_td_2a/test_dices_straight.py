"""
@brief      test log(time=1s)
"""
import os
import unittest
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.td_2a import DiceStraight


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

    def test_parsed_and_solve_triplet(self):
        probs = DiceStraight.parse(TestDicesStraight.text)
        exps = [[(0, 5287), (1, 5288)],
                [(0, 1), (1, 2), (2, 3)],
                [],
                [(3, 2), (2, 3), (0, 4), (1, 5)]]
        self.assertEqual(len(probs), 4)
        for prob, exp in zip(probs, exps):
            s = str(prob)
            self.assertNotEmpty(s)
            sol = prob.longest_straight_sequence()
            self.assertEqual(len(sol), len(exp))

    def test_parsed_and_solve_small(self):
        this = os.path.dirname(__file__)
        name = os.path.join(this, "data", "A-small-practice.in")
        probs = DiceStraight.parse(name)
        self.assertEqual(len(probs), 100)
        for i, prob in enumerate(probs):
            sol = prob.longest_straight_sequence()
            self.assertIsInstance(sol, list)
            if i > 1:
                break

    def test_max_number_sequence(self):
        for n in range(2, 101):
            r = DiceStraight.max_number_sequences(n)
            self.assertEqual(len(r), 2)


if __name__ == "__main__":
    unittest.main()
