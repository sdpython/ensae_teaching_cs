# -*- coding: utf-8 -*-
"""
@brief      test log(time=96s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.ipythonhelper import test_notebook_execution_coverage
from pyquickhelper.pycode import add_missing_development_version, ExtTestCase
from pyquickhelper.pycode import skipif_appveyor, skipif_travis, skipif_circleci
import ensae_teaching_cs


class TestNotebookCov_Sentiment(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "jyquickhelper"],
                                        __file__, hide=True)

    @skipif_appveyor('missing module en_core_web_sm')
    @skipif_travis('missing module en_core_web_sm')
    @skipif_circleci('missing module en_core_web_sm')
    def test_notebook_sentiment(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            if "dico[0]  ##" in cell:
                return False
            return True

        self.assertTrue(ensae_teaching_cs is not None)
        folder = os.path.join(os.path.dirname(__file__),
                              "..", "..", "_doc", "notebooks", "td2a_ml")
        test_notebook_execution_coverage(__file__, "sentiment", folder, valid=valid,
                                         this_module_name="ensae_teaching_cs", fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
