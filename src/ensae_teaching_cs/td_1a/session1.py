# -*- coding: utf8 -*-
"""
@file
@brief  quelques fonctions à propos de la première séance
"""

def dix_entiers_carre():
    """
    fait la somme des dix premiers entiers au carré
    
    :returns: nombre réel
    
    @FAQ(Quelle est la différence entre return et print ?)
    La fonction ``print`` sert à afficher un résultat sur la sortie standard.
    Elle peut être utilisée à tout moment
    mais elle n'a pas d'impact sur le déroulement programme. Le mot-clé ``return``
    n'est utilisé que dans une fonction. Lorsque le programme rencontre
    une instruction commençant par ``return``, il quitte la fonction
    et transmet le résultat à l'instruction qui a appelé la fonction.
    @endFAQ
    
    @example(calcul de la somme des dix premiers entiers au carré)
    Ce calcul simple peut s'écrire de différentes manières.
    @code
    s = 0
    for i in range(1,11):
        s += i**2
    @endcode
    D'une façon abrégée :
    @code
    s = sum ( [ i**2 for i in range(1,11) ] )
    @endcode
    @endexample
    """
    s = 0
    for i in range(1,11):
        s += i**2
    return s