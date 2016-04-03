#-*- coding: utf-8 -*-
"""
@file
@brief Fonctions, classes pour résoudre un puzzle à 9 pièces disposé en carré 3x3. Voir :ref:`l-puzzle_girafe`.
"""

import time
import os
from pyquickhelper.loghelper import fLOG
from ..helpers.pygame_helper import wait_event, empty_main_loop


class PuzzleGirafeBord:
    """
    définition d'un bord ou côté d'une pièce, il posside :

    - partie : une partie de la girafe (haut ou bas)
    - une couleur : la couleur de cette partie, (orange, violet, bleu clair, bleu foncé)
    """

    def __init__(self, definition):
        """
        constructeur

        @param      definition      chaîne de caractères


        *definition* est une chaîne de 2 caractères qui définit un bord, exemple :

        * ``HO`` pour haut orange
        * ``BB`` pour bas bleu
        * ``BV`` pour bas violet
        * ``HM`` pour haut mauve
        """

        if definition[0] == "H":
            self.partie = "haut"
        elif definition[0] == "B":
            self.partie = "bas"
        else:
            self.partie = definition + "###"

        if definition[1] == "O":
            self.couleur = "orange"
        elif definition[1] == "B":
            self.couleur = "bleu clair"
        elif definition[1] == "M":
            self.couleur = "violet"
        elif definition[1] == "V":
            self.couleur = "bleu fonce"
        else:
            self.couleur = definition + "##"

    def __str__(self):
        """
        cette méthode est appelée lorsqu'on exécute l'instruction print
        avec un objet de type Bord
        """
        return self.partie + " " + self.couleur

    def compatible(self, bord):
        """
        dit si deux bords sont compatibles, c'est à dire
        de la même couleur et de partie différente
        """
        return self.couleur == bord.couleur and self.partie != bord.partie


class PuzzleGirafePiece:
    """
    définition d'une pièce du puzzle, celle-ci inclut :

    - **bord** : cette liste contient quatre objets de type Bord, cette liste ne changera plus
    - **position** : c'est la position de la pièce dans le puzzle, ce qui nous intéresse,
      c'est la position finale de la pièce dans le puzzle, cette information
      va donc bouger au fur et à mesure que nous allons essayer de
      résoudre le puzzle
    - **orientation** : de même que pour la position, une pièce peut être tournée sans changer de
      position, c'est le résultat final qui nous intèresse

    pour l'affichage, on ajoute deux informations :

    - **name** : le nom de l'image de la pièce
    - **image** : c'est la représentation de l'image dans la mèmoire de
      l'ordinateur pour le module pygame
    """

    def __init__(self, name, definition, position, numero):
        """
        on définit la pièce

        @param  name        nom de l'image représentant la pièce
        @param  definition  chaîne de 8 caractères, c'est une suite de 4 x 2 caractères définissant
                            chaque bord, voir la classe bord pour leur signification
        @param  position    c'est la position initiale de la pièce, on suppose que
                            l'orientation est nulle pour commencer
        @param  numero      numéro de la pièce

        à partir de ces informations, on construit :

        - **image** : c'est la représentation en mémoire de l'image de la pièce
        - **bord** : c'est une liste qui définit les 4 bords de la pièce
        - **orientation** : c'est l'orientation de la pièce, au début de la résolution, elle est nulle
        """
        self.name = name
        self.bord = []

        for i in range(0, 4):
            self.bord.append(PuzzleGirafeBord(definition[i * 2:i * 2 + 2]))

        self.orientation = 0
        self.position = position
        self.numero = numero

    def load_image(self, pygame):
        """
        charge l'image pour une simulation graphique

        @param      pygame      moulde pygame
        """
        image = pygame.image.load(self.name)
        self.image = pygame.transform.scale(image, (250, 250))
        s = self.image.get_size()
        self.image_petite = pygame.transform.scale(
            self.image, (int(s[0] * 0.7), int(s[1] * 0.7)))

    def __str__(self):
        """
        définition ce qu'on doit afficher lorsqu'on exécute
        l'instruction print avec un objet de type @see cl PuzzleGirafePiece.
        """
        s = str(self.position) + " : "
        for b in self.bord:
            s += str(b) + " - "
        s += " orientation " + str(self.orientation)
        s += " numero " + str(self.numero)
        return s

    def bord_angle(self, angle, orientation=None):
        """
        retourne le bord connaissant l'orientation de la pièce,
        le bord demandé est celui correspondant à :

        - 0  bord droit
        - 90 bord haut
        - 180 bord gauche
        - 270 bord bas
        """
        if orientation is None:
            return self.bord_angle(angle, self.orientation)
        else:
            dif = (angle - orientation + 360) % 360 // 90
            return self.bord[dif]

    def voisin_possible(self, p, a):
        """
        détermine si la pièce *self* peut être voisine avec la pièce *p* tournée de l'angle *a*
        """
        d = p.position - self.position
        if abs(d) == 1 and (p.position - 1) // 3 == (self.position - 1) // 3:
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

        b1 = self.bord_angle(a1)
        b2 = p.bord_angle(a2, a)
        return b1.compatible(b2)


