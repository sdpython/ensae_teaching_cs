#-*- coding: utf-8 -*-
"""
@brief      test log(time=180s)
"""

import sys
import os
import unittest


try:
    import src.ensae_teaching_cs as thismodule
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src.ensae_teaching_cs as thismodule

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
from pyquickhelper.filehelper import synchronize_folder
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut, get_additional_paths


class TestNotebook123Coverage2(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper", "mlstatpy"],
                                        __file__, hide=True)

    def a_test_notebook_runner(self, name, folder, valid=None, copy_folder=None):
        temp = get_temp_folder(__file__, "temp_notebook_123_{0}".format(name))
        doc = os.path.join(temp, "..", "..", "..", "_doc", "notebooks", folder)
        self.assertTrue(os.path.exists(doc))
        keepnote = [os.path.join(doc, _) for _ in os.listdir(doc) if name in _]
        self.assertTrue(len(keepnote) > 0)

        if copy_folder is not None:
            if not os.path.exists(copy_folder):
                raise FileNotFoundError(copy_folder)
            dest = os.path.split(copy_folder)[-1]
            dest = os.path.join(temp, dest)
            if not os.path.exists(dest):
                os.mkdir(dest)
            synchronize_folder(copy_folder, dest, fLOG=fLOG)

        import pyquickhelper
        import jyquickhelper
        import pyensae
        import mlstatpy
        add_path = get_additional_paths(
            [jyquickhelper, pyquickhelper, pyensae, mlstatpy, thismodule])
        res = execute_notebook_list(
            temp, keepnote, additional_path=add_path, valid=valid)
        execute_notebook_list_finalize_ut(res, fLOG=fLOG, dump=thismodule)

    def test_notebook_ml_d_library_h2o(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if False:
            # h2o is difficult to make work as it launches a server.
            self.a_test_notebook_runner("ml_d_library_h2o", "td2a_ml")

    def test_notebook_visualisation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            if "plotly" in cell:
                return False
            return True

        self.a_test_notebook_runner("td2a_visualisation", "td2a", valid=valid)

    def test_notebook_some_nlp(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("td2a_some_nlp", "td2a")

    def test_notebook_progressbar(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("td2a_progressbar", "td2a")

    def test_notebook_bigdata(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("td2a_bigdata_memory", "td2a")

    def test_notebook_timeseries(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("ml_timeseries_base", "td2a")


if __name__ == "__main__":
    unittest.main()
