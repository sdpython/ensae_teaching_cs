# -*- coding: utf-8 -*-
"""
@file
@brief définition des objets permettant de construire une image de synthèse
"""
import math
import copy


class Vecteur (object):
    """définit ce qu'est un point"""
    __slots__ = "x", "y", "z"

    def __str__(self):
        """pour l'affichage"""
        return "(%3.2f,%3.2f,%3.2f)" % (self.x, self.y, self.z)

    def __init__(self, x, y, z):
        """initialisation"""
        self.x, self.y, self.z = float(x), float(y), float(z)

    def __add__(self, p):
        """addition de deux points"""
        return Vecteur(self.x + p.x, self.y + p.y, self.z + p.z)

    def __neg__(self):
        """retourne l'opposé d'un vecteur"""
        return Vecteur(-self.x, -self.y, -self.z)

    def __iadd__(self, p):
        """addition de deux points"""
        self.x += p.x
        self.y += p.y
        self.z += p.z
        return self

    def __sub__(self, p):
        """soustraction de deux points"""
        return Vecteur(self.x - p.x, self.y - p.y, self.z - p.z)

    def __isub__(self, p):
        """soustraction de deux points"""
        self.x -= p.x
        self.y -= p.y
        self.z -= p.z
        return self

    def __mul__(self, x):
        """multiplication par un scalaire"""
        return Vecteur(self.x * x, self.y * x, self.z * x)

    def __imul__(self, x):
        """multiplication par un scalaire"""
        self.x *= x
        self.y *= x
        self.z *= x
        return self

    def __truediv__(self, x):
        """division par un scalaire"""
        return Vecteur(self.x / x, self.y / x, self.z / x)

    def __itruediv__(self, x):
        """division par un scalaire"""
        self.x /= x
        self.y /= x
        self.z /= x
        return self

    def norme2(self):
        """retourne la norme du vecteur au carré"""
        return self.x * self.x + self.y * self.y + self.z * self.z

    def scalaire(self, v):
        """calcule le produit scalaire entre self et v"""
        return self.x * v.x + self.y * v.y + self.z * v.z

    def vectoriel(self, v):
        """calcule le produit vectoriel entre self et v"""
        res = Vecteur(0, 0, 0)
        res.x = self.y * v.z - self.z * v.y
        res.y = self.z * v.x - self.x * v.z
        res.z = self.x * v.y - self.y * v.x
        return res

    def norme(self):
        """retourne la norme du vecteur"""
        return math.sqrt(self.norme2())

    def renorme(self):
        """renorme ce vecteur"""
        n = self.norme()
        if n > 0:
            return self / n
        else:
            return copy.copy(self)

    def cosinus(self, v):
        """retourne le cosinus de entre le vecteur self et le vecteur r"""
        sc = self.scalaire(v)
        n1 = self.norme()
        n2 = v.norme()
        n = n1 * n2
        if n == 0:
            return 0
        return float(sc) / float(n)

    def sinus(self, v, norm):
        """retourne le sinus de entre le vecteur self et le vecteur r,
        norm est un vecteur normal et de norme 1 permettant d'orienter
        le plan dans lequel se trouve les deux vecteurs dont il faut mesurer le sinus"""
        sc = self.vectoriel(v)
        n1 = self.norme()
        n2 = v.norme()
        n = n1 * n2
        if n == 0:
            return 0
        return sc.scalaire(norm) / float(n)

    def angle(self, v, norm):
        """retourne l'angle entre les vecteur self et v,
        retourne un angle compris entre -pi et pi,
        norm est la direction du vecteur normal au plan des deux vecteurs"""
        cos = self.cosinus(v)
        sin = self.sinus(v, norm)
        angle = math.atan2(sin, cos)
        if angle > math.pi:
            angle -= math.pi * 2
        return angle

    def diff_abs(self, v):
        """retourne la somme des valeurs absolues des différentes entre coordonnées"""
        r = abs(self.x - v.x)
        r += abs(self.y - v.y)
        r += abs(self.z - v.z)
        return r

    def __eq__(self, v):
        """définit l'égalité entre deux vecteurs"""
        if v is None:
            return False
        return self.diff_abs(v) < 1e-10

    def __ne__(self, v):
        """définit l'égalité entre deux vecteurs"""
        if v is None:
            return True
        return self.diff_abs(v) > 1e-10


