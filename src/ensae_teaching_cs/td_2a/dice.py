# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes de
`Google Jam <https://code.google.com/codejam/>`_.

"""
from collections import OrderedDict
from pyquickhelper.loghelper import noLOG


class DiceStraight:
    """
    Inspired by `Problem A. Dice Straight <https://code.google.com/codejam/contest/6314486/dashboard>`_.

    On dispose de *n* dés à six faces, chaque face contient un nombre entier.
    On dispose les dès en ligne en choisissant chaque face
    de telle sorte que le nombre entier d'un dé
    précède celui de son voisin de droite, plus exactement,
    on veut construire une suite d'entiers consécutifs.
    Le problème consiste à déterminer, pour un jeu de dès donné
    la séquence la plus longue.
    """

    def __init__(self, dices):
        """
        Dices = list of 6-uples
        """
        self.dices = dices

    @staticmethod
    def parse(str_or_file):
        """
        Reads the content of a problem
        Returns a list of @see cl DiceStraight.

        @param      str_or_file     string or filename
        @return                     list of @see cl DiceStraight
        """
        if "\n" not in str_or_file:
            with open(str_or_file, "r") as f:
                str_or_file = f.read()
        parsed = []
        lines = str_or_file.strip("\n ").split("\n")
        nbp = int(lines[0])
        pos = 1
        for i in range(0, nbp):
            nbd = int(lines[pos])
            pos += 1
            dices = []
            for j in range(0, nbd):
                dice = [int(_) for _ in lines[pos].split()]
                if len(dice) != 6:
                    raise ValueError(
                        "A dice has no 6 faces '{0}'".format(lines[pos]))
                pos += 1
                dices.append(dice)
            parsed.append(DiceStraight(dices))
        return parsed

    def __len__(self):
        """
        Retourne le nombre de dés.
        """
        return len(self.dices)

    def compute_edges(self):
        """
        Computes all possible edges.

        @return     ``list of tuple (n1, n2)``

        Each node is a triplet: (position, dice, face value).
        """
        values = {}
        root = (-1, -1, -1)
        edges = []
        for pos in range(len(self)):
            for di in range(len(self)):
                for face in range(0, 6):
                    value = self.dices[di][face]
                    key = (pos, di, value)
                    if value not in values:
                        values[value] = []
                    values[value].append(key)
                    if pos == 0:
                        edges.append((root, key))
        for val, keys in values.items():
            cross = values.get(val + 1)
            if cross is None:
                continue
            for val2 in cross:
                for key in keys:
                    if key[0] == val2[0] - 1:
                        edges.append((key, val2))
        return edges

    def compute_number_paths(self, edges):
        """
        Computes the number of paths accross every node.
        """
        # Stores keys by positions.
        pos = {}
        for b, f in edges:
            p = b[0]
            if p not in pos:
                pos[p] = set()
            pos[p].add((b, f))

        # Computes the number of path. Use the properties of the topology.
        root = (-1, -1, -1)
        nbpath = {root: 1}
        for p in range(-1, len(self) - 1):
            if p not in pos:
                continue
            for k1, k2 in pos[p]:
                if k1 not in nbpath:
                    continue
                if (k1, k2) in edges:
                    if k1[1] == k2[1]:
                        continue
                    if k2 not in nbpath:
                        nbpath[k2] = 0
                    nbpath[k2] += nbpath[k1]
        return nbpath

    def compute_paths(self, edges):
        """
        Computes the paths accross every node. Checks that
        the same dice does not appear twice along the path.
        The function returns a list of paths described by a list
        of tuple (dice, face).
        """
        # Stores keys by positions.
        pos = {}
        for b, f in edges:
            p = b[0]
            if p not in pos:
                pos[p] = set()
            pos[p].add((b, f))

        # Computes the number of path. Use the properties of the topology.
        root = (-1, -1, -1)
        paths = {root: [OrderedDict()]}
        paths[root][0][-1] = -1
        for p in range(-1, len(self) - 1):
            if p not in pos:
                continue
            for k1, k2 in pos[p]:
                if k1 not in paths:
                    continue
                if (k1, k2) in edges:
                    if k1[1] == k2[1]:
                        continue
                    if k2 not in paths:
                        paths[k2] = []
                    d = k2[1]
                    for exp in paths[k1]:
                        if d not in exp:
                            e = exp.copy()
                            e[d] = k2[2]
                            paths[k2].append(e)
        return paths

    def __str__(self):
        """
        Usual.
        """
        return "\n".join(str(_) for _ in self.dices)

    def longest_path_length(self, fLOG=noLOG):
        """
        One good and bad solution.

        TODO: Remmove nbpath, put face number in between
        """
        fLOG(
            "[longest_path_length] compute edges with {0} dices".format(len(self)))
        edges = self.compute_edges()
        fLOG("[longest_path_length] nb edges {0}".format(len(edges)))
        nbpath = self.compute_number_paths(edges)
        fLOG("[longest_path_length] nb path {0}".format(len(nbpath)))
        mul = list(filter(lambda el: el[1] > 1, nbpath.items()))
        rev = [(v, k) for k, v in mul]
        if len(rev) > 0:
            rev.sort()
            max_mul = rev[-1][0]
        else:
            max_mul = 0
        fLOG("[longest_path_length] max_mul={0}".format(max_mul))
        if max_mul > 5:
            # The problem has multiple solution and the multiplication of
            # paths might be big.
            rows = []
            for i, (k, v) in enumerate(sorted(nbpath.items())):
                if min(i, len(nbpath) - i) < 20:
                    rows.append('{0}:{1}'.format(k, v))

            raise NotImplementedError(
                "nb={0}-max={1}\n{2}".format(len(mul), rev[-1], "\n".join(rows)))
        else:
            # Only one path --> easy but we need to check the same dice was not used twice.
            paths = self.compute_paths(edges)
            new_paths = []
            for start, ps in paths.items():
                for path in ps:
                    del path[-1]
                    new_paths.append([(k, v) for k, v in path.items()])
            best = None
            for path in sorted(new_paths):
                if best is None or len(path) > len(best):
                    best = path
            del best[-1]
            return best
