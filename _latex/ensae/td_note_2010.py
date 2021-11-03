# coding: latin-1
import random
import numpy


def dessin(nuage, image=None):
    """dessine un nuage de points
    @param      nuage       le nuage de points
    @param      image       si None, on affiche le nuage au travers d'une fenêtre,
                            sinon, image correspond à un nom d'image
                            sur disque dur qui contiendra le graphique final"""
    import matplotlib.pyplot as plt
    x = [p[0] for p in nuage]
    y = [p[1] for p in nuage]
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, 'o')
    if image == None:
        plt.show()
    else:
        plt.savefig(image)


def dessin_classes(nuage, classes, image=None):
    """dessine un nuage, donne des couleurs différentes
    selon que le point appartient à telle ou telle classes
    @param      nuage           nuage[i], c'est le point i
    @param      classes         classes [i] est la classe associée au point i
    @param      image           voir la fonction précédente
    """
    import matplotlib.pyplot as plt
    x = {}
    y = {}
    for i in range(0, len(nuage)):
        cl = classes[i]
        if cl not in x:
            x[cl] = []
            y[cl] = []
        x[cl].append(nuage[i][0])
        y[cl].append(nuage[i][1])
    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for cl in x:
        ax.plot(x[cl], y[cl], "+")
    if image == None:
        plt.show()
    else:
        plt.savefig(image)


def sous_nuage(nb, x, y):
    """retourne un ensemble de points tirés aléatoirement selon
    une loi normale centrée autour du point x,y
    @param      nb              nombre de points
    @param      x               abscisse du centre
    @param      y               ordonnée du centre
    @return                     une liste de points ou matrice de deux colonnes
                                - la première correspond aux abscisses,
                                - la seconde aux ordonnées
    """
    res = []
    for i in xrange(0, nb):
        xx = random.gauss(0, 1)
        yy = random.gauss(0, 1)
        res.append([x + xx, y + yy])
    return res


def n_sous_nuages(nb_class, nb_point):
    """crée un nuage de points aléatoires
    @param      nb_class        nombre de sous nuages
    @param      nb_point        nombre de points dans chaque sous nuage
    @return                     une liste de points ou matrice de deux colonnes
                                - la première correspond aux abscisses,
                                - la seconde aux ordonnées"""
    res = []
    for c in xrange(0, nb_class):
        x = random.gauss(0, 1) * 5
        y = random.gauss(0, 1) * 5
        res += sous_nuage(nb_point, x, y)
    return res


def random_class(nuage, n):
    """choisis aléatoirement un entier pour chaque point du nuage
    @param      nuage           un nuage de points (matrice de deux colonnes)
    @param      n               nombre de classes
    @return                     une liste d'entiers
    """
    res = []
    for p in nuage:
        c = random.randint(0, n - 1)
        res.append(c)
    return res


def proche_barycentre(point, barycentres):
    """détermine le barycentre le plus d'un point
    @param      point           liste de 2 réels : [x,y]
    @param      barycentres     liste de n points = matrice de deux colonnes,
                                chaque ligne correspond à un barycentre
    @return                     un entier qui correspond à l'index
                                du barycentre le plus proche"""
    dmax = 1e6
    for i in range(0, len(barycentres)):
        b = barycentres[i]
        dx = point[0] - b[0]
        dy = point[1] - b[1]
        d = (dx**2 + dy**2) ** 0.5
        if d < dmax:
            dmax = d
            m = i
    return m


def association_barycentre(points, barycentres):
    """détermine pour chaque point le barycentre le plus proche
    @param      points          nuage (matrice de deux colonnes)
    @param      barycentres     c'est aussi une matrice de deux colonnes mais
                                avec moins de lignes
    @return                     liste d'entiers, chaque entier
                                correspond à la classe du point points[i],
                                c'est-à-dire l'index du barycentre le plus proche
                                ici:
                                point:      points [i]
                                classe:     res[i]
                                barycentre: barycentres[ res[i] ]
    """
    res = []
    for p in nuage:
        m = proche_barycentre(p, barycentres)
        res.append(m)
    return res


