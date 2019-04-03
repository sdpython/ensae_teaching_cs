"""
@brief      test log(time=3s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.data import gutenberg_name


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
