"""
@brief      test log(time=7s)
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
from src.ensae_teaching_cs.special import tsp_kruskal_algorithm, distance_haversine


class TestFaqMatplotlibVideo(unittest.TestCase):

    def test_american_cities(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[:2] <= (3, 4):
            warnings.warn(
                "Issue with Python 3.4, bug probably related to wrong pointers")
            return
        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt

        def haversine(p1, p2):
            return distance_haversine(p1[0], p1[1], p2[0], p2[1])

        temp = get_temp_folder(__file__, "temp_matplotlib_video")
        data = os.path.join(temp, "..", "data", "american_cities.txt")
        df = pandas.read_csv(data)
        df["Longitude"] = -df["Longitude"]
        df = df[df.Latitude < 52]
        df = df[df.Longitude > -130].copy()
        fLOG(df.columns)
        df = df.dropna()

        if __name__ != "__main__":
            df = df[:40].copy()
        fLOG(df.shape)
        # df["City"] = df["City"].apply(lambda v: filter.get(v, ""))
        points = [(row[1], row[2], row[3])
                  for row in df.itertuples(index=False)]
        fLOG("number of cities:", len(points))
        trip = tsp_kruskal_algorithm(
            points, distance=haversine, fLOG=fLOG, max_iter=10)

        # trip
        dftrip = pandas.DataFrame(
            trip, columns=["Latitude", "Longitude", "City"])
        save = os.path.join(temp, "trip.txt")
        dftrip.to_csv(save, sep="\t", index=False)

        # graph
        for i in range(0, dftrip.shape[0]):
            if i % 10 != 0:
                dftrip.ix[i, "City"] = ""
        fig, ax = plt.subplots(figsize=(32, 32))
        ax = graph_cities(dftrip, ax=ax, markersize=3, linked=True, fLOG=fLOG,
                          fontcolor="red", fontsize='16', loop=True)
        assert ax is not None
        img = os.path.join(temp, "img.png")
        fig.savefig(img)
        assert os.path.exists(img)
        if __name__ == "__main__":
            fig.show()
        plt.close('all')
        fLOG("end")


if __name__ == "__main__":
    unittest.main()
