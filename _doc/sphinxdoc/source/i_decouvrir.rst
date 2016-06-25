


.. _l-extra:
.. _l-expose-explication:


Découvrir
=========

Programmation récréative, algorithmes, bouts de code, chaque exemple
est indépendante des autres et propose un problème ou un jeu 
qu'on peut résoudre grâce à un algorithme et un peu d'imagination.


Algorithme
----------


Culture
^^^^^^^

.. toctree::
    :maxdepth: 1
    
    algorithm_culture


Algorithmes
^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    tsp_kohonen
    tsp_kruskal
    graph_distance
    notebooks/expose_graphe_et_map_reduce
    notebooks/expose_rwr_recommandation
    notebooks/expose_TSP
    image_synthese


Puzzles
^^^^^^^

.. toctree::
    :maxdepth: 1

    notebooks/expose_vigenere
    notebooks/expose_einstein_riddle
    puzzle_girafe
    hermionne
    sudoku

.. index:: entretien, entretien d'embauche, algorithme

Exercice classique d'algorithmie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
.. toctree::
    :maxdepth: 1

    notebooks/exercice_xn
    notebooks/exercice_echelle
    notebooks/exercice_morse
    notebooks/exercice_lcs
    notebooks/exercice_plus_grande_somme

Exemples simples et moins simples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    notebooks/pp_exo_deviner_un_nombre
    notebooks/pp_exo_deviner_un_nombre_correction
    notebooks/code_liste_tuple
    notebooks/code_multinomial
    all_example_ConstructionsClassiques
    
        

Algorithmes réutilisables
^^^^^^^^^^^^^^^^^^^^^^^^^

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






Machine learning
----------------


Ca tient presque dans un notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    elections
    notebooks/expose_velib
    notebooks/ml_table_mortalite
    notebooks/ml_huge_datasets
    notebooks/ml_rue_paris_parcours
    notebooks/ml_features_model
    

Simulation
^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    corde
    voisinage
    
Coding parties
^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 2
    
    coding_party
    

Techniques
----------

Web, cloud
^^^^^^^^^^

.. toctree::
    :maxdepth: 1
    
    azure
    siteflask
        
    
Pratiques
^^^^^^^^^

.. toctree::
    :maxdepth: 1
    
    unittest_coverage_git_profling    
    
Inclassables
------------

.. toctree::
    :maxdepth: 1
    
    all_example_Ngatifs
    all_example_Impossibleretenir    
    all_example_TD1A
    all_example_science
    all_example_techniques
    all_example_AutoTeachings    
    
    



