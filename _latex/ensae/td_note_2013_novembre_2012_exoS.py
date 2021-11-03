# coding:latin-1
import math

# cette fonction construit deux spirales imbriquées dans une matrice nb x nb
# le résultat est retourné sous forme de liste de listes


def construit_matrice(nb):
    mat = [[0 for x in range(0, nb)] for y in range(0, nb)]

    def pointij(nb, r, th, mat, c, phase):
        i, j = r * th * math.cos(th + phase), r * th * math.sin(th + phase)
        i, j = int(i * 100 / nb), int(j * 100 / nb)
        i, j = (i + nb) / 2, (j + nb) / 2
        if 0 <= i < nb and 0 <= j < nb:
            mat[i][j] = c
        return i, j

    r = 3.5
    t = 0
    for tinc in range(nb * 100000):
        t += 1.0 * nb / 100000
        th = t * math.pi * 2
        i, j = pointij(nb, r, th, mat, 1, 0)
        i, j = pointij(nb, r, th, mat, 1, math.pi)
        if i >= nb and j >= nb:
            break

    return mat

# cette fonction reçoit une matrice sous forme de liste de listes contenant des entiers : 0,1,2
# à chaque valeur est associée une couleur :
# 0 pour blanc, 1 pour bleu, 2 pour rouge


def dessin_matrice(matrice):
    import pylab
    colors = {1: "blue", 2: "red"}
    for i in range(0, len(matrice)):
        for j in range(0, len(matrice[i])):
            if matrice[i][j] in colors:
                pylab.plot([i - 0.5, i - 0.5, i + 0.5, i + 0.5, i - 0.5, i + 0.5, i - 0.5, i + 0.5],
                           [j - 0.5, j + 0.5, j + 0.5, j - 0.5,
                            j - 0.5, j + 0.5, j + 0.5, j - 0.5],
                           colors[matrice[i][j]])
    pylab.show()


if __name__ == "__main__":
    matrice = construit_matrice(100)
    dessin_matrice(matrice)
