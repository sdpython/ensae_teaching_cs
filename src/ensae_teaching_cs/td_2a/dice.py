# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes de
`Google Jam <https://code.google.com/codejam/>`_.

"""
import numpy


class DiceStraight:
    """
    Inspired by `Problem A. Dice Straight
    <https://codingcompetitions.withgoogle.com/codejam/
    round/0000000000201909/00000000002017fc>`_.
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
            for _ in range(0, nbd):
                dice = [int(_) for _ in lines[pos].split()]
                if len(dice) != 6:
                    raise ValueError(
                        f"A dice has no 6 faces '{lines[pos]}'")
                pos += 1
                dices.append(dice)
            parsed.append(DiceStraight(dices))
        return parsed

    def __len__(self):
        """
        Retourne le nombre de dés.
        """
        return len(self.dices)

    def __str__(self):
        """
        Displays dices.
        """
        rows = []
        for dice in self.dices:
            rows.append(f'{dice!r}')
        return '\n'.join(rows)

    @staticmethod
    def max_number_sequences(n):
        """
        Returns the maximum number of sequences
        given the number of dices.
        """
        res = []
        for k in range(1, n + 1):
            res.append(((6. * n / k) ** k, k))
        return max(res)

    def longest_straight_sequence(self):
        """
        Returns one of the longest sequence of consecutive integers.
        It returns a list of tuple (face, dice). The implementation
        may be improved a lot.
        """
        des = numpy.array(self.dices)
        faces = []
        nde = []
        for i in range(des.shape[0]):
            faces.extend(des[i, :])
            nde.extend([i for j in range(des.shape[1])])
        ensemble = list(zip(faces, nde))
        ensemble.sort()

        def sequence(ensemble, pos, seq):
            des_choisis = set(ensemble[s][1] for s in seq)
            face = ensemble[pos][0]

            a = pos + 1
            while a < len(ensemble) and ensemble[a][0] == face:
                a += 1
            if a >= len(ensemble) or ensemble[a][0] != face + 1:
                # pas possible
                return seq

            b = a
            while b < len(ensemble) and ensemble[b][0] == face + 1:
                b = b + 1

            seqs = []
            for i in range(a, b):
                if ensemble[i][1] not in des_choisis:
                    seq2 = seq.copy()
                    seq2.append(i)
                    seq2 = sequence(ensemble, i, seq2)
                    seqs.append(seq2)
            if len(seqs) == 0:
                return seq
            seqs_len = max([(len(s), s) for s in seqs])
            return seqs_len[1]

        best = None
        for i in range(len(ensemble)):
            res = sequence(ensemble, i, [i])
            if best is None or len(res) > len(best):
                best = res

        if len(best) == 1:
            return []
        res = [ensemble[i] for i in best]
        return [(d, f) for (f, d) in res]
