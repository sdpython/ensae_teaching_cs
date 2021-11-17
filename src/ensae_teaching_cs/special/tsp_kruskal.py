# -*- coding: utf-8 -*-
"""
@file
@brief Implémente un algorithme qui cherche le plus court chemin passant
par tous les noeuds d'un graphe (TSP). Applique un algorithme de Kruskal
puis cherche à améliorer le chemin localement.
Voir :ref:`l-tsp_kruskal`. La fonction principale est
@see fn tsp_kruskal_algorithm.
"""
import functools
import random
import math
import os
from pyquickhelper.loghelper import noLOG
from .tsp_bresenham import draw_line
from ..helpers.pygame_helper import wait_event, empty_main_loop


def construit_ville(n, x=1000, y=700):
    """
    Tire aléatoirement *n* villes dans un carrée ``x * y``, on choisit
    ces villes de sortent qu'elles ne soient pas trop proches."""
    # deux villes ne pourront pas être plus proches que mind
    mind = math.sqrt(x * x + y * y) / (n * 0.75)
    # liste vide
    lv = []
    while n > 0:
        # on tire aléatoirement les coordonnées d'une ville
        xx = x * random.random()
        yy = y * random.random()
        # on vérifie qu'elle n'est pas trop proche d'aucune autre ville
        ajout = True
        for t in lv:
            d1 = t[0] - xx
            d2 = t[1] - yy
            d = math.sqrt(d1 * d1 + d2 * d2)
            if d < mind:
                ajout = False  # ville trop proche
        # si la ville n'est pas trop proche des autres, on l'ajoute à la liste
        if ajout:
            lv.append((xx, yy))
            n -= 1  # une ville en moins à choisir
    return lv


def distance_euclidian(p1, p2):
    """
    Calcule la distance entre deux villes.
    """
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(x * x + y * y)


def vecteur_points(p1, p2):
    """
    Retourne le vecteur entre les points *p1* et *p2*.
    """
    return (p2[0] - p1[0], p2[1] - p1[1])


def vecteur_norme(vec):
    """
    Retourne la norme d'un vecteur.
    """
    return math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])


def vecteur_cosinus(vec1, vec2):
    """
    Retourne le cosinus entre deux vecteurs,
    utilise le produit scalaire.
    """
    norm1 = vecteur_norme(vec1)
    norm2 = vecteur_norme(vec2)
    if norm1 == 0:
        return 1
    if norm2 == 0:
        return 1
    scal = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    return scal / (norm1 * norm2)


def vecteur_sinus(vec1, vec2):
    """
    Retourne le sinus entre deux vecteurs,
    utilise le produit vectoriel.
    """
    norm1 = vecteur_norme(vec1)
    norm2 = vecteur_norme(vec2)
    if norm1 == 0:
        return 0
    if norm2 == 0:
        return 0
    scal = vec1[0] * vec2[1] - vec1[1] * vec2[0]
    return scal / (norm1 * norm2)


def oppose_vecteur(vec):
    """
    retourne le vecteur opposé.
    """
    return (-vec[0], -vec[1])


def repartition_zone(villes, zone_taille, ask_zone=False):
    """
    Répartit les villes en zones, retourne les villes rangées par zones,
    chaque éléments zones [z][k] contient :

    - les coordonnées de la ville
    - ses coordonnées en zone, (zx, zy)
    - son indice dans la liste villes

    La fonction retourne également le nombre de zones
    selon l'axe des abscisses et l'axe des ordonnées,
    retourne aussi le nombre de zones, si *ask_zone* est True,
    retourne un paramètre supplémentaire : *zone*.
    """
    mx = min(v[0] for v in villes)
    my = min(v[1] for v in villes)
    X = max((v[0] - mx) / zone_taille for v in villes)
    Y = max((v[1] - my) / zone_taille for v in villes)
    X = int(X) + 1
    Y = int(Y) + 1

    # attribution des zones
    zone = []
    Zmax = 0
    for i in range(0, len(villes)):
        v = villes[i]
        x = int((v[0] - mx) / zone_taille)
        y = int((v[1] - my) / zone_taille)
        z = int(y * X + x)
        Zmax = max(z, Zmax)
        zone.append((z, v, (x, y), i))

    # rangement par zone
    Zmax += 1
    zones = [[] for i in range(0, Zmax)]
    for z in zone:
        zones[z[0]].append((z[1], z[2], z[3]))

    if ask_zone:
        return zones, X, Y, mx, my, Zmax, zone
    return zones, X, Y, mx, my, Zmax


