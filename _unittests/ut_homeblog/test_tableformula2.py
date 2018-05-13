"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest
import random
import pandas
from pyquickhelper.loghelper import fLOG


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


from src.ensae_teaching_cs.homeblog.table_formula import TableFormula


class TestTableFormula2 (unittest.TestCase):

    def test_TableFormulaCore_Excel(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        fold = os.path.split(__file__)[0]

        assert TableFormula.delta is not None

        file = os.path.join(fold, "data", "BNP.PA.txt")
        table = TableFormula(file, sep=",")
        table.sort(lambda v: v["Date"])
        assert len(table) > 0

        tempfold = os.path.join(fold, "temp_store")
        if not os.path.exists(tempfold):
            os.mkdir(tempfold)

        tempexc = os.path.join(tempfold, "temp_excel_table.xls")
        if os.path.exists(tempexc):
            os.remove(tempexc)
        assert not os.path.exists(tempexc)

        table.save_as_excel(tempexc)
        assert os.path.exists(tempexc)

        tempexc = os.path.join(tempfold, "temp_excel_table.xlsx")
        if os.path.exists(tempexc):
            os.remove(tempexc)
        assert not os.path.exists(tempexc)

        table.save_as_excel(tempexc)
        assert os.path.exists(tempexc)

    def test_issubclass(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        fold = os.path.split(__file__)[0]

        tbl = TableFormula
        r = issubclass(tbl, TableFormula)
        assert r

        file = os.path.join(fold, "data", "BNP.PA.txt")
        table = tbl(file, sep=",")
        r = issubclass(table.__class__, TableFormula)
        assert r

    def test_addc(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        values = [random.random() for i in range(0, 100)]
        values = [[x, x + random.random() / 2] for x in values]
        tbl = TableFormula(["x", "y"], values)

        tbl.addc("a", lambda v: 0, 0)
        assert tbl.header == ["a", "x", "y"]

        tbl.addc(("aa", "bb"), [lambda v: 4, lambda v: 5], 0)
        assert tbl.header == ["aa", "bb", "a", "x", "y"]

        tbl.addc(("aaa", "bbb"), lambda v: (7, 8), 0)
        assert tbl.header == ["aaa", "bbb", "aa", "bb", "a", "x", "y"]
        assert tbl[0, 0] == 7
        assert tbl[0, 1] == 8

        tbl.addc(("aaaa", "bbba"), lambda v: (8, 9))
        assert tbl.header == ["aaa", "bbb", "aa",
                              "bb", "a", "x", "y", "aaaa", "bbba"]
        assert tbl[0, -2] == 8
        assert tbl[0, -1] == 9

    def test_pandas_matrix(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        fold = os.path.split(__file__)[0]
        file = os.path.join(fold, "data", "BNP.PA.txt")

        df = pandas.read_csv(file, sep=",")
        assert "Date" in df.columns
        assert "High" in df.columns
        assert len(df) == 2344
        mat = TableFormula(df)
        assert len(mat) == 2344
        if not isinstance(mat.header, list):
            raise Exception("expecting type: " + str(type(mat.header)))
        assert mat.header == ['index', 'Date', 'Open',
                              'High', 'Low', 'Close', 'Volume', 'Adj Close']

        df = pandas.read_csv(file, sep=",")
        df.set_index("Date")
        mat = TableFormula(df)
        assert len(mat) == 2344
        assert mat.header == ['index', 'Date', 'Open',
                              'High', 'Low', 'Close', 'Volume', 'Adj Close']
        df = mat.dataframe
        assert len(df) == 2344

    def test_pandas_matrix_index(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")
        fold = os.path.split(__file__)[0]
        file = os.path.join(fold, "data", "BNP.PA.txt")
        df = pandas.read_csv(file, sep=",", index_col=["Date"])
        mat = TableFormula(df)
        assert len(mat) == 2344
        assert mat.header == ['index', 'Open', 'High',
                              'Low', 'Close', 'Volume', 'Adj Close']


if __name__ == "__main__":
    unittest.main()
