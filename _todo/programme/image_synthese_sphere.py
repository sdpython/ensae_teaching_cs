# coding: cp1252
"""définition d'une sphère"""
import image_synthese_base as base
import math

class sphere (base.objet):
    """définit une sphère"""
    __slots__ = "centre", "rayon", "couleur"
    
    def __init__ (self, centre, rayon, couleur):
        """initialisation"""
        self.centre, self.rayon, self.couleur = centre, float (rayon), couleur

    def intersection (self, r) :
        """retourne le point d'intersection avec le rayon r, 
        retourne None s'il n'y pas d'intersection"""
        oc      = self.centre - r.origine
        vn      = r.direction.norme2 ()
        s       = r.direction.scalaire (oc)
        delta   = s*s - vn * (oc.norme2 () - self.rayon * self.rayon)
        if delta < 0 : return None
        delta   = math.sqrt (delta)
        l1      = (s - delta) / vn
        l2      = (s + delta) / vn
        
        if      0 < l1 < l2 :   l = l1
        elif    l1 < 0 < l2 :   l = l2
        elif    0 < l2 < l1 :   l = l2
        elif    l2 < 0 < l1 :   l = l1
        else :                  l = None

        if l == None : return None

        v = r.origine + r.direction * l
        return v
        
    def normale (self, p, rayon) :
        """retourne la normale au point de coordonnée p"""
        v = (p - self.centre) / self.rayon
        return v     
        
    def couleur_point (self, p) :
        """retourne la couleur au point de coordonnée p"""
        return self.couleur
        
    def __str__ (self):
        """affichage"""
        s  = "sphère --- centre : " + str (self.centre)
        s += " rayon : " + str (self.rayon)
        s += " couleur : " + str (self.couleur)
        return s
        
        
        
if __name__ == "__main__" :
    s = sphere (base.vecteur (0,0,0), 5, base.couleur (0,1,0))
    r = base.rayon (    base.vecteur (10,0,0), base.vecteur (1,0,0), \
                        base.pixel (0,0), base.couleur (0,0,0))
    print (s)
    print (r)
    p = s.intersection (r)
    print (p)
    

