from scipy.stats import norm
from scipy.stats import zipf
import sys
sys.path.append ("../tableformula")
from tableformula import *
from tableformulagraph import *

def generate_n_obs_zipf (tail_index, n) :
    return list(zipf.rvs(tail_index, size=n))
        
def diff_std_deviation (px, py) :
    s = px*(1-px) + py*(1-py)
    return px, py, s**0.5

def pvalue (diff, std, N) :
    theta = abs(diff)
    bn = (2*N)**0.5 * theta / std
    pvalue = (1 - norm.cdf(bn))*2
    return pvalue
    
def draw_heavy_tail (sample, imagename) :
    table   = TableFormula (["obs"], [ [_] for _ in sample ] )
    avg,std = table.avg_std (lambda v : v["obs"])
    print ("avg,std", avg,std)
    std = 1

    normal  = norm.rvs (size = len(sample))
    normal  = [ x*std  for x in normal ]
    nortbl  = TableFormula (["obs"], [ [_] for _ in normal ] )
    nortbl.addc ("iobs", lambda v : int(v ["obs"] * 10))
    histon  = nortbl.groupby ( lambda v :v["iobs"], 
                            [ lambda v : v["iobs"] ],
                            ["value", "nb"],
                            [ len ] )
    histon.sort (lambda v : v["nb"], reverse = True)
    
    histo   = table.groupby ( lambda v :v["obs"], 
                            [ lambda v : v["obs"] ],
                            ["value", "nb"],
                            [ len ] )
                            
    histo.sort (lambda v : v["nb"], reverse = True)
    histo.add_column_index("index", 1)
    
    vec  = list (histon.select (lambda v : v ["nb"]))
    vec += [0,] * len(histo)
    histo.add_column_vector("nb_normal", vec [:len(histo) ] )
    
    histo.addc ("log(index)", lambda v : math.log(v ["index"]) / math.log(10) )
    histo.addc ("log(nb)", lambda v : math.log(v ["nb"]) / math.log(10) )
    histo.addc ("log(nb_normal)", lambda v : math.log(v ["nb_normal"]) / math.log(10) if v["nb_normal"] > 0 else 0) 
    histo = TableFormulaGraph (histo)
    histo.graph_XY ( [ 
            [ lambda v: v["log(index)"], lambda v: v["log(nb)"], "Zipf"],
            [ lambda v: v["log(index)"], lambda v: v["log(nb_normal)"], "Gauss"],
                        ],
                     outImage = imagename,
                     marker=False, linkPoint=True)    
    
def draw_variancen (sample, imagename) :
    avg = 0.
    std = 0.
    n   = 0.
    w   = 1.
    add = [] 
    for i,x in enumerate(sample) :
        x    = float (x)
        avg += x * w
        std += x*x * w
        n   += w
        val  = (std/n - (avg/n)**2)**0.5
        add.append ( [ i, avg/n, val] )
    
    print add[-1]
    table = TableFormulaGraph ( ["index", "avg(n)", "std(n)"], add)
    table.graph_XY ( [ 
            [ lambda v: v["index"], lambda v: v["avg(n)"], "avg(n)"],
            [ lambda v: v["index"], lambda v: v["std(n)"], "std(n)"],
                        ],
                     outImage = imagename,
                     marker=False, linkPoint=True)    
                     
def hill_estimator (sample) :
    sample = list(sample)
    sample.sort(reverse=True)
    end = len(sample)/10
    end = min(end,100)
    s = 0.
    res = []
    for k in range (0,end) :
        s += math.log(sample[k])
        h = (s - (k+1)*math.log(sample[k+1]))/(k+1)
        h = 1./h
        res.append( [k, h] )
    return res
    
def draw_hill_estimator (sample, imagename) :
    res = hill_estimator(sample)
    table = TableFormulaGraph (["d", "hill"], res )
    table.graph_XY ( [ 
            [ lambda v: v["d"], lambda v: v["hill"], "Hill"],
                        ],
                     outImage = imagename,
                     marker=False, linkPoint=True)    

    
def generate_series ( Ndays, tail_index, N) :
    res = [ ]
    total = [ ]
    for i in range(0,Ndays) :
        sample = generate_n_obs_zipf(tail_index, N)
        total.extend(sample)
        dis = { }
        for t in total : dis[t] = 0
        res.append( len(dis) )
    return res
    
def std (l) :
    m = sum(l)
    v = sum ( [_*_ for _ in l ] )
    m = m*1. / len(l)
    v = v*1. / len(l)
    return (v - m*m)**0.5

if __name__ == "__main__" :
    sys.path.append("../tableformula")
    from tableformula import *
    TableFormula = TableFormulaCore
    
    # mix
    tail_index  = 3
    N           = 100
    Ndays       = 200
    
    values = [ ]
    label  = None 
    for k in range (0,50) :
        print k
        series      = generate_series( Ndays, tail_index, N)
        if label == None :
            label = [ "d%d" % (k+1) for k in range(0,len(series)) ]
        values.append (series)
        
    table = TableFormula (label, values)
    table = table.transpose (labelAsRow = False)
    table.addc ("ave", lambda v : sum( v.values() )*1.0 / len(v) )
    table.addc ("dev", lambda v : std( v.values() ) )
    
    print table

    if False :
        draw_heavy_tail(sample, "distribution_zipf_%d.png" % N)
        draw_variancen(sample, "std deviation after n obs.png")
        draw_hill_estimator(sample, "hill.png")
        
        TableFormulaGraph.ShowLastGraph()
    