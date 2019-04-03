"""
@brief      test log(time=2s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.homeblog import music_statistics


class TestFilenameHelper(unittest.TestCase):

    def test_TableFormulaCore_Excel(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        this = os.path.abspath(os.path.dirname(__file__))
        r = music_statistics(this)
        assert isinstance(r, dict)


if __name__ == "__main__":
    unittest.main()
