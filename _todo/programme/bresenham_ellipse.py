# coding: cp1252
"""ce module contient la fonction trace_ellipse qui retourne l'ensemble des pixels
concernés par le tracé d'une ellipse en 8-connexité"""
import pygame                 # pour les affichages
import random
import math


def trace_ellipse(xc, yc, a, b):
    """dessine une ellipse de centre xc,yc, de demi axe horizontal a,
    de demi-axe vertical b, l'ellipse a pour équation x²/a² + y²/b² = 1
    si l'origine est placée en xc,yc,
    l'équation de la tangente au point x0, y0 est :  x x0 / a² + y y0 / b² = 0,
    ou x x0 b² + y y0 a² = 0"""

    # on évite les cas litigieux
    if a == 0:
        return [(xc, yc + y) for y in xrange(-b, b)]
    if b == 0:
        return [(xc + x, yc) for x in xrange(-a, a)]

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


def display_ligne(ensemble, screen):
    """affiche un ensemble de pixels à l'écran"""
    color = 0, 0, 0
    for p in ensemble:
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

    size = width, height = x, y = 300, 300
    black = 0, 0, 0
    white = 255, 255, 255
    screen = pygame.display.set_mode(size)
    screen.fill(white)

    print trace_ellipse(0, 0, 6, 6)
    # pour le premier quart, affiche
    # [(6, 0), (6, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 6), (0, 6), ...

    for n in xrange(0, 10):
        x1 = random.randint(0, x - 1)
        y1 = random.randint(0, y - 1)
        x2 = random.randint(0, x - 1)
        y2 = random.randint(0, y - 1)
        xc, yc = (x1 + x2) / 2, (y1 + y2) / 2
        a, b = abs(x2 - x1) / 2, abs(y2 - y1) / 2
        ell = trace_ellipse(xc, yc, a, b)
        display_ligne(ell, screen)

    attendre_clic(screen)
