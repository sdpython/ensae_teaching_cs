# -*- coding: utf-8 -*-
"""
@brief      test log(time=183s)
"""

import sys
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_travis, add_missing_development_version

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


class TestNotebookRunner2aEcoSNCF(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    @skipif_travis("execution does not stop")
    def test_notebook_runner_2a_eco_sncf(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from src.ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_eco_sncf")
        keepnote = ls_notebooks("td2a_eco")
        shutil.copy(simple_database(), temp)
        folder_note = os.path.split(keepnote[0])[0]
        jsfile = os.path.join(folder_note, "stop_areas.json")
        shutil.copy(jsfile, temp)

        def filter(i, n):
            if "SNCF" not in n:
                return False
            return True

        execute_notebooks(temp, keepnote,
                          filter,
                          fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
