


.. _l-extra:
.. _l-expose-explication:

=========
Découvrir
=========

Culture algorithmique
=====================

Programmation récréative, algorithmes, bouts de code, chaque exemple
est indépendante des autres et propose un problème ou un jeu 
qu'on peut résoudre grâce à un algorithme et un peu d'imagination.

.. toctree::
    :maxdepth: 1
    
    specials/algorithm_culture
    
Algorithmes illustrés
=====================

**Finance**

.. toctree::
    :maxdepth: 1
    
    specials/finance_autostrat
    

**Graphes**

.. toctree::
    :maxdepth: 1

    specials/tsp_kohonen
    specials/tsp_kruskal
    specials/graph_distance
    notebooks/expose_graphe_et_map_reduce
    notebooks/expose_rwr_recommandation
    notebooks/expose_TSP

**Images**

.. toctree::
    :maxdepth: 1

    specials/image_synthese
    specials/corde
    
**Puzzles**

.. toctree::
    :maxdepth: 1

    notebooks/expose_vigenere
    notebooks/expose_einstein_riddle
    specials/puzzle_girafe
    specials/hermionne
    specials/sudoku

.. index:: entretien, entretien d'embauche, algorithme


    
**Algorithmes réutilisables**

* :func:`tsp_kruskal_algorithm <ensae_teaching_cs.special.tsp_kruskal.tsp_kruskal_algorithm>`: `TSP <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
* :func:`draw_line <ensae_teaching_cs.special.tsp_bresenham.draw_line>`: `Bresenham <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`_ algorithm (line)
* :func:`draw_ellipse <ensae_teaching_cs.special.tsp_bresenham.draw_ellipse>`: `Bresenham <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`_ algorithm (ellipse)
* :func:`distance_haversine <ensae_teaching_cs.special.rues_paris.distance_haversine>`: distance of `Haversine <https://en.wikipedia.org/wiki/Haversine_formula>`_
* :func:`bellman <ensae_teaching_cs.special.rues_paris.bellman>`: shortest paths in a graph with `Bellman-Ford <http://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford>`_
* :func:`connected_components <ensae_teaching_cs.special.rues_paris.connected_components>`: computes the `connected components <https://en.wikipedia.org/wiki/Connected_component_(graph_theory)>`_
* :func:`graph_degree <ensae_teaching_cs.special.rues_paris.graph_degree>`: computes the degree of each node in a graph `degree <https://en.wikipedia.org/wiki/Degree_(graph_theory)>`_
* :class:`GraphDistance <ensae_teaching_cs.special.graph_distance.GraphDistance>`: computes a distance between two graphs (acyclic), see :ref:`l-graph_distance`
* :func:`resolution_sudoku <ensae_teaching_cs.special.sudoku.resolution_sudoku>`: solves a `sudoku <https://fr.wikipedia.org/wiki/Sudoku>`_

        
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






Machine learning illustré
=========================


**Ca tient presque dans un notebook**

.. toctree::
    :maxdepth: 1

    elections
    notebooks/expose_velib
    notebooks/ml_table_mortalite
    notebooks/ml_huge_datasets
    notebooks/ml_rue_paris_parcours
    notebooks/ml_features_model
    coding_party
    
**Simulation**

.. toctree::
    :maxdepth: 1

    specials/voisinage
        

Cloud illustré
==============

.. toctree::
    :maxdepth: 1
    
    specials/azure
        
    
Génie logiciel illustré
=======================

.. toctree::
    :maxdepth: 1
    
    specials/unittest_coverage_git_profling    
    specials/siteflask
    
Aspects cachés de ce cours
==========================

.. toctree::
    :maxdepth: 1
    
    all_example_AutoTeachings    



