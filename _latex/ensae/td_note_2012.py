# coding: latin-1
# ce fichier contient le programme fournit au début de l'examen
# http://www.xavierdupre.fr/enseignement/examen_python/python_examen_2011_2012.py
from td_note_2012_enonce import *
import numpy, pylab

########################################################################
# exercice 1
########################################################################

# question 1 (+1=1p)
donnees = charge_donnees ()
colonne = donnees [0]
matrice = numpy.array (donnees [1:], dtype=float)

mat     = matrice
mat     = mat [ mat [:,3] > 0, : ]

# question 2 (+1=2p)
mat [ mat[:,3] == 1, 3 ] = 24
mat [ mat[:,3] == 2, 3 ] = 24*7
mat [ mat[:,3] == 3, 3 ] = 24*30

# question 3 (+1=3p)
res = mat [:,2] / mat [:,3]
print res.sum() / res.shape [0]       # 0.111 ~ 11,1% du temps passé devant la télévision
print res.sum() / res.shape [0] * 24  # soit 2h40min

# question 4 (+2=5p)
m = mat[:,1] * mat[:,2] / mat[:,3]
print m.sum() / mat[:,1].sum()        # 0.108 ~ 10,8%

# question 5 (+1=6p)
m = mat[ mat[:,2] > mat[:,3], : ]
print m  # il y a deux personnes et la raison la plus probable est une erreur dans l'unité de temps

# question 6 (+2=8p)
res = numpy.sort (res, 0)
print res[res.shape[0]/2]   # 0.083 ~ 8.3% = 2h

# question 7 (+2=10p)
pr = numpy.zeros ((mat.shape[0],4)) 
pr [:,0] = mat[:,2] / mat[:,3]
pr [:,1] = mat[:,1]
pr [:,2] = pr[:,0] * pr[:,1]
pr = numpy.sort (pr, 0)
total = pr[:,2].sum()
pr[0,3] = pr [0,2] 
for i in xrange (1, pr.shape[0]) :
    pr[i,3] = pr[i-1,3] + pr[i,2]
    if pr[i,3]/total > 0.5 :
        fin = i
        break
print pr[fin,3] / pr[:fin+1,1].sum()  # 0.0895 ~ 8.95%
    
########################################################################
# exercice 2
########################################################################

# question 1 (+1=1p)
temperature = charge_donnees("cannes_charleville_2010_max_t.txt")

def conversion_reel (temperature) :
    return [ [ float (x) for x in l ] for l in temperature [1:] ]

temperature = conversion_reel(temperature)

#question 2  (+2=3p)
def valeur_manquante (temperature, c) :
    for i in xrange (1, len (temperature)-1) :
        if temperature [i][c] == -1000 :
            temperature [i][c] = (temperature [i-1][c] + temperature [i+1][c]) / 2

valeur_manquante(temperature, 3)
valeur_manquante(temperature, 4)

def dessin_temperature (temperature) :
    import pylab
    u = [ t[3] for t in temperature ]
    v = [ t[4] for t in temperature ]
    pylab.plot (u)
    pylab.plot (v)
    pylab.show()

# on met en commentaire pour éviter de l'exécuter à chaque fois
# dessin_temperature(temperature)

# question 3 (+1=4p)

def distance (u,t) :
    return (u-t)**2
    
# question 4 (+3=7p)

def somme_ecart (temperature, t1, t2, T) :
    s = 0
    for i in xrange (0, len(temperature)) :
        if t1 < i < t2 :
            s += distance (temperature[i][3], T) # charleville
        else :
            s += distance (temperature[i][4], T) # cannes
    return s

# question 5 (+3=10p)

def minimisation (temperature, T) :
    best = 1e10
    t1t2 = None
    for t1 in xrange (0,len(temperature)) :
        for t2 in xrange (t1+1,len(temperature)) :
            d = somme_ecart(temperature,t1,t2,T)
            if best == None or d < best :
                best = d
                t1t2 = t1,t2
    return t1t2, best
    
#for i in range (300,363) : print "*",somme_ecart (temperature, i, i+2, 20)
print temperature [191]
print temperature [266]
for T in range (15, 25) :
    print T, "**",minimisation (temperature,T) # (191 = 11/7, 266 = 24/9)  (attendre 2 minutes)

# question 6
# Le coût de l'algorithme est on O(n^2) car l'optimisation est une double boucle sur les températures.
# Passer des jours aux semaines, c'est utiliser des séries 7 fois plus courtes, 
# l'optimisation sera 7^2 fois plus rapide.
