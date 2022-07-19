# -*- coding: utf-8 -*-
"""
@brief      test log(time=209s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.filehelper import synchronize_folder
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut, get_additional_paths


class TestNotebook123Coverage4Dask(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def a_test_notebook_runner(self, name, folder, valid=None, copy_folder=None):
        temp = get_temp_folder(__file__, f"temp_notebook_123_{name}")
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
        import ensae_teaching_cs
        add_path = get_additional_paths(
            [jyquickhelper, pyquickhelper, pyensae, ensae_teaching_cs])
        res = execute_notebook_list(
            temp, keepnote, additional_path=add_path, valid=valid,
            clean_function=clean_function)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=ensae_teaching_cs)

    def test_compet2017(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            return True

        self.a_test_notebook_runner(
            "prepare_data_2017", "competitions/2017", valid=valid)


if __name__ == "__main__":
    unittest.main()
