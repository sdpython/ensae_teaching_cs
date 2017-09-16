#-*- coding: utf-8 -*-
"""
@brief      test log(time=12s)
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
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version, is_travis_or_appveyor


class TestNotebook123CoverageHuge(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper", "mlstatpy"],
                                        __file__, hide=True)

    def a_test_notebook_runner(self, name, folder):
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        from src.ensae_teaching_cs.helpers.size_helper import total_size
        self.assertTrue(total_size)
        temp = get_temp_folder(__file__, "temp_notebook_123_{0}".format(name))
        keepnote = ls_notebooks(folder)
        self.assertTrue(len(keepnote) > 0)

        replacements = {'input("Entrez un nombre")': 'random.randint(0, 100)',
                        'input(message)': 'random.randint(0, 100)'}

        execute_notebooks(temp, keepnote,
                          lambda i, n: name in n,
                          fLOG=fLOG, replacements=replacements,
                          clean_function=clean_function_1a,
                          dump=src.ensae_teaching_cs)

    def test_notebook_runner_ml_huge(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "appveyor":
            # pytables has an issue
            # return
            pass

        if sys.platform.startswith("win"):
            try:
                from tables import IsDescription
            except ImportError:
                import numpy
                fold = os.path.abspath(os.path.dirname(numpy.__file__))
                fold = os.path.normpath(os.path.join(fold, "..", "tables"))
                if not os.path.exists(fold):
                    raise ImportError(
                        "tables is not installed in '{0}'".format(fold))
                os.environ["PATH"] = os.environ.get("PATH", "") + ";" + fold
                from tables import IsDescription
                self.assertTrue(IsDescription is not None)

        self.a_test_notebook_runner("ml_huge", "expose")


if __name__ == "__main__":
    unittest.main()
