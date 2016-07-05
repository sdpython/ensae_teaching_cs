# coding: cp1252
import numpy as Num           # pour les tableaux
import psyco


class optimisation_bfgs (object):
    """optimisation à l'aide de l'algorithme BFGS"""

    def __init__(self, f, derivee, args=None,
                 epsilon=0.1, erreur=1e-5, maxiter=100):
        """initialisation
        @param      f           fonction à minimiser --> f (x, args)
                                        où x est un vecteur (Numeric.array)
        @param      derivee     dérivée de f  --> derivee (x, args)
        @param      args        autres paramètres de la fonction
        @param      epsilon     coefficient devant le gradient
        @param      erreur      on s'arrête lorsque l'erreur ne décroît plus
        @param      maxiter     nombre d'itérations maximum
        """

        self._f = f
        self._derivee = derivee
        self._epsilon = epsilon
        self._erreur = erreur
        self._maxiter = maxiter
        self._args = args

    def erreur(self, x):
        """calcule l'erreur"""
        return self._f(x, *self._args)

    def gradient(self, x):
        """calcule le gradient"""
        return self._derivee(x, *self._args)

    def identite(self, dim):
        """retourne la matrice identité"""
        b = Num.array([[0 for i in xrange(0, dim)] for j in xrange(0, dim)])
        for i in xrange(0, dim):
            b[(i, i)] = 1
        return b

    def optimise(self, xO, classic=False, pr=True):
        """optimisation selon l'algorithme BFGS,
        x0 est le vecteur initiale, retourne la meilleure solution,
        si pr == True, affiche des résultats intermédiaires,
        classic == True, la matrice bt est mise à jour à chaque itération,
        équivaut à une descente de gradient du premier degré"""

        dim = len(self.gradient(xO))
        stop = 1e-12
        err = self.erreur(xO)
        bt = self.identite(dim)
        id = True
        t = 0
        iter = 0
        old = err * (1.0 + self._erreur * 2) * 2
        x = xO
        gt_ = self.gradient(xO)
        xt_ = xO
        nbt = 0

        while   (abs ((old - err) / err) > self._erreur or t == 0) and \
                iter < self._maxiter:

            if pr:
                print "itération ", iter, " (", \
                    t, nbt, ") \t erreur : ", err, " (", old, ")"
            iter = iter + 1
            gt = self.gradient(x)
            ct = Num.dot(bt, gt)

            e = abs(err) * 2 + 1
            eps = self._epsilon * 2
            while e > err and eps > stop:
                eps = eps / 2
                xt = x - ct * eps
                e = self.erreur(xt)

            if eps < 1e-12 and t > 0:
                bt = self.identite(dim)
                if t == 0:
                    nbt += 1
                else:
                    nbt = 0
                t = 0
            else:
                old = err
                x = xt
                err = e
                if not classic:
                    gt = self.gradient(x)
                    dt = gt - gt_
                    gbtg = Num.dot(Num.transpose(gt), Num.dot(bt, gt))
                    gbtd = Num.dot(Num.transpose(gt), Num.dot(bt, dt))
                    if (gbtg <= 0 or gbtd <= 0) and nbt < 2:
                        if t == 0:
                            nbt += 1
                        else:
                            nbt = 0
                        bt = self.identite(dim)
                        t = 0
                    else:
                        t = t + 1
                        st = xt - xt_
                        dtbtdt = Num.dot(Num.transpose(dt), Num.dot(bt, dt))
                        dtst = Num.dot(Num.transpose(dt), st)
                        stdt = Num.dot(Num.transpose(st), dt)
                        stst = Num.outer(st, st)
                        stdtbt = Num.dot(Num.outer(st, dt), bt)
                        btdtst = Num.dot(bt, Num.outer(dt, st))
                        c = 1.0 + dtbtdt / dtst
                        b = stst * (c / stdt)
                        b -= (stdtbt + btdtst) / dtst
                        bt = bt + b

                gt_ = gt
                xt_ = x

        return x

if __name__ == "__main__":
    psyco.full()

    def fonction(x, a, b, c):
        return x[0]**4 + a * x[0]**3 + b * x[1]**2 + c * x[1]

    def derivee(x, a, b, c):
        return Num.array([4 * x[0]**3 + 3 * a * x[0]**2, b * 2 * x[1] + c])

    opt = optimisation_bfgs(fonction, derivee, (1, 0.01, 0.01),
                            maxiter=2000, epsilon=0.2, erreur=1e-10)
    x0 = Num.array([3, 4])
    print "solution initiale : ", x0
    x = opt.optimise(x0, classic=False)
    print "solution finale : ", x