def voisinage_zone(z, Zmax, X, Y):
    """
    Retourne la liste des voisins d'une zone *z*
    sachant qu'il y a *X* zones sur l'axe des abscisses
    et *Y* zones sur l'axe des ordonnées,
    *Zmax* est le nombre de zones,
    inclus *z* dans cette liste.
    """
    x = z % X
    y = z // X
    voisin_ = [z]
    if x > 0:
        voisin_.append(z - 1)
    if x < X:
        voisin_.append(z + 1)
    if y > 0:
        voisin_.append(z - X)
    if y < Y:
        voisin_.append(z + X)
    if x > 0 and y > 0:
        voisin_.append(z - 1 - X)
    if x > 0 and y < Y:
        voisin_.append(z - 1 + X)
    if x < X and y > 0:
        voisin_.append(z + 1 - X)
    if x < X and y < Y:
        voisin_.append(z + 1 + X)
    voisin = [int(i) for i in voisin_ if Zmax > i >= 0]
    return voisin


def arbre_poids_minimal(villes, zone_taille, distance):
    """
    Construit l'arbre de poids minimal, retourne une liste de
    listes, chaque sous-liste associée à une ville contient la liste des ses voisins,
    *zone_taille* permet de découper l'image en zones,
    les distances ne seront calculées que si
    deux éléments sont dans la même zone ou dans une zone voisine.

    @param      villes          list of tuples (tuple = coordinates)
    @param      zone_taille     @see fn repartition_zone
    @param      distance        distance function which returns the distance between two
                                elements
    @return                     list of lists: each sublist *r[i]* contains the indexes of
                                neighbors of node *i* so that the whole graph is
                                only one connected component
    """

    def tri_distance(u, v):
        if u[2] < v[2]:
            return -1
        elif u[2] > v[2]:
            return 1
        else:
            return 0

    rz = repartition_zone(villes, zone_taille=zone_taille)
    zones, X, Y, mx, my, Zmax = rz[:6]

    # calcul des distances
    li = []
    for z in range(0, len(zones)):
        voisin = voisinage_zone(z, Zmax, X, Y)
        for v in zones[z]:
            for zz in voisin:
                for u in zones[zz]:
                    d = distance(v[0], u[0])
                    li.append((v[2], u[2], d))

    # tri
    li = list(sorted(li, key=functools.cmp_to_key(tri_distance)))

    # nombre de composantes connexes
    nb_comp = len(villes)

    # indice de la composante d'une ville
    num_comp = [i for i in range(0, len(villes))]

    # liste des voisins pour chaque ville
    arbre = [[] for i in range(0, len(villes))]

    # liste des villes par composante connexe
    list_comp = [[i] for i in range(0, len(villes))]

    while nb_comp > 1:
        iii = 0
        for c in li:
            iii += 1
            i, j = c[0], c[1]
            if num_comp[i] != num_comp[j]:
                # on relie les villes i et j car elles appartiennent
                # à des composantes connexes différentes
                arbre[i].append(j)        # i est voisine de j
                arbre[j].append(i)        # j est voisine de i
                cl = num_comp[i]           # composante connexe restante
                # composante connexe à agréger à la précédente
                ki = num_comp[j]
                for k in list_comp[ki]:
                    num_comp[k] = cl
                    list_comp[cl].append(k)
                list_comp[ki] = []
                nb_comp -= 1                # une composante connexe en moins

                if nb_comp <= 1:
                    break  # il n'y a plus qu'une seule composante connexe, inutile de continuer

        if nb_comp > 1:
            # it usually means that zone_taille is too small and some edges
            # we find lost connected components
            # so for these, assuming they are not too many
            # we look for the closest point outside the connected component
            first_count = min((len(l), i)
                              for i, l in enumerate(list_comp) if len(l) > 0)
            comp = first_count[1]
            city = list_comp[comp][random.randint(0, len(list_comp[comp]) - 1)]
            # city is not the best choice, just a random one
            dist = min((distance(villes[city], v), i) for i, v in enumerate(villes)
                       if city != i and num_comp[i] != num_comp[city])
            li = [(city, dist[1])]

    return dict(arbre=arbre, X=X, Y=Y, mx=mx, my=my, Zmax=Zmax)


