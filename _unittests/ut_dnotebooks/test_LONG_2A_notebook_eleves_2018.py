"""
@brief      test log(time=20s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version
import ensae_teaching_cs


class TestNotebookEleves201809(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def get_replacements(self):
        return {"https://archive.ics.uci.edu/ml/machine-learning-databases/00222/":
                "http://www.xavierdupre.fr/enseignement/complements/"}

    def test_notebook_runner_eleves_201809(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from ensae_teaching_cs.automation.notebook_test_helper import a_test_notebook_runner
        copy_files = [os.path.join("titanic.csv", "titanic.csv")]
        exe = os.path.join("notebook_eleves", "2018-2019")

        def valid_cell(cell):
            if "nuplet[1] = 5" in cell:
                return False
            if cell == "dico[0]  ##":
                return False
            if cell == "dico[ [4,6] ] = 6":
                return False
            return True

        a_test_notebook_runner(__file__, "2018-09", exe, fLOG=fLOG, valid=valid_cell,
                               copy_files=copy_files, modules=[ensae_teaching_cs])


if __name__ == "__main__":
    unittest.main()
