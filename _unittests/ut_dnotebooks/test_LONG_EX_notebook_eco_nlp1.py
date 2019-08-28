# -*- coding: utf-8 -*-
"""
@brief      test log(time=68s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestLONGNotebookRunner2aEcoNLP1(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner_2a_eco_nlp_long1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_eco_nlp_long1")
        keepnote = ls_notebooks("td2a_eco2")

        def filter(i, n):
            if "td2a_Seance_7_Analyse_de_textes" in n:
                return True
            return False

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
