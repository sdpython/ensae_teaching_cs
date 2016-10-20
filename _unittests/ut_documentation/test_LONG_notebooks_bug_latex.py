"""
@brief      test log(time=19s)
@author     Xavier Dupre
"""

import sys
import os
import unittest
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
from pyquickhelper.helpgen import process_notebooks
from pyquickhelper.pycode import is_travis_or_appveyor, get_temp_folder


class TestLONGNotebookBug(unittest.TestCase):

    def test_notebook_latex_problems(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.split(__file__)[0])
        fold = os.path.normpath(os.path.join(
            path, "..", "..", "_doc", "notebooks", "td2a_ml"))
        nbs = [os.path.join(fold, _)
               for _ in os.listdir(fold) if _.endswith(".ipynb") and "problems" in _]
        nbs.sort()
        print(nbs)
        formats = ["pdf", "ipynb", "html", "python", "rst", "docx"]

        if is_travis_or_appveyor() is not None:
            warnings.warn(
                "travis, appveyor, unable to test %s" % self._testMethodName)
            return

        temp = get_temp_folder(__file__, "temp_nb_td2A_ml_bug_latex")

        res = process_notebooks(nbs, temp, temp, formats=formats)
        fLOG("*****", len(res))
        for _ in res:
            fLOG(_)
            assert os.path.exists(_[0])


if __name__ == "__main__":
    unittest.main()
