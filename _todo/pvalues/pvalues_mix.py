from scipy.stats import norm
import random, math

# functions for a bootstrap
# http://statisticalrecipes.blogspot.fr/2012/04/applying-em-algorithm-binomial-mixtures.html

def average_std_deviation (sample) :
    mean = 0.
    var  = 0.
    for x in sample :
        mean += x
        var += x*x
    mean /= len(sample)
    var /= len(sample)
    var -= mean*mean
    return mean,var ** 0.5

def bootsample (sample) :
    n = len(sample)-1
    return [ sample[ random.randint(0,n) ] for _ in sample ]
    
def bootstrap_difference (sampleX, sampleY, draws = 2000, confidence = 0.05) :
    diff = [ ]
    for n in range (0,draws) :
        if n % 1000 == 0 : print (n)
        sx = bootsample(sampleX)
        sy = bootsample(sampleY)
        px = sum(sx) * 1.0/ len(sx)
        py = sum(sy) * 1.0/ len(sy)
        diff.append (px-py) 
    diff.sort()
    n = int(len(diff) * confidence / 2)
    av = sum(diff) / len(diff)
    return av, diff [n], diff [len(diff)-n]

# generation of a sample

def generate_obs (p) :
    x = random.random()
    if x <= p : return 1
    else : return 0

def generate_n_obs (p, n) :
    return [ generate_obs(p) for i in range (0,n) ]
        
# std deviation

def diff_std_deviation (px, py) :
    s = px*(1-px) + py*(1-py)
    return px, py, s**0.5

def pvalue (diff, std, N) :
    theta = abs(diff)
    bn = (2*N)**0.5 * theta / std
    pvalue = (1 - norm.cdf(bn))*2
    return pvalue
    
def omega_i (X, pi, p, q) :
    np = p * pi     if X == 1 else (1-p)*pi
    nq = q * (1-pi) if X == 1 else (1-q)*(1-pi)
    return np / (np + nq)
    
def likelihood (X, pi, p, q) :
    np = p * pi     if X == 1 else (1-p)*pi
    nq = q * (1-pi) if X == 1 else (1-q)*(1-pi)
    return math.log(np) + math.log(nq)
    
def algoEM (sample) :
    p   = random.random()
    q   = random.random()
    pi  = random.random()
    iter   = 0
    while iter < 10 :
        lk = sum ( [ likelihood (x, pi, p, q) for x in sample ] )
        wi  = [ omega_i (x, pi, p, q) for x in sample ]
        sw  = sum(wi)
        pin = sum(wi) / len(wi)
        pn  = sum([ x * w     for x,w in zip (sample,wi) ]) / sw
        qn  = sum([ x * (1-w) for x,w in zip (sample,wi) ]) / (len(wi) - sw)
        
        pi,p,q = pin,pn,qn
        iter += 1
        
    lk = sum ( [ likelihood (x, pi, p, q) for x in sample ] )
    return pi,p,q, lk

if __name__ == "__main__" :
    # mix
    p,q   = 0.20, 0.80
    pi    = 0.7
    N     = 1000
    na    = int(N * pi)
    nb    = N - na

    print ("------- sample")
    sampleX = generate_n_obs(p, na) + generate_n_obs (q, nb)
    random.shuffle(sampleX)
    print ("ave", p * pi + q*(1-pi))
    print ("mea", sum(sampleX)*1./len(sampleX))

    lk = sum ( [ likelihood (x, pi, p, q) for x in sampleX ] )
    print ("min lk", lk, sum (sampleX)*1. / len(sampleX))
    res = []
    for k in range (0, 10) :
        r = algoEM (sampleX)
        res.append ( (r[-1], r) )
    res.sort ()
    for r in res:
        pi,p,q,lk = r[1]
        print ("ave", p * pi + q*(1-pi))
        print r[1]