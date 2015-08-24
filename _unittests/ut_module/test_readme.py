"""
@brief      test tree node (time=50s)
"""

import sys
import os
import unittest
import re
import shutil
import warnings
import pandas

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
    import src
    import pyquickhelper
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
    import pyquickhelper

from pyquickhelper import fLOG, get_temp_folder

if sys.version_info[0] == 2:
    from codecs import open


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

        temp = get_temp_folder(__file__, "temp_readme")

        if __name__ != "__main__":
            # does not work from a virtual environment
            return

        from pyquickhelper.pycode import check_readme_syntax
        from pyquickhelper.helpgen.markdown_helper import yield_sphinx_only_markup_for_pipy

        check_readme_syntax(readme, folder=temp, fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
