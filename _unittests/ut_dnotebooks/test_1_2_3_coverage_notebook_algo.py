# -*- coding: utf-8 -*-
"""
@brief      test log(time=50s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebook123CoverageAlgo(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper", "mlstatpy"],
                                        __file__, hide=True)

    def a_test_notebook_runner(self, name, folder):
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from ensae_teaching_cs.helpers.size_helper import total_size
        self.assertTrue(total_size)
        temp = get_temp_folder(__file__, f"temp_notebook_123_{name}")
        keepnote = ls_notebooks(folder)
        self.assertTrue(len(keepnote) > 0)

        def custom_clean_function_1a(cell):
            if "..." in cell:
                return ""
            if "b[0,0] = 44444444" in cell:
                return ""
            return clean_function_1a(cell)

        replacements = {'input("Entrez un nombre")': 'random.randint(0, 100)',
                        'input(message)': 'random.randint(0, 100)'}

        execute_notebooks(temp, keepnote,
                          lambda i, n: name in n,
                          fLOG=fLOG, replacements=replacements,
                          clean_function=custom_clean_function_1a,
                          dump=ensae_teaching_cs)

    def test_notebook_runner_algo_quicksort(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("quicksort", "td1a_algo")

    def test_notebook_runner_algo_decorrelation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("decorrelation", "td1a_dfnp")

    def test_notebook_runner_algo_sobel(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("sobel_cor", "td1a_algo")


if __name__ == "__main__":
    unittest.main()
