"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
import re
import pandas
import numpy

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
    import pyquickhelper
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
    import pyquickhelper

from pyquickhelper import fLOG
from src.ensae_teaching_cs.faq.faq_pandas import groupby_topn, df_equal


class TestFaqPandas(unittest.TestCase):

    def test_groupby_sort_head(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        l = [dict(k1="a", k2="b", v=4, i=1),
             dict(k1="a", k2="b", v=5, i=1),
             dict(k1="a", k2="b", v=4, i=2),
             dict(k1="b", k2="b", v=1, i=2),
             dict(k1="b", k2="b", v=1, i=3),
             ]

        exp = [dict(k1="a", k2="b", v=4, i=1),
               dict(k1="b", k2="b", v=1, i=2),
               ]

        df = pandas.DataFrame(l)
        exp = pandas.DataFrame(exp)

        res = groupby_topn(df, by_keys=["k1", "k2"],
                           sort_keys=["v", "i"], as_index=False)
        b = df_equal(exp, res)
        if not b:
            raise Exception(
                "dataframe not equal\nRES:\n{0}\nEXP\n{1}".format(str(res), str(exp)))

    def test_df_equal(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        exp1 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=4, i=1), dict(k1="b", k2="b", v=1, i=2)])
        exp2 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=4, i=1), dict(k1="b", k2="b", v=1, i=2)])
        assert df_equal(exp1, exp2)

        exp1 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=4, i=1), dict(k1="b", k2="b", v=1, i=2)])
        exp2 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=4, i=1), dict(k1="b", k2="b", v=1, i=2)])
        exp2 = exp2[["k2", "k1", "v", "i"]]
        assert df_equal(exp1, exp2)

        exp1 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=4, i=1), dict(k1="b", k2="b", v=1, i=2)])
        exp2 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=3, i=1), dict(k1="b", k2="b", v=1, i=2)])
        assert not df_equal(exp1, exp2)

        exp1 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=4, i=1), dict(k1="b", k2="b", v=1, i=2)])
        exp2 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=numpy.nan, i=1), dict(k1="b", k2="b", v=1, i=2)])
        assert not df_equal(exp1, exp2)

        exp1 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=numpy.nan, i=1), dict(k1="b", k2="b", v=1, i=2)])
        exp2 = pandas.DataFrame(
            [dict(k1="a", k2="b", v=numpy.nan, i=1), dict(k1="b", k2="b", v=1, i=2)])
        assert not df_equal(exp1, exp2)


if __name__ == "__main__":
    unittest.main()
