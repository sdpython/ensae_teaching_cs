"""
@brief      test log(time=2s)
"""
import os
import unittest
from pyquickhelper.pycode import get_temp_folder
from ensae_teaching_cs.homeblog.latex_file import LatexFile


class TestLatex(unittest.TestCase):

    def test_latex(self):
        temp = get_temp_folder(__file__, "temp_latex")
        name = os.path.abspath(os.path.normpath(
            os.path.join(temp, "..", "data", "quicksort_cor.tex")))
        ht = LatexFile(name)
        htm = ht.code_in_html()
        self.assertIn("def __", htm)


if __name__ == "__main__":
    unittest.main()
