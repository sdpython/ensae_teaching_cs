# -*- coding: utf-8 -*-
"""
@brief      test log(time=9s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_travis, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner1a_correction_9(unittest.TestCase):

    def setUp(self):
        fLOG("add missing dependencies", OutputPrint=__name__ == "__main__")
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    @skipif_travis("too long on travis")
    def test_notebook_runner_correction_9(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a, copy_data_file
        temp = get_temp_folder(__file__, "temp_notebook1a_correction_9")
        keepnote = ls_notebooks("td1a_algo")
        copy_data_file("td1a", "seance4_excel.txt", temp, fLOG=fLOG)
        copy_data_file("td1a", "seance4_excel.xlsx", temp, fLOG=fLOG)
        execute_notebooks(temp, keepnote, (lambda i, n: "_12" not in n and
                                           "session9." in n and "correction" in n),
                          fLOG=fLOG, clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