def circuit_eulerien(villes, arbre, screen, pygame, fLOG):
    """
    Définit un circuit eulérien, villes contient la liste des villes,
    tandis que arbre est une liste de listes, ``arbre[i]`` est la liste des villes
    connectées à la ville *i*,
    on suppose que arbre est un graphe de poids minimal non orienté,
    l'algorithme ne marche pas s'il existe des villes confondues,
    un circuit eulérien passe par tous les arêtes une et une seule fois.
    """

    # on choisit une ville qui est une extrémité et parmi celle-là on la
    # choisit au hasard
    has = []
    for i in range(0, len(villes)):
        n = len(arbre[i])
        if n == 1:
            has.append(i)

    bm = random.randint(0, len(has) - 1)
    bm = has[bm]

    # vecteur, le circuit eulérien contient
    # nécessairement 2 * len (villes) noeuds puisque c'est
    # le graphe eulérien d'un arbre de poids minimal non orienté
    vec = (1, 1)
    chemin = [bm]
    done = set()
    done.add(bm)
    iter = []
    while len(done) < len(villes):
        iter.append(len(done))
        if len(iter) % 1000 == 0:
            fLOG("  circuit_eulerien: iter={0} len(done)={1} len(villes)={2}".format(
                len(iter), len(done), len(villes)))
            if len(done) == iter[-1000]:
                # there is apparently something wrong
                break
        v = villes[bm]
        ma = - math.pi - 1
        bvec = vec
        opvec = oppose_vecteur(vec)
        bl = None
        for k in range(0, len(arbre[bm])):
            la = arbre[bm][k]
            vec2 = vecteur_points(v, villes[la])
            if vec2 == (0.0, 0.0):
                # same point, we keep the same direction
                if la not in done:
                    bl = la
                    bvec = vec2
                    # no need to go further if the points are equal
                    break
                # we skip
                continue
            if opvec == vec2:
                angle = -math.pi
            else:
                cos = vecteur_cosinus(vec, vec2)
                sin = vecteur_sinus(vec, vec2)
                angle = math.atan2(sin, cos)
            if angle > ma:
                ma = angle
                bl = la
                bvec = vec2

        if bl is not None:
            if bl not in done:
                chemin.append(bl)
                done.add(bl)
            bm = bl
            if bvec != (0.0, 0.0):
                vec = bvec
        else:
            # something is wrong (it might an issue with duplicated points)
            rows = []
            for i, p in enumerate(villes):
                rows.append("p{0}: {1},{2}".format(i, p[0], p[1]))
            for i, c in enumerate(chemin):
                rows.append("c{0}: i={1} -> {2},{3}".format(i,
                                                            c, villes[c][0], villes[c][1]))
            rows.append("bm={0} ma={1} bvec={2} vec={3} bl={4}".format(
                bm, ma, vec2, vec, bl))
            rows.append("arbre[{0}]={1}".format(bm, arbre[bm]))
            rows.append("arbre[{0}]={1}".format(
                arbre[bm][0], arbre[arbre[bm][0]]))
            mes = "\n".join(rows)
            raise Exception("this case should not happen\n" + mes)

    if len(done) < len(villes):
        # something is wrong (it might an issue with duplicated points)
        rows = []
        for i, p in enumerate(villes):
            rows.append("p{0}: {1},{2}".format(i, p[0], p[1]))
        for i, c in enumerate(chemin):
            rows.append("c{0}: i={1} -> {2},{3}".format(i,
                                                        c, villes[c][0], villes[c][1]))
        rows.append("bm={0} ma={1} bvec={2} vec={3} bl={4}".format(
            bm, ma, vec2, vec, bl))
        mes = "\n".join(rows)
        raise Exception("circuit_eulerien cannot give a path:\n" + mes)

    return chemin


def circuit_hamiltonien(chemin):
    """
    Extrait un circuit hamiltonien depuis un circuit eulérien,
    passe par tous les sommets une et une seule fois.
    """
    nb = max(chemin) + 1
    res = []
    coche = [False for i in range(0, nb)]
    for c in chemin:
        if coche[c]:
            continue
        res.append(c)
        coche[c] = True
    return res


def equation_droite(p1, p2):
    """
    retourne l'équation d'une droite passant par p1 et p2,
    ax + by + c = 0, retourne les coefficients a,b,c
    """
    vec = vecteur_points(p1, p2)
    a = vec[1]
    b = - vec[0]
    c = - a * p1[0] - b * p1[1]
    return a, b, c


def evaluation_droite(a, b, c, p):
    """
    L'équation d'une droite est : ``ax + by + c``, retourne la valeur
    de cette expression au point *p*.
    """
    return a * p[0] + b * p[1] + c


def intersection_segment(p1, p2, p3, p4):
    """
    Dit si les segments *[p1 p2]* et *[p3 p4]* ont une intersection,
    ne retourne pas l'intersection.
    """
    # équation de la droite (p1 p2)
    a1, b1, c1 = equation_droite(p1, p2)
    a2, b2, c2 = equation_droite(p3, p4)
    s1 = evaluation_droite(a2, b2, c2, p1)
    s2 = evaluation_droite(a2, b2, c2, p2)
    s3 = evaluation_droite(a1, b1, c1, p3)
    s4 = evaluation_droite(a1, b1, c1, p4)
    return s1 * s2 <= 0 and s3 * s4 <= 0


