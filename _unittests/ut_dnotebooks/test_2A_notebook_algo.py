# -*- coding: utf-8 -*-
"""
@brief      test log(time=73s)
"""
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_appveyor, skipif_travis, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner2aAlgo(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    @skipif_appveyor("too long for appveyor")
    @skipif_travis("execution does not stop")
    def test_notebook_runner_2a_algo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_algo")
        keepnote = ls_notebooks("td2a_algo")
        shutil.copy(simple_database(), temp)

        def filter(i, n):
            if "SNCF" in n:
                return False
            return True

        def clean_function_1a_upgraded(code):
            code = clean_function_1a(code)
            rep = "[1000, 2000, 5000, 10000, 12000, 15000, 17000, 20000]"
            by = "[1000, 2000]"
            code = code.replace(rep, by)
            rep = "[10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]"
            by = "[10, 20, 50, 100, 200]"
            code = code.replace(rep, by)
            return code

        fold = os.path.dirname(keepnote[0])
        for png in os.listdir(fold):
            if ".png" not in png:
                continue
            fLOG("copy", png)
            shutil.copy(os.path.join(fold, png), temp)

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          clean_function=clean_function_1a_upgraded,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
