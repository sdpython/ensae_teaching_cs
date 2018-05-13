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

from src.ensae_teaching_cs.td_1a.optimisation_contrainte import exercice_particulier2


class TestOptimisation (ExtTestCase):

    def test_optimisation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        sol2 = exercice_particulier2()
        x2 = sol2['x']
        d = abs(x2[0] - 0.428571428055853) + abs(x2[1] - 0.2857142848749249)
        self.assertLesser(d, 1e-5)


if __name__ == "__main__":
    unittest.main()
