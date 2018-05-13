"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
import clr


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


from src.ensae_teaching_cs.td_2a.pythoncs import create_cs_function


class TestPythonnetMagicCS(unittest.TestCase):

    def test_magic_cs(self):
        code = "public static double SquareX(double x) {return x*x ; }"
        f = create_cs_function("SquareX", code)
        r = f(2.0)
        self.assertEqual(r, 4)


if __name__ == "__main__":
    unittest.main()
