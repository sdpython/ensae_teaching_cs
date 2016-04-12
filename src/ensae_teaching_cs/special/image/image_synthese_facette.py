#-*- coding: utf-8 -*-
"""
@file
@brief définition d'une facette
"""
from .image_synthese_base import Objet
import math


class Facette (Objet):
    """définit un triangle dans l'espace"""

    def __init__(self, a, b, c, couleur):
        """initialisation"""
        self.a, self.b, self.c = a, b, c
        ab = b - a
        ac = c - a
        self.vnorm = ab.vectoriel(ac)
        self.vnorm = self.vnorm.renorme()
        self.couleur = couleur

    def intersection_plan(self, r):
        """retourne le point d'intersection entre le plan et le rayon r"""
        if r.direction.scalaire(self.vnorm) == 0:
            return None
        oa = self.a - r.origine
        l = self.vnorm.scalaire(oa) / self.vnorm.scalaire(r.direction)
        p = r.origine + r.direction * l
        return p

    def point_interieur(self, p):
        """dit si un point appartient à l'intérieur du triangle"""
        pa = self.a - p
        pb = self.b - p
        pc = self.c - p
        theta = pa.angle(pb, self.vnorm)
        theta += pb.angle(pc, self.vnorm)
        theta += pc.angle(pa, self.vnorm)
        theta = abs(theta)
        if theta >= math.pi * 0.9:
            return True
        else:
            return False

    def intersection(self, r):
        """retourne le point d'intersection avec le rayon r,
        retourne None s'il n'y pas d'intersection"""
        p = self.intersection_plan(r)
        if p is None:
            return None
        if self.point_interieur(p):
            return p
        else:
            return None

    def normale(self, p, rayon):
        """retourne la normale au point de coordonnée p et connaissant le rayon"""
        if rayon.direction.scalaire(self.vnorm) < 0:
            return self.vnorm
        else:
            return - self.vnorm

    def couleur_point(self, p):
        """retourne la couleur au point de coordonnée p"""
        return self.couleur

    def __str__(self):
        """affichage"""
        s = "facette --- a : " + str(self.a)
        s += " b : " + str(self.b)
        s += " c : " + str(self.c)
        s += " couleur : " + str(self.couleur)
        return s


class Rectangle (Facette):
    """définit un rectangle dans l'espace"""

    def __init__(self, a, b, c, d, couleur):
        """initialisation, si d == None, d est calculé comme étant
        le symétrique de b par rapport au milieu du segment [ac]"""
        Facette.__init__(self, a, b, c, couleur)
        if d is not None:
            self.d = d
        else:
            i = (a + c) / 2
            self.d = b + (i - b) * 2

    def point_interieur(self, p):
        """dit si un point appartient à l'intérieur du triangle"""
        pa = self.a - p
        pb = self.b - p
        pc = self.c - p
        pd = self.d - p
        theta = pa.angle(pb, self.vnorm)
        theta += pb.angle(pc, self.vnorm)
        theta += pc.angle(pd, self.vnorm)
        theta += pd.angle(pa, self.vnorm)
        theta = abs(theta)
        if theta >= math.pi * 0.9:
            return True
        else:
            return False

    def __str__(self):
        """affichage"""
        s = "rectangle --- a : " + str(self.a)
        s += " b : " + str(self.b)
        s += " c : " + str(self.c)
        s += " d : " + str(self.d)
        s += " couleur : " + str(self.couleur)
        return s
