# coding: cp1252
"""définition d'une scène"""
import image_synthese_base as base
import image_synthese_sphere as obj
import math
import pygame

class scene (object):
    """définit une scène, les axes x,y sont ceux de l'écran, 
    z-1 est la distance à l'écran du point (x,y,z)"""
    
    def __init__ (self, repere, alpha, x,y) :
        """définit la position de l'oeil, l'angle d'ouverture,
        et la taille de l'écran"""
        self.repere = repere
        self.alpha  = float (alpha)
        self.dim    = (int (x), int (y))
        
    def ajoute_source (self, source):
        """ajoute une source ponctuelle de lumière"""
        if "sources" not in self.__dict__: 
            self.sources = []
        self.sources.append (source)
        
    def ajoute_objet (self, objet):
        """ajoute un objet à la scène"""
        if "objets" not in self.__dict__: 
            self.objets = []
        self.objets.append (objet)
        
    def __str__ (self) :
        """affichage"""
        s  = "scène ----------------------------\n"
        s += "repère : " + str (self.repere) + "\n"
        s += "angle d'ouverture : " + str (self.alpha) + "\n"
        s += "dimension de l'écran : " + str (self.dim) + "\n"
        if "sources" in self.__dict__:
            for a in self.sources : s += "   " +str (a) + "\n"
        if "objets" in self.__dict__:
            for a in self.objets :  s += "   " + str (a) + "\n"
        return s
        
    def intersection (self, rayon) : 
        """calcule le point d'intersection entre un rayon et le plus proche des objets,
        retourne l'objet et le point d'intersection"""
        if "objets" not in self.__dict__: return None, None
        p       = rayon.origine
        sp,so   = None, None
        for o in self.objets :
            i = o.intersection (rayon)
            if i == None : continue
            if rayon.direction.scalaire (i - p) <= 0 : continue 
            if i == rayon.origine : continue 
            if sp == None : 
                sp  = i
                so  = o
            else :
                v = i - p
                d = sp - p
                if v.norme2 () < d.norme2 () :
                    sp = i
                    so = o
        return so, sp                
                
    def sources_atteintes (self, p) : 
        """retourne la liste des sources atteintes depuis une position p de l'espace,
        vérifie qu'aucun objet ne fait obstacle"""
        res = []
        for s in self.sources:
            r   = base.rayon (s.origine, p - s.origine, base.pixel (0,0), s.couleur)
            o,i = self.intersection (r)
            if i == None : continue
            if (i - p).norme2 () < 1e-10 :   # possible problème d'arrondi
                res.append (s)
                continue
        return res
                        
    def construit_rayon (self, pixel) :
        """construit le rayon correspondant au pixel pixel"""
        x = (pixel.x - self.dim [0] / 2) * math.tan (self.alpha / 2) / min (self.dim)
        y = (pixel.y - self.dim [1] / 2) * math.tan (self.alpha / 2) / min (self.dim)
        v = base.vecteur (x,y,1)
        r = base.rayon (self.repere.origine, self.repere.coordonnees (v), \
                            pixel, base.couleur (1,1,1))
        return r
        
    def modele_illumination (self, rayon, p, obj, source) :
        """calcule la couleur pour un rayon donné, un point p, un objet obj, 
        et une source de lumière source"""
        n   = obj.normale (p, rayon)
        cos = n.cosinus (source.origine - p)
        cl  = obj.couleur_point (p) * cos
        cl  = cl.produit_terme (rayon.couleur)
        return cl
        
    def couleur_fond (self) :
        """retourne la couleur du fond"""
        return base.couleur (0,0,0)
        
    def rayon_couleur (self, rayon, ref = True) :
        """retourne la couleur d'un rayon connaissant les objets,
        cette fonction doit être surchargée pour chaque modèle d'illumination, 
        si ref == True, on tient compte des rayons réfracté et réfléchi"""
        
        list_rayon = [ rayon ]
        c = base.couleur (0,0,0)
        b = False
        while len (list_rayon) > 0 :
            r   = list_rayon.pop ()
            o,p = self.intersection (r)

            if p == None : continue
                
            if ref :
                t   = o.rayon_refracte (r, p)
                if t != None : list_rayon.append (t)
                t   = o.rayon_reflechi (r, p)
                if t != None : list_rayon.append (t)
                
            sources = self.sources_atteintes (p)
            if len (sources) == 0 : return base.couleur (0,0,0)
            for s in sources :
                cl  = self.modele_illumination (r, p, o, s)
                c  += cl
                b   = True

        if not b : c = self.couleur_fond ()
        else : c.borne ()
        return c        
        
    def construit_image (self, screen):
        """construit l'image de synthèse où screen est un objet du module pygame"""
        count   = 0
        nbpixel = int (self.dim [0] * self.dim [1] / 100)
        for y in range (0, self.dim [1]) :
            for x in range (0, self.dim [0]) :
                p = base.pixel (x,y)
                r = self.construit_rayon (p)
                c = self.rayon_couleur (r, True)
                q = (p.x,self.dim [1] - p.y - 1) 
                d = (int (c.x * 255), int (c.y * 255), int (c.z * 255))
                pygame.draw.line (screen, d, q,q)
                count += 1
                if count % 150 == 0 : pygame.display.flip ()
                if count % nbpixel == 0 : print ("avancement " , count // nbpixel , "%")
        pygame.display.flip ()


def attendre_clic ():
    """dessine une croix sur l'écran et attend la pression d'un clic de souris"""
    reste = True
    while reste:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP :
                reste = False
                break


if __name__ == "__main__" :
    s = scene (base.repere (), math.pi / 1.5, 400, 300)
    s.ajoute_source ( base.source (base.vecteur (0,10,10), \
                        base.couleur (1,1,1) ) )
    s.ajoute_source ( base.source (base.vecteur (10,10,5), \
                        base.couleur (0.5,0.5,0.5) ) )
    s.ajoute_objet  ( obj.sphere  (base.vecteur (0,0,12), \
                        3, base.couleur (1,0,0) ) )
    s.ajoute_objet  ( obj.sphere  (base.vecteur (0,-400,12), \
                        396, base.couleur (0.5,0.5,0.5) ) )
    print (s)
    
    screen  = pygame.display.set_mode (s.dim)
    screen.fill ((255,255,255))
    s.construit_image (screen)

    print ("image terminée")
    attendre_clic ()