def longueur_chemin(chemin, distance):
    """
    Retourne la longueur d'un chemin.
    """
    s = 0
    nb = len(chemin)
    for i in range(0, nb):
        s += distance(chemin[i], chemin[(i + 1) % nb])
    return s


def retournement_essai(chemin, i, j, negligeable=1e-5, distance=None):
    """
    Dit s'il est judicieux de parcourir le chemin entre les sommets *i* et *j*
    en sens inverse, si c'est judicieux, change le chemin et retourne True,
    sinon, retourne False,
    si *j < i*, alors la partie à inverser est
    *i*, *i+1*, *i+2*, ..., *len(chemin)*,
    *-1*, *0*, *1*, ..., *j*.
    """

    nb = len(chemin)
    if i == j:
        return False
    if j - i == -1:
        return False
    if j - i - nb == -1:
        return False

    ia = (i - 1 + nb) % nb
    ja = (j + 1) % nb
    # arcs enlevés
    d_ia_i = distance(chemin[ia], chemin[i])
    d_j_ja = distance(chemin[j], chemin[ja])
    # arcs ajoutés
    d_ia_j = distance(chemin[ia], chemin[j])
    d_i_ja = distance(chemin[i], chemin[ja])
    # amélioration ?
    d = d_ia_j + d_i_ja - d_j_ja - d_ia_i
    if d >= -negligeable:
        return False

    # si amélioration, il faut retourner le chemin entre les indices i et j
    jp = j
    if jp < i:
        jp = j + nb
    ip = i

    while ip < jp:
        i = ip % nb
        j = jp % nb
        ech = chemin[i]
        chemin[i] = chemin[j]
        chemin[j] = ech
        ip = ip + 1
        jp = jp - 1

    return True


def retournement(chemin, taille, fLOG, distance):
    """
    Amélioration du chemin par un algorithme simple,
    utilise des retournements de taille au plus <taille>,
    retourne le nombre de modifications.
    """

    # traitement des petits retournements
    nb = len(chemin)
    nb_change = 1
    nbtout = 0
    retour = {}
    while nb_change > 0:
        nb_change = 0
        for t in range(1, taille + 1):
            retour[t] = 0
            for i in range(0, nb):
                j = (i + t) % nb
                b = retournement_essai(chemin, i, j, distance=distance)
                if b:
                    retour[t] += 1
                    nb_change += 1
        nbtout += nb_change
    fLOG("nombre de retournements %d longueur : \t %10.0f --- \t"
         % (nbtout, longueur_chemin(chemin, distance)), " --- : ", retour)
    return nbtout


def echange_position_essai(chemin, a, b, x, inversion, negligeable=1e-5, distance=None):
    """
    Echange la place des villes ka et kb pour les placer entre les villes *i* et *i+1*,
    si inversion est True, on inverse également le chemin inséré, si inversion est False,
    on ne l'inverse pas,
    si cela améliore, déplace les villes et retourne True, sinon, retourne False.
    """

    nb = len(chemin)
    xa = (x + 1) % nb
    ka = (a - 1 + nb) % nb
    kb = (b + 1) % nb

    if not inversion:

        if x == ka:
            return False
        if x == kb:
            return False
        if xa == ka:
            return False
        if b < a:
            if a <= x <= b + nb:
                return False
        elif a <= x <= b:
            return False
        if b < a:
            if a <= x + nb <= b + nb:
                return False
        elif a <= x + nb <= b:
            return False

        # arcs enlevés
        d_x_xa = distance(chemin[x], chemin[xa])
        d_ka_a = distance(chemin[ka], chemin[a])
        d_b_kb = distance(chemin[b], chemin[kb])
        # arcs ajoutés
        d_ka_kb = distance(chemin[ka], chemin[kb])
        d_x_a = distance(chemin[x], chemin[a])
        d_b_xa = distance(chemin[b], chemin[xa])

        d = d_ka_kb + d_x_a + d_b_xa - d_x_xa - d_ka_a - d_b_kb
        if d >= -negligeable:
            return False

        # villes à déplacer
        ech = []
        bp = b
        if bp < a:
            bp = b + nb
        for i in range(a, bp + 1):
            ech.append(chemin[i % nb])
        diff = bp - a + 1

        xp = x
        if xp < b:
            xp += nb

        for le in range(b + 1, xp + 1):
            ll = le % nb
            bp = (a + le - b - 1) % nb
            chemin[bp] = chemin[ll]

        for le in range(0, len(ech)):
            chemin[(x + le - diff + 1 + nb) % nb] = ech[le]

        return True

    else:

        if x == ka:
            return False
        if x == kb:
            return False
        if xa == ka:
            return False
        if b < a:
            if a <= x <= b + nb:
                return False
        elif a <= x <= b:
            return False
        if b < a:
            if a <= x + nb <= b + nb:
                return False
        elif a <= x + nb <= b:
            return False

        # arcs enlevés
        d_x_xa = distance(chemin[x], chemin[xa])
        d_ka_a = distance(chemin[ka], chemin[a])
        d_b_kb = distance(chemin[b], chemin[kb])
        # arcs ajoutés
        d_ka_kb = distance(chemin[ka], chemin[kb])
        d_x_b = distance(chemin[x], chemin[b])
        d_a_xa = distance(chemin[a], chemin[xa])

        d = d_ka_kb + d_x_b + d_a_xa - d_x_xa - d_ka_a - d_b_kb
        if d >= -negligeable:
            return False

        # villes à déplacer
        ech = []
        bp = b
        if bp < a:
            bp = b + nb
        for i in range(a, bp + 1):
            ech.append(chemin[i % nb])
        ech.reverse()
        diff = bp - a + 1

        xp = x
        if xp < b:
            xp += nb

        for le in range(b + 1, xp + 1):
            ll = le % nb
            bp = (a + le - b - 1) % nb
            chemin[bp] = chemin[ll]

        for le in range(0, len(ech)):
            chemin[(x + le - diff + 1 + nb) % nb] = ech[le]

        return True


