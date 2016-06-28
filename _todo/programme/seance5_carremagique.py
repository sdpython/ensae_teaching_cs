#coding:latin-1
class CarreMagique :
    def __init__(self, coef) :
        self.mat = [ [ coef[i+j*3] for i in range(3) ] for j in range(3) ]
    def __str__(self) :
        return "\n".join ( [ ",".join( [ str(n) for n in row ] ) for row in self.mat ] )
    def __add__ (self, carre) :
        coef = []
        for i in range(3) :
            for j in range(3) :
                coef.append ( self.mat[i][j] + carre.mat[i][j])
        return CarreMagique(coef)
        
    def somme_ligne_colonne_diagonale(self):
        tout = [ sum ( ligne ) for ligne in self.mat ] + \
               [ sum ( [ self.mat[i][j] for j in range(3) ] ) for i in range(3) ] + \
               [ sum ( [ self.mat[i][i] for i in range(3) ] ) ] + \
               [ sum ( [ self.mat[2-i][i] for i in range(3) ] ) ] 
        return tout
        
    def coefficient_unique(self): 
        d = { }
        for ligne in self.mat :
            for c in ligne :
                d [c] = d.get(c,0) + 1
        return len(d) == 9
        
    def est_magique(self):
        unique = self.coefficient_unique()
        if not unique : return False
        somme = self.somme_ligne_colonne_diagonale()
        return min(somme) == max(somme) 
        
def tous_les_carres_permutation_ligne12_meme_somme( permut = None, pos = 0):
    if pos == 9 :
        carre = CarreMagique (permut) 
        if carre.est_magique() :
            #print (carre)
            #print ()
            return [ carre ]
        else :
            return []
    else :
        if pos >= 6 :                                       # ajout
            if sum ( permut[:3]) != sum(permut[3:6]) :      # ajout
                return [ ]                                  # ajout
        
        res = [ ]
        if permut == None :
            permut = [ i+1 for i in range(9) ]
        for i in range (pos,9) :
            # on permute les éléments i et pos
            a = permut[i]
            permut[i] = permut[pos]
            permut[pos] = a

            res += tous_les_carres_permutation_ligne12_meme_somme(permut, pos+1)  # changé
            
            # on effectue la permutation inverse
            a = permut[i]
            permut[i] = permut[pos]
            permut[pos] = a
        return res
        
import time
d = time.clock()    
res = tous_les_carres_permutation_ligne12_meme_somme()
d = time.clock() - d
print ("nombre de carrés", len(res), " en ", d)
