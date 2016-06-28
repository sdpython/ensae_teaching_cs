# coding: cp1252
import random                 # pour tirer aléatoirement des nombres
import math                   # fonction sqrt
import PIL.Image as Im        # pour les images
import PIL.ImageDraw as Id    # pour dessiner

infini = 10000000 # l'infini est égal à dix millions, c'est une variable globale

def construit_ville(n, x =1000, y = 800):
    """tire aléatoirement n villes dans un carrée x * y, on choisit
    ces villes de sortent qu'elles ne soient pas trop proches"""
    # deux villes ne pourront pas être plus proches que mind
    mind = math.sqrt (x*x+y*y) / (n * 0.75)
    # liste vide
    l = []
    while n > 0:
        # on tire aléatoirement les coordonnées d'une ville
        xx = x * random.random ()
        yy = y * random.random ()
        # on vérifie qu'elle n'est pas trop proche d'aucune autre ville
        ajout = True
        for t in l :
            d1 = t [0] - xx
            d2 = t [1] - yy
            d  = math.sqrt (d1*d1+d2*d2)
            if d < mind :
                ajout = False  # ville trop proche
        # si la ville n'est pas trop proche des autres, on l'ajoute à la liste
        if ajout:
            l.append ((xx,yy))
            n -= 1  # une ville en moins à choisir
    return l

def distance_ville (l,i,j):
    """calcule la distance entre deux villes i et j de la liste l"""
    x = l [i][0] - l [j][0]
    y = l [i][1] - l [j][1]
    return math.sqrt (float (x*x+y*y))

def construit_arete (l,part = 0.15):
    """tire aléatoirement part * len (l) arêtes et construit la matrice
    d'adjacence"""
    global infini
    nb  = len (l)
    m   = [ [ 0 for i in range(0,nb) ] for i in range (0,nb) ] # crée un vecteur de nb zéros

    are = int (part * nb * nb)
    while are > 0:
        i = random.randint (0,nb-1)            # première ville
        j = random.randint (0,nb-1)            # seconde ville
        if i == j : continue                   # pas besoin d'arête entre i et i
        if m [i][j] > 0: continue               # si l'arête existe déjà, on recommence
        m [i][j] = int (distance_ville (l,i,j)) # on affecte comme poids à l'arête
                                                # la distance entre les deux villes
        m [j][i] = m [i][j] # symétrie de la matrice car le graphe est non orienté
        are -= 2            # deux cases de la matrice ne sont plus nulles

    # on associe à toutes les arêtes nulles de poids nul, donc inexistantes,
    # une valeur égale à l'infini pour signifier qu'elles ne sont pas reliées
    global infini
    for i in range (0, nb):
        for j in range (0, nb):
            if m [i][j] == 0:
                m [i][j] = infini

    return m

def dessin_ville_arete (l,m,chemin):
    """dessine la ville et les routes dans une image"""

    # on prend les coordonnées maximales
    mx, my = 0,0
    for i in l:
        mx = max (mx, i [0])
        my = max (my, i [1])
    mx += 25
    my += 25
    mx, my = int (mx), int (my)
    im = Im.new ("RGB", (mx, my), (255,255,255)) # création d'une image blanche
    draw = Id.Draw(im)

    # dessin des villes
    for i in l:
        j  = (int (i [0]), int (i[1]))
        j2 = (j [0] + 10, j [1] + 10)
        draw.ellipse ((j,j2), fill = (0,0,0))

    # dessin des arêtes
    global infini
    for i in range (0,len(l)):
        for j in range (0,len(l)):
            if m [i][j] > 0 and m [i][j] < infini :
                a = (int (l [i][0]+5), int (l [i][1]+5))
                b = (int (l [j][0]+5), int (l [j][1]+5))
                draw.line ((a,b),fill=(255,0,0))

    # dessin des villes de départ et d'arrivée en vert
    v1 = chemin [0]
    v2 = chemin [ len (chemin)-1]
    a = (int (l [v1][0]), int (l [v1][1]))
    b = (int (l [v1][0]+10), int (l [v1][1]+10))
    draw.ellipse ((a,b), fill = (0,255,0))
    a = (int (l [v2][0]), int (l [v2][1]))
    b = (int (l [v2][0]+10), int (l [v2][1]+10))
    draw.ellipse ((a,b), fill = (0,255,0))

    # dessin du chemin, arêtes en bleu
    for c in range (0,len(chemin)-1):
        i = chemin [c]
        j = chemin [c+1]
        if m [i][j] > 0 and m [i][j] < infini :
            a = (int (l [i][0]+5), int (l [i][1]+5))
            b = (int (l [j][0]+5), int (l [j][1]+5))
            draw.line ((a,b),fill=(0,0,255))
        else:
            a = (int (l [i][0]+5), int (l [i][1]+5))
            b = (int (l [j][0]+5), int (l [j][1]+5))
            draw.line ((a,b),fill=(0,0,50))

    # on retourne l'image
    return im

