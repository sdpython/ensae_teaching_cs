"""
@brief      test log(time=2s)

"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.special import resolution_sudoku, sudoku2str


class TestSudoku(unittest.TestCase):

    def test_sudolu(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        s = [[0, 0, 0, 3, 0, 0, 8, 0, 0],
             [0, 0, 7, 9, 0, 8, 0, 0, 5],
             [0, 0, 0, 2, 0, 4, 1, 0, 0],
             [0, 9, 0, 8, 1, 0, 0, 4, 7],
             [0, 4, 0, 0, 0, 0, 0, 0, 6],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 5, 0, 2, 0],
             [5, 3, 4, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 7, 0, 0, 0, 0, 0]]

        ps = sudoku2str(s)
        fLOG(ps)

        resolution_sudoku(s)

        self.assertEqual(len(s), 9)
        for i in range(0, 9):
            self.assertEqual(len(s[i]), 9)
            self.assertEqual(sum(s[i]), sum(range(1, 10)))

        ps = sudoku2str(s)
        fLOG(ps)


if __name__ == "__main__":
    unittest.main()
