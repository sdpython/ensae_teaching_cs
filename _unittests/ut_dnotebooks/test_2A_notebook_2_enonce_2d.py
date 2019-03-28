"""
@brief      test log(time=50s)
"""
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
import ensae_teaching_cs


class TestNotebookRunner2a_2_enonce_2D(unittest.TestCase):

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        # this notebook describes how to distribute the work with multiple processors
        # it requires to start multiple clusters first (a command line)
        # and to stop them afterwards
        # it still needs to be implemented
        # we skip !
        warnings.warn(
            "TODO: implement a unit test testing the distribution on multiple processors")

        do_test = False
        if do_test:
            temp = get_temp_folder(__file__, "temp_notebook2a_2_enonce_2D")
            keepnote = ls_notebooks("td2a")
            execute_notebooks(temp, keepnote, lambda i, n: "_2" in n and
                              "enonce" in n and "_2D" in n,
                              fLOG=fLOG, clean_function=clean_function_1a,
                              dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
