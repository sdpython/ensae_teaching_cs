"""
@brief      test log(time=35s)
"""

import sys
import os
import unittest
import pandas
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
from src.ensae_teaching_cs.faq.faq_matplotlib import graph_cities


class TestFaqMatplotlib(unittest.TestCase):

    def test_american_cities(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[:2] <= (3, 4):
            warnings.warn("Issue with Python 3.4, bug probably related to wrong pointers")
            return
        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        import mpld3
        filter = {"NewYork": "NY", "Chicago": "CH",
                  "SanFrancisco": "SF", "Seattle": "Sea"}
        temp = get_temp_folder(__file__, "temp_american_cities")
        data = os.path.join(temp, "..", "data", "american_cities.txt")
        df = pandas.read_csv(data)
        df["Longitude"] = -df["Longitude"]
        df["City"] = df["City"].apply(lambda v: filter.get(v, ""))
        fig, ax = plt.subplots(figsize=(32, 32))
        df = df[df.Latitude < 52]
        df = df[df.Longitude > -130].copy()
        ax = graph_cities(df, ax=ax, markersize=3, fontcolor=(0, 1.0, 0), fontsize='40',
                          fontname="Courrier", fontweight="bold")
        assert ax is not None
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        assert os.path.exists(img)
        name2 = os.path.join(temp, "picture.html")
        mpld3.save_html(fig, name2)
        assert os.path.exists(name2)
        if __name__ == "__main__":
            fig.show()
        plt.close('all')
        fLOG("end")


if __name__ == "__main__":
    unittest.main()
