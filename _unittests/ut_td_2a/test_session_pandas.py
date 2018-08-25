"""
@brief      test log(time=1s)
"""


import sys
import os
import unittest
import pandas
from pyquickhelper.loghelper import fLOG


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

from src.ensae_teaching_cs.pandas_helper import dfs2excel


class TestSessionPandas(unittest.TestCase):

    def test_excel(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        df1 = pandas.DataFrame([{"name": "xavier", "school": "ENSAE"},
                                {"name": "antoine", "school": "ENSAE"}])

        df2 = pandas.DataFrame([{"name": "xavier", "company": "Microsoft"},
                                {"name": "antoine", "company": "Alephd"}])

        ef = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "out_example.xlsx"))
        if os.path.exists(ef):
            os.remove(ef)
        dfs2excel({"ecole": df1, "boite": df2}, ef)
        assert os.path.exists(ef)


if __name__ == "__main__":
    unittest.main()
