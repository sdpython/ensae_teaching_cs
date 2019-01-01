# -*- coding: utf-8 -*-
"""
@file
@brief `Réseaux de Kohonen <https://fr.wikipedia.org/wiki/Carte_auto_adaptative>`_
pour résoudre le
problème du `voyageur de commerce <https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce>`_.
"""
import os
import random
import math
import functools
from pyquickhelper.loghelper import fLOG
from ..helpers.pygame_helper import wait_event, empty_main_loop


def construit_ville(n, x=1000, y=700):
    """
    Tire aléatoirement *n* villes dans un carré ``x * y``,
    on choisit ces villes de sorte qu'elles ne soient pas trop proches.
    """
    # deux villes ne pourront pas être plus proches que mind
    mind = math.sqrt(x * x + y * y) / (n * 0.75)
    # liste vide
    lt = []
    while n > 0:
        # on tire aléatoirement les coordonnées d'une ville
        xx = x * random.random()
        yy = y * random.random()
        # on vérifie qu'elle n'est pas trop proche d'aucune autre ville
        ajout = True
        for t in lt:
            d1 = t[0] - xx
            d2 = t[1] - yy
            d = math.sqrt(d1 * d1 + d2 * d2)
            if d < mind:
                ajout = False  # ville trop proche
        # si la ville n'est pas trop proche des autres, on l'ajoute à la liste
        if ajout:
            lt.append((xx, yy))
            n -= 1  # une ville en moins à choisir
    return lt


def construit_liste_neurones(villes, nb=0):
    """
    Place les neurones sur l'écran,
    il y a autant de neurones que de villes,
    le paramètre villes est la liste des villes.
    """
    if nb == 0:
        nb = len(villes)

    # coordonnées maximale
    maxx, maxy = 0, 0
    for v in villes:
        if v[0] > maxx:
            maxx = v[0]
        if v[1] > maxy:
            maxy = v[1]

    maxx /= 2
    maxy /= 2

    if nb > 1:
        # dispose les neurones en ellipse
        n = []
        for i in range(0, nb):
            x = maxx + maxx * math.cos(math.pi * 2 * float(i) / nb) / 4
            y = maxy + maxy * math.sin(math.pi * 2 * float(i) / nb) / 4
            n.append((x, y))
        return n
    else:
        n = [(maxx, maxy)]
        return n


def distance_euclidienne_carree(p1, p2):
    """
    Calcule la distance euclidienne entre deux points.
    """
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return x * x + y * y


def ajoute_vecteur(v, n):
    """
    Ajoute deux vecteurs entre eux.
    """
    return (v[0] + n[0], v[1] + n[1])


def soustrait_vecteur(v, n):
    """
    Soustrait deux vecteurs.
    """
    return (v[0] - n[0], v[1] - n[1])


def multiplie_vecteur(v, f):
    """
    Multiplie un vecteur par un scalaire.
    """
    return (v[0] * f, v[1] * f)


def poids_attirance(p, dist):
    """
    Calcule le poids d'attraction d'une neurone vers une ville.
    """
    d = p[0] * p[0] + p[1] * p[1]
    d = math.sqrt(d)
    d = dist / (d + dist)
    return d


def vecteur_norme(p):
    """
    Calcul la norme d'un vecteur.
    """
    return math.sqrt(p[0] * p[0] + p[1] * p[1])


def deplace_neurone(n, villes, neurones, dist_w, forces, compte):
    """
    Déplace le neurone de plus proche de la ville *n*,
    déplace ses voisins.

    @param    villes        liste des villes
    @param    neurones      liste des neurones
    @param    dist          distance d'attirance
    @param    forces        force de déplacement des voisins du neurones
    @param    compte        incrémente compte [n] où n est l'indice du neurone choisi
    @return                 indice du neurone le plus proche
    """
    # recherche du neurone le plus proche
    v = villes[n]
    proche = 0
    dist = distance_euclidienne_carree(v, neurones[0])
    for i in range(1, len(neurones)):
        d = distance_euclidienne_carree(v, neurones[i])
        if d < dist:
            dist = d
            proche = i

    # vecteur de déplacement
    i = proche
    compte[i] += 1
    n = neurones[i]
    vec = soustrait_vecteur(v, n)
    poids = poids_attirance(vec, dist_w)
    vec = multiplie_vecteur(vec, poids)
    n = ajoute_vecteur(n, vec)
    neurones[i] = n

    # déplacement des voisins
    for k in range(0, len(forces)):
        i1 = (i + k + 1) % len(neurones)
        i2 = (i - k - 1 + len(neurones)) % len(neurones)
        n1 = neurones[i1]
        n2 = neurones[i2]

        vec = soustrait_vecteur(n, n1)
        poids = poids_attirance(vec, dist_w)
        vec = multiplie_vecteur(vec, poids)
        vec = multiplie_vecteur(vec, forces[k])
        n1 = ajoute_vecteur(n1, vec)

        vec = soustrait_vecteur(n, n2)
        poids = poids_attirance(vec, dist_w)
        vec = multiplie_vecteur(vec, poids)
        vec = multiplie_vecteur(vec, forces[k])
        n2 = ajoute_vecteur(n2, vec)

        neurones[i1] = n1
        neurones[i2] = n2

    return proche


def iteration(villes, neurones, dist, forces, compte_v, compte_n):
    """
    Choisit une ville aléatoirement et attire le neurones le plus proche,
    choisit cette ville parmi les villes les moins fréquemment choisies.

    @param    villes     liste des villes
    @param    neurones   liste des neurones
    @param    dist       distance d'attirance
    @param    forces     force de déplacement des voisins du neurones
    @param    compte_v   incrémente compte_v [n] où n est l'indice de la ville choisie
    @param    compte_n   incrémente compte_n [n] où n est l'indice du neurone choisi
    @return              indices de la ville et du neurone le plus proche
    """
    m = min(compte_v)
    ind = [i for i in range(0, len(villes)) if compte_v[i] == m]
    n = random.randint(0, len(ind) - 1)
    n = ind[n]
    compte_v[n] += 1
    return n, deplace_neurone(n, villes, neurones, dist, forces, compte_n)


def modifie_structure(neurones, compte, nb_sel):
    """
    Modifie la structure des neurones, supprime les neurones jamais
    déplacés, et ajoute des neurones lorsque certains sont trop sollicités.
    """
    def cmp_add(i, j):
        return -1 if i[0] < j[0] else (1 if i[0] > j[0] else 0)

    if nb_sel > 0:
        # supprime les neurones les moins sollicités
        sup = [i for i in range(0, len(neurones)) if compte[i] == 0]
        if len(sup) > 0:
            sup.sort()
            sup.reverse()
            for i in sup:
                del compte[i]
                del neurones[i]

        # on ajoute un neurone lorsque max (compte) >= 2 * min (compte)
        add = []
        for i in range(0, len(compte)):
            if compte[i] > nb_sel:
                d1 = math.sqrt(distance_euclidienne_carree(neurones[i],
                                                           neurones[(i + 1) % len(neurones)]))
                d2 = math.sqrt(distance_euclidienne_carree(neurones[i],
                                                           neurones[(i - 1 + len(neurones)) % len(neurones)]))
                if d1 > d2:
                    d1 = d2
                p = neurones[i]
                p = (p[0] + random.randint(0, int(d1 / 2)),
                     p[1] + random.randint(0, int(d1 / 2)))
                add.append((i, p, 0))

        add = list(sorted(add, key=functools.cmp_to_key(cmp_add)))
        add.reverse()
        for a in add:
            neurones.insert(a[0], a[1])
            compte.insert(a[0], a[2])

    # on remet les compteurs à zéros
    for i in range(0, len(compte)):
        compte[i] = 0


def moyenne_proximite(villes):
    """
    Retourne la distance moyenne entre deux villes les plus proches.
    """
    c = 0
    m = 0
    for v in villes:
        mn = 100000000
        for vv in villes:
            if v == vv:
                continue
            d = distance_euclidienne_carree(v, vv)
            if d < mn:
                mn = d
        c += 1
        m += math.sqrt(mn)
    m /= float(c)
    return m


def display_neurone(neurones, screen, bn, pygame):
    """
    Dessine les neurones à l'écran.
    """
    color = 0, 0, 255
    color2 = 0, 255, 0
    for n in neurones:
        pygame.draw.circle(screen, color, (int(n[0]), int(n[1])), 5)
    v = neurones[bn]
    pygame.draw.circle(screen, color2, (int(v[0]), int(v[1])), 5)
    if len(neurones) > 1:
        pygame.draw.lines(screen, color, True, neurones, 2)


def display_ville(villes, screen, bv, pygame):
    """
    Dessine les villes à l'écran.
    """
    color = 255, 0, 0
    color2 = 0, 255, 0
    for v in villes:
        pygame.draw.circle(screen, color, (int(v[0]), int(v[1])), 5)
    v = villes[bv]
    pygame.draw.circle(screen, color2, (int(v[0]), int(v[1])), 5)


def pygame_simulation(pygame, folder=None, size=(800, 500), nb=200,
                      tour=2, dist_ratio=4, fs=(1.5, 1, 0.75, 0.5, 0.25),
                      max_iter=12000, alpha=0.99, beta=0.90,
                      first_click=False, flags=0, fLOG=fLOG):
    """
    @param      pygame          module pygame
    @param      first_click     attend la pression d'un clic de souris avant de commencer
    @param      folder          répertoire où stocker les images de la simulation
    @param      size            taille de l'écran
    @param      delay           delay between two tries
    @param      flags           see `pygame.display.set_mode <https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode>`_
    @param      fLOG            logging function
    @param      fs              paramètres
    @param      max_iter        nombre d'itérations maximum
    @param      alpha           paramètre alpha
    @param      beta            paramètre beta
    @param      dist_ratio      ratio distance
    @param      tour            nombre de tours
    @param      nb              nombre de points

    La simulation ressemble à ceci :

    .. raw:: html

        <video autoplay="" controls="" loop="" height="125">
        <source src="http://www.xavierdupre.fr/enseignement/complements/tsp_kohonen.mp4" type="video/mp4" />
        </video>

    Pour lancer la simulation::

        from ensae_teaching_cs.special.tsp_kohonen import pygame_simulation
        import pygame
        pygame_simulation(pygame)

    Voir :ref:`l-puzzle_girafe`.
    """
    pygame.init()
    size = x, y = size[0], size[1]
    white = 255, 255, 255
    screen = pygame.display.set_mode(size, flags)
    villes = construit_ville(nb, x, y)
    neurones = construit_liste_neurones(villes, 3)
    compte_n = [0 for i in neurones]
    compte_v = [0 for i in villes]
    maj = tour * len(villes)
    dist = moyenne_proximite(villes) * dist_ratio

    if first_click:
        wait_event(pygame)
    images = [] if folder is not None else None

    iter = 0
    while iter < max_iter:
        iter += 1

        if iter % 1000 == 0:
            fLOG("iter", iter)

        if iter % maj == 0:
            modifie_structure(neurones, compte_n, tour)
            dist *= alpha
            f2 = tuple(w * beta for w in fs)
            fs = f2

        bv, bn = iteration(villes, neurones, dist, fs, compte_v, compte_n)

        screen.fill(white)
        display_ville(villes, screen, bv, pygame)
        display_neurone(neurones, screen, bn, pygame)
        empty_main_loop(pygame)
        pygame.display.flip()

        if images is not None and iter % 10 == 0:
            images.append(screen.copy())

    if first_click:
        wait_event(pygame)

    if folder is not None:
        fLOG("saving images")
        for it, screen in enumerate(images):
            if it % 10 == 0:
                fLOG("saving image:", it, "/", len(images))
            image = os.path.join(folder, "image_%04d.png" % it)
            pygame.image.save(screen, image)
