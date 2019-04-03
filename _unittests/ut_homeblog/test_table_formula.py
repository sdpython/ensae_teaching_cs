"""
@brief      test log(time=2s)

"""
import os
import unittest
import random
import numpy
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.homeblog.table_formula import TableFormula


class TestTableFormula(unittest.TestCase):

    def fonction1(self, p):
        return (True, True) if p else (False, False)

    def fonction2(self, p):
        if p:
            return (True, True)
        else:
            return (False, False)

    def test_simple_check(self):
        assert self.fonction1(True) == self.fonction2(True)
        assert self.fonction1(False) == self.fonction2(False)

    def test_TableFormulaCore(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        fold = os.path.split(__file__)[0]

        assert TableFormula.delta is not None

        file = os.path.join(fold, "data", "BNP.PA.txt")
        table = TableFormula(file, sep=",")
        table.sort(lambda v: v["Date"])
        assert len(table) > 0

        table = TableFormula("name d_a d_b d_c#A 1 2 3#A 1.1 2.1 3.1#B 3 4 5"
                             .replace(" ", "\t").replace("#", "\n"))
        assert "d_a\td_b\td_c" in str(table)

        dist = table.get_distinct_values("name")
        assert len(dist) > 0

        table.add_column("has_A", lambda v: 1. if "A" in v["name"] else 0.)
        assert len(table) > 0

        x = 1. / 3
        table.add_column_smooth("has_A_smooth", lambda v: v[
                                "has_A"], [-1, 0, 1], [x, x, x])
        assert len(table) > 0

        fil = table.filter(lambda v: v["d_b"] == 2)
        assert len(table) > 0

        rnd = table.random(5)
        assert len(rnd) > 0

        rnd = table.random(1, True)
        assert len(rnd) > 0

        fil = table.filter_quantile(lambda v: v["d_b"], 0, 0.4)
        assert len(fil) > 0

        total = table.aggregate(lambda v: v["d_c"])
        assert total > 0

        table.sort(lambda v: v["d_b"] + v["d_c"])
        assert len(table) > 0

        union = table.union(table)
        assert len(union) > len(table)

        group = table.groupby(lambda v: v["name"],
                              [lambda v: v["d_a"],
                               lambda v: v["d_b"]],
                              ["name", "sum_d_a", "sum_d_b"])
        assert len(group) > 0

        groupmax = table.groupby(lambda v: v["name"],
                                 [lambda v: v["d_a"],
                                  lambda v: v["d_b"]],
                                 ["name", "max_d_a", "max_d_b"],
                                 [max, max])
        assert len(groupmax) > 0

        group = table.groupby(lambda v: v["name"],
                              [lambda v: v["d_a"]],
                              ["name", "weight", "sum_d_a"],
                              [lambda vec, w: sum(vec) / w],
                              lambda v: v["d_b"])
        innerjoin = table.innerjoin(group, lambda v: v["name"],
                                    lambda v: v["name"], "group")
        assert len(innerjoin) > 0

        ext = table.extract_columns(["name", "d_a"])
        assert len(ext) > 0

        ext = table.remove_columns(["d_a"])
        assert len(ext) > 0

        d = table.todict(lambda v: v["name"], lambda v: v["d_b"], True)
        assert len(d) > 0

        d = table.select(lambda v: (v["name"], v["d_b"]))
        assert len(list(d)) > 0

        table.create_index(lambda v: (v["name"], v["d_a"]))
        row = table.get(('A', 1.1))
        assert row
        value = table.get(('A', 1.1), 2)
        assert value
        table = TableFormula("name d_a d_b d_c#A 1 2 3#A 1.1 2.1 3.1#B 3 4 5"
                             .replace(" ", "\t").replace("#", "\n"))
        table.add_column("key_add", lambda v: "unique")
        mul = table.multiply_column_by_row_instance(
            lambda v: v["key_add"],
            lambda v: v["name"])
        assert len(mul) > 0

        table = TableFormula("key_name sum_a len_b avg_c#A 1 2 3#A 1.1 2.1 3.1#B 3 4 5"
                             .replace(" ", "\t").replace("#", "\n"))
        gr = table.groupby_implicit(lambda v: v["key_name"])
        assert len(gr) > 0

    def test_TableFormulaStat(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        table = TableFormula("sum_y#1#1#1#1#1#1#1#1#1#1#1"
                             .replace(" ", "\t").replace("#", "\n"))
        gini = table.Gini(lambda v: v["sum_y"])
        assert gini == 0.

        table = TableFormula("sum_y#1#1#1#1#1#1#1#1#1#1#1#5#10"
                             .replace(" ", "\t").replace("#", "\n"))
        gini = table.Gini(lambda v: v["sum_y"])
        assert 0 < gini < 1

    def test_TableFormulaCore_with_dict(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        data = [{"one": 1, "two": 2}, {"two": 2.1, "three": 3}]
        table = TableFormula(data)
        for row in table.values:
            assert len(row) == 3

    def test_multiply_implicit(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        text = """city\tdate
        A\tjan
        A\tfeb
        B\tfeb""".replace("        ", "")
        table = TableFormula(text)
        assert len(table) == 3
        mul = table.multiply_column_by_row_instance(
            lambda v: v["date"],
            lambda v: v["city"])
        exp = """KEY\tA|city\tA|date\tB|city\tB|date
        feb\tA\tfeb\tB\tfeb
        jan\tA\tjan\tNone\tNone""".replace("        ", "")
        exp = TableFormula(exp)
        exp.sort(lambda v: v["KEY"])
        mul.sort(lambda v: v["KEY"])
        delta = mul.delta(exp)
        if len(delta) > 0:
            for _ in delta:
                fLOG(_)
            assert False

    def test_split_files(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        fold = os.path.split(__file__)[0]
        file = os.path.join(fold, "data", "BNP.PA.txt")
        tempf = os.path.join(fold, "temp_split")
        assert os.path.exists(file)
        if not os.path.exists(tempf):
            os.mkdir(tempf)
        f_ = os.path.join(tempf, "temp_split")
        f1 = f_ + ".0000.txt"
        f2 = f_ + ".0001.txt"
        for f in [f1, f2]:
            if os.path.exists(f):
                os.remove(f)

        split = TableFormula.random_split_file(file, f_, 2, logFunction=fLOG)
        assert split
        for f in [f1, f2]:
            fLOG(f)
            assert os.path.exists(f)

        with open(file, "r") as f:
            lines = f.readlines()
        with open(f1, "r") as f:
            lines1 = f.readlines()
        with open(f2, "r") as f:
            lines2 = f.readlines()

        assert len(lines) == len(lines1) + len(lines2) - 1

    def test_correlation(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [random.random() for i in range(0, 100)]
        values = [[x, x + random.random() / 2] for x in values]
        tbl = TableFormula(["x", "y"], values)
        cov = tbl.covariance()
        assert len(cov.values) == 2
        assert len(cov.header) == 3
        assert cov[1, 1] == cov[0, 2]
        cor = tbl.correlation()
        assert len(cor.values) == 2
        assert len(cor.header) == 3
        assert cov[1, 1] == cov[0, 2]
        assert abs(cor[0, 1] - cor[1, 2]) < 1e-5
        assert abs(1 - cor[1, 2]) < 1e-5

    def test_histogram(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [random.random() for i in range(0, 100)]
        values = [[x, x + random.random() / 2] for x in values]
        tbl = TableFormula(["x", "y"], values)
        hist = tbl.histogram(lambda v: (v["x"], 1), 10)
        assert len(hist) == 11
        ma = max([h[1] for h in hist.values])
        mi = min([h[1] for h in hist.values])
        assert mi < ma
        assert ma < 0.5
        su = sum([h[1] for h in hist.values])
        assert abs(su - 1) < 1e-5
        tbl.values.append([-1., -1.])
        tbl.values.append([2., 2.])
        hist2 = tbl.histogram(lambda v: (v["x"], 1), 10)
        assert hist2[0, 0] > 0
        assert hist2[-1, 0] < 1

        hist = tbl.values_to_float().histograms(["x", "y"], 10)
        fil = hist.filter(lambda v: v["histKey"] is None)
        assert len(fil) == 0
        fil = hist.filter(lambda v: v["x"] is None)
        assert len(fil) > 0

    def test_union_columns(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [random.random() for i in range(0, 100)]
        values = [[x, x + random.random() / 2] for x in values]
        tbl = TableFormula(["x", "y"], values)
        union = tbl.union_columns(["x", "y"])
        assert union.size == (200, 1)

    def test_mu_sigma(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [random.random() for i in range(0, 1000)]
        values = [[random.gauss(-1, 3)] for x in values]
        tbl = TableFormula(["x"], values)
        mu, si = tbl.mu_sigma(lambda v: v["x"])
        self.assertTrue(abs(mu + 1) < 0.5)
        self.assertTrue(abs(si - 3) < 0.5)
        mu, si = tbl.mu_sigma(lambda v: v["x"], removeExtreme=0.01)
        self.assertTrue(abs(mu + 1) < 0.5)
        self.assertTrue(abs(si - 3) < 0.5)
        alls = tbl.mu_sigma_each_column(removeExtreme=0.01)
        self.assertEqual(alls.size, (2, 1))

    def test_matrix_array(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [[random.random(), random.random()] for i in range(0, 10)]
        tbl = TableFormula(["x", "y"], values)
        mat = tbl.np_matrix
        self.assertTrue(isinstance(mat, numpy.matrix))
        tblm = TableFormula(tbl.header, mat)
        self.assertTrue(isinstance(tblm[0, 0], float))
        self.assertTrue("[[" not in str(tblm))
        if tblm != tbl:
            delta = tbl.delta(tblm)
            for d in delta:
                fLOG(d)
            raise AssertionError("should not be")
        arr = tbl.np_array
        self.assertTrue(isinstance(arr, numpy.ndarray))
        tbla = TableFormula(tbl.header, arr)
        self.assertEqual(tbla, tbl)

    def test_matrix_array2(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [[random.random(), random.random()] for i in range(0, 10)]
        tbl = TableFormula(["x", "y"], values)
        cen = tbl.center_reduce()
        self.assertEqual(cen.size, tbl.size)
        self.assertNotEqual(cen[0, 0], tbl[0, 0])

    def test_iter(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [[random.random(), random.random()] for i in range(0, 10)]
        tbl = TableFormula(["x", "y"], values)
        nb = 0
        for row in tbl:
            self.assertTrue(isinstance(row, dict))
            self.assertTrue("x" in row)
            self.assertTrue("y" in row)
            nb += 1
        assert nb > 0

    def test_matrix_operator(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [[random.random(), random.random()] for i in range(0, 10)]
        tbl = TableFormula(["x", "y"], values)
        d2 = tbl + tbl
        dm = tbl * -1
        tt = d2 + dm
        self.assertEqual(tbl, tt)
        rep = tbl.replicate(2)
        self.assertEqual(len(rep), len(tbl) * 2)

    def test_empty_table(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        tbl = TableFormula([["x", "y"]])
        self.assertEqual(tbl.size, (0, 2))

    def test_json(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        values = [random.random() for i in range(0, 100)]
        values = [[x, x + random.random() / 2] for x in values]
        tbl = TableFormula(["x", "y"], values)
        jso = tbl.json
        self.assertTrue(len(jso) > 0)
        self.assertTrue(isinstance(jso, str))


if __name__ == "__main__":
    unittest.main()
