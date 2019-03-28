# -*- coding: utf-8 -*-
"""
@brief      test log(time=50s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner1a_enonce(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner_enonce_1_7(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook1a_enonce_1_7")
        keepnote = ls_notebooks("td1a")
        execute_notebooks(temp, keepnote,
                          lambda i, n: "_12" not in n and
                          "cenonce_session1." not in n and
                          "cenonce_session6." not in n and
                          "cenonce_session8." not in n and
                          "cenonce_session9." not in n and
                          "cenonce_session_10." not in n and
                          "cenonce_session_11." not in n and
                          "enonce" in n,
                          fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
