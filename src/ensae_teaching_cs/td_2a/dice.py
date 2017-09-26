# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes de
`Google Jam <https://code.google.com/codejam/>`_.

"""


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

    def one_solution(self):
        """
        One good and bod solution.
        """
        graph = {}
        for i in range(len(self)):
            for j in range(len(self)):
                for f in range(0, 6):
                    pass
        return graph
