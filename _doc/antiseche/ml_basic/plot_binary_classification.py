# -*- coding: utf-8 -*-
"""
Classification Binaire
======================

Un problème de classification binaire consiste à trouver
un moyen de séparer deux nuages de points
(voir `classification <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn_3_clas.html>`_).

.. contents::
    :local:
"""

###########################
#
# Principe
# --------
#
# On commence par générer un nuage de points artificiel.

from sklearn.datasets import make_classification
X, Y = make_classification(n_samples=100, n_features=2, n_classes=2,
                           n_repeated=0, n_redundant=0)

###########################
# On représente ces données.

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5, 5))
ax = plt.subplot()
ax.plot(X[Y == 0, 0], X[Y == 0, 1], "ob")
ax.plot(X[Y == 1, 0], X[Y == 1, 1], "or")

##########################
# D'un point de vue géométrique, un problème de classification
# consiste à trouver la meilleure frontière entre deux nuages
# de points. Le plus simple est de supposer que c'est une
# droite. Dans ce cas, on choisira un modèle de
# régression logistique :
# `LogisticRegression <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html>`_.

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X, Y)

##############################
# L'optimisation du modèle produit une droite
# dont les coefficients sont :
print(logreg.coef_, logreg.intercept_)

###############################
# Nous pourrions tracer cette droite mais ce graphe
# ne serait valable que pour un modèle linéaire.
# Il est aussi facile de colorier le fond du graphe avec
# la couleur de la classe prédite par le modèle.

import numpy


def colorie(X, model, ax, fig):
    xmin, xmax = numpy.min(X[:, 0]), numpy.max(X[:, 0])
    ymin, ymax = numpy.min(X[:, 1]), numpy.max(X[:, 1])
    hx = (xmax - xmin) / 100
    hy = (ymax - ymin) / 100
    xx, yy = numpy.mgrid[xmin:xmax:hx, ymin:ymax:hy]
    grid = numpy.c_[xx.ravel(), yy.ravel()]
    probs = model.predict_proba(grid)[:, 1].reshape(xx.shape)

    contour = ax.contourf(xx, yy, probs, 25, cmap="RdBu", vmin=0, vmax=1)
    ax_c = fig.colorbar(contour)
    ax_c.set_label("$P(y = 1)$")
    ax_c.set_ticks([0, .25, .5, .75, 1])
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])


fig = plt.figure(figsize=(7, 5))
ax = plt.subplot()
colorie(X, logreg, ax, fig)
ax.scatter(X[:, 0], X[:, 1], c=Y, s=50,
           cmap="RdBu", vmin=-.2, vmax=1.2,
           edgecolor="white", linewidth=1)
ax.set(aspect="equal", xlabel="$X_1$", ylabel="$X_2$")

##############################
#
# Evaluation
# ----------
#
# Il y a deux tests qu'on effectue de façon quasi-systématique
# pour ce type de problème : une  :epkg:`matrice de confusion`
# et une courbe :epkg:`ROC`.

plt.show()
