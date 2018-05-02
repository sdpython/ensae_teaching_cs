# -*- coding: utf-8 -*-
"""
@file
@brief Implémentation de la résolution de l'énigme d'Hermionne (Harry Potter tome 1)
avec des classes.
`logique <https://fr.wikipedia.org/wiki/R%C3%A8gle_de_r%C3%A9solution>`_.
"""


class Case:
    """
    L'énigme d'Hermionne repose sur 7 cases disposées en ligne.
    Cette classe définit une case.
    """
    contenu_case = ["poison", "vin", "reculer", "avancer"]

    def __init__(self, contenu):
        """
        constructeur
        """
        self.contenu = Case.contenu_case.index(contenu)

    def __str__(self):
        """
        affiche le contenu
        """
        return Case.contenu_case[self.contenu]


class Regle:
    """
    L'énigme repose sur des règles.
    Chaque règle hérite de cette classe et implémente la méthode
    *correcte* qui vérifie si la règle est vérifiée ou non.
    """

    def correcte(self, cases):
        """
        cette méthode doit être surchargée
        """
        raise NotImplementedError()


class Regle1(Regle):
    """
    implémente la première règle
    """

    def correcte(self, cases):
        """
        vérifie qu'on a bien le bon nombre de types de fioles
        """
        nb = [0, 0, 0, 0]
        for s in cases:
            nb[s.contenu] += 1
        if nb[0] != 3:
            return False  # 3 poison
        if nb[1] != 2:
            return False  # 2 vin
        if nb[2] != 1:
            return False  # 1 reculer
        if nb[3] != 1:
            return False  # 1 avancer
        return True


class Regle2(Regle):
    """
    implémente la seconde règle
    """

    def correcte(self, cases):
        """
        vérifie le voisi n de reculer
        """
        for i in range(1, len(cases)):
            if cases[i].contenu == 1 and cases[i - 1].contenu != 0:
                return False
        return True


class Regle3(Regle):
    """
    implémente la troisième règle
    """

    def correcte(self, cases):
        """
        ...
        """
        if cases[0].contenu == cases[6].contenu:
            return False
        if cases[0].contenu == 3:
            return False
        if cases[6].contenu == 3:
            return False
        return True


class Regle4(Regle):
    """
    implémente la quatrième règle
    """

    def correcte(self, cases):
        """
        ...
        """
        if cases[2].contenu == 0:
            return False
        if cases[5].contenu == 0:
            return False
        return True


class Regle5(Regle):
    """
    implémente la cinquième règle
    """

    def correcte(self, cases):
        """
        ...
        """
        if cases[1].contenu != cases[5].contenu:
            return False
        return True


class Enigme:
    """
    description de l'énigme
    """

    def __init__(self):
        """
        constructeur, définit les règles et les cases
        """
        self.regle = [Regle1(), Regle2(), Regle3(), Regle4(), Regle5()]
        self.cases = [Case("poison") for i in range(0, 7)]

    def __str__(self):
        """
        affiche la solution
        """
        return ", ".join(str(c) for c in self.cases)

    def solution_correcte(self):
        """
        détermine si une solution vérifie toutes les règles
        """
        for r in self.regle:
            if not r.correcte(self.cases):
                return False
        return True

    def resoud(self):
        """
        résoud l'énigme en essayant toutes les combinaisons possibles,
        ce n'est pas la plus efficace des solutions
        """
        for c in self.cases:
            c.contenu = 0

        while self.cases[0].contenu < 4:
            r = self.solution_correcte()
            if r:
                return self

            self.cases[6].contenu += 1
            # on parcourt les indices en, allant de 6 a 1 inclus
            for i in range(len(self.cases) - 1, 0, -1):
                if self.cases[i].contenu >= 4:
                    self.cases[i].contenu = 0
                    self.cases[i - 1].contenu += 1


def solution():
    """
    parcourt toutes les configurations possibles
    et s'arrête à la première qui satsifait toutes les règles

    ::

        from ensae_teaching_cs.special.hermionne_classe import solution
        print(solution())

    """
    e = Enigme()
    e.resoud()
    return e
