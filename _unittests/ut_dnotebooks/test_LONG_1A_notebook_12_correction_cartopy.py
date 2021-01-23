# -*- coding: utf-8 -*-
"""
@brief      test log(time=452s)
"""
import unittest
from pyquickhelper.loghelper import fLOG, noLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version, skipif_travis
import ensae_teaching_cs


class TestNotebookRunner1a_correction_12(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    @staticmethod
    def clean_function(code):
        code = code.replace(
            'run_cmd("exemple.xlsx"',
            'skip_run_cmd("exemple.xlsx"')

        skip = ['df["difference"] = ...',
                "df.plot (...)",
                ]
        for s in skip:
            if s in code:
                return ""
        return code

    @skipif_travis("issue with MKL on travis")
    def test_notebook_runner_correction_12(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        temp = get_temp_folder(__file__, "temp_notebook1a_correction_12")
        keepnote = ls_notebooks("td1a_dfnp")
        execute_notebooks(temp, keepnote, (lambda i, n: "correction_session_12" in n),
                          fLOG=fLOG, deepfLOG=fLOG if __name__ == "__main__" else noLOG,
                          clean_function=TestNotebookRunner1a_correction_12.clean_function,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