class PuzzleGirafe:
    """
    définition d'une classe puzzle, elle contient simplement
    une liste de 9 pièces dont les positions sont ::

        1 2 3
        4 5 6
        7 8 9

    et les orientations choisies dans l'ensemble *{ 0,90,180,270 }*

    Voir :ref:`l-puzzle_girafe`.
    """

    def __init__(self):
        """
        on définit le puzzle à partir des informations contenues
        dans le répertoire *data* de ce module qui doit contenir :

        - 9 images appelées ``piece1.png``, ..., ``piece0.png``
        - un fichier ``definition_puzzle_girafe.txt`` contenant la définition de
          chacun des 4 bords de chacune des 9 pièces::

            HOBBBVHM
            HOBBBVHM
            HBBMBVHO
            HMBBBVHB
            BMBOHBHV
            HVBMBOHM
            BMBVHBHO
            HVHMBBBO
            BMHOHVBB
        """
        dir = os.path.abspath(os.path.dirname(__file__))
        dir = os.path.join(dir, "data")

        with open(os.path.join(dir, "definition_puzzle_girafe.txt"), "r") as f:
            bo = f.readlines()

        # on définit chaque pièce
        self.piece = []
        for i in range(1, 10):
            name = os.path.join(dir, "piece%d.png" % i)
            d = bo[i - 1]
            p = PuzzleGirafePiece(name, d, 0, i)
            self.piece.append(p)

    def load_images(self, pygame):
        """
        charge les images pour une simulation graphique

        @param      pygame      moulde pygame
        """
        for p in self.piece:
            p.load_image(pygame)

    def __str__(self):
        """
        ce qu'on doit afficher lorsqu'on exécute
        l'instruction print avec un objet de type @see cl PuzzleGirafe.
        """
        s = """1 2 3
                4 5 6
                7 8 9
                """.replace("                ", "")
        for p in self.piece:
            s += str(p) + "\n"
        return s

    def pixel(self, position):
        """
        retourne en fonction de la position (1 à 9) de la pièce sa position sur l'écran,
        soit deux coordonnées

        @return         tuple *(x,y)*
        """
        p = position - 1
        ligne = p // 3
        colonne = p % 3
        return (colonne * 250, ligne * 250)

    def meilleure_piece(self, free, pos):
        """
        retourne la prochaine pièce à placer sur le puzzle,
        dans un premier temps, on peut prend la première qui vient,
        ensuite, on peut essayer un choix plus judicieux
        """
        if len(free) == 0:
            return None
        else:
            return free[0]

    def piece_position(self, pi):
        """
        recherche la piece associée à la position pi
        """
        for p in self.piece:
            if p.position == pi:
                return p
        return None

    def ensemble_voisin(self, i):
        """
        retourne les positions voisins de la position i
        """
        i -= 1
        res = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if abs(x) == abs(y):
                    continue
                if x == -1 and i % 3 == 0:
                    continue
                if x == 1 and i % 3 == 2:
                    continue
                if y == -1 and i // 3 == 0:
                    continue
                if y == 1 and i // 3 == 2:
                    continue
                j = i + x + y * 3
                if j in range(0, 9):
                    res.append(j)
        return [j + 1 for j in res]

    def nb_place(self):
        """
        retourne le nombre de places vides
        """
        i = 0
        for p in self.piece:
            if p.position == 0:
                i += 1
        return i

    def angle_possible(self, p, display=False):
        """
        retourne l'ensemble des angles possibles pour une pièce donnée
        """
        voisin = self.ensemble_voisin(p.position)
        if display:
            print("voisin = ", voisin)
        res = []
        for a in [0, 90, 180, 270]:
            r = True
            for v in voisin:
                piece = self.piece_position(v)
                if piece is not None:
                    r = r and piece.voisin_possible(p, a)
            if r:
                res.append(a)
        return res

    def solution(self, pos=1, screen=None, pygame=None, images=None, delay=200):
        """
        résoud le puzzle de façon récursive : on pose une pièce puis on résoud
        le puzzle restant (une pièce en moins, une case en moins)

        @param      pos         niveau de récursivité
        @param      screen      image pygame
        @param      pygame      module pygame
        @param      images      stores images in this list if not None
        @param      delay       delay between two tries

        L'affichage *pygame* est optionnel.
        """
        if pos == 1:
            for p in self.piece:
                p.position = 0
            self.nb_position = 0
            self.essai = 0

        self.essai += 1

        if self.nb_position == len(self.piece):
            time.sleep(0.2)
            return

        # le tableau free mémorise l'ensemble des pièces non encore placées
        free = []
        for p in self.piece:
            if p.position == 0:
                free.append(p)

        if screen is not None and pygame is not None and images is not None:
            empty_main_loop(pygame)
            display_puzzle_girafe(self, screen, True, pygame=pygame)
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
            # l'appel à self.solution et on enlève le choix précédemment testé
            free2 = free
            free = []
            for f in free2:
                if f.numero != p.numero:
                    free.append(f)

            # on passe au choix suivant avec free contenant les pièces
            # placées et les pièces essayées
            p = self.meilleure_piece(free, pos)


