

.. index:: culture algorithmique, algorithme, culture

.. _l-algoculture:


Survol algorithmique
====================

Il est facile de caler un modèle statistiques lorsque les données sont propres 
et de taille raisonnable. Ce n'est quasiment jamais le cas.
On a besoin de nettoyer ou de transformer les données. On a besoin
de réduire le temps de calcul d'un algorithme car il est inexploitable en l'état.
Pour ces deux raisons, il est utile de connaître quelques algorithmes
afin d'avoir d'avoir des idées. On a besoin d'avoir un moyen rapide, visuelle
et efficace de comparer deux résultats.

Ordres de grandeur
++++++++++++++++++

Qu'est-il raisonnable de faire à supposer qu'on ne dispose que d'une seule machine ?
La mémoire n'est plus un problème. Le temps de calcul l'est toujours.

* :math:`n \leqslant 10` : coût :math:`\leqslant O(2^n)`
* :math:`n \leqslant 15` : coût :math:`\leqslant O(n!)`
* :math:`n \leqslant 10^2` : coût :math:`\leqslant O(n^3)`
* :math:`n \leqslant 10^3` : coût :math:`\leqslant O(n^2)`
* :math:`n \leqslant 10^7` : coût :math:`\leqslant O(n \ln (n))`
* :math:`n > 10^8` : coût :math:`\leqslant O(n)`

Comprendre le coût d'un algorithme
++++++++++++++++++++++++++++++++++

Le coût de nombreux algorithmes non NP-complet se décomposer comme suit : 
:math:`O(n^\alpha) O( \ln^\beta n ) O(1)`. Chaque terme correspond à :

* :math:`O(n^\alpha)` avec :math:`\alpha \in \mathbb{N} > 1` : un probème combinatoire se résume à un algorithme
  de coût quadratique, cela est dû à la `programmation dynamique <https://fr.wikipedia.org/wiki/Programmation_dynamique>`_.
  Dans la plupart des cas, on obtient ce coût après avoir transformé le problème dans une forme
  récurrente : on écrit ce qu'il faut faire pour calculer la solution avec *n+1* éléments
  sachant qu'on connaît la solution avec *n* éléments.
* :math:`O(\n^\beta n)` avec :math:`\beta \in \mathbb{N} > 0`, 
  coût `dichotomique <https://fr.wikipedia.org/wiki/Recherche_dichotomique>`_, 
  on coupe le problème en deux à chaque itération.
* :math:`O(1)` : `table de hashage <https://fr.wikipedia.org/wiki/Table_de_hachage>`_

