"""
@file
@brief This file proposes a simple algorithm to solve a Sudoku. It finds the first possible solution.
"""


def chiffre_barre_ligne(s, r, i):
    """
    Look into every number in line *i*,
    if the number in column *k* ``s[i][k]`` is not null,

    @param      s       current state of the sudoku
    @param      r       array ``r[n] == 0`` means number *n+1* is already taken on this line
    @param      i       line index (0 based)
    """
    for k in range(0, 9):
        if s[i][k] > 0:
            r[s[i][k] - 1] = 0


def chiffre_barre_colonne(s, r, j):
    """
    Look into every number in column *j*,
    if the number in column *k* ``s[i][k]`` is not null,

    @param      s       current state of the sudoku
    @param      r       array ``r[n] == 0`` means number *n+1* is already taken on this column
    @param      j       column index (0 based)
    """
    for k in range(0, 9):
        if s[k][j] > 0:
            r[s[k][j] - 1] = 0


def chiffre_barre_carre(s, r, i, j):
    """
    Look into every number in sub square *i, j*,
    if a number in it ``s[i][k]`` is not null,

    @param      s       current state of the sudoku
    @param      r       array ``r[n] == 0`` means number *n+1* is already taken on this sub square
    @param      i       sub square are indexed by :math:`(i, j) \\in \\{0, 1, 2\\}^2` (0 based)
    @param      j       see parameter *i*
    """
    a = i // 3 * 3
    b = j // 3 * 3
    for k in range(a, a + 3):
        for lb in range(b, b + 3):
            if s[k][lb] > 0:
                r[s[k][lb] - 1] = 0


def nombre_possible(s, i, j):
    """
    tells for a particular position the list of possible number

    @param      s       current state of the sudoku
    @param      i       line index (0 based)
    @param      j       column index (0 based)
    @return             9-element array, 0: not possible, 1: possible at position *(i, j)*
    """
    r = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    chiffre_barre_ligne(s, r, i)
    chiffre_barre_colonne(s, r, j)
    chiffre_barre_carre(s, r, i, j)
    return r


def meilleure_case(s):
    """
    look over all empty place and pick the one with the least possible options

    @param      s       current state of the sudoku
    @return             *(i,j,r)*, *(i,j)* is the best position,
                        *r* the list of possible numbers
    """
    dmin = 10
    imin = jmin = -1
    rmin = []
    for i in range(0, 9):
        for j in range(0, 9):
            if s[i][j] == 0:
                r = nombre_possible(s, i, j)
                d = sum(r)
                if d < dmin:
                    dmin = d
                    imin = i
                    jmin = j
                    rmin = r
    return imin, jmin, rmin


def resolution_sudoku(s):
    """
    Solves the Sudoku.

    @param      s       sudoku (0 for empty case)
    @return             0 for impossible, 1 for possible, then *s* contains the solution

    The algorithm is the following:

    #. Find the position of a zero element (no number yet) with the smallest number of options
    #. If there is at least one possible option, try the first one, go to step 1
    #. If not, the Sudoku cannot be solved, go back to last list of multiple options and try the next one.

    Example::

        s = [[0, 0, 0, 3, 0, 0, 8, 0, 0],
             [0, 0, 7, 9, 0, 8, 0, 0, 5],
             [0, 0, 0, 2, 0, 4, 1, 0, 0],
             [0, 9, 0, 8, 1, 0, 0, 4, 7],
             [0, 4, 0, 0, 0, 0, 0, 0, 6],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 5, 0, 2, 0],
             [5, 3, 4, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 7, 0, 0, 0, 0, 0]]

        resolution_sudoku(s)

        for i in range(0, 9):
        print(s[i])
    """
    imin, jmin, rmin = meilleure_case(s)
    if imin == -1:
        return "jackpot"
    d = sum(rmin)
    if d == 1:
        p = rmin.index(1)
        s[imin][jmin] = p + 1
        # s modifie ",imin,jmin,p+1
        a = resolution_sudoku(s)
        if a == 0:
            s[imin][jmin] = 0
            return 0
        else:
            return 1
    elif d == 0:
        # on s'arrete
        return 0
    elif d > 1:
        # on continue
        for n in range(0, 9):
            if rmin[n] == 1:
                s[imin][jmin] = n + 1
                a = resolution_sudoku(s)
                if a == 0:
                    s[imin][jmin] = 0
                else:
                    return 1
        return 0
    else:
        raise RuntimeError("Should not happend.")


def sudoku2str(su):
    """
    Converts a sudoku into a string.

    @param      su      sudoku
    @return              string
    """
    s = ""
    for i in range(0, len(su)):
        if i % 3 == 0:
            s += "-" * 35
            s += "\n"
        for j in range(0, len(su[i])):
            if j % 3 == 0:
                s += " | "
            if su[i][j] > 0:
                s += str(su[i][j]) + " "
            else:
                s += "_ "
        s += " |\n"
    s += "-" * 35
    s += "\n"
    return s
