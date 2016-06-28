import math

def factorielle(x):
     if x == 0: return 1
     else: return x * factorielle(x-1)
         
def profit (N,X,p,q,s) :
    if X <= N : return X * (q-p)
    else : return X * (s-p) + N * (q-s)

def proba_poisson (l, i) :
    return math.exp (-l) * (l ** i) / factorielle (i)
    
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
    res = maximum (2,5,1,80)
    m = find_maximum (res)
    print m    
    # dessin d'une courbe
    from pylab import *
    plot ( [ r [1] for r in res] )
    show ()