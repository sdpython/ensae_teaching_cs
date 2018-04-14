# -*- coding: utf-8 -*-
"""
@file
@brief image et synthèse
"""

from .image_synthese_facette import Rectangle
from .image_synthese_base import Rayon, Couleur
from .image_synthese_sphere import Sphere


class RectangleImage(Rectangle):
    """définit un rectangle contenant un portrait"""

    def __init__(self, a, b, c, d, nom_image, pygame, invertx=False):
        """initialisation, si d == None, d est calculé comme étant
        le symétrique de b par rapport au milieu du segment [ac],
        la texture est une image,
        si invertx == True, inverse l'image selon l'axe des x"""
        Rectangle.__init__(self, a, b, c, d, Couleur(0, 0, 0))
        self.image = pygame.image.load(nom_image)
        self.nom_image = nom_image
        self.invertx = invertx

    def __str__(self):
        """affichage"""
        s = "rectangle image --- a : " + str(self.a)
        s += " b : " + str(self.b)
        s += " c : " + str(self.c)
        s += " d : " + str(self.d)
        s += " image : " + self.nom_image
        return s

    def couleur_point(self, p):
        """retourne la couleur au point de coordonnée p"""
        ap = p - self.a
        ab = self.b - self.a
        ad = self.d - self.a
        abn = ab.norme2()
        adn = ad.norme2()
        x = ab.scalaire(ap) / abn
        y = ad.scalaire(ap) / adn
        sx, sy = self.image.get_size()
        k, li = int(x * sx), int(y * sy)
        k = min(k, sx - 1)
        li = min(li, sy - 1)
        li = sy - li - 1
        if not self.invertx:
            c = self.image.get_at((k, li))
        else:
            c = self.image.get_at((sx - k - 1, li))
        cl = Couleur(float(c[0]) / 255, float(c[1]) / 255, float(c[2]) / 255)
        return cl


class SphereReflet (Sphere):
    """implémente une sphère avec un reflet"""

    def __init__(self, centre, rayon, couleur, reflet):
        """initialisation, reflet est un coefficient de réflexion"""
        Sphere.__init__(self, centre, rayon, couleur)
        self.reflet = reflet

    def __str__(self):
        """affichage"""
        s = "sphere reflet --- centre : " + str(self.centre)
        s += " rayon : " + str(self.rayon)
        s += " couleur : " + str(self.couleur)
        return s

    def rayon_reflechi(self, rayon, p):
        """retourne le rayon réfléchi au point p de la surface,
        si aucune, retourne None"""
        if p == rayon.origine:
            return None
        n = self.normale(p, rayon)
        n = n.renorme()
        y = n.scalaire(rayon.direction)
        d = rayon.direction - n * y * 2
        r = Rayon(p, d, rayon.pixel, rayon.couleur * self.reflet)
        return r
