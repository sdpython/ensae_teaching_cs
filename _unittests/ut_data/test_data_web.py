"""
@brief      test log(time=3s)
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

try:
    import pyensae as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae as skip__

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.data import google_trends


class TestDataWeb(unittest.TestCase):

    def test_google_trends_macron(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_google_trends_macron")
        text = google_trends(local=True, filename=False)
        assert text is not None

        name = google_trends(local=True, filename=True)
        assert name.endswith("macron.csv")

        try:
            text2 = google_trends(
                local=False, cache_folder=temp, filename=False)
        except ConnectionResetError as e:
            warnings.warn("Cannot check remote marathon.txt.\n" + str(e))
            return

        assert text2 is not None
        self.assertEqual(len(text), len(text2))
        self.maxDiff = None
        self.assertEqual(text, text2)


if __name__ == "__main__":
    unittest.main()
