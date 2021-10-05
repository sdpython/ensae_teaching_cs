# -*- coding: utf-8 -*-
"""
@file
@brief Fonctions, classes pour résoudre un puzzle à 8 pièces
disposé de façon non conventionnelle. Voir :ref:`l-puzzle_2`.
"""

import time
import os
from textwrap import dedent
from pyquickhelper.loghelper import fLOG
from ..helpers.pygame_helper import wait_event, empty_main_loop


class Puzzle2Bord:
    """
    Définition d'un bord ou côté d'une pièce, il possède deux couleurs.
    """

    def __init__(self, definition):
        """
        :param definition: chaîne de caractères

        *definition* est une chaîne de 2 caractères qui définit un bord, exemple :

        * ``RG`` for rouge vert (red, green)

        Les quatre couleurs sont R (red, rouge), Y (yellow, jaune),
        G (green, vert), B (blue, bleu).
        """
        if len(definition) != 2:
            raise ValueError("Deux couleurs attendues pas %r." % definition)
        for i in range(2):
            if definition[i] not in 'RYGB':
                raise ValueError("Couleurs inattendues: %r." % definition)
        self.couleur = tuple(definition)

    def __str__(self):
        """
        Cette méthode est appelée lorsqu'on exécute l'instruction print
        avec un objet de type @see cl Puzzle2Bord.
        """
        return "".join(self.couleur)

    def compatible(self, bord):
        """
        Dit si deux bords sont compatibles, ils ont les mêmes
        couleurs mais inversées.
        """
        return (self.couleur[0] == bord.couleur[1] and
                self.couleur[1] == bord.couleur[0])


class Puzzle2Piece:
    """
    Définition d'une pièce du puzzle, celle-ci inclut :

    - **bord** : cette liste contient quatre objets de type Bord,
      cette liste ne changera plus
    - **position** : c'est la position de la pièce dans le puzzle,
      ce qui nous intéresse, c'est la position finale de la pièce
      dans le puzzle, cette information va donc bouger au fur et
      à mesure que nous allons essayer de résoudre le puzzle
    - **orientation** : de même que pour la position, une pièce peut
      être tournée sans changer de position, c'est le résultat final
      qui nous intèresse

    Pour l'affichage, on ajoute deux informations :

    - **name** : le nom de l'image de la pièce
    - **image** : c'est la représentation de l'image dans la mèmoire de
      l'ordinateur pour le module pygame
    """

    def __init__(self, name, definition, position, numero):
        """
        On définit la pièce:

        :param name: nom de l'image représentant la pièce
        :param definition: chaîne de 4 caractères indiquant les quatre couleurs
            au quatre angles
        :param position: c'est la position initiale de la pièce,
            on suppose que l'orientation est nulle pour commencer
        :param numero: numéro de la pièce

        A partir de ces informations, on construit :

        - **image** : c'est la représentation en mémoire de l'image de la pièce
        - **bord** : c'est une liste qui définit les 4 bords de la pièce
        - **orientation** : c'est l'orientation de la pièce, au début de
          la résolution, elle est nulle
        """
        self.name = name
        self.bord = []

        for i in range(0, 3):
            self.bord.append(Puzzle2Bord(definition[i:i + 2]))
        self.bord.append(Puzzle2Bord(definition[-1] + definition[0]))

        self.orientation = 0
        self.position = position
        self.numero = numero

    def load_image(self, pygame):
        """
        Charge l'image pour une simulation graphique.

        :param pygame: module :epkg:`pygame`
        """
        image = pygame.image.load(self.name)
        self.image = pygame.transform.scale(image, (250, 250))
        s = self.image.get_size()
        self.image_petite = pygame.transform.scale(
            self.image, (int(s[0] * 0.7), int(s[1] * 0.7)))

    def __str__(self):
        """
        Définition ce qu'on doit afficher lorsqu'on exécute
        l'instruction print avec un objet de type
        @see cl Puzzle2Piece.
        """
        s = str(self.position) + " : "
        s += "-".join("".join(self.bord_angle(a * 90, 0).couleur)
                      for a in range(0, 4))
        s += " :: "
        s += "-".join("".join(self.bord_angle(a * 90, self.orientation).couleur)
                      for a in range(0, 4))
        s += " or=%d" % self.orientation
        s += " numero=%d" % self.numero
        s += " pos=%d" % self.position
        return s

    def bord_angle(self, angle, orientation=None):
        """
        Retourne le bord connaissant l'orientation de la pièce,
        le bord demandé est celui correspondant à :

        - 0  bord droit
        - 90 bord haut
        - 180 bord gauche
        - 270 bord bas
        """
        if orientation is None:
            return self.bord_angle(angle, self.orientation)
        dif = (angle - orientation + 360) % 360 // 90
        return self.bord[dif]


