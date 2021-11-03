#coding: latin-1

# énoncé 1, exercice 1, recherche dichotomique

# question 1

def recherche_dichotomique(element, liste_triee):
    """
    premier code: http://www.xavierdupre.fr/blog/2013-12-01_nojs.html
    """
    a = 0
    b = len(liste_triee) - 1
    m = (a + b) // 2
    while a < b:
        if liste_triee[m] == element:
            return m
        elif liste_triee[m] > element:
            b = m - 1
        else:
            a = m + 1
        m = (a + b) // 2
    return a


l = [0, 2, 3, 5, 10, 100, 340]
print(recherche_dichotomique(100, l))  # affiche 5

# question 2


def recherche_dichotomique(element, liste_triee):
    a = 0
    b = len(liste_triee) - 1
    m = (a + b) // 2
    while a < b:
        if liste_triee[m] == element:
            return m
        elif liste_triee[m] > element:
            b = m - 1
        else:
            a = m + 1
        m = (a + b) // 2
    if liste_triee[a] != element:
        return -1       # ligne ajoutée
    else:
        return m


l = [0, 2, 4, 6, 8, 100, 1000]
for i in l:
    print(i, recherche_dichotomique(i, l))
    # vérifier qu'on retrouve tous les éléments existant
print(recherche_dichotomique(1, l))   # affiche -1


# question 3

def deux_recherches(element, liste1, liste2):
    return recherche_dichotomique(element, liste1),  \
        recherche_dichotomique(element, liste2)


l1 = [0, 2, 4, 6, 8, 100, 1000]
l2 = [1200, 3000, 4000, 5555]
print(deux_recherches(100, l1, l2))    # affiche (5,-1)

# question 4

"""
Les logarithmes sont en base 2.

cas 1 : 1000 ln(n) + 10 (ln(n) + ln(10n)) = 1020 ln(n) + 10 ln(10) = C1
cas 2 : 1010 ln(n + 10n) = 1010 ln(n) + 1010 ln(11)                = C2
delta = C2 - C1 = -10 ln(n) + 1010 ln(11) - 10 ln(10)

Conclusion : pour n petit, le cas C1 est préférable, pour les n grands, c'est le cas 2.
"""

# question 5


def deux_recherches(element, liste1, liste2):
    if element > liste1[-1]:
        return -1, recherche_dichotomique(element, liste2)
    else:
        return recherche_dichotomique(element, liste1), -1


l1 = [0, 2, 4, 6, 8, 100, 1000]
l2 = [1200, 3000, 4000, 5555]
print(deux_recherches(100, l1, l2))    # affiche (5,-1)
