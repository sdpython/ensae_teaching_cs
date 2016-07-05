import numpy as np
import copy

import random

print random.gauss(0, 1)


def combinaison():
    x = random.gauss(0, 1)
    y = random.gauss(0, 1)
    z = random.gauss(0, 1)
    x2 = x
    y2 = 3 * x + y
    z2 = -2 * x + y + 0.2 * z
    return [x2, y2, z2]

l = [combinaison() for i in range(0, 100)]


mat = np.matrix(l)

# print mat

print mat.shape
cor = mat.transpose() * mat

print cor

L, P = np.linalg.eig(cor)

print P
print L
print np.diag(L)

print P.transpose() * P
print cor * np.linalg.inv(cor)
