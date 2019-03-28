"""
@brief      test log(time=20s)
"""
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_travis, skipif_appveyor, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner2a_2_enonce(unittest.TestCase):

    def setUp(self):
        fLOG("add missing dependencing")
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    @skipif_travis("forgotten issue")
    @skipif_appveyor("forgotten issue")
    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_2_enonce")
        keepnote = ls_notebooks("td2a")

        fold = os.path.dirname(keepnote[0])
        for png in os.listdir(fold):
            if ".png" not in png:
                continue
            fLOG("copy", png)
            shutil.copy(os.path.join(fold, png), temp)
        self.assertTrue(len(keepnote) > 0)

        execute_notebooks(temp, keepnote, lambda i, n: "_2" in n and
                          "enonce" in n and "_2D" not in n and "_2B" not in n,
                          fLOG=fLOG, clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
