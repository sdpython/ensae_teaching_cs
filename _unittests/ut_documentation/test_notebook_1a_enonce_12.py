#-*- coding: utf-8 -*-
"""
@brief      test log(time=50s)

notebook test
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

try:
    import pymyinstall
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymyinstall",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymyinstall


from pyquickhelper import fLOG, get_temp_folder, noLOG
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, unittest_raise_exception_notebook


class TestNotebookRunner1a_enonce_12 (unittest.TestCase):

    @staticmethod
    def clean_function(code):
        code = code.replace(
            'run_cmd("exemple.xlsx"',
            'skip_run_cmd("exemple.xlsx"')

        skip = ['df["difference"] = ...',
                "df.plot (...)",
                "from ggplot import *",
                "folium.initialize_notebook()",
                "map_osm.display()",
                # ggplot calls method show and it opens window blocking the
                # offline execution
                ]
        for s in skip:
            if s in code:
                return ""
        return code

    def test_notebook_runner_enonce_12(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_enonce_12")
        keepnote = ls_notebooks("td1a")
        assert len(keepnote) > 0
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "cenonce_session_12" in n,
                                fLOG=fLOG,
                                deepfLOG=fLOG if __name__ == "__main__" else noLOG,
                                clean_function=TestNotebookRunner1a_enonce_12.clean_function)
        unittest_raise_exception_notebook(res, fLOG)


if __name__ == "__main__":
    unittest.main()
