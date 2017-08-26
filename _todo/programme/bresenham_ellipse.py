# coding: cp1252
"""ce module contient la fonction trace_ellipse qui retourne l'ensemble des pixels
concern�s par le trac� d'une ellipse en 8-connexit�"""
import pygame                 # pour les affichages
import random
import math


def trace_ellipse(xc, yc, a, b):
    """dessine une ellipse de centre xc,yc, de demi axe horizontal a,
    de demi-axe vertical b, l'ellipse a pour �quation x�/a� + y�/b� = 1
    si l'origine est plac�e en xc,yc,
    l'�quation de la tangente au point x0, y0 est :  x x0 / a� + y y0 / b� = 0,
    ou x x0 b� + y y0 a� = 0"""

    # on �vite les cas litigieux
    if a == 0:
        return [(xc, yc + y) for y in xrange(-b, b)]
    if b == 0:
        return [(xc + x, yc) for x in xrange(-a, a)]

    bb = b * b
    aa = a * a

    # on trace l'ellipse de centre 0,0
    ellipse = []
    # premier huiti�me
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

    # second huiti�me
    while x >= 0:
        ellipse.append((x, y))
        x -= 1
        vx -= bb        # vx  = x * bb
        bl += vx
        if bl > 0:
            y += 1
            vy += aa    # vy  = y * aa
            bl -= vy

    # second quart, sym�trique par rapport � l'axe des ordonn�es
    ellipse2 = [(-x, y) for (x, y) in ellipse]
    ellipse2.reverse()
    ellipse.extend(ellipse2)

    # troisi�me et quatri�me quarts : sym�trique par rapport � l'axe des
    # abscisse
    ellipse2 = [(x, -y) for (x, y) in ellipse]
    ellipse2.reverse()
    ellipse.extend(ellipse2)

    return [(x + xc, y + yc) for (x, y) in ellipse]


def display_ligne(ensemble, screen):
    """affiche un ensemble de pixels � l'�cran"""
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
    screen = pygame.display.set_mode(size, flags)
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
