
.. _l-feuille-de-route-2018-2A:

Feuille de route 2018 (2A)
==========================
*en préparation*

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td2a>`

Plan
++++

Les cours et séances se déroulent sur 8 séances de 3h
mardi matin. Le cours est divisé en deux pistes
*Stat* et *Eco* qui correspondent aux profils décrits
dans :ref:`l-td2a-notions`. Un compte **slack**
`python-ensae-2a.slack.com <https://python-ensae-2a.slack.com/>`_
a été créé pour faciliter les échanges, annonces et questions.
Une compétition sera ouverte le premier jour et
fermée à la dernière session où les résultas et les idées seront
discutées.

+---------------------------+---------------------------------------------------+-----------------------------------------------+
| Séance                    | Voie stat                                         | Voie éco                                      |
+===========================+===================================================+===============================================+
| 11/9 (1) *amphi*          | * Présentation du cours, évaluation                                                               |
|                           | * Rappels sur le langage :epkg:`Python`, les modules les plus utilisés                            |
| :ref:`l-route2018-stat1`  | * Classification binaire, régression logistique, régression linéaire                              |
|                           | * Apprentissage test, validation croisée                                                          |
|                           | * **A faire** : exécuter trois notebooks                                                          |
|                           |   :ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`, :ref:`mlfeaturesmodelrst`   |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 18/9 (2) *TD*             | Rappels et exercices sur la manipulation des      | Rappels et exercices sur le langage           |
|                           | données avec :epkg:`pandas`, :epkg:`numpy`,       | :epkg:`Python`, manipulation des données avec |
| :ref:`l-route2018-stat2`, | :epkg:`matplotlib`, :epkg:`scikit-learn`          | :epkg:`pandas`                                |
| :ref:`l-route2018-eco2`   |                                                   |                                               |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 25/9 (3) *TD*             | Notion, de prédicteur, transformeurs, pipelines,  | Suite et fin des exercices pandas et          |
|                           | application aux variables catégorielles,          | représentations graphiques variées, fin des   |
| :ref:`l-route2018-stat3`, | introduction de :epkg:`statsmodels`,              | exercices sur :epkg:`pandas`, :epkg:`numpy`,  |
| :ref:`l-route2018-eco3`,  | :epkg:`xgboost`, stacking                         | visualisation avec :epkg:`matplotlib`,        |
| **deux exposés**          |                                                   | cartographie                                  |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 2/10 (5) *TD*             | Ranking, Détection d'anomalies, clustering,       | Econométrie, analyse de données et premiers   |
|                           | valeurs manquantes, imbalanced classification     | pas avec :epkg:`scikit-learn`, (ACP,          |
| :ref:`l-route2018-stat4`, |                                                   | Regréssion linéaire, Logit, séries            |
| :ref:`l-route2018-eco4`   |                                                   | temporelles)                                  |
| **deux exposés**          |                                                   |                                               |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 9/10 (5) *TD*             | Machine learning crypté, hyperparamètres,         | Travailler le texte, de la récupération à     |
|                           | recommandation, séries temporelles                | l'exploitation (1/2), Expressions régulière,  |
| :ref:`l-route2018-stat5`, |                                                   | web scrapping                                 |
| :ref:`l-route2018-eco5`,  |                                                   |                                               |
| **deux exposés**          |                                                   |                                               |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 16/10 (6) *amphi*         | * Propriétés des modèles mathématiques, modèles linéaires, modèles ensemblistes, modèles          |
|                           |   dérivables, feature importance (*Xavier Dupré*)                                                 |
| :ref:`l-route2018-stat6`, | * Interprétation des modèles de machine learning (*Gaël Varoquaux*)                               |
| **deux exposés**          |                                                                                                   |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 23/10 (7) *amphi*         | * notion de deep learning sans en faire, application au texte, et aux images,                     |
|                           |   transfer learning, exemples avec un moteur de recherche d'images (*Xavier Dupré*)               |
| :ref:`l-route2018-stat7`, | * *Ethique et algorithmes* avec (*Frédéric Bardolle*)                                             |
| **deux exposés**          |                                                                                                   |
+---------------------------+---------------------------------------------------+-----------------------------------------------+
| 6/11 (8) *TD*             | Notion d'algorithmes, écrire du code efficace en  | Travailler le texte, de la récupération à     |
|                           | :epkg:`Python`, avec :epkg:`pandas`,              | l'exploitation (2/2), Exercice de             |
| :ref:`l-route2018-stat8`, | :epkg:`numpy`, discussion sur les projets         | webscraping, API, NLP                         |
| :ref:`l-route2018-eco8`,  |                                                   |                                               |
| **deux exposés**          |                                                   |                                               |
+---------------------------+---------------------------------------------------+-----------------------------------------------+

Prérequis
+++++++++

* *Voix stat* : maîtrise du langage :epkg:`Python`, connaissance des modules :epkg:`pandas`,
  :epkg:`numpy`, voir
  `quelques rappels <http://www.xavierdupre.fr/app/papierstat/helpsphinx/rappel.html>`_
