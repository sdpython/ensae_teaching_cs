# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.automation.modules_documentation import rst_table_modules


class TestModulesDocumentation(unittest.TestCase):

    def test_jenkins_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        st = rst_table_modules()
        fLOG("\n" + st)
        self.assertTrue(st is not None)
        self.assertTrue(len(st) > 0)


if __name__ == "__main__":
    unittest.main()
