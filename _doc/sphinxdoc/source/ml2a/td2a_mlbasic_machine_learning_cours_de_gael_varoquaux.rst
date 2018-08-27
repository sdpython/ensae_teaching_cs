
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-ml-skgael:

Machine learning, cours de Gaël Varoquaux
+++++++++++++++++++++++++++++++++++++++++

`Gaël Varoquaux <http://gael-varoquaux.info/>`_
est un des concepteurs de
`scikit-learn <http://scikit-learn.org/stable/>`_.

* machine learning et `scikit-learn <http://scikit-learn.org/stable/>`_
  (`tutoriels sur scikit-learn <http://nbviewer.jupyter.org/github/GaelVaroquaux/sklearn_pandas_tutorial/tree/master/rendered_notebooks/>`_),
* *Quelques extraits.* Par définition les plus proches voisins ne font pas d'erreur sur la base d'apprentissage,
  l'apprentissage consiste à forcer le modèle à faire des erreurs. `Overfitting <http://en.wikipedia.org/wiki/Overfitting>`_ et
  `régularisation <http://en.wikipedia.org/wiki/Regularization_(mathematics)>`_.
  Erreur `L2 <http://en.wikipedia.org/wiki/Lp_space>`_ et pénalisation `L1 <http://fr.wikipedia.org/wiki/Espace_L1>`_.
  `RandomizedPCA <http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.RandomizedPCA.html>`_,
  `GridSearch <http://scikit-learn.org/stable/modules/grid_search.html>`_,
  `LassoCV <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html>`_.
  `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_.

Les `notes de lectures <https://github.com/GaelVaroquaux/sklearn_ensae_course>`_
(`Gaël Varoquaux <http://gael-varoquaux.info/>`_) sont disponibles sur GitHub et reprise
ici :

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_ensae_sklearn
    ../specials/machine_learning
    ../notebooks/td2a_eco_regressions_lineaires

La série d'articles suivante est tirée de
:epkg:`Freakeconometrics` revient sur les propriétés
des modèles de classification et régression illustrées
avec le langage :epkg:`R` :

* :ref:`Séries d'articles sur les modèles linéaires <post-freak-linear-models>`

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_statdes
    ../notebooks/_gs2a_ml_base

*Lectures*

* `API design for machine learning software: experiences from the scikit-learn project <https://arxiv.org/pdf/1309.0238.pdf>`_
* `Économétrie & Machine Learning <https://arxiv.org/pdf/1708.06992.pdf>`_
* `A Visual Introduction to Machine Learning <http://www.r2d3.us/visual-intro-to-machine-learning-part-1/>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `A Tour of Machine Learning Algorithms <http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/>`_
* `12 Algorithms Every Data Scientist Should Know <https://datafloq.com/read/12-algorithms-every-data-scientist-should-know/2024>`_ *(2016/06)*
* `10+2 Data Science Methods that Every Data Scientist Should Know in 2016 <http://tjo-en.hatenablog.com/entry/2016/04/18/190000>`_ *(2016/06)*
* `Complete Guide to Parameter Tuning in XGBoost (with codes in Python) <https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/>`_ *(2016/08)*
* `XGBoost: A Scalable Tree Boosting System <http://arxiv.org/pdf/1603.02754v1.pdf>`_, Tianqi Chen, Carlos Guestrin
* `Round Robin Classification <http://www.jmlr.org/papers/volume2/fuernkranz02a/fuernkranz02a.pdf>`_
* `ANN-Benchmarks: A Benchmarking Tool for Approximate Nearest Neighbor Algorithms? <http://www.itu.dk/people/maau/additional/sisap2017-preprint.pdf>`_
* `Time for a Change: a Tutorial for Comparing Multiple Classifiers Through Bayesian Analysis <http://www.jmlr.org/papers/volume18/16-305/16-305.pdf>`_

*Livres*

* `Python Data Science Handbook <https://github.com/jakevdp/PythonDataScienceHandbook>`_
* `The Elements of Statistical Learning <https://web.stanford.edu/~hastie/ElemStatLearn/>`_ :
  la bible que tout le monde recommande :

*Comprendre*

* `Explaining the Success of AdaBoost and Random Forests as Interpolating Classifiers <http://jmlr.org/papers/volume18/15-240/15-240.pdf>`_

*Modules*

* :epkg:`scikit-learn`
* :epkg:`statsmodels`
* :epkg:`XGBoost`

Et quelques autres comme :

* `annoy <https://github.com/spotify/annoy>`_
