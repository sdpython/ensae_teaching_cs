# -*- coding: utf-8 -*-
"""
@brief      test log(time=38s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.filehelper import synchronize_folder
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version, skipif_circleci
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut, get_additional_paths


class TestNotebook123Coverage2d(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper", "mlstatpy"],
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

        import pyquickhelper
        import jyquickhelper
        import pyensae
        import mlstatpy
        import ensae_teaching_cs
        add_path = get_additional_paths(
            [jyquickhelper, pyquickhelper, pyensae, mlstatpy, ensae_teaching_cs])
        res = execute_notebook_list(
            temp, keepnote, additional_path=add_path, valid=valid)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=ensae_teaching_cs)

    @skipif_circleci('Check failed: PyBfloat16_Type.tp_base != nullptr')
    def test_notebook_some_nlp(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_runner("td2a_some_nlp", "td2a")


if __name__ == "__main__":
    unittest.main()
