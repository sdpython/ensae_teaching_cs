import numpy, matplotlib, random, pylab, math

def matrix_square_root(sigma) :
    eigen, vect = numpy.linalg.eig(sigma)
    dim = len(sigma)
    res = numpy.identity(dim)
    for i in range(0,dim) :
        res[i,i] = eigen[i]**0.5
    return vect * res * vect.transpose()
    
def chi2_level (alpha = 0.95) :
    N = 1000
    x = [ random.gauss(0,1) for _ in range(0,N) ]
    y = [ random.gauss(0,1) for _ in range(0,N) ]
    r = map ( lambda c : (c[0]**2+c[1]**2)**0.5, zip(x,y))
    r = list(r)
    r.sort()
    res = r [ int (alpha * N) ]
    return res
    
def square_figure(mat, a) :    
    x = [ ]
    y = [ ]
    for i in range (0,100) :
        x.append ( a * mat[0][0]**0.5 ) 
        y.append ( (random.random ()-0.5) * a * mat[1][1]**0.5*2 )
        x.append ( -a * mat[0][0]**0.5 ) 
        y.append ( (random.random ()-0.5) * a * mat[1][1]**0.5*2 )

        y.append ( a * mat[1][1]**0.5 ) 
        x.append ( (random.random ()-0.5) * a * mat[0][0]**0.5*2 )
        y.append ( -a * mat[1][1]**0.5 ) 
        x.append ( (random.random ()-0.5) * a * mat[0][0]**0.5*2 )
        
    pylab.plot(x,y, 'ro')
    
    x = [ ]
    y = [ ]
    for i in range (0,100) :
        x.append ( a ) 
        y.append ( (random.random ()-0.5) * a*2 )
        x.append ( -a ) 
        y.append ( (random.random ()-0.5) * a*2  )
        
        y.append ( a ) 
        x.append ( (random.random ()-0.5) * a*2  )
        y.append ( -a ) 
        x.append ( (random.random ()-0.5) * a*2  )
        
    xs,ys = [],[]
    for a,b in zip (x,y) :
        ar = numpy.matrix( [ [a], [b] ] ).transpose()
        we = ar * root
        xs.append ( we [0,0] )
        ys.append ( we [0,1] )
        
    pylab.plot(xs,ys, 'bo')
    pylab.show()

def circle_figure (mat, a) :
    x = [ ]
    y = [ ]
    for i in range (0,200) :
        z = random.random() * math.pi * 2
        i = a * mat[0][0]**0.5 * math.cos(z)
        j = a * mat[0][0]**0.5 * math.sin(z)
        x.append ( i )
        y.append ( j )
    pylab.plot(x,y, 'ro')
    
    x = [ ]
    y = [ ]
    for i in range (0,200) :
        z = random.random() * math.pi * 2
        i = a * math.cos(z)
        j = a * math.sin(z)
        x.append ( i )
        y.append ( j )
        
    xs,ys = [],[]
    for a,b in zip (x,y) :
        ar = numpy.matrix( [ [a], [b] ] ).transpose()
        we = ar * root
        xs.append ( we [0,0] )
        ys.append ( we [0,1] )
        
    pylab.plot(xs,ys, 'bo')
    pylab.show()

if __name__ == "__main__" :
    level = chi2_level ()

    mat   = [ [0.1, 0.05], [0.05, 0.2] ]
    npmat = numpy.matrix(mat)
    root  = matrix_square_root (npmat)

    square_figure (mat, 1.96)
    circle_figure (mat, level)