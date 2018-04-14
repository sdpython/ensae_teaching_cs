# -*- coding: utf-8 -*-
"""
@file
@brief définition d'une scène
"""
import math
from .image_synthese_base import Pixel, Vecteur, Rayon, Couleur


class Scene (object):
    """
    définit une scène, les axes x,y sont ceux de l'écran,
    z-1 est la distance à l'écran du point (x,y,z)
    """

    def __init__(self, repere, alpha, x, y):
        """définit la position de l'oeil, l'angle d'ouverture,
        et la taille de l'écran"""
        self.repere = repere
        self.alpha = float(alpha)
        self.dim = (int(x), int(y))

    def ajoute_source(self, source):
        """ajoute une source ponctuelle de lumière"""
        if not hasattr(self, "sources"):
            self.sources = []
        self.sources.append(source)

    def ajoute_objet(self, objet):
        """ajoute un objet à la scène"""
        if not hasattr(self, "objets"):
            self.objets = []
        self.objets.append(objet)

    def __str__(self):
        """affichage"""
        s = "scene ----------------------------\n"
        s += "repere : " + str(self.repere) + "\n"
        s += "angle d'ouverture : " + str(self.alpha) + "\n"
        s += "dimension de l'ecran : " + str(self.dim) + "\n"
        if hasattr(self, "sources"):
            for a in self.sources:
                s += "   " + str(a) + "\n"
        if hasattr(self, "objets"):
            for a in self.objets:
                s += "   " + str(a) + "\n"
        return s

    def intersection(self, rayon):
        """calcule le point d'intersection entre un rayon et le plus proche des objets,
        retourne l'objet et le point d'intersection"""
        if not hasattr(self, "objets"):
            return None, None
        p = rayon.origine
        sp, so = None, None
        for o in self.objets:
            i = o.intersection(rayon)
            if i is None:
                continue
            if rayon.direction.scalaire(i - p) <= 0:
                continue
            if i == rayon.origine:
                continue
            if sp is None:
                sp = i
                so = o
            else:
                v = i - p
                d = sp - p
                if v.norme2() < d.norme2():
                    sp = i
                    so = o
        return so, sp

    def sources_atteintes(self, p):
        """retourne la liste des sources atteintes depuis une position p de l'espace,
        vérifie qu'aucun objet ne fait obstacle"""
        res = []
        for s in self.sources:
            r = Rayon(s.origine, p - s.origine, Pixel(0, 0), s.couleur)
            o, i = self.intersection(r)
            if i is None:
                continue
            if (i - p).norme2() < 1e-10:   # possible problème d'arrondi
                res.append(s)
                continue
        return res

    def construit_rayon(self, pixel):
        """construit le rayon correspondant au pixel pixel"""
        x = (pixel.x - self.dim[0] / 2) * \
            math.tan(self.alpha / 2) / min(self.dim)
        y = (pixel.y - self.dim[1] / 2) * \
            math.tan(self.alpha / 2) / min(self.dim)
        v = Vecteur(x, y, 1)
        r = Rayon(self.repere.origine, self.repere.coordonnees(v),
                  pixel, Couleur(1, 1, 1))
        return r

    def modele_illumination(self, rayon, p, obj, source):
        """calcule la couleur pour un rayon donné, un point p, un objet obj,
        et une source de lumière source"""
        n = obj.normale(p, rayon)
        cos = n.cosinus(source.origine - p)
        cl = obj.couleur_point(p) * cos
        cl = cl.produit_terme(rayon.couleur)
        return cl

    def couleur_fond(self):
        """retourne la couleur du fond"""
        return Couleur(0, 0, 0)

    def rayon_couleur(self, rayon, ref=True):
        """retourne la couleur d'un rayon connaissant les objets,
        cette fonction doit être surchargée pour chaque modèle d'illumination,
        si ref == True, on tient compte des rayons réfractés et réfléchis"""

        list_rayon = [rayon]
        c = Couleur(0, 0, 0)
        b = False
        while len(list_rayon) > 0:
            r = list_rayon.pop()
            o, p = self.intersection(r)

            if p is None:
                continue

            if ref:
                t = o.rayon_refracte(r, p)
                if t is not None:
                    list_rayon.append(t)
                t = o.rayon_reflechi(r, p)
                if t is not None:
                    list_rayon.append(t)

            sources = self.sources_atteintes(p)
            if len(sources) == 0:
                return Couleur(0, 0, 0)
            for s in sources:
                cl = self.modele_illumination(r, p, o, s)
                c += cl
                b = True

        if not b:
            c = self.couleur_fond()
        else:
            c.borne()
        return c

    def construit_image(self, screen, pygame, fLOG):
        """construit l'image de synthèse où screen est un objet du module pygame"""
        count = 0
        nbpixel = int(self.dim[0] * self.dim[1] / 100)
        for y in range(0, self.dim[1]):
            for x in range(0, self.dim[0]):
                p = Pixel(x, y)
                r = self.construit_rayon(p)
                c = self.rayon_couleur(r, True)
                q = (p.x, self.dim[1] - p.y - 1)
                d = (int(c.x * 255), int(c.y * 255), int(c.z * 255))
                pygame.draw.line(screen, d, q, q)
                count += 1
                if count % 150 == 0:
                    pygame.display.flip()
                if count % nbpixel == 0:
                    fLOG("avancement ", count // nbpixel, "%")
        pygame.display.flip()
