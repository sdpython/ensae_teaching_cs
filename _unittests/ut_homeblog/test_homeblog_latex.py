"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from ensae_teaching_cs.homeblog import py_to_html_file


class TestHomeBlogLatex(unittest.TestCase):

    def test_cs2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_home_latex")
        out = os.path.join(temp, "out.html")
        py_to_html_file(__file__.replace(".pyc", ".py"), out)
        assert os.path.exists(out)


if __name__ == "__main__":
    unittest.main()
