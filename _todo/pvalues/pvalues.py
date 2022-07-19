from scipy.stats import norm

def pvalue (p, q, N) :
    theta   = abs(p-q)
    var     = p*(1-p) 
    bn      = (2*N)**0.5 * theta / var**0.5
    ret     = (1 - norm.cdf(bn))*2
    return ret

def pvalue_N (p, q, alpha) :
    theta   = abs(p-q)
    var     = p*(1-p) 
    rev     = abs(norm.ppf (alpha/2))
    N       = 2 * (rev * var**0.5 / theta)** 2
    return int(N+1)

def alphatable (ps, dps, alpha) :
    values = []
    for p in ps :
        row=[]
        for dp in dps :
            q = p+dp
            r = pvalue_N (p,q,alpha) if 1 >= q >= 0 else -1
            row.append (r)
        values.append (row)
    return values
    
def pprint(ps,dps,table, format, fileFormat = "latex") :
    text = []
    if fileFormat == "latex" :
        cc = "r" + ("|r" * len(dps))
        text.append("\\begin{tabular}{" + cc + "}")
        row  = [""] + [ r"\textbf{%1.3f}" % _ for _ in dps ]
        text.append("&".join(row) + r"\\\hline")
        for p,line in zip(ps,table) :
            row  = ["\\textbf{%1.2f}" % p] + \
                   [ format % _ if _ != -1 else ""  for _ in line ]
            text.append("&".join(row) + r"\\\hline")
        text.append("\\end{tabular}")
        return "\n".join(text)
    else :
        # TSV
        row  = [""] + [ r"%1.3f" % _ for _ in dps ]
        text.append("\t".join(row) )
        for p,line in zip(ps,table) :
            row  = [f"{p:1.2f}"] + \
                   [ format % _ if _ != -1 else ""  for _ in line ]
            text.append("\t".join(row) )
        return "\n".join(text)
        
        
if __name__ == "__main__" :
    print ("norm.ppf(0.025)",norm.ppf (0.025)) # -1.9599639845400545
    ps  = [0.001, 0.002] + [ 0.05*i for i in range (1,20) ]
    dps = [ -0.2, -0.1,  -0.02, -0.01, -0.002, -0.001,
             0.2,  0.1,   0.02,  0.01,  0.002,  0.001, ]
    dps.sort()
    t = alphatable (ps, dps, 0.05)
    print (pprint (ps, dps, t, "%d", "latex"))
    print (pprint (ps, dps, t, "%d", "html")) 