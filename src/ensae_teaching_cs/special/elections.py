# -*- coding: utf-8 -*-
"""
@file
@brief Contains a class to process elections results (France)
"""
import random
import numpy
import pandas


class ElectionResults:
    """
    Processes data coming from
    `data.gouv.fr <http://www.data.gouv.fr/content/search?SortBy=Pertinence&SortOrder=0&SearchText=%C3%A9lections+2012>`_.

    The class uses `pandas <http://pandas.pydata.org/>`_ to process the data.
    See `Elections françaises <http://www.xavierdupre.fr/blog/2013-12-06_nojs.html>`_.
    See `Optimisation sous contraintes appliquée au calcul du report des voix <http://www.xavierdupre.fr/blog/2013-12-07_nojs.html>`_.
    """

    def __init__(self, file, year=None, level="Départements"):
        """
        Loads the data downloaded from
        `data.gouv.fr <http://www.data.gouv.fr/content/search?SortBy=Pertinence&SortOrder=0&SearchText=%C3%A9lections+2012>`_.

        @param      file        xls file
        @param      year        year (optional)
        @param      level       ``Départements`` or ``Cantons``
        """
        self.year = year
        self.level = level.lower().replace("s", "")
        if isinstance(file, list):
            self.tours = file
        else:
            self.tours = [pandas.read_excel(file, sheet_name=f"{level} T1", engine='openpyxl'),
                          pandas.read_excel(file, sheet_name=f"{level} T2", engine='openpyxl')]
            for i, t in enumerate(self.tours):
                if len(t) == 0:
                    raise Exception("no data for tour %d" % (i + 1))
            self.tours = [self.process_tour(_) for _ in self.tours]
            for i, t in enumerate(self.tours):
                if len(t) == 0:
                    raise Exception("no data for tour %d" % i)
            try:
                self.tours = [
                    _.sort_values(f"Libellé du {self.level}", inplace=False) for _ in self.tours]
            except Exception as e:
                message = "unable to sort, shape={1} columns={0}".format(
                    ",".join(self.tours[0].columns), self.tours[0].shape)
                raise Exception(message) from e

    def get_candidates_votes(self, round):
        """
        Returns the numbers of voters for each candidate.

        @param      round       0 or 1
        @return                 dictionary
        """
        cols0 = [_ for _ in self.tours[
            round].columns if _ not in self.LevelCol]
        sums = [self.tours[round][c].sum() for c in cols0]
        return {c: s for c, s in zip(cols0, sums)}

    def correct(self, method=None):
        """
        Corrects the second round in a way there is the same number of voters.

        @param      method      some preprocess before going on (see below)

        About ``method``:

        - *'N'* --> correct the number of voters for each regions
        - *'cand'* --> gives the same weights to every candidates
        """
        if method == "N":
            if len(self.T0) != len(self.T1):
                raise Exception(
                    "unable to proceed because of different numbers of regions")
            cols0 = [_ for _ in self.tours[
                0].columns if _ not in self.LevelCol]
            cols1 = [_ for _ in self.tours[
                1].columns if _ not in self.LevelCol]
            for i in range(len(self.T0)):
                s1 = self.T0.loc[i, cols0].sum()
                s2 = self.T1.loc[i, cols1].sum()
                coef = 1.0 * s1 / s2
                for c in cols1:
                    self.T1.loc[i, c] *= coef
        elif method == "cand":
            cols0 = [_ for _ in self.tours[
                0].columns if _ not in self.LevelCol]
            sums = [self.T0[c].sum() for c in cols0]
            total = sum(sums)
            for c, s in zip(cols0, sums):
                self.T0[c] = self.T0[c] * total / s
            self.correct("N")
        else:
            raise NotImplementedError("unknown method: " + method)

    def __str__(self):
        """usual"""
        message = "Year: {0} T1: {1} T2: {2}".format(
            self.Year, len(self.tours[0]), len(self.tours[1]))
        return message

    def GetNbCandidates(self, round):
        """
        Returns the number of candidates.
        @param      round       round (0 or 1)
        @return                 number of candidates
        """
        return len(self.tours[round].columns) - 4

    @property
    def Year(self):
        """
        Returns the year.
        """
        return self.year

    @property
    def Level(self):
        """
        Returns the level (``département`` or ``canton``).
        """
        return self.level

    @property
    def LevelCol(self):
        """
        Returns the column associated to the level (their name depends on the level).
        """
        return [f"Code du {self.level}", f"Libellé du {self.level}"]

    @property
    def T0(self):
        """
        Returns the dataframe for the first round.
        """
        return self.tours[0]

    @property
    def T1(self):
        """
        Returns the dataframe for the second round.
        """
        return self.tours[1]

    def process_tour(self, tour):
        """
        Keeps the interesting columns, move candidates name as column name.

        @param      tour    dataframe
        @return             dataframe
        """
        keep = [isinstance(_, (float, int, numpy.int64, numpy.float64)) and ~numpy.isnan(_)
                for _ in tour["Abstentions"]]
        tour = tour.loc[keep, :]
        names = [_ for _ in tour.columns if _.startswith("Nom")]
        res = []
        for n in names:
            c = list(tour[n])
            res.extend(c)
        unique = set(res)
        unique = list(unique)

        try:
            unique.sort()
        except TypeError as e:
            raise Exception("unable to sort " + str(unique) +
                            f"\ncolumns:{','.join(tour.columns)}") from e

        columns0 = [f"Code du {self.level}", f"Libellé du {self.level}", ]
        columns1 = ["Abstentions", "Blancs et nuls", ]

        def proc(row):
            res = {}
            for i, v in enumerate(row):
                k = tour.columns[i]
                if k in columns0:
                    res[k] = row[i]
                elif k in columns1:
                    res[k] = row[i]
                elif k.startswith("Nom"):
                    res[v] = row[i + 2]
                badkeys = [_ for _ in res if len(_) == 0]
                if len(badkeys) > 0:
                    return None
            return res
        rows = list(map(lambda r: proc(r), tour.values))
        rows = [_ for _ in rows if _ is not None]
        return pandas.DataFrame(rows)

    def vote_transfer(self):
        """
        Computes the votes between the two rounds using
        contrainsts optimization, the optimization
        requires :epkg:`cvxopt`.

        See `Optimisation sous contraintes appliquée au calcul du report des voix <http://www.xavierdupre.fr/blog/2013-12-07_nojs.html>`_.

        @return                     results (as a DataFrame)
        """
        cols0 = [_ for _ in self.tours[0] if _ not in self.LevelCol]
        X = self.tours[0][cols0].values
        X = numpy.matrix(X)

        cols1 = [_ for _ in self.tours[1] if _ not in self.LevelCol]
        Y = self.tours[1][cols1].values
        Y = numpy.matrix(Y)

        nbC = Y.shape[1]
        lin, col = X.shape

        # construction de Q
        def _zeros(lin, col):
            return [[0.0 for i in range(0, col)] for j in range(0, lin)]
        bigX = [numpy.matrix(_zeros(lin, col * nbC)) for i in range(0, nbC)]

        for i in range(0, nbC):
            bigX[i][:, col * i:col * (i + 1)] = X[:, :]

        pX = []
        for m in bigX:
            pX.append(m.transpose() * m)

        Q = None
        for m in pX:
            if Q is None:
                Q = +m
            else:
                Q += m * 2

        # construction de p
        p = None
        for i in range(0, nbC):
            tr = bigX[i].transpose()
            y2 = Y[:, i] * (-2)
            t = tr * y2
            if p is None:
                p = t
            else:
                p += t

        # construction de G, h
        def _identite(n):
            return [[0.0 if i != j else 1.0 for i in range(0, n)] for j in range(0, n)]
        h = numpy.matrix(_zeros(col * nbC, 1))
        G = - numpy.matrix(_identite(col * nbC))

        # construction de C,b
        b = numpy.matrix(_zeros(col, 1))
        b[:, :] = 1.0
        C = numpy.matrix(_zeros(col, col * nbC))
        for i in range(0, col):
            for ni in range(0, nbC):
                C[i, i + col * ni] = 1.0

        # résolutation
        from cvxopt import solvers
        from cvxopt import matrix

        Q = matrix(Q)
        p = matrix(p)
        G = matrix(G)
        h = matrix(h)
        C = matrix(C)
        b = matrix(b)

        old = solvers.options.get("show_progress", True)
        solvers.options["show_progress"] = False
        sol = solvers.qp(Q, p, G, h, C, b)
        solvers.options["show_progress"] = old
        coef = sol['x']

        res = numpy.matrix(_zeros(col, nbC))
        for i in range(0, nbC):
            res[:, i] = coef[col * i:col * (i + 1)]

        rown = [_ for _ in self.tours[0].columns if _ not in self.LevelCol]
        coln = [_ for _ in self.tours[1].columns if _ not in self.LevelCol]
        return pandas.DataFrame(data=res, index=rown, columns=coln)

    def resample(self, method="uniform"):
        """
        Builds a new sample: it produces a results with the same number of
        rows, but each rows is randomly drawn from the current data.
        This is needed for the bootstrap procedures.

        @param      method      ``weight`` or ``uniform``
        @return                 two matrices
        """
        if len(self.T0) != len(self.T1):
            raise Exception(
                "unable to proceeed, we need to draw the same regions, assuming both matrices are sorted in the same order")

        def resample_matrix(mat, h):
            return mat.loc[h, :]
        if method == "uniform":
            n = len(self.T0)
            h = [random.randint(0, n - 1) for i in range(0, n)]
        else:
            def find_index(x):
                s = 0
                for i, _ in enumerate(self.WeightsNorm):
                    s += _
                    if x < s:
                        return i
                return len(self.WeightsNorm) - 1
            n = len(self.T0)
            h = [find_index(random.random()) for i in range(0, n)]

        return ElectionResults([resample_matrix(self.T0, h),
                                resample_matrix(self.T1, h), ],
                               year=self.year, level=self.level)

    def get_people(self, round=0):
        """
        Returns the number of people per regions.
        @param          round       first (0) or second (1) round
        @return                     series
        """
        return self.tours[round].apply(lambda row: sum([row[_] for _ in self.tours[round].columns if _ not in self.LevelCol]), axis=1)

    @property
    def WeightsNorm(self):
        """
        Returns the proportion of voters for each regions.
        """
        if "weightsnorm" not in self.__dict__:
            self.weightsnorm = list(self.get_people())
            s = sum(self.weightsnorm)
            self.weightsnorm = [_ * 1.0 / s for _ in self.weightsnorm]
        return self.weightsnorm

    @staticmethod
    def min_max_mean_std(series, alpha=0.05):
        """
        returns the mean standard deviation, bounds of the confidence interval

        @param      series      list of numbers
        @param      alpha       confidence level
        @return                 mean, std, low, high
        """
        series = list(sorted(series))
        a = int(len(series) * alpha / 2)
        low, high = series[a], series[-a - 1]
        mean = sum(series) / len(series)
        std = sum([(x - mean) ** 2 for x in series]) / len(series)
        return mean, std ** 0.5, low, high

    def bootstrap(self, iter=1000, method="vote_transfer", alpha=0.05, fLOG=None, **params):
        """
        Uses the bootstrap method to compute confidence intervals
        see `bootstrap <http://fr.wikipedia.org/wiki/Bootstrap_%28statistiques%29>`_.

        @param      iter        number of iteration
        @param      method      method to bootstrap
        @param      alpha       confidence level
        @param      fLOG        logging function or none
        @param      params      parameters to give to ``method``
        @return                 four matrices, averaged results, sigma, lower bound, higher bound
        """
        if fLOG is None:
            fLOG = lambda *x: ""
        fLOG("sampling", iter)
        samples = [self.resample() for i in range(iter)]
        if method == "vote_transfer":
            matrices = [_.vote_transfer(**params) for _ in samples]
        else:
            raise NotImplementedError()

        mean = matrices[0].copy()
        std = matrices[0].copy()
        low = matrices[0].copy()
        high = matrices[0].copy()

        shape = mean.shape
        fLOG("level for each coefficient", shape)
        for i in range(0, shape[0]):
            for j in range(0, shape[1]):
                series = [m.iloc[i, j] for m in matrices]
                xmean, xstd, xlow, xhigh = ElectionResults.min_max_mean_std(
                    series, alpha=alpha)
                mean.iloc[i, j] = xmean
                std.iloc[i, j] = xstd
                low.iloc[i, j] = xlow
                high.iloc[i, j] = xhigh
        return mean, std, low, high

    @staticmethod
    def combine_into_string(matrices, float_format=str, agg_format=str):
        """
        Combines two matrices into one before displaying it.

        @param      matrices            list of matrices (same dimension)
        @param      float_format        to format each float of all matrices
        @param      agg_format          to build the aggregated string
        @return                         matrixes (dataframe)

        Example:

        ::

            def pour(x) :
                if x < 0.01 : return ""
                else : return "%2.0f" % (x*100) + "%"

            boot = el.bootstrap(iter=10)
            comb = el.combine_string( [boot[2],boot[3]], pour, lambda v : "%s-%s" % tuple(v))
        """
        shape = matrices[0].shape
        res = [["" for i in range(shape[1])] for j in range(shape[0])]
        for i in range(0, shape[0]):
            for j in range(0, shape[1]):
                series = [float_format(m.iloc[i, j]) for m in matrices]
                res[i][j] = agg_format(series)
        return pandas.DataFrame(data=res, columns=list(matrices[0].columns), index=list(matrices[0].index))
