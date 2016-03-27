"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_____
    import pyensae as skip___
    import pyrsslocal as skip__
    import pymyinstall as skip_
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
    import src
    import pyquickhelper as skip_____
    import pyensae as skip___
    import pyrsslocal as skip__
    import pymmails as skip_

from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.automation_students import ProjectsRepository


class TestRepositoryLittleAspect(unittest.TestCase):

    def test_regular_expression(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        text = """<br /></div>
                    <div><div dir="ltr">Pourriez-vous vous ajouter sur le doodle suivant ?<div><br></div><div>
                    <p style="margin:0in;font-family:Calibri;font-size:11pt" lang="fr">
                    <a href="http://doodle.com/poll/xxxxxxxxc9w8">http://doodle.com/poll/xxxxxxsyz7c9w8</a></p></div></div><div class
                    """
        f = ProjectsRepository._link_regex.findall(text)
        fLOG(f)
        self.assertEqual(len(f), 2)
        self.assertEqual(f[0], "http://doodle.com/poll/xxxxxxxxc9w8")


if __name__ == "__main__":
    unittest.main()
