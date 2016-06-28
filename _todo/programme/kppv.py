# coding: cp1252
import math
import random


class nuage_points (object) :
    """définit une classe de nuage de points"""
    
    def __init__ (self) :
        """constructeur"""
        self.nb = 0         # aucun élément
        self.nuage = []     # aucun élément
        
    def __iter__(self) :
        """retourne un itérateur sur l'ensemble de points"""
        return self.nuage.__iter__ ()
        
    def __len__ (self) :
        """retourne le nombre d'élément"""
        return len (self.nuage)
        
    def distance (self, obj1, obj2) :
        """retourne une distance entre deux éléments obj1 et obj2"""
        return 0
        
    def label (self, obj) :
        """retourne le label d'un objet"""
        return None
        
    def ppv (self, obj) :
        """retourne l'élément le plus proche de obj et sa distance avec obj"""
        mn = None
        dm = None
        for l in self.nuage :
            d = self.distance (l, obj)
            if dm == None or d < dm :
                dm = d
                mn = l
        return mn,dm
        
    def ppv_nuage (self, nuage, bienclasse = None, erreur = None) :
        """calcule un taux de classification pour un nuage,
        utilise la fonction ppv pour chaque élément de nuage,
        retourne le nombre d'élément bien classés, et mal classés,
        si bienclasse est une liste vide (!= None), cette liste contiendra
        la liste des couples d'éléments (x,y) in (nuage, self) pour lesquels
        la classification est bonne,
        si erreur est une liste vide (!= None), cette liste contiendra 
        la liste des couples d'éléments (x,y) in (nuage,self) 
        pour lesquels la classification est mauvaise"""
        disp    = len (nuage) / 10 ;
        good    = 0
        bad     = 0
        n       = 0
        for x in nuage :
            obj,d = self.ppv (x)
            if self.label (obj) == self.label (x) : 
                good += 1
                if bienclasse != None : bienclasse.append ((obj,x))
            else : 
                bad += 1
                if erreur != None : erreur.append ((obj, x))
            if n % disp == 0 : print "ppv_nuage ", n * 100 / len (nuage), "%"
            n += 1
        return good, bad
        
