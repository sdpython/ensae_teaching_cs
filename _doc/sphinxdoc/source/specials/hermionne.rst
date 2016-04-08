



.. _l-hermionne:


L'énigme d'Hermionne, Harry Potter tome 1
=========================================

Lors du premier tome de `Harry Potter <https://fr.wikipedia.org/wiki/Harry_Potter>`_
les trois héros doivent résoudre une énigme 
- qui ne nécessite aucune magie - 
afin d'accéder à la salle où est cachée la pierre philosophale. 
Ce problème, dont l'auteur serait le professeur 
`Rogue <https://fr.wikipedia.org/wiki/Severus_Rogue>`_
(Professor `Snape <https://en.wikipedia.org/wiki/Severus_Snape>`_ pour les anglophones), 
consiste à trouver deux potions parmi les sept qui se trouvent devant 
eux : celles permettent d'avancer et de reculer. 
Ils sont aidés de quelques indices :


#. Il y a trois fioles de poison, deux fioles de vin d'ortie, 
   une fiole permettant d'avancer et une fiole permettant de reculer.
#. Immédiatement à gauche de chacune des deux fioles de vin se trouve 
   une fiole de poison.
#. Les fioles 1 et 7 ont des contenus différents~; 
   ni l'une ni l'autre n'est la fiole qui permet d'avancer.
#. Ni la fiole la plus grande (fiole 6) ni la plus petite (fiole 3) 
   ne contient du poison.
#. Les contenus des fioles 2 et 6 sont identiques.


Les deux solutions proposées sont équivalentes, elles consistent à parcourir toutes les
solutions et à accepter la première qui valide toutes les règles.
L'ensemble des possibilités n'est pas très élevé et l'algorithme le plus simple suffit.
La première fonction
:func:`solution <ensae_teaching_cs.special.hermionne.solution>`
n'utilise que des fonctions pour trouver la solution,
la seconde implémente le même algorithme avec des classes :
:func:`solution <ensae_teaching_cs.special.hermionne_classes.solution>`.
Et la solution est :

.. runpython::
    :showcode:

    from ensae_teaching_cs.special.hermionne_classes import solution
    print(solution())
    

Le parcours des solutions de la fonction :func:`solution <ensae_teaching_cs.special.hermionne.solution>`
fait intervenir deux boucles qui implémentent un compteur. Chacune des 7 cases
peut contenir 4 potions différenes (poison, vin, avancer, reculer) codé 0, 1, 2, 3. 
Il y a :math:`4^7` solutions. Pourquoi ne pas les parcourir de 1 à :math:`4^7` ? 
La *n* ième solution correspond à :

* case 1 : :math:`n \mod 4`
* case 2 : partie entière de :math:`(n \mod 16) / 4`
* case 3 : partie entière de :math:`(n \mod 64) / 16`
* case *i* : partie entière de :math:`(n \mod 4^i) / 4^{i-1}`

Cela donne :

::

    for i in range(4**7):
        l = [(i % (4**k)) // (4**(k-1)) for k in range(1,8)]

Soit :

.. runpython::

    for i in range(7):
        l = [(i % (4**k)) // (4**(k-1)) for k in range(1,8)]
        print(l)

Cela revient à écrire un nombre entier en base 4. Comme 4 est une puissance
de deux, on peut utiliser des opérateurs binaires ``>>`` qui déplacent les bits
d'un nombre vers la droite (division par deux à chaque décalage et ``&``
qui est l'opérateur ``ET``.

::

    for i in range(4**7):
        l = [(i >> (2*k) & 4 for k in range(0,7)]
        
Pour chaque des solutions, utilise une fonction qui vérifie les cinq règles du programme :

::

    from collections import Counter
    def solution_correcte(case):
        if case[1] != case[5]: return False
        if case[5] == 0: return False
        if case[2] == 0: return False
        if case[0] == case[6] : return False
        if case[0] == 2: return False
        if case[6] == 2: return False
        c = Counter(case)
        if c[0] != 3: return False
        if c[1] != 2: return False
        if c[2] != 1: return False
        if c[3] != 1: return False
        for k in range(1, 7):
            if case[k] == 1 and case[k-1] != 0:
                return False
        return True
        
La boucle qui parcourt les solutions est modifiée ::

    solutions = []
    for i in range(4**7):
        l = [(i >> (2*k)  & 4 for k in range(0,7)]
        if solution_correcte(l):
            solutions.append(l)
    print(solutions)
    
Le programme perd beaucoup de temps à parcourir toutes les solutions.
Une idée simple pour aller plus vite est de réduire l'ensemble des solutions à 
parcourir en s'appuyant sur une règle. Par exemple celle qui affirme 
que les potions cases 2 et 6 sont identiques. ::


    solutions = []
    for i in range(4**6):
        l = [(i % (4**k)) // (4**(k-1)) for k in range(1,7)]
        l.insert(5, l[1])
        if solution_correcte(l):
            solutions.append(l)
    print(solutions)
    
On parcourt 4 fois moins de solutions.
