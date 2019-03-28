"""
@brief      test log(time=35s)
"""
import os
import unittest
import pandas
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv, ExtTestCase
from ensae_teaching_cs.faq.faq_matplotlib import graph_cities


class TestFaqMatplotlib(ExtTestCase):

    def test_american_cities(self):
        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        filters = {"NewYork": "NY", "Chicago": "CH",
                   "SanFrancisco": "SF", "Seattle": "Sea"}
        temp = get_temp_folder(__file__, "temp_american_cities")
        data = os.path.join(temp, "..", "data", "american_cities.txt")
        df = pandas.read_csv(data)
        df["Longitude"] = -df["Longitude"]
        df["City"] = df["City"].apply(lambda v: filters.get(v, ""))
        df = df[df.Latitude < 52]
        df = df[df.Longitude > -130].copy()
        fig, ax = graph_cities(df, markersize=3, fontcolor=(0, 1.0, 0), fontsize='40',
                               fontweight="bold", figsize=(32, 32))
        self.assertNotEmpty(ax)
        img = os.path.join(temp, "img.png")
        if __name__ == "__main__":
            fig.show()
        fig.savefig(img)
        self.assertExists(img)
        plt.close('all')


if __name__ == "__main__":
    unittest.main()