Dès qu'on sort des puissances entières, il faut s'attendre à un algorithme non trivial
tel que l'`algorithme de Strassen <https://fr.wikipedia.org/wiki/Algorithme_de_Strassen>`_
pour la multiplication de matrice (:math:`n^{2.807}), ou celui
de `Marco Bodrato <http://www.bodrato.it/papers/>`_ 
(`A Strassen-like Matrix Multiplication Suited for Squaring and Higher Power Computation <http://marco.bodrato.it/papers/Bodrato2010-StrassenLikeMatrixMultiplicationForSquares.pdf>`_).

Le coût minimal d'un algorithme de tri est :math:`O(n \ln n)` dans le cas générique 
c'est-à-dire sans hypothèse sur les données. En revanche, dans le cas où les données
sont issues d'un ensemble fini de cardinal *m*, le meilleur tri revient à calculer un histogramme
et est de coût inférieur à :math:`O( \inf \{ n \ln n, m \} )`.


Mot-clé
+++++++

L'objectif n'est pas de les comprendre tous mais plus de connaître
les problèmes pour lesquels ils ont été conçus. 

La distance d'édition sert à calculer la distance entre deux mots.
On peut l'utiliser pour trouver les mots les plus proches d'un autre
à condition que ces mots ne soient pas nombreux (:math:`\sim 10^4`).
Que faire quand ils sont un milliard ? Ce serait plus facile
si les mots étaient représentés par des vecteurs (voir 
`word2vec <https://pypi.python.org/pypi/word2vec>`_,
`Auto Encoders <https://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_).

On veut comparer deux modèles de ranking. 
On veut pouvoir comparer visuellement les résultats. Quel ordre
est mieux qu'un autre ? Comment afficher les résultats
de deux moteurs de recherche de telle sorte que l'oeil
humain saisisse rapidement la différence ?

Tout ce qui suit vous donnera des idées.

Catalogue
+++++++++

    
* Tri
    * `tri fusion <http://fr.wikipedia.org/wiki/Tri_fusion>`_ **algo**
    * `bucket sort <http://en.wikipedia.org/wiki/Bucket_sort>`_ **algo**
    * `tri à bulles <http://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles>`_ **algo**
* Diviser pour reigner
    * `dichotomie <http://fr.wikipedia.org/wiki/Dichotomie>`_ **algo**
    * `branch and bound <http://en.wikipedia.org/wiki/Branch_and_bound>`_ **algo**
* Programmation dynamique
    * `distance d'édition <http://fr.wikipedia.org/wiki/Distance_de_Levenshtein>`_ **algo**
    * `plus court chemin dans un graphe <orghttp://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra>`_ **algo**
    * `problème d'ordonnancement <http://fr.wikipedia.org/wiki/Th%C3%A9orie_de_l'ordonnancement>`_ **algo**
* Problème non `NP-complet <http://fr.wikipedia.org/wiki/Liste_de_probl%C3%A8mes_NP-complets>`_
    * `Problème du voyageur de commerce <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce>`_  **algo**
      (ou `Graphe Hamiltonien <http://fr.wikipedia.org/wiki/Graphe_hamiltonien>`_)
    * `Problème de tournées de véhicules <https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_tourn%C3%A9es_de_v%C3%A9hicules>`_ **algo**,
      extension du problème du voyageur de commerce
    * `problème d'affectation, méthode hongroise <http://fr.wikipedia.org/wiki/Algorithme_hongrois>`_ **algo**
    * `arbre de poids miminum (Kruskal) <http://fr.wikipedia.org/wiki/Algorithme_de_Kruskal>`_ **algo**
    * `problème du sac-à-dos <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos>`_ **algo**
* Structure de données
    * `liste chaînée <http://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e>`_ **déf**
    * `table de hachage <http://fr.wikipedia.org/wiki/Table_de_hachage>`_ **déf**
    * `suffix tree <http://fr.wikipedia.org/wiki/Arbre_des_suffixes>`_ **déf**
    * `trie <http://fr.wikipedia.org/wiki/Trie_(informatique)>`_ **déf**
    * `b-tree <http://fr.wikipedia.org/wiki/Arbre_B>`_ **déf**
* Graphes
    * composantes connexes ou `parcours de graphe en profondeur <http://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur>`_, 
      `parcours de graphe en largeur <http://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur>`_ **déf/algo**
    * `graphe orienté <http://fr.wikipedia.org/wiki/Graphe_orient%C3%A9>`_, `graphe acyclique <http://fr.wikipedia.org/wiki/Graphe_acyclique>`_ **déf**
    * `degré <http://fr.wikipedia.org/wiki/Degr%C3%A9_(th%C3%A9orie_des_graphes)>`_ **déf**
    * `FLoyd-Flukerson <http://fr.wikipedia.org/wiki/Algorithme_de_Ford-Fulkerson>`_ **algo**
    * `minimum cut <http://en.wikipedia.org/wiki/Minimum_cut>`_ **algo**
    * `maximum cut <http://en.wikipedia.org/wiki/Maximum_cut>`_ **algo**
    * `graphe bi-parti <http://fr.wikipedia.org/wiki/Graphe_biparti>`_ **déf**
    * `PageRank <http://fr.wikipedia.org/wiki/PageRank>`_ **algo**
    * `Appariement <http://fr.wikipedia.org/wiki/Couplage_(th%C3%A9orie_des_graphes)>`_, 
      `Edmonds Blossum <http://en.wikipedia.org/wiki/Blossom_algorithm>`_, 
      `Hopcroft–Karp <http://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm>`_,
      `Blossom 5 <http://pub.ist.ac.at/~vnk/papers/blossom5.pdf>`_,
      **déf/algo** (ou couplage)
    * `Algorithme de Gale-Shapley <http://fr.wikipedia.org/wiki/Probl%C3%A8me_des_mariages_stables>`_, **algo**, problème des mariages stables
    * `distance de Robinson–Foulds <https://en.wikipedia.org/wiki/Robinson%E2%80%93Foulds_metric>`_, **algo**, distance entre deux arbres
* Texte
    * `Algorithme de Knuth-Morris-Pratt <http://fr.wikipedia.org/wiki/Algorithme_de_Knuth-Morris-Pratt>`_ **algo**
    * `Algorithme de Rabin-Karp <http://fr.wikipedia.org/wiki/Algorithme_de_Rabin-Karp>`_ **algo**
    * `distance de Jaccard <http://fr.wikipedia.org/wiki/Indice_et_distance_de_Jaccard>`_ **algo**
    * `n-grammes <http://fr.wikipedia.org/wiki/N-gramme>`_ **déf**
    * `Algorithme d'Aho-Corasick <http://fr.wikipedia.org/wiki/Algorithme_d%27Aho-Corasick>`_ **algo**
    * `Transformée de Burrows-Wheeler <http://fr.wikipedia.org/wiki/Transform%C3%A9e_de_Burrows-Wheeler>`_ **algo**
    * `algorithme Apriori <https://en.wikipedia.org/wiki/Apriori_algorithm>`_ : apprentissage de règles d'associations **algo**
* Autre
    * `codage Huffman <http://fr.wikipedia.org/wiki/Codage_de_Huffman>`_ (voir aussi `LZ77, LZ78 <http://fr.wikipedia.org/wiki/LZ77_et_LZ78>`_) **algo**
    * `bootstrap, intervalles de confiance <http://fr.wikipedia.org/wiki/Bootstrap_(statistiques)#Intervalle_de_confiance>`_ **algo**
    * `filtre de Bloom <http://fr.wikipedia.org/wiki/Filtre_de_Bloom>`_ **algo**
    * `Algorithme de Strassen <http://fr.wikipedia.org/wiki/Algorithme_de_Strassen>`_ **algo**
    * `Simplexe <http://fr.wikipedia.org/wiki/Simplexe>`_ **algo**
    * `Woodbury matrix identity <http://en.wikipedia.org/wiki/Woodbury_matrix_identity>`_ **algo**
    * `Blockwise inversion <http://en.wikipedia.org/wiki/Invertible_matrix#Blockwise_inversion>`_ **algo**
    * `Toom-Cook <https://en.wikipedia.org/wiki/Toom%E2%80%93Cook_multiplication>`_ **algo**
* Programmation
    * `itérateur <http://fr.wikipedia.org/wiki/It%C3%A9rateur>`_ (mot-clé `yield <http://sametmax.com/comment-utiliser-yield-et-les-generateurs-en-python/>`_) **déf**
    * `mémoïzation <http://fr.wikipedia.org/wiki/M%C3%A9mo%C3%AFsation>`_ **déf** (voir aussi `Mémoïzation d'une fonction Python <http://sametmax.com/memoization-dune-fonction-python/>`_)
    * `programmation fonctionnelle <http://fr.wikipedia.org/wiki/Programmation_fonctionnelle>`_ **déf**
    * `récursivité <http://fr.wikipedia.org/wiki/R%C3%A9cursivit%C3%A9>`_ **déf**
    
    
Liens
+++++

* `Liste d'algorithme sur Wikipédia <http://en.wikipedia.org/wiki/List_of_algorithms>`_ 
  (`version française <http://fr.wikipedia.org/wiki/Liste_d%27algorithmes>`_)
* `List of machine learning concepts <http://en.wikipedia.org/wiki/List_of_machine_learning_concepts>`_
