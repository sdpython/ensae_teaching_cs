"""
@brief      test log(time=170s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestLONGNotebookRunner_2A_Competition_2016(unittest.TestCase):

    def setUp(self):
        fLOG("add missing dependencies", OutputPrint=__name__ == "__main__")
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "jyquickhelper"], __file__)

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_1")
        keepnote = ls_notebooks("competitions/2016")
        execute_notebooks(temp, keepnote, (lambda i, n: "solution" not in n),
                          clean_function=clean_function_1a,
                          fLOG=fLOG, dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
