import random, math

def densite_gauss (mu, sigma, x) :
    e = -(x - mu)**2 / (sigma**2 * 2)
    d = 1. / ((2*math.pi)**0.5 * sigma)
    return d * math.exp (e)
    
def simulation_vector (N, mu, sigma) :
    return [ random.gauss(mu,sigma) for n in range(N) ]
    
def ratio (vector, x, fdensite) :
    under = 0
    above = 0
    fx    = fdensite(x)
    for u in vector :
        f = fdensite (u)
        if f >= fx : above += 1
        else : under += 1
    return float(above) / float (above + under)
        
if __name__ == "__main__" :
    x     = 1.96
    N     = 10000
    mu    = 0
    sigma = 1
    
    v = simulation_vector (N, mu, sigma)
    g = ratio (v, x, lambda y : densite_gauss (mu, sigma, y) )
    print (g)