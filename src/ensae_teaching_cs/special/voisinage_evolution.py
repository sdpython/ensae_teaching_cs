#-*- coding: utf-8 -*-
"""
@file
@brief Implémente une simulation d'évolution des catégories de population
selon un modèle de Schelling.
"""
import random
import copy
import os
from pyquickhelper.loghelper import noLOG
from ..helpers.pygame_helper import wait_event, empty_main_loop


def round(r, g, b):
    """
    arrondit chaque couleur
    """
    return (int(r), int(g), int(b))


class Ville:
    """
    définit une ville qui va évoluer par la suite
    @param      colors          couleurs vives : simulation sans tenir compte de riches ou pauvres,
                                seulement regroupement
    @param      colors_grade    simulation en tenant compte des riches, du plus foncé
                                au plus clair (riches)
    """
    colors = {-1: (0, 0, 0), 0: (255, 0, 0), 1: (0, 255, 0), 2: (0, 0, 255),
              3: (255, 255, 0), 4: (255, 0, 255), 5: (0, 255, 255)}

    colors_grade = {-1: (0, 0, 0), 0: round(131.28918999850276, 137.49288815690971, 51.799520886360227),
                    1: round(151.28918999850276, 147.49288815690971, 71.799520886360227),
                    2: round(191.42448385755856, 191.27629208812527, 57.413606761812389),
                    3: round(190.99311386065693, 133.49749594932979, 41.781926646045072),
                    4: round(167.25849848112253, 76.347509523120692, 41.289551087323403),
                    5: round(196.76664713923063, 39.476078890841634, 31.506444053895724)
                    }

    def __init__(self, cote=100, group=3, taille=3, riche=False, th2=1.2,
                 renouvellement=0.15, delay=1):
        """
        constructeur
        @param      cote            côté du carré utilisé pour la simulation
        @param      group           nombre de catégories de gens
        @param      taille          chaque individu regarde ses voisins à +- taille près
        @param      riche           simulation avec riche ou non
        @param      th2             le voisin le plus pauvre peut-être contaminé,
                                    si la différence de classes est importante (cl1 > cl2 * th2)
        @param      renouvellement  à chaque itération, une certaine proportion des pâtés sont mis à jour,
                                    cette proportion correspond au renouvellement
        @param      delay           la simulation prend en compte la ville lors des "delay" dernières itérations

        On tire au hasard la classe d'un pâté de maison dans un disque de rayon cote.

        """
        if cote is None:
            pass
        else:
            self.mat = [[random.randint(0, group - 1)
                         for i in range(0, cote)] for j in range(0, cote)]
            self.group = group
            self.taille = taille
            self.past = []
            self.th2 = th2
            self.riche = riche
            self.delay = delay
            self.renouvellement = renouvellement
            c = len(self.mat) / 2
            R = c ** 2 / 4
            for i in range(0, len(self.mat)):
                for j in range(0, len(self.mat[0])):
                    d = (i - c) ** 2 + (j - c) ** 2
                    if d > R:
                        self.mat[i][j] = -1

    def _voisinage(self, i, j, mat):
        """calcul de la répartition du voisiage
        @param      i       i,j coordonnées
        @param      j
        @param      mat     matrice
        @return             dictionnaire { classe:nombre }
        """
        d = {}
        x1 = max(0, i - self.taille)
        y1 = max(0, j - self.taille)
        x2 = min(len(self.mat), i + self.taille + 1)
        y2 = min(len(self.mat), j + self.taille + 1)
        for i in range(x1, x2):
            for j in range(y1, y2):
                c = mat[i][j]
                if c not in d:
                    d[c] = 0
                d[c] += 1
        return d

    def evolution(self):
        """
        évolution d'une itération à l'autre
        @return         nb1,nb2
        """

        keep = copy.deepcopy(self.mat)
        self.past.append(keep)
        if len(self.past) > self.delay:
            del self.past[:len(self.past) - self.delay]

        def fff(x, c):
            if c not in x:
                return 0
            elif x[c] >= sum(x.values()) * self.th:
                return 1
            else:
                return 0

        # on renouvelle une certaine proportion de pâtés (renouvellement)
        # tiré au hasard
        nb1, nb2 = 0, 0
        for n in range(0, int(len(self.mat) ** 2 * self.renouvellement)):

            # on tire deux voisins au hasard
            i = random.randint(0, len(self.mat) - 1)
            j = random.randint(0, len(self.mat) - 1)
            k = i + random.randint(-1, 1)
            l = j + random.randint(-1, 1)
            if k == i and l == j:
                continue
            x1 = max(0, k)
            y1 = max(0, l)
            x2 = min(len(self.mat) - 1, k)
            y2 = min(len(self.mat) - 1, l)
            if x1 != x2 or y1 != y2:
                continue

            # calcul des deux voisinages
            v1 = self._voisinage(i, j, self.mat)
            v2 = self._voisinage(k, l, self.mat)
            c = self.mat[i][j]
            d = self.mat[k][l]

            # c,d : leurs catégorie

            if c >= 0 and d >= 0:
                # s'ils sont tous les deux habités
                if v1.get(c, 0) < v2.get(c, 0) and v1.get(d, 0) > v2.get(d, 0):
                    # premier cas: si l'un voisin a plus de voisins qui ressemblent à l'autre
                    # et réciproquement, ils échangent
                    self.mat[k][l] = c
                    self.mat[i][j] = d
                    nb1 += 1
                elif v1.get(c, 0) > v2.get(d, 0) * self.th2 and (not self.riche or c > d):
                    # deuxième cas : cas riche, le voisin le plus pauvre peut-être contaminé
                    # si la différence est importante
                    self.mat[k][l] = c
                    nb2 += 1
            elif c == -1:
                # celui qui n'est pas habité prend la couleur de l'autre
                self.mat[i][j] = d
            elif d == -1:
                # celui qui n'est pas habité prend la couleur de l'autre
                self.mat[k][l] = c

        return nb1, nb2

    def count(self):
        """
        @return la population
        """
        d = {}
        for line in self.mat:
            for c in line:
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
        return d


