def pion_prendre(i,j,damier):
   c = damier [i][j]
   if c == 0: return False  # case vide, impossible de prendre
   c = 3 - c                # couleur de l'adversaire

   # on répète ce test pour les trois autres cases
   if i >= 2                 and j >= 2                  and \
      damier [i-1][j-1] == c and damier [i-2][j-2] == 0: return True
   if i >= 2                 and j < len (damier)-2      and \
      damier [i-1][j+1] == c and damier [i-2][j+2] == 0: return True
      
   if i < len (damier)-2     and j >= 2                  and \
      damier [i+1][j-1] == c and damier [i+2][j-2] == 0: return True
   if i < len (damier)-2     and j < len (damier)-2      and \
      damier [i+1][j+1] == c and damier [i+2][j+2] == 0: return True
        
   return False