# coding: latin-1
import random
import numpy
import math
import pylab
import copy

###
# réponse à la question 1
###


def get_tour():
    tour = """Auxerre	3,537309885	47,76720047
Bastia	9,434300423	42,66175842
Bordeaux	-0,643329978	44,80820084
Boulogne	1,579570055	50,70875168
Caen	-0,418989986	49,14748001
Le Havre	0,037500001	49,45898819
Lens	2,786649942	50,40549088
Lille	2,957109928	50,57350159
Lyon	4,768929958	45,70447922
Paris	2,086790085	48,65829086
Lyon	4,768929958	45,70447922
Marseille	5,290060043	43,1927681
Lille	2,957109928	50,57350159
Nantes	-1,650889993	47,16867065
Rennes	-1,759150028	48,05683136
Toulouse	1,356109977	43,5388298
Strasbourg	7,687339783	48,49562836
Nancy	6,134119987	48,66695023
Nice	7,19904995	43,6578598
Saint-Etienne	4,355700016	45,39992905
Brest	-4,552110195	48,36014938
Metz	6,11729002	49,0734787
Sedan	4,896070004	49,68407059
Grenoble	5,684440136	45,13940048
Annecy	6,082499981	45,8782196""".replace(",", ".").split("\n")
    # ligne d'avant : on découpe l'unique chaîne de caractères

    # ligne suivant : on découpe chaque ligne en colonne
    tour = [t.strip("\r\n ").split("\t") for t in tour]
    # puis on convertit les deux dernières colonnes
    tour = [t[:1] + [float(x) for x in t[1:]] for t in tour]
    return tour

###
# réponse à la question 2
###


def distance(tour, i, j):
    dx = tour[i][1] - tour[j][1]
    dy = tour[i][2] - tour[j][2]
    return (dx**2 + dy**2) ** 0.5

###
# réponse à la question 3
###


def longueur_tour(tour):
    # n villes = n segments
    d = 0
    for i in xrange(0, len(tour) - 1):
        d += distance(tour, i, i + 1)
    # il ne faut pas oublier de boucler pour le dernier segment
    d += distance(tour, 0, -1)
    return d

###
# réponse à la question 4
###


def graph(tour):
    x = [t[1] for t in tour]
    y = [t[2] for t in tour]
    x += [x[0]]   # on ajoute la dernière ville pour boucler
    y += [y[0]]   #
    pylab.plot(x, y)
    for ville, x, y in tour:
        pylab.text(x, y, ville)
    pylab.show()

###
# réponse à la question 5
###


def permutation(tour):

    # on calcule la longueur du tour actuelle
    best = longueur_tour(tour)

    # variable fix : dit combien d'échanges ont eu lieu depuis la
    # dernière amélioration
    fix = 0
    while True:
        # on tire deux villes au hasard
        i = random.randint(0, len(tour) - 1)
        j = random.randint(0, len(tour) - 1)
        if i == j:
            continue

        # on les échanges si i != j
        e = tour[i]
        tour[i] = tour[j]
        tour[j] = e

        # on calcule la nouvelle longueur
        d = longueur_tour(tour)

        if d >= best:
            # si le résultat est plus long --> retour en arrière
            # ce qui consiste à échanger à nouveau les deux villes
            fix += 1
            e = tour[i]
            tour[i] = tour[j]
            tour[j] = e
        else:
            # sinon, on garde le tableau tel quel
            best = d
            # et on met fix à 0 pour signifier qu'une modification a eu lieu
            fix = 0

        # si aucune modification n'a eu lieu durant les dernières 10000 itérations,
        # on s'arrête
        if fix > 10000:
            break

###
# réponse à la question 6
###


def retourne(tour, i, j):
    """
    on échange les éléments i et j
    puis i+1 et j-1
    puis i+2 et j-2
    tant que i+k < j-k
    """
    while i <= j:
        e = tour[i]
        tour[i] = tour[j]
        tour[j] = e
        i += 1
        j -= 1

###
# réponse à la question 7
###


def croisement(tour):
    """
    cette fonction reprend le même schéma que la fonction permutation
    on annule une modification en appelant à nouveau la fonction retourne
    """
    best = longueur_tour(tour)
    fix = 0
    while True:
        i = random.randint(0, len(tour) - 2)
        j = random.randint(i + 1, len(tour) - 1)
        retourne(tour, i, j)
        d = longueur_tour(tour)
        if d >= best:
            # retour en arrière
            fix += 1
            retourne(tour, i, j)
        else:
            fix = 0
            best = d
        if fix > 10000:
            break

###
# réponse à la question 8
###


def enchaine(tour):
    """
    cette fonction est plus complexe que le résultat demandé pour cette question
    on enchaîne les deux fonctions (croisement, permutation) tant que
    la longueur du circuit diminue

    et si jamais cette longueur ne diminue plus, on perturbe le circuit
    au plus deux fois
    en échangeant trois couples de villes choisies au hasard,
    cette dernière partie n'était pas prévue dans l'énoncé
    """
    best = longueur_tour(tour)
    tttt = copy.deepcopy(tour)
    print "debut", best
    nom = 0
    while True:

        croisement(tour)
        d = longueur_tour(tour)
        print "croisement", d, best

        permutation(tour)
        d = longueur_tour(tour)
        print "permutation", d, best

        if d < best:
            best = d
            tttt = copy.deepcopy(tour)
            nom = 0
        elif nom > 2:
            break
        else:
            nom += 1
            for k in range(0, 3):
                i = random.randint(0, len(tour) - 2)
                j = random.randint(i + 1, len(tour) - 1)
                e = tour[i]
                tour[i] = tour[j]
                tour[j] = e

    return tttt


if __name__ == "__main__":
    tour = get_tour()
    tour = enchaine(tour)
    graph(tour)
