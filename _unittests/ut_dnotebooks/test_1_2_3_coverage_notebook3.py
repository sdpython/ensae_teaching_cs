# -*- coding: utf-8 -*-
"""
@brief      test log(time=21s)
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


class TestNotebook123Coverage3(unittest.TestCase):

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

        import pyquickhelper
        import jyquickhelper
        import pyensae
        add_path = get_additional_paths(
            [jyquickhelper, pyquickhelper, pyensae, thismodule])
        res = execute_notebook_list(
            temp, keepnote, additional_path=add_path, valid=valid)
        execute_notebook_list_finalize_ut(res, fLOG=fLOG, dump=thismodule)

    def test_notebook_interro_rapide_20_minutes_2014_11(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            if "for n in nbs:          #" in cell:
                return False
            if "a+b       #" in cell:
                return False
            if "nbs = ( 1, 5, 4, 7 )    #" in cell:
                return False
            if "# on évite la variable l pour ne pas la confondre avec 1" in cell:
                return False
            if "del l[i]                #" in cell:
                return False
            if "del l[i]                  #" in cell:
                return False
            return True

        self.a_test_notebook_runner(
            "interro_rapide_20_minutes_2014_11", "exams", valid=valid)

    def test_notebook_td1a_cenonce_session1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        def valid(cell):
            if "# il manque quelque chose sur cette ligne" in cell:
                return False
            if "# regardez bien" in cell:
                return False
            if "# petit problème de type" in cell:
                return False
            if "# comptez bien" in cell:
                return False
            return True

        self.a_test_notebook_runner(
            "td1a_cenonce_session1", "td1a", valid=valid)


if __name__ == "__main__":
    unittest.main()
