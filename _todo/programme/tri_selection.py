# coding: cp1252
import random

def construit_suite(n):
    """construit une liste de n nombres entiers compris entre 0 et 99"""
    l = []
    for i in range(0,n):
        l.append (random.randint(0,100))
    return l

def tri_selection(l):
    """ tri une liste l, tri par sélection"""
    # première boucle, répétition des étapes A et B
    for i in range(0,len(l)):

        # recherche du maximum, on suppose pour commencer
        # qu'il est à la position 0
        pos = 0
        # boucle de l'étape A
        for j in range(1,len(l)-i):
            if l [pos] < l [j]: pos = j

        # échange de l'étape B
        # la position du maximum est conservé dans la variable pos
        # on fait l'échange avec l'élément à la position len(l)-i-1
        k       = len(l)-i-1
        ech     = l [k]
        l [k]   = l [pos]
        l [pos] = ech

l = construit_suite(8)          # création d'une suite aléatoirement
print "liste non triée :\t",l   # affichage
tri_selection (l)               # tri
print "liste triée     :\t",l   # affichage
