# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `CVXOPT <http://cvxopt.org/>`_.

"""

def entier_grande_taille():
    """
    @FAQ(Quel est l'entier le plus grand ?)
    La version 3 du langage Python a supprimé la constante ``sys.maxint``
    qui définissait l'entier le plus grand (voir 
    `What’s New In Python 3.0 <https://docs.python.org/3.1/whatsnew/3.0.html#integers>`_).
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
    """
    pass

