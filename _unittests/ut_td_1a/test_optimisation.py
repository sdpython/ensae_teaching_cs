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
from src.ensae_teaching_cs.td_1a.optimisation_contrainte import exercice_particulier1, exercice_particulier2


class TestOptimisation (unittest.TestCase):

    def test_optimisation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        sol1 = exercice_particulier1()
        sol2 = exercice_particulier2()
        fLOG("cvxopt")
        fLOG(sol1)
        fLOG("solution:", sol1['x'].T)
        fLOG("Arrow_Hurwicz")
        fLOG(sol2)
        fLOG("solution:", sol2['x'])

        x1 = sol1['x']
        x2 = sol2['x']
        d1 = x1[0] - x2[0]
        d2 = x1[1] - x2[1]
        fLOG(d1, d2)
        assert abs(d1) < 1e-5
        assert abs(d2) < 1e-5


if __name__ == "__main__":
    unittest.main()
