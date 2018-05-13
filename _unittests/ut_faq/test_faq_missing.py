"""
@brief      test log(time=4s)
"""

import sys
import os
import unittest
from datetime import datetime
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv


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


from src.ensae_teaching_cs.faq.faq_python import entier_grande_taille, difference_div, python_path, test_unitaire, same_variable, stringio
from src.ensae_teaching_cs.faq.faq_python import property_example, enumerate_regex_search, download_from_url
from src.ensae_teaching_cs.faq.faq_python import sortable_class, list_of_installed_packages
from src.ensae_teaching_cs.faq.faq_python import information_about_package, get_month_name, get_day_name
from src.ensae_teaching_cs.faq.faq_pandas import df_to_clipboard, df_equal, speed_dataframe
from src.ensae_teaching_cs.faq.faq_matplotlib import change_legend_location, avoid_overlapping_dates
from src.ensae_teaching_cs.faq.faq_jupyter_helper import find_best_server, nb_open
from src.ensae_teaching_cs.faq.faq_jupyter import jupyter_open_notebook
from src.ensae_teaching_cs.faq.faq_cvxopt import optimisation


class TestFaqMissing (unittest.TestCase):

    def test_faq_pythonm(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        entier_grande_taille()
        difference_div()
        python_path()
        test_unitaire()
        a, b = 1, 1
        same_variable(a, b)
        stringio("e")
        property_example()
        res = list(enumerate_regex_search("r*", "rararr"))
        self.assertEqual(len(res), 6)

    def test_faq_pythonm2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_faq_pythonm2")
        out = os.path.join(temp, "index.html")
        download_from_url("http://www.xavierdupre.fr", out)

    def test_faq_pythonm3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        sortable_class([5, 5])
        list_of_installed_packages()
        fLOG(information_about_package("pip"))
        self.assertEqual(get_month_name(datetime(2016, 4, 5)), 'April')
        self.assertEqual(get_day_name(datetime(2016, 4, 17)), 'Sunday')

    def test_faq_pandas(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        df = pandas.DataFrame([{"a": 1}])
        more_testing = False
        if more_testing:
            # does not work
            df_to_clipboard(df)
        self.assertTrue(df_equal(df, df))
        speed_dataframe()

    def test_faq_matplotlib(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 1], [1, 1])
        change_legend_location(ax)
        avoid_overlapping_dates(fig)
        plt.close('all')

    def test_faq_jupyter(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.dirname(__file__))
        nb = os.path.join(data, "exercice_xn.ipynb")
        find_best_server(nb)
        more_testing = False
        if more_testing:
            # does not work
            r = nb_open(nb, open_browser=False)
            fLOG(r)
            r = jupyter_open_notebook(nb)
            fLOG(r)

    def test_faq_cvxopt(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        optimisation()


if __name__ == "__main__":
    unittest.main()
