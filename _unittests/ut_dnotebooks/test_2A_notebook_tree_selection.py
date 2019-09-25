# -*- coding: utf-8 -*-
"""
@brief      test log(time=32s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version, ExtTestCase
import ensae_teaching_cs


class TestNotebook_TreeSelection(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_tree_selection(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertTrue(ensae_teaching_cs is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "td2a_ml")
        test_notebook_execution_coverage(__file__, "td2a_tree_selection", folder,
                                         this_module_name="ensae_teaching_cs", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
