"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest


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

try:
    import pyquickhelper as skip_
except ImportError:
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
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.data import gutenberg_name


class TestGutenberg(unittest.TestCase):

    def test_condamne(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        text = gutenberg_name(local=True)
        assert text is not None
        assert text.endswith("pg6838.txt")
        text = gutenberg_name(local=True, load=True)
        assert text is not None
        assert len(text) > 200000

        text = gutenberg_name(local=False)
        assert text is not None
        assert "http" in text
        assert text.endswith("pg6838.txt")
        text = gutenberg_name(local=False, load=True)
        assert text is not None
        assert len(text) > 200000


if __name__ == "__main__":
    unittest.main()
