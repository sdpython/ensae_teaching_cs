# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.

"""

import os

def entier_grande_taille():
    """
    
    @FAQ(Quel est l'entier le plus grand ?)
    La version 3 du langage Python a supprimé la constante ``sys.maxint``
    qui définissait l'entier le plus grand (voir 
    `What's New In Python 3.0 <https://docs.python.org/3.1/whatsnew/3.0.html#integers>`_).
    De ce fait la fonction `getrandbit <https://docs.python.org/3.4/library/random.html#random.getrandbits>`_
    retourne un entier aussi grand que l'on veut.
    
    @code
    import random,sys
    x = random.getrandbits(2048)
    print(type(x),x)    
    @endcode
    
    Qui affiche ::
    
        <class 'int'> 28821592245571075131654830983838148370214474845580101472119213042190172126736565496812698627920295650674001797895985629679099064974713574340970814696233578272198061719231359573083186306654342306192322853809386167953610349383945699523678043826057910352338185386934425139215277777285416123100069406811011284910239819101658048202284988811705076819806294753255877254609472467038968542731954915621043682174519015068283521575989003211477579416601653132293861235314484703125172048342096920580957771246615770710590596119341983358658507235612104581804871612316272382587635599344895821316316356994838247665194550292758379858074
            
    Les calculs en nombre réels se font toujours avec huit octets de précision. 
    Au delà, il faut utiliser la librairie `gmpy2 <http://gmpy2.readthedocs.org/en/latest/>`_.
    Il est également recommandé d'utiliser cette librairie pour les grands nombres entiers
    (entre 20 et 40 chiffres). La librairie est plus rapide que l'implémentation
    du langage Python (voir `Overview of gmpy2 <https://gmpy2.readthedocs.org/en/latest/overview.html>`_).
    
    @endFAQ
    
    @FAQ(Tabulations ou espace ?)
    Il est préférable de ne pas utiliser les tabulations et de les remplacer par des espaces.
    Lorsqu'on passe d'un Editeur à un autre, les espaces ne bougent pas. Les tabulations sont plus ou moins grandes visuellement.
    L'essentiel est de ne pas mélanger.
    Dans `SciTE <http://www.scintilla.org/SciTE.html>`_, il faut aller dans le menu Options / Change Indentation Settings...
    Tous les éditeurs ont une option similaire.
    @endFAQ
    """
    pass


def difference_div():
    """
    @FAQ(Quelle est la différence entre / et // - division ?)
    Le résultat de la division avec l'opérateur ``/`` est toujours réel : 
    la division de deux entiers ``1/2`` donne ``0.5``.
    Le résultat de la division avec l'opérateur ``//`` est toujours entier.
    Il correspond au quotient de la division.
    
    @code
    div1 = 1/2
    div2 = 4/2
    div3 = 1//2
    div4 = 1.0//2.0
    print(div1,div2,div3,div4) # affiche (0.5, 2.0, 0, 0)
    @endcode
    
    Le reste d'une division entière est obtenue avec l'opérateur ``%``.
    
    @code
    print ( 5 % 2 )  # affiche 1
    @endcode
    
    C'est uniquement vrai pour les version Python 3.x. 
    Pour les versions 2.x, les opérateurs ``/`` et ``//`` avaient des comportements différents
    (voir `What’s New In Python 3.0 <https://docs.python.org/3/whatsnew/3.0.html#integers>`_).
    @endFAQ
    """
    div1 = 1/2
    div2 = 4/2
    div3 = 1//2
    div4 = 1.0//2.0
    return div1,div2,div3,div3
    
def python_path():
    """
    @FAQ(Comment éviter sys.path.append... quand on développe un module ?)
    Lorsqu'on développe un module, 
    on ne veut pas l'installer. On ne veut pas qu'il soit présent dans le répertoire ``site-packages`` de la distribution
    de Python car cela introduit deux versions : celle qu'on développe et celle qu'on a installer.
    Avant, je faisais cela pour créer un petit programme utilisant mon propre module
    (et on en trouve quelque trace dans mon code) :
    
    @code
    import sys
    sys.path.append("c:/moncode/monmodule/src")
    import monmodule
    @endcode
    
    Quand je récupère un programme utilisant ce module, il me faudrait ajouter 
    ces petites lignes à chaque fois et c'est barbant.
    Pour éviter cela, il est possible de dire à l'interpréteur Python d'aller chercher
    ailleurs pour trouver des modules en ajoutant le chemin à la 
    `variable d'environnement <http://fr.wikipedia.org/wiki/Variable_d'environnement>`_
    `PYTHON_PATH <https://docs.python.org/3.4/using/cmdline.html#envvar-PYTHONPATH>`. 
    Sous Windows :
    
    @code
    set PYTHON_PATH=%PYTHON_PATH%;c:\\moncode\\monmodule\\src
    @endcode
    
    @endFAQ
    """
    return os.environ.get("PYTHON_PATH","")
    
def test_unitaire():
    """
    @FAQ(Qu'est-ce qu'un test unitaire ?)
    
    Un `test unitaire <http://fr.wikipedia.org/wiki/Test_unitaire>`_ 
    une procédure permettant de vérifier le bon fonctionnement d'une partie précise.
    Concrètement, cela consiste à écrire une fonction qui exécute la partie de code
    à vérifier. Cette fonction retourne ``True`` si le test est valide, c'est-à-dire 
    que la partie de code s'est comportée comme prévue : elle a retourné le résultat attendu.
    Elle déclenche une exception si elle le code à vérifier ne se comporte pas comme prévu.
    
    Par example, si on voulait écrire un test unitaire pour la fonction 
    `pow <https://docs.python.org/3.4/library/functions.html#pow>`_, on pourrait
    écrire ::
    
        def test_pow():
            assert pow(2,1) == 2   # on vérifie que 2^1 == 0
            assert pow(2,0) == 1
            assert pow(2,-1) == 0.5
            assert pow(2,-1) == 0.5
            assert pow(0,0) == 1     # convention, on s'assure qu'elle ne change pas
            assert isinstance(pow(-2,3.4), complex)
            return True
            
    
    **A quoi ça sert ?**
    
    On écrit la fonction ``x_exp`` (:math:`=y x^{-n}`) comme suit ::
    
        def x_exp(x,y,n):
            return y / pow(x,n)
            
    La fonction retourne 0 si :math:`x=y=n=0`.
    Admettons maintenant qu'un dévelopeur veuille changer la convention :math:`0^0=1` en :math:`0^0=0`.
    La fonction précédente produira une erreur à cause d'une division ``0/0``.
    Un test unitaire détectera au plus tôt cette erreur.
    
    Les tests unitaires garantissent la qualité d'un logiciel qui est considéré comme bonne
    si 80% du code est couvert par un test unitaire. Lorsque plusieurs personnes
    travaillent sur un même programme, un dévelopeur utilisera une fonction faite par un
    autre. Il s'attend donc à ce que la fonction produise les mêmes résultats
    avec les mêmes entrées
    **même si on la modifie ultérieurement**.
    Les tests unitaires servent à s'assurer qu'il n'y a pas d'erreur
    introduite au sein des résultats intermédiaire d'une chaîne de traitement, auquel
    cas, c'est une cascade d'erreur qui est susceptible de se produite. La source
    d'une erreur est plus facile à trouver lorsque les tests unitaires sont nombreux.
            
    @endFAQ
    """
    assert pow(2,1) == 2   # on vérifie que 2^1 == 0
    assert pow(2,0) == 1
    assert pow(2,-1) == 0.5
    assert pow(2,-1) == 0.5
    assert pow(0,0) == 1    
    assert isinstance(pow(-2,3.4), complex)
    return True
    
if __name__ == "__main__" :
    #print(difference_div())
    test_unitaire()
