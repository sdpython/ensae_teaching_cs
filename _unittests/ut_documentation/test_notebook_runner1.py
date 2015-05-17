"""
@brief      test log(time=55s)
"""

import sys
import os
import unittest
import re

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

try:
    import pyensae
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae

from pyquickhelper.ipythonhelper.notebook_helper import run_notebook
from pyquickhelper import get_temp_folder, fLOG


class TestNotebookRunner1 (unittest.TestCase):

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1")
        nbfile = os.path.join(
            temp,
            "..",
            "..",
            "..",
            "_doc",
            "notebooks",
            "td2a",
            "td2a_correction_session_1.ipynb")
        nbfile = os.path.normpath(nbfile)
        assert os.path.exists(nbfile)
        addpath = [
            os.path.dirname(
                pyquickhelper.__file__), os.path.dirname(
                pyensae.__file__)]
        addpath = [os.path.normpath(os.path.join(_, "..")) for _ in addpath]

        outfile = os.path.join(temp, "out_" + os.path.split(nbfile)[-1])
        assert not os.path.exists(outfile)
        stat, out = run_notebook(nbfile, working_dir=temp, outfilename=outfile,
                                 additional_path=addpath,
                                 valid=lambda code: '%system' not in code)
        fLOG(out)
        assert os.path.exists(outfile)


if __name__ == "__main__":
    unittest.main()
