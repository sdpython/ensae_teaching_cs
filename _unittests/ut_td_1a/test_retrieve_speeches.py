"""
@brief      test log(time=21s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_
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
    import src
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.td_1a.discours_politique import enumerate_speeches_from_elysees


class TestRetrieveSpeeches(unittest.TestCase):

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
        for i, disc in enumerate(enumerate_speeches_from_elysees()):
            fLOG(i, disc)
            if i >= 2:
                break
            assert len(disc) > 0
        assert i > 0


if __name__ == "__main__":
    unittest.main()
