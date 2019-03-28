"""
@brief      test log(time=35s)
"""
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner2a_2_correction(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        from ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_2_corection")
        keepnote = ls_notebooks("td2a")
        shutil.copy(simple_database(), temp)
        execute_notebooks(temp, keepnote, (lambda i, n: "n_2" in n and
                                           "correction" in n and "_2B" not in n), fLOG=fLOG,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
