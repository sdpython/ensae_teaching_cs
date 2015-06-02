"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest
import warnings
import shutil

try:
    import src
    import pyquickhelper
    import pyensae
    import pyrsslocal
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
from src.ensae_teaching_cs.automation.project_helper import get_sections, get_emails


class TestSuivi(unittest.TestCase):

    def test_emails(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.dirname(__file__))
        data = os.path.join(data, "data")
        emails = get_emails(path=data)
        assert emails == [
            'name.lastname@something.fr', ' name.lastname@something']

    def test_sections(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        data = os.path.abspath(os.path.dirname(__file__))
        data = os.path.join(data, "data")
        sections = get_sections(path=data)
        names = [k for k in sorted(sections)]
        assert names == [
            '', 'extrait', 'next', 'pitch', 'programme', 'rapport', 'title']
        #for k,v in sections.items(): fLOG(k,v)
        assert sections["next"] == ['* module tweepy']
        assert sections["extrait"] == [
            '::', '    paragraphe 1', '    paragraphe 2']


if __name__ == "__main__":
    unittest.main()
