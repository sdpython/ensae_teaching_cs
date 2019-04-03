# -*- coding: utf-8 -*-
"""
@brief      test log(time=17s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version, is_travis_or_appveyor
import ensae_teaching_cs


class TestNotebookRunner1a_algo(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper", "mlstatpy"],
                                        __file__, hide=True)

    def test_notebook_runner_enonce_algo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_algo")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        keepnote = ls_notebooks("td1a_algo")

        def filter(i, n):
            if is_travis_or_appveyor() == "travis":
                if "graph1exo_parcours" in n or "graph4exos" in n:
                    # Graphviz is installed but cannot be found.
                    return False
                if "graph_spectral_clustering" in n:
                    # Graphviz is installed but cannot be found.
                    return False
            return "BJKST" in n or ("enonce" not in n and "correction" not in n)

        execute_notebooks(temp, keepnote, filter, fLOG=fLOG,
                          clean_function=clean_function_1a,
                          dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
