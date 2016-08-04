# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `CVXOPT <http://cvxopt.org/>`_.

"""


def optimisation():
    """
    Quelques erreurs lorsqu'on cherche à optimiser avec `CVXOPT <http://cvxopt.org/>`_.

    .. faqref::
        :tag: cvxopt
        :title: TypeError: 'q' must be a 'd' matrix with one column
        
        Cette erreur survient même lorsque la dimension de la matrice ``q`` en question
        est la dimension attendue. Dans le cas présent, elle est définie comme suit :

        :: 
        
            q=matrix([[0,0,0]])

        Mais la fonction `coneqp <http://abel.ee.ucla.edu/cvxopt/userguide/coneprog.html?highlight=coneqp#cvxopt.solvers.coneqp>`_
        retourne l'erreur :

        :: 
        
            Traceback (most recent call last):
              File "toutbiss.py", line 236, in <module>
                liste_composition,liquide = actualisation(liste_df,index,liquide,liste_composition,nb_jours_rendement,nb_jours_volatilite,volatilite_max)
              File "toutbiss.py", line 136, in actualisation
                objectif_repartition=volatilite_quadra2(liste_df,index,nb_jours_rendement,nb_jours_volatilite,volatilite_max)
              File "toutbiss.py", line 121, in volatilite_quadra2
                sol=solvers.coneqp(P=P,q=q,G=G,h=h,b=b,A=A)
              File "C:\\Python35_x64\\lib\\site-packages\\cvxopt\\coneprog.py", line 1852, in coneqp
                raise TypeError("'q' must be a 'd' matrix with one column")
            TypeError: 'q' must be a 'd' matrix with one column

        C'est dû au fait que le module fait la différence entre les entiers et les réels.
        Il suffit juste d'écrire :

        ::
        
            q=matrix([[0.0,0.0,0.0]])

        Bien sûr, si l'erreur est vraiment un problème de dimension, cette correction
        n'aidera pas.

    .. faqref::
        :tag: cvxopt
        :title: ValueError: Rank[|A|] < p or Rank[|[P; A; G]|] < n)

        La fonction `coneqp <http://abel.ee.ucla.edu/cvxopt/userguide/coneprog.html?highlight=coneqp#cvxopt.solvers.coneqp>`_
        déclenche parfois cette erreur :

        ::
        
            Traceback (most recent call last):
              File "C:\\Python35_x64\\lib\\site-packages\\cvxopt\\coneprog.py", line 2271, in coneqp
                try: f3 = kktsolver(W)
              File "C:\\Python35_x64\\lib\\site-packages\\cvxopt\\coneprog.py", line 1996, in kktsolver
                return factor(W, P)
              File "C:\\Python35_x64\\lib\\site-packages\\cvxopt\\misc.py", line 1457, in factor
                lapack.potrf(F['S'])
            ArithmeticError: 3

            During handling of the above exception, another exception occurred:

            Traceback (most recent call last):
              File "toutbiss.py", line 237, in <module>
                liste_composition,liquide = actualisation(liste_df,index,liquide,liste_composition,nb_jours_rendement,nb_jours_volatilite,volatilite_max)
              File "toutbiss.py", line 137, in actualisation
                objectif_repartition=volatilite_quadra2(liste_df,index,nb_jours_rendement,nb_jours_volatilite,volatilite_max)
              File "toutbiss.py", line 122, in volatilite_quadra2
                sol=solvers.coneqp(P=P,q=q,G=G,h=h,b=b,A=A)
              File "C:\\Python35_x64\\lib\\site-packages\\cvxopt\\coneprog.py", line 2274, in coneqp
                raise ValueError("Rank(A) < p or Rank([P; A; G]) < n")
            ValueError: Rank(A) < p or Rank([P; A; G]) < n

        Le message est explicite mais si aucune de ces conditions n'est vérifiée, cela peut
        vouloir dire qu'une autre hypothèse du problème à résoudre n'est pas vérifiée :

        - la symétrie d'une matrice
        - le fait qu'une matrice doit être `définie semi-positive <http://fr.wikipedia.org/wiki/Matrice_d%C3%A9finie_positive>`_
    """
    pass