def meilleur_chemin (n,m,a,b):
    """détermine le meilleur chemin,
    n est le nombre de villes,
    m est la matrice d'adjacence,
    a est la ville de départ,
    b la ville d'arrivée"""

    # création d'un tableau, d [i] contient la meilleure distance minimale actuelle
    # séparant la ville i de la ville a
    d = [ 10000000 for i in range(0,n) ]

    # p [i] contient la ville prédécesseur qui permet d'atteindre la ville i
    # avec la distance d [i]
    p = [ -1 for i in range(0,n) ]

    # au départ, seul la distance d[a] est nulle
    d [a] = 0

    # cette boucle s'exécute tant qu'on effectue des mises à jour
    # dans le tableau d[i]
    modif = 1
    while modif > 0:
        modif = 0
        # on parcourt toutes les arêtes
        for i in range(0,n):
            for j in range (0,n):
                # nouvelle distance
                t = d [i] + m [i][j]
                if t < d [j] :  # si on a trouvé une meilleure distance minimale
                    d [j] = t   # on met à jour
                    p [j] = i
                    modif += 1  # une mise à jour de plus

    # on récupère le meilleur chemin
    l = []
    while b != -1:
        l.append (b)
        b = p [b]
    # on le retourne
    l.reverse ()
    return l

def choix_villes_depart_arrive(nb,m):
    """cette fonction choisit deux villes aléatoirement, départ et arrivée,
    elle évite que la ville et départ et d'arrivée soient les mêmes,
    elle évite que ces deux villes soient reliés par un seul arc,
    elle choisit deux villes pour lesquelles il existe un meilleur
    chemin"""
    global infini
    a,b = -1,-1
    tour = 0
    while True:
        a = random.randint (0,nb-1)     # première ville au hasard
        b = random.randint (0,nb-1)     # seconde ville au hasard
        if a == b: continue             # villes identiques, on recommence
        if m [a][b] != infini : continue # villes reliées, on recommence
        l = meilleur_chemin (nb,m,a,b)
        if l != None and len(l) > 3 :
            return a,b  # si le meilleur chemin existe,
                        # et n'est pas trop court (4 villes minimum,
                        # soit deux étapes entre a et b), alors
                        # on retourne le résultat
        else:
            tour += 1
            if tour > 120 : return 0,0       # au bout de 120 essais, on s'arrête

###############################################################################
# programme principal
# construction des villes
l = construit_ville (15)

# construction des arêtes
print "adjacence"
m = construit_arete (l)

# choix de la ville de départ de d'arrivée
print "départ"
a,b = choix_villes_depart_arrive(len(l),m)

print "recherche du meilleur chemin"
chemin  = meilleur_chemin (len(l), m, a,b)

if chemin != None and len(chemin) > 0:
    print "meilleur chemin ", a, " --> ", b, " : ", chemin
    # construction de l'image du résultat
    im = dessin_ville_arete(l,m,chemin)
    im.save ("image.png")
    im.show ()  # on affiche l'image
else :
    print "il n'existe pas de meilleur chemin"

