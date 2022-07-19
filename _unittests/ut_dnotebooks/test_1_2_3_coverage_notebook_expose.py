# -*- coding: utf-8 -*-
"""
@brief      test log(time=80s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebook123CoverageExpose(unittest.TestCase):

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

        replacements = {'input("Entrez un nombre")': 'random.randint(0, 100)',
                        'input(message)': 'random.randint(0, 100)'}

        execute_notebooks(temp, keepnote,
                          lambda i, n: name in n,
                          fLOG=fLOG, replacements=replacements,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)

    def test_notebook_runner_expose_bjkst(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("BJKST", "expose")

    def test_notebook_runner_expose_einstein(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("einstein", "expose")

    def test_notebook_runner_expose_rwr(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("rwr", "expose")

    def test_notebook_runner_graphe(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("graphe", "expose")

    def test_notebook_runner_hash(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("hash", "expose")

    def test_notebook_runner_ml_feature(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("ml_feature", "expose")


if __name__ == "__main__":
    unittest.main()
