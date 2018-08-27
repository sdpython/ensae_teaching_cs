# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, ExtTestCase

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


from src.ensae_teaching_cs.automation import ftp_list_modules


class TestFtpBackup(ExtTestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no credentials")
    def test_ftp_backup(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = ftp_list_modules()
        fLOG(mod)
        self.assertNotEmpty(mod)


if __name__ == "__main__":
    unittest.main()
