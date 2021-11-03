#coding:latin-1
import random

# question 1
def sequence () :
    res = [ ]
    nb = 1
    while nb > 0 :
        i = random.randint(0,2)
        nb += i - 1
        res.append (i)
    return res

# question 2
def moyenne (nb_tirage) :
    somme = 0.0
    for i in range(nb_tirage) :
        s = sequence()
        somme += len(s)
    return somme / nb_tirage
    
s = sequence ()
print len(s),s
m = moyenne (100)
print m