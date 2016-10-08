
Machine Learning
================

La bible que tout le monde recommande :
`The Elements of Statistical Learning <http://statweb.stanford.edu/~tibs/ElemStatLearn/>`_, Trevor Hastie, Robert Tibshirani, Jerome Friedman

Modèle ou features ?
++++++++++++++++++++

On passe 90% du temps à créer de nouvelles features, 10% restant à améliorer
les paramètres du modèle : 
:ref:`Travailleur les features ou changer de modèle <mlfeaturesmodelrst>`.

XGBoost
+++++++

`XGBoost <https://github.com/dmlc/xgboost>`_ 
est une librairie de machine learning connue pour avoir gagné de nombreuses 
`compétitions <https://github.com/dmlc/xgboost/blob/master/demo/README.md#machine-learning-challenge-winning-solutions>`_.
Extrait de `XGBoost: A Scalable Tree Boosting System <https://arxiv.org/pdf/1603.02754.pdf>`_ :

.. image:: images/xgboost.png
    :height: 400
    

Plusieurs améliorations ont été implémentées pour rendre l'apprentissage rapide
et capable de gérer de gros volumes de données :

* *exact greedy :* algorithme standard pour apprendre une forêt aléatoire
* *approximate global :* chaque noeud est un seuil sur une variable, ce seuil est choisi
  parmi toutes les valeurs possibles ou des quantiles, ces quantiles sont fixes pour un arbre
* *approximate local :* ou ces quantiles sont réalustés pour chaque noeud
* *out-of-core :* la librairie compresse les valeurs des variables par colonnes pour réduire l'empreinte
  mémoire
* *sparsity aware :* la librairie tient compte des valeurs manquantes qui ne sont pas traitées
  comme des valeurs comme les autres, chaque noeud d'un arbre possède une direction par défaut 
* *parallel :* certains traitements sont parallélisés

Interprétabilité
++++++++++++++++

* `Making Tree Ensembles Interpretable <https://arxiv.org/pdf/1606.05390v1.pdf>`_
* `Confidence Intervals for Random Forests: The Jackknife and the Infinitesimal Jackknife <http://jmlr.csail.mit.edu/papers/volume15/wager14a/wager14a.pdf>`_
* `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_
* `Understanding variable importances in forests of randomized trees <http://papers.nips.cc/paper/4928-understanding-variable-importances-in-forests-of-randomized-trees.pdf>`_
