# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes de
`Google Jam <https://code.google.com/codejam/>`_.

"""
from collections import OrderedDict
from pyquickhelper.loghelper import noLOG
from .edmonds_karp import EdmondsKarpGraph


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

    def compute_edges(self, add_position=True):
        """
        Computes all possible edges.

        @param      add_position    add position into the node definition
        @return                     ``list of tuple (n1, n2)``

        Each node is a triplet: (position, dice, face value) if *app_position*,
        a couple (dice, face value) otherwise.
        """
        values = {}
        root = (-1, -1, -1) if add_position else (-1, -1)
        edges = []
        for di in range(len(self)):
            for face in range(0, 6):
                value = self.dices[di][face]
                if add_position:
                    for pos in range(len(self)):
                        key = (pos, di, value)
                        if value not in values:
                            values[value] = []
                        values[value].append(key)
                        if pos == 0:
                            edges.append((root, key))
                else:
                    key = (di, value)
                    if value not in values:
                        values[value] = []
                    values[value].append(key)

        for val, keys in values.items():
            cross = values.get(val + 1)
            if cross is None:
                continue
            for val2 in cross:
                for key in keys:
                    if key[1] == val2[1]:
                        # Reject edges to itself.
                        continue
                    if not add_position or key[0] == val2[0] - 1:
                        edges.append((key, val2))
        return edges

    def compute_paths(self, edges):
        """
        Computes the paths accross every node if the position is
        included in the node description as triplet.
        The function checks that the same dice does not appear twice along the path.
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
                            if len(paths) > 1000:
                                raise ValueError(
                                    "The number of paths is more than 1000 in one particular note {0}.".format(k2))
        return paths

    def __str__(self):
        """
        Usual.
        """
        return "\n".join(str(_) for _ in self.dices)

    def find_intervals(self):
        """
        We need to find the longest sequence of consecutive
        face values. We are then looking to order the face
        values and to determine intervals of consecutives
        values. Wwe check that every pair of
        consecutive numbers can be linked with two different dices.

        @return     list of intervals.
        """
        cons = set()
        for n1, n2 in self.compute_edges(add_position=False):
            cons.add((n1[1], n2[1]))

        values = set()
        for dice in self.dices:
            for p in dice:
                values.add(p)
        values = list(sorted(values))
        intervals = []
        first = values[0]
        for i in range(1, len(values)):
            v1, v2 = values[i] - 1, values[i]
            if (v1, v2) not in cons:
                if first != values[i - 1]:
                    intervals.append((first, values[i - 1]))
                first = values[i]
        i = len(values)
        if first != values[i - 1]:
            intervals.append((first, values[i - 1]))

        return intervals

    def longest_path_length_graph(self, fLOG=noLOG):
        """
        This solution is fast as long as the problem
        does not include too similar dices.
        In that case, the created graph is too big.
        """
        fLOG(
            "[longest_path_length_triplet] compute edges with {0} dices".format(len(self)))
        edges = self.compute_edges()
        fLOG("[longest_path_length_triplet] nb edges {0}".format(len(edges)))
        paths = self.compute_paths(edges)
        fLOG("[longest_path_length_triplet] nb paths {0}".format(len(paths)))
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
        fLOG("[longest_path_length_triplet] path {0}".format(best))
        return best

    def longest_path_length_flow(self, fLOG=noLOG):
        """
        We use an algorithm of maximum flow to solve the graph.
        We use the graph where each node is a triplet *(position, dice, face value)*.
        Each node is connected to *(-1, -1, -1)*.
        We add another node *(-2, -2, -2)* which begins every path.
        We write N as the number of dices + 1.
        We add edges to nodes *(position, N, N)* from every node.
        We finally add final edges from nodes *(position, N, N)* to
        *(N, N, N)* whose weight is ``1/N``.
        Let's denote the maximum flow as *M*. *MN* determines
        the longest length.
        """
        edges = self.compute_edges(add_position=True)
        nodes = set(_[0] for _ in edges).union(set(_[1] for _ in edges))
        capacity = [(e[0], e[1], 1) for e in edges]
        N = len(self) + 1
        for node in nodes:
            if node[0] >= 0:
                capacity.append((node, (N, node[0], node[0]), 1))
        capacity.append(((-2, -2, -2), (-1, -1, -1), 1))
        # We skip the first position as we are not
        # interted in path of length 1.
        for p in range(1, len(self)):
            capacity.append(((N, p, p), (N, N, p), 1))
            capacity.append(((N, N, p), (N, N, N), 1. / len(self)))

        edmond = EdmondsKarpGraph(capacity)
        try:
            max_flow = edmond.edmonds_karp((-2, -2, -2), (N, N, N), fLOG=fLOG)
        except ValueError:
            # No available path.
            return 0
        return int(max_flow * len(self) - 1e-5) + 1
