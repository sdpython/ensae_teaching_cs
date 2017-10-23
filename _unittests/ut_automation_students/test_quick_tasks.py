"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_
    import pyensae as skip__
    import pyrsslocal as skip___
    import pymyinstall as skip____
    import pymmails as skip_____
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymyinstall",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymmails",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyrsslocal",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper as skip_
    import pyensae as skip__
    import pyrsslocal as skip___
    import pymmails as skip____

from pyquickhelper.loghelper import fLOG
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
