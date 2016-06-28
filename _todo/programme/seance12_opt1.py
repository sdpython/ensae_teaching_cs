#coding:latin-1
exercices = [ 1,2,3,4,5 ] [-1:]

if 1 in exercices :
    print ("---------------------")
    print ("cvxopt, contrainte d'égalité")
    from cvxopt import solvers, matrix
    import random

    def fonction(x=None,z=None) : 
        if x is None :
            x0 = matrix ( [[ random.random(), random.random() ]])
            return 0,x0
        f = x[0]**2 + x[1]**2 - x[0]*x[1] + x[1]
        d = matrix ( [ x[0]*2 - x[1], x[1]*2 - x[0] + 1 ] ).T
        h = matrix ( [ [ 2.0, -1.0], [-1.0, 2.0] ])
        if z is None: return  f, d
        else : return f, d, h
        
    A = matrix([ [ 1.0, 2.0 ] ]).trans()
    b = matrix ( [[ 1.0] ] )
        
    sol = solvers.cp ( fonction, A = A, b = b)
    print (sol)
    print (sol['x'])

if 2 in exercices :
    print ("---------------------")
    print ("Arrow-Hurwicz, Lagrangien, contrainte d'égalité")
    
    def fonction(X) : 
        x,y = X
        f = x**2 + y**2 - x*y + y
        d = [ x*2 - y, y*2 - x + 1  ] 
        return f, d
        
    def contrainte(X) : 
        x,y = X
        f = x+2*y-1
        d = [ 1,2]
        return f, d
        
    X0  = [ random.random(),random.random() ]
    p0  = random.random()
    epsilon = 0.1
    rho     = 0.1

    diff = 1
    iter = 0
    while diff > 1e-10 :
        f,d   = fonction( X0 )
        th,dt = contrainte( X0 )
        Xt    = [ X0[i] - epsilon*(d[i] + dt[i] * p0) for i in range(len(X0)) ]

        th,dt = contrainte( Xt )
        pt    = p0 + rho * th
        
        iter += 1
        diff = sum ( [ abs(Xt[i] - X0[i]) for i in range(len(X0)) ] )
        X0 = Xt
        p0 = pt
        if iter % 100 == 0 :
            print ("i {0} diff {1}".format(iter,diff),":", f,X0,p0,th)
            
    print (diff,iter,p0,X0)
    
if 3 in exercices :
    print ("---------------------")
    print ("Arrow-Hurwicz avec Lagrangien augmenté, contrainte d'égalité")
    
    def fonction(X,c) : 
        x,y = X
        f = x**2 + y**2 - x*y + y
        d = [ x*2 - y, y*2 - x + 1 ] 
        
        v = x+2*y-1
        v = c/2 * v**2
        
        dv = [ 2*(x+2*y-1), 4*(x+2*y-1) ]
        dv = [ c/2 * dv[0], c/2 * dv[1] ]
        return f + v, d, dv
        
    def contrainte(X) : 
        x,y = X
        f = x+2*y-1
        d = [ 1,2]
        return f, d
        
    X0  = [ random.random(),random.random() ]
    p0  = random.random()
    epsilon = 0.1
    rho     = 0.1
    c       = 1

    diff = 1
    iter = 0
    while diff > 1e-10 :
        f,d,dv = fonction( X0,c )
        th,dt = contrainte( X0 )
        Xt    = [ X0[i] - epsilon*(d[i] + dt[i] * p0 + dv[i]) for i in range(len(X0)) ]

        th,dt = contrainte( Xt )
        pt    = p0 + rho * th
        
        iter += 1
        diff = sum ( [ abs(Xt[i] - X0[i]) for i in range(len(X0)) ] )
        X0 = Xt
        p0 = pt
        if iter % 100 == 0 :
            print ("i {0} diff {1}".format(iter,diff),":", f,X0,p0,th)
            
    print (diff,iter,p0,X0)
    
if 4 in exercices :
    print ("---------------------")
    print ("cvxopt, avec inégalité")
    from cvxopt import solvers, matrix
    import random

    def fonction(x=None,z=None) : 
        if x is None :
            x0 = matrix ( [[ random.random(), random.random() ]])
            return 0,x0
        f = x[0]**2 + x[1]**2 - x[0]*x[1] + x[1]
        d = matrix ( [ x[0]*2 - x[1], x[1]*2 - x[0] + 1 ] ).T
        h = matrix ( [ [ 2.0, -1.0], [-1.0, 2.0] ])
        if z is None: return  f, d
        else : return f, d, h
        
    A = matrix([ [ 1.0, 2.0 ] ]).trans()
    b = matrix ( [[ 1.0] ] )

    G = matrix ( [[0.0, -1.0] ]).trans()
    h = matrix ( [[ -0.3] ] )
        
    sol = solvers.cp ( fonction, A = A, b = b, G=G, h=h)
    print (sol)
    print (sol['x'])    

if 5 in exercices :
    print ("---------------------")
    print ("Arrow-Hurwicz, Lagrangien, contrainte d'inégalité")
    import numpy,random

    X0 = numpy.matrix ( [[ random.random(), random.random() ]]).transpose()
    P0 = numpy.matrix ( [[ random.random(), random.random() ]]).transpose()
        
    A  = numpy.matrix([ [ 1.0, 2.0 ], [ 0.0, -1.0]  ])
    tA = A.transpose()
    b = numpy.matrix ( [[ 1.0], [-0.30] ] )

    epsilon = 0.1
    rho     = 0.1
    c       = 1    

    first = True
    iter  = 0
    while first or abs(J - oldJ) > 1e-8 :
        if first :
            J = X0[0,0]**2 + X0[1,0]**2 - X0[0,0]*X0[1,0] + X0[1,0]
            oldJ = J+1
            first = False
        else :
            oldJ = J
            J = X0[0,0]**2 + X0[1,0]**2 - X0[0,0]*X0[1,0] + X0[1,0]
            
        dj   = numpy.matrix ( [ X0[0,0]*2 - X0[1,0], X0[1,0]*2 - X0[0,0] + 1 ] ).transpose()

        Xt = X0 - ( dj + tA * P0 ) * epsilon
        Pt = P0 + ( A * Xt - b) * rho
        
        if Pt [1,0] < 0 : Pt[1,0] = 0
        
        X0,P0 = Xt,Pt
        iter += 1
        if iter % 100 == 0 :
            print ("iteration",iter, J)
        
    print (iter)
    print (Xt)


    
