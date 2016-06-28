# coding: cp1252
import random

def construit_suite(n):
    """construit une liste de n nombres entiers compris entre 0 et 99"""
    l = []
    for i in range(0,n):
        l.append (random.randint(0,10))
    return l

def tri_entiers(l):
    """ tri une liste l, les éléments à trier sont entiers"""
    # première boucle, minimum, maximum
    m = l [0]
    M = l [0]
    for k in range(1,len(l)):
        if l [k] < m : m = l [k]
        if l [k] > M : M = l [k]
    
    # calcul du nombre d'occurrences
    p = [0 for i in range (m,M+1) ]
    for i in range (0, len (l)) :
        p [ l [i] - m ] += 1
        
    # fonction de répartition
    P = [0 for i in range (m,M+1) ]
    P [0] = p [0]
    for k in range (1, len (p)) :
        P [k] = P [k-1] + p [k]
        
    # tri
    pos = 0
    for i in range (1, len (l)) :
        while P [pos] < i : pos += 1
        l [i-1] = pos + m
    l [len (l)-1] = M


l = construit_suite(8)          # création d'une suite aléatoirement
print "liste non triée :\t",l   # affichage
tri_entiers (l)                 # tri
print "liste triée     :\t",l   # affichage
