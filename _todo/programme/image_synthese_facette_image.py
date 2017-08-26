# coding: cp1252
"""d�finition d'une sph�re"""
import image_synthese_base as base
import image_synthese_sphere as obj
import image_synthese_phong as scene
import image_synthese_scene as scene_p
import image_synthese_facette as facette
import pygame
import math
import psyco

       
        
class rectangle_image (facette.rectangle):
    """d�finit un rectangle contenant un portrait"""
    
    def __init__(self, a,b,c,d, nom_image, invertx = False):
        """initialisation, si d == None, d est calcul� comme �tant 
        le sym�trique de b par rapport au milieu du segment [ac],
        la texture est une image, 
        si invertx == True, inverse l'image selon l'axe des x"""
        facette.rectangle.__init__(self, a,b,c,d, base.couleur (0,0,0))
        self.image      = pygame.image.load (nom_image)
        self.nom_image  = nom_image
        self.invertx    = invertx

    def __str__ (self):
        """affichage"""
        s  = "rectangle image --- a : " + str (self.a)
        s += " b : " + str (self.b)
        s += " c : " + str (self.c)
        s += " d : " + str (self.d)
        s += " image : " + self.nom_image
        return s
        
    def couleur_point (self, p) :
        """retourne la couleur au point de coordonn�e p"""
        ap  = p - self.a
        ab  = self.b - self.a
        ad  = self.d - self.a
        abn = ab.norme2 ()
        adn = ad.norme2 ()
        x   = ab.scalaire (ap) / abn
        y   = ad.scalaire (ap) / adn
        sx,sy = self.image.get_size ()
        k,l   = int (x * sx), int (y * sy)
        k   = min (k, sx-1)
        l   = min (l, sy-1)
        l   = sy - l - 1
        if not self.invertx :
            c   = self.image.get_at ((k,l))
        else :
            c   = self.image.get_at ((sx-k-1,l))
        cl  = base.couleur (float (c [0]) / 255, float (c [1]) / 255, float (c [2]) / 255)
        return cl

class sphere_reflet (obj.sphere) :
    """impl�mente une sph�re avec un reflet"""
    
    def __init__ (self, centre, rayon, couleur, reflet):
        """initialisation, reflet est un coefficient de r�flexion"""
        obj.sphere.__init__ (self, centre, rayon, couleur)
        self.reflet = reflet
        
    def __str__ (self):
        """affichage"""
        s  = "sph�re reflet --- centre : " + str (self.centre)
        s += " rayon : " + str (self.rayon)
        s += " couleur : " + str (self.couleur)
        return s

    def rayon_reflechi (self, rayon, p) :
        """retourne le rayon r�fl�chi au point p de la surface,
        si aucune, retourne None"""
        if p == rayon.origine : return None
        n = self.normale (p, rayon)
        n = n.renorme ()
        y = n.scalaire (rayon.direction)
        d = rayon.direction - n * y * 2
        r = base.rayon (p, d, rayon.pixel, rayon.couleur * self.reflet)
        return r

        
if __name__ == "__main__" :
    
    psyco.full ()
    
    s = scene.scene_phong (base.repere (), math.pi / 1.5, 400, 200)

    s.ajoute_source ( base.source (base.vecteur (0,8,8), \
                        base.couleur (0.4,0.4,0.4) ) )
    s.ajoute_source ( base.source (base.vecteur (10,0,0), \
                        base.couleur (0.4,0.4,0.4) ) )
    s.ajoute_source ( base.source (base.vecteur (8,8,4.5), \
                        base.couleur (0.4,0.4,0.4) ) )
    s.ajoute_objet  ( obj.sphere  (base.vecteur (3,-4,7), \
                        1, base.couleur (1,0,0) ) )
    s.ajoute_objet  ( sphere_reflet  (base.vecteur (0,-400,12), \
                        396, base.couleur (0.5,0.5,0.5), 0.5 ) )
                        
    s.ajoute_objet (rectangle_image ( base.vecteur (8,-3.5,9),   \
                               base.vecteur (2,-3.5,8), \
                               base.vecteur (2,3.8,8), \
                               None, \
                               "bette_davis.png",
                               invertx = True))

    s.ajoute_source ( base.source (base.vecteur (7,2,8), \
                        base.couleur (0.2,0.2,0.2) ) )
    s.ajoute_source ( base.source (base.vecteur (12.5,3,5), \
                        base.couleur (0.2,0.2,0.2) ) )
                        
    s.ajoute_source ( base.source (base.vecteur (-12.5,1,6), \
                        base.couleur (0.2,0.2,0.2) ) )
                        
    s.ajoute_objet (facette.rectangle ( base.vecteur (-12.4,0.99,5.9),   \
                               base.vecteur (-12.6,0.99,5.9), \
                               base.vecteur (-12.6,0.99,6.1), \
                               None, \
                               base.couleur (0,0,0)))
                               
    print s
    
    screen  = pygame.display.set_mode (s.dim, flags)
    screen.fill ((255,255,255))
    s.construit_image (screen)

    print "sauvegarde de l'image"
    im = pygame.display.get_surface()
    print "image size : ", im.get_size ()
    pygame.image.save (im, "c:\\temp\\image.jpg")
    pygame.image.save (im, "c:\\temp\\image.tif")
    pygame.image.save (im, "c:\\temp\\image.bmp")

    print "image termin�e"
    scene_p.attendre_clic ()
       
    
    

