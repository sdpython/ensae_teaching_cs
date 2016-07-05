# coding:latin-1
"""
On cherche à comparer deux fonctions qui simulent une variable aléatoire multinomiale.
Elles utilisent deux fonctions différentes simulant une loi uniforme différente.
"""

chideux_table = [3.84, 5.99, 7.82, 9.49, 11.07,
                 12.59, 14.07, 15.51, 16.92, 18.31, 19.68, 21.03]

import random
import copy
import numpy as np


def tirage_entier(proba):
    """tire un nombre aléatoire entre 1 et len(proba)
    selon la distribution indiquée par proba
    on suppose que chaque valeur * 100 est entière"""
    r = random.randint(1, 10)
    x = 0
    i = 0
    while i < len(proba):
        x += proba[i] * 10
        if r <= x:
            return i + 1
        i += 1
    raise Exception("impossible a priori sauf si sum(proba) != 1")


def tirage_reel(vecteur):
    """tire un nombre aléatoire entre 1 et len(vecteur)
    selon la distribution indiquée par vecteur"""
    a = random.uniform(0, 1)
    p = 0
    k = 1
    j = vecteur[p]
    while a > j:
        p += 1
        j += vecteur[p]
        k += 1
    return k


def tirages(N, fonction, proba):
    """effectue N tirage et compte les valeurs"""
    cont = {}
    for i in xrange(0, N):
        x = fonction(proba)
        if x not in cont:
            cont[x] = 1
        else:
            cont[x] += 1
    return cont


def chideux(cont, proba):
    """calcul le chi deux entre la distribution simulée et la distribution théorique"""
    s = 0
    t = sum(cont.values())
    for i, v in enumerate(proba):
        d = t * v - cont[i + 1]
        d *= d / t * v
        s += d
    return s


def affichage(cont, proba):
    key = cont.keys()
    key.sort()
    print "---------"
    for k in key:
        print k, "\t", cont[k]
    print "pr ", " ".join(["%1.2f" % p for p in proba])
    chi = chideux(cont, proba)
    print "chi deux", chi, " 95% ", chideux_table[len(proba) - 2]
    return chi


def tirageT(T, fonction, p1, p2, p3):
    """
    on fait T tirages:
        x1: le premier est fait selon p1
        xt: le second est fait selon:
              p1 si x t-1 in [1,2]
              p2 si x t-1 in [1,2]
              p3 si x t-1 in [1,2]
    """
    x1 = fonction(p1)
    all = [x1]
    while len(all) < T:
        if x1 in [1, 2]:
            x2 = fonction(p1)
        elif x1 in [3, 4]:
            x2 = fonction(p2)
        else:
            x2 = fonction(p3)
        all.append(x2)
        x1 = x2
    return tuple(all)


def tiragesT(T, N, fonction, p1, p2, p3):
    """effectue N tirage et compte les du second chiffre"""
    cont = {}
    for i in xrange(0, N):
        xx = tirageT(T, fonction, p1, p2, p3)
        if xx[-1] not in cont:
            cont[xx[-1]] = 1
        else:
            cont[xx[-1]] += 1
    return cont


def proba2_th(t, p1, p2, p3):
    """
    retourne la probabilité théorique de distribution du tirage t
    """
    if t == 1:
        return p1
    B = [p1, p1, p2, p2, p3, p3]
    mat = np.matrix(B)
    v = np.matrix(p1)
    while t > 1:
        v = v * mat
        t = t - 1
    return [v[0, i] for i in xrange(0, len(p1))]


if __name__ == "__main__":
    proba = [0.1, 0.2, 0.3, 0.1, 0.1, 0.2]
    N = 10000
    affichage(tirages(N, tirage_entier, proba), proba)
    affichage(tirages(N, tirage_reel, proba), proba)

    memo = []

    for T in xrange(1, 10):
        print "########", T
        p1 = [0.1, 0.2, 0.3, 0.1, 0.1, 0.2]
        p2 = [0.3, 0.1, 0.1, 0.1, 0.1, 0.3]
        p3 = [0.3, 0.1, 0.1, 0.1, 0.1, 0.3]
        pr = proba2_th(T, p1, p2, p3)
        c1 = affichage(tiragesT(T, N, tirage_entier, p1, p2, p3), pr)
        c2 = affichage(tiragesT(T, N, tirage_reel, p1, p2, p3), pr)
        memo.append((T, c1, c2))

    for _ in memo:
        print _