class Puzzle2:
    """
    Définition d'une classe puzzle, elle contient simplement
    une liste de 9 pièces dont les positions sont:

    ::

          5
        6 1 2
          4 3 7
            8

    et les orientations choisies dans l'ensemble ``{ 0, 90, 180, 270 }``

    Voir :ref:`l-puzzle_2`.
    """

    def __init__(self):
        """
        On définit le puzzle à partir des informations contenues
        dans le répertoire *data* de ce module qui doit contenir :

        - 8 images appelées ``piece21.png``, ..., ``piece28.png``
        - un fichier ``definition_puzzle_girafe.txt`` contenant la définition de
          chacun des 4 bords de chacune des 9 pièces :

        ::

            GBYR
            BRYG
            BGYR
            YRGB
            YBRG
            BGYR
            BYGR
            RYBG
        """
        dir_ = os.path.abspath(os.path.dirname(__file__))
        dir_ = os.path.join(dir_, "data")

        with open(os.path.join(dir_, "definition_puzzle_2.txt"), "r") as f:
            bo = f.readlines()

        # on définit chaque pièce
        self.piece = []
        for i in range(1, 9):
            name = os.path.join(dir_, "piece2%d.png" % i)
            d = bo[i - 1].strip(" \n\r")
            d = d[1:] + d[0]
            p = Puzzle2Piece(name, d, 0, i)
            self.piece.append(p)
            print(p)

    def load_images(self, pygame):
        """
        Charge les images pour une simulation graphique.

        :param pygame: module :epkg:`pygame`
        """
        for p in self.piece:
            p.load_image(pygame)

    def __str__(self):
        """
        Ce qu'on doit afficher lorsqu'on exécute
        l'instruction print avec un objet de type
        @see cl Puzzle2.
        """
        s = dedent("""
              5
            6 1 2
              4 3 7
                8
            """).strip("\n\r") + "\n"
        for p in self.piece:
            s += str(p) + "\n"
        return s

    def pixel(self, position):
        """
        Retourne en fonction de la position (1 à 8) de la
        pièce sa position sur l'écran, soit deux coordonnées.

        :return: `tuple(x,y)`

        ::

              5
            6 1 2
              4 3 7
                8
        """
        positions = {
            1: (1, 1),
            2: (1, 2),
            3: (2, 2),
            4: (2, 1),
            5: (0, 1),
            6: (1, 0),
            7: (2, 3),
            8: (3, 2)
        }
        ligne, colonne = positions[position]
        return (colonne * 250, ligne * 250)

    def meilleure_piece(self, free, pos):
        """
        Retourne la prochaine pièce à placer sur le puzzle,
        dans un premier temps, on peut prend la première qui vient,
        ensuite, on peut essayer un choix plus judicieux.
        """
        if len(free) == 0:
            return None
        return free[0]

    def piece_position(self, pi):
        """
        Recherche la piece associée à la position pi.
        """
        for p in self.piece:
            if p.position == pi:
                return p
        return None

    def ensemble_voisin(self, i):
        """
        Retourne les positions voisins de la position i.
        Retourne toujours quatre voisins, 0 si la case
        est hors-jeu.

        ::

              5
            6 1 2
              4 3 7
                8

        ::
              1
            0   3
              2
        """
        if i == 1:
            return [6, 5, 4, 2]
        if i == 2:
            return [1, 0, 3, 0]
        if i == 3:
            return [4, 2, 8, 7]
        if i == 4:
            return [0, 1, 0, 3]
        if i == 5:
            return [0, 0, 1, 0]
        if i == 6:
            return [0, 0, 0, 1]
        if i == 7:
            return [3, 0, 0, 0]
        if i == 8:
            return [0, 3, 0, 0]
        raise ValueError("Unexpected position %r." % i)

    def nb_place(self):
        """
        Retourne le nombre de places vides.
        """
        i = 0
        for p in self.piece:
            if p.position == 0:
                i += 1
        return i

    def voisin_possible(self, piece, p, a):
        """
        Détermine si la pièce *self* peut être voisine
        avec la pièce *p* tournée de l'angle *a*.
        """
        v1 = self.ensemble_voisin(piece.position)
        if p.position not in set(v1):
            return False
        v2 = self.ensemble_voisin(p.position)
        if piece.position not in set(v2):
            return False
        d = p.position - piece.position
        if abs(d) == 1 and (p.position - 1) // 3 == (piece.position - 1) // 3:
            # voisin en x
            if d == 1:
                a1 = 0
                a2 = a1 + 180
            else:
                a1 = 180
                a2 = 0
        elif abs(d) == 3:
            # voisin en y
            if d == 1:
                a1 = 90
                a2 = 270
            else:
                a1 = 270
                a2 = 90
        else:
            # pas voisin
            return False

        b1 = piece.bord_angle(a1)
        b2 = p.bord_angle(a2, a)
        return b1.compatible(b2)

    def angle_possible(self, p, display=False):
        """
        Retourne l'ensemble des angles possibles
        pour une pièce donnée.
        """
        voisin = self.ensemble_voisin(p.position)
        if display:
            print("voisin = ", voisin)
        res = []
        for a in [0, 90, 180, 270]:
            r = True
            for v in voisin:
                if v == 0:
                    continue
                piece = self.piece_position(v)
                if piece is not None:
                    t = self.voisin_possible(piece, p, a)
                    r = r and t
            if r:
                res.append(a)
        return res

    def solution(self, pos=1, screen=None, pygame=None, images=None, delay=200):
        """
        Résoud le puzzle de façon récursive : on pose une
        pièce puis on résoud le puzzle restant
        (une pièce en moins, une case en moins).

        :param pos: niveau de récursivité
        :param screen: image pygame
        :param pygame: module pygame
        :param images: stores images in this list if not None
        :param delay: delay between two tries

        L'affichage :epkg:`pygame` est optionnel.
        """
        if pos == 1:
            for p in self.piece:
                p.position = 0
            self.nb_position = 0
            self.essai = 0

        self.essai += 1

        if self.nb_position == len(self.piece):
            time.sleep(0.2)
            return None

        # le tableau free mémorise l'ensemble des pièces non encore placées
        free = []
        for p in self.piece:
            if p.position == 0:
                free.append(p)

        if screen is not None and pygame is not None and images is not None:
            empty_main_loop(pygame, lambda: str(self))
            display_puzzle_2(self, screen, True, pygame=pygame)
            pygame.display.flip()
            images.append(screen.copy())

        p = self.meilleure_piece(free, pos)
        # si p == None, on n'étudie pas les solutions avec les pièces placées
        # avant aux positions 1 à pos --> on n'entrera pas dans la boucle
        # suivante
        while p is not None:

            p.position = pos
            angle = self.angle_possible(p)

            # p est la pièce choisie, pour cette pièce
            # on passe en revue toutes les orientations
            for a in angle:
                p.orientation = a

                if pygame is not None:
                    pygame.time.wait(delay)

                if self.nb_place() == 0:
                    return True
                else:
                    r = self.solution(pos + 1, screen=screen,
                                      pygame=pygame, images=images, delay=delay)
                    if r:
                        return True

            p.position = 0

            # on réactualise le tableau free qui aura été modifié par
            # l'appel à self.solution et on enlève le choix précédemment
            # testé
            free2 = free
            free = []
            for f in free2:
                if f.numero != p.numero:
                    free.append(f)

            # on passe au choix suivant avec free contenant les pièces
            # placées et les pièces essayées
            p = self.meilleure_piece(free, pos)
        return None


