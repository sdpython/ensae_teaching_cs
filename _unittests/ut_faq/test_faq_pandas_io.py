"""
@brief      test log(time=1s)
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
from src.ensae_teaching_cs.pandas_helper import read_csv


class TestFaqPandasIo(unittest.TestCase):

    def test_graph_ggplots(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        data = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "data",
            "dfbom.txt")
        df = read_csv(data, encoding="utf8")
        fLOG(df.columns)
        fLOG(df.dtypes)
        assert "\ufeff" not in df.columns[0]
        try:
            df = read_csv(data, encoding="ascii")
        except UnicodeDecodeError:
            pass


if __name__ == "__main__":
    unittest.main()
