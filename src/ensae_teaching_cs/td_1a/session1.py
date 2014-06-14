# -*- coding: utf-8 -*-
"""
@file
@brief  quelques fonctions à propos de la première séance

"""

import datetime

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
    
    **L'encodage ``utf-8`` est la norme sur Internet.** C'est pourquoi il est préférable d'utiliser celui-ci pour 
    partager son code via une page Web.
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
    
    @example(TD 1A___calcul de la somme des dix premiers entiers au carré)
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
    
def racine_carree(x):
    """
    retourne la racine carrée d'un nombre
    
    @param  x       nombre
    @return         racine carrée
    """
    return x**0.5
    
def repetition_a_eviter(serie):
    """
    Une répétition à éviter.
    
    @example(Négatifs___Eviter d'effectuer le même appel deux fois)
    
    Dans cette fonction on calcule la variance d'une série d'observations.
    
    @code
    def moyenne(serie):
        return sum(serie) / len(serie)
        
    def variance_a_eviter(serie):
        s = 0
        for obs in serie :
            s += (obs-moyenne(serie))**2
        return s / len(serie)
    @endcode
    
    La fonction ``variance_a_eviter`` appelle la fonction ``moyenne`` à chaque passage
    dans la boucle. Or, rien ne change d'un passage à l'autre. Il vaut mieux stocker
    le résultat dans une variable :
    
    @code
    def moyenne(serie):
        return sum(serie) / len(serie)
        
    def variance(serie):
        s = 0
        moy = moyenne(serie)
        for obs in serie :
            s += (obs-moy)**2
        return s / len(serie)
    @endcode
    
    Le coût de la variance passe alors d'un coût en :math:`O(n^2)` à :math:`O(n)`.
    Ce n'est pas le seul endroit où cette erreur survient. Dans le code suivant,
    on appelle deux fois la fonction ``major`` avec le même argument.
    C'est à éviter.
    
    @code
    meilleur = major(data)[0]  # retourne ("quelque chose", True)
    if major(data)[1]: 
        return {"leaf":guess} 
    @endcode
    
    @endexample
    """
    
    def moyenne(serie):
        return sum(serie) / len(serie)
        
    def variance_a_eviter(serie):
        s = 0
        for obs in serie :
            s += (obs-moyenne(serie))**2
        return s / len(serie)
        
    def variance(serie):
        s = 0
        moy = moyenne(serie)
        for obs in serie :
            s += (obs-moy)**2
        return s / len(serie)
        
    return variance (serie)

def dictionnaire_modifie_dans_la_boucle():
    """
    Dictionnaires, listes modifiés dans la boucle qui les parcourt.
    
    @example(Négatifs___Modifier un dictionnaire en le parcourant)
    
    Il faut éviter de modifier un container lorsqu'on le parcourt. 
    Lorsqu'on supprime un élément d'un dictionnaire, la structure de celui-ci
    s'en trouve modifiée et affecte la boucle qui le parcourt. La boucle parcourt
    toujours l'ancienne structure du dictionnaire, celle qui existait au début
    au début de la boucle.
    
    @code
    d = { k:k for k in range(10) }
    for k,v in d.items():
        if k == 4 : 
            del d[k]    
    @endcode
    
    En Python, cela produit l'erreur qui suit mais d'autres langages ne préviennent 
    pas (C++) et cela aboutit à une erreur qui intervient plus tard dans le code 
    (comme une valeur numérique inattendue).
    
    @code
    Traceback (most recent call last):
      File "session1.py", line 176, in <module>
        l = liste_modifie_dans_la_boucle()
      File "session1.py", line 169, in liste_modifie_dans_la_boucle
        for k,v in d.items():
    RuntimeError: dictionary changed size during iteration
    @endcode
    
    Il faut pour éviter cela stocker les éléments qu'on veut modifier pour les supprimer
    ensuite.
    
    @code
    d = { k:k for k in l }
    rem = [ ]
    for k,v in d.items():
        if k == 4 : 
            rem.append(k)
    for r in rem :
        del d[r]
    @endcode
    
    Même si Python autorise cela pour les listes,
    il est conseillé de s'en abstenir ainsi que pour tout type d'objets qui en contient d'autres.
    C'est une habitude qui vous servira pour la plupart des autres langages.
    
    @endexample
    """
    l = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 ]
    for i in l :
        if i == 2 : 
            l.remove(3)
    
    d = { k:k for k in l }
    rem = [ ]
    for k,v in d.items():
        if k == 4 : 
            rem.append(k)
    for r in rem :
        del d[r]
    
    return l,d
    
def str2date(s, format = "%d/%m/%Y"):
    """
    convertit une chaîne de caractères en datetime
    
    @param      s       chaîne de caractères
    @param      format  format de la conversion
    
    
    @example(Impossible à retenir___conversion d'une chaîne de caractère en date)
    C'est le genre de fonction qu'on n'utilise pas souvent mais qu'on peine à retrouver
    lorsqu'on en a besoin.
    Il faut utiliser la fonction `strftime <https://docs.python.org/3.4/library/datetime.html#strftime-and-strptime-behavior>`_.
    
    @code
    import datetime
    dt = datetime.datetime.strptime ("16/01/2014", "%d/%m/%Y")        
    @endcode
    @endexample
    
    """
    return datetime.datetime.strptime (s, format)    
    
if __name__ == "__main__" :
    l,d = liste_modifie_dans_la_boucle()
    print(l,d)
    r = repetition_a_eviter(l)
    print(r)
    