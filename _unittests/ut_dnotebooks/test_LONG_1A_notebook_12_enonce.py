# -*- coding: utf-8 -*-
"""
@brief      test log(time=50s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG, noLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, add_missing_development_version


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


class TestNotebookRunner1a_enonce_12 (unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    @staticmethod
    def clean_function(code):
        code = code.replace(
            'run_cmd("exemple.xlsx"',
            'skip_run_cmd("exemple.xlsx"')

        skip = ['df["difference"] = ...',
                "df.plot (...)",
                "folium.initialize_notebook()",
                "map_osm.display()",
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
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        if is_travis_or_appveyor() == "travis":
            # issue with MKL on travis
            return
        temp = get_temp_folder(__file__, "temp_notebook1a_enonce_12")
        keepnote = ls_notebooks("td1a_dfnp")
        execute_notebooks(temp, keepnote, (lambda i, n: "cenonce_session_12" in n),
                          fLOG=fLOG, deepfLOG=fLOG if __name__ == "__main__" else noLOG,
                          clean_function=TestNotebookRunner1a_enonce_12.clean_function,
                          dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
