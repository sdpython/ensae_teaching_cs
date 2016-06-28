# coding: cp1252
import poisson
#import scipy.optimize.lbfgsb as Opt    # optimisation
import bfgs                      # optimisation
import numpy as Num           # pour les tableaux
import psyco

def fonction_bfgs (x, cl, l) :
    """fonction retournant l'opposé de la log-vraisemblance 
    de l'instance cl, fonction à minimiser"""
    cl.set (x)
    f = - cl.log_densite_list (l)
    #print f, "\t", x
    return f
    
def fonction_derivee_bfgs (x, cl, l) :
    """fonction retournant l'opposé de la log-vraisemblance 
    de l'instance cl, fonction à minimiser"""
    cl.set (x)
    f           = cl.gradient_total (l)
    return - Num.array (f)

class poisson_loi_bfgs (poisson.poisson_loi) :
    """loi de distribution de la taille des poissons,
    optimisation à l'aide de l'algorithme BFGS"""
    
    def __init__(self, alpha = 0.5, mm = 1, sm = 1, mf = 1, sf = 1) :
        """initialisation des paramètres de la loi"""
        poisson.poisson_loi.__init__(self, alpha, mm, sm, mf, sf)
        
    def set (self, x) :
        """initialisation avec un tableau"""
        self.alpha    = x [0]
        self.mm       = x [1]
        self.sm       = abs (x [2])
        self.mf       = x [3]
        self.sf       = abs (x [4])
        
    def get (self) :
        """retourne un tableau contenant les paramètres"""
        return Num.array ( (self.alpha, self.mm, self.sm, self.mf, self.sf) ) 
        
    def __str__(self) :
        """affichage"""
        s = "classe poisson_loi BFGS\n"
        s += "alpha = " + str (self.alpha) + "\n"
        s += "moyenne male = " + str (self.mm) + "\n"
        s += "sigma male = " + str (self.sm) + "\n"
        s += "moyenne femelle = " + str (self.mf) + "\n"
        s += "sigma femelle = " + str (self.sf) + "\n"
        return s
        
    def optimisation (self, l, epsilon = 0.001) :
        """recherche du maximum de la fonction f"""
        self.init (l)
        x0     = self.get ()
        print x0
        opt    = bfgs.optimisation_bfgs (fonction_bfgs, \
                                        fonction_derivee_bfgs, \
                                        args = (self, l))
        x = opt.optimise (x0)
        #x      = bfgs.Opt.fmin_l_bfgs_b ( fonction_bfgs, \
        #                             x0, \
        #                             fonction_derivee_bfgs, \
        #                             args = (self, l))
        self.set (x)
        print "optimisation terminée"
        print "valeur maximale : ", self.log_densite_list (l)
        print "message ", d


if __name__ == "__main__" :
    psyco.full ()
    # création d'une instance de la classe        
    cl = poisson.poisson_loi (0.55, 0.40, 0.020, 0.35, 0.015)
    print cl                # affichage
    #cl.trace_densite ()     # courbe densité
    
    l = cl.generate (10000)
    cl2 = poisson_loi_bfgs ()
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
