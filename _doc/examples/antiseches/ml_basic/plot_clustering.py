# -*- coding: utf-8 -*-
"""
Clustering
==========

Le `clustering <https://fr.wikipedia.org/wiki/Partitionnement_de_donn%C3%A9es>`_
est une méthode non supervisée qui vise à répartir les données selon
leur similarité dans des clusters. L'inconnu de ce type de problèmes
est le nombre de clusters.

.. contents::
    :local:

"""

###########################
#
# Principe
# --------
#
# On commence par générer un nuage de points artificiel.

from sklearn.datasets import make_blobs
X, Y = make_blobs(n_samples=500, n_features=2, centers=4)

###########################
# On représente ces données.

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.plot(X[:, 0], X[:, 1], '.')

##########################
# On utilise un algorithme très utilisé :
# `KMeans <http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html>`_.

from sklearn.cluster import KMeans
km = KMeans()
km.fit(X)

##############################
# L'optimisation du modèle produit autant de points
# que de clusters.
print(km.cluster_centers_)

##############################
# On dessine le résultat en choisissant une couleur
# différente pour chaque cluster.

cmap = plt.cm.get_cmap("hsv", km.cluster_centers_.shape[0])
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
colors = [cmap(i) for i in km.labels_]
ax.scatter(X[:, 0], X[:, 1], c=colors)

# plt.show()
