"""
@brief      test log(time=12s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookEleves2017(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def get_replacements(self):
        return {"https://archive.ics.uci.edu/ml/machine-learning-databases/00222/":
                "http://www.xavierdupre.fr/enseignement/complements/"}

    def test_notebook_runner_eleves(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        temp = get_temp_folder(__file__, "temp_notebook_eleves_2017")
        keepnote = ls_notebooks("notebook_eleves/2017-2018")
        self.assertTrue(len(keepnote) > 0)
        execute_notebooks(temp, keepnote, (lambda i, n: True), fLOG=fLOG,
                          replacements=self.get_replacements(), dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
