"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import warnings


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

try:
    import pyquickhelper as skip_
except ImportError:
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
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv


class TestFaqMatplotlibVideo(unittest.TestCase):

    def test_american_cities(self):
        fLOG(__file__, self._testMethodName, OutputPrint=True)

        if sys.version_info[:2] <= (3, 4):
            warnings.warn(
                "Issue with Python 3.4, bug probably related to wrong pointers")
            return
        fix_tkinter_issues_virtualenv()
        try:
            from .american_cities import american_cities
        except (ImportError, SystemError):
            from american_cities import american_cities
        temp = get_temp_folder(__file__, "temp_matplotlib_video")
        american_cities(40, fLOG, temp)


if __name__ == "__main__":
    unittest.main()
