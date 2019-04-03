# -*- coding: utf-8 -*-
"""
@brief      test log(time=13s)
"""
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version


class TestNotebook1236Coverage201711fair(unittest.TestCase):

    def setUp(self):
        base = ["pymyinstall", "pyensae", "pymmails", "jyquickhelper"]
        try:
            import fairtest
            self.fairtest_installed = fairtest
        except ImportError:
            self.fairtest_installed = None
            base.append('fairtest')
        add_missing_development_version(base, __file__, hide=True)

    def a_test_notebook_runner(self, name, folder, valid=None, copy_files=None, modules=None):
        from ensae_teaching_cs.automation.notebook_test_helper import a_test_notebook_runner
        return a_test_notebook_runner(__file__, name, folder, valid=valid,
                                      copy_files=copy_files, modules=modules, fLOG=fLOG)

    def test_notebook_ethics(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            return '[inv]' not in cell

        import fairtest  # pylint: disable=E0401
        self.a_test_notebook_runner("ethics", "td2a_ml", valid=valid, copy_files=[
                                    "fairtesttree.png"], modules=[fairtest])


if __name__ == "__main__":
    unittest.main()
