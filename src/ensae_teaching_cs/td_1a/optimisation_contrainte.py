# -*- coding: utf-8 -*-
"""
@file
@brief  quelques fonctions sur l'optimisation quadratique avec contraintes
"""

import random


def f_df_H(x=None, z=None):
    """
    Fonction demandée par la fonction
    `solvers.cp <http://cvxopt.org/userguide/solvers.html#problems-with-nonlinear-objectives>`_.

    Elle répond aux trois cas :

    * ``F()`` : la fonction doit retourne le nombre de contraintes
      non linéaires (:math:`f_k`) et un premier point :math:`X_0`,
    * ``F(x)`` : la fonction retourne l'évaluation de :math:`f_0`
      et de son gradient au point ``x``,
    * ``F(x,z)`` : la fonction retourne l'évaluation de :math:`f_0`,
      son gradient et de la dérivée seconde au point ``x``.

    Voir @see fn exercice_particulier1.
    Le problème d'optimisation est le suivant :

    .. math::

        \\left\\{ \\begin{array}{l} \\min_{x,y} \\left\\{ x^2 + y^2 - xy + y \\right\\}
        \\\\ sous \\; contrainte \\; x + 2y = 1 \\end{array}\\right.

    """
    if x is None:
        from cvxopt import matrix
        # cas 1
        x0 = matrix([[random.random(), random.random()]])
        return 0, x0
    else:
        matrix = x.__class__
    f = x[0] ** 2 + x[1] ** 2 - x[0] * x[1] + x[1]
    d = matrix([x[0] * 2 - x[1], x[1] * 2 - x[0] + 1]).T
    h = matrix([[2.0, -1.0], [-1.0, 2.0]])
    if z is None:
        # cas 2
        return f, d
    else:
        # cas 3
        return f, d, h


def Arrow_Hurwicz(F, C, X0, p0, epsilon=0.1, rho=0.1,
                  do_print=True):
    """

    .. _code_Arrow_Hurwicz:

    On implémente l'algorithme de `Arrow-Hurwicz <https://hal.archives-ouvertes.fr/hal-00490826/document>`_
    d'une façon générique. Cela correspond au problème d'optimisation :

    .. math::

        \\left\\{ \\begin{array}{l} \\min_{X} f(X)  \\\\ sous \\; contrainte \\; C(x) = 0 \\end{array}\\right.

    @param      F           fonction qui retourne :math:`f(X)` et :math:`\\nabla f(X)`
    @param      C           fonction qui retourne :math:`C(X)` et :math:`\\nabla C(X)`
    @param      X0          premier :math:`X`
    @param      p0          premier :math:`\\rho`
    @param      epsilon     paramètre multiplicatif devant le gradient
    @param      rho         paramètre multiplicatif durant la mise à jour prenant en compte la contrainte
    @param      do_print    pour écrire des résultats intermédiaire en fonction des itérations
    @return                 un dictionnaire ``{'x': solution, 'iteration': nombre d'itérations }``
    """
    diff = 1
    itern = 0
    while diff > 1e-10:
        f, d = F(X0)
        th, dt = C(X0)
        Xt = [X0[i] - epsilon * (d[i] + dt[i] * p0) for i in range(len(X0))]

        th, dt = C(Xt)
        pt = p0 + rho * th

        itern += 1
        diff = sum([abs(Xt[i] - X0[i]) for i in range(len(X0))])
        X0 = Xt
        p0 = pt
        if do_print and iter % 100 == 0:
            print("i {0} diff {1:0.000}".format(itern, diff),
                  ":", f, X0, p0, th)

    return {'x': X0, 'iteration': itern}


def f_df(X):
    """
    F dans @see fn Arrow_Hurwicz
    """
    x, y = X
    f = x ** 2 + y ** 2 - x * y + y
    d = [x * 2 - y, y * 2 - x + 1]
    return f, d


def contrainte(X):
    """
    C dans @see fn Arrow_Hurwicz
    """
    x, y = X
    f = x + 2 * y - 1
    d = [1, 2]
    return f, d


def exercice_particulier1():
    """
    .. exref::
        :title: solver.cp de cvxopt
        :tag: Computer Science

        On résoud le problème suivant avec `cvxopt <http://cvxopt.org/userguide/index.html>`_ :

        .. math::

            \\left\\{ \\begin{array}{l} \\min_{x,y} \\left \\{ x^2 + y^2 - xy + y \\right \\}
            \\\\ sous \\; contrainte \\; x + 2y = 1 \\end{array}\\right.

        Qui s'implémente à l'aide de la fonction suivante :

        ::

            def f_df_H(x=None,z=None) :
                if x is None :
                    # cas 1
                    x0 = matrix ( [[ random.random(), random.random() ]])
                    return 0,x0
                f = x[0]**2 + x[1]**2 - x[0]*x[1] + x[1]
                d = matrix ( [ x[0]*2 - x[1], x[1]*2 - x[0] + 1 ] ).T
                h = matrix ( [ [ 2.0, -1.0], [-1.0, 2.0] ])
                if z is None:
                    # cas 2
                    return  f, d
                else :
                    # cas 3
                    return f, d, h

            solvers.options['show_progress'] = False
            A = matrix([ [ 1.0, 2.0 ] ]).trans()
            b = matrix ( [[ 1.0] ] )
            sol = solvers.cp ( f_df_H, A = A, b = b)

    """
    from cvxopt import solvers, matrix
    t = solvers.options.get('show_progress', True)
    solvers.options['show_progress'] = False
    A = matrix([[1.0, 2.0]]).trans()
    b = matrix([[1.0]])
    sol = solvers.cp(f_df_H, A=A, b=b)
    solvers.options['show_progress'] = t
    return sol


def exercice_particulier2():
    """
    .. exref::
        :title: algorithme de Arrow-Hurwicz
        :tag: Computer Science

        On résoud le problème suivant avec l'algorithme de
        `Arrow-Hurwicz <https://hal.archives-ouvertes.fr/hal-00490826/document>`_.

        .. math::

            \\left\\{ \\begin{array}{l} \\min_{x,y} \\left \\{ x^2 + y^2 - xy + y \\right \\}  \\\\
            sous \\; contrainte \\; x + 2y = 1 \\end{array}\\right.

        Qui s'implémente à l'aide de la fonction suivante :

        ::

            import random
            from ensae_teaching_cs.td_1a.optimisation_contrainte import Arrow_Hurwicz

            def f_df(X) :
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
            sol = Arrow_Hurwicz(f_df, contrainte, X0, p0, do_print=False)
    """
    X0 = [random.random(), random.random()]
    p0 = random.random()
    sol = Arrow_Hurwicz(f_df, contrainte, X0, p0, do_print=False)
    return sol


if __name__ == "__main__":
    sol1 = exercice_particulier1()
    sol2 = exercice_particulier2()
    print("cvxopt")
    print(sol1)
    print("solution:", sol1['x'].T)
    print("Arrow_Hurwicz")
    print(sol2)
    print("solution:", sol2['x'])
