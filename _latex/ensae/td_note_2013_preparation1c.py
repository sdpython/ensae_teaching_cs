#coding:latin-1
import random

def randomint (a,b,c) :
    x = random.random()
    if x <= a : return 0
    elif x <= a+b : return 1
    else : return 2

def sequence (a,b,c) :
    res = [  ]
    nb = 1
    while nb > 0 :
        i = randomint(a,b,c)
        nb += i - 1
        res.append (i)
    return res

def moyenne (nb_tirage,a,b,c) :
    somme = 0.0
    for i in range(nb_tirage) :
        s = sequence(a,b,c)
        somme += len(s)
    return somme / nb_tirage
    
a,c = 0.3, 0.2
b = 1-a-c

moy = 1.0 / (a-c)
print "calcul",moy

m1 = moyenne (100000, a,b,c)
print "simulée", m1