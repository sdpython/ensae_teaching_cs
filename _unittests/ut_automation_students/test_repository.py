"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest
import warnings
import shutil
import pandas

try:
    import src
    import pyquickhelper
    import pyensae
    import pyrsslocal
    import pymyinstall
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
    import pyquickhelper
    import pyensae
    import pyrsslocal

from pyquickhelper import fLOG, get_temp_folder
from src.ensae_teaching_cs.automation_students import ProjectsRepository


class TestRepository(unittest.TestCase):

    def test_sections(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.dirname(__file__))
        data = os.path.join(data, "data")
        dfile = os.path.join(data, "notes_eleves_2104_2015.xlsx")
        df = pandas.read_excel(dfile, skiprows=5)
        df = df[df["Groupe"] != "moyenne"].copy()
        fLOG(df.columns)
        fLOG(df.tail())
        fLOG(df.shape)
        emails = ["firstname.ABOUT@machin.fr".lower(),
                  "one_name.another_name.third.fourth@machin.fr"]
        temp = get_temp_folder(__file__, "temp_repository")
        try:
            proj = ProjectsRepository.create_folders_from_dataframe(df, temp, col_subject="sujet",
                                                                    fLOG=fLOG, col_group=None, email_function=emails,
                                                                    skip_if_nomail=True)
        except ProjectsRepository.MailNotFound:
            pass

        proj = ProjectsRepository.create_folders_from_dataframe(df, temp, col_subject="sujet",
                                                                fLOG=fLOG, col_group=None, email_function=emails,
                                                                must_have_email=False)
        suivi = os.path.join(temp, "firstname.SECOND", "suivi.rst")
        with open(suivi, "r", encoding="utf8") as f:
            content = f.read()
        self.assertIn("* mails: firstname.about@machin.fr", content)

        self.assertEqual(len(proj.Groups), 3)
        mails = proj.get_emails(proj.Groups[0])
        fLOG(mails)
        self.assertEqual(mails, ['firstname.about@machin.fr'])


if __name__ == "__main__":
    unittest.main()
