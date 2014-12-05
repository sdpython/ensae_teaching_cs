
.. _l-graphes:


Graphes
=======

Les `graphes <http://fr.wikipedia.org/wiki/Th%C3%A9orie_des_graphes>`_ représente
une partie importante de l'informatique. C'est souvent très visuel et 
assez intuitif à petite échelle.

.. image:: http://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Breadth-first-tree.png/220px-Breadth-first-tree.png


Termes
++++++

* **noeud** (ou vertex en anglais) : élément du graphe
* **arc** (ou edge en anglais) : lien reliant deux n\oe uds
* **graphe orienté** : les arcs sont orientés, aller du noeud _i_ à _j_ ou de _j_ à _i_ n'a pas le même sens

Représentation
++++++++++++++

On parle de `matrice d'adjacence <http://fr.wikipedia.org/wiki/Matrice_d'adjacence>`_.
La matrice :math:`A=(a_{ij})` définit les arcs entre les noeuds.
:math:`a_{ij}` définit le poids de l'arc. Si ce coefficient est nul, il n'y a pas d'arc.

Un graphe orienté signifie que la matrice d'adjacence n'est pas symétrique.

On représente la matrice d'adjacence souvent sous forme de dictionnaire car
cette matrice est souvent creuse : beaucoup de coefficients sont nuls car le nombre d'arcs
comparé au nombre total d'arcs (:math:`n^2` pour un graphe de :math:`n` noeuds) 
est très petit. 
