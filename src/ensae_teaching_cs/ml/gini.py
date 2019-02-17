"""
@file
@brief Functions about the `Gini coefficient <https://en.wikipedia.org/wiki/Gini_coefficient>`_.
"""
import numpy


def gini(Y, X=None):
    """
    Computes the
    `Gini coefficients <https://en.wikipedia.org/wiki/Gini_coefficient>`_.

    @param  Y           Y values (or revenues)
    @param  X           None for a uniform population or not None for already order value.
    @return             a curve ``(x, Gini(x))``
    """
    n = len(Y)
    couples = numpy.empty((n, 2))
    if X is None:
        couples[:, 0] = 1
    else:
        couples[:, 0] = X
    couples[:, 1] = Y
    couples = couples
    couples = numpy.cumsum(couples, axis=0)
    couples[:, 0] /= max(couples[n - 1, 0], 1e-7)
    couples[:, 1] /= max(couples[n - 1, 1], 1e-7)

    gini = 0.
    n = couples.shape[0]

    for i in range(0, n):
        dx = couples[i, 0] - couples[i - 1, 0]
        y = couples[i - 1, 1] + couples[i, 1]
        gini += dx * y

    return (1. - gini) / 2
