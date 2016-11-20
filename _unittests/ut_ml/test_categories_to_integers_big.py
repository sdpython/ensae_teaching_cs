"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
import pandas


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
from src.ensae_teaching_cs.ml import CategoriesToIntegers


class TestCategoriesToIntegersBig(unittest.TestCase):

    def test_categories_to_integers_big(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), "data", "adult_set.txt")
        df = pandas.read_csv(data, sep="\t")

        trans = CategoriesToIntegers(single=True)
        trans.fit(df)
        newdf = trans.transform(df)
        self.assertEqual(len(newdf.columns), len(df.columns))
        self.assertEqual(list(newdf.columns), list(df.columns))


if __name__ == "__main__":
    unittest.main()
