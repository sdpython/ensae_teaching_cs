"""
@brief      test log(time=57s)
"""
import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv
from ensae_teaching_cs.tests.american_cities import american_cities


class TestLONGFaqMatplotlibVideo(unittest.TestCase):

    def test_all_american_cities(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[:2] <= (3, 4):
            warnings.warn(
                "Issue with Python 3.4, bug probably related to wrong pointers")
            return
        fix_tkinter_issues_virtualenv()
        temp = get_temp_folder(__file__, "temp_LONG_matplotlib_video")
        name = os.path.join(temp, "..", "data", "american_cities.txt")
        img = os.path.join(temp, "img.png")
        res = american_cities(name, -1, img, fLOG)
        assert res is not None


if __name__ == "__main__":
    unittest.main()
