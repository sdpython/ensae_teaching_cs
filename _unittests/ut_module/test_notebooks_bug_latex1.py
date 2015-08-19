"""
@brief      test log(time=19s)
@author     Xavier Dupre
"""

import sys
import os
import unittest
import re
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

from pyquickhelper import fLOG, process_notebooks, get_temp_folder


class TestNoteBooksBugLatex_ecs(unittest.TestCase):

    def test_notebook_latex1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        path = os.path.abspath(os.path.split(__file__)[0])
        nbfold = os.path.normpath(
            os.path.join(path, "..", "..", "_doc", "notebooks"))
        nbs = [os.path.join(nbfold, "notebook_eleves", "2014_2015", "2015_kmeans.ipynb"),
               # os.path.join(nbfold, "notebook_eleves", "2014_2015", "2015_page_rank.ipynb"),
               # os.path.join(nbfold, "notebook_eleves", "2014_2015", "2015_factorisation_matrice.ipynb"),
               ]

        formats = ["pdf", ]

        temp = get_temp_folder(__file__, "temp_nb_bug_latex1")

        if "travis" in sys.executable:
            warnings.warn("travis, unable to test TestNoteBooksBugLatex_ecs.test_notebook_latex1")
            return

        res = process_notebooks(nbs, temp, temp, formats=formats)
        fLOG("*****", len(res))
        for _ in res:
            fLOG(_)
            assert os.path.exists(_[0])


if __name__ == "__main__":
    unittest.main()
