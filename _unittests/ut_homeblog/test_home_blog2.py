"""
@brief      test log(time=2s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.homeblog.program_helper import guess_language_code


class TestHomeBlog2(unittest.TestCase):

    def test_guess_language_code(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")

        res = guess_language_code("import numpy\nx = 3\nprint(x)")
        self.assertEqual(res, ('py', 1))
        res = guess_language_code("<html></html>")
        self.assertEqual(res, ('xml', 1))


if __name__ == "__main__":
    unittest.main()
