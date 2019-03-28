"""
@brief      test log(time=2s)
"""
import unittest
import numpy
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.homeblog.table_formula import TableFormula


class TestTableFormula3(ExtTestCase):

    def test_TableFormula_correlation_bicolumn(self):
        vals = [0., 1.]
        vals = [vals, vals]
        cor = TableFormula.correlation_bicolumn(vals)
        self.assertEqual(cor, 0.)

    def test_TableFormula_bootstrap(self):
        vals = [0., 1.]
        vals = [vals, vals]
        res = TableFormula.bootstrap(vals, lambda xx: sum(sum(x) for x in xx))
        self.assertEqual(res, (2.0, 2.0, 2.0, 2.0, 2.0))

    def test_TableFormula_init(self):
        vals = [0., 1.]
        vals = [vals, vals]
        tbl = TableFormula(vals)
        tbl.header = ["x", "y"]
        np = numpy.array(vals)
        tbl2 = TableFormula(np)
        self.assertEqual(str(tbl), 'x\ty\n0.0\t1.0')
        self.assertEqual(str(tbl2), 'c0\tc1\n0.0\t1.0\n0.0\t1.0')
        tbl[0, 1] = 2.
        tbl3 = tbl.multiplication_term_term(tbl)
        self.assertEqual(str(tbl3), 'x\ty\n0.0\t4.0')
        html = tbl.__html__()
        self.assertEqual(
            html, '<table>\n<tr><th>x</th><th>y</th></tr>\n<tr><td>0.0</td><td>2.0</td></tr>\n</table>\n')
        rst = tbl.__rst__()
        self.assertEqual(
            rst, '+-----+-----+\n| x   | y   |\n+=====+=====+\n| 0.0 | 2.0 |\n+-----+-----+\n')
        st = tbl.strtype()
        self.assertEqual(st, "x\ty\n<class 'float'>\t<class 'float'>")
        tbl.change_header(['xx', 'yy'])
        st = tbl.strtype()
        self.assertEqual(st, "xx\tyy\n<class 'float'>\t<class 'float'>")
        tbl.add_column_vector('zz', [5.])
        b = str(tbl)
        self.assertEqual(b, 'xx\tyy\tzz\n0.0\t2.0\t5.0')
        tbl4 = tbl.concatenate(tbl2)
        b = str(tbl4)
        self.assertEqual(
            b, 'xx\tyy\tzz\tc0\tc1\n0.0\t2.0\t5.0\t0.0\t1.0\nNone\tNone\tNone\t0.0\t1.0')

        vals = [0., 1.]
        vals = numpy.array([vals, vals])
        tbl = TableFormula(vals)
        tbl.header = ["x", "y"]
        cor = tbl.covariance_col('x', 'y')
        self.assertEqual(cor, 0)


if __name__ == "__main__":
    unittest.main()
