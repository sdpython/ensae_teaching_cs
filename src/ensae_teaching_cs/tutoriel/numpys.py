# -*- coding: utf-8 -*-
"""
@file
@brief Quelques constructions classiques pour éviter de recoder des variantes d'algorithmes.
classiques.
"""

from functools import reduce

def numpy_matrix2list(mat):
    """
    Convertit une matrice `numpy <http://www.numpy.org/>`_ en list.

    @param      mat     matrix
    @return             liste de listes

    @example(science___opérations avec numpy.matrix)
    Voici quelques écritures classiques avec le module
    `numpy <http://www.numpy.org/>`_.

    @code
    import numpy as np
    mat = np.matrix ( [[1,2],[3,4]] ) # crée une matrice 2*2
    s   = mat.shape           # égale à (nombre de lignes, nombre de colonnes)
    l   = mat [0,:]           # retourne la première ligne
    c   = mat [:,0]           # retourne la première colonne
    iv  = mat.I               # inverse la matrice
    mat [:,0] = mat [:,1]     # la première ligne est égale à la seconde
    o   = np.ones ( (10,10) ) # crée un matrice de 1 10x10
    d   = np.diag (mat)       # extrait la diagonale d'une matrice
    dd  = np.matrix (d)       # transforme d en matrice
    t   = mat.transpose ()    # obtient la transposée
    e   = mat [0,0]           # obtient de première élément
    k   = mat * mat           # produit matriciel
    m   = mat * 4             # multiplie la matrice par 4
    mx  = np.max (mat [0,:])  # obtient le maximum de la première ligne
    s   = np.sum (mat [0,:])  # somme de la première ligne


    mat = np.diagflat ( np.ones ( (1,4) ) )
    print (mat)  # matrice diagonale
    t   =  mat == 0
    print (t)    # matrice de booléens
    mat [ mat == 0 ] = 4
    print (mat)  # ...
    print (iv)  # ...
    @endcode

    @endexample
    """
    return mat.tolist()