# coding: latin-1
import string

class SecondeInserstion (AttributeError):
    "insertion d'un mot déjà inséré"

class NoeudTri :
    
    def __init__(self,s): self.mot = s
        
    # la création d'un nouveau noeud a été placée dans une méthode
    def nouveau_noeud (self, s) : 
        return self.__class__ (s)
        #return NoeudTri (s)
        
    def __str__(self):
        s = ""
        if "avant" in self.__dict__: s += self.avant.__str__ ()
        s += self.mot + "\n"
        if "apres" in self.__dict__: s += self.apres.__str__()
        return s

    def insere (self,s):
        c = cmp (s, self.mot)
        if c == -1:
            if "avant" in self.__dict__ : self.avant.insere (s) # délégation
            else :  self.avant = self.nouveau_noeud (s)         # création
        elif c == 1:
            if "apres" in self.__dict__ : self.apres.insere (s) # délégation
            else: self.apres = self.nouveau_noeud (s)           # création
        else:
            raise SecondeInsertion, "mot : " + s
        
l = ["un", "deux", "unite", "dizaine", "exception", "dire", \
     "programme", "abc", "xyz", "opera", "quel"]
     
racine = None
for mot in l :
    if racine == None : 
        # premier cas : aucun mot --> on crée le premier noeud
        racine = NoeudTri (mot)
    else : 
        # second cas : il y a déjà un mot, on ajoute le mot suivant 
        # à l'arbre
        racine.insere (mot)

print racine