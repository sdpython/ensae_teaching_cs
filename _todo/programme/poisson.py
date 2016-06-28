# coding: cp1252
import random
import math

class poisson_loi (object) :
    """loi de distribution de la taille des poissons"""
    
    def __init__(self, alpha = 0.5, mm = 1, sm = 1, mf = 1, sf = 1) :
        """initialisation des paramètres de la loi"""
        self.alpha  = alpha 
        self.mm     = mm
        self.sm     = sm
        self.mf     = mf
        self.sf     = sf
        
    def init (self, l) :
        """initialisation de la classe avec une liste de variables"""
        m = 0 
        s = 0
        for x in l :
            m += x 
            s += x*x 
        m /= len (l)
        s /= len (l)
        s -= m*m
        self.alpha  = 0.5
        self.sm     = s / 2
        self.sf     = s / 2
        self.sm     = math.sqrt (self.sm)
        self.sf     = math.sqrt (self.sf)
        self.mm     = m + self.sm * 2
        self.mf     = m - self.sf * 2
        
    def __str__(self) :
        """affichage"""
        s = "classe poisson_loi\n"
        s += "alpha = " + str (self.alpha) + "\n"
        s += "moyenne male = " + str (self.mm) + "\n"
        s += "sigma male = " + str (self.sm) + "\n"
        s += "moyenne femelle = " + str (self.mf) + "\n"
        s += "sigma femelle = " + str (self.sf) + "\n"
        return s
        
    def simulation (self) :
        """simule une taille de poisson"""
        u = random.uniform (0,1)
        v = random.gauss (0,1)
        if u <= self.alpha :
            return v * self.sm + self.mm
        else :
            return v * self.sf + self.mf
            
    def generate (self,N) :
        """simule N tailles de poisson"""
        return [ self.simulation () for i in xrange (0,N) ]
        
    def trace_densite (self, autre = None) :
        """trace la courbe de la densité, 
        si autre != None, en trace une autre"""
        xa = min (self.mm, self.mf) - 3.0 * max (self.sm, self.sf)
        xb = max (self.mm, self.mf) + 3.0 * max (self.sm, self.sf)
        n  = 100
        x  = [ xa + (xb - xa) * i / n for i in xrange (0,n+1) ]
        y  = [ self.densite (xa + (xb - xa) * i / n) for i in xrange (0,n+1) ]
        import pylab as pl
        pl.plot ( x, y, "b" )
        if autre != None :
            xa = min (autre.mm, autre.mf) - 3.0 * max (autre.sm, autre.sf)
            xb = max (autre.mm, autre.mf) + 3.0 * max (autre.sm, autre.sf)
            n  = 100
            x  = [ xa + (xb - xa) * i / n for i in xrange (0,n+1) ]
            y  = [ autre.densite (xa + (xb - xa) * i / n) for i in xrange (0,n+1) ]
            pl.plot (x, y, "r")
            
        pl.title ("Distribution des tailles de poisson")
        pl.xlabel ("x")
        pl.ylabel ("y")
        
        pl.show()
        
    def densite (self, x) :
        """calcule de la densité au point x"""
        dpi = 1.0 / math.sqrt (math.pi * 2)
        xm = (x - self.mm) ** 2 / (2 * self.sm * self.sm)
        xm = math.exp (- xm)
        xf = (x - self.mf) ** 2 / (2 * self.sf * self.sf)
        xf = math.exp (- xf)
        return self.alpha * xm / self.sm + (1.0 - self.alpha) * xf / self.sf
        
    def log_densite (self, x) :
        """calcule de la log-densité au point x"""
        try :
            return math.log (self.densite (x))
        except :
            print "---------- erreur -------------------------------------------"
            print x
            return 0
        
    def log_densite_list (self, l) :
        """calcule la somme des log-densités au point x de l"""
        s = 0 
        for x in l :
            s += self.log_densite (x)
        s /= len (l)
        return s
        
    def gradient (self, x) :
        """calcul le gradient au point x, retourne un t-uple"""
        unpim   = 1.0 / (math.sqrt (2 * math.pi) * self.sm)
        unpif   = 1.0 / (math.sqrt (2 * math.pi) * self.sf)
        expm    = math.exp ( - ( x - self.mm)**2 / (2 * (self.sm**2)))
        expf    = math.exp ( - ( x - self.mf)**2 / (2 * (self.sf**2)))
        grada   = unpim * expm - unpif * expf
        gradmm  = (x - self.mm) / (self.sm** 2) * self.alpha * unpim * expm
        gradmf  = (x - self.mf) / (self.sf** 2) * (1.0 - self.alpha) * unpif * expf
        gradsm  = self.alpha * unpim * (x - self.mm) ** 2 / (self.sm ** 3) - \
                    self.alpha * unpim / self.sm
        gradsm *= expm
        gradsf  = (1.0 - self.alpha) * unpif * (x - self.mf) ** 2 / (self.sf ** 3) - \
                    self.alpha * unpif / self.sf
        gradsf *= expf
        f       = self.densite (x)
        return (grada / f, gradmm / f, gradsm / f, gradmf / f, gradsf / f)
        
    def gradient_total (self, l) :
        """calcul la somme des gradients pour tous les x de l"""
        g = [ 0.0 for i in range (0,5) ]
        for x in l :
            (a,b,c,d,e) = self.gradient (x)
            g [0] += a
            g [1] += b
            g [2] += c
            g [3] += d
            g [4] += e
        for i in range (0,len (g)) :
            g [i] /= len (l)
        return ( g [0], g [1], g [2], g [3], g [4] ) 
        
    def optimisation (self, l, epsilon = 0.001, erreur = 1e-5) :
        """recherche du maximum de la fonction f"""
        self.init (l)
        de   = self.log_densite_list (l)
        print "première densité : ", de
        dold = de / 2
        nb   = 0
        while abs (dold - de) / de > erreur :
            (a,b,c,d,e) = self.gradient_total (l)
            self.alpha      += epsilon * a
            self.mm         += epsilon * b
            self.sm         += epsilon * c
            self.mf         += epsilon * d
            self.sf         += epsilon * e
            dold = de
            de   = self.log_densite_list (l)
            nb  += 1
            print "itération ", nb, " densité ", de, " (", dold, ")  ", \
                    abs (dold - de) / de, " epsilon = ", epsilon
        

if __name__ == "__main__" :
    # création d'une instance de la classe        
    cl = poisson_loi (0.55, 0.40, 0.020, 0.35, 0.015)
    print cl                # affichage
    #cl.trace_densite ()     # courbe densité
    
    l = cl.generate (10000)
    cl2 = poisson_loi ()
    print "-----------------------------------------------------------"
    print "log densité maximale ", cl.log_densite_list (l)
    (a,b,c,d,e) = cl.gradient_total (l)
    print "gradient idéal ", (a,b,c,d,e)
    print "-----------------------------------------------------------"
    
    (a,b,c,d,e) = cl2.gradient_total (l)
    print "gradient avant", (a,b,c,d,e)
    cl2.optimisation (l)
    (a,b,c,d,e) = cl2.gradient_total (l)
    print "gradient après ", (a,b,c,d,e)
    print "-----------------------------------------------------------"
    print cl2
    cl2.trace_densite (cl)
    print "log vraisemblance  : ", cl2.log_densite_list (l)
    
    
