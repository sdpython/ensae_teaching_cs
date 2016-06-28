# coding: cp1252
import math
import random
import psyco
psyco.full ()

proba_poisson_melange_tableau = []

def exponentielle (l) :
    u = random.random ()
    return - 1.0 / l * math.log (1.0 - u)
    
def poisson (l) :
    s = 0
    i = 0
    while s <= 1 :
        s += exponentielle (l)
        i += 1
    return i-1
    
def poisson_melange (params, coef) :
    s = 0
    for i in range (0, len (params)) :
        p = poisson (params [i])
        s += p * coef [i]
    return s
    
def histogramme_poisson_melange (params, coef, n = 100000) :
    h = [ 0.0 for i in range (0, 4*max(params)) ]
    for i in range (0, n) :
        x = poisson_melange (params, coef)
        if x < len (h) :
            h [x] += 1
    s = sum (h)
    for i in range (0, len (h)) :
        h [i] = float (h [i]) / s
    return h        

def profit (N,X,p,q,s) :
    if X <= N : return X * (q-p)
    else : return X * (s-p) + N * (q-s)
        
def proba_poisson_melange (params, coef, i) :
    global proba_poisson_melange_tableau
    if len (proba_poisson_melange_tableau) == 0 :
        proba_poisson_melange_tableau = histogramme_poisson_melange (params, coef)
    if i >= len (proba_poisson_melange_tableau) : return 0.0
    else : return proba_poisson_melange_tableau [i]
    
def esperance (X,p,q,s,params, coef) :
    res = 0.0
    for i in range (0,4*sum(params)) :
        res += profit (float (i),X,p,q,s) * proba_poisson_melange (params, coef,i)
    return res
    
def maximum (p,q,s,params, coef) :
    res = []
    for X in range (0, 4*sum (params)) :
        r = esperance (X,p,q,s,params, coef) 
        res.append ((X,r))
    return res
    
def find_maximum (res) :
    m = (0,0)
    for r in res :
        if r [1] > m [1] :
            m = r
    return m
    
if __name__ == "__main__" :
    res = maximum (2,5,1,[48,10,4], [1,2,3])
    m = find_maximum (res)
    print m    
    # dessin d'une courbe
    from pylab import *
    plot ( [ r [1] for r in res] )
    show ()