
.. _l-feuille-de-route-2019-2A:

Feuille de route 2019 (2A)
==========================

*en constante élaboration*

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td2a>`

Les cours et séances se déroulent sur 9 séances de 3h
mardi matin. Le cours est divisé en deux pistes
*Stat* et *Eco* qui correspondent aux profils décrits
dans :ref:`l-td2a-notions`. Voici les principaux
thèmes abordés durant le cours :

*Commun data scientist - économiste*

* Pratique des principaux problèmes de machines Learning
  avec scikit-learn (classification, régression,
  clustering, prétraitement)
* Visualisation des données
* Construction d'un module python
* Traitement des données textuelles (NLP, analyse de sentiments...)

*Data scientiste*

* Implémentation de modèles personnalisés avec scikit-learn
* Déploiement de modèles de machine Learning via des API rest
* Problèmes moins fréquents de machine learning :
  apprentissage par renforcement, ranking, recommandation

*Economiste*

* Rappel sur les notebooks,
  les dataframes, pandas, numpy, manipulation de données...
* Cartographie
* Ethique des données
* Webscrapping, API et expressions régulières
* Séries temporelles

Evaluation
++++++++++

* :ref:`l-projinfo2a-plot` - 19 novembre (1/3 de la note finale,
  6/20 pour réaliser le module, 6/20 pour un graphique
  ou un algorithme qui fonctionne, 6/20 pour
  écrire un test unitaire, 2/20 pour fournir un exemple
  d'utilisation du module qui fonctionne)
* :ref:`l-projinfo2a` - rapport 20 décembre, soutenance mi-janvier,
  (2/3 de la note finale)

Séance 1 - 10/9 - amphi - introduction
++++++++++++++++++++++++++++++++++++++

* Précision sur le cours, évaluation, exposés, ressources, TD, amphi,
* `Rappels de mathématiques
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/rappel.html>`_
* :ref:`td2ecorappels1arst`,
  :ref:`mlcmachinelearningproblemsrst`
* Support de cours, ce site,
  `Lectures sur le machine learning
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/index.html>`_,
  github: :epkg:`sdpython`
* `Un exemple simple de régression linéaire
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/2019-01-25_linreg.html>`_
* `Base d'apprentissage et de test
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_knn_split.html>`_
* `Classifications et courbes ROC
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_color_roc.html>`_
* `Validation croisée
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_knn_cross_val.html>`_

**A faire pour la prochaine fois** : exécuter trois notebooks,
:ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`,
:ref:`mlfeaturesmodelrst`

.. _l-seance2-2A-2019:

Séance 2 - 17/9
+++++++++++++++

**DS - TD** : régression quantile - détection d'anomalies

* `Régression quantile
  <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/questions/exams_1A.html>`_
  (correction : :ref:`tdnote20172rst`)
* `Wine Quality Datasets
  <http://archive.ics.uci.edu/ml/datasets/Wine+Quality?ref=datanews.io>`_,
  corréler les erreurs de prédictions de plusieurs modèles
  avec plusieurs détection d'anomalies
* :ref:`td2aenonceclreganomalyrst`
  (:ref:`correction <td2acorrectionclreganomalyrst>`)

**DS - cours**

* Retour sur la classification, notion de frontière comme
  le `ratio de deux probabilités
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/regclass.html#classification>`_
* Cas multi-classe
* Présentation des `réseaux de neurones
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn_1_def.html
  #un-reseau-de-neurones-le-perceptron>`_
* `Overfitting avec les réseaux de neurones
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn_2_reg.html>`_
* Apprentissage méthode à `base de gradient
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn_5_newton.html>`_
* Différence entre le gradient global et le `gradient stochastique
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn_6_apprentissage.html
  #apprentissage-avec-gradient-stochastique>`_
* Méthode ensembliste
* Le cas des random forest pour éviter l'overfitting
* Normalisation L1, L2,
  L1 = `sélection de variables
  <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/notebooks/ml_scikit_learn_simple_correction.html
  ?highlight=ridge#exercice-8-augmenter-le-nombre-de-features-et-regulariser-une-regression-logistique>`_,
  L2 = dilution de la masse des coefficients,
  `Pénalisation L1 L2 <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/l1l2.html>`_
* Retour sur le cas multi-classe avec un nombre de classes grand,
  notion de `imbalanced dataset
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_multiclass.html>`_

**Eco - Cours** : rappels :epkg:`pandas` :epkg:`numpy`
:epkg:`matplotlib` début :epkg:`scikit-learn`

* Rappels sur le langage :epkg:`python`,
  `Cheat sheet: Python <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_resume/python_sheet.html>`_,
  variable, listes, dictionnaires, boucles, fonctions,
  :ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`,
  :ref:`mlfeaturesmodelrst`
* Rappels sur :epkg:`pandas`, notion de table, lecture, écriture de fichiers
  texte, :epkg:`Excel`, ajout de colonne, opérations entre
  colonne, *apply*, opérations standard (sort, filter, group by, join),
  :epkg:`numpy`, opérations standard, calcul matriciel, différences
  avec un dataframe,
  :ref:`2018-09-18rappelspythonrst`,
  :ref:`2018-09-18rappelspythonpandasmatplotlibrst`
* :ref:`td2ecorappels1arst`
* :ref:`td2acenoncesession2arst`
* :ref:`td2acorrectionsession2arst`

Séance 3 - 24/9
+++++++++++++++

**DS - TD**

Voir :ref:`l-seance2-2A-2019`.

**DS - cours**

Voir :ref:`l-seance2-2A-2019`.

**Eco**

* :ref:`td2avisualisationrst`
* :ref:`td2aecoexercicesdemanipulationdedonneesrst`
* :ref:`td2aecoexercicesdemanipulationdedonneescorrectionarst`
* :ref:`td2aecoexercicesdemanipulationdedonneescorrectionbrst`
* :ref:`td2aecoexercicesdemanipulationdedonneescorrectioncrst`

Séance 4 - 1/10
+++++++++++++++

**DS - TD**

* :ref:`td2atreeselectionenoncerst`,
  :ref:`correction <td2atreeselectioncorrectionrst>`
* :ref:`td2apipelinetreeselectionenoncerst`,
  :ref:`correction <td2apipelinetreeselectioncorrectionrst>`

**DS - cours**

* `API de scikit-learn et implémentation de modèles customisés
  <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2019/sklearnapi201910.html>`_
* :class:`LassoRandomForestRegressor
  <ensae_teaching_cs.ml.lasso_random_forest_regressor.LassoRandomForestRegressor>`
* Prétraitements des données, réductions de dimensions,
  normalisation, transformation du texte en variable
  numériques

**Eco**

* :ref:`td2aeco5dTravaillerdutextelesexpressionsregulieresrst`
* :ref:`2018-10-02scrapingrecupererimagesrst`
* :ref:`TD2AEcoWebScrapingrst`

Séance 5 - 8/10
+++++++++++++++

**DS**

* Reinforcement learning avec Jean-Baptiste Rémy (amphi à 8h30, TD à 10h15 en amphi),
  notebooks : `Reinforcement_Toys <https://github.com/JbRemy/Reinforcement_Toys>`_

**Eco**

* :ref:`TD2AecolesAPIrst`
* :ref:`TD2AecoAPISNCFrst`
* :ref:`TD2AecoAPISNCFcorrigerst`

Séance 6 - 15/10
++++++++++++++++

Deux notebooks ont été ajoutés pour le projet :ref:`l-projinfo2a-plot`,
ils présentent les deux jeux de données disponibles pour cet exercice
si le graphe est choisi. Si c'est l'algorithme, il est possible de
s'inspirer de `lasso_random_forest_regressor.py
<https://github.com/sdpython/ensae_teaching_cs/blob/master/src/ensae_teaching_cs/ml/lasso_random_forest_regressor.py>`_
qui implémente la réduction d'une random forest à l'aide
d'une régression Lasso.

**DS - TD**

* :ref:`td2atreeselectionenoncerst`,
  :ref:`correction <td2atreeselectioncorrectionrst>`
* :ref:`td2apipelinetreeselectionenoncerst`,
  :ref:`correction <td2apipelinetreeselectioncorrectionrst>`

**DS - cours**

* `API de scikit-learn et implémentation de modèles customisés
  <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2019/sklearnapi201910.html>`_
* :class:`LassoRandomForestRegressor
  <ensae_teaching_cs.ml.lasso_random_forest_regressor.LassoRandomForestRegressor>`
* Prétraitements des données, réductions de dimensions,
  normalisation, transformation du texte en variable
  numériques

**Eco**

* :ref:`td2acenoncesession3Arst`
* :ref:`td2aecoregressionslineairesrst`
* `Maximum Likelihood Estimation
  <https://github.com/QuantEcon/quantecon-notebooks-python/blob/master/mle.ipynb>`_
  du site `QuantEcon <https://quantecon.org/>`_
