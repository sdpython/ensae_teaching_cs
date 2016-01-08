"""
@file
@brief edit distance
"""


def edit_distance(mot1, mot2):
    """
    computes the edit distance between two strings

    @param      mot1        first string
    @param      mot2        second string
    @return                 distance, path

    *distance* is an integer,
    *path* is a series of 2-uples of positions
    """
    dist = {(-1, -1): 0}
    pred = {(-1, -1):  None}
    for i, c in enumerate(mot1):
        dist[i, -1] = dist[i - 1, -1] + 1
        pred[i, -1] = (i - 1, -1)
        dist[-1, i] = dist[-1, i - 1] + 1
        pred[-1, i] = (-1, i - 1)
        for j, d in enumerate(mot2):
            opt = []
            if (i - 1, j) in dist:
                x = dist[i - 1, j] + 1
                opt.append((x, (i - 1, j)))
            if (i, j - 1) in dist:
                x = dist[i, j - 1] + 1
                opt.append((x, (i, j - 1)))
            if (i - 1, j - 1) in dist:
                x = dist[i - 1, j - 1] + (1 if c != d else 0)
                opt.append((x, (i - 1, j - 1)))
            mi = min(opt)
            dist[i, j] = mi[0]
            pred[i, j] = mi[1]

    p = (len(mot1) - 1, len(mot2) - 1)
    chemin = []
    while p is not None:
        chemin.append(p)
        p = pred[p]
    chemin.reverse()
    return dist[len(mot1) - 1, len(mot2) - 1], chemin