* *Voix éco* : maîtrise du langage :epkg:`Python`, :ref:`td2ecorappels1arst`

Intervenants
++++++++++++

`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_,
Anne Muller, Elodie Royant,
Antoine Ly, Eliot Barril,
Frédéric Bardolle,
`Gaël Varoquaux <http://gael-varoquaux.info/>`_.

Notes
+++++

Liens, notebooks prévus pour les séances pratiques.

.. contents::
    :local:

.. _l-route2018-stat1:

Séance 1
^^^^^^^^

* Précision sur le cours, évaluation, exposés, ressources, TD, amphi,
* notebook, :epkg:`python`, prérequis
* `Rappels de mathématiques <http://www.xavierdupre.fr/app/papierstat/helpsphinx/rappel.html>`_
* :ref:`td2ecorappels1arst`
* :ref:`mlcmachinelearningproblemsrst`
* Lectures `Lectures sur le machine learning <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/index.html>`_
* principe de la prédiction
* plus proches voisins
* base d'apprentissage et de tests, découpage stratifié
* hyperparamètres
* définition de la régression et de la classification
* score et ROC
* **A faire pour la prochaine fois** : exécuter trois notebooks,
  :ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`,
  :ref:`mlfeaturesmodelrst`

.. _l-route2018-stat2:

Séance 2 - stat
^^^^^^^^^^^^^^^

* :ref:`td2acenoncesession2arst`
* :ref:`td2acorrectionsession2arst`
* :ref:`td2acenoncesession1rst`
* :ref:`td2acorrectionsession1rst`

**A faire** : exécuter deux notebooks,
:ref:`structuresdonneesconversionrst`, :ref:`mlfeaturesmodelrst`.

.. _l-route2018-eco2:

Séance 2 - éco
^^^^^^^^^^^^^^

* :ref:`td2ecorappels1arst`
* :ref:`td2acenoncesession2arst`
* :ref:`td2acorrectionsession2arst`

.. _l-route2018-stat3:

Séance 3 - stat
^^^^^^^^^^^^^^^

* `Comparison de prédicteurs <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_reg.html>`_
* :epkg:`XGBoost`
* `transformer les catégories <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_color_linear.html>`_
* `stacking <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_multi_stacking.html>`_
* `Régression polynômiale et pileline <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_reg_poly.html>`_

.. _l-route2018-eco3:

Séance 3 - éco
^^^^^^^^^^^^^^

* `Tracer une carte en Python <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/enedis_cartes.html>`_

.. _l-route2018-stat4:

Séance 4 - stat
^^^^^^^^^^^^^^^

* :ref:`l-mlbasic-anomaly`
* :ref:`l-ml2a-ranking`
* :ref:`l-imbalanced-classification`
* :ref:`l-td2a-missing-values`
* :ref:`td2aclusteringrst`, :ref:`td2aclusteringcorrectionrst`

.. _l-route2018-eco4:

Séance 4 - éco
^^^^^^^^^^^^^^

Beaucoup de choses pour ce TD, voici ce que vous devez absolument
avoir lu pendant les 3 heures.

* Regardez différentes options disponibles pour faire les graphiques et
  passez un peu de temps sur l'exemple :ref:`td2avisualisationrst`
* Réaliser des modèles économétriques avec les outils :epkg:`Python` :
    * :ref:`ACP <td2acenoncesession3arst>` (s'arrêter à l'exercice 1)
    * :ref:`Régression linéaire <td2aecoregressionslineairesrst>`
    * :ref:`Logit <td2aecocompetitionmodeleslogistiquesrst>`
* :ref:`td2atimeseriesrst`
	
* SQL : lire attentivement le notebook :ref:`td2aecosqlrst`

*Exercice à réaliser*

* Exercice 2 de cette page :ref:`td2acenoncesession3arst`

*Objectifs*

* avoir compris comment réaliser les différentes classes de modèles
  présentées (régression linéaire, ACP , logit)
* avoir bien compris les notions de SQL utilisées
  dans le début de l'exercice
* réaliser la regression demandée avec les deux
  packages proposés (:epkg:`scikit-learn` et :epkg:`statsmodels`)

Pour aller plus loin :

* Panoplie de graphes et cartes : :ref:`td1acenoncesession12rst`
* ROC pour un modèle logit :epkg:`antiseches_ml_basic_plot_binary_classification`
* Les exercices du notebook SQL : :ref:`td2aecosqlrst` (question 1)
* Manipuler les données et modéliser les incidents dans le transport aérien
  :ref:`td2acenoncesession5rst`

.. _l-route2018-stat5:

Séance 5 - stat
^^^^^^^^^^^^^^^

* :ref:`l-td2a-ml-crypted`
* :ref:`l-td2a-hyperparametre`
* :ref:`mltimeseriesbaserst`
* `Liens entre factorisation de matrices, ACP, k-means <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/missing_values_mf.html>`_
* :ref:`l-td2a-sys-recommandation`

.. _l-route2018-eco5:

Séance 5 - éco
^^^^^^^^^^^^^^

.. _l-route2018-stat6:

Séance 6
^^^^^^^^

* `Gradient et méthodes ensemblistes <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/gradienttree.html>`_
* :ref:`mlcccmachinelearninginterpretabiliterst`
* :ref:`l-ml2a-selvar`
* :ref:`mlccmachinelearningproblems2rst`
* `Régression logistique, diagramme de Voronoï, k-Means <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/lr_voronoi.html>`_
* :ref:`mlcccmachinelearninginterpretabiliterst`

.. _l-route2018-stat7:

Séance 7
^^^^^^^^

* `Réseaux de neurones <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn.html>`_
* :ref:`l-nolabel`
* `Galleries de problèmes résolus ou presque <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/dl_resolus.html>`_
* `Transfer Learning <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/deep_transfer_learning.html>`_
* `Search images with deep learning <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/notebooks/search_images.html>`_

.. _l-route2018-stat8:

Séance 8 - stat
^^^^^^^^^^^^^^^

* :ref:`knnhighdimensionrst`, :ref:`knnhighdimensioncorrectionrst`
* :ref:`BJKSTrst`
* :ref:`td2acenoncesession6Arst`, :ref:`td2acorrectionsession6Arst`
* :ref:`td2acenoncesession6Brst`, :ref:`td2acorrectionsession6Brst`

.. _l-route2018-eco8:

Séance 8 - éco
^^^^^^^^^^^^^^

* :ref:`td2amltextfeaturesrst`
* :ref:`td2asomenlprst`
