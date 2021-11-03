#coding: latin-1

######### énoncé 1, exercice 1, recherche dichotomique

## question 1 

def recherche_dichotomique( element, liste_triee ):
    """
    premier code: http://www.xavierdupre.fr/blog/2013-12-01_nojs.html    
    """
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        if liste_triee[m] == element :
            return m
        elif liste_triee[m] > element :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a
    
l = [ 0, 2, 4, 6, 8, 100, 1000 ]
print (recherche_dichotomique(100, l))  # affiche 5

## question 2

def deux_recherches(element,liste_impair,liste_pair) :
    if element % 2 == 0 :
        return recherche_dichotomique(element, liste_pair), -1
    else :
        return -1, recherche_dichotomique(element, liste_impair)

lp = [ 0, 2, 4, 6, 8, 100, 1000 ]
li = [ 1, 3, 5 ]
print (deux_recherches(100, li, lp))  # affiche (5, -1)

## question 3
"""       
                            liste coupée       liste non coupée (2n)
recherche simple                1 + n                 2n
recherche dichotomique          1 + ln n             ln(2n) = 1 + ln(n)

coût équivalent
"""

## question 4 

def recherche_dichotomique( element, liste_triee ):
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        if liste_triee[m] == element :
            return m
        elif liste_triee[m] > element :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    if liste_triee[a] != element :  return -1       # ligne ajoutée
    else : return m                                 # ligne ajoutée
    
l = [ 0, 2, 4, 6, 8, 100, 1000 ]
for i in l :
    print (i,recherche_dichotomique(i, l))  
    # vérifier qu'on retrouve tous les éléments existant
print (recherche_dichotomique(1, l))   # affiche -1

## question  5

def deux_recherches(element,liste_impair,liste_pair) :
    i = recherche_dichotomique(element, liste_impair)
    if i == -1 : return recherche_dichotomique(element, liste_pair)
    else : return i
    
##question 6 

"""
Les logarithmes sont en base 2.

coût fonction question 2 : 1001 ( 1 + ln(n) )      = C1
coût fonction question 5 : 1000 ln(n)  + 2 ln(n)   = C2
C2 - C1 = ln(n) - 1001 > 0
    
La fonction 5 est plus rapide dans ce cas.
"""
