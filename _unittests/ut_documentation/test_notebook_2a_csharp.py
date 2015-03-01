#-*- coding: utf-8 -*-
"""
@brief      test log(time=23s)
"""

import sys
import os
import unittest
import re

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
    import pyquickhelper
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
    import pyquickhelper

try:
    import pyensae
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae

try:
    import pymmails
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymmails",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymmails

from pyquickhelper import fLOG, get_temp_folder
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a


class TestNotebookRunner2a_csharp (unittest.TestCase):

    def test_notebook_runner_2a(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook2a_sharp")
        keepnote = ls_notebooks("2a")
        assert len(keepnote) > 0
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "csharp" in n,
                                fLOG=fLOG,
                                clean_function=clean_function_1a)

        assert len(res) > 0
        fails = [(os.path.split(k)[-1], v)
                 for k, v in sorted(res.items()) if not v[0]]
        for f in fails:
            fLOG(f)
        if len(fails) > 0:
            e = str(fails[0][1][1])
            if "Audio device error encountered" in str(e):
                # maybe the script is running on a virtual machine (no Audia
                # device)
                if os.environ["USERNAME"] == "ensaestudent" or \
                   os.environ["USERNAME"] == "vsxavierdupre" or \
                   "paris" in os.environ["COMPUTERNAME"].lower() or \
                   os.environ["USERNAME"].endswith("$"):  # anonymous Jenkins configuration
                    # I would prefer to catch a proper exception
                    # it just exclude one user only used on remotre machines
                    fLOG("no audio")
                    return
            raise e
        else:
            fLOG("success")


if __name__ == "__main__":
    unittest.main()