def dessin_arete_zone(chemin, taille_zone, X, Y):
    """
    Retourne une liste de listes de listes,
    ``res[i][j]`` est une liste des arêtes passant près de la zone ``(x,y) = [i][j]``,
    si *k* in ``res[i][j]``, alors l'arête *k*, *k+1* est dans la zone *(i,j)*,
    *X* est le nombre de zones horizontalement, *Y* est le nombre de zones verticalement,
    *taille_zone* est la longueur du côté du carré d'une zone.
    """
    res = [[[] for j in range(0, Y + 1)] for i in range(0, X + 1)]
    nb = len(chemin)
    mx = min(_[0] for _ in chemin)
    my = min(_[1] for _ in chemin)
    for i in range(0, nb):
        a = chemin[i]
        b = chemin[(i + 1) % nb]
        x1, x2 = int(
            (a[0] - mx) // taille_zone), int((b[0] - mx) // taille_zone)
        y1, y2 = int(
            (a[1] - my) // taille_zone), int((b[1] - my) // taille_zone)
        line = draw_line(x1, y1, x2, y2)
        for x, y in line:
            res[x][y].append(i)
    return res


def voisinage_zone_xy(x, y, X, Y):
    """
    Retourne la liste des voisins d'une zone *(x,y)*
    sachant qu'il y a *X* zones sur l'axe des abscisses
    et *Y* zones sur l'axe des ordonnées,
    inclus *z* dans cette liste
    """
    voisin = [(x, y)]
    if x > 0:
        voisin.append((x - 1, y))
    if x < X - 1:
        voisin.append((x + 1, y))
    if y > 0:
        voisin.append((x, y - 1))
    if y < Y - 1:
        voisin.append((x, y + 1))
    if x > 0 and y > 0:
        voisin.append((x - 1, y - 1))
    if x > 0 and y < Y - 1:
        voisin.append((x - 1, y + 1))
    if x < X - 1 and y > 0:
        voisin.append((x + 1, y - 1))
    if x < X - 1 and y < Y - 1:
        voisin.append((x + 1, y + 1))
    return voisin


def echange_position(chemin, taille, taille_zone, X, Y, grande=0.5, fLOG=None, distance=None):
    """
    Regarde si on ne peut pas déplacer un segment de longueur taille
    pour supprimer les arêtes les plus longues,
    au maximum <grande> longues arêtes,
    retourne le nombre de changement effectués,
    *X* est le nombre de zones horizontalement,
    *Y* est le nombre de zones verticalement,
    *taille_zone* est la longueur d'un côté du carré d'une zone.
    """

    nb = len(chemin)

    def tri_arete(x, y):
        """pour trier la liste l par ordre décroissant"""
        if x[2] < y[2]:
            return 1
        elif x[2] > y[2]:
            return -1
        else:
            return 0

    tmx = min(v[0] for v in chemin)
    tmy = min(v[1] for v in chemin)

    # list des arêtes triés par ordre décroissant
    la = []
    for i in range(0, nb):
        im = (i + 1) % nb
        la.append((i, im, distance(chemin[i], chemin[im])))
    la = list(sorted(la, key=functools.cmp_to_key(tri_arete)))

    # zone associée à chaque arête
    zone = dessin_arete_zone(chemin, taille_zone, X, Y)

    dseuil = la[int(nb * grande)][2]
    nbtout = 0
    nb_change = 0
    iarete = 0
    retour = {}
    for t in range(1, taille + 1):
        retour[t] = 0

    while iarete < nb:
        nb_change = 0
        arete = la[iarete]
        iarete += 1
        x = arete[0]
        xm = arete[1]
        a = chemin[x]
        b = chemin[xm]
        d = distance(a, b)
        if d < dseuil:
            break    # arête trop petite

        # zone traversée par la ligne
        x1, x2 = (int((a[0] - tmx) // taille_zone),
                  int((b[0] - tmx) // taille_zone))
        y1, y2 = (int((a[1] - tmy) // taille_zone),
                  int((b[1] - tmy) // taille_zone))
        ens = draw_line(x1, y1, x2, y2)
        ville = []
        for k, l in ens:
            voisin = voisinage_zone_xy(k, l, X, Y)
            for u, v in voisin:
                ville.extend(zone[u][v])

        # on supprime les doubles
        ville.sort()
        if len(ville) == 0:
            continue
        sup = []
        mx = -1
        for v in ville:
            if v == mx:
                sup.append(v)
            mx = v
        for s in sup:
            ville.remove(s)

        # on étudie les possibilités de casser l'arête (x,xm) aux alentours des villes
        # comprise dans l'ensemble ville
        for t in range(1, taille + 1):

            for i in ville:

                # on essaye d'insérer le sous-chemin (x- t + 1 + nb)  --> x
                # au milieu de l'arête i,i+1
                b = echange_position_essai(
                    chemin, (x - t + 1 + nb) % nb, x, i, False, distance=distance)
                if b:
                    nb_change += 1
                    retour[t] += 1
                    continue

                # on essaye d'insérer le sous-chemin (xm+ t - 1)  --> xm
                # au milieu de l'arête i,i+1
                b = echange_position_essai(
                    chemin, (xm + t - 1) % nb, xm, i, False, distance=distance)
                if b:
                    nb_change += 1
                    retour[t] += 1
                    continue

                # on essaye de casser l'arête x,xm en insérant
                # le sous-chemin i --> (i+t) % nb
                b = echange_position_essai(
                    chemin, i, (i + t) % nb, x, False, distance=distance)
                if b:
                    nb_change += 1
                    retour[t] += 1
                    continue
                # idem
                b = echange_position_essai(
                    chemin, i, (i + t) % nb, x, True, distance=distance)
                if b:
                    retour[t] += 1
                    nb_change += 1
                    continue
                # idem
                b = echange_position_essai(
                    chemin, (i - t + nb) % nb, i, x, False, distance=distance)
                if b:
                    nb_change += 1
                    retour[t] += 1
                    continue
                # idem
                b = echange_position_essai(
                    chemin, (i - t + nb) % nb, i, x, True, distance=distance)
                if b:
                    retour[t] += 1
                    nb_change += 1
                    continue

        nbtout += nb_change

    fLOG("nombre de déplacements %d longueur :   \t %10.0f --- \t"
         % (nbtout, longueur_chemin(chemin, distance=distance)), " --- : ", retour)
    return nbtout


def supprime_croisement(chemin, taille_zone, X, Y, fLOG, distance=None):
    """
    Supprime les croisements d'arêtes,
    retourne le nombre de changement effectués,
    *X* est le nombre de zones horizontalement,
    *Y* est le nombre de zones verticalement,
    *taille_zone* est la longueur d'un côté du carré d'une zone
    """

    nb = len(chemin)
    tmx = min(v[0] for v in chemin)
    tmy = min(v[1] for v in chemin)

    # zone associée à chaque arête
    zone = dessin_arete_zone(chemin, taille_zone, X, Y)
    nbtout = 0

    for i in range(0, nb):
        im = (i + 1) % nb
        a = chemin[i]
        b = chemin[im]

        # zone traversée par la ligne
        x1, x2 = (int((a[0] - tmx) // taille_zone),
                  int((b[0] - tmx) // taille_zone))
        y1, y2 = (int((a[1] - tmy) // taille_zone),
                  int((b[1] - tmy) // taille_zone))
        ens = draw_line(x1, y1, x2, y2)
        ville = []
        for k, l in ens:
            voisin = voisinage_zone_xy(k, l, X, Y)
            for u, v in voisin:
                ville.extend(zone[u][v])

        # on supprime les doubles
        ville.sort()
        if len(ville) == 0:
            continue
        sup = []
        mx = -1
        for v in ville:
            if v == mx:
                sup.append(v)
            mx = v
        for s in sup:
            ville.remove(s)

        nb_change = 0
        for v in ville:
            b = retournement_essai(chemin, i, v, distance=distance)
            if b:
                nb_change += 1
                continue
            b = retournement_essai(chemin, im, v, distance=distance)
            if b:
                nb_change += 1
                continue

        nbtout += nb_change

    fLOG("nombre de croisements %d longueur :      \t %10.0f --- \t"
         % (nbtout, longueur_chemin(chemin, distance=distance)))
    return nbtout


def amelioration_chemin(chemin, taille_zone, X, Y, taille=10, screen=None,
                        fLOG=None, pygame=None, max_iter=None, images=None,
                        distance=None):
    """
    Amélioration du chemin par un algorithme simple,
    utilise des retournements de taille au plus *taille*,
    traite les arcs qui se croisent,
    traite les grands arcs, utilise un quadrillage de taille *window*,
    *X* est le nombre de zones horizontalement,
    *Y* est le nombre de zones verticalement,
    *taille_zone* est la longueur d'un côté du carré d'une zone.
    """

    white = 255, 255, 255

    if pygame is not None and images is not None:
        images.append(screen.copy())

    # première étape rapide
    iter = 0
    nb = 1
    while nb > 0 and (max_iter is None or iter < max_iter):
        nb = retournement(chemin, taille, fLOG=fLOG, distance=distance)
        if screen is not None:
            screen.fill(white)
            display_chemin(chemin, 0, screen, pygame=pygame)
            pygame.display.flip()
            if images is not None:
                images.append(screen.copy())
            empty_main_loop(pygame)
        iter += 1

    # amélioration
    nb = 1
    while nb > 0 and (max_iter is None or iter < max_iter):
        nb = retournement(chemin, taille, fLOG=fLOG, distance=distance)
        if screen is not None:
            screen.fill(white)
            display_chemin(chemin, 0, screen=screen, pygame=pygame)
            pygame.display.flip()
            if images is not None:
                images.append(screen.copy())
            empty_main_loop(pygame)
        nb += echange_position(chemin, taille // 2,
                               taille_zone, X, Y, fLOG=fLOG,
                               distance=distance)
        if screen is not None:
            screen.fill(white)
            display_chemin(chemin, 0, screen=screen, pygame=pygame)
            pygame.display.flip()
            if images is not None:
                images.append(screen.copy())
            empty_main_loop(pygame)
        nb += supprime_croisement(chemin, taille_zone,
                                  X, Y, fLOG=fLOG, distance=distance)
        if screen is not None:
            screen.fill(white)
            display_chemin(chemin, 0, screen=screen, pygame=pygame)
            pygame.display.flip()
            if images is not None:
                images.append(screen.copy())
            empty_main_loop(pygame)
        iter += 1


def tsp_kruskal_algorithm(points, size=20, length=10, max_iter=None,
                          fLOG=noLOG, pygame=None, screen=None, images=None,
                          distance=None):
    """
    Finds the shortest path going through all points,
    points require to be a 2 dimensional space.

    @param      points      list 2-tuple (X,Y)
    @param      size        the 2D plan is split into square zones
    @param      length      sub path
    @param      max_iter    max number of iterations
    @param      pygame      pygame for simulation
    @param      screen      with pygame
    @param      fLOG        logging function
    @param      images      save intermediate images
    @param      distance    distance function
    @return                 path

    The distance is a function which takes two tuples and returns a distance::

        def distance(p1, p2):
            # ...
            return d

    Les points identiques sont enlevés puis ajoutés à la fin.
    """
    # verification
    if distance is None:
        distance = distance_euclidian
    unique = set()
    for point in points:
        if isinstance(point, list):
            raise TypeError("points cannot be list")
        unique.add(point)

    # remove duplicates
    groups = {}
    for p in points:
        x, y = p[:2]
        if (x, y) in groups:
            groups[x, y].append(p)
        else:
            groups[x, y] = [p]

    before = len(points)
    points = [v[0] for v in groups.values()]
    fLOG("[tsp_kruskal_algorithm] with no duplicates {0} <= {1}".format(
        len(points), before))

    # begin of the algortihm
    fLOG("[tsp_kruskal_algorithm] arbre_poids_minimal nb={0}".format(
        len(points)))
    di = arbre_poids_minimal(points, size, distance=distance)
    arbre = di["arbre"]
    X, Y = di["X"], di["Y"]
    if screen is not None:
        display_arbre(points, arbre, screen=screen, pygame=pygame)
        pygame.display.flip()
        if images is not None:
            c = screen.copy()
            for i in range(0, 5):
                images.append(c)
    fLOG("[tsp_kruskal_algorithm] circuit_eulerien X={0} Y={1}".format(X, Y))
    chemin = circuit_eulerien(points, arbre, screen, pygame, fLOG)

    if len(chemin) != len(points):
        raise Exception(  # pragma: no cover
            "The path should include all points: path:{0} points:{1}".format(
                len(chemin), len(points)))

    if screen is not None:
        display_chemin([points[c] for c in chemin], 0,
                       screen=screen, pygame=pygame)
        pygame.display.flip()
        if images is not None:
            c = screen.copy()
            for i in range(0, 5):
                images.append(c)

    fLOG("[tsp_kruskal_algorithm] circuit_hamiltonien")
    neurone = circuit_hamiltonien(chemin)
    neurones = [points[i] for i in neurone]
    if screen is not None:
        display_chemin(neurones, 0, screen=screen, pygame=pygame)
    fLOG("[tsp_kruskal_algorithm] amelioration_chemin")
    amelioration_chemin(neurones, size, X, Y, length, screen,
                        fLOG=fLOG, pygame=pygame, max_iter=max_iter,
                        images=images, distance=distance)

    # we add duplicates back
    final = []
    for p in neurones:
        x, y = p[:2]
        g = groups[x, y]
        if len(g) == 1:
            final.append(p)
        else:
            final.extend(g)
    return final


def display_ville(villes, screen, bv, pygame):
    """
    dessine les villes à l'écran
    """
    color = 255, 0, 0
    color2 = 0, 255, 0
    for v in villes:
        pygame.draw.circle(screen, color, (int(v[0]), int(v[1])), 3)
    v = villes[bv]
    pygame.draw.circle(screen, color2, (int(v[0]), int(v[1])), 3)


def display_chemin(neurones, bn, screen, pygame):
    """
    dessine le chemin à l'écran
    """
    color = 0, 0, 255
    color2 = 0, 255, 0
    for n in neurones:
        pygame.draw.circle(screen, color, (int(n[0]), int(n[1])), 3)
    v = neurones[bn]
    pygame.draw.circle(screen, color2, (int(v[0]), int(v[1])), 3)
    if len(neurones) > 1:
        pygame.draw.lines(screen, color, True, neurones, 2)


def display_arbre(villes, arbre, mult=1, screen=None, pygame=None):
    """
    dessine le graphe de poids minimal dꧩni par arbre
    """
    if mult == 2:
        color = 0, 255, 0
        li = 4
    else:
        li = 1
        color = 0, 0, 255

    for i in range(0, len(villes)):
        for j in arbre[i]:
            v = (villes[i][0] * mult, villes[i][1] * mult)
            vv = (villes[j][0] * mult, villes[j][1] * mult)
            pygame.draw.line(screen, color, v, vv, li)


def pygame_simulation(size=(800, 500), zone=20, length=10, max_iter=None,
                      nb=700, fLOG=noLOG, pygame=None, folder=None,
                      first_click=False, distance=None, flags=0):
    """
    @param      pygame          module pygame
    @param      nb              number of cities
    @param      first_click     attend la pression d'un clic de souris avant de commencer
    @param      folder          répertoire où stocker les images de la simulation
    @param      size            taille de l'écran
    @param      delay           delay between two tries
    @param      folder          folder where to save images
    @param      first_click     pause
    @param      fLOG            logging function
    @param      distance        distance function
    @param      flags           see `pygame.display.set_mode <https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode>`_
    @return                     @see fn tsp_kruskal_algorithm

    La simulation ressemble à ceci :

    .. raw:: html

        <video autoplay="" controls="" loop="" height="250">
        <source src="http://www.xavierdupre.fr/enseignement/complements/tsp_kruskal.mp4" type="video/mp4" />
        </video>

    Pour lancer la simulation::

        from ensae_teaching_cs.special.tsp_kruskal import pygame_simulation
        import pygame
        pygame_simulation(pygame)

    Voir :ref:`l-tsp_kruskal`.
    """
    pygame.init()
    size = x, y = size[0], size[1]
    white = 255, 255, 255
    screen = pygame.display.set_mode(size, flags)
    screen.fill(white)
    points = construit_ville(nb, x, y)

    if first_click:
        wait_event(pygame)  # pragma: no cover

    images = [] if folder is not None else None
    tsp_kruskal_algorithm(points, size=zone, length=length, max_iter=max_iter,
                          fLOG=fLOG, pygame=pygame, screen=screen, images=images,
                          distance=distance)
    fLOG("folder", folder)
    fLOG("images", len(images))

    if first_click:
        wait_event(pygame)  # pragma: no cover

    if folder is not None:
        fLOG("saving images")
        for it, screen in enumerate(images):
            if it % 10 == 0:
                fLOG("saving image:", it, "/", len(images))
            image = os.path.join(folder, "image_%04d.png" % it)
            pygame.image.save(screen, image)
