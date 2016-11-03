"""
@file
@brief edit distance
"""


def edit_distance(mot1, mot2):
    """
    Computes the edit distance between two strings.

    @param      mot1        first string
    @param      mot2        second string
    @return                 distance, path

    More alternatives are available in the following paper
    `Harry: A Tool for Measuring String Similarity <http://jmlr.org/papers/v17/rieck16a.html>`_.

    *distance* is an integer,
    *path* is a series of 2-uples of positions
    """
    dist = {(-1, -1): 0}
    pred = {(-1, -1): None}
    if len(mot1) == 0:
        for j, d in enumerate(mot2):
            dist[-1, j] = dist[-1, j - 1] + 1
            pred[-1, j] = (-1, j - 1)
            dist[j, -1] = dist[j - 1, -1] + 1
            pred[j, -1] = (j - 1, -1)
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
    try:
        while p is not None:
            chemin.append(p)
            p = pred[p]
    except KeyError as e:
        raise Exception("Issue with:\n'{0}'\n'{1}'\ndist={2}\npred={3}\np={4}".format(
            mot1, mot2, dist, pred, p)) from e
    chemin.reverse()
    return dist[len(mot1) - 1, len(mot2) - 1], chemin
