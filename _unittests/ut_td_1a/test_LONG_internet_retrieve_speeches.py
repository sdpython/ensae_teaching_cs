"""
@brief      test log(time=21s)
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase


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

from src.ensae_teaching_cs.td_1a.discours_politique import enumerate_speeches_from_elysees


class TestRetrieveSpeeches(ExtTestCase):

    def test_retrieve_speeches(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "temp_speeches"))
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            f = os.path.join(temp, _)
            if os.path.isfile(f):
                os.remove(f)

        i = 0
        url = "agenda-decembre-2018"
        for i, disc in enumerate(enumerate_speeches_from_elysees(url=url)):
            fLOG(i, disc)
            if i >= 1:
                break
            self.assertNotEmpty(disc)
        self.assertGreater(i, 1)


if __name__ == "__main__":
    unittest.main()
