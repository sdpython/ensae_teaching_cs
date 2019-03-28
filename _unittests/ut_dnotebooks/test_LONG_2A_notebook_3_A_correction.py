"""
@brief      test log(time=620s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner2a_3A_correction(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner_correction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_3A_correction")
        keepnote = ls_notebooks("td2a_ml")
        execute_notebooks(temp, keepnote, (lambda i, n: "_3A" in n and "correction" in n),
                          clean_function=clean_function_1a, dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
