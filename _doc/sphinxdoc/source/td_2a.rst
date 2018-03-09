
.. _l-td2a:

==========================================
Python pour un Data Scientist / Economiste
==========================================

`ENSAE - OMI2F2 <http://www.ensae.fr/ensae/fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/2me-anne-formationsdiplome-95.html?id=101352>`_

Ce cours s'étale sur 24 heures de cours/TD.
Les outils proposés sont en langage :epkg:`Python`. Ils sont tous :epkg:`open source`,
pour la plupart disponibles sur :epkg:`GitHub` et en développement actif.
:epkg:`Python` est devenu le premier langage pour les scientifiques
et comme c'est un langage générique, il est possible de gérer
l'ensemble des traitements appliqués aux données, depuis
le traitements des sources de données jusqu'à leur visualisation
sans changer de langage.
Le cours est prévu pour des profils plutôt statistiques |pystatpng|
ou plutôt économiques |pyecopng|. Ces images reviendront pour indiquer
si les contenus s'adressent plutôt aux uns ou aux autres.

* :ref:`l-feuille-de-route-2017-2A`
* :ref:`l-projinfo2a`
* :ref:`l-feuille-de-route-2018-2A` (en préparation)

Le terme *cheat sheet* est un mot-clé plutôt efficace sur Internet pour
retrouver les bout de codes les plus fréquents. Cette page regroupe des
*cheat sheets* sur beaucoup de sujet évoqués ci-dessous :
`Essential Cheat Sheets for Machine Learning and Deep Learning Engineers <https://startupsventurecapital.com/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5>`_.
Le site :epkg:`Kaggle` recense de nombreuses compétitions de machine learning
qui permettent de s'exercer ou de se mesurer à d'autres data scientists.
Quelques compétitions ont aussi été créées pour ce cours :
:ref:`l-competition`.
Le cours est organisé sous forme de thèmes,
tous associés à un problème de données et
ou de machine learning. Les thèmes sont de difficultés croissantes
et sont abordés invariablement par,
des exercices sous la forme de notebooks (énoncé / correction),
des articles, des modules connus.

**Thèmes**

.. contents::
    :local:

.. |pyecopng| image:: _static/pyeco.png
            :height: 20
            :alt: Economie
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: _static/pystat.png
            :height: 20
            :alt: Statistique
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Agilité avec les données
========================

Il est indispensable de savoir manipuler les données
avant de pouvoir faire du machine learning. Filtrer,
fusionner, concaténer, il faut savoir faire cela vite
pour passer plus de temps sur les problèmes intéressants.

.. toctree::
    :maxdepth: 3

    ml2a/td_2a_manip

Machine Learning - les briques de bases
=======================================

Un problème de données est rarement résolu avec un seul modèle,
un seul algorithme et plus souvent un assemblage.
La première étape consiste à analyser un problème
concret à l'aide d'une grille de problèmes formalisés.
C'est cette grille qui est parcourue dans les paragraphes
svuiants.

.. toctree::
    :maxdepth: 3

    ml2a/td_2a_mlbasic

Machine learning - extensions
=============================

Les données ne sont pas toujours organisés sous la forme
d'une table de données où il s'agit de prédire *Y*
en fonction de *X*. Il faut parfois prendre en compte
une dépendance temporelle ou spatiale. Cette section
étend la grille précédente et proposent des modèles
parfois récents.

.. toctree::
    :maxdepth: 3

    ml2a/td_2a_mlplus

Algorithmes, Optimisation, Programmation
========================================

Plus les données sont volumineuses, plus les contraintes sont
nombreuses, plus il faut se montrer inventif. Ecrire un code efficace
est souvent utile et parfois impératif simplement
pour obtenir un résultat. Néanmoins, il arrive régulièrement
que le premier besoin soit celui de collecter des données
qui ne sont pas encore disponibles.

.. toctree::
    :maxdepth: 3

    ml2a/td_2a_talgo

Bibliographie
=============

La plupart des articles sont référencés dans la section du thème
auquel ils sont reliés. Les suivants sont en quelque sorte
des inclassables.

.. toctree::
    :maxdepth: 2

    ml2a/td_2a_biblio

A propos du cours
=================

Ce cours a commencé en 2014 et n'a cessé de s'enrichir.
Il est animé par `Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_ (ENSAE 1999)
et Anne Muller (ENSAE 2012).
Le cours qui a pour objectif de vous présenter les
notions suivantes.

.. toctree::
    :maxdepth: 2

    ml2a/td_2a_notions

**Auteurs et Contributeurs**

Ce cours a bénéficié de nombreuses contributions dont les auteurs sont :
Xavier Dupré, Anne Muller (API, scrapping, tutoriels, ...),
Elodie Royant (API, scrapping, tutoriels, ...),
Matthieu Bizien (deep learning),
Nicolas Rousset (itérateurs),
Jérémie Jakubowicz (puzzle algorithmique),
Gilles Drigout (streaming),
Gaël Varoquaux (machine learning avec scikit-learn)
et bien sûr les étudiants de l':epkg:`ENSAE`.
Feuilles de route et compétitions passées :

.. toctree::
    :maxdepth: 2

    questions/route_2A_2016
    questions/route_2A_2017
    questions/route_2A_2018
    questions/competition_2A