def display_puzzle_2(self, screen, petite=False, pygame=None):
    """
    Affiche les pièces sur l'écran,
    en plus petit pour celles qui ne sont pas encore placées.
    """
    screen.fill((0, 0, 0))
    free = [0 for i in self.piece]
    for p in self.piece:
        if p.position > 0:
            p.darker = False
            display_puzzle_2_piece(
                p, screen, self.pixel(p.position), pygame=pygame)
            free[p.position - 1] = 1

    if petite:
        em = []
        for i in range(0, len(free)):
            if free[i] == 0:
                em.append(i + 1)
        i = 0
        for p in self.piece:
            if p.position == 0:
                p.darker = True
                display_puzzle_2_piece(
                    p, screen, self.pixel(em[i]), pygame)
                i += 1

    pygame.display.flip()


def display_puzzle_2_piece(self, screen, position, pygame):
    """
    Affiche la pièce en tenant compte de sa position
    et de son orientation.
    """
    if "darker" in self.__dict__ and self.darker:
        position = (position[0] + 20, position[1] + 20)
        image = pygame.transform.rotate(self.image_petite, self.orientation)
        screen.blit(image, position)
    else:
        image = pygame.transform.rotate(self.image, self.orientation)
        screen.blit(image, position)


def pygame_simulation(pygame, first_click=False, folder=None,
                      size=(1000, 1000), fLOG=fLOG, delay=200,
                      flags=0):
    """
    Simulation graphique.
    Illuste la résolution du puzzle

    :param pygame: module pygame
    :param first_click: attend la pression d'un clic de souris avant de commencer
    :param folder: répertoire où stocker les images de la simulation
    :param size: taille de l'écran
    :param delay: delay between two tries
    :param flags: see `pygame.display.set_mode
        <https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode>`_
    :param fLOG: logging function
    :return: @see cl Puzzle2

    La simulation ressemble à ceci :

    .. raw:: html

        <video autoplay="" controls="" loop="" height="500">
        <source src="http://www.xavierdupre.fr/enseignement/complements/puzzle_2.mp4" type="video/mp4" />
        </video>

    Pour lancer la simulation :

    ::

        from ensae_teaching_cs.special.puzzle_girafe import pygame_simulation
        import pygame
        pygame_simulation(pygame)

    Voir :ref:`l-puzzle_girafe`.
    """
    # initialisation du module pygame
    pygame.init()
    screen = pygame.display.set_mode(size, flags)

    # on définit le puzzle
    p = Puzzle2()
    p.load_images(pygame)

    # on affiche le puzzle avec print (format texte)
    fLOG("\n" + str(p))

    # on affiche le puzzle à l'écran
    display_puzzle_2(p, screen, petite=True, pygame=pygame)
    if first_click:
        wait_event(pygame)

    # on rafraîchit l'écran pour que le puzzle apparaissent
    pygame.display.flip()

    images = [] if folder is not None else None

    # on trouve la solution
    r = p.solution(screen=screen, pygame=pygame, images=images, delay=delay)
    fLOG("résolution ", r)
    fLOG("nombre d'appels à la méthode solution ", p.essai)

    if images is not None:
        empty_main_loop(pygame)
        display_puzzle_2(p, screen, True, pygame=pygame)
        pygame.display.flip()
        images.append(screen.copy())

    if folder is not None:
        fLOG("saving images")
        for it, screen in enumerate(images):
            if it % 10 == 0:
                fLOG("saving image:", it)
            image = os.path.join(folder, "image_%04d.png" % it)
            pygame.image.save(screen, image)

    # on attend la pression d'un clic de souris avant de terminer le programme
    display_puzzle_2(p, screen, petite=True, pygame=pygame)
    if first_click:
        wait_event(pygame)
