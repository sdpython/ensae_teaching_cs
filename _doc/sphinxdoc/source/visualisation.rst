

.. _l-visualisation:


Visualisation
=============

Modules
+++++++

Ces notebooks parcourent différents exemples de visualisations avec différentes librairies.
Liste non exhaustive.

.. toctree::
    :maxdepth: 1
    
    notebooks/lightning_python

Galleries
+++++++++

*Quelques fonctions en guise d'exemples*

* :func:`graph_cities <ensae_teaching_cs.faq.faq_matplotlib.graph_cities>` : 
  représenter des points sur une **carte**
* :func:`graph_ggplot_with_label <ensae_teaching_cs.faq.faq_matplotlib.graph_ggplot_with_label>` :
  n'afficher qu'un nombre réduit de labels sur l'axe des abscisses en fonction de la taille du graphe demandée
* :mod:`matplotlib_helper_xyz <ensae_teaching_cs.helpers.matplotlib_helper_xyz>` :
  trois fonctions pour afficher des **scatter plots** (graphes XY) avec plusieurs couleurs, des **lignes de niveau**, 
  ou une courbe en **3D** définie à partir de quelques points
* `2A : TD 4B : Visualisation <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_enonce.html#seance6graphesenoncerst>`_
  (`correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_correction.html#seance6graphescorrectionrst>`_),
  ce notebook présente un moyen de faire une **carte** géographique, **seaborn**
* :ref:`td2acorrectionsession4arst` : courbe `ROC <https://fr.wikipedia.org/wiki/Receiver_operating_characteristic>`_ et 
  `ACP <https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales>`_ avec labels      
* :ref:`1A :TD 12 : Visualisation des données <td1acenoncesession12rst>`  (:ref:`correction <td1acorrectionsession12rst>`) :
  représentation de **graphes** (`networkx <https://networkx.github.io/>`_, 
  `graphviz <http://www.graphviz.org/>`_), `Open Street Map <http://www.openstreetmap.org/>`_ 
  avec `folium <https://github.com/python-visualization/folium>`_
* :ref:`2A : TD 3B : Arbres de décision et Random Forests <td2acenoncesession3brst>` : 
  représentation d'un **arbre de décision**

  
Trucs et astuces
++++++++++++++++

  
* :func:`avoid_overlapping_dates <ensae_teaching_cs.faq.faq_matplotlib.avoid_overlapping_dates>` : 
  éviter la superposition des dates sur l'axe des abscisses
* :func:`change_legend_location <ensae_teaching_cs.faq.faq_matplotlib.change_legend_location>` : 
  changer la position de la légende
* :func:`graph_style <ensae_teaching_cs.faq.faq_matplotlib.graph_style>` : 
  changer le style d'un graphe
