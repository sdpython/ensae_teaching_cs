
.. |pyecopng| image:: ../_static/pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: ../_static/pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

|pyecopng| |pystatpng|

.. _l-imbalanced-classification:

Imbalanced classification
+++++++++++++++++++++++++

.. index:: imbalanced, mal-balancé

Imbalanced, mal balancé, skewed, ce type de problème de données
est très fréquent. Il signifie qu'une classe dans un problème de classification
est sous-représentée par rapport aux autres et que le modèle de machine
learning n'est pas suffisamment pénalisé s'il n'en tient pas compte.
Le cas classique est un problème à deux classes, une majoritaire à 99%,
une minoritaire à 1%. Un modèle qui répond toujours la majorité est correct
99% du temps mais il n'a rien appris puisque sa réponse est constante.
Comment le forcer à apprendre quelque chose ? Il existe trois types approches
et la réponse est souvent un mélange des trois :

* *boosting* : le modèle pondère davantage les exemples sur lesquels il fait
  des erreurs, a fortiori, les exemples de la classe minoritaire
* *over sampling* : on multiplie les exemples de la classe minoritaire
  de façon à lui donner plus de poids
* *under sampling* : on réduit le nombre d'exemples de la classe majoritaire
  sans altérer la capacité du modèle à trouver une bonne solution, cela consiste
  à enlever des exemples loin de la frontière de classification.

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/ml_b_imbalanced

*Lectures*

* `Classification of Imbalanced Data with a Geometric Digraph Family <http://www.jmlr.org/papers/volume17/15-604/15-604.pdf>`_
* `RUSBoost: A Hybrid Approach to Alleviating Class Imbalance <http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=9260A5C92AC5F8FA3B8590A53A06248D?doi=10.1.1.309.2305&rep=rep1&type=pdf>`_
* `RAMOBoost: Ranked Minority Oversampling in Boosting <https://ai2-s2-pdfs.s3.amazonaws.com/9640/1540d5d8c4d5d956ae5fa487590dd8682507.pdf>`_
* `ND DIAL: Imbalanced Algorithms <https://github.com/dialnd/imbalanced-algorithms>`_
* `rusboost.py <https://github.com/harusametime/RUSBoost>`_ (plutôt un bout de code)
* `xgboost <https://xgboost.readthedocs.io/en/latest/>`_
* `Boosting and AdaBoost for Machine Learning <https://machinelearningmastery.com/boosting-and-adaboost-for-machine-learning/>`_,
  `A Gentle Introduction to the Gradient Boosting Algorithm for Machine Learning <https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/>`_,
  `Thoughts on Hypothesis Boosting <https://www.cis.upenn.edu/~mkearns/papers/boostnote.pdf>`_,
  `Predictions Games and Arcing Algorithms <https://www.stat.berkeley.edu/~breiman/games.pdf>`_

*Lectures - subsampling*

* `Data Subsampling (Edward) <http://edwardlib.org/api/inference-data-subsampling>`_
* `5601 Notes: The Subsampling Bootstrap <http://www.stat.umn.edu/geyer/5601/notes/sub.pdf>`_
* `Bootstrapping and Subsampling: Part I <https://normaldeviate.wordpress.com/2013/01/19/bootstrapping-and-subsampling-part-i/>`_
* `Subsampling versus bootstrapping in resampling-based model selection for multivariable regression <https://epub.ub.uni-muenchen.de/21724/1/technRep_171.pdf>`_
* `Subsampling vs Bootstrap <https://web.stanford.edu/~doubleh/lecturenotes/lecture13.pdf>`_

*Modules*

* `imbalanced-learn <https://github.com/scikit-learn-contrib/imbalanced-learn>`_
  (la documentation est intéressante)
