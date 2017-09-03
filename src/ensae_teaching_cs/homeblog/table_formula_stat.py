#-*- coding: utf8 -*-
"""
@file
@brief  Contains TableFormulaStat.
"""


class _TableFormulaStat:
    """
    Contains various statistical functions.

    ::

        table = TableFormula ("sum_y#1#1#1#1#1#1#1#1#1#1#1".replace(" ", "\\t").replace("#","\\n"))
        gini = table.Gini (lambda v : v["sum_y"])
        print (gini)  # expects 1

        table = TableFormula ("sum_y#1#1#1#1#1#1#1#1#1#1#1#5#10".replace(" ", "\\t").replace("#","\\n"))
        gini = table.Gini (lambda v : v["sum_y"])
        print (gini) # expects much more less than 1

    """

    def GiniCurve(self, functionY, functionX=None, isXdx=False):
        """
        Computes the Gini curve, takes the following parameters.

        @param  functionY   revenues
        @param  functionX   sum of persons having an income below Y
                                (or having Y is isXdx is True)
        @param  isXdx       number of persons equal to Y (True) or inferior (False),
                            if True, X,Y couples are sorted
        @return             a curve (x, Gini(x))
        """
        couples = [(0., 0.)]
        for i, row in enumerate(self.values):
            v = self._interpret_row(row)
            x = functionX(v) if functionX is not None else float(i + 1)
            y = functionY(v)
            couples.append((x, y))
            if y < 0:
                raise ValueError(
                    "a value should not be negative for y: " + str(y))
            if x < 0:
                raise ValueError(
                    "a value should not be negative for x: " + str(x))

        if not isXdx:
            couples.sort()

        sumx = sum(_[0] for _ in couples) if isXdx else max(_[0]
                                                            for _ in couples)
        sumy = sum(_[1] for _ in couples)
        couples = [[_[0] / sumx, _[1] / sumy] for _ in couples]

        for i in range(1, len(couples)):
            couples[i][1] += couples[i - 1][1]
            if isXdx:
                couples[i][0] += couples[i - 1][0]
            for _ in (0, 1):
                couples[i][_] = min(couples[i][_], 1.)

        return self._private_getclass()(["x", "Gini(x)"], couples)

    def Gini(self, functionY, functionX=None, isXdx=False):
        """
        computes the Gini, it calls GiniCurve (@see me GiniCurve),
        it takes the following parameters:
        @param  functionY   revenues
        @param  functionX   sum of persons having an income below Y
                                (or having Y is isXdx is True)
        @param  isXdx       number of persons equal to Y (True) or inferior (False),
                            if True, X,Y couples are sorted
        @return             a curve (x, Gini(x))
        """
        giniC = self.GiniCurve(functionY, functionX, isXdx)
        gini = 0.
        row_ = giniC.values[0]

        for i in range(1, len(giniC)):
            row = giniC.values[i]
            dx = row[0] - row_[0]
            y = row[1] + row_[1]
            gini += dx * y
            row_ = row

        return 1. - gini

    def summary(self):
        """
        produces a summary on each columns
        @return     TableFormulaStat
        """

        row = []
        for col in self.header:
            res = self.summary_column(col)
            row.append(res)

        return self._private_getclass()(row)

    def summary_column(self, column_name):
        """
        produces a summary of a column, it the column is numerical, it
        computes, the min, max, quantile, mean, med, std. If it is not,
        count the number of distinct values.
        The function considers an empty column as a non-numerical column.
        The fonction do not consider None values.

        @param      column_name     column name
        @return                     dictionary
        """
        vals = self.select(lambda v: v[column_name])
        vals = [_ for _ in vals if _ is not None]
        missing = len(self) - len(vals)

        if len(vals) > 0:
            try:
                s = sum(vals)
                s2 = sum([v**2 for v in vals])
                m = s / len(vals)
                vals.sort()
                res = {"ave": m,
                       "std": (s2 / len(vals) - m**2) ** 0.5,
                       "med": vals[len(vals) // 2],
                       "min": vals[0],
                       "max": vals[-1],
                       "1qua": vals[len(vals) * 1 // 4],
                       "3qua": vals[len(vals) * 3 // 4],
                       "02.5%": vals[len(vals) * 25 // 1000],
                       "97.5%": vals[len(vals) * 975 // 1000],
                       }
            except Exception:
                count = {}
                for v in vals:
                    count[v] = count.get(v, 0) + 1
                res = {"count": len(count)}
        else:
            res = {"count": 0}

        if missing > 0:
            res["missing"] = missing
        res["var"] = column_name

        return res
