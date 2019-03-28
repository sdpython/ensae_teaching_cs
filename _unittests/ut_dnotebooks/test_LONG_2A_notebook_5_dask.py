"""
@brief      test log(time=20s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
import ensae_teaching_cs


class TestNotebookRunner2a_5_Dask(unittest.TestCase):

    def setUp(self):
        from pyquickhelper.pycode import add_missing_development_version
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=__name__ == "__main__")

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        temp = get_temp_folder(__file__, "temp_notebook2a_5")
        keepnote = ls_notebooks("2a")
        execute_notebooks(temp, keepnote, (lambda i, n: "_5" in n),
                          fLOG=fLOG, dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
