# -*- coding: utf-8 -*-
"""
@brief      test log(time=17s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.pycode import skipif_travis, skipif_appveyor
import ensae_teaching_cs


class TestNotebookRunner1a_enonce(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    @skipif_travis("issue with MKL")
    @skipif_appveyor("issue with DLL missing")
    def test_notebook_runner_enonce_9(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_enonce_9")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        keepnote = ls_notebooks("td1a_algo")
        execute_notebooks(temp, keepnote,
                          lambda i, n: "cenonce_session9." in n,
                          fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
