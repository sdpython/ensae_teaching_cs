"""
@brief      test tree node (time=50s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestReadme(unittest.TestCase):

    def test_venv_docutils08_readme(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fold = os.path.dirname(os.path.abspath(__file__))
        readme = os.path.join(fold, "..", "..", "README.rst")
        assert os.path.exists(readme)
        with open(readme, "r", encoding="utf8") as f:
            content = f.read()

        assert len(content) > 0
        temp = get_temp_folder(__file__, "temp_readme")

        if __name__ != "__main__":
            # does not work from a virtual environment
            return

        from pyquickhelper.pycode import check_readme_syntax

        check_readme_syntax(readme, folder=temp, fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
