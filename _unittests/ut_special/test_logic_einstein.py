"""
@brief      test log(time=3s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.special.einstein_prolog import Enigma


class TestSpecialLogic(unittest.TestCase):

    def test_einstein_prolog(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        en = Enigma()
        en.solve(logf=fLOG)
        sol = str(en)
        assert "jaune     , norvegien , eau       , Dunhill   , chats" in sol


if __name__ == "__main__":
    unittest.main()
