# -*- coding: utf-8 -*-
"""
@brief      test log(time=53s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version, ExtTestCase


class TestNotebookMlLrf(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "jyquickhelper"],
                                        __file__, hide=True)
        import ensae_teaching_cs
        self.assertTrue(ensae_teaching_cs is not None)

    def test_notebook_(self):
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "td2a_ml")
        test_notebook_execution_coverage(__file__, "ml_lasso_rf_grid_search", folder,
                                         this_module_name="ensae_teaching_cs", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