* :ref:`mltimeseriesbaserst`
* :ref:`td2aenonceclreganomalyrst`

Séance 7 - 22/10
++++++++++++++++

**DS - cours**

* Valeurs manquantes
* Système de recommandations
* Séries temporelles
* Notions de graphes, matrice d'adjacence
  :epkg:`sklearn:cluster:SpectralClustering`,
  énigmes algorithmiques
  (placements de tables, énigme des dés,
  :ref:`td2acenoncesession6Arst` - :ref:`corretion <td2acorrectionsession6Arst>`),
  :ref:`td2acenoncesession6Brst` - :ref:`correction <td2acorrectionsession6Brst>`,
  :ref:`mlrueparisparcoursrst`, :ref:`exposerwrrecommandationrst`,
  :ref:`exerciceplusgrandesommerst`)

**DS - TD**

* :ref:`mllassorfgridsearchenoncerst`
  (:ref:`correction <mllassorfgridsearchcorrectionrst>`)
* :ref:`mlbimbalancedrst`

**Eco**

* :ref:`td2aecoNLPtfidfngramsLDAword2vecsurdesextraitslitterairesrst`
* :ref:`td2aTD5TraitementautomatiquedeslanguesenPythonrst`
* `Classification de phrases avec word2vec
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/text_sentiment_wordvec.html>`_
* :ref:`td2asomenlprst`
* :ref:`td2asentimentanalysisrst`

Séance 8 - 5/11
+++++++++++++++

**DS - cours**

* Valeurs manquantes
* Système de recommandations
* Séries temporelles
* Notions de graphes, matrice d'adjacence
  :epkg:`sklearn:cluster:SpectralClustering`,
  énigmes algorithmiques
  (placements de tables, énigme des dés,
  :ref:`td2acenoncesession6Arst` - :ref:`corretion <td2acorrectionsession6Arst>`),
  :ref:`td2acenoncesession6Brst` - :ref:`correction <td2acorrectionsession6Brst>`,
  :ref:`mlrueparisparcoursrst`, :ref:`exposerwrrecommandationrst`,
  :ref:`exerciceplusgrandesommerst`)
* **Questions pour le projet de cartes**

**DS - TD**

* :ref:`mllassorfgridsearchenoncerst`
  (:ref:`correction <mllassorfgridsearchcorrectionrst>`)
* :ref:`mlbimbalancedrst`
* **Questions pour le projet de cartes**

**Eco**

* :ref:`td2aecoNLPtfidfngramsLDAword2vecsurdesextraitslitterairesrst`
* :ref:`td2aTD5TraitementautomatiquedeslanguesenPythonrst`
* `Classification de phrases avec word2vec
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/text_sentiment_wordvec.html>`_
* :ref:`td2asomenlprst`
* :ref:`td2asentimentanalysisrst`
* **Questions pour le projet de cartes**

Séance 9 - 12/10
++++++++++++++++

Pour les groupes, travail sur le projet de module
python.

**DS - cours**

* :ref:`l-ml2a-autolearning`
* :ref:`l-ml2a-mlethical`
* :ref:`l-td2a-ml-crypted`
* `Petit voyage au pays des assurances, un jeu de données hypothétique
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/histoires/assurance.html>`_

Prérequis
+++++++++

* *Voix stat* : maîtrise du langage :epkg:`Python`,
  connaissance des modules :epkg:`pandas`, :epkg:`numpy`,
  :epkg:`matplotlib`, voir `quelques rappels
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/rappel.html>`_
* *Voix éco* : maîtrise du langage :epkg:`Python`, :ref:`td2ecorappels1arst`

Autres contenus
+++++++++++++++

* Apprentissage par renforcement,
  `Reinforcement_Toys <https://github.com/JbRemy/Reinforcement_Toys>`_,
  de Jean-Baptiste Rémy
* `ensae-python-2019 <https://github.com/sally14/ensae-python-2019>`_,
  de Solamé Do
* `Données de l'IREP et Devoir
  <https://nbviewer.jupyter.org/github/gabsens/Python-for-Data-Scientists-ENSAE/
  blob/master/Devoir/IREP%20et%20devoir.ipynb>`_ de Gabriel Romon

Intervenants
++++++++++++

`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_,
Anne Muller,
Eliot Barril,
Mayeul Picard,
Salomé Do,
Gilles Cornec,
Gabriel Romon,
Jean-Baptiste Rémy
