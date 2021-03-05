
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-ml2a-selvar:

Sélection de variables
++++++++++++++++++++++

La sélection de features peut paraître de moindre importance
dans un contexte où la puissance de calcul ne cesse d'augmenter mais
cette puissance est de plus en plus accessible via la parallélisation
qui nécessite quelques ajustements algorithmiques. L'ajout de features
complique également l'interprétation des résultats.

*Notebooks*

* :ref:`td2atreeselectionenoncerst`,
  :ref:`td2atreeselectioncorrectionrst`

*Lectures*

* `An Introduction to Variable and Feature Selection <http://www.jmlr.org/papers/volume3/guyon03a/guyon03a.pdf>`_
* `Feature Selection (wikipédia) <https://en.wikipedia.org/wiki/Feature_selection>`_
* `Feature Selection (scikit-learn) <http://scikit-learn.org/stable/modules/feature_selection.html>`_
* `Consistent Feature Selection for Pattern Recognition in Polynomial Time <http://jmlr.csail.mit.edu/papers/volume8/nilsson07a/nilsson07a.pdf>`_ (boruta)
* `Variable selection using pseudo-variables <https://arxiv.org/abs/1804.01201>`_ :
  l'article utilise la pénalisation pour classer les variables par importance,
  plus le modèle est pénalisé (type :epkg:`Lasso`), plus il réduit le nombre de variables.
* `Complete Search for Feature Selection in Decision Trees
  <http://jmlr.org/papers/volume20/18-035/18-035.pdf>`_

* *Modules*

* :epkg:`scikit-learn`
* `borutapy <https://github.com/scikit-learn-contrib/boruta_py>`_
