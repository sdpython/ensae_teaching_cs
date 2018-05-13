# -*- coding: utf-8 -*-
"""
@file
@brief Ce module contient la fonction trace_ligne qui retourne l'ensemble des pixels
concernés par le tracé d'une ligne en 8-connexité entre deux pixels.
"""


def trace_ligne_simple(x1, y1, x2, y2):
    """
    Trace une ligne entre les points de coordonnées *(x1,y1)* et *(x2,y2)*,
    on suppose que *x2 > x1*, *y2 >= y1*,
    retourne la ligne sous la forme d'un ensemble de pixels *(x,y)*."""

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
    """
    Trace une ligne entre les points de coordonnées *(x1,y1)* et *(x2,y2)*,
    aucune contrainte sur les coordonnées,
    retourne la ligne sous la forme d'un ensemble de pixels *(x,y)*.
    Utilise l'algorithme de :epkg:`Bresenham`.
    """

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

    raise RuntimeError("All cases have already been processed.")


def draw_ellipse(xc, yc, a, b):
    """
    Dessine une ellipse de centre *xc, yc*, de demi axe horizontal *a*,
    de demi-axe vertical b, l'ellipse a pour équation x²/a² + y²/b² = 1
    si l'origine est placée en *xc, yc*,
    l'équation de la tangente au point *x0, y0* est :
    :math:`\frac{x x_0}{a^2} + \frac{y y_0}{b^2}=0`,
    ou :math:`x x_0 b^2 + y y_0 a^2 = 0`.
    Utilise l'algorithme de :epkg:`Bresenham`.
    """

    # on évite les cas litigieux
    if a == 0:
        return [(xc, yc + y) for y in range(-b, b)]
    if b == 0:
        return [(xc + x, yc) for x in range(-a, a)]

    bb = b * b
    aa = a * a

    # on trace l'ellipse de centre 0,0
    ellipse = []
    # premier huitième
    vx = a * bb
    vy = 0
    x = a
    y = 0
    bl = vx / 2

    while vx >= vy and x >= 0:
        ellipse.append((x, y))
        y += 1
        vy += aa        # vy  = y * aa
        bl -= vy
        if bl < 0:
            x -= 1
            vx -= bb    # vx  = x * bb
            bl += vx

    # second huitième
    while x >= 0:
        ellipse.append((x, y))
        x -= 1
        vx -= bb        # vx  = x * bb
        bl += vx
        if bl > 0:
            y += 1
            vy += aa    # vy  = y * aa
            bl -= vy

    # second quart, symétrique par rapport à l'axe des ordonnées
    ellipse2 = [(-x, y) for (x, y) in ellipse]
    ellipse2.reverse()
    ellipse.extend(ellipse2)

    # troisième et quatrième quarts : symétrique par rapport à l'axe des
    # abscisse
    ellipse2 = [(x, -y) for (x, y) in ellipse]
    ellipse2.reverse()
    ellipse.extend(ellipse2)

    return [(x + xc, y + yc) for (x, y) in ellipse]


def display_line(ligne, screen, pygame):
    """
    Affiche une ligne à l'écran.
    """
    color = 0, 0, 0
    for p in ligne:
        pygame.draw.line(screen, color, p, p)
    pygame.display.flip()
