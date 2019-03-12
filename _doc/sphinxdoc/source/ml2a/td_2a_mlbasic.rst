
.. _l-td2a-mlbasic:

=======================================
Machine learning - les briques de bases
=======================================

Le machine learning avant les années 2000 se résumait à un problème
d'optimisation. On définit une fonction d'erreur et on détermine le modèle
qui minimise cette erreur. Depuis 2010, le problème d'optimisation
s'est mué en une série de problèmes plutôt bien identifiés et correspondant
à des cas concrets. Classification, régression, ranking... En pratique,
on ne commence plus par modéliser mais plus par trouver le bon assemblage
qui correspondent aux besoins.

.. contents::
    :local:

Statistiques Descriptives
=========================

.. toctree::
    :maxdepth: 1

    td2a_mlbasic_acp_acm_anova
    td2a_mlbasic_intervalles_de_confiance
    td2a_mlbasic_donnees_de_panels

Transformations des données, Embedding
======================================

Construire un `embedding <https://en.wikipedia.org/wiki/Embedding>`_ consiste le plus
souvent à construire une fonction qui convertit un entier, un graphe, un texte en
un vecteur réel de dimension fixe exploitable par un modèle de machine learning.
Cette partie s'intéresse à construire de meilleures variables que celles issues
du problème initiale.

.. toctree::
    :maxdepth: 1

    td2a_mlbasic_projections_reduction_des_dimensions
    td2a_mlbasic_hasard_robustesse
    td2a_mlbasic_variables_categorielles
    td2a_mlbasic_distances
    td2a_mlbasic_clustering
    td2a_mlbasic_detection_anomalies
    td2a_mlbasic_text_embedding
    td2a_mlbasic_embedding_de_donnees_complexes
    td2a_mlbasic_graphe_et_embedding
    td2a_mlbasic_valeurs_manquantes

Machine Learning - Formalisation
================================

.. toctree::
    :maxdepth: 1

    td2a_mlbasic_machine_learning_cours_de_gael_varoquaux    
    td2a_mlbasic_de_la_theorie_a_la_pratique
    td2a_mlbasic_visualisation
    td2a_mlbasic_ranking
    td2a_mlbasic_imbalanced_classification
    td2a_mlbasic_classification_multilabel
    td2a_mlbasic_systeme_de_recommandations
    td2a_mlbasic_reinforcement_learning
    td2a_mlbasic_bandits
    td2a_mlbasic_modeles_bayesiens
    td2a_mlbasic_factorization_machines
    td2a_mlbasic_boosting
