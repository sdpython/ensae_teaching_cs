def pion_prendre(i,j,damier):
   c = damier [10*i+j]
   if c == 0: return False  # case vide, impossible de prendre
   c = 3 - c                # couleur de l'adversaire

   # test pour une prise du pion dans les quatre cases voisines
   if damier [10*(i-1)+j-1] == c and damier [10*(i-2)+j-2] == 0: return True
   if damier [10*(i-1)+j+1] == c and damier [10*(i-2)+j+2] == 0: return True
   if damier [10*(i+1)+j-1] == c and damier [10*(i+2)+j-2] == 0: return True
   if damier [10*(i+1)+j+1] == c and damier [10*(i+2)+j+2] == 0: return True
        
   return False