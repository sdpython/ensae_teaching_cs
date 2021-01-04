# -*- coding: utf-8 -*-
"""
@brief      test log(time=120s)
"""
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner1a_home(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper", "mlstatpy"],
                                        __file__, hide=True)

    def test_notebook_runner_enonce_home(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_home")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        keepnote = ls_notebooks("td1a_home")
        sr = [_ for _ in keepnote if "json" in _]
        shutil.copy(sr[0], temp)

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
