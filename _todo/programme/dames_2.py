def pion_prendre(i,j,damier):
   c = damier [(i,j)]       # ou encore damier [i,j]
   if c == 0: return False  # case vide, impossible de prendre
   c = 3 - c                # couleur de l'adversaire

   # test pour une prise du pion dans les quatre cases voisines
   if damier [i-1,j-1] == c and damier [i-2,j-2] == 0: return True
   if damier [i-1,j+1] == c and damier [i-2,j+2] == 0: return True
   if damier [i+1,j-1] == c and damier [i+2,j-2] == 0: return True
   if damier [i+1,j+1] == c and damier [i+2,j+2] == 0: return True
        
   # si tous les tests ont échoué, on ne peut pas prendre
   return False