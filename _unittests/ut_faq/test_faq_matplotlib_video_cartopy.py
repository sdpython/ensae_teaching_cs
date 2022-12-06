"""
@brief      test log(time=7s)
"""

import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import (
    get_temp_folder, fix_tkinter_issues_virtualenv, ExtTestCase, skipif_circleci)
from ensae_teaching_cs.tests.american_cities import american_cities


class TestFaqMatplotlibVideo(ExtTestCase):

    @skipif_circleci("Received 'segmentation fault' signal")
    def test_american_cities(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv()
        temp = get_temp_folder(__file__, "temp_matplotlib_video")
        name = os.path.join(temp, "..", "data", "american_cities.txt")
        img = os.path.join(temp, "img.png")
        try:
            res = american_cities(name, 40, img, fLOG)
        except AttributeError as e:
            if "'GeoAxesSubplot' object has no attribute '_autoscaleXon'" in str(e):
                return
            raise e
        self.assertNotEmpty(res)


if __name__ == "__main__":
    unittest.main()
