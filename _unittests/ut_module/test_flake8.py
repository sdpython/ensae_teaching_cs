"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
import re
import flake8


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


from pyquickhelper import fLOG, run_cmd


class TestFlake8(unittest.TestCase):

    def test_flake8(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        thi = os.path.abspath(os.path.dirname(__file__))
        src = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        exe = os.path.dirname(sys.executable)
        scr = os.path.join(exe, "Scripts")
        fla = os.path.join(scr, "flake8")
        cmd = fla + " " + src
        out, err = run_cmd(cmd, fLOG=fLOG, wait=True)

        lines = out.split("\n")
        lines = [_ for _ in lines if "E501" not in _ and "__init__.py" not in _ and "E265" not in _
                 and "W291" not in _ and "W293" not in _]
        lines = [_ for _ in lines if len(_) > 1]
        if __name__ == "__main__":
            for l in lines:
                spl = l.split(":")
                if len(spl[0]) == 1:
                    spl[1] = ":".join(spl[0:2])
                    del spl[0]
                    print(
                        '  File "{0}", line {1}, {2}'.format(spl[0], spl[1], spl[-1]))
        if len(lines) > 1:
            raise Exception(
                "{0} lines\n{1}".format(len(lines), "\n".join(lines)))

if __name__ == "__main__":
    unittest.main()
