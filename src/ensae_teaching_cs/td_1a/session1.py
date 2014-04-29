# -*- coding: utf-8 -*-
"""
@file
@brief  quelques fonctions à propos de la première séance

"""

def commentaire_accentues():
    """
    L'aide de cette fonction contient assuréments des accents.
    
    @FAQ(Python n'accepte pas les accents)
    Le langage Python a été conçu en langage anglais. Dès qu'on on ajoute un caractère
    qui ne fait pas partie de l'alphabet anglais (ponctuation comprise), il déclenche une erreur :

    @code
    File "faq_cvxopt.py", line 3
    SyntaxError: Non-UTF-8 code starting with '\xe8' in file faq_cvxopt.py on line 4, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
    @endcode

    Pour la résoudre, il faut dire à l'interpréteur que des caractères non anglais peuvent apparaître 
    et écrire sur la première ligne du programme :

    @code
    # -*- coding: latin-1 -*-
    @endcode

    Ou pour tout caractère y compris chinois :

    @code
    # -*- coding: utf-8 -*-
    @endcode
    
    Si vous utilisez l'éditeur `SciTE <http://www.scintilla.org/SciTE.html>`_ sous Windows,
    après avoir ajouté cette ligne avec l'encoding `utf-8`,
    il est conseillé de fermer le fichier puis de le réouvrir.
    SciTE le traitera différemment.

    @endFAQ
    """
    pass

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
    Ce calcul simple peut s'écrire de diffèrentes manières.
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
    
