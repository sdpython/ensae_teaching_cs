# coding: cp1252
import math
import random
import kppv


class nuage_point_laesa (kppv.nuage_points) :
    """implémente l'algorithme des plus proches voisins,
    version LAESA"""
    
    def __init__ (self) :
        """construit la classe"""
        kppv.nuage_points.__init__ (self)
        
    def selection_pivots (self,nb) :
        """sélectionne nb pivots aléatoirements"""
        nb = min (nb, len (self.nuage))
        self.pivots = []
        while len (self.pivots) < nb :
            i = random.randint (0,len (self.nuage))
            if not self.nuage [i] in self.pivots :
                self.pivots.append (self.nuage [i])
                
        # on calcule aussi la distance de chaque éléments au pivots
        self.dist = []
        for el in self.nuage :
            dl = []
            for p in self.pivots :
                d = self.distance (el, p)
                dl.append (d)
            self.dist.append (dl)                
                
    def ppv (self, obj) :
        """retourne l'élément le plus proche de obj et sa distance avec obj,
        utilise la sélection à l'aide pivots"""
        
        # initialisation
        dp  = [ self.distance (obj, p) for p in self.pivots ]
        
        # pivots le plus proche
        dm  = dp [0]
        im  = self.pivots [0] 
        for i in xrange (0, len(self.pivots)) :
            d = dp [i]
            if d < dm :
                dm = d
                im = self.pivots [i]
        
        # améliorations
        for i in xrange (0, len (self.nuage)) :
            
            # on regarde si un pivots permet d'éliminer l'élément i
            calcul = True
            for j in xrange (0, len (self.pivots)) :
                d = abs (dp [j] - self.dist[i][j])
                if d > dm :
                    calcul = False
                    break 


            # dans le cas contraire on calcule la distance
            if calcul :
                d = self.distance (obj, self.nuage [i])
                if d < dm :
                    dm = d 
                    im = self.nuage [i]
                
        return im,dm


