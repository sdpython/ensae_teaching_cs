"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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


from src.ensae_teaching_cs.homeblog import py_to_html_file


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
