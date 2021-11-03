#coding:latin-1
import random, math

# question 1
def calcul_suite_a (n, e, a,b,c) :
    p = {}
    p [0,0]  = 1
    for u in range (1,n+1) :
        for k in range (e,u+2) :
            if   k == e   : p [u,k] = a * p.get ( (u-1,k+1), 0 )
            elif k == e+1 : p [u,k] = a * p.get ( (u-1,k+1), 0 ) + \
                                      b * p.get ( (u-1,k  ), 0 )
            elif k >  e+1 : p [u,k] = a * p.get ( (u-1,k+1), 0 ) + \
                                      b * p.get ( (u-1,k  ), 0 ) + \
                                      c * p.get ( (u-1,k-1), 0 )
    return p
    
def affiche_proba (ps, e) :
    n     = max ( [ k[1] for k,z in ps.iteritems () ] )
    moy = 0.0
    logru = []
    logu  = []
    for u in range (1, n+1) :
        p = ps.get((u,e),0)*1.0 
        moy += p * u
        mes = "u % 3d P(U=u) %1.6g r_u %1.6g" % (u, p, moy)
        if u < 3 or u %50 == 0 : print mes
        logru.append(math.log(moy))
        logu.append(math.log(u))
        
    import pylab
    pylab.plot ( logu, logru, "o")
    pylab.show()
    
a,c = 1.0/3, 1.0/3
b = 1-a-c
e = -1

su = calcul_suite_a(600,e,a,b,c)
affiche_proba(su, e)