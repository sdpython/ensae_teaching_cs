# coding: cp1252
"""définition d'une sphère"""
import image_synthese_base as base
import image_synthese_sphere as obj
import image_synthese_phong as scene
import image_synthese_scene as scene_p
import pygame
import math

class facette (base.objet):
    """définit un triangle dans l'espace"""
    
    def __init__ (self, a,b,c, couleur):
        """initialisation"""
        self.a, self.b, self.c = a,b,c
        ab = b - a
        ac = c - a
        self.vnorm = ab.vectoriel (ac)
        self.vnorm = self.vnorm.renorme ()
        self.couleur = couleur
        
    def intersection_plan (self, r) :
        """retourne le point d'intersection entre le plan et le rayon r"""
        if r.direction.scalaire (self.vnorm) == 0 :
            return None
        oa      = self.a - r.origine 
        l       = self.vnorm.scalaire (oa) / self.vnorm.scalaire (r.direction)
        p       = r.origine + r.direction * l
        return p
        
    def point_interieur (self, p) :
        """dit si un point appartient à l'intérieur du triangle"""
        pa      = self.a - p        
        pb      = self.b - p        
        pc      = self.c - p   
        theta   = pa.angle (pb, self.vnorm)
        theta  += pb.angle (pc, self.vnorm)
        theta  += pc.angle (pa, self.vnorm)
        theta   = abs (theta)
        if theta >= math.pi * 0.9 : return True
        else : return False

    def intersection (self, r) :
        """retourne le point d'intersection avec le rayon r, 
        retourne None s'il n'y pas d'intersection"""
        p = self.intersection_plan (r)
        if p == None : return None
        if self.point_interieur (p) : return p
        else : return None
        
    def normale (self, p, rayon) :
        """retourne la normale au point de coordonnée p et connaissant le rayon"""
        if rayon.direction.scalaire (self.vnorm) < 0 :
            return self.vnorm
        else :
            return - self.vnorm 
        
    def couleur_point (self, p) :
        """retourne la couleur au point de coordonnée p"""
        return self.couleur
        
    def __str__ (self):
        """affichage"""
        s  = "facette --- a : " + str (self.a)
        s += " b : " + str (self.b)
        s += " c : " + str (self.c)
        s += " couleur : " + str (self.couleur)
        return s
        
        
class rectangle (facette):
    """définit un rectangle dans l'espace"""
    
    def __init__ (self, a,b,c,d, couleur):
        """initialisation, si d == None, d est calculé comme étant 
        le symétrique de b par rapport au milieu du segment [ac]"""
        facette.__init__(self, a,b,c, couleur)
        if d != None : self.d = d
        else :
            i       = (a + c) / 2
            self.d  = b + (i-b) * 2
        
    def point_interieur (self, p) :
        """dit si un point appartient à l'intérieur du triangle"""
        pa      = self.a - p        
        pb      = self.b - p        
        pc      = self.c - p   
        pd      = self.d - p   
        theta   = pa.angle (pb, self.vnorm)
        theta  += pb.angle (pc, self.vnorm)
        theta  += pc.angle (pd, self.vnorm)
        theta  += pd.angle (pa, self.vnorm)
        theta   = abs (theta)
        if theta >= math.pi * 0.9 : return True
        else : return False
        
    def __str__ (self):
        """affichage"""
        s  = "rectangle --- a : " + str (self.a)
        s += " b : " + str (self.b)
        s += " c : " + str (self.c)
        s += " d : " + str (self.d)
        s += " couleur : " + str (self.couleur)
        return s
        
       


        
if __name__ == "__main__" :
    
    s = scene.scene_phong (base.repere (), math.pi / 1.5, 400, 300)

    s.ajoute_source ( base.source (base.vecteur (0,8,8), \
                        base.couleur (0.6,0.6,0.6) ) )
    s.ajoute_source ( base.source (base.vecteur (10,0,0), \
                        base.couleur (0.6,0.6,0.6) ) )
    s.ajoute_source ( base.source (base.vecteur (8,8,4.5), \
                        base.couleur (0.6,0.6,0.6) ) )
    s.ajoute_objet  ( obj.sphere  (base.vecteur (1,0,5), \
                        1, base.couleur (1,0,0) ) )
    s.ajoute_objet  ( obj.sphere  (base.vecteur (0,-400,12), \
                        396, base.couleur (0.5,0.5,0.5) ) )
    s.ajoute_objet (facette ( base.vecteur (0,-2.5,6),   \
                               base.vecteur (-2,-2.5,3), \
                               base.vecteur (1,-3.5,4.5), \
                               base.couleur (0.2,0.8,0)))
    s.ajoute_objet (rectangle ( base.vecteur (0,-2.5,6),   \
                               base.vecteur (-2,-2.5,3), \
                               base.vecteur (-2,2.8,3.5), \
                               None, \
                               base.couleur (0,0,1)))
    print s
    
    screen  = pygame.display.set_mode (s.dim)
    screen.fill ((255,255,255))
    s.construit_image (screen)

    print "image terminée"
    scene_p.attendre_clic ()
    
    

