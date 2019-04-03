"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.faq.faq_jupyter import jupyter_open_notebook


class TestFaqIPython(unittest.TestCase):

    def test_faq_ipython(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nbfile = os.path.abspath(os.path.dirname(__file__))
        nbfile = os.path.join(
            nbfile, "..", "..", "_doc", "notebooks", "1a", "code_liste_tuple.ipynb")
        assert os.path.exists(nbfile)

        if __name__ == "__main__" and "travis" not in sys.executable.lower():
            s = jupyter_open_notebook(nbfile, fLOG=fLOG)
            fLOG(s)


if __name__ == "__main__":
    unittest.main()
