# -*- coding: utf-8 -*-
"""
@file
@brief Implémentation de la résolution de l'énigme d'Hermionne (Harry Potter tome 1)
"""


def solution_correcte(sol):
    """
    Cette fonction reçoit un tableau de 7 cases,
    chaque case contient un entier compris entre 0 et 3 inclus :
    0 : poison, 1 : vin, 2 : reculer, 3 : avancer
    la fonction détermine si l'agencement proposé dans *sol*
    vérifie les cinq règles de l'énoncé,
    retourne *True* si toutes les règles sont vérifiées
    ou *False* si l'une des règles n'est pas vérifiée.
    Rappel : les indices vont de 0 a 6 inclus car il y a 7 cases.
    """

    # règle 1
    nb = [0, 0, 0, 0]
    for s in sol:
        nb[s] += 1
    if nb[0] != 3:
        return False  # 3 poison
    if nb[1] != 2:
        return False  # 2 vin
    if nb[2] != 1:
        return False  # 1 reculer
    if nb[3] != 1:
        return False  # 1 avancer

    # règle 2
    for i in range(1, len(sol)):
        if sol[i] == 1 and sol[i - 1] != 0:
            return False

    # règle 3
    if sol[0] == sol[6]:
        return False
    if sol[0] == 3:
        return False
    if sol[6] == 3:
        return False

    # règle 4
    if sol[2] == 0:
        return False
    if sol[5] == 0:
        return False

    # règle 5
    if sol[1] != sol[5]:
        return False

    # si on arrive ici, c'est que toutes les règles sont vérifiées
    return True


def affiche_solution(sol):
    """
    Retourne une chaîne de caractères qui représente la solution.
    """
    a = ["poison", "vin", "reculer", "avancer"]
    res = ""
    for s in sol:
        res += "{0}, ".format(a[s])
    return res


def solution():
    """
    Parcourt toutes les configurations possibles
    et s'arrête à la première qui satsifait toutes les règles.

    ::

        from ensae_teaching_cs.special.hermionne import solution, affiche_solution
        res = solution()
        print(affiche_solution(res))
    """
    sol = [0, 0, 0, 0, 0, 0, 0]
    while sol[0] < 4:
        r = solution_correcte(sol)
        if r:
            return sol

        sol[6] += 1
        # on parcourt les indices en, allant de 6 à 1 inclus
        for i in range(len(sol) - 1, 0, -1):
            if sol[i] >= 4:
                sol[i] = 0
                sol[i - 1] += 1


if __name__ == "__main__":
    ressol = solution()
    print(affiche_solution(ressol))
