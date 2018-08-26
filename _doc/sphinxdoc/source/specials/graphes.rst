
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
* **graphe orienté** : les arcs sont orientés, aller du noeud :math:`i`
  à :math:`j` ou de :math:`j` à :math:`i` n'a pas le même sens

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

Cyclique, acyclique
+++++++++++++++++++

C'est une distinction importante. Un graphe cyclique implique
qu'on puisse partir d'un noeud et y revenir. Dans un graphe acyclique,
tout chemin a un début et une fin. Le graphe suivant est tiré de
wikipédia et il ne comporte pas de cycle. Un graphique ayclique est
nécessairement orienté.
Le plus long chemin n'a pas de sens dans un graphe cyclique.

.. image:: acy.png
    :width: 500

Trois problèmes classiques de graphes
+++++++++++++++++++++++++++++++++++++

Ils concernent les graphiques cycliques et acycliques.

* Recherche des `composantes connexes <https://en.wikipedia.org/wiki/Connected_component_(graph_theory)>`_.
  Un graphe a deux composantes connexes s'il n'est pas possible de relier pas un chemin
  deux points quelconques du graphes.
* `Plus court chemin dans un graphe <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_plus_court_chemin>`_,
  c'est problème qu'on retrouve très souvent même parfois où on ne l'attend pas.
  L'`algorithme de Viterbi <https://fr.wikipedia.org/wiki/Algorithme_de_Viterbi>`_
  équivaut à la recherche du plus court chemin dans un graphe où les arcs sont des
  logarithmes de probabilités.
* Le `voyageur de commerce <https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce>`_
  pour lequel il faut trouver le plus court chemin passant par tous les noeuds d'un graphe.

Ces trois problèmes concernent les graphes orientés et non orientés,
acyclique ou non (excepté pour le dernier).
Pour les graphes orientés et acyclique,
on en revient le plus souvent à les parcourir.

Parcours de graphes
+++++++++++++++++++

* `Algorithme de parcours en largeur <https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur>`_ :
  on parcourt d'abord les fils d'un noeud, puis les fils des fils...
* `Algorithme de parcours en profondeur <https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur>`_ :
  on parcourt le premier fils, puis son premier et ainsi de suite jusqu'à tomber sur un
  noeud sans fils.

Ces deux algorithmes peuvent être utilisé pour colorier un graphe.
Un graphe symbolise un ensemble de relations entre des objets ou des personnes
comme dans la plupart des séries policières qui vous rappellent l'intrigue
en l'écrivant sur un tableau transparent.
