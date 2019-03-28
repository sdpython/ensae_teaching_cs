# -*- coding: utf-8 -*-
"""
@brief      test log(time=183s)
"""
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
import ensae_teaching_cs


class TestNotebookRunner2aEcoNLP(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def common_notebook_runner_2a_eco_nlp_enonce(self, sub):
        from ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_eco_nlp_" + sub)
        keepnote = ls_notebooks("td2a_eco")
        if sub in ("correction", "enonce"):
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
                                clean_function=clean_function_1a,
                                dump=ensae_teaching_cs)
        return res

    def test_notebook_runner_2a_eco_nlp_enonce(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        self.common_notebook_runner_2a_eco_nlp_enonce("enonce")

    def test_notebook_runner_2a_eco_nlp_correction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        import nltk  # pylint: disable=E0401
        nltk.download('stopwords')
        self.common_notebook_runner_2a_eco_nlp_enonce("correction")


if __name__ == "__main__":
    unittest.main()
