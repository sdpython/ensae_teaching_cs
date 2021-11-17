# coding: latin-1
# question 1
def lit_fichier(file):
    f = open(file, "r")
    mot = []
    for l in f:
        mot.append(l.replace("\n", ""))
    f.close()
    return mot


mot = lit_fichier("td_note_texte.txt")
print mot

# question 2


def est_trie(mot):
    for i in range(1, len(mot)):
        if mot[i - 1] > mot[i]:
            return False
    return True


tri = est_trie(mot)
print "liste tri�e ", tri

# question 3


def cherche(mot, m):
    for i in range(0, len(mot)):
        if mot[i] == m:
            return i
    return -1


print "mot ACHATS ", cherche(mot, "ACHATS")
print "mot achats ", cherche(mot, "achats")

# question 4
un = cherche(mot, "UN")
deux = cherche(mot, "DEUX")
print "recherche normale ", un, deux
print "nombre d'it�rations", un + deux

# question 5, 6, nbun et nbdeux contiennent le nombre de comparaisons


def cherche_dicho(mot, m):
    a = 0
    b = len(mot) - 1
    nb = 0
    while a < b:
        nb += 1
        p = (a + b) / 2
        if mot[p] == m:
            return p, nb
        elif mot[p] > m:
            b = p - 1
        else:
            a = p + 1
    return -1, nb


un, nbun = cherche_dicho(mot, "UN")
deux, nbdeux = cherche_dicho(mot, "DEUX")
print "recherche dichotomique ", un, deux
print "nombre d'it�rations ", nbun + nbdeux

# question 7
"""
Lors d'une recherche simple, au pire, l'�l�ment cherche sera
en derni�re position, ce qui signifie n it�rations pour le trouver.
Le co�t de la recherche simple est en O(n).
"""

# question 8
"""
Lors de la recherche dichotomique, � chaque it�ration, on divise par deux
l'ensemble dans lequel la recherche s'effectue,
au d�part n, puis n/2, puis n/4 jusqu'� ce que n/2^k soit nul
c'est-�-dire k = partie enti�re de ln n / ln 2
il y a au plus k it�rations donc le co�t de l'algorithme est en O (ln n).
"""
