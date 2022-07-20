# -*- coding: utf-8 -*-
"""
@brief      test log(time=25s)
"""
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import (
    get_temp_folder, skipif_appveyor, skipif_travis, add_missing_development_version,
    skipif_circleci)
import ensae_teaching_cs


class TestNotebookRunner2aML2_grad(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    @skipif_appveyor("too long for appveyor")
    @skipif_travis("execution does not stop")
    @skipif_circleci("too long for circleci")
    def test_notebook_runner_2a_ml_grad(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_ml2_grad")
        keepnote = ls_notebooks("td2a_ml")
        keepnote = [
            _ for _ in keepnote if (
                "machine_learning" not in _ and
                "overfitting" not in _)]
        shutil.copy(simple_database(), temp)

        def filter(i, n):
            if "SNCF" in n:
                return False
            if "Scraping" in n:
                return False
            if "deep_python" in n:
                return False
            if "h2o" in n:
                # h2o is not working from a virtual environment
                return False
            if "td2a" in os.path.split(n)[-1]:
                # already tested by others tests
                return False
            if "libraries" in n:
                return False
            if 'gradient' not in n:
                return False
            return True

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
