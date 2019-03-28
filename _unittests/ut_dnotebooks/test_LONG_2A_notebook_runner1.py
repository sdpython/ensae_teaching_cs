"""
@brief      test log(time=92s)
"""
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner1(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        temp = get_temp_folder(__file__, "temp_notebook1")
        keepnote = ls_notebooks("td2a")
        fold = os.path.dirname(keepnote[0])
        for png in os.listdir(fold):
            if ".png" not in png:
                continue
            fLOG("copy", png)
            shutil.copy(os.path.join(fold, png), temp)
        self.assertTrue(len(keepnote) > 0)
        execute_notebooks(temp, keepnote, (lambda i, n: "td2a_correction_session_1" in n),
                          fLOG=fLOG, dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
