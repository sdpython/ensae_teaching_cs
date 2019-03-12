"""
@brief      test log(time=19s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.helpgen.process_notebooks import process_notebooks
from pyquickhelper.pycode import get_temp_folder

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


class TestLONGNotebookBug2(unittest.TestCase):

    def test_notebook_latex_problems(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.split(__file__)[0])
        fold = os.path.normpath(os.path.join(
            path, "..", "..", "_doc", "notebooks", "td2a_eco"))
        nbs = [os.path.join(fold, _)
               for _ in os.listdir(fold) if _.endswith(".ipynb") and "TD2A_eco_API_SNCF_corrige" in _]
        nbs.sort()
        formats = ["pdf", "ipynb", "html", "python", "rst"]

        temp = get_temp_folder(__file__, "temp_nb_td2A_eco_bug_latex2")

        res = process_notebooks(nbs, temp, temp, formats=formats)
        fLOG("*****", len(res))
        for _ in res:
            fLOG(_)
            self.assertTrue(os.path.exists(_[0]))


if __name__ == "__main__":
    unittest.main()