def barycentre_classe(points, classes, numero_class):
    """calcule le barycentre d'une classe
    @param      points          ensemble de points (matrice de deux colonnes)
    @param      classes         liste d'entiers de même longueur,
                                chaque élément classes[i] est la classe de point[i]
    @param      numero_class    classe pour laquelle on doit calculer le barycentre
    @return                     résultat barycentre x,y

    dans cette fonction, on doit calculer le barycentre d'une classe
    c'est-à-dire le barycentre des points points[i]
    pour lesquelles classes[i] == numero_class
    """
    mx, my = 0.0, 0.0
    nb = 0
    for i in range(0, len(points)):
        p = points[i]
        c = classes[i]
        if c != numero_class:
            continue
        nb += 1
        mx += p[0]
        my += p[1]
    return mx / nb, my / nb


def tous_barycentres(points, classes):
    """calcule les barycentres pour toutes les classes
    @param      points      points, nuage, matrice de deux colonnes
    @param      classes     liste d'entiers
    @return                 liste de barycentre = matrice de deux colonnes
    """
    mx = max(classes) + 1
    barycentre = []
    for m in range(0, mx):
        b = barycentre_classe(points, classes, m)
        barycentre.append(b)
    return barycentre


def numpy_tous_barycentres(points, classes):
    """écriture de barycentre_classe et tous_barycentres
    en une seule fonction avec numpy
    """
    nbcl = max(classes) + 1
    mat = numpy.matrix(points)
    vec = numpy.array(classes)
    clas = numpy.zeros((len(points), nbcl))
    for i in range(0, nbcl):
        clas[vec == i, i] = 1.0
    nb = clas.sum(axis=0)
    for i in range(0, nbcl):
        clas[vec == i, i] = 1.0 / nb[i]
    ba = mat.transpose() * clas
    ba = ba.transpose()
    ba = ba.tolist()
    barycentre = [b for b in ba]
    return barycentre


def numpy_tous_barycentres2(points, classes):
    """écriture de barycentre_classe et tous_barycentres
    en une seule fonction avec numpy
    """
    nbcl = max(classes) + 1
    mat = numpy.matrix(points)
    matt = mat.transpose()
    matcl = numpy.matrix(classes).transpose()
    barycentre = []
    for c in xrange(0, nbcl):
        w = numpy.matrix(matcl)
        w[matcl == c] = 1
        w[matcl != c] = 0
        wt = w.transpose()
        r = matt * w
        n = wt * w
        r /= n[0, 0]
        barycentre += [[r[0, 0], r[1, 0]]]

    return barycentre


def nuees_dynamiques(points, nbcl):
    """algorithme des nuées dynamiques
    @param      points          ensemble points = matrice de deux colonnes
    @param      nbcl            nombre de classes demandées
    @return                     un tableau incluant la liste d'entiers
    """
    classes = random_class(points, nbcl)

    # on a le choix entre la version sans numpy
    for i in range(0, 10):
        print "iteration", i, max(classes) + 1
        barycentres = tous_barycentres(points, classes)        # ou l'un
        classes = association_barycentre(points, barycentres)
    cl1 = classes

    # ou la première version avec numpy
    for i in range(0, 10):
        print "iteration", i, max(classes) + 1
        barycentres = numpy_tous_barycentres(points, classes)  # ou l'autre
        classes = association_barycentre(points, barycentres)
    cl2 = classes

    # ou la seconde version avec numpy
    for i in range(0, 10):
        print "iteration", i, max(classes) + 1
        barycentres = numpy_tous_barycentres2(points, classes)  # ou l'autre
        classes = association_barycentre(points, barycentres)
    cl3 = classes

    # on doit trouver cl1 == cl2 == cl3
    if cl1 != cl2 or cl1 != cl3:
        print "erreur de calculs dans l'une des trois fonctions"
    return classes


# début du programme : on construit un nuage de points
nuage = n_sous_nuages(3, 50)
# on appelle l'algorithme
classes = nuees_dynamiques(nuage, 3)
# on dessine le résultat
dessin_classes(nuage, classes)
