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
from src.ensae_teaching_cs.automation_students import ProjectsRepository


class TestSuivi(unittest.TestCase):

    def test_emails(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.dirname(__file__))
        data = os.path.join(data, "data")
        repo = ProjectsRepository(data)
        self.assertEqual(len(repo.Groups), 2)
        gr = repo.Groups[0]
        emails = repo.get_emails(gr)
        fLOG(emails)
        self.assertEqual(emails, ['name.lastname@something.fr',
                                  'name.lastname@something', 'name.lastname@something.fr', 'name.lastname@something'])

    def test_sections(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.dirname(__file__))
        data = os.path.join(data, "data")
        repo = ProjectsRepository(data)
        if len(repo.Groups) != 2:
            for f in repo.Groups:
                fLOG(f)
            self.assertEqual(len(repo.Groups), 2)
        gr = repo.Groups[0]
        sections = repo.get_sections(gr)
        names = [k for k in sorted(sections)]
        assert names == [
            '', 'extrait', 'next', 'pitch', 'programme', 'rapport', 'title']
        #for k,v in sections.items(): fLOG(k,v)
        if sections["next"] != ['', '* module tweepy', '']:
            raise Exception(sections["next"])
        if sections["extrait"] != ['', '::', '', '    paragraphe 1', '', '    paragraphe 2', '']:
            raise Exception(sections["extrait"])


if __name__ == "__main__":
    unittest.main()
