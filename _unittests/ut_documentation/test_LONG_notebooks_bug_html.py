"""
@brief      test log(time=19s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.helpgen import process_notebooks
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


class TestLONGNotebookBugHtml(unittest.TestCase):

    def test_notebook_html_problems(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.split(__file__)[0])
        fold = os.path.normpath(os.path.join(
            path, "..", "..", "_doc", "notebooks", "td2a_eco2"))
        nbs = [os.path.join(fold, _)
               for _ in os.listdir(fold) if _.endswith(".ipynb") and "pocket" in _ and "correction" in _]
        nbs.sort()
        if len(nbs) == 0:
            raise ValueError("No notebooks")
        formats = ["pdf", "ipynb", "html", "python", "rst"]

        temp = get_temp_folder(__file__, "temp_nb_td2A_eco2_bug_html")

        res = process_notebooks(nbs, temp, temp, formats=formats)
        fLOG("*****", len(res))
        for _ in res:
            fLOG(_)
            self.assertTrue(os.path.exists(_[0]))


if __name__ == "__main__":
    unittest.main()
