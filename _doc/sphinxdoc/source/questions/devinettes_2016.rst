
.. _l-devinettes-2016:

Devinettes 2016
===============

Q1 : groupby et NaN
+++++++++++++++++++

*Que se passe-t-il lorsqu'on application un groupby (dataframe)
sur une colonne qui contient des valeurs manquantes ?*

Elles ne sont tout simplement pas prise en compte.

`Pandas et groupby <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/notebooks/pandas_groupby.html#groupby-et-valeur-manquantes>`_.

Q2 : float et double
++++++++++++++++++++

En informatique, on utilise deux types de réels, les float (4 octets) et
les double (8 octets = plus précis). Pourquoi quelques librairies de
machine learning utilisent des float ?
(comme `xgboost <https://github.com/dmlc/xgboost>`_,
ou `scikit-learn <https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/tree.py#L123>`_).

Même si les float sont deux fois plus petits, les processeurs 64 bit sont aussi rapides pour faire
du calcul en double précision (lire aussi `SIMD <https://en.wikipedia.org/wiki/SIMD>`_).
Le principal avantage est l'emprunte mémoire réduite de moitié avec des floats.
Côté GPU, les cartes graphiques capables de calcul avec des doubles sont significativement
plus chère et cette précision pour la génération d'images virtuelles.

* `What Every Computer Scientist Should Know About Floating-Point Arithmetic <http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html>`_
* `Random thoughts on High Performance Computing <https://blogs.fau.de/hager/>`_

Q3 : imbalanced
+++++++++++++++

Un jeu de données `imabalenced <http://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/>`_ ...

Q4 : multiclass et imabalanced
++++++++++++++++++++++++++++++