class Couleur (Vecteur):
    """une couleur est un vecteur dont les coordonnées sont comprises entre 0 et 1,
    x <--> rouge, y <--> vert, z <--> bleu"""

    def __init__(self, x, y, z):
        Vecteur.__init__(self, x, y, z)
        self.borne()

    def borne(self):
        """si une couleur est hors bornes, réajuste la couleur, prend le maximum devient 1,
        les autres intensités sont ajustées selon ce facteur d'échelle"""
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.z < 0:
            self.z = 0
        m = max(self.x, self.y)
        m = max(m, self.z)
        if m > 1:
            self.x /= m
            self.y /= m
            self.z /= m

    def __add__(self, p):
        """addition de deux couleurs"""
        return Couleur(self.x + p.x, self.y + p.y, self.z + p.z)

    def produit_terme(self, v):
        """effectue un produit terme à terme"""
        return Couleur(self.x * v.x, self.y * v.y, self.z * v.z)

    def __mul__(self, x):
        """multiplication par un scalaire"""
        return Couleur(self.x * x, self.y * x, self.z * x)


class Repere (object):
    """définition d'un repère orthonormé"""

    def __init__(self, origine=Vecteur(0, 0, 0),
                 axex=Vecteur(1, 0, 0),
                 axey=Vecteur(0, 1, 0),
                 axez=Vecteur(0, 0, 1)):
        """initialisation, origine et les trois axes"""
        self.origine = origine
        self.x = axex
        self.y = axey
        self.z = axez

    def coordonnees(self, v):
        """on suppose que les coordonnées de v sont exprimées dans ce repère,
        calcule les coordonnées de v dans le repère d'origine"""
        res = copy.copy(self.origine)
        res.x += v.x * self.x.x + v.y * self.y.x + v.z * self.z.x
        res.y += v.x * self.x.y + v.y * self.y.y + v.z * self.z.y
        res.z += v.x * self.x.z + v.y * self.y.z + v.z * self.z.z
        return res

    def __str__(self):
        """affichage"""
        s = "origine : " + str(self.origine) + "\n"
        s += "axe des x : " + str(self.x) + "\n"
        s += "axe des y : " + str(self.y) + "\n"
        s += "axe des z : " + str(self.z) + "\n"
        return s


class Pixel (object):
    """définit ce qu'est un pixel"""
    __slots__ = "x", "y"

    def __init__(self, x, y):
        """initialisation"""
        self.x, self.y = int(x), int(y)

    def __str__(self):
        """pour l'affichage"""
        return "(%d, %d)" % (self.x, self.y)


class Rayon (object):
    """définit ce qu'est un rayon"""
    __slots__ = "origine", "direction", "pixel", "couleur"

    def __init__(self, origine, direction, pixel, couleur):
        """initialisation"""
        self.origine, self.direction, self.pixel, self.couleur = origine, direction, pixel, couleur

    def __str__(self):
        """pour l'affichage"""
        s = "origine   : " + str(self.origine)
        s += " direction : " + str(self.direction)
        s += " pixel : " + str(self.pixel)
        s += " couleur : " + str(self.couleur)
        return s


class Objet (object):
    """définit l'interface pour un objet à dessiner dans une image de synthese"""

    def intersection(self, r):
        """retourne le point d'intersection avec le rayon r,
        retourne None s'il n'y pas d'intersection"""
        return None

    def normale(self, p, rayon):
        """retourne la normale au point de coordonnée p, et connaissant le rayon"""
        return None

    def couleur_point(self, p):
        """retourne la couleur au point de coordonnée p"""
        return None

    def rayon_refracte(self, rayon, p):
        """retourne le rayon réfracté au point p de la surface,
        si aucune, retourne None"""
        return None

    def rayon_reflechi(self, rayon, p):
        """retourne le rayon réfléchi au point p de la surface,
        si aucune, retourne None"""
        return None

    def phong_coefficient(self):
        """retourne un coefficient propre à l'objet pour
        le modèle d'illumination de Phong"""
        return float(0)


class Source (object):
    """définition d'une source ponctuelle"""
    __slots__ = "origine", "couleur"

    def __init__(self, origine, couleur):
        """initialisation"""
        self.origine, self.couleur = origine, couleur

    def __str__(self):
        """affichage"""
        return "source : " + str(self.origine) + " couleur : " + str(self.couleur)
