
.. _l-machine-learning-tips:

Machine Learning - Repères
==========================

Cette page est un petit catalogue des problèmes et termes
les plus usités en machine learning.

.. contents::
    :local:

Problèmes classiques
++++++++++++++++++++

Les problèmes les plus simples supposent toujours qu'on
disposent d'un jeu d'observations indépendantes les unes
des autres et qu'on optimise un critère numérique.
On distingue deux classes :

**non supervisé**

On dispose d'une suite de vecteurs indépendants et
identiquement distribués, :math:`(X_i)` dans un espace de dimension *d*,
on minimise un critère :

.. math::

    E(X) = f(X_1, ..., X_n)

**supervisé**

On dispose d'une suite de vecteurs indépendants et
identiquement distribués, :math:`(X_i)` dans un espace de dimension *d*,
et d'une séquence de labels qui représente la réponse connue.
On minimise une fonction d'erreur :

.. math::

    E(X, Y) = \sum_i e(f(X_i), Y_i)

La fonction *f* est un prédicteur (ou une fonction de scoring en anglais).

* :ref:`sphx_glr_ml_basic_plot_binary_classification.py` (supervisé)
* :ref:`sphx_glr_ml_basic_plot_regression.py` (supervisé)
* ranking (supervisé)
* recommandation (supervisé)
* ACP (non supervisé)
* :ref:`sphx_glr_ml_basic_plot_clustering.py` (non supervisé)

Frontière, Optimisation
+++++++++++++++++++++++

Dans le cas de problème supervisé, on distingue les paramètres :math:`\Theta`
et la fonction *f*.

.. math::

    E(X, Y, \Theta, f) = \sum_i e(f(\Theta, X_i), Y_i)

Par exemple, dans un problème de classification, la fonction *f* détermine
la forme que peut prendre la frontière entre deux classes. Linéaire pour
un modèle linéaire, en escalier pour un arbre, courbe pour un réseau
de neurones. Parmi tous ces modèles, on distingue deux classes qui
s'optimisent chacune d'une manière particulière.

`gradient <https://en.wikipedia.org/wiki/Gradient_descent>`_

Les fonctions *f* et *e* sont dérivables par rapport à :math:`\Theta`.
Les paramètres sont optimisés grâce à une méthode de descente de gradient.
La plue connue est la
`Algorithme du gradient stochastique <https://fr.wikipedia.org/wiki/Algorithme_du_gradient_stochastique>`_.
Un tel algorithme n'aime les variables discrètes car l'ensemble des valeurs que le
gradient peut prendre est limité. Il n'aime pas non plus les entrées hétérogènes
(non normalisées) car le gradient prendra des valeurs élevés sur certains
dimensions et faibles sur d'autres.

`ensemble <https://en.wikipedia.org/wiki/Ensemble_learning>`_

La fonction *f* n'est pas dérivable. Il n'y a pas de gradient possible.
Le plus souvent, on en revient à trier les observations selon une dimension
puis à déterminer un seuil de coupure approprié par rapport à la cible.
Ce type d'algorithme produit souvent des assemblages de fonctions
en escalier. En contre partie, les variables discrètes ou non normalisées
ne le gênent pas.

Fonction de coût - loss function
++++++++++++++++++++++++++++++++

C'est le critère qu'on cherche à optimiser. Il est parfois liée
au modèle *f* choisi mais il est rare qu'une fonction *f* puisse être
associée à une seule fonction de coût. Elle est en revanche liée au problème
à résoudre (classification, régression, ranking, recommandation). A chaque
problème, son ensemble de métriques correspondant.

`Classification <http://scikit-learn.org/stable/modules/classes.html#classification-metrics>`_

La fonction de coût pénalise la distance d'un point où la prédiction
est mauvaise à la frontière entre deux classes.
La norme `L1 <https://en.wikipedia.org/wiki/Norm_(mathematics)#Absolute-value_norm>`_
pénalise linéairement et est moins sensible aux points aberrants.
La norme `L2 <https://en.wikipedia.org/wiki/Norm_(mathematics)#Euclidean_norm>`_
pénalise quadratiquement.

`Régression <http://scikit-learn.org/stable/modules/classes.html#regression-metrics>`_

La fonction de coût pénalise l'écart entre la valeur attendue
et la valeur prédite. On retrouve les mêmes propriétés pour les normes
`L1 <https://en.wikipedia.org/wiki/Norm_(mathematics)#Absolute-value_norm>`_
et `L2 <https://en.wikipedia.org/wiki/Norm_(mathematics)#Euclidean_norm>`_.

`Ranking <http://scikit-learn.org/stable/modules/classes.html#pairwise-metrics>`_,
`Recommandation <https://www.quora.com/What-metrics-are-used-for-evaluating-recommender-systems>`_

Les deux problèmes sont assez similaires quoique mieux posé dans le cas
du ranking. La différence vient souvent de leur utilisation. Un modèle de ranking
répond toujours la même chose et est facile à évaluer. Un modèle de recommandation
est souvent évalué indirectement. Il est utilie
On pénalise l'ordre entre la liste de résultats prédite et celle attendue,
on mesure la `précision et le rappel <https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Precision_at_K>`_
à une position donnée.

`Clustering <http://scikit-learn.org/stable/modules/classes.html#clustering-metrics>`_

Il n'y a pas de vraiment parfaite car le clustering est souvent un résultat
intermédiaire ou une méthode d'exploration des données.

`Projection <http://scikit-learn.org/stable/modules/classes.html#module-sklearn.decomposition>`_
(`manifold <http://scikit-learn.org/stable/modules/classes.html#module-sklearn.manifold>`_)

Ces méthodes réduisent les dimensions, enlève le bruit. La métrique dépend
de l'algorithme choisi.

Train/Test
++++++++++

On dispose de peu de résultat théorique sur la précision des modèles
excepté dans le cas linéaire. Pour s'assurer qu'un modèle est pertinent, on
calcule des prédictions sur des données qui n'ont pas servi à estimer ses
coefficients.

Overfitting (Sur apprentissage)
+++++++++++++++++++++++++++++++

Le modèle s'est spécialisé sur la base d'apprentissage et ses prédictions
sont mauvaises sur toute nouvelle donnée. Il n'arrive pas à généraliser.
On dit aussi qu'il a appris le bruit dans les données d'apprentissage.

Cross-validation
++++++++++++++++

Une fois qu'un modèle est appris, il est testé sur un jeu de données
*test* différent des données d'apprentissage. Mais cela ne donne qu'une valeur
sans assurance que la prédiction soit reproductible. La
`cross validation <http://scikit-learn.org/stable/modules/cross_validation.html>`_
consiste à recommencer sur plusieurs découpages train/test différents
du jeu de données initial de manière à s'assurer que la prédiction est
stable.

Hyperparamètres
+++++++++++++++

Un `hyperparamètre <https://en.wikipedia.org/wiki/Hyperparameter>`_
n'est pas appris par l'algorithme d'apprentissage, il définit
la façon dont le modèle est appris. Le pas de gradient, le nombre de coefficients,
le type de modèles sont des hyperparamètres.

Boosting
++++++++

La plupart du temps, chaque observation a le même poids que toutes les autres
lors de l'apprentissage. Certaines techniques permettent d'en pondérer certaines
en fonction de l'erreur que le modèle fait. On peut soit donner plus de poids
`AdaBooost <http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html>`_ soit considérer qu'une erreur récurrente ne peut
venir que d'un point aberrant
`HuberRegressor <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html>`_.
