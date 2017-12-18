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

from pyquickhelper.loghelper import fLOG, run_cmd
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version, is_travis_or_appveyor


class TestNotebook123CoverageHuge(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper", "mlstatpy"],
                                        __file__, hide=True)

    def a_test_notebook_runner(self, name, folder, additional_path=None):
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
                          dump=src.ensae_teaching_cs,
                          additional_path=additional_path)

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
            import numpy
            import tables
            foldn = os.path.abspath(os.path.dirname(numpy.__file__))
            foldt = os.path.normpath(os.path.dirname(tables.__file__))
            rootn = os.path.dirname(foldn)
            roott = os.path.dirname(foldt)
            if rootn != roott:
                pp = os.environ.get('PYTHONPATH', '')
                if "SECONDTRY" in pp:
                    raise Exception(
                        "Infinite loog\n{0}\n{1}\n**EXE\n{2}\n**PP\n{3}\n****".format(rootn, roott, sys.executable, pp))
                # We need to run this file with the main python.
                # Otherwise it fails for tables: DLL load failed.
                exe = os.path.normpath(os.path.join(
                    rootn, "..", "..", "python.exe"))
                cmd = '"{0}" -u "{1}"'.format(exe, os.path.abspath(__file__))
                import pyquickhelper
                import pyensae
                import jyquickhelper
                import src.ensae_teaching_cs
                import mlstatpy
                import pymyinstall
                add = ["SECONDTRY"]
                for mod in [pyquickhelper, pyensae, jyquickhelper, src.ensae_teaching_cs, mlstatpy, pymyinstall]:
                    add.append(os.path.normpath(os.path.join(
                        os.path.dirname(mod.__file__), "..")))
                fLOG("set PYTHONPATH={0}".format(";".join(add)))
                os.environ['PYTHONPATH'] = ";".join(add)
                out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
                if len(err) > 0:
                    lines = err.split("\n")
                    lines = [_ for _ in lines if _[0] != " "]
                    lines = [_ for _ in lines if "warning" not in _.lower()]
                    if len(lines) > 0:
                        raise Exception("--CMD:\n{0}\n--OUT:\n{1}\n--ERR\n{2}\n--ERR2\n{3}\n--PP\n{4}".format(
                            cmd, out, err, "\n".join(lines), pp))
            return

        import tables
        assert tables is not None
        this = os.path.abspath(os.path.dirname(tables.__file__))
        self.a_test_notebook_runner(
            "ml_huge", "expose", additional_path=[this])


if __name__ == "__main__":
    unittest.main()
