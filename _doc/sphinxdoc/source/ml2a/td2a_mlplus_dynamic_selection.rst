
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-dynamic-selection-ml:

Sélection dynamique de modèles
++++++++++++++++++++++++++++++

La plupart du temps, on souhaite sélectionner le meilleur
modèle sur l'ensemble d'une base de données. Cette fois-ci,
le problème est de sélectionner le ou les meilleurs modèles
pour une observation donnée. Ces techniques introduisent
la notion de *compétence* d'un modèle ce qui revient à
choisir le modèle le plus compétent pour une observation donnée.
Elles utilisent les plus proches voisins pour déterminer
les performances des modèles autour d'un voisinage d'un point
donné.

*Notebooks*

*(à venir)*

*Lectures*

* `Dynamic classifier selection: Recent advances and perspectives
  <https://www.sciencedirect.com/science/article/pii/S1566253517304074>`_
* `A survey of multiple classifier systems as hybrid systems
  <https://www.sciencedirect.com/science/article/abs/pii/S156625351300047X>`_
* `A probabilistic model of classifier competence for dynamic ensemble selection
  <http://ccc.inaoep.mx/~ariel/2012/A%20probabilistic%20model%20of%20classifier%20competence%20for%20dynamic%20ensemble%20selection.pdf>`_
* `Classifier Selection
  <https://www.cs.rit.edu/~rlaz/prec20092/slides/ClassifierSelection.pdf>`

*Modules*

* `deslib <https://deslib.readthedocs.io/en/latest/>`_
