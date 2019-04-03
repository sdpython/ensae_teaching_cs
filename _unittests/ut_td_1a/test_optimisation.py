"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.td_1a.optimisation_contrainte import exercice_particulier2


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
