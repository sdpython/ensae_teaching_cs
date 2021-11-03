# coding: latin-1
import urllib2, math

# question 1
def lit_fichier () :
    # le principe est le même que pour le chargement d'un fichier
    # le programme lit directement les informations depuis Internet
    f = urllib2.urlopen ("http://www.xavierdupre.fr/enseignement"\
                         "/examen_python/restaurant_paris.txt")
    s = f.read ()
    f.close ()
    lines = s.split ("\n")  # on découpe en lignes
    # on découpe en colonnes
    lines = [ _.strip ("\n\r ").split ("\t") for _ in lines if len (_) > 0 ]  
    lines = [ _ for _ in lines if len (_) == 3 ]  # on supprime les lignes vides
    # on convertit les coordonnées en réel
    lines = [ (a [3:], float (b), float (c)) for a,b,c in lines ]
    return lines
    
# question 2
def compte_restaurant (mat) :
    # simple comptage, voir le chapitre 3...
    compte = { }
    for cp,x,y in mat :
        if cp not in compte : compte [cp] = 0
        compte [cp] += 1
    return compte
    
# question 3
def barycentre (mat) :
    # un barycentre est un point (X,Y)
    # où X et Y sont respectivement la moyenne des X et des Y
    barycentre = { }
    # boucle sur la matrice
    for cp,x,y in mat :
        if cp not in barycentre : barycentre [cp] = [ 0, 0.0, 0.0 ]
        a,b,c           = barycentre [cp]
        barycentre [cp] = [a+1, b+x, c+y]
    # boucle sur les barycentres
    for cp in barycentre :
        a,b,c = barycentre [cp]
        barycentre [cp] = [b/a, c/a]
        
    # le coût de cette fonction est en O (n log k)
    # où k est le nombre de barycentre
    # de nombreux élèves ont deux boucles imbriquées, 
    # d'abord sur la matrice, ensuite sur les barycentres
    # ce qui donne un coût en O (nk), beaucoup plus grand
    return barycentre
    
# question 4 
def distance (x1, y1, x2, y2) :
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

# question 5
def plus_proche_restaurant (x,y, arr, mat) :
    m,mx,my = None, None, None
    for cp,a,b in mat :
        if cp != arr and (m == None or distance (a,b,x,y) < m) :
            mx,my = a,b
            m     = distance (a,b,x,y)
    return mx,my
    
# question 6
def densite_approchee (mat) :
    g      = barycentre (mat)
    compte = compte_restaurant (mat)
    res    = { }
    
    for cp in g :
        out  = plus_proche_restaurant (g [cp][0], g [cp][1], cp, mat)
        r    = distance (g [cp][0], g [cp][1], out [0], out [1])
        aire = math.pi * r ** 2
        res [cp] = compte [cp] / aire
        
    return res
    
if __name__ == "__main__" :
    
    if False :  #mettre à vrai pour remplacer la fonction plus_proche_restaurant
        # ajout par rapport à l'énoncé
        # en réponse à la dernière question
        # plutôt que de prendre le premier point à hors de l'arrondissement
        # on considère celui correspondant à un quantile (5%)
        # ce qui évite les quelques restaurants dont les données
        #sont erronées
        def plus_proche_restaurant_avec_amelioration (x,y, arr, mat) :
            all     = []
            for cp,a,b in mat :
                if cp != arr :
                    m = distance (a,b,x,y)
                    all.append ( (m,a,b))
            all.sort ()
            a,b = all [len(all)/20][1:]
            return a,b
            
        # ajout par rapport à l'énoncé
        plus_proche_restaurant = plus_proche_restaurant_avec_amelioration
    
    mat = lit_fichier ()
    com = densite_approchee (mat)
    ret = [ (v,k) for k,v in com.iteritems () ]
    ret.sort ()
    for a,b in ret : print "%d\t%s" % (a,b)
        
    # ajout par rapport à l'énoncé
    # permet de dessiner les restaurants, une couleur par arrondissement
    # on observe que certains points sont aberrants, ce qui réduit d'autant 
    # l'estimation du rayon d'un arrondissement (il suffit qu'un restaurant 
    # étiquetés dans le 15ème soit situé près du barycentre du 14ème.)
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.mlab as mlab
    import matplotlib.cbook as cboo

    fig = plt.figure()
    ax = fig.add_subplot(111)
    colors = [  'red', 'blue', 'yellow', 'orange', 'black', 'green', 
                'purple', 'brown', 'gray', 'magenta', 'cyan', 'pink', 'burlywood',
                'chartreuse', '#ee0055']
    for cp in barycentre (mat) :
        lx = [ m[1] for m in mat if m [0] == cp ]
        ly = [ m[2] for m in mat if m [0] == cp ]
        c  = colors [ int(cp) % len (colors) ]
        #if cp not in ["02", "20"] : continue
        ax.scatter(lx,ly, s = 5., c=c,edgecolors = 'none'  )
    plt.show ()
        
        
        
    