# -*- coding: utf8 -*-
"""
@file
@brief  Implements TableFormula.
"""
import copy
import os
import sys
import datetime
import random
import math
import json
import numpy
import pandas
from xlwt import Formatting as EXf
from xlwt import Style as EXs
import xlwt as EXw
from xlsxwriter import workbook as EXxw
from xlrd import open_workbook
from pyquickhelper.loghelper import fLOG, noLOG
from pyquickhelper.loghelper.convert_helper import str2datetime
from pyensae.sql import Database
from .table_formula_stat import _TableFormulaStat


class TableFormula(_TableFormulaStat):
    """
    This class aims at representating a table, it provides
    some "SQL like" functionalities such groupby or innerjoin, select, where...
    This was a custom implementation of a DataFrame before I discover
    `pandas <http://pandas.pydata.org/>`_.

    The class provides an easy to go through the row table by converting each row
    in a dictionary ``{ column_name: value }`` on the run. Example:

    ::

        tbl = TableFormula(...)
        newtbl = tbl.filter(lambda v: v["criteria"] == 5)

    See @see op __init__ for others ways to create a table.

    @var    header      list of column names
    @var    values      list of rows(each row contains as many value as the number of columns)
    @var    index       dictionary { column name: position }, changing ``header`` means also changing ``header``.

    Example:

    ::

        table = TableFormula("name d_a d_b d_c#A 1 2 3#A 1.1 2.1 3.1#B 3 4 5".replace(" ", "\\t").replace("#","\\n"))
        print(table)
        print("one value 0,1:", table[0,1])

        print("---------")
        dist = table.get_distinct_values("name")
        for k in sorted(dist): print("*%d: %s"%(int(dist[k]),k))

        print("---------")
        table.add_column("has_A", lambda v: 1. if "A" in v["name"] else 0.)
        print(table)

        x = 1./3
        print("------------- smoothing", x)
        table.add_column_smooth("has_A_smooth", lambda v: v["has_A"], [-1,0,1], [x,x,x])
        print(table)

        print("--------- filter")
        fil = table.filter(lambda v: v["d_b"] == 2)
        print(fil)

        print("--------- random")
        rnd = table.random(5)
        print(rnd)

        print("--------- random unique")
        rnd = table.random(1, True)
        print(rnd)

        print("--------- filter quantile")
        fil = table.filter_quantile(lambda v: v["d_b"], 0, 0.4)
        print(fil)

        print("--------- aggregate_column")
        total = table.aggregate(lambda v: v["d_c"])
        print(total)

        print("--------- sort")
        table.sort(lambda v: v["d_b"] + v["d_c"])
        print(table)

        print("--------- union")
        union = table.union(table)
        print(union)

        print("--------- group sum")
        group = table.groupby(lambda v: v["name"],
                                [lambda v: v["d_a"],
                                  lambda v: v["d_b"]],
                                ["name", "sum_d_a", "sum_d_b"])
        print(group)

        print("--------- group max")
        groupmax = table.groupby(lambda v: v["name"],
                                [lambda v: v["d_a"],
                                  lambda v: v["d_b"]],
                                ["name", "max_d_a", "max_d_b"],
                                [max, max])
        print(groupmax)

        print("--------- group sum with weights")
        group = table.groupby(lambda v: v["name"],
                                [lambda v: v["d_a"]],
                                ["name", "weight", "sum_d_a"],
                                [lambda vec,w:  sum(vec) / w],
                                lambda v: v ["d_b"])

        print("--------- innerjoin")
        innerjoin = table.innerjoin(group, lambda v: v["name"],
                                           lambda v: v["name"], "group")
        print(innerjoin)

        print("------------- extraction")
        ext = table.extract_columns(["name", "d_a"])
        print(ext)

        print("------------- remove")
        ext = table.remove_columns(["d_a"])
        print(ext)

        print("------------- todict")
        d = table.todict(lambda v: v["name"], lambda v: v["d_b"], True)
        print(d)

        print("------------- select")
        d = table.select(lambda v:(v["name"], v["d_b"]))
        print(list(d))

        print("------------- use of an index")
        table.create_index(lambda v:(v["name"], v["d_a"]))
        row = table.get(('A', 1.1))
        print(row)
        value = table.get(('A', 1.1), 2)
        print(value)

        print("------------- multiply_column_by_row_instance ")
        table = TableFormula("name d_a d_b d_c#A 1 2 3#A 1.1 2.1 3.1#B 3 4 5".replace(" ", "\\t").replace("#","\\n"))
        table.add_column("key_add", lambda v:"unique")
        print(table)
        mul = table.multiply_column_by_row_instance(
                            lambda v: v["key_add"],
                            lambda v: v["name"])
        print(mul)

        if os.path.exists("BNP.PA.txt"):
            print("--------------- financial stock")
            table = TableFormula("BNP.PA.txt", sep=",")
            table.sort(lambda v: v["Date"])
            print(table[:10])

        print("--------------- groupby_implicit")
        table = TableFormula("key_name sum_a len_b avg_c#A 1 2 3#A 1.1 2.1 3.1#B 3 4 5".replace(" ", "\\t").replace("#","\\n"))
        print(table)
        gr = table.groupby_implicit(lambda v: v ["key_name"])
        print(gr)

        print("--------------- covariance")
        values = [random.random() for i in range(0,100)]
        values = [[x, x + random.random()/2] for x in values]
        tbl = TableFormula(["x", "y"], values).values_to_float()
        cov = tbl.covariance()
        print(cov)

        print("--------------- histogram")
        hist = tbl.histogram(lambda v:(v["x"],1), 10)
        print(hist)

        print("--------------- histogram")
        hist = tbl.values_to_float().histograms(["x", "y"], 10)
        print(hist)

        print("--------------- unions of columns")
        hist = tbl.values_to_float().union_columns(["x", "y"])
        print(hist)
    """

    @staticmethod
    def add_header_if_not_present(filename, header, encoding=None, logFunction=noLOG):
        """
        the function checks if the first line contains the column in header
        otherwise, it modifies the file and add them on the first line

        @param      filename        filename
        @param      header          list of column name(all strings)
        @param      encoding        encoding
        @param      logFunction     use this function to log information about what is happening
        """
        if encoding is None:
            with open(filename, "r") as f:
                firstline = f.readline().strip("\n\r ")
            su = sum(map(lambda _: 1 if _ in header else 0, firstline.split("\t")))
            if su < len(header) / 2.0:
                logFunction(  # pragma: no cover
                    "add_header_if_not_present: adding header({0}<{1}){2} to '{3}'\nfirstline:\n{4}".format(
                        su, len(header) / 2, header, filename, firstline))
                with open(filename, "r") as f:
                    text = f.read()
                text = "\t".join(header) + "\n" + text
                logFunction(  # pragma: no cover
                    "add_header_if_not_present: writing")
                with open(filename, "w") as f:
                    f.write(text)
                logFunction(  # pragma: no cover
                    "add_header_if_not_present: complete")
        else:
            with open(filename, "r", encoding=encoding) as f:
                firstline = f.readline().strip("\n\r ")
            su = sum(map(lambda _: 1 if _ in header else 0, firstline.split("\t")))
            if su < len(header) / 2.0:
                logFunction(  # pragma: no cover
                    "add_header_if_not_present: adding header({0}<{1}){2} to '{3}'\nfirstline:\n{4}".format(
                        su, len(header) / 2, header, filename, firstline))
                with open(filename, "r", encoding=encoding) as f:
                    text = f.read()
                text = "\t".join(header) + "\n" + text
                logFunction(  # pragma: no cover
                    "add_header_if_not_present: writing")
                with open(filename, "w", encoding=encoding) as f:
                    f.write(text)
                logFunction(  # pragma: no cover
                    "add_header_if_not_present: complete")

    @staticmethod
    def random_split_file(filename, outfileprefix, nb, has_header=True, encoding=None, logFunction=noLOG):
        """
        split a file in nb buckets by random(lines are sent to a random file as they come)

        @param      filename        filename to split
        @param      nb              number of buckets
        @param      outfileprefix   output files will start with outfileprefix + '%04d.txt' % i
        @param      encoding        encoding
        @param      has_header      the header will be replicated in each created file
        @param      logFunction     to display information
        @return                     list of created files
        """
        firstline = None
        if has_header:
            if encoding is None:
                with open(filename, "r") as f:
                    firstline = f.readline().strip("\n\r ")
            else:  # pragma: no cover
                with open(filename, "r", encoding=encoding) as f:
                    firstline = f.readline().strip("\n\r ")

            logFunction(  # pragma: no cover
                f"random_split_file: file {filename} has header {firstline}")

        logFunction("random_split_file: split %s in %d parts" % (filename, nb))
        fileName = [outfileprefix + (".%04d.txt" % n) for n in range(0, nb)]
        nbline = 0

        if encoding is None:
            filesP = [open(_, "w") for _ in fileName]
            if firstline is not None:
                for _ in filesP:
                    _.write(firstline + "\n")
            with open(filename, "r") as f:
                line = f.readline()
                if firstline is not None:
                    line = f.readline()
                while line is not None and len(line) > 0:
                    h = random.randint(0, nb - 1)
                    filesP[h].write(line)
                    line = f.readline()
                    nbline += 1
                    if nbline % 1000000 == 0:
                        logFunction(  # pragma: no cover
                            "random_split_file: processed %d lines" % nbline)
        else:
            filesP = [open(_, "w", encoding=encoding) for _ in fileName]
            if firstline is not None:
                for _ in filesP:
                    _.write(firstline + "\n")
            with open(filename, "r", encoding=encoding) as f:
                line = f.readline()
                if firstline is not None:
                    line = f.readline()
                while line is not None and len(line) > 0:
                    h = random.randint(0, nb - 1)
                    filesP[h].write(line)
                    line = f.readline()
                    nbline += 1
                    if nbline % 1000000 == 0:
                        logFunction(  # pragma: no cover
                            "random_split_file: processed %d lines" % nbline)

        for _ in filesP:
            _.close()
        logFunction("random_split_file: end")
        return fileName

    @staticmethod
    def ratio(x, y):
        """
        return a ratio between two real values or an empty string if the denominateur is null
        @return   a real of an empty string
        """
        return x * 1.0 / y if y != 0 else (0 if x == 0 else "")

    @staticmethod
    def bootstrap(values, function, nbdraws=-1, alpha=0.05):
        """
        return a confidence interval for a statistics
        @param      values      values
        @param      function    produces the statistics over a random set of observations chosen in values
        @param      nbdraws     number of draws, if it is equal to -1, is equal to len(values)
        @param      alpha       confidence level
        @return                 average, min, lower bound, higher bound, max
        """
        stat = []
        N = len(values) - 1
        if nbdraws == - 1:
            nbdraws = len(values)
        for i in range(nbdraws):
            randset = [values[random.randint(0, N)] for i in range(N + 1)]
            s = function(randset)
            stat.append(s)
        stat.sort()
        lv = len(stat)
        alpha = alpha / 2
        i1 = int(lv * alpha + 0.5)
        i2 = int(lv * (1 - alpha) + 0.5)
        i2 = min(i2, len(stat) - 1)
        av = sum(stat) / len(stat)
        return av, min(stat), stat[i1], stat[i2], max(stat)

    @staticmethod
    def correlation_bicolumn(values, deviations=False, noCenter=False):
        """
        assume values is a matrix with two columns
        @param          values      2 column matrix
        @param          deviations  if True, returns cor, sigma1, sigma2
        @param          noCenter    if True, do not remove the average before computing the covariance,
                                    it means we assume variables are already centered
        @return                     correlation factor or correlation, sigma1, sigma2 if deviations is True
        """
        if len(values) <= 1:
            raise ValueError(  # pragma: no cover
                f"expecting more than one observation, not {len(values)}")

        mx = 0.
        my = 0.
        vx = 0.
        vy = 0.
        co = 0.
        nb = 0.
        for a, b in values:
            nb += 1
            mx += a
            my += b
            vx += a ** 2
            vy += b ** 2
            co += a * b
        mx /= nb
        my /= nb
        vx /= nb
        vy /= nb
        co /= nb
        if not noCenter:
            vx -= mx ** 2
            vy -= my ** 2
            co -= mx * my
        vx = vx ** 0.5
        vy = vy ** 0.5
        v = vx * vy
        if v != 0:
            co /= v
        if deviations:
            return co, vx, vy  # pragma: no cover
        return co

    def _private_getclass(self):
        """
        the class often creates another class of the same type,
        this function returns the class object
        """
        return self.__class__

    def __init__(self, file, numeric_column=None, sep="\t", encoding=None,
                 read_n_lines=-1, sheet=0, **options):
        """
        It can either take a filename, an object TableFormula,
        a list of columns and values.

        :param file: filename or a list of column names or a dictionary,
            file can also be a `pandas DataFrame
            <http://pandas.pydata.org/pandas-docs/dev/dsintro.html#dataframe>`_.
        :param numeric_column: depends on file types(see below examples)
        :param sep: column separator if file is a filename
        :param read_n_lines: read the first n lines(or all if it is -1)
        :param sheet: in case the file is an Excel file, this parameter precises the sheet number or name
        :param suffix_nb: if True, adds an integer to the column name if it is a duplicate

        Example:

        ::

            table = TableFormula("name d_a d_b d_c#A 1 2 3#A 1.1 2.1 3.1#B 3 4 5".replace(" ", "\\t").replace("#","\\n"))

        or

        ::

            table = TableFormula("file.txt", ["nb"])

        or

        ::

            table  = TableFormula(["date", "Y", "Y2", "xl"], values)

        or

        ::

            data = [{ "one":1, "two":2 }, {"two":2.1, "three":3 }]
            table = TableFormula(data)

        or

        ::

            data = { 1:{ "one":2.3, "two":2.2 }, 2:{"one":2.1, "two":3 }
            table = TableFormula("__byrow__", data)

        or

        ::

        table = TableFormula(numpy.matrix(...))

        or

        ::

            table = TableFormula(numpy.array(...))


        @warning In this second case, rows and header are not copied.
        """
        if numeric_column is None:
            numeric_column = []
        if isinstance(file, str):
            if os.path.exists(file):
                self._read_file(file, numeric_column, sep,
                                encoding, read_n_lines, sheet=sheet)
            elif file == "__byrow__" and isinstance(numeric_column, dict):
                self._fill_by_row(numeric_column)
            else:
                lines = file.split("\n")
                if len(lines) == 1:
                    raise FileNotFoundError(  # pragma: no cover
                        f"A file was probably expected but was not found: '{file}'.")
                self._readlines(lines, numeric_column, sep)

        elif isinstance(file, list):
            if len(file) == 0:
                raise ValueError(  # pragma: no cover
                    "Empty data and columns are not allowed.")

            if isinstance(file[0], dict):
                self.index = {}
                self.values = []
                for row in file:
                    for k, v in row.items():
                        if k not in self.index:
                            self.index[k] = len(self.index)

                # we sort the labels to avoid instabilities
                labels = [k for k, v in self.index.items()]
                labels.sort()
                self.index = {}
                for la in labels:
                    self.index[la] = len(self.index)

                for row in file:
                    line = [None for k in self.index]
                    for k, v in row.items():
                        line[self.index[k]] = v
                    self.values.append(line)

                self.header = [None for k in self.index]
                for k, v in self.index.items():
                    self.header[v] = k

                n = len(self.index)
                for row in self.values:
                    while len(row) < n:
                        row.append(None)

            elif isinstance(numeric_column, numpy.matrix):
                self.header = file
                self.index = {}
                for i, h in enumerate(self.header):
                    self.index[h] = i
                self.values = [[float(numeric_column[i, j]) for j in range(
                    numeric_column.shape[1])] for i in range(numeric_column.shape[0])]
            elif isinstance(numeric_column, numpy.ndarray):
                self.header = file
                self.index = {}
                for i, h in enumerate(self.header):
                    self.index[h] = i
                self.values = [[float(numeric_column[i, j]) for j in range(
                    numeric_column.shape[1])] for i in range(numeric_column.shape[0])]
            elif isinstance(file[0], list):
                if len(file) == 1:
                    self.header = file[0]
                    self.values = file[1:] + numeric_column
                    self.index = {}
                    for i, h in enumerate(self.header):
                        self.index[h] = i
                else:
                    self.header = file[0]
                    self.values = file[1:]
                    self.index = {}
                    for i, h in enumerate(self.header):
                        self.index[h] = i
            elif isinstance(file[0], str):
                self.header = file
                self.values = numeric_column
                self.index = {}
                for i, h in enumerate(self.header):
                    self.index[h] = i
            else:
                raise RuntimeError(  # pragma: no cover
                    "This case should not happen: " + str(type(file[0])))

        elif isinstance(file, numpy.matrix):  # pragma: no cover
            self.header = ["c%d" % d for d in range(file.shape[1])]
            self.index = {}
            for i, h in enumerate(self.header):
                self.index[h] = i
            self.values = [[float(file[i, j]) for j in range(
                file.shape[1])] for i in range(file.shape[0])]

        elif isinstance(file, numpy.ndarray):
            self.header = ["c%d" % d for d in range(file.shape[1])]
            self.index = {}
            for i, h in enumerate(self.header):
                self.index[h] = i
            self.values = [[float(file[i, j]) for j in range(
                file.shape[1])] for i in range(file.shape[0])]

        else:
            if isinstance(file, pandas.DataFrame):
                def convert(x):
                    return None if isinstance(x, float) and numpy.isnan(x) else x
                df = file
                self.header = [_ for _ in df.columns]
                hi = 'index'
                while hi in self.header:
                    hi += "_"
                self.header.insert(0, hi)
                self.values = []
                for i, row in enumerate(df.values):
                    row = [df.index[i]] + [convert(x) for x in row]
                    self.values.append(row)

                self.index = {}
                for i, h in enumerate(self.header):
                    self.index[h] = i
            else:
                raise TypeError(  # pragma: no cover
                    "File has an unexpected type: " + str(type(file)))

        unique = {}
        for i, c in enumerate(self.header):
            if c in unique:
                if options.get("suffix_nb", False):
                    c = "%s_%d" % (c, i)
                    self.header[i] = c
                else:
                    raise KeyError(  # pragma: no cover
                        f"column '{c}' already exists in '{self.header}'")
            unique[c] = True

    def __add__(self, other):
        """
        do an addition, add values if types are matching
        :param other: matrix or float or string
        :return: new matrix, keep the header of the first matrix
        """
        if len(self) != len(other):
            raise ValueError(  # pragma: no cover
                "both matrices should have the same number of rows")
        if len(self.header) != len(other.header):
            raise ValueError(  # pragma: no cover
                "both matrices should have the same number of columns")
        values = []
        for row, rowo in zip(self.values, other.values):
            r = []
            for a, b in zip(row, rowo):
                if type(a) == type(b):
                    x = a + b
                else:
                    x = None
                r.append(x)
            values.append(r)
        return self._private_getclass()(self.header, values)

    def __mul__(self, other):
        """
        do a multiplication(by a number)
        :param other: matrix or float or string
        :return: new matrix, keep the header of the first matrix
        """
        if not isinstance(other, float) and not isinstance(other, int):
            raise TypeError(  # pragma: no cover
                "other should be a number")
        values = []
        for row in self.values:
            r = []
            for a in row:
                if a is not None:
                    x = a * other
                else:
                    x = None
                r.append(x)
            values.append(r)
        return self._private_getclass()(self.header, values)

    def multiplication_term_term(self, other):
        """
        do a multiplication term by term(similar to an addition),
        add values if types are matching

        :param other: matrix or float or string
        :return: new matrix, keep the header of the first matrix
        """
        if len(self) != len(other):
            raise ValueError(  # pragma: no cover
                "both matrices should have the same number of rows")
        if len(self.header) != len(other.header):
            raise ValueError(  # pragma: no cover
                "both matrices should have the same number of columns")
        values = []
        for row, rowo in zip(self.values, other.values):
            r = []
            for a, b in zip(row, rowo):
                if type(a) == type(b) and not isinstance(a, str):
                    x = a * b
                else:
                    x = None
                r.append(x)
            values.append(r)
        return self._private_getclass()(self.header, values)

    def replicate(self, times):
        """replicates all rows a given number of times
        :param times: number of multiplication
        :return: new matrix, keep the header of the first matrix
        """
        values = []
        for i in range(0, times):
            values.extend(copy.copy(self.values))
        return self._private_getclass()(self.header, values)

    @property
    def size(self):
        """
        returns the size(nb rows, nb columns)
        """
        return len(self), len(self.header)

    @property
    def shape(self):
        """
        returns the size(nb rows, nb columns)
        """
        return self.size

    def _fill_by_row(self, values):
        """
        fill the table
        :param values: dictionary { <int_row_index>: { <column name>: value} }
        """
        mx = max(values.keys()) + 1
        self.index = {}
        self.header = []
        for k, v in values.items():
            for col in v:
                if col not in self.index:
                    self.index[col] = len(self.index)
                    self.header.append(col)
        self.values = [[None for h in self.header] for k in range(mx)]
        for k, v in values.items():
            for col, to in v.items():
                self.values[k][self.index[col]] = to

    def __getitem__(self, irow):
        """
        operator [], accepts slices
        :param irow: integer, tuple, slice or list
        :return: depends on irow
            - int --> a table with one row
            - slice --> a table with several rows
            - list --> a table with the selected rows
            - tuple --> a value
        """
        if isinstance(irow, int):
            return self._private_getclass()(
                self.header, [self.values[irow]])
        if isinstance(irow, slice):
            return self._private_getclass()(
                self.header, [self.values[ii] for ii in range(*irow.indices(len(self)))])
        if isinstance(irow, list):
            return self._private_getclass()(
                self.header, [self.values[ii] for ii in irow])
        if isinstance(irow, tuple):
            if isinstance(irow[1], str):
                row = self.values[irow[0]]
                v = self._interpret_row(row)
                return v[irow[1]]
            return self.values[irow[0]][irow[1]]
        raise TypeError("Invalid argument type: " + str(type(irow)))

    def __setitem__(self, irow, value):
        """
        operator [], just accepts tuple(to change a value)
        :param irow: 2-uple
        :param value: new value
        """
        if isinstance(irow, tuple):
            if isinstance(irow[1], str):
                row = self.values[irow[0]]
                v = self._interpret_row(row)
                v[irow[1]] = value
            else:
                self.values[irow[0]][irow[1]] = value
        else:
            raise TypeError(  # pragma: no cover
                "Invalid argument type(only tuple accepted): " + str(type(irow)))

    def __len__(self):
        """
        returns the number of rows
        """
        return len(self.values)

    def __copy__(self):
        """
        operator copy
        """
        return self._private_getclass()(self.header, self.values)

    def __deepcopy__(self, memo):
        """
        operator ``deepcopy``
        """
        return self._private_getclass()(copy.deepcopy(self.header, memo), copy.deepcopy(self.values, memo))

    def copy(self):
        """
        call ``copy.deepcopy(self)``
        """
        return copy.deepcopy(self)

    def delta(self, other):
        """
        returns a list of differences between self and others

        :param other: TableFormula
        :return: list of differences(first one)
        """
        if other is None:
            return False
        if not isinstance(other, TableFormula):
            raise TypeError("other is not a table: " + str(type(other)))
        if len(self.header) != len(other.header):
            return ["different number of columns"]
        for a, b in zip(self.header, other.header):
            if a != b:
                return ["different columns"]
        if len(self.values) != len(other.values):
            return ["different number of rows"]
        line = 0
        for r, s in zip(self.values, other.values):
            if len(r) != len(s):
                return ["different number of values on row %d" % line]
            col = 0
            for a, b in zip(r, s):
                if a != b:
                    return ["different value on cell %d,%d: %s!=%s(type %s, %s)" % (line, col, a, b, str(type(a)), str(type(b)))]
                col += 1
            line += 1
        return []

    def __eq__(self, other):
        """
        check if two tables are equal by value
        :param other: other table
        :return: boolean
        """
        if other is None:
            return False
        if not isinstance(other, TableFormula):
            return False
        if len(self.header) != len(other.header):
            return False
        for a, b in zip(self.header, other.header):
            if a != b:
                return False
        if len(self.values) != len(other.values):
            return False
        for r, s in zip(self.values, other.values):
            if len(r) != len(s):
                return False
            for a, b in zip(r, s):
                if a != b:
                    return False
        return True

    def __str__(self):
        """
        convert the table into a string
        :return: string
        """
        rows = ["\t".join(self.header)]
        for row in self.values:
            s = "\t".join([str(_) for _ in row])
            rows.append(s)
        return "\n".join(rows)

    def __html__(self, class_table=None, class_td=None, class_tr=None, class_th=None):
        """
        Converts the table into a :epkg:`html` string.

        :param class_table: adds a class to the tag ``table`` (None for none)
        :param class_td: adds a class to the tag ``td`` (None for none)
        :param class_tr: adds a class to the tag ``tr`` (None for none)
        :param class_th: adds a class to the tag ``th`` (None for none)
        """
        clta = f' class="{class_table}"' if class_table is not None else ""
        cltr = f' class="{class_tr}"' if class_tr is not None else ""
        cltd = f' class="{class_td}"' if class_td is not None else ""
        clth = f' class="{class_th}"' if class_th is not None else ""

        rows = [f"<table{clta}>"]
        rows.append("{0}{1}{2}".format(("<tr%s><th%s>" % (cltr, clth)),
                                       ("</th><th%s>" % clth).join(self.header), "</th></tr>"))
        septd = f"</td><td{cltd}>"
        strtd = f"<tr{cltr}><td{cltd}>"
        for row in self.values:
            s = septd.join([str(_) for _ in row])
            rows.append(strtd + s + "</td></tr>")
        rows.append("</table>")
        rows.append("")
        return "\n".join(rows)

    def __rst__(self, add_line=True):
        """
        convert the table into rst format

        ::

            +------------------------+------------+----------+----------+
            | Header row, column 1   | Header 2   | Header 3 | Header 4 |
            | (header rows optional) |            |          |          |
            +========================+============+==========+==========+
            | body row 1, column 1   | column 2   | column 3 | column 4 |
            +------------------------+------------+----------+----------+
            | body row 2             | ...        | ...      |          |
            +------------------------+------------+----------+----------+

        :param add_line: add a line separator between each row
        """
        tbl = self.values_to_str()
        length = [len(_) for _ in tbl.header]
        for row in tbl.values:
            for i, v in enumerate(row):
                length[i] = max(length[i], len(v))
        length = [_ + 2 for _ in length]
        line = ["-" * le for le in length]
        lineb = ["=" * le for le in length]
        sline = f"+{'+'.join(line)}+"
        slineb = f"+{'+'.join(lineb)}+"
        res = [sline]

        def complete(cool):
            s, i = cool
            i -= 2
            if len(s) < i:
                s += " " * (i - len(s))
            return s

        res.append(f"| {' | '.join(map(complete, zip(tbl.header, length)))} |")
        res.append(slineb)
        res.extend([f"| {' | '.join(map(complete, zip(row, length)))} |"
                    for row in tbl.values])
        if add_line:
            t = len(res)
            for i in range(t - 1, 3, -1):
                res.insert(i, sline)
        res.append(sline)
        return "\n".join(res) + "\n"

    def strtype(self):
        """
        displays the type of values(not the values)
        """
        rows = ["\t".join(self.header)]
        for row in self.values:
            s = "\t".join([str(type(_)) for _ in row])
            rows.append(s)
        return "\n".join(rows)

    def _read_file(self, file, numeric_column, sep, encoding, read_n_lines, sheet=0):
        """
        private
        """
        ext = os.path.splitext(file)[-1].lower()
        if ext in [".xls", ".xlsx"]:
            lines = list(open_workbook(file, sheet=sheet))
            # removing empty column(assuming first row is the header)
            ind = [i for i, n in enumerate(lines[0]) if len(n) > 0]
            if len(ind) < len(lines[0]):
                lines = [[line[i] for i in ind] for line in lines]
        else:
            if sys.version_info.major >= 3 or encoding is None:
                if encoding is None:
                    f = open(file, "r")
                else:
                    f = open(file, "r", encoding=encoding)
            else:
                f = open(file, "r", encoding=encoding)

            if read_n_lines > 0:
                lines = []
                for line in f:
                    if len(lines) >= read_n_lines:
                        break
                    lines.append(line)
            else:
                lines = f.readlines()
            f.close()
        self._readlines(lines, numeric_column, sep)

    def change_header(self, new_header):
        """
        change the column names

        :param new_header: a list or a function which modifies the header

        Example:

        ::

            tbl.change_header(lambda h: h if h != "column" else "new_name")

        .. warning:: Do not do that yourself, the class holds a dictionary up to date with the column index.
        """
        if isinstance(new_header, list):
            self.header = new_header
            self.index = {}
            for i, h in enumerate(self.header):
                self.index[h] = i
        else:
            he = [new_header(h) for h in self.header]
            self.change_header(he)

    def rename_column(self, old_name, new_name):
        """
        rename a column

        :param old_name: old name
        :param new_name: new name
        """
        header = [{old_name: new_name}.get(_, _) for _ in self.header]
        self.change_header(header)

    def save(self, filename, sep="\t", encoding=None, newline="\n"):
        """
        saves the tables in a text file, first row is the column names

        :param filename: filename
        :param sep: column separator
        :param encoding: encoding
        :param newline: line separator
        """
        if sys.version_info.major >= 3 or encoding is None:
            if encoding is None:
                f = open(filename, "w", newline=newline)
            else:
                f = open(filename, "w", encoding=encoding, newline=newline)
        else:
            f = open(filename, "w", encoding=encoding)

        f.write(sep.join(self.header))
        f.write("\n")
        for row in self.values:
            f.write(sep.join([str(_) for _ in row]))
            f.write("\n")
        f.close()

    def _readlines(self, lines, numeric_column, sep):
        """private"""
        if isinstance(lines[0], str):
            lines = [_.replace("\ufeff", "").replace("\xef\xbb\xbf", "")
                     .strip("\n\r ").split(sep) for _ in lines if len(_) > 0]
            self.header = lines[0]
            self.values = lines[1:]
            self.index = {}
            for i, h in enumerate(self.header):
                self.index[h] = i
        elif isinstance(lines[0], list):
            self.header = lines[0]
            self.values = lines[1:]
            self.index = {}
            for i, h in enumerate(self.header):
                self.index[h] = i
        else:
            raise Exception("unexpected format: " + str(type(lines[0])))

        self._auto_conversion(numeric_column)

    def _auto_conversion(self, others_columns):
        """
        private
        set up the column type based on the column name
        """
        def condition(k):
            if k.startswith("sum_") or k.startswith("pos_"):
                return True
            if k.startswith("avg_") or k.startswith("len_"):
                return True
            if k.startswith("nb_") or k.startswith("max_") or k.startswith("min_"):
                return True
            if k.startswith("d_") or k in others_columns:
                return True
            if k in ["Open", "High", "Low", "Close", "Volume", "Adj Close"]:
                return True
            if k in ["distance", "nb"]:
                return True
            return False

        for i, k in enumerate(self.header):
            if k == "Date":
                for row in self.values:
                    if isinstance(row[i], str):
                        row[i] = datetime.datetime.strptime(row[i], '%Y-%m-%d')
                    elif isinstance(row[i], float):
                        row[i] = datetime.datetime.utcfromtimestamp(row[i])
                    else:
                        raise Exception(
                            f"unable to extract a date from type {type(row[i])}")
            elif condition(k):
                for row in self.values:
                    row[i] = float(row[i])
            else:
                for row in self.values:
                    if isinstance(row[i], str) and row[i] == "None":
                        row[i] = None

    def get_column_values(self, col):
        """
        private
        returns all values for one column
        """
        i = self.index[col]
        return [row[i] for row in self.values]

    def get_distinct_values(self, col):
        """private"""
        row = self.get_column_values(col)
        dis = {}
        for r in row:
            dis[r] = dis.get(r, 0) + 1
        return dis

    def _interpret_row(self, row):
        """
        private
        returns each row as a dictionary { column_name:value }
        """
        values = {}
        for a, b in zip(self.header, row):
            values[a] = b
        return values

    def __iter__(self):
        """
        iterator on all rows, it returns a dictionary { column:value }
        @return     dictionary
        """
        for row in self.values:
            yield self._interpret_row(row)

    def add_column(self, colname, function, position=-1):
        """
        Adds a column.
        :param colname: column name or columns name if it is a list or a tuple
        :param function: function which will gives the values(or a list of functions, or a function which return a tuple)
        :param position: where to insert the column, -1 for the end

        Example:

        ::

            table.add_column("has_A", lambda v: 1 if "A" in v["name"] else 0, 0)

            table.add_column(("has_A", "has_B"),(lambda v: 1 if "A" in v["name"] else 0,
                                                    lambda v: 1 if "B" in v["name"] else 0))

            table.add_column(("has_A", "has_B"),(lambda v:(1 if "A" in v["name"] else 0, 1 if "B" in v["name"] else 0))
        """
        if isinstance(colname, str):
            if position == -1:
                self.index[colname] = len(self.index)
                for row in self.values:
                    v = self._interpret_row(row)
                    x = function(v)
                    row.append(x)
                self.header.append(colname)
            else:
                for row in self.values:
                    v = self._interpret_row(row)
                    x = function(v)
                    row.insert(position, x)
                self.header.insert(position, colname)
                self.index = {v: i for i, v in enumerate(self.header)}

        elif isinstance(function, list):
            if len(colname) != len(function):
                raise ValueError(  # pragma: no cover
                    "unable to continue, colname and function do not have the same number of elements")
            if position == -1:
                position = [-1] * len(colname)
            elif isinstance(position, int):
                position = [position] * len(colname)
            else:
                if len(position) != len(colname):
                    raise RuntimeError(  # pragma: no cover
                        "Unable to continue, colname and position do not "
                        "have the same number of elements.")
            dec = 0
            for a, b, c in zip(colname, function, position):
                self.add_column(a, b, c + dec)
                dec += 1

        else:
            # we assume here, the function returns a tuple
            if not isinstance(position, int):
                raise TypeError(  # pragma: no cover
                    "Int expected for position for this case.")

            if position == -1:
                for row in self.values:
                    v = self._interpret_row(row)
                    x = function(v)
                    row.extend(x)
                self.header.extend(colname)

            else:
                for row in self.values:
                    v = self._interpret_row(row)
                    x = function(v)
                    for i, _ in enumerate(x):
                        row.insert(position + i, _)
                for i, c in enumerate(colname):
                    self.header.insert(position + i, c)
            self.index = {v: i for i, v in enumerate(self.header)}
        return self

    def add_column_index(self, colname="index", start=0):
        """
        Example:

        ::

            table.add_column("index_row")
        """
        self.index[colname] = len(self.index)
        for i, row in enumerate(self.values):
            row.append(i + start)
        self.header.append(colname)
        return self

    def addc(self, colname, function, position=-1):
        """
        @see me add_column
        """
        return self.add_column(colname, function, position)

    def add_column_recursive(self, colname, functionValue, functionAgg):
        """
        Example:

        ::

            table.add_column_recursive(lambda v: v ["norm_%s" % loi],
                                       lambda li, v: li[-1] + v)
        """
        self.index[colname] = len(self.index)
        values = []
        for row in self.values:
            v = self._interpret_row(row)
            x = functionValue(v)
            y = functionAgg(values, x)
            row.append(y)
            values.append(y)
        self.header.append(colname)
        return self

    def add_column_recursive_row(self, colname, functionAgg):
        """
        Example:

        ::

            table.add_column_recursive_row("w_%s" % loi,
                            lambda li, v: li[-1] + v ["norm_%s" % loi] \
                            if len(li)> 0 else v ["norm_%s" % loi])
        """
        self.index[colname] = len(self.index)
        values = []
        for row in self.values:
            v = self._interpret_row(row)
            y = functionAgg(values, v)
            row.append(y)
            values.append(y)
        self.header.append(colname)
        return self

    def add_column_vector(self, colname, vector):
        """
        add a column defined by vector(list of values for each row)

        :param colname: column to add
        :param vector: (list) list of values to add to each row
        :return self
        """
        if len(vector) != len(self):
            raise ValueError(  # pragma: no cover
                f"vector and table have different length {len(vector)} != {len(self)}")
        for vec, row in zip(vector, self.values):
            row.append(vec)
        self.index[colname] = len(self.index)
        self.header.append(colname)
        return self

    def add_column_smooth(self, colname, function, position, weights):
        """
        Example:

        ::

            x = 1./3
            table.add_column_smooth("has_A_smooth", lambda v: v["has_A"], [-1,0,1], [x,x,x])
        """
        if len(position) != len(weights):
            raise ValueError(  # pragma: no cover
                "position and weights must have the same length")
        self.index[colname] = len(self.index)
        column = [function(self._interpret_row(row)) for row in self.values]
        tw = sum(weights)
        couple = list(zip(position, weights))
        for p, row in enumerate(self.values):
            sx = 0.
            sw = 0.
            ms = 0
            for i, w in couple:
                pi = p + i
                if 0 <= pi < len(self):
                    sx += column[pi] * w
                    sw += w
                else:
                    ms += 1

            if ms == 0:
                row.append(sx)
            elif sw != 0:
                row.append(sx * tw / sw)
            else:
                row.append(sx)
        self.header.append(colname)
        return self

    def aggregate_column(self, colname, aggregated_function=sum):
        """
        Example:

        ::

            total = table.aggregate_column("d_c", sum)
        """
        def function(v):
            return v[colname]
        return self.aggregate(function, aggregated_function)

    def aggregate(self, function, aggregated_function=sum):
        """
        Example:

        ::

            total = table.aggregate_column(lambda v: v["d_c"], len)
        """
        return aggregated_function([function(self._interpret_row(row)) for row in self.values])

    def where(self, condition_function):
        """
        @see me filter
        """
        return self.filter(condition_function)

    def filter(self, condition_function):
        """
        Example:

        ::

            fil = table.filter(lambda v: v["d_b"] == 2)

        @warning Rows are not copied.
        """
        newv = []
        for row in self.values:
            v = self._interpret_row(row)
            x = condition_function(v)
            if x:
                newv.append(row)
        final = self._private_getclass()(self.header, newv)
        return final

    def groupby_implicit(self, functionKey, functionWeight=None, logging=None):
        """
        use prefix of a column name to know which function to use
        as an aggregated(sum, avg, len, key, none, max, min)
        Example:

        ::

            group = table.groupby_implicit(lambda v: v["name"])
        """
        def identical(col, v):
            return v[col]

        def first(vec):
            return vec[0]

        def avg(vec):
            return TableFormula.ratio(sum(vec), len(vec))

        functions = []
        labels = ["key"]
        functionsAgg = []
        for col in self.header:
            if col.startswith("key"):
                values = self.select(
                    lambda v, col=col: (v[col], functionKey(v)))
                dd = {}
                for v in values:
                    if v[1] not in dd:
                        dd[v[1]] = {}
                    dd[v[1]][v[0]] = 1
                for k in dd:
                    dd[k] = len(dd[k])  # pylint: disable=E4702
                keep = []
                for k, v in dd.items():
                    if v > 1:
                        keep.append((k, v))

                if len(keep) == 0:
                    functions.append(lambda v, col=col: identical(col, v))
                    labels.append(col)
                    functionsAgg.append(first)
                elif logging is not None:
                    end = min(len(keep), 10)
                    mes = ",".join([str(_) for _ in keep[:end]])
                    logging("removing column '{0}' no unique value: {1}: {2}".format(
                        col, len(dd), mes))
            elif col.startswith("sum"):
                functions.append(lambda v, col=col: identical(col, v))
                labels.append(col)
                functionsAgg.append(sum)
            elif col.startswith("len"):
                functions.append(lambda v, col=col: 1)
                labels.append(col)
                functionsAgg.append(len)
            elif col.startswith("min"):
                functions.append(lambda v, col=col: 1)
                labels.append(col)
                functionsAgg.append(min)
            elif col.startswith("max"):
                functions.append(lambda v, col=col: 1)
                labels.append(col)
                functionsAgg.append(max)
            elif col.startswith("avg"):
                functions.append(lambda v, col=col: identical(col, v))
                labels.append(col)
                functionsAgg.append(avg)
            elif col.startswith("none"):
                pass
            else:
                raise RuntimeError("unable to aggregate column " + col)

        return self.groupby(functionKey, functions, labels, functionsAgg, functionWeight)

    def groupby(self, functionKey, functionsValue, columns=None, functionsAgg=None, functionWeight=None):
        """
        Example:

        ::

            group = table.groupby(lambda v: v["name"],
                                    [lambda v: v["d_a"],
                                      lambda v: v["d_b"]],
                                    ["name", "sum_d_a", "sum_d_b"])

        or

        ::

            groupmax = table.groupby(lambda v: v["name"],
                                    [lambda v: v["d_a"],
                                      lambda v: v["d_b"]],
                                    ["name", "max_d_a", "max_d_b"],
                                    [max, max])
        """
        if not isinstance(functionsValue, list):
            functionsValue = [functionsValue]
        if functionsAgg is None:
            functionsAgg = [sum for f in functionsValue]
        if functionWeight is None:
            if columns is not None and len(columns) != len(functionsValue) + 1:
                raise Exception("columns should have %d names not(%d)" % (
                    len(functionsValue) + 1, len(columns)))
        else:
            if columns is not None and len(columns) != len(functionsValue) + 2:
                raise Exception("columns should have %d names not(%d)" % (
                    len(functionsValue) + 2, len(columns)))
        if columns is not None and not isinstance(columns[0], str):
            raise TypeError("expecting type str not %s in columns" %
                            (str(type(columns[0]))))

        hist = {}
        if functionWeight is not None:
            histWeight = {}

            for row in self.values:
                v = self._interpret_row(row)
                key = functionKey(v)
                w = 1. if functionWeight is None else functionWeight(v)

                if key not in hist:
                    histWeight[key] = [w]
                    hist[key] = [[f(v) * w] for f in functionsValue]
                else:
                    histWeight[key].append(w)
                    h = hist[key]
                    for i, f in enumerate(functionsValue):
                        h[i].append(f(v) * w)

            for key in hist:  # pylint: disable=C0206
                h = hist[key]
                w = sum(histWeight[key])
                for i in range(0, len(h)):
                    h[i] = functionsAgg[i](h[i], w)

            f = hist.items if sys.version_info.major >= 3 else hist.items
            histValues = [[k, sum(histWeight[k])] + v for k, v in f()]

            if columns is None:
                columns = ["key", "weight"] + ["val%d" %
                                               i for i, f in enumerate(functionsValue)]
            ret = self._private_getclass()(columns, histValues)
            return ret
        else:
            for row in self.values:
                v = self._interpret_row(row)
                key = functionKey(v)
                if key not in hist:
                    hist[key] = [[f(v)] for f in functionsValue]
                else:
                    h = hist[key]
                    for i, f in enumerate(functionsValue):
                        h[i].append(f(v))

            for key in hist:  # pylint: disable=C0206
                h = hist[key]
                for i in range(0, len(h)):
                    h[i] = functionsAgg[i](h[i])

            f = hist.items if sys.version_info.major >= 3 else hist.items
            histValues = [[k] + v for k, v in f()]

            if columns is None:
                columns = ["key"] + ["val%d" %
                                     i for i, f in enumerate(functionsValue)]
            ret = self._private_getclass()(columns, histValues)
        return ret

    def sort(self, functionValue, reverse=False):
        """
        Example:

        ::

            table.sort(lambda v: v["d_b"] + v["d_c"])
        """
        values = [(functionValue(self._interpret_row(row)), i)
                  for i, row in enumerate(self.values)]
        values.sort(reverse=reverse)
        self.values = [self.values[_[1]] for _ in values]
        return self

    def extract_columns(self, listColumns):
        """
        extract some columns

        @param      listColumns     list of columns to remove or a function
                                    which returns True if the column has to be extracted
                                    based on its name
        @return                     table

        Example:

        ::

            ext = table.extract_columns(["name", "d_a"])
        """
        if isinstance(listColumns, list):
            indexes = [(self.index[col] if isinstance(col, str) else col)
                       for col in listColumns]
            header = listColumns
            values = [[row[i] for i in indexes] for row in self.values]
            return self._private_getclass()(header, values)
        else:
            header = [_ for _ in self.header if listColumns(_)]
            return self.extract_columns(header)

    def remove_columns(self, listColumns):
        """
        remove some columns

        @param      listColumns     list of columns to remove or a function
                                    which returns True if the column has to be removed
                                    based on its name
        @return                     table

        Example:

        ::

            rem = table.remove("d_a")
        """
        if isinstance(listColumns, list):
            cols = [_ for i, _ in enumerate(
                self.header) if _ not in listColumns and i not in listColumns]
            return self.extract_columns(cols)
        if isinstance(listColumns, str):
            cols = [_ for _ in self.header if _ != listColumns]
            return self.extract_columns(cols)
        cols = [_ for _ in self.header if not listColumns(_)]
        return self.extract_columns(cols)

    def innerjoin(self, table, functionKey1, functionKey2, nameKey="key",
                  addSuffixAnyWay=False, prefixToAdd=None, full=False,
                  keepKey=True, putKeyInColumn=None, missingValue=None,
                  uniqueKey=False):
        """
        @param      table           other table to join with
        @param      functionKey1    key for the first table(a function)
        @param      functionKey2    key for the second table(a function) innerjoin .... ON ...
        @param      addSuffixAnyWay add a suffix to every column from the second table even
                                    if names are different(suffix is "+")
        @param      prefixToAdd     prefix to add the the columns of the second table
        @param      full            add all items even if there is no common keys(``FULL OUTER JOIN``),
                                    otherwise keep only common keys
        @param      keepKey         keep the key as a column in the result(column is key), otherwise not
        @param      putKeyInColumn  private parameter: keepKey has to be true and in this case,
                                    put the key in this column(integer)
        @param      missingValue    when there is not key on one side, this default value will be put in place
        @param      uniqueKey       if True, the function assumes there is a bijection between rows
                                    and keys(one row <--> one key) on both tables,
                                    otherwise, it will not.
        @return                     a table

        Example:

        ::

            innerjoin = table.innerjoin(group, lambda v: v["name"],
                                               lambda v: v["name"], "group")
        """
        defaultVal1 = [missingValue for k in self.header]
        defaultVal2 = [missingValue for k in table.header]

        if uniqueKey:
            keys = {}
            for row in self.values:
                v = self._interpret_row(row)
                key = functionKey1(v)
                keys[key] = (row, None)

            for row in table.values:
                v = table._interpret_row(row)
                key = functionKey2(v)
                if key in keys:
                    keys[key] = (keys[key][0], row)
                elif full:
                    keys[key] = (None, row)

            if not full:
                d = []
                for k, v in keys.items():
                    if None in v:
                        d.append(k)
                for _ in d:
                    del keys[_]
            else:
                for k in keys:  # pylint: disable=C0206
                    v = keys[k]
                    if v[0] is None:
                        keys[k] = (defaultVal1, v[1])  # pylint: disable=E4702
                    elif v[1] is None:
                        keys[k] = (v[0], defaultVal2)  # pylint: disable=E4702

            if keepKey:
                columns = [nameKey]
                for x in self.header:
                    while x in columns:
                        x += "~"
                    columns.append(x)

                for x in table.header:
                    if prefixToAdd is not None:
                        x = prefixToAdd + x
                    elif addSuffixAnyWay:
                        x += "+"
                    while x in columns:
                        x += "+"
                    columns.append(x)

                f = keys.items if sys.version_info.major >= 3 else keys.items
                values = [[k] + v[0] + v[1] for k, v in f() if len(v) == 2]
                return self._private_getclass()(columns, values)
            else:
                columns = []
                for x in self.header:
                    while x in columns:
                        x += "~"
                    columns.append(x)

                for x in table.header:
                    if prefixToAdd is not None:
                        x = prefixToAdd + x
                    elif addSuffixAnyWay:
                        x += "+"
                    while x in columns:
                        x += "+"
                    columns.append(x)

                f = keys.items if sys.version_info.major >= 3 else keys.items

                if putKeyInColumn is None:
                    values = [v[0] + v[1] for k, v in f() if len(v) == 2]
                else:
                    values = []
                    for k, v in f():
                        if len(v) == 2:
                            nr = v[0] + v[1]
                            nr[putKeyInColumn] = k
                            values.append(nr)

                return self._private_getclass()(columns, values)
        else:
            keys = {}
            for row in self.values:
                v = self._interpret_row(row)
                key = functionKey1(v)
                if key in keys:
                    keys[key][0].append(row)
                else:
                    keys[key] = ([row], None)

            for row in table.values:
                v = table._interpret_row(row)
                key = functionKey2(v)
                if key in keys:
                    if keys[key][1] is None:
                        keys[key] = (keys[key][0], [row])
                    else:
                        keys[key][1].append(row)
                elif full:
                    keys[key] = (None, [row])

            if not full:
                d = []
                for k, v in keys.items():
                    if None in v:
                        d.append(k)
                for _ in d:
                    del keys[_]
            else:
                for k in keys:  # pylint: disable=C0206
                    v = keys[k]
                    if v[0] is None:
                        keys[k] = ([defaultVal1], v[1]
                                   )  # pylint: disable=E4702
                    elif v[1] is None:
                        keys[k] = (v[0], [defaultVal2]
                                   )  # pylint: disable=E4702

            if keepKey:
                columns = [nameKey]
                for x in self.header:
                    while x in columns:
                        x += "~"
                    columns.append(x)

                for x in table.header:
                    if prefixToAdd is not None:
                        x = prefixToAdd + x
                    elif addSuffixAnyWay:
                        x += "+"
                    while x in columns:
                        x += "+"
                    columns.append(x)

                f = keys.items if sys.version_info.major >= 3 else keys.items

                values = []
                for k, v in f():
                    if len(v) == 2:
                        for ka in v[0]:
                            for kb in v[1]:
                                values.append([k] + ka + kb)
                return self._private_getclass()(columns, values)
            else:
                columns = []
                for x in self.header:
                    while x in columns:
                        x += "~"
                    columns.append(x)

                for x in table.header:
                    if prefixToAdd is not None:
                        x = prefixToAdd + x
                    elif addSuffixAnyWay:
                        x += "+"
                    while x in columns:
                        x += "+"
                    columns.append(x)

                f = keys.items if sys.version_info.major >= 3 else keys.items

                if putKeyInColumn is None:
                    values = [v[0] + v[1] for k, v in f() if len(v) == 2]
                else:
                    values = []
                    for k, v in f():
                        if len(v) == 2:
                            for ka in v[0]:
                                for kb in v[1]:
                                    nr = ka + kb
                                    nr[putKeyInColumn] = k
                                    values.append(nr)

                return self._private_getclass()(columns, values)

    def filter_quantile(self, function, alpha_min=0.025, alpha_max=0.025):
        """
        sort all rows using criteria defined by function and remove
        rows at the extremes

        @param      function        values used to estimate the quantiles
        @param      alpha_min       lower quantile
        @param      alpha_max       higher quantile
        @return                     a table containing all the rows where the criterium
                                    is within the two quantiles

        Example:

        ::

            fil = table.filter_quantile(lambda v: v["d_b"], 0, 0.4)

        @warning Rows are not copied.
        """
        values = []
        for row in self.values:
            v = self._interpret_row(row)
            val = function(v)
            values.append((val, row))
        values.sort()
        lv = len(values)
        i1 = int(lv * alpha_min + 0.5)
        i2 = int(lv * (1 - alpha_max) + 0.5)
        i1 = max(i1, 0)
        i1 = min(i1, lv)
        i2 = max(i1, i2)
        i2 = min(i2, lv)
        if i2 == i1:
            raise RuntimeError("unable to extract quantile, the table is either "
                               "empty or chosen quantile are not correct")
        values = [_[1] for _ in values[i1:i2]]
        return self._private_getclass()(self.header, values)

    def union(self, table):
        """
        @param      table       table
        @return                 table(with the same number of columns)

        concatenates two tables by rows, they must have the same header, rows of both tables are merged into a single matrix
        Example:

        ::

            union = table.union(table2)
        """
        if len(self.header) != len(table.header):
            raise ValueError(  # pragma: no cover
                "tables do not have the same number of columns\ntbl1: %s\ntbl2: %s" % (
                    ",".join(self.header), ",".join(table.header)))
        for a, b in zip(self.header, table.header):
            if a != b:
                raise ValueError(  # pragma: no cover
                    "tables do not have the same column names")
        return self._private_getclass()(self.header, self.values + table.values)

    def concatenate(self, table, addPrefix=""):
        """
        concatenates two tables by columns
        @param      table       table
        @param      addPrefix   add a prefix to each column from table
        @return                 table (with the same number of rows as the longest one)
        """
        maxr = max(len(self), len(table))
        header = self.header + [addPrefix + h for h in table.header]
        values = []
        for i in range(0, maxr):
            r1 = self.values[i] if i < len(self) else [None] * len(self.header)
            r2 = table.values[i] if i < len(
                table) else [None] * len(self.table)
            values.append(r1 + r2)
        return self._private_getclass()(header, values)

    def random(self, n, unique=False):
        """
        select n random row from the table, returns a table

        @param      n       number of desired random rows
        @param      unique  draws unique rows or non unique rows
                           (tirage sans remise ou avec remise)
        @return             a table

        Example:

        ::

            rnd = table.random(10)
        """
        if unique:
            if n > len(self):
                raise ValueError(  # pragma: no cover
                    "number of desired random rows is higher "
                    "than the number of rows in the table")
            index = {}
            while len(index) < n:
                h = random.randint(0, len(self) - 1)
                index[h] = 0
            values = [self.values[h] for h in index]
            return self._private_getclass()(self.header, values)
        else:
            values = []
            for i in range(0, n):
                h = random.randint(0, len(self) - 1)
                values.append(self.values[h])
            return self._private_getclass()(self.header, values)

    def todict(self, functionKey, functionValue, useList=False):
        """
        convert the table as a dictionary { key:value }
        each of them is defined by functions.

        @param      functionKey     defines the key
        @param      functionValue   defines the value
        @param      useList         if there are multiple rows sharing the same key, it should be true,
                                    all values are stored in a list
        @return                     a dictionary { key:row } or { key: [row1, row2, ...] }

        Example:

        ::

            d = table.todict(lambda v: v["name"], lambda v: v["d_b"], True)
        """
        res = {}
        if useList:
            for row in self.values:
                v = self._interpret_row(row)
                key = functionKey(v)
                val = functionValue(v)
                if key in res:
                    res[key].append(val)
                else:
                    res[key] = [val]
        else:
            for row in self.values:
                v = self._interpret_row(row)
                key = functionKey(v)
                val = functionValue(v)
                res[key] = val
        return res

    def reduce_dict(self, functionKey, functionValue, uselist=False):
        """
        @see me todict
        """
        return self.todict(functionKey, functionValue, uselist)

    def select(self, functionRow):
        """
        @param      functionRow   fonction
        @return                   table

        Example:

        ::

            d = table.select(lambda v:(v["name"], v["d_b"]))
            print(list(d))
        """
        for row in self.values:
            v = self._interpret_row(row)
            nr = functionRow(v)
            yield nr

    def modify_all(self, modification_function):
        """
        apply the same modification to every number
        @param      modification_function       modification to apply to every number
        @return                                 new table

        The signature of the function is the following one:

        ::

            def function(value, column_name):
                # ....
                return new_value

        Example:

        ::

            tbl = tbl.modify_all(lambda v,c: {"string":"", "numerical":0}.get(c,None) if v is None else v)
        """
        values = []
        for row in self.values:
            r = []
            for v, h in zip(row, self.header):
                r.append(modification_function(v, h))
            values.append(r)
        return self._private_getclass()(self.header, values)

    def dcast(self, functionKey, functionInstance, full=True):
        """
        @see me multiply_column_by_row_instance
        """
        return self.multiply_column_by_row_instance(functionKey, functionInstance, full)

    def multiply_column_by_row_instance(self, functionKey, functionInstance, full=True):
        """
        @param      functionKey         defines a key(function)
        @param      functionInstance    defines a second key(will be moved to the columns dimension)
        @param      full                introduces missing values for not found combinations
        @return                         a table

        If a column contains a finite set of value, for example,
        we have the temperature for several cities organized like if
        it were a table from a database: city, date, temperatue.
        We would like to get another table where we have:
        date temparature_city1 temperature_city2...

        Then we would type:
        Example:

        ::

            mul = table.multiply_column_by_row_instance(
                                lambda v: v["date"],
                                lambda v: v["city"])

        The input table would be like:

        ::

            city   date
            A      jan
            A      feb
            B      feb

        It returns:

        ::

            KEY	    A|city	A|date	B|city	B|date
            feb	    A	    feb	    B	    feb
            jan	    A	    jan	    None	None
        """
        values = [functionInstance(self._interpret_row(row))
                  for row in self.values]
        distinct = {}
        for v in values:
            distinct[v] = 0
        distinct = [_ for _ in distinct]
        distinct.sort()
        table1 = copy.deepcopy(self)
        table = None
        header = copy.copy(table1.header)
        orig = len(header)
        nameKey = "~KEY~"
        while nameKey in header:
            nameKey += "*"
        nbJoin = 0

        for val in distinct:
            table2 = table1.filter(
                lambda v, val=val: functionInstance(v) == val)
            if table is None:
                table = table2.copy()
            else:
                colkey = table.header[0]
                table = table.innerjoin(table2, functionKey if nbJoin == 0 else (lambda v, c=colkey: v[c]),
                                        functionKey, nameKey=nameKey,
                                        prefixToAdd=str(val) + "|",
                                        full=full, keepKey=nbJoin == 0,
                                        putKeyInColumn=None if nbJoin == 0 else 0,
                                        uniqueKey=True)

                if nbJoin == 0:
                    head = []
                    nb = 0
                    for h in table.header:
                        if not h.endswith("~") and nb < orig:
                            head.append(f"{distinct[0]}|{h}")
                            nb += 1
                        else:
                            head.append(h)
                    header = ["KEY"] + head[1:]
                    table = self._private_getclass()(header, table.values)

                nbJoin += 1

        if nbJoin == 0:
            head = []
            nb = 0
            for h in table.header:
                if not h.endswith("~") and nb < orig:
                    head.append(f"{distinct[0]}|{h}")
                    nb += 1
                else:
                    head.append(h)
            values = []
            for row in self.values:
                v = self._interpret_row(row)
                r = [functionKey(v)] + row
                values.append(r)
            header = ["KEY"] + head
            table = self._private_getclass()(header, values)

        return table

    def create_index(self, functionIndex):
        """
        this method creates an index,
        to get an indexes row, use method get
        Example:

        ::

            table.create_index(lambda v:(v["name"], v["d_a"]))
            row = table.get(('A', 1.1))
            value = table.get(('A', 1.1), 2)
        """
        self.indexspecial = {}
        for row in self.values:
            v = self._interpret_row(row)
            nr = functionIndex(v)
            if nr in self.indexspecial:
                raise KeyError(
                    f"unable to add {str(nr)} because it is already present")
            self.indexspecial[nr] = row
        return self

    def get(self, rowIndex, column=None):
        """
        use the index created by method create_index
        Example:

        ::

            table.create_index(lambda v:(v["name"], v["d_a"]))
            row = table.get(('A', 1.1))
            value = table.get(('A', 1.1), 2)
        """
        if "indexspecial" not in self.__dict__:
            raise Exception("no index was created")
        row = self.indexspecial[rowIndex]
        if column is None:
            return row
        elif isinstance(column, int):
            return row[column]
        else:
            return row[self.index[column]]

    def avg_std(self, functionValue, functionWeight=lambda v: 1):
        """
        returns the average and standard deviation
        """
        avg = 0.
        std = 0.
        n = 0.
        for i, row in enumerate(self.values):
            v = self._interpret_row(row)
            x = float(functionValue(v))
            w = functionWeight(v)
            avg += x * w
            std += x * x * w
            n += w

        if n != 0:
            avg /= n
            std /= n
            std -= avg * avg
            std = math.sqrt(std)
        else:
            avg = 0.
            std = 0.
        return avg, std

    def add_column_cumulative(self, column_index, column_name, functionIndex, functionValue,
                              normalize=False, reverse=False, cumulative=True, functionSort=None):
        """
        also called the Gini function
        Example:

        ::

            table.add_column_cumulative("index_%s" % col, "dist_%s" % col,
                                        lambda v: v["sum_nbclient"], lambda v: v[col],
                                        functionSort = lambda v: v [col] / v["sum_nbclient"],
                                        normalize=True)
        """
        if functionSort is None:
            functionSort = functionValue
        val = []
        for row in self.values:
            v = self._interpret_row(row)
            i = functionIndex(v)
            s = functionSort(v)
            v = functionValue(v)
            val.append((s, i, v))
        val.sort(reverse=reverse)

        if cumulative:
            res = [(0., 0.)]
            for s, i, v in val:
                res.append((i + res[-1][0], v + res[-1][1]))
            del res[0]

            if normalize:
                sumi = res[-1][0]
                sumv = res[-1][1]
                if sumi != 0 and sumv != 0:
                    res = [(_[0] / sumi, _[1] / sumv) for _ in res]
                else:
                    raise ZeroDivisionError(
                        "cannot divide by zero, all indexes or all values are null")
        else:
            res = [(i, v) for s, i, v in val]

            if normalize:
                sumi = sum([_[0] for _ in res])
                sumv = sum([_[1] for _ in res])
                if sumi != 0 and sumv != 0:
                    res = [(_[0] / sumi, _[1] / sumv) for _ in res]
                else:
                    raise ZeroDivisionError(
                        "cannot divide by zero, all indexes or all values are null")

        for row, add in zip(self.values, res):
            row.extend(add)
        self.index[column_index] = len(self.index)
        self.index[column_name] = len(self.index)
        self.header.append(column_index)
        self.header.append(column_name)
        return self

    def transpose(self, labelC=None, labelAsRow=True):
        """
        Computes the transpose.
        @param      labelC          proposes labels for the column,
                                    if None, take "r%d" % i,
                                    if it is a string, the function assumes it is a column name
        @param      labelAsRow      add the label as a row
        @return                     new table
        """
        if labelC is None:
            label = ["r%d" % i for i in range(0, len(self.values))]
            if labelAsRow:
                label = ["rowheader"] + label
            rem = None
        elif isinstance(labelC, str):
            label = list(self.select(lambda v: v[labelC]))
            rem = label
        else:
            rem = None
            label = labelC

        values = []
        for i in range(0, len(self.header)):
            if rem is not None and self.header[i] == labelC:
                continue
            row = [_[i] for _ in self.values]
            if labelAsRow:
                row = [self.header[i]] + row
            values.append(row)
        return self._private_getclass()(label, values)

    def covariance(self):
        """
        Computes the covariance matrix, the first column
        will contains the column names.
        @return         new table
        """
        for i, x in enumerate(self.values[0]):
            if not isinstance(x, float):
                raise TypeError("expecting a float on column %d" % i)
        values = self.np_matrix
        N = values.shape[0]
        sums = numpy.sum(values, axis=0) / N
        for i in range(0, values.shape[1]):
            values[:, i] -= sums[0, i]
        cov = values.transpose() * values
        cov /= N
        head = ["var"] + self.header
        size = cov.shape
        values = [[self.header[
            i]] + [float(cov[i, j]) for j in range(0, size[1])] for i in range(0, size[0])]
        tbl = self._private_getclass()(head, values)
        return tbl

    def correlation_col(self, col1, col2, noCenter=False):
        """
        Computes the correlation between two columns.
        @param      col1        column 1
        @param      col2        column 2
        @param      noCenter    does the computation without removing the average
        @return                 float(covariance)
        """
        values = [[self._interpret_row(row)[col1], self._interpret_row(row)[
            col2]] for row in self.values]
        if len(values) <= 1:
            raise ValueError(  # pragma: no cover
                f"expecting more than one observation, not {len(values)}")
        mx = 0.
        my = 0.
        vx = 0.
        vy = 0.
        co = 0.
        nb = 0.
        for a, b in values:
            nb += 1
            mx += a
            my += b
            vx += a ** 2
            vy += b ** 2
            co += a * b
        mx /= nb
        my /= nb
        vx /= nb
        vy /= nb
        co /= nb
        if not noCenter:
            vx -= mx ** 2
            vy -= my ** 2
            co -= mx * my
        vx = vx ** 0.5
        vy = vy ** 0.5
        v = vx * vy
        if v != 0:
            co /= v
        return co

    def covariance_col(self, col1, col2, noCenter=False):
        """
        Computes the correlation between two columns.
        @param      col1        column 1
        @param      col2        column 2
        @param      noCenter    does the computation without removing the average
        @return                 float(covariance)
        """
        values = [[self._interpret_row(row)[col1],
                   self._interpret_row(row)[col2]] for row in self.values]

        if len(values) <= 1:
            raise ValueError(  # pragma: no cover
                f"expecting more than one observation, not {len(values)}")

        mx = 0.
        my = 0.
        co = 0.
        nb = 0.
        for a, b in values:
            nb += 1
            mx += a
            my += b
            co += a * b
        mx /= nb
        my /= nb
        co /= nb
        if not noCenter:
            co -= mx * my
        return co

    def correlation_row(self, row1, row2, noCenter=False):
        """
        computes the correlation between two columns
        @param      row1        row 1(integer)
        @param      row2        row 2(integer)
        @param      noCenter    does the computation without removing the average
        @return                 float(covariance)
        """
        values = [[a, b] for a, b in zip(self.values[row1], self.values[row2])]
        if len(values) <= 1:
            raise ValueError(  # pragma: no cover
                f"expecting more than one observation, not {len(values)}")
        mx = 0.
        my = 0.
        vx = 0.
        vy = 0.
        co = 0.
        nb = 0.
        for a, b in values:
            nb += 1
            mx += a
            my += b
            vx += a ** 2
            vy += b ** 2
            co += a * b
        mx /= nb
        my /= nb
        vx /= nb
        vy /= nb
        co /= nb
        if not noCenter:
            vx -= mx ** 2
            vy -= my ** 2
            co -= mx * my
        vx = vx ** 0.5
        vy = vy ** 0.5
        v = vx * vy
        if v != 0:
            co /= v
        return co

    def covariance_row(self, row1, row2, noCenter=False):
        """
        computes the correlation between two columns
        @param      row1        row 1(integer)
        @param      row2        row 2(integer)
        @param      noCenter    does the computation without removing the average
        @return                 float(covariance)
        """
        values = [[a, b] for a, b in zip(self.values[row1], self.values[row2])]
        if len(values) <= 1:
            raise ValueError(  # pragma: no cover
                f"expecting more than one observation, not {len(values)}")
        mx = 0.
        my = 0.
        co = 0.
        nb = 0.
        for a, b in values:
            nb += 1
            mx += a
            my += b
            co += a * b
        mx /= nb
        my /= nb
        co /= nb
        if not noCenter:
            co -= mx * my
        return co

    def correlation(self, useBootstrap=False, collapseFormat=True, nbdraws=-1, alpha=0.05,
                    functionKeepValue=lambda val, low, high: f"{val:f}|{low:f},{high:f}"):
        """
        Computes the correlation matrix, the first column
        will contains the column names.

        @param      useBootstrap            if True, use a bootstrap method to estimate the correlation
        @param      collapseFormat          if True and useBootstrap is True, produces a format
                                            ``average|lower bound|higher bound(at a definite confidence level)``
        @param      nbdraws                 number of draws(if -1, then it will be equal to the number of observations)
        @param      alpha                   confidence level
        @param      functionKeepValue       if collapseFormat is True, this function is used to collapse val,low,high in a single string
        @return                             new table
        """
        if useBootstrap:
            head = ["var"] + self.header
            values = [[i] + [0. for r in self.header] for i in self.header]
            for i in range(len(self.header)):
                values[i][0] = self.header[i]
                for j in range(len(self.header)):
                    vs = [[row[i], row[j]] for row in self.values]
                    bo = TableFormula.bootstrap(vs, function=TableFormula.correlation_bicolumn,
                                                nbdraws=nbdraws, alpha=alpha)
                    if collapseFormat:
                        st = functionKeepValue(bo[0], bo[2], bo[3])
                        values[i][j + 1] = st
                    else:
                        raise NotImplementedError(  # pragma: no cover
                            "collapseFormat False is not implemented yet")
            tbl = self._private_getclass()(head, values)
            return tbl
        else:
            for i, x in enumerate(self.values[0]):
                if not isinstance(x, float):
                    raise TypeError(  # pragma: no cover
                        "expecting a float on column %d" % i)

            values = self.np_matrix
            N = values.shape[0]
            sums = [sum(values[:, i]) / N for i in range(0, values.shape[1])]

            for i in range(0, values.shape[1]):
                values[:, i] -= sums[i]

            cov = values.transpose() * values
            cov /= N
            diag = [cov[i, i] ** 0.5 for i in range(cov.shape[0])]
            for i in range(cov.shape[0]):
                if diag[i] > 0:
                    cov[i, :] /= diag[i]
                    cov[:, i] /= diag[i]

            head = ["var"] + self.header
            size = cov.shape
            values = [[self.header[
                i]] + [float(cov[i, j]) for j in range(0, size[1])] for i in range(0, size[0])]
            tbl = self._private_getclass()(head, values)
            return tbl

    def values_to_float(self, only_if_possible=False, subset_columns=None):
        """
        converts all values into float
        @param    only_if_possible      if True, converts all possible values and catches exception,
                                        if False, converts everything, raises an exception when not possible
        @param    subset_columns        if None, takes all of them, otherwise, try to convert
                                        only for the listed columns
        @return                         table
        """
        tbl = self.copy()
        if subset_columns is not None:
            subset = {i: True for i, v in enumerate(
                self.header) if v in subset_columns}
        if only_if_possible:
            for row in tbl.values:
                for i in range(0, len(row)):
                    if subset_columns is None or i in subset:
                        try:
                            v = float(row[i])
                            row[i] = v
                        except (ValueError, TypeError):
                            continue
        else:
            for row in tbl.values:
                for i in range(0, len(row)):
                    if subset_columns is None or i in subset:
                        row[i] = float(row[i])
        return tbl

    def values_to_str(self, subset_columns=None, format=None):
        """
        converts all values into str
        @param    subset_columns        if None, takes all of them, otherwise, try to convert
                                        only for the listed columns
        @param    format                format for the conversion, by None by default but it could be for exemple %1.2f.
        @return                         table
        """
        tbl = self.copy()
        if subset_columns is not None:
            subset = {i: True for i, v in enumerate(
                self.header) if v in subset_columns}

        if format is None:
            for row in tbl.values:
                for i in range(0, len(row)):
                    if subset_columns is None or i in subset:
                        row[i] = str(row[i])
        else:
            for row in tbl.values:
                for i in range(0, len(row)):
                    if (subset_columns is None or i in subset) and isinstance(row[i], float):
                        row[i] = format % row[i]
        return tbl

    def values_to_date(self, format=None, only_if_possible=False, subset_columns=None):
        """
        converts all values into dates
        @param    only_if_possible      if True, converts all possible values and catches exception,
                                        if False, converts everything, raises an exception when not possible
        @param    format                date format see fn str_to_datetime
        @param    subset_columns        if None, takes all of them, otherwise, try to convert
                                        only for the listed columns
        @return                         table
        """
        tbl = self.copy()
        if subset_columns is not None:
            subset = {i: True for i, v in enumerate(
                self.header) if v in subset_columns}
        if only_if_possible:
            if subset_columns is not None:
                subset = {i: True for i, v in enumerate(
                    self.header) if v in subset_columns}

            for row in tbl.values:
                for i in range(0, len(row)):
                    if subset_columns is None or i in subset:
                        try:
                            v = str2datetime(row[i], format)
                            row[i] = v
                        except (ValueError, TypeError):
                            continue
        else:
            for row in tbl.values:
                for i in range(0, len(row)):
                    if subset_columns is None or i in subset:
                        row[i] = float(row[i])
        return tbl

    def histogram(self, functionValue, nbDiv=100, secondColumnIsWeight=False,
                  normalize=True, removeExtreme=0.05):
        """
        computes an histograms on one vector
        @param      functionValue           function which produces the value to histogram
        @param      nbDiv                   number of divisions for this histograms(boundaries are min and max)
        @param      secondColumnIsWeight    if True, the second column is the weight
        @param      normalize               if True, normalize by the sum of weights
        @param      removeExtreme           remove extreme values at both sides(0.05 means 0.025 on each side)
        @return                             table with two columns
        """
        values = list([functionValue(self._interpret_row(row))  # pylint: disable=R1728
                       for row in self.values])
        if removeExtreme is not None and removeExtreme > 0:
            values.sort()
            al = int(len(values) * removeExtreme / 2)
            if al == 0:
                raise Exception(  # pragma: no cover
                    "removeExtreme has no impact(%d,%f)" % (
                        len(values), len(values) * removeExtreme / 2))
            if al * 2 < len(values):
                values = values[al:len(values) - al]

        mi = min(values)
        ma = max(values)

        if isinstance(values[0], (tuple, list)):
            W = 0.
            div = (ma[0] - mi[0]) / nbDiv
            hist = [[mi[0] + n * div, 0.] for n in range(0, nbDiv + 1)]
            for v in values:
                x = int((v[0] - mi[0]) // div)
                hist[x][1] += v[1]
                W += v[1]
            mi = mi[0]
        else:
            W = len(values)
            div = (ma - mi) / nbDiv
            hist = [[mi + n * div, 0.] for n in range(0, nbDiv + 1)]
            for v in values:
                x = int((v - mi) // div)
                if 0 <= x < len(hist):
                    hist[x][1] += 1.

        if normalize and W > 0:
            for i in range(len(hist)):
                hist[i][1] /= W

        values = [[mi + n * div, hist[n]] for n in range(len(hist))]
        tbl = self._private_getclass()(["x", "hist(x)"], hist)
        return tbl

    def histograms(self, columnsSet, nbDiv=100, secondColumnIsWeight=False,
                   normalize=True, removeExtreme=0.05, histxName="histKey"):
        """
        computes a common histograms on all columns
        @param      columnsSet              set of columns
        @param      nbDiv                   number of divisions for this histograms(boundaries are min and max)
        @param      secondColumnIsWeight    if True, the second column is the weight
        @param      normalize               if True, normalize by the sum of weights
        @param      removeExtreme           remove extreme values at both sides(0.05 means 0.025 on each side)
        @param      histxName               column name given to the x axis shared by every histogram
        @return                             table with two columns

        @warning The function skips any NaN of Inf value.
        """
        values = []
        for row in self.values:
            temp = self._interpret_row(row)
            for t in columnsSet:
                values.append(temp[t])

        if removeExtreme is not None and removeExtreme > 0:
            values.sort()
            al = int(len(values) * removeExtreme / 2)
            if al == 0:
                raise Exception(  # pragma: no cover
                    "removeExtreme has no impact(%d,%f)" % (
                        len(values), len(values) * removeExtreme / 2))
            if al * 2 < len(values):
                values = values[al:len(values) - al]

        mi = min(values)
        ma = max(values)
        W = len(values)
        div = (ma - mi) / nbDiv
        if div == 0:
            raise RuntimeError(  # pragma: no cover
                f"unable to continue since div is null: min,max = {mi:f},{ma:f}")
        hist = [[mi + n * div, 0.] for n in range(0, nbDiv + 1)]
        value = {i: {histxName: hist[i][0]} for i in range(len(hist))}
        su = {}
        for row in self.values:
            for _ in columnsSet:
                temp = self._interpret_row(row)
                if math.isnan(temp[_]) or math.isinf(temp[_]):
                    continue
                x = int((temp[_] - mi) // div)
                if x not in value:
                    # it means extremes were removed
                    continue
                    #raise Exception("value %d,%f is not allowed min,max = [%f,%f]" %(x, temp[_], mi, ma))
                value[x][_] = value[x].get(_, 0.) + 1.
                su[_] = su.get(_, 0.) + 1.

        if normalize and W > 0:
            for v in value.values():
                for _ in v:
                    if _ != histxName:
                        v[_] /= su[_]

        tbl = self._private_getclass()("__byrow__", value)
        return tbl

    def union_columns(self, columnsSet):
        """
        computes the union of all values from all columns present in columnSet
        @param      columnsSet      set of columns
        @return                     table
        """
        values = []
        for row in self.values:
            temp = self._interpret_row(row)
            for t in columnsSet:
                values.append(temp[t])
        tbl = self._private_getclass()(["x"], [[x] for x in values])
        return tbl

    def mu_sigma(self, functionValues, removeExtreme=None):
        """
        computes the average and the standard deviation a vector of values
        @param      functionValues      function produces the vector of values
        @param      removeExtreme       remove extreme values at both sides(0.05 means 0.025 on each side)
        @return                        (average, standard deviation)
        """
        if removeExtreme is not None and removeExtreme > 0:
            values = []
            for row in self.values:
                row = self._interpret_row(row)
                val = functionValues(row)
                values.append(val)
            values.sort()
            al = int(len(values) * removeExtreme / 2)
            if al == 0:
                raise Exception("removeExtreme has no impact(%d,%f)" % (
                    len(values), len(values) * removeExtreme / 2))
            if al * 2 < len(values):
                values = values[al:len(values) - al]
            tbl = TableFormula(["x"], [[_] for _ in values])
            return tbl.mu_sigma(lambda v: v["x"], 0)
        else:
            mu = 0.
            si = 0.
            nb = 0.
            for row in self.values:
                row = self._interpret_row(row)
                val = functionValues(row)
                mu += val
                si += val ** 2
                nb += 1.
            mu /= nb
            si /= nb
            si -= mu ** 2
            return mu, si ** 0.5

    def mu_sigma_each_column(self, columnsSet=None, removeExtreme=None):
        """
        returns a table with the average and the standard deviation for each columns
        @param      removeExtreme       remove extreme values at both sides(0.05 means 0.025 on each side)
        @param      columnsSet          set of column to deal with
        @return                         table with two rows: average and standard deviation
        """
        values = [[], []]
        if columnsSet is None:
            columnsSet = self.header
        for col in columnsSet:
            mu, sigma = self.mu_sigma(
                (lambda v, col=col: v[col]), removeExtreme)
            values[0].append(mu)
            values[1].append(sigma)
        tbl = self._private_getclass()(columnsSet, values)
        return tbl

    @property
    def np_matrix(self):
        """
        returns the values as a numpy matrix
        @return         numpy matrix
        """
        return numpy.matrix(self.values)

    @property
    def np_array(self):
        """
        returns the values as a numpy array
        @return         numpy array
        """
        return numpy.array(self.values)

    @property
    def dataframe(self):
        """
        creates a pandas dataframe
        @return     pandas.dataframe
        """
        return pandas.DataFrame(self.values, columns=self.header)

    @property
    def json(self):
        """
        returns a json format
        @return         string
        """
        rows = [row for row in self]
        return json.dumps(rows)

    def center_reduce(self, columnsSet=None, op=None, removeExtreme=None, mu_sigma=None):
        """
        center and reduce a set of columns(or all if columnsSet is None)
        @param      removeExtreme       remove extreme values at both sides(0.05 means 0.025 on each side)
        @param      columnsSet          set of column to deal with
        @param      op                  if can be:
                                        - None:   substract mean and normalize,
                                        - "mean": substract mean only,
                                        - "norm": normalize only
        @param      mu_sigma            matrix with two rows(one for mean, second for sigma), if None,
                                        if computes that from the matrix self, columns must have the same order
                                        that columnSet
        @return                         the same table(with only the considered columns)
        """
        if op not in [None, "mean", "norm"]:
            raise ValueError(  # pragma: no cover
                'expecting a value in [None, "mean", "norm"] for op')
        if columnsSet is None:
            columnsSet = self.header
        mus = self.mu_sigma_each_column(
            columnsSet, removeExtreme) if mu_sigma is None else mu_sigma
        tbl = self.extract_columns(columnsSet)
        n = len(self.header)
        for row in tbl.values:
            if op is None or op == "mean":
                for i in range(n):
                    row[i] -= mus.values[0][i]
            if op is None or op == "norm":
                for i in range(n):
                    row[i] /= mus.values[1][i]
        return tbl

    @staticmethod
    def save_multiple_as_excel(filename, list_table, font="Calibri", close=True, encoding=None):
        """
        saves multiple table in one Excel file

        @param      filename        filename(can be None)
        @param      list_table      list of 2uple("name", tbl)
        @param      font            font name
        @param      close           if True, close the file, otherwise, the user will have to
        @param      encoding        encoding
        @return                     object Workbook
        """
        ext = os.path.splitext(
            filename)[-1].lower() if filename is not None else None
        if ext is not None and ext == ".xls":
            font0 = EXf.Font()
            font0.name = font
            font0.bold = True
            style0 = EXs.XFStyle()
            style0.font = font0

            wb = EXw.Workbook(
                encoding=encoding) if encoding is not None else EXw.Workbook()
            for sheet_name, self in list_table:
                ws0 = wb.add_sheet(sheet_name)

                for i, l in enumerate(self.header):
                    ws0.write(0, i, l, style0)

                fnt = EXf.Font()
                fnt.name = font
                style = EXs.XFStyle()
                style.font = fnt

                for irow, row in enumerate(self.values):
                    for icol, val in enumerate(row):
                        if isinstance(val, (int, float)):
                            st = val
                        elif isinstance(val, str):
                            if encoding is not None:
                                st = val.encode(encoding).decode(encoding)
                            else:
                                st = val
                        elif val is not None:
                            st = str(val)
                        else:
                            continue
                        ws0.write(irow + 1, icol, st, style)

            wb.save(filename)
            return wb

        elif ext is None or ext == ".xlsx":
            wb = EXxw.Workbook(
                filename) if filename is not None else EXxw.Workbook()
            for sheet_name, self in list_table:
                ws0 = wb.add_worksheet(sheet_name)

                style0 = wb.add_format({'bold': True})
                style0.set_font_name(font)

                for i, l in enumerate(self.header):
                    ws0.write(0, i, l, style0)

                style = wb.add_format()
                style.set_font_name(font)

                for irow, row in enumerate(self.values):
                    for icol, val in enumerate(row):
                        if isinstance(val, (int, float)):
                            st = val
                        elif isinstance(val, str):
                            if encoding is not None:
                                st = val.encode(encoding).decode(encoding)
                            else:
                                st = val
                        elif val is not None:
                            st = str(val)
                        else:
                            continue
                        ws0.write(irow + 1, icol, st, style)

            if filename is not None and close:
                wb.close()
            return wb
        else:
            raise NameError(
                "extension should be .xls or .xlsx for file " + filename)

    def save_as_excel(self, filename, font="Calibri", sheet_name="sheet0",
                      close=True, encoding=None):
        """
        saves the table as a new Excel file, you can use ``.xls`` or ``.xlsx``
        if filename is None, the function returns an object(xslx) and does not save it.

        @param      filename        Excel filename
        @param      sheet_name      name of the sheet to add
        @param      font            font name
        @param      close           if True, close the file, otherwise, the user will have to
        @param      encoding        encoding
        @return                     object Workbook
        """
        return TableFormula.save_multiple_as_excel(filename, [(sheet_name, self)],
                                                   font=font, close=close, encoding=encoding)

    def schema_database(self, add_id=True):
        """
        returns the schema for a database which would contains this database

        @param      add_id      if True, adds an index "PRIMARYKEY"
        @return                 dictionary { index_column:(name, type) }
        """
        schema = {i: (l, str) for i, l in enumerate(self.header)}
        if add_id is not None:
            schema[-1] = (add_id, int, "PRIMARYKEY", "AUTOINCREMENT")

        if len(self) > 0:
            # we use the first row to determine type
            for i, v in enumerate(self.values[0]):
                if not isinstance(v, str):
                    schema[i] = (schema[i][0], type(v))
        return schema

    def fill_sql_table(self, filename_or_database, tablename, add_id="idr"):
        """
        returns a Database object, creates the database if it does not exists,
        same for the table

        @param      filename_or_database    filename or Database object,
                                            in that second case, we assume method connect
                                            was called before
        @param      tablename               table name
        @param      add_id                  if is not None, then the function adds an id, it first takes the
                                            max(id) and goes on incrementing it;
        @return                             Database object(new or the one from the parameters),
                                            in both case, the database is not disconnected
        """
        schema = self.schema_database(add_id)

        if isinstance(filename_or_database, str):
            fLOG("fill_sql_table: creating database ", filename_or_database)
            db = Database(filename_or_database, LOG=fLOG)
            db.connect()

            fLOG("fill_sql_table ", schema)
            if tablename not in db.get_table_list():
                fLOG("creationg of table ", schema)
                cursor = db.create_table(tablename, schema)
                db.append_values(self.values, tablename, schema, cursor=cursor)
            else:
                db.append_values(self.values, tablename, schema)
        else:
            db = filename_or_database
            db.append_values(self.values, tablename, schema)

        return db
