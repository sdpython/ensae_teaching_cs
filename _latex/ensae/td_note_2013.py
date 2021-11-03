#coding:latin-1
import td_note_2013_novembre_2012_exoS as exoS

# question 1, exo S (1 ou 4)
def voisins_a_valeurs_nulle (matrice,i,j) :
    res = []
    if i > 0                 and matrice[i-1][j] == 0 : res.append ( (i-1,j) )
    if i < len(matrice)-1    and matrice[i+1][j] == 0 : res.append ( (i+1,j) )
    if j > 0                 and matrice[i][j-1] == 0 : res.append ( (i,  j-1) )
    if j < len(matrice[i])-1 and matrice[i][j+1] == 0 : res.append ( (i,  j+1) )
    return res
    
# question 2, exo S (1 ou 4)
def tous_voisins_a_valeurs_nulle (matrice, liste_points) :
    res = []
    for i,j in liste_points :
        res += voisins_a_valeurs_nulle (matrice, i,j) 
    return res
    
# question 3, exo S (1 ou 4)
def fonction_coloriage ( matrice, i0, j0) :
    # étage 1
    acolorier = [ ( i0, j0 ) ]
    while len (acolorier) > 0 :
        # étape 2
        for i,j in acolorier : 
            matrice [i][j] = 2
        # étape 3
        acolorier = tous_voisins_a_valeurs_nulle ( matrice, acolorier )
        # on enlève les doublons car sinon cela prend trop de temps
        d = { }
        for i,j in acolorier : d [i,j] = 0
        acolorier = [ (i,j) for i,j in d ]
        
# question 5, exo S (version 1)
def surface_coloriee (matrice) :
    surface = 0
    for line in matrice : 
        for c in line : 
            if c == 2 : surface += 1
    return surface
    
# question 5, exo S (version 4)
def fonction_coloriage_1000 ( matrice, i0, j0) :
    acolorier = [ ( i0, j0 ) ]
    nb = 0                                 # ligne ajoutée
    while len (acolorier) > 0 :
        for i,j in acolorier : 
            matrice [i][j] = 2
            nb += 1                        # ligne ajoutée
        if nb > 1000 : break               # ligne ajoutée
        acolorier = tous_voisins_a_valeurs_nulle ( matrice, acolorier )
        d = { }
        for i,j in acolorier : d [i,j] = 0
        acolorier = [ (i,j) for i,j in d ]

# question 4, exo S (1 ou 4)
matrice = exoS.construit_matrice(100)
fonction_coloriage  (matrice, 53, 53)
exoS.dessin_matrice(matrice)
print surface_coloriee (matrice) # retourne 3258

# question 5, exo S (version 4) vérification
matrice = exoS.construit_matrice(100)
fonction_coloriage_1000  (matrice, 53, 53)
exoS.dessin_matrice(matrice)
print surface_coloriee (matrice) # retourne 1002