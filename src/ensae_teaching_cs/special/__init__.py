"""
@file
@brief Shortcuts to special

.. _l-almost_reusable:

List of almost reusable algorithms implemented in this module
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* @see fn tsp_kruskal_algorithm: `TSP <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_
* @see fn draw_line: `Bresenham <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`_ algorithm (line)
* @see fn draw_ellipse: `Bresenham <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`_ algorithm (ellipse)
* @see fn distance_haversine: distance of `Haversine <https://en.wikipedia.org/wiki/Haversine_formula>`_
* @see fn bellman: shortest paths in a graph with `Bellman-Ford <http://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford>`_
* @see fn connected_components: computes the `connected components <https://en.wikipedia.org/wiki/Connected_component_(graph_theory)>`_
* @see fn graph_degree: computes the degree of each node in a graph `degree <https://en.wikipedia.org/wiki/Degree_(graph_theory)>`_
* @see cl GraphDistance: computes a distance between two graphs (acyclic), see :ref:`l-graph_distance`
"""

from .tsp_kruskal import tsp_kruskal_algorithm
from .tsp_bresenham import draw_line, draw_ellipse
from .rues_paris import distance_haversine, bellman, connected_components, graph_degree
from .graph_distance import GraphDistance
