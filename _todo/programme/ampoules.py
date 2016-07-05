# coding: cp1252

import math
import random


def generate_expo(mu):
    return random.expovariate(mu)

S = 10000
iteration = 500
mu = 1.0 / 100

# création d'un tableau de S ampoule qui contient la durée de
# vide restante d'une ampoule
ampoule = [0 for a in range(0, S)]
moyenne_grille = 0
for i in range(0, iteration):
    grille = 0
    mean = 0
    for n in range(0, S):
        mean += ampoule[n]
        if ampoule[n] == 0:
            # remplacement d'une ampoule grillée
            grille += 1
            # on détermine la durée de vie de cette ampoule
            # on arrondit à l'entier le plus proche
            ampoule[n] = int(generate_expo(mu))
        else:
            # on enlève une heure à la durée de vie de l'ampoule
            ampoule[n] -= 1
    mean /= S
    if i > 0:
        moyenne_grille += grille
    print "itération : ", i, " moyenne durée : ", mean, " grillées :", grille

moyenne_grille = float(moyenne_grille) / float(iteration - 1)
print "nombre moyen d'ampoules grillées :", moyenne_grille
