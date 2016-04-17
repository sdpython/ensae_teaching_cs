"""
@brief      test log(time=4s)
"""

import sys
import os
import unittest
from datetime import datetime
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
from src.ensae_teaching_cs.faq.faq_python import entier_grande_taille, difference_div, python_path, test_unitaire, same_variable, stringio
from src.ensae_teaching_cs.faq.faq_python import property_example, enumerate_regex_search, download_from_url, sortable_class, list_of_installed_packages
from src.ensae_teaching_cs.faq.faq_python import information_about_package, get_month_name, get_day_name
from src.ensae_teaching_cs.faq.faq_pandas import df_to_clipboard, df_equal, speed_dataframe
from src.ensae_teaching_cs.faq.faq_matplotlib import change_legend_location, avoid_overlapping_dates
from src.ensae_teaching_cs.faq.faq_jupyter_helper import find_best_server, nb_open
from src.ensae_teaching_cs.faq.faq_jupyter import jupyter_open_notebook


class TestFaqMissing (unittest.TestCase):

    def _test_faq_pythonm(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_fpyhton")
        entier_grande_taille()
        difference_div()
        python_path()
        test_unitaire()
        a, b = 1, 1
        same_variable(a, b)
        stringio("e")
        property_example()
        assert list(enumerate_regex_search("r*", "rararr"))
        out = os.path.join(temp, "index.html")
        download_from_url("http://www.xavierdupre.fr", out)
        sortable_class([5, 5])
        list_of_installed_packages()
        fLOG(information_about_package("pip"))
        self.assertEqual(get_month_name(datetime(2016, 4, 5)), 'April')
        self.assertEqual(get_day_name(datetime(2016, 4, 17)), 'Sunday')

    def _test_faq_pandas(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        df = pandas.DataFrame([{"a": 1}])
        if False:
            # does not work
            df_to_clipboard(df)
        assert df_equal(df, df)
        speed_dataframe()

    def _test_faq_matplotlib(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fig, ax = plt.subplots()
        ax.plot([1, 1], [1, 1])
        change_legend_location(ax)
        avoid_overlapping_dates(fig)

    def test_faq_jupyter(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.dirname(__file__))
        nb = os.path.join(data, "exercice_lcs.ipynb")
        find_best_server(nb)
        if False:
            # does not work
            r = nb_open(nb, open_browser=False)
            fLOG(r)
            r = jupyter_open_notebook(nb)
            fLOG(r)


if __name__ == "__main__":
    unittest.main()
