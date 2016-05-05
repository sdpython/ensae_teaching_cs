


.. _l-expose-explication:



Coups de projecteur
===================


Programmation récréative, algorithmes, bouts de code, chaque exemple
est indépendante des autres et propose un problème ou un jeu 
qu'on peut résoudre grâce à un algorithme et un peu d'imagination.



.. toctree::
    :maxdepth: 1

    corde
    puzzle_girafe
    hermionne
    tsp_kohonen
    tsp_kruskal
    graph_distance
    voisinage
    image_synthese
    elections
    
    
Certains de ces algorithmes sont réutilisables :

* :func:`tsp_kruskal_algorithm <ensae_teaching_cs.special.tsp_kruskal.tsp_kruskal_algorithm>`: `TSP <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
* :func:`draw_line <ensae_teaching_cs.special.tsp_bresenham.draw_line>`: `Bresenham <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`_ algorithm (line)
* :func:`draw_ellipse <ensae_teaching_cs.special.tsp_bresenham.draw_ellipse>`: `Bresenham <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`_ algorithm (ellipse)
* :func:`distance_haversine <ensae_teaching_cs.special.rues_paris.distance_haversine>`: distance of `Haversine <https://en.wikipedia.org/wiki/Haversine_formula>`_
* :func:`bellman <ensae_teaching_cs.special.rues_paris.bellman>`: shortest paths in a graph with `Bellman-Ford <http://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford>`_
* :func:`connected_components <ensae_teaching_cs.special.rues_paris.connected_components>`: computes the `connected components <https://en.wikipedia.org/wiki/Connected_component_(graph_theory)>`_
* :func:`graph_degree <ensae_teaching_cs.special.rues_paris.graph_degree>`: computes the degree of each node in a graph `degree <https://en.wikipedia.org/wiki/Degree_(graph_theory)>`_
* :class:`GraphDistance <ensae_teaching_cs.special.graph_distance.GraphDistance>`: computes a distance between two graphs (acyclic), see :ref:`l-graph_distance`

