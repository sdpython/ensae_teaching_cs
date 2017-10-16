# -*- coding: utf-8 -*-
"""
Grid Search
===========

Dans la plupart des cas, l'apprentissage des modèles dépend
d'hyperparamètres. Les valeurs par défaut choisies par
les auteurs des librairies de machine learning
fonctionnent dans la plupart des cas et dans d'autres il
peut être utile de les optimiser. La méthode la plus
simple consiste à essayer différentes valeurs puis à retenir
celle qui minimise l'erreur sur la base de test.

.. contents::
    :local:
"""

###########################
#
# Paramètre par défaut
# --------------------
#
# On commence par générer un jeu de données artificiel
# pour une régression.

from sklearn.datasets import make_friedman1
X, Y = make_friedman1(n_samples=500, n_features=5)

###########################
# On représente ces données.

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5, 5))
ax = plt.subplot()
ax.plot(X[:, 0], Y, '.')

##########################
# On choisira un modèle de régression linéaire
# avec une contrainte sur les coefficients
# `Lasso <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html>`_.

from sklearn.linear_model import Lasso
reglin = Lasso()
reglin.fit(X, Y)

##############################
# L'optimisation du modèle produit une droite
# dont les coefficients sont :
print(reglin.coef_, reglin.intercept_)

###############################
# On reprend le premier graphe est on y ajoute
# la droite qui correspond à la régression linéaire
# uniquement sur la première dimension.

reglin = Lasso()
reglin.fit(X[:, :1], Y)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5, 5))
ax = plt.subplot()
x = list(sorted(X[:, :1]))
y = reglin.predict(x)
ax.plot(X[:, 0], Y, '.')
ax.plot(x, y)

########################
#
# Gird Search
# -----------
#
# On optimise la valeur du paramètre :math:`\alpha`
# en choisissant différent valeur entre 0.5 et 2.


from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(
    Lasso(), {'alpha': [1e-5, 0.01, 0.1, 0.5, 0.8, 1]}, verbose=3)
grid.fit(X[:, :1], Y)

###########################
# On affiche les résultats.

import pandas
df = pandas.DataFrame(grid.cv_results_)
df["alpha"] = df.params.apply(lambda x: x["alpha"])
print(df)

###########################
# Sur cet exemple, la contrainte Lasso dégrade beaucoup les performances.

fig = plt.figure(figsize=(5, 5))
ax = plt.subplot()
df.set_index("alpha")[["mean_test_score"]].plot(ax=ax)
ax.set_xlabel("alpha")
ax.set_ylabel("mean_test_score")

##########################
# On représente les prédictions pour le meilleur modèle.


fig = plt.figure(figsize=(5, 5))
ax = plt.subplot()
x = list(sorted(X[:, :1]))
y = grid.predict(x)
ax.plot(X[:, 0], Y, '.')
ax.plot(x, y)

#############################
#
# Overfitting
# -----------
#
# Par défaut :epkg:`scikit-learn` optimise les hyperparamètres
# tout en faisant une cross-validation. Sans celle-ci,
# c'est comme si le modèle optimisait ses coefficients sur la
# base d'apprentissage et ses hyperparamètres sur la base de test.
# De ce fait, toutes les données servent à optimiser un paramètre.
# La cross-validation limite en vérifiant la stabilité de l'apprentissage
# sur plusieurs découpages. On peut également
# découper en train / test / validation mais cela réduit d'autant
# le nombre de données pour apprendre.


# plt.show()
