# -*- coding: utf-8 -*-
"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest
import copy


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

try:
    import pyensae as skip__
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
    import pyensae as skip__

from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.homeblog.table_formula import TableFormula


class TestTableFormula_td9 (unittest.TestCase):

    def test_td9_json(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        fold = os.path.split(__file__)[0]
        data = os.path.join(fold, "data", "td9_by_hours.txt")
        tbl = TableFormula(data)
        tbl = tbl.values_to_float(True)
        jso = []
        for row in tbl:
            r = copy.copy(row)
            r["name"] = r["last_update"]
            jso.append(r)

        assert len(jso) > 0
        outf = os.path.join(fold, "out_json_paris_velib.json")
        if os.path.exists(outf):
            os.remove(outf)
        with open(outf, "w") as f:
            f.write("[\n")
            f.write("\n".join([str(_) for _ in jso]))
            f.write("\n]\n")
        assert os.path.exists(outf)


if __name__ == "__main__":
    unittest.main()
