"""
@brief      test log(time=40s)
"""
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner2aSQL(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def get_replacements(self):
        return {"https://archive.ics.uci.edu/ml/machine-learning-databases/00222/":
                "http://www.xavierdupre.fr/enseignement/complements/"}

    def test_notebook_runner_enonce(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        from ensae_teaching_cs.data import simple_database
        temp = get_temp_folder(__file__, "temp_notebook2a_eco_sql")
        keepnote = ls_notebooks("td2a_eco")
        shutil.copy(simple_database(), temp)
        execute_notebooks(temp, keepnote, (lambda i, n: "sql" in n), fLOG=fLOG,
                          replacements=self.get_replacements(), dump=ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
