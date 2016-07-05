from load_distance_matrix import *

matrice_line = charge_donnees()
mat = conversion_en_dictionnaire(matrice_line)

villes = [_[0] for _ in mat]
unique = {}
for v in villes:
    unique[v] = 0
print len(unique)


def misajour(unique, mat):
    mm = 0
    for v in unique:
        for vv in unique:
            dxy = mat.get((v, vv), 1e9)
            # if dxy == 1e9 : continue
            for k in unique:
                dxk = mat.get((v, k), 1e9)
                dyk = mat.get((vv, k), 1e9)
                s = dxk + dyk
                if s < dxy:
                    mat[v, vv] = s
                    mat[vv, v] = s
                    mm += 1
    return mm


def somme_distance(mat):
    return sum(mat.values())


print len(mat)
for i in xrange(0, 302):
    print i, "*", misajour(unique, mat), " nb ", len(mat), " sum ", somme_distance(mat)
