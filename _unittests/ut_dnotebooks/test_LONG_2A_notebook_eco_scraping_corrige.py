# -*- coding: utf-8 -*-
"""
@brief      test log(time=14s)
"""
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_appveyor, skipif_travis, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner2aEcoScrapingCorrige(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    @skipif_appveyor("too long for appveyor")
    @skipif_travis("execution does not stop")
    def test_notebook_runner_2a_eco_scraping(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_eco_scraping_corrige")
        keepnote = ls_notebooks("td2a_eco")
        shutil.copy(simple_database(), temp)

        def filter(i, n):
            if "Scraping" not in n:
                return False
            if "corrige" not in n:
                return False
            return True

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