def display_puzzle_girafe(self, screen, petite=False, pygame=None):
    """
    affiche les pièces sur l'écran,
    en plus petit pour celles qui ne sont pas encore placées
    """
    screen.fill((0, 0, 0))
    free = [0 for i in self.piece]
    for p in self.piece:
        if p.position > 0:
            p.darker = False
            display_puzzle_girafe_piece(
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
                display_puzzle_girafe_piece(
                    p, screen, self.pixel(em[i]), pygame)
                i += 1

    pygame.display.flip()


def display_puzzle_girafe_piece(self, screen, position, pygame):
    """
    affiche la pièce en tenant compte de sa position et de son orientation
    """
    if "darker" in self.__dict__ and self.darker:
        position = (position[0] + 20, position[1] + 20)
        image = pygame.transform.rotate(self.image_petite, self.orientation)
        screen.blit(image, position)
    else:
        image = pygame.transform.rotate(self.image, self.orientation)
        screen.blit(image, position)


def pygame_simulation(pygame, first_click=False, folder=None,
                      size=(750, 750), fLOG=fLOG, delay=200):
    """
    Simulation graphique.
    Illuste la résolution du puzzle

    @param      pygame          module pygame
    @param      first_click     attend la pression d'un clic de souris avant de commencer
    @param      folder          répertoire où stocker les images de la simulation
    @param      size            taille de l'écran
    @param      delay           delay between two tries
    @return                     @see cl PuzzleGirafe

    La simulation ressemble à ceci :

    .. raw:: html

        <video autoplay="" controls="" loop="" height="500">
        <source src="http://www.xavierdupre.fr/enseignement/complements/puzzle_girafe.mp4" type="video/mp4" />
        </video>

    Pour lancer la simulation::

        from ensae_teaching_cs.special.puzzle_girafe import pygame_simulation
        import pygame
        pygame_simulation(pygame)

    Voir :ref:`l-puzzle_girafe`.
    """
    # initialisation du module pygame
    pygame.init()
    screen = pygame.display.set_mode(size)

    # on définit le puzzle
    p = PuzzleGirafe()
    p.load_images(pygame)

    # on affiche le puzzle avec print (format texte)
    fLOG("\n" + str(p))

    # on affiche le puzzle à l'écran
    display_puzzle_girafe(p, screen, petite=True, pygame=pygame)
    if first_click:
        wait_event(pygame)

    # on rafraîchit l'écran pour que le puzzle apparaissent
    pygame.display.flip()

    if folder is not None:
        images = []
    else:
        images = None

    # on trouve la solution
    r = p.solution(screen=screen, pygame=pygame, images=images, delay=delay)
    fLOG("résolution ", r)
    fLOG("nombre d'appels à la méthode solution ", p.essai)

    if images is not None:
        empty_main_loop(pygame)
        display_puzzle_girafe(p, screen, True, pygame=pygame)
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
    display_puzzle_girafe(p, screen, petite=True, pygame=pygame)
    if first_click:
        wait_event(pygame)