class VilleImage (Ville):
    """
    Définit une ville à partir d'une image (donc non aléatoire).
    """

    def __init__(self, image,
                 cote=100,
                 group=3,
                 taille=3,
                 riche=False,
                 th2=1.2,
                 renouvellement=0.15,
                 delay=1):
        """constructeur
        @param      image           nom d'une image pour définir l'initialisation
        @param      cote            cote du carré utilisé pour la simulation
        @param      group           nombre de catégories de gens
        @param      taille          chaque individu regarde ses voisins à +- taille près
        @param      riche           simulation avec riche ou non
        @param      th2             le voisin le plus pauvre peut-être contaminé,
                                    si la différence de classes est importante (cl1 > cl2 * th2)
        @param      renouvellement  à chaque itération, une certaine proportion des pâtés sont mis à jour,
                                    cette proportion correspond à renouvellement
        @param      delay           la simulation prend en compte la ville lors des "delay" dernières itérations

        On tire au hasard la classe d'un pâté de maison dans un disque de rayon cote.
        """
        Ville.__init__(self, cote, group, taille, riche,
                       th2, renouvellement, delay)
        self._initialisation(image)

    def _initialisation(self, im):
        for i in range(0, len(self.mat)):
            for j in range(0, len(self.mat[0])):
                p = im.get_at((i, j))

                mins = 1e6
                best = None
                for k, v in Ville.colors_grade.items():
                    s = 0
                    for z in [0, 1, 2]:
                        s += (v[z] - p[z]) ** 2
                    s = s ** 0.5
                    if s < mins:
                        mins = s
                        best = k
                self.mat[i][j] = best


def display(self, screen, x, pygame):
    """
    affichage
    @param      screen      écran
    @param      x           dimension d'un pâté de maison
    """
    screen.fill((0, 0, 0))
    if self.riche:
        colors = Ville.colors_grade
    else:
        colors = Ville.colors
    for i in range(0, len(self.mat)):
        for j in range(0, len(self.mat[i])):
            c = colors[self.mat[i][j]]
            pygame.draw.rect(screen, c, pygame.Rect(i * x, j * x, x, x))


def pygame_simulation(pygame, first_click=False, folder=None,
                      x=6, nb=100, group=6, max_iter=150, th2=1.75,
                      image=None, fLOG=noLOG):
    """
    Simulation graphique.
    Illuste la résolution du puzzle

    @param      pygame          module pygame
    @param      first_click     attend la pression d'un clic de souris avant de commencer
    @param      folder          répertoire où stocker les images de la simulation
    @param      size            taille de l'écran
    @param      delay           delay between two tries
    @param      x               pour l'affichage, taille d'un pâté de maison à l'écran
    @param      group           ...
    @param      nb              taille du carré de la simulation en nombre de pâtés de maisons
    @param      th2             ...
    @param      max_iter        nombre d'itérations
    @param      image           définition de la ville
    @return                     @see cl Ville

    La simulation ressemble à ceci :

    .. raw:: html

        <video autoplay="" controls="" loop="" height="500">
        <source src="http://www.xavierdupre.fr/enseignement/complements/voisinage.mp4" type="video/mp4" />
        </video>

    Pour lancer la simulation::

        from ensae_teaching_cs.special.voisinage_evolution import pygame_simulation
        import pygame
        pygame_simulation(pygame)

    Voir :ref:`l-simulation_voisinage`.
    """

    if image is None:
        this = os.path.dirname(__file__)
        image = os.path.join(this, "paris_today.png")

    image = pygame.image.load(image)
    image = pygame.transform.scale(image, (100, 100))

    pygame.init()
    size = nb * x, nb * x
    screen = pygame.display.set_mode(size)

    ville = VilleImage(image, nb, group, th2=th2, riche=True)

    if first_click and pygame is not None:
        wait_event(pygame)

    if pygame is not None:
        display(ville, screen, x, pygame)
        pygame.display.flip()
        images = []
        if folder is not None:
            images.append(screen.copy())

    fLOG(ville.count())
    for i in range(0, max_iter):
        nb = ville.evolution()
        fLOG("iteration ", i, " ch ", nb)
        if pygame is not None:
            if folder is not None:
                images.append(screen.copy())
            display(ville, screen, x, pygame)
            pygame.display.flip()
            empty_main_loop(pygame)

    fLOG(ville.count())
    if first_click and pygame is not None:
        wait_event(pygame)

    if folder is not None and pygame is not None:
        images.append(screen.copy())

    if folder is not None:
        fLOG("saving images")
        for it, screen in enumerate(images):
            if it % 10 == 0:
                fLOG("saving image:", it)
            image = os.path.join(folder, "image_%04d.png" % it)
            pygame.image.save(screen, image)

    return ville
