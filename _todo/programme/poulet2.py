# coding: cp1252
import math
import random
import psyco
psyco.full ()

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
    
def histogramme_poisson (l, n = 1000) :
    h = [ 0.0 for i in range (0,4*l+1) ]
    for i in range (0, n) :
        x = poisson (l)
        if x < len (h) :
            h [x] += 1
    s = sum (h)
    for i in range (0, len (h)) :
        h [i] = float (h [i]) / s
    return h

def histogramme_poisson_melange (params, coef, n = 1000) :
    h = [ 0.0 for i in range (0, 4*max(params)+1) ]
    for i in range (0, n) :
        x = poisson_melange (params, coef)
        if x < len (h) :
            h [x] += 1
    s = sum (h)
    for i in range (0, len (h)) :
        h [i] = float (h [i]) / s
    return h

def factorielle(x):
     if x == 0: return 1
     else: return x * factorielle(x-1)
         
def profit (N,X,p,q,s) :
    if X <= N : return X * (q-p)
    else : return X * (s-p) + N * (q-s)

def proba_poisson (l, i) :
    try :
        x = math.exp (-l) * (l ** i) / factorielle (i)
        return x
    except :
        print "problème avec ", l,i
        return 0.0
    
    
def esperance (X,p,q,s,l) :
    res = 0.0
    for i in range (0,l*2) :
        res += profit (float (i),X,p,q,s) * proba_poisson (l,i)
    return res
    
def maximum (p,q,s,l) :
    res = []
    for X in range (0, 2 * l) :
        r = esperance (X,p,q,s,l) 
        res.append ((X,r))
    return res
    
def find_maximum (res) :
    m = (0,0)
    for r in res :
        if r [1] > m [1] :
            m = r
    return m
    
if __name__ == "__main__" :
    if False :
        res = maximum (2,5,1,80)
        m = find_maximum (res)
        print m    
        # dessin d'une courbe
        from pylab import *
        plot ( [ r [1] for r in res] )
        show ()
    
    if False :
        h = histogramme_poisson (10)
        for i in range (0, len (h)) :
            print i, "\t", h [i], "\t", proba_poisson (10, i)
        from pylab import *
        plot (h, "r")
        plot ([ proba_poisson (10, i) for i in range (0, len (h))])
        legend ( ["histogramme", u"densité" ] )
        show ()
        
    if True :
        h = histogramme_poisson_melange ([48,10,4], [1,2,3])
        from pylab import *
        plot (h, "r")
        plot ([ proba_poisson (80, i) for i in range (0, len (h))])
        legend ( [u"N1 + 2 N2 + 3 N3", \
                 u"Poisson (80)" ], "right") 
                 #prop = FontProperties(size='smaller'))
        help (legend)
        show ()