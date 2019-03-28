# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import unittest
from pyquickhelper.pycode import is_travis_or_appveyor, ExtTestCase
from ensae_teaching_cs.automation import ftp_list_modules


class TestFtpBackup(ExtTestCase):

    @unittest.skipIf(is_travis_or_appveyor() is not None, reason="no credentials")
    def test_ftp_backup(self):
        mod = ftp_list_modules()
        self.assertNotEmpty(mod)


if __name__ == "__main__":
    unittest.main()
