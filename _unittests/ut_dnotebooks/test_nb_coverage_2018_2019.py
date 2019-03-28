# -*- coding: utf-8 -*-
"""
@brief      test log(time=88s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version, ExtTestCase
import ensae_teaching_cs


class TestNotebookCov_2018_2019(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_2018_2019(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            if "nuplet[1] = 5" in cell:
                return False
            if "dico[0]  ##" in cell:
                return False
            if "dico[ [4,6] ] = 6" in cell:
                return False
            return True

        self.assertTrue(ensae_teaching_cs is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "notebook_eleves", "2018-2019")
        test_notebook_execution_coverage(__file__, "", folder, valid=valid,
                                         this_module_name="ensae_teaching_cs", fLOG=fLOG,
                                         copy_files=['titanic.csv/titanic.csv'])


if __name__ == "__main__":
    unittest.main()
