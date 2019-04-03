# -*- coding: utf-8 -*-
"""
@brief      test log(time=803s)

notebook test
"""
import unittest
from pyquickhelper.loghelper import fLOG, noLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunnerExposeLong3(unittest.TestCase):

    def setUp(self):
        fLOG("add missing dependencies", OutputPrint=__name__ == "__main__")
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    def test_notebook_runner_exposelong3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebookexposelong3_")
        keepnote = ls_notebooks("expose")
        execute_notebooks(temp, keepnote,
                          lambda i, n: "mortalite" in n,
                          fLOG=fLOG,
                          deepfLOG=fLOG if __name__ == "__main__" else noLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
