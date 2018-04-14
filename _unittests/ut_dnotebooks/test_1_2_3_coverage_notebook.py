# -*- coding: utf-8 -*-
"""
@brief      test log(time=21s)
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version


class TestNotebook123Coverage(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def a_test_notebook_runner_1a(self, name, folder):
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from src.ensae_teaching_cs.helpers.size_helper import total_size
        self.assertTrue(total_size)
        temp = get_temp_folder(__file__, "temp_notebook_123_{0}".format(name))
        keepnote = ls_notebooks(folder)
        self.assertTrue(len(keepnote) > 0)

        replacements = {'input("Entrez un nombre")': 'random.randint(0, 100)',
                        'input(message)': 'random.randint(0, 100)'}

        execute_notebooks(temp, keepnote,
                          lambda i, n: name in n,
                          fLOG=fLOG, replacements=replacements,
                          clean_function=clean_function_1a,
                          dump=src.ensae_teaching_cs)

    def test_notebook_runner_1a_exo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("pp_exo_deviner_un_nombre", "td1a")

    def test_notebook_runner_clustering(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("td2a_clustering", "td2a_ml")

    def test_notebook_session8_wikiroot(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("session8_wikiroot", "td1a_algo")

    def test_notebook_session7_edition(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("session7_edition", "td1a_algo")

    def test_notebook_session7_correction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("td1a_correction_session7", "td1a_algo")

    def test_notebook_session7_enonce(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("td1a_cenonce_session7", "td1a_algo")

    def test_notebook_jaccard(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("jaccard", "td1a_algo")

    def test_notebook_texte_langue(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("texte_langue", "td1a")

    def test_notebook_td1a_correction_session6(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("td1a_correction_session6", "td1a")

    def test_notebook_integrale_rectangle(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner_1a("integrale_rectangle", "td1a")


if __name__ == "__main__":
    unittest.main()
