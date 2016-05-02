#-*- coding: utf-8 -*-
"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest
import pandas


try:
    import src
    import pyquickhelper as skip_
    import pyensae as skip__
    import pyrsslocal as skip___
    import pymyinstall as skip____
    import pymmails as skip_____
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
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
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyrsslocal",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper as skip_
    import pyensae as skip__
    import pyrsslocal as skip___
    import pymmails as skip____

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.automation_students import enumerate_feedback


class TestFeedback(unittest.TestCase):

    def test_enumerate_feedback(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        exp = [
            "s'il est nécessaire",
        ]

        temp = get_temp_folder(__file__, "temp_enumerate_feedback")
        data = os.path.abspath(os.path.dirname(__file__))
        data = os.path.join(data, "data")
        xls = os.path.join(data, "groupes_eleves_pitch.xlsx")
        df = pandas.read_excel(xls, sheetname=0, index=False)
        comment = pandas.read_excel(xls, sheetname=1, header=None, index=False)
        mails = list(enumerate_feedback(df, comment))
        for i, m in enumerate(mails):
            fLOG("------------", i)
            name = os.path.join(temp, "m%d.html" % i)
            with open(name, "w", encoding="utf-8") as f:
                f.write(
                    '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>\n')
                f.write(m[1])
                f.write("\n</body></html>")
            if i < len(exp):
                assert exp[i] in m[1]


if __name__ == "__main__":
    unittest.main()
