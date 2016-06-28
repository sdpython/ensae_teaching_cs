# coding: cp1252
"""implémentation du modèle d'illumination de Phong"""
import image_synthese_scene as scene
import image_synthese_base as base
import image_synthese_sphere as obj
import math
import pygame


class scene_phong (scene.scene):
    """définit une scène et utilise le modèle d'illumination de Phong
    pour construire l'image de synthèse"""
    
    def __init__ (self, repere, alpha, x,y,
                    ka          = 0.1,
                    kb          = 0.8,
                    kc          = 0.3,
                    reflet      = 6,
                    fond        = base.couleur (200,200,200)) :
        """définit la position de l'oeil, l'angle d'ouverture,
        et la taille de l'écran"""
        scene.scene.__init__ (self, repere, alpha, x, y)
        self.ka, self.kb, self.kc   = ka,kb,kc
        self.reflet                 = reflet
        self.fond                   = fond
        self.constante              = float (1)
        
    def __str__ (self) :
        """affichage"""
        s  = scene.scene.__str__ (self)
        s += "ka = %1.3f   kb = %1.3f   kc = %1.3f\n" % (self.ka,self.kb,self.kc)
        s += "reflet " + str (self.reflet) + "\n"
        s += "couleur du fond " + str (self.fond) + "\n"
        return s
        
    def couleur_fond (self) :
        """retourne la couleur du fond"""
        return self.fond * self.ka
        
    def modele_illumination (self, rayon, p, obj, source) :
        """calcule la couleur pour un rayon donné, un point p, un objet obj, 
        et une source de lumière source"""
        n   = obj.normale (p, rayon).renorme ()
        vr  = rayon.direction.renorme ()
        vr *= float (-1)
        vs  = source.origine - p
        vs  = vs.renorme ()
        bi  = vs + vr
        bi  = bi.renorme ()
        
        # premier terme
        cos      = n.scalaire (vs)
        couleur  = source.couleur.produit_terme (obj.couleur_point (p)) * (cos * self.kb)
        
        # second terme : reflet
        cos      = n.scalaire (bi) ** self.reflet
        couleur += source.couleur.produit_terme (source.couleur) * (cos * self.kc)
        couleur  = couleur.produit_terme (rayon.couleur)
        
        return couleur


if __name__ == "__main__" :
    s = scene_phong (base.repere (), math.pi / 1.5, 400, 300)

    s.ajoute_source ( base.source (base.vecteur (0,10,10), \
                        base.couleur (1,1,1) ) )
    s.ajoute_source ( base.source (base.vecteur (10,10,5), \
                        base.couleur (0.5,0.5,0.5) ) )
    s.ajoute_objet  ( obj.sphere  (base.vecteur (0,0,12), \
                        3, base.couleur (1,0,0) ) )
    s.ajoute_objet  ( obj.sphere  (base.vecteur (0,-400,12), \
                        396, base.couleur (0.5,0.5,0.5) ) )
    print s
    
    screen  = pygame.display.set_mode (s.dim)
    screen.fill ((255,255,255))
    s.construit_image (screen)

    print "image terminée"
    scene.attendre_clic ()

