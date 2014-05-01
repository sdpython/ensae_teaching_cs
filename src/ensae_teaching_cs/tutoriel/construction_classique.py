# -*- coding: utf-8 -*-
"""
@file
@brief Quelques constructions classiques pour éviter de recoder des variantes d'algorithmes.
classiques.
"""

def recherche(li, c):
    """
    Retourne l'index d'un élément ou -1 si non trouvé
    
    @param      li      liste
    @param      c       élément à trouver
    @return             position
    
    @example(construction classique___recherche avec index)

    Lorsqu'on cherche un élément dans un tableau, on cherche plus souvent 
    sa position que le fait que le tableau contient cet élément.

    @code
    def recherche (li, c) :
        for i,v in enumerate (li) :
            if v == c : return i
        return -1
    li = [ 45, 32, 43, 56 ]
    print (recherche (li, 43))  # affiche 2
    @endcode
    
    En python, il existe un fonction simple qui permet de faire ça :
    
    @code
    print (li.index (43))  # affiche 2
    @endcode
    
    Lorsque l'élément n'y est pas, on retourne souvent la position ``-1``
    qui ne peut être prise par aucun élément :
    
    @code
    if c in li :  return li.index(c)
    else: return -1
    @endcode
    
    Même si ce bout de code parcourt deux fois le tableau (une fois déterminer
    sa présence, une seconde fois pour sa position), ce code est souvent plus rapide
    que la première version et la probabilité d'y faire une erreur plus faible.
    @endexample
    """
    if c in li : 
        return li.index(c)
    else:
        return -1
        
def minindex(li):
    """
    Retourne l'index du minimum et le minimum.
    
    @param  li      liste
    @return         tuple (minimum,position)
    

    @example(construction classique___minimum avec position)
    La fonction `min <https://docs.python.org/3.4/library/functions.html#min>`_ 
    retourne le minium d'un tableau mais pas sa position.
    Le premier réflexe est alors de recoder le parcours de la liste
    tout en conservant la position du minimum.
    
    @code
    li = [ 0, 434, 43, 6436, 5 ]
    m  = 0
    for i in xrange (0, len (li)) : 
        if li [m] < li [i] : m = i
    @endcode
    
    Mais il existe une astuce pour obtenir la position sans avoir à le reprogrammer.
    
    @code
    k = [ (v,i) for i,v in enumerate (li) ]
    m = min(k)
    @endcode
    
    La fonction ``min`` choisit l'élément minimum d'un tableau dont les éléments sont des 
    couples (élément du premier tableau, sa position).
    Le minimum est choisi en comparant les éléments, et la position
    départegera les exaequo.
    
    @endexample
    """
    return min  ( (v,i) for i,v in enumerate (li) )
    