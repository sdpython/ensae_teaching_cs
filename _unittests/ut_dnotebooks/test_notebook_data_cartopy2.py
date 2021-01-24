# -*- coding: utf-8 -*-
"""
@brief      test log(time=59s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import (
    add_missing_development_version, ExtTestCase, skipif_circleci)


class TestNotebookDataIrep(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "jyquickhelper"],
                                        __file__, hide=True)
        import ensae_teaching_cs
        self.assertTrue(ensae_teaching_cs is not None)

    @skipif_circleci('too long')
    def test_notebook_data_irep(self):
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "data")
        test_notebook_execution_coverage(__file__, "irep", folder,
                                         this_module_name="ensae_teaching_cs", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
