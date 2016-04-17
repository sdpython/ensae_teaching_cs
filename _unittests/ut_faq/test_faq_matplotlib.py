"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import pandas
import matplotlib.pyplot as plt


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
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.faq.faq_matplotlib import graph_cities


class TestFaqMatplotlib(unittest.TestCase):

    def test_american_cities(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        filter = {"NewYork": "NY", "Chicago": "CH", "SanFrancisco": "SF"}
        temp = get_temp_folder(__file__, "temp_matplotlib")
        data = os.path.join(temp, "..", "data", "american_cities.txt")
        df = pandas.read_csv(data)
        df["Longitude"] = -df["Longitude"]
        df["City"] = df["City"].apply(lambda v: filter.get(v, ""))
        fig, ax = plt.subplots(figsize=(32, 32))
        df = df[df.Latitude < 52]
        df = df[df.Longitude > -130].copy()
        ax = graph_cities(df, ax=ax, markersize=3)
        assert ax is not None
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        assert os.path.exists(img)
        if __name__ == "__main__":
            fig.show()


if __name__ == "__main__":
    unittest.main()
