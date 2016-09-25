"""
@brief      test log(time=92s)
"""

import sys
import os
import unittest


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

try:
    import pyensae as skip__
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
    import pyensae as skip__

from pyquickhelper.ipythonhelper import run_notebook
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper import __file__ as location
from pyensae import __file__ as location2
from src import __file__ as init_file


class TestNotebookRunner1 (unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks
        assert ls_notebooks
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
            os.path.dirname(location), os.path.dirname(location2)]
        addpath = [os.path.normpath(os.path.join(_, "..")) for _ in addpath]
        addpath.append(os.path.abspath(os.path.dirname(init_file)))

        outfile = os.path.join(temp, "out_" + os.path.split(nbfile)[-1])
        assert not os.path.exists(outfile)
        stat, out = run_notebook(nbfile, working_dir=temp, outfilename=outfile,
                                 additional_path=addpath,
                                 valid=lambda code: '%system' not in code,
                                 fLOG=fLOG)
        fLOG(out)
        assert os.path.exists(outfile)


if __name__ == "__main__":
    unittest.main()
