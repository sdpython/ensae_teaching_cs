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

from src.ensae_teaching_cs.td_1a.optimisation_contrainte import exercice_particulier1, exercice_particulier2


class TestOptimisationCVXOPT(ExtTestCase):

    @unittest.skipIf(sys.platform.startswith("win"),
                     reason="import cvxopt.base, ImportError: DLL load failed")
    def test_optimisation_cvxopt(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        sol2 = exercice_particulier2()
        x2 = sol2['x']
        d = abs(x2[0] - 0.428571428055853) + abs(x2[1] - 0.2857142848749249)
        self.assertLesser(d, 1e-5)

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
        self.assertLesser(abs(d1), 1e-5)
        self.assertLesser(abs(d2), 1e-5)


if __name__ == "__main__":
    unittest.main()
