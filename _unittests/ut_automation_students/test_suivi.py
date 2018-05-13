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
        groups = list(sorted(repo.Groups))
        gr = groups[0]
        if gr is None or len(gr) < 2:
            raise Exception("Empty group '{0}'".format(gr))
        self.assertEqual(gr, 'group_el1')
        emails = repo.get_emails(gr)
        self.assertEqual(emails, ['name.lastname@something.fr', 'name.lastname@something',
                                  'name.lastname@something.fr', 'name.lastname@something'])

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
        groups = list(sorted(repo.Groups))
        gr = groups[0]
        if gr is None or len(gr) < 2:
            raise Exception("Empty group '{0}'".format(gr))
        self.assertEqual(gr, 'group_el1')
        sections = repo.get_sections(gr)
        names = [k for k in sorted(sections)]
        self.assertEqual(names, ['', 'extrait', 'next',
                                 'pitch', 'programme', 'rapport', 'title'])
        if sections["next"] != ['', '* module tweepy', '']:
            raise Exception(sections["next"])
        if sections["extrait"] != ['', '::', '', '    paragraphe 1', '', '    paragraphe 2', '']:
            raise Exception(sections["extrait"])


if __name__ == "__main__":
    unittest.main()
