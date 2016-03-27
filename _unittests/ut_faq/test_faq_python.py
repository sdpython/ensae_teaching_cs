"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest


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
from src.ensae_teaching_cs.faq.faq_python import get_month_name, get_day_name


class TestFaqPython(unittest.TestCase):

    def test_month_name(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import datetime
        dt = datetime.datetime(2016, 1, 25)
        name = get_month_name(dt)
        self.assertEqual(name, "January")

    def test_day_name(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import datetime
        dt = datetime.datetime(2016, 1, 25)
        name = get_day_name(dt)
        self.assertEqual(name, "Monday")


if __name__ == "__main__":
    unittest.main()
