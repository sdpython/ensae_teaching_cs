



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
#. Immédiatement à gauche de chacune des deux fioles de vin se trouve une fiole de poison.
#. Les fioles 1 et 7 ont des contenus différents~; ni l'une ni l'autre n'est la fiole 
   qui permet d'avancer.
#. Ni la fiole la plus grande (fiole 6) ni la plus petite (fiole 3) ne contient du poison.
#. Les contenus des fioles 2 et 6 sont identiques.


Les deux solutions proposées sont équivalentes, elles consistent à parcourir toutes les
solutions et à accepter la première qui valide toutes les règles.
L'ensemble des possibilités n'est pas très élevé et l'algorithme le plus simple suffit.
La première fonction
:func:`solution <ensae_teaching_cs.special.hermionne.solution>`
n'utilise que des fonctions pour trouver la solution,
la seconde implémente le même algorithme avec des classes :
:func:`solution <ensae_teaching_cs.special.hermionne.solution_classe>`.
Et la solution est :

.. runpython::
    :showcode:

    from ensae_teaching_cs.special.hermionne_classes import solution
    print(solution())
