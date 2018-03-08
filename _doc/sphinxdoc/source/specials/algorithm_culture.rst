
.. index:: culture algorithmique, algorithme, culture

.. _l-algoculture:

Survol algorithmique
====================

.. contents::
    :local:

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
* :math:`O(n^\beta n)` avec :math:`\beta \in \mathbb{N} > 0`,
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

L'article de blog
`Fast Interesection of Sorted Lists Using SSE Instructions <https://highlyscalable.wordpress.com/2012/06/05/fast-intersection-sorted-lists-sse/>`_
part d'un problème simple qui est l'intersection de deux listes triées et montre
comment optimiser son implémentation en introduisant la notion de partitions et un peu
de parallélisation.

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

.. _l-algoculture-shortlist:

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
      (ou `Graphe Hamiltonien <http://fr.wikipedia.org/wiki/Graphe_hamiltonien>`_),
      lire `Solution of a Large-Scale Traveling-Salesman Problem <http://www.cs.uleth.ca/~benkoczi/OR/read/tsp-dantzig-fulkerson-johnson-54.pdf>`_.
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
    * `x-fast-trie <https://en.wikipedia.org/wiki/X-fast_trie>`_ **déf**
    * `Fibonacci Heap <https://en.wikipedia.org/wiki/Fibonacci_heap>`_ **déf**
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
    * robustesse d'un réseau
      `Quantifying the robustness of metro networks <https://arxiv.org/abs/1505.06664>`_
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
    * `Optimisation Combinatoire : Programmation Linéaire et Algorithmes <http://www-desir.lip6.fr/~fouilhoux/documents/OptComb.pdf>`_ **thèse**
    * `Canopy Clustering <https://en.wikipedia.org/wiki/Canopy_clustering_algorithm>`_ **algo**
* Programmation
    * `itérateur <http://fr.wikipedia.org/wiki/It%C3%A9rateur>`_ (mot-clé `yield <http://sametmax.com/comment-utiliser-yield-et-les-generateurs-en-python/>`_) **déf**
    * `mémoïzation <http://fr.wikipedia.org/wiki/M%C3%A9mo%C3%AFsation>`_ **déf** (voir aussi `Mémoïzation d'une fonction Python <http://sametmax.com/memoization-dune-fonction-python/>`_)
    * `programmation fonctionnelle <http://fr.wikipedia.org/wiki/Programmation_fonctionnelle>`_ **déf**
    * `récursivité <http://fr.wikipedia.org/wiki/R%C3%A9cursivit%C3%A9>`_ **déf**
* Algorithmes probabilistes
    * `Probabilistic Data Structures for Web Analytics and Data Mining <https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/>`_

Problèmes NP-complets
+++++++++++++++++++++

* `21 problèmes NP-complet de Karp <https://fr.wikipedia.org/wiki/21_probl%C3%A8mes_NP-complets_de_Karp>`_
* `Liste de problèmes NP complets <https://fr.wikipedia.org/wiki/Liste_de_probl%C3%A8mes_NP-complets>`_
  (`en <https://en.wikipedia.org/wiki/List_of_NP-complete_problems>`_)
* :ref:`l-np-complets`

Liens
+++++

* :ref:`l-problem-solved`
* `Liste d'algorithme sur Wikipédia <http://en.wikipedia.org/wiki/List_of_algorithms>`_
  (`version française <http://fr.wikipedia.org/wiki/Liste_d%27algorithmes>`_)
* `List of machine learning concepts <http://en.wikipedia.org/wiki/List_of_machine_learning_concepts>`_
* `Machine Learning, Statistiques et Programmation <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/index.html>`_
* `Introduction to graphs and networks <http://freakonometrics.hypotheses.org/51106>`_
  (échantillon dans un graphe, chaîne de Markov, centralité, ...)
* `Networks and Flows #2 <http://freakonometrics.hypotheses.org/51457>`_
* :ref:`Algorithmes classiques implémentés <l-blog-algo-impl>`

