#-*- coding: utf-8 -*-
"""
ce module contient la fonction trace_ligne qui retourne l'ensemble des pixels
concernés par le tracé d'une ligne en 8-connexité entre deux pixels
"""


def trace_ligne_simple(x1, y1, x2, y2):
    """
    trace une ligne entre les points de coordonnées *(x1,y1)* et *(x2,y2)*,
    on suppose que *x2 > x1*, *y2 >= y1*,
    retourne la ligne sous la forme d'un ensemble de pixels *(x,y)*"""

    if y2 - y1 <= x2 - x1:  # droite en dessous de la première bissectrice
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
    else:                   # droite au dessus de la première bissectrice
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


def draw_line(x1, y1, x2, y2):
    """trace une ligne entre les points de coordonnées (x1,y1) et (x2,y2),
    aucune contrainte sur les coordonnées,
    retourne la ligne sous la forme d'un ensemble de pixels (x,y)"""

    if x1 == x2:
        if y1 <= y2:
            return [(x1, i) for i in range(y1, y2 + 1)]
        else:
            return [(x1, i) for i in range(y2, y1 + 1)]

    if y1 == y2:
        if x1 <= x2:
            return [(i, y1) for i in range(x1, x2 + 1)]
        else:
            return [(i, y1) for i in range(x2, x1 + 1)]

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


def display_line(ligne, screen, pygame):
    """
    affiche une ligne à l'écran
    """
    color = 0, 0, 0
    for p in ligne:
        pygame.draw.line(screen, color, p, p)
    pygame.display.flip()
