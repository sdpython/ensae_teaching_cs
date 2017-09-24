#-*- coding: utf-8 -*-
"""
@brief      test log(time=209s)
"""

import sys
import os
import unittest


try:
    import src.ensae_teaching_cs as thismodule
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src.ensae_teaching_cs as thismodule

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
from pyquickhelper.filehelper import synchronize_folder
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut, get_additional_paths


class TestNotebook123Coverage4(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def a_test_notebook_runner(self, name, folder, valid=None, copy_folder=None):
        temp = get_temp_folder(__file__, "temp_notebook_123_{0}".format(name))
        doc = os.path.join(temp, "..", "..", "..", "_doc", "notebooks", folder)
        self.assertTrue(os.path.exists(doc))
        keepnote = [os.path.join(doc, _) for _ in os.listdir(doc) if name in _]
        self.assertTrue(len(keepnote) > 0)

        if copy_folder is not None:
            if not os.path.exists(copy_folder):
                raise FileNotFoundError(copy_folder)
            dest = os.path.split(copy_folder)[-1]
            dest = os.path.join(temp, dest)
            if not os.path.exists(dest):
                os.mkdir(dest)
            synchronize_folder(copy_folder, dest, fLOG=fLOG)

        this = os.path.join(temp, "..", "data",
                            "fr.openfoodfacts.org.products.head100.csv")
        this = os.path.normpath(this)

        def clean_function(cell):
            cell = cell.replace("c:/temp/fr.openfoodfacts.org.products.csv",
                                this.replace("\\", "/"))
            return cell

        import pyquickhelper
        import jyquickhelper
        import pyensae
        add_path = get_additional_paths(
            [jyquickhelper, pyquickhelper, pyensae, thismodule])
        res = execute_notebook_list(
            temp, keepnote, additional_path=add_path, valid=valid,
            clean_function=clean_function)
        execute_notebook_list_finalize_ut(res, fLOG=fLOG, dump=thismodule)

    def test_notebook_session_5_cor(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            return True

        self.a_test_notebook_runner(
            "td2a_correction_session_5_donnees_non_structurees_et_programmation_fonctionnelle_corrige",
            "td2a", valid=valid)

    def test_notebook_session_5_cor_short(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            return True

        self.a_test_notebook_runner(
            "td2a_correction_session_5",
            "td2a", valid=valid)

    def test_flask(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            return True

        self.a_test_notebook_runner(
            "TD2A_eco_debuter_flask", "td2a_eco", valid=valid)

    def test_compet2017(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            return True

        self.a_test_notebook_runner(
            "prepare_data_2017", "competitions/2017", valid=valid)

    def test_plus_grande_somme(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            return True

        self.a_test_notebook_runner(
            "td1a_plus_grande_somme_correction", "td1a_algo", valid=valid)


if __name__ == "__main__":
    unittest.main()