Articles sur des algorithmes
++++++++++++++++++++++++++++

* `Blossom5 <http://pub.ist.ac.at/~vnk/papers/blossom5.pdf>`_ **matching**
* `Local max-cut in smoothed polynomial time <http://blogs.princeton.edu/imabandit/2016/10/24/local-max-cut-in-smoothed-polynomial-time/>`_ **max-cut**

Livres
++++++

* `Précis de recherche opérationnelle <https://www.dunod.com/sciences-techniques/precis-recherche-operationnelle-methodes-et-exercices-d-application>`_,
  Robert Faure, Bernard Lemaire, Christophe Picouleau
* `Programming Pearls <https://www.amazon.com/Programming-Pearls-2nd-Jon-Bentley/dp/0201657880>`_,
  Jon Bentley
* `Introduction to Algorithms <https://mitpress.mit.edu/books/introduction-algorithms>`_,
  Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein
  
Pour s'entraîner
++++++++++++++++

* `Project Euler <https://projecteuler.net/about>`_
* `Google Jam <https://code.google.com/codejam/>`_

Google's recommandations
++++++++++++++++++++++++

*Coding*

You should know at least one programming language really well, 
and it should preferably be C++ or Java. C# is OK too, since 
it's pretty similar to Java. You will be expected to write some code 
in at least some of your interviews. You will be expected to know a 
fair amount of detail about your favorite programming language. 

*Sorting*

Know how to sort. Don't do bubble-sort. You should know the details of 
at least one :math:`n \log(n)` sorting algorithm, preferably two 
(say, quick sort and merge sort). Merge sort can be highly useful 
in situations where quick sort is impractical, so take a look at it.

*Hashtables*

Arguably the single most important data structure known to mankind. 
You absolutely should know how they work. Be able to implement one 
using only arrays in your favorite language, in about the space 
of one interview.

*Trees*

Know about trees; basic tree construction, traversal and manipulation 
algorithms. Familiarize yourself with binary trees, n-ary trees, 
and trie-trees. Be familiar with at least one type of balanced binary 
tree, whether it's a red/black tree, a splay tree or an AVL tree, 
and know how it's implemented. Understand treetraversal

*Algorithms*

BFS and DFS, and know the difference between inorder, postorder and preorder.

*Graphs*

Graphs are really important at Google. There are 3 basic ways to 
represent a graph in memory (objects and pointers, matrix, and 
adjacency list); familiarize yourself with each representation and its 
pros & cons. You should know the basic graph traversal algorithms: 
breadth-first search and depth-first search. Know their computational 
complexity, their tradeoffs, and how to implement them in real code. 
If you get a chance, try to study up on fancier algorithms, such 
as Dijkstra and A*.

*Other Data Structures*

You should study up on as many other data structures and algorithms as 
possible. You should especially know about the most famous classes of 
NP-complete problems, such as traveling salesman and the knapsack problem, 
and be able to recognize them when an interviewer asks you them in disguise. 
Find out whatNP-complete means.

*Mathematics*

Some interviewers ask basic discrete math questions. This is more prevalent 
at Google than at other companies because counting problems, probability problems
, and other Discrete Math 101 situations surrounds us. Spend some time 
before the interview refreshing your memory on (or teaching yourself) 
the essentials of combinatorics and probability. You should be familiar 
with n-choose-k problems and their ilk – the more the better.

*Operating Systems*

Know about processes, threads and concurrency issues. Know about locks and 
mutexes and semaphores and monitors and how they work. Knowabout deadlock 
and livelock and how to avoid them. Know what resources a processes needs, 
and a thread needs, and how context switching works, and how it's initiated 
by the operating system and underlying hardware. Know a little about 
scheduling. The world is rapidly moving towards multi-core, so know the 
fundamentals of "modern" concurrency constructs. For information on System 

*Design*

`Distributed Systems and Parallel Computing <http://research.google.com/pubs/DistributedSystemsandParallelComputing.html>`_

