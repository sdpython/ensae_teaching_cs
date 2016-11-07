#-*- coding: utf-8 -*-
"""
@brief      test log(time=183s)
"""

import sys
import os
import unittest
import shutil

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
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, add_missing_development_version


class TestNotebookRunner2aEcoNLP(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def common_notebook_runner_2a_eco_nlp_enonce(self, sub):
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a, unittest_raise_exception_notebook
        temp = get_temp_folder(__file__, "temp_notebook2a_eco_nlp_" + sub)
        keepnote = ls_notebooks("td2a_eco")
        assert len(keepnote) > 0
        if sub == "correction":
            folder = os.path.join(temp, "ressources_googleplus")
            os.mkdir(folder)
            folder_note = os.path.split(keepnote[0])[0]
            jsfile = os.path.join(
                folder_note, "ressources_googleplus", "107033731246200681024.json")
            shutil.copy(jsfile, folder)

        def filter(i, n):
            if "Traitement_automatique" not in n:
                return False
            if sub == "enonce":
                if "correction" in n:
                    return False
            elif sub not in n:
                return False
            return True

        res = execute_notebooks(temp, keepnote,
                                filter,
                                fLOG=fLOG,
                                clean_function=clean_function_1a)
        unittest_raise_exception_notebook(res, fLOG)

    def test_notebook_runner_2a_eco_nlp_enonce(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if is_travis_or_appveyor():
            # requires credentials
            return
        self.common_notebook_runner_2a_eco_nlp_enonce("enonce")

    def test_notebook_runner_2a_eco_nlp_correction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        import nltk
        nltk.download('stopwords')
        self.common_notebook_runner_2a_eco_nlp_enonce("correction")


if __name__ == "__main__":
    unittest.main()
