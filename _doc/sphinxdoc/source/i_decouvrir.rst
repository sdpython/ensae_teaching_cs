
.. _l-extra:
.. _l-expose-explication:

=========
Découvrir
=========

.. contents::
    :local:

Culture algorithmique
=====================

Programmation récréative, algorithmes, bouts de code, chaque exemple
est indépendante des autres et propose un problème ou un jeu
qu'on peut résoudre grâce à un algorithme et un peu d'imagination.

* :ref:`l-algoculture`
* :ref:`l-np-complets`

Algorithmes illustrés
=====================

*Finance*

.. toctree::
    :maxdepth: 1

    specials/finance_autostrat

*Graphes*

.. toctree::
    :maxdepth: 1

    specials/tsp_kohonen
    specials/tsp_kruskal
    notebooks/expose_graphe_et_map_reduce
    notebooks/expose_rwr_recommandation
    notebooks/expose_TSP
    specials/floyd_dice

*Images*

.. toctree::
    :maxdepth: 1

    specials/image_synthese
    specials/corde

*Puzzles*

.. toctree::
    :maxdepth: 1

    notebooks/expose_vigenere
    notebooks/expose_einstein_riddle
    specials/puzzle_girafe
    specials/puzzle_2
    specials/hermionne
    specials/sudoku

*Statistiques*

.. toctree::
    :maxdepth: 1

    notebooks/hash_distribution

*Streaming*

.. toctree::
    :maxdepth: 1

    notebooks/BJKST

.. index:: entretien, entretien d'embauche, algorithme

**Algorithmes réutilisables**

* :func:`tsp_kruskal_algorithm <ensae_teaching_cs.special.tsp_kruskal.tsp_kruskal_algorithm>`: `TSP <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
* :func:`draw_line <ensae_teaching_cs.special.tsp_bresenham.draw_line>`: `Bresenham <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`_ algorithm (line)
* :func:`draw_ellipse <ensae_teaching_cs.special.tsp_bresenham.draw_ellipse>`: `Bresenham <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`_ algorithm (ellipse)
* :func:`distance_haversine <ensae_teaching_cs.special.rues_paris.distance_haversine>`: distance of `Haversine <https://en.wikipedia.org/wiki/Haversine_formula>`_
* :func:`bellman <ensae_teaching_cs.special.rues_paris.bellman>`: shortest paths in a graph with `Bellman-Ford <http://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford>`_
* :func:`connected_components <ensae_teaching_cs.special.rues_paris.connected_components>`: computes the `connected components <https://en.wikipedia.org/wiki/Connected_component_(graph_theory)>`_
* :func:`graph_degree <ensae_teaching_cs.special.rues_paris.graph_degree>`: computes the degree of each node in a graph `degree <https://en.wikipedia.org/wiki/Degree_(graph_theory)>`_
* :func:`resolution_sudoku <ensae_teaching_cs.special.sudoku.resolution_sudoku>`: solves a `sudoku <https://fr.wikipedia.org/wiki/Sudoku>`_

Machine learning illustré
=========================

.. toctree::
    :maxdepth: 1

    i_visualisation
    elections
    notebooks/expose_velib
    notebooks/ml_table_mortalite
    notebooks/ml_huge_datasets
    notebooks/ml_rue_paris_parcours
    specials/voisinage
    specials/elections

.. todoext::
    :title: Quelques idées de notebooks pour le futur
    :tag: plus

    * `bootstrap pair <http://www.stat.ncsu.edu/people/lu/courses/ST505/Ch2.pdf>`_
    * `The Large-Sample Power of Tests Based on Permutations of Observations <http://projecteuclid.org/euclid.aoms/1177729436>`_
    * `On Some Pitfalls in Automatic Evaluation and Significance Testing for MT <http://www.cl.uni-heidelberg.de/~riezler/publications/papers/ACL05WS.pdf>`_
    * `More accurate tests for the statistical significance of result differences <http://arxiv.org/pdf/cs/0008005v1.pdf>`_
    * `Randomized Significance Tests in Machine Translation <http://www.statmt.org/wmt14/pdf/W14-3333.pdf>`_
    * `Statistical Hypothesis Tests for NLP <http://masanjin.net/sigtest.pdf>`_
    * `Unit 4: Inference for numerical variables Lecture 1: Bootstrap, paired, and two sample <http://stat.duke.edu/courses/Spring13/sta101.001/slides/unit4lec1H.pdf>`_
