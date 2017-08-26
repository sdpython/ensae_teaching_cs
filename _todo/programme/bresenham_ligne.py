# coding: cp1252
"""ce module contient la fonction trace_ligne qui retourne l'ensemble des pixels
concern�s par le trac� d'une ligne en 8-connexit� entre deux pixels"""
import pygame                 # pour les affichages
import random


def trace_ligne_simple(x1, y1, x2, y2):
    """trace une ligne entre les points de coordonn�es (x1,y1) et (x2,y2),
    on suppose que x2 > x1, y2 >= y1,
    retourne la ligne sous la forme d'un ensemble de pixels (x,y)"""

    if y2 - y1 <= x2 - x1:  # droite en dessous de la premi�re bissectrice
        vx = x2 - x1
        vy = y2 - y1
        b = vx / 2
        y = y1
        x = x1

        ligne = []
        while x <= x2:
            ligne.append((x, y))
            b -= vy
            x += 1
            if b < 0:
                b += vx
                y += 1
        return ligne
    else:                   # droite au dessus de la premi�re bissectrice
        vx = x2 - x1
        vy = y2 - y1
        b = vy / 2
        y = y1
        x = x1

        ligne = []
        while y <= y2:
            ligne.append((x, y))
            b -= vx
            y += 1
            if b < 0:
                b += vy
                x += 1
        return ligne


def trace_ligne(x1, y1, x2, y2):
    """trace une ligne entre les points de coordonn�es (x1,y1) et (x2,y2),
    aucune contrainte sur les coordonn�es,
    retourne la ligne sous la forme d'un ensemble de pixels (x,y)"""

    if x1 == x2:
        if y1 <= y2:
            return [(x1, i) for i in xrange(y1, y2 + 1)]
        else:
            return [(x1, i) for i in xrange(y2, y1 + 1)]

    if y1 == y2:
        if x1 <= x2:
            return [(i, y1) for i in xrange(x1, x2 + 1)]
        else:
            return [(i, y1) for i in xrange(x2, x1 + 1)]

    if x1 < x2:
        if y1 < y2:
            return trace_ligne_simple(x1, y1, x2, y2)
        else:
            ligne = trace_ligne_simple(x1, y2, x2, y1)
            return [(x, y1 + y2 - y) for (x, y) in ligne]

    if x2 < x1:
        if y1 < y2:
            ligne = trace_ligne_simple(x2, y1, x1, y2)
            return [(x1 + x2 - x, y) for (x, y) in ligne]
        else:
            ligne = trace_ligne_simple(x2, y2, x1, y1)
            return [(x1 + x2 - x, y1 + y2 - y) for (x, y) in ligne]


def display_ligne(ligne, screen):
    """affiche une ligne � l'�cran"""
    color = 0, 0, 0
    for p in ligne:
        pygame.draw.line(screen, color, p, p)
    pygame.display.flip()


def attendre_clic(screen):
    """attend la pression d'un clic de souris pour continuer"""
    reste = True
    while reste:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                reste = False
                break

if __name__ == "__main__":
    pygame.init()

    size = width, height = x, y = 200, 200
    black = 0, 0, 0
    white = 255, 255, 255
    screen = pygame.display.set_mode(size, flags)
    screen.fill(white)

    print trace_ligne(0, 0, 7, 3)
    # affiche [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2), (5, 2), (6, 3), (7, 3)]

    for n in xrange(0, 10):
        x1 = random.randint(0, x - 1)
        y1 = random.randint(0, y - 1)
        x2 = random.randint(0, x - 1)
        y2 = random.randint(0, y - 1)
        ligne = trace_ligne(x1, y1, x2, y2)
        display_ligne(ligne, screen)

    attendre_clic(screen)
