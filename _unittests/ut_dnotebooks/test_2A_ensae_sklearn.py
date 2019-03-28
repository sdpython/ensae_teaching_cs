# -*- coding: utf-8 -*-
"""
@brief      test log(time=50s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookEnsaeSklearn(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner_ensae_sklearn(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from ensae_teaching_cs.automation.notebook_test_helper import copy_data_file
        from ensae_teaching_cs.helpers.size_helper import total_size
        self.assertTrue(total_size)
        temp = get_temp_folder(__file__, "temp_notebook_ensae_sklearn")
        keepnote = ls_notebooks("sklearn_ensae_course")
        self.assertTrue(len(keepnote) > 0)
        copy_data_file("sklearn_ensae_course",
                       "iris_setosa.jpg", temp, fLOG=fLOG)
        copy_data_file("sklearn_ensae_course",
                       "iris_versicolor.jpg", temp, fLOG=fLOG)
        copy_data_file("sklearn_ensae_course",
                       "iris_virginica.jpg", temp, fLOG=fLOG)
        execute_notebooks(temp, keepnote,
                          lambda i, n: True,
                          fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs,
                          additional_path=[os.path.dirname(keepnote[0])])


if __name__ == "__main__":
    unittest.main()
