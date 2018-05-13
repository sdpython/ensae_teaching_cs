"""
@brief      test log(time=2s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG


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

from src.ensae_teaching_cs.automation_students.quick_tasks import build_mailing_list


class TestQuickTasks(unittest.TestCase):

    def test_mail_build(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        names = ["DUPRE Xavier", "DU PRE Xav ier"]
        mails = build_mailing_list(names, domain="ensae.fr")
        self.assertEqual(
            mails, ['xavier.dupre@ensae.fr', 'xav.ier.du.pre@ensae.fr'])


if __name__ == "__main__":
    unittest.main()
