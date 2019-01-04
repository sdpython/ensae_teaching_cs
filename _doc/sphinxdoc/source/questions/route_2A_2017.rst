
.. _l-feuille-de-route-2017-2A:

Feuille de route 2017 (2A)
==========================

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

.. list-table::
    :widths: 2 5 5
    :header-rows: 1

    * - Séance
      - Stat
      - Eco
    * - 19/9 (1)
      - Introduction du cours,
        présentation de la compétition,
        rappel pandas, numpy, matplotlib,
        SQL, Cartes, sérialisation
        :ref:`l-route2017-stat1`
      - Introduction du cours,
        présentation de la compétition,
        pandas, numpy, matplotlib, manipulation de données,
        :ref:`l-route2017-eco1`
    * - 26/9 (2)
      - Algorithmes, itérateur,
        notion de pipelines, mise en production de modèles, test unitaires,
        régression, logging, dask, parallélisation, :ref:`l-route2017-stat2`
      - SQL, Cartes,
        Rappel des méthodes linéaires (régression linéaire, logistique, ACP, ...),
        :ref:`l-route2017-eco2`
    * - 3/10 (3)
      - Python et C++, sérialisation, profiling
        cours de Gaël Varoquaux, :ref:`l-route2017-stat3`
      - pandas, vélib
        cours de Gaël Varoquaux, :ref:`l-route2017-eco3`
    * -
      - **Après 3 séances, vous devriez connaître et savoir utiliser**
        :epkg:`numpy`, :epkg:`pandas`, :epkg:`matplotlib`.
      - **Après 3 séances, vous devriez connaître et savoir utiliser**
        :epkg:`numpy`, :epkg:`pandas`, :epkg:`matplotlib`.
    * - 10/10 (4)
      - Revue de problèmes de machine learning formalisés, cross-validation
        Données textuelles, variables catégorielles, word embedding
        :ref:`l-route2017-stat4`
      - Texte et expression régulière,
        Revue de problèmes de machine learning formalisés,
        Données textuelles, variables catégorielles,
        :ref:`l-route2017-eco4`
    * - 17/10 (5)
      - Machine learning données cryptées, hyperparamètres,
        données textuelles
        :ref:`l-route2017-stat5`
      - Web scrapping, API, :ref:`l-route2017-eco5`
    * - 24/10 (6)
      - Deep learning, Keras, Torch, Transfer Learning, :ref:`l-route2017-stat6`
      - NLP, :ref:`l-route2017-eco6`
    * - 7/11 (7)
      - Série temporelles,
        éthique dans les modèles,
        :ref:`l-route2017-stat7`
      - Traitement du langage, LDA, tf-idf,
        expression régulière, :ref:`l-route2017-eco7`
    * - 14/11 (8)
      - Algorithme de streaming, Imbalanced datasets
        Revue de compétition Kaggle, présentation des projets,
        premiers suivis de projets,
        :ref:`l-route2017-stat8`
      - Premiers suivis de projets,
        Revue de compétition Kaggle,
        présentation des projets,
        :ref:`l-route2017-eco8`

Intervenants
++++++++++++

`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_,
Anne Muller, Elodie Royant, Antoine Thabault,
Antoine Ly, Benjamin Donnot, Eliot Barril,
Gaël Varoquaux.

.. _l-remarque-2A-2017-2018:

Retour sur les projets
++++++++++++++++++++++

Le cours est évalué par un projet informatique
:ref:`l-projinfo2a`. Voici quelques retours sur les projets
de cette année. Le barême choisi se résume ainsi :

* *8* : le projet est mauvais,
* *12* : le projet s'est arrête à la comparaison de modèles de
  machine learning,
* *16* : le projet contient une idée originale,
  une analyse intéressantes des résultats,
* *20* : les auteurs ont construit un raisonnement
  qui a abouti à un fait intéressant sur le jeu de données
  de départ.

Beaucoup de projets se sont conclus par un graphique comparant
les performances de plusieurs modèles de machine learning sur une
problématique précise, extraite
d'`UCI <https://archive.ics.uci.edu/ml/datasets.html>`_,
:epkg:`Kaggle` ou d'un autre site. Les enseignements
qu'on peut en tirer sont assez pauvres si le projet s'arrête là.
Il n'y a rien de répliquable à d'autres projets (méthodologie),
ni rien qu'on puisse vraiment apprendre des données (domaine).
Les premiers résultats intéressants viennent souvent
d'une analyse d'erreurs qui consiste à comprendre pourquoi le modèle
s'est trompé sur tel ou tel exemple avec un haut score de confiance.

Notes
+++++

Liens, notebooks prévus pour les séances pratiques.

.. contents::
    :local:

.. _l-route2017-eco1:

Séance 1 Eco
^^^^^^^^^^^^

* Rappels sur des bases du langage :epkg:`Python` : :ref:`td2ecorappels1arst`
* Manipulation de fichiers : :ref:`td1acenoncesession4rst`
* Manipulation des données :
    * :ref:`td2acenoncesession2arst`
    * :ref:`td2acorrectionsession2arst`
    * :ref:`td2acenoncesession1rst`
    * :ref:`td2acorrectionsession1rst`

*Notebooks*

* `try.jupyter.org <https://try.jupyter.org/>`_
* `Notebook <http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb>`_

*Compléments*

* Rappels sur des bases du langage :epkg:`Python` :
    * :ref:`td1acenoncesession1rst`
    * :ref:`td1acenoncesession2rst`
    * :ref:`td1acenoncesession3rst`
    * :ref:`codelistetuplerst`
    * :ref:`structuresdonneesconversionrst`
* Notebook : :ref:`td2acenoncesession2crst`
* Compétition : :ref:`solution2016creditclementrst`

.. _l-route2017-stat1:

Séance 1 Stat
^^^^^^^^^^^^^

* Manipulation des données :
    * :ref:`td2acenoncesession1rst`
    * :ref:`td2acorrectionsession1rst`
    * :ref:`td2acenoncesession2arst`
    * :ref:`td2acorrectionsession2arst`
* Graphes :
    * :ref:`td2avisualisationrst`
    * `10 plotting libraries <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_
* Cartes :
    * :ref:`td1acenoncesession12carterst`
    * :ref:`td1acorrectionsession12rst`
* SQL :
    * :ref:`l-sql-principe-base-2a`
    * :ref:`td2aecosqlrst`
    * :ref:`td2aecosqlcorrectionrst`
* Sérialisation : :ref:`td2acenoncesession2erst`

.. _l-route2017-eco2:

Séance 2 Eco
^^^^^^^^^^^^

Beaucoup de choses pour ce TD, voici ce que vous devez absolument
avoir lu pendant les 3 heures.

* Regardez différentes options disponibles pour faire les graphiques et
  passez un peu de temps sur l'exemple :ref:`td2avisualisationrst`
* Réaliser des modèles économétriques avec les outils :epkg:`Python` :
    * :ref:`ACP <td2acenoncesession3arst>` (s'arrêter à l'exercice 1)
    * :ref:`Régression linéaire <td2aecoregressionslineairesrst>`
    * :ref:`Logit <td2aecocompetitionmodeleslogistiquesrst>`
	
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

* Panoplie de graphes et cartes : :ref:`td1acenoncesession12carterst`
* ROC pour un modèle logit :epkg:`antiseches_ml_basic_plot_binary_classification`
* Les exercices du notebook SQL : :ref:`td2aecosqlrst` (question 1)
* Manipuler les données et modéliser les incidents dans le transport aérien
  :ref:`td2acenoncesession5rst`

.. _l-route2017-stat2:

Séance 2 Stat
^^^^^^^^^^^^^

* Itérateur, parallélisation :
    * :ref:`td2acenoncesession5donneesnonstructureesetprogrammationfonctionnellerst`
    * :ref:`seance5daskrst`
    * :ref:`td2acorrectionsession5donneesnonstructureesetprogrammationfonctionnellecorrigerst`
    * :ref:`pandasiteratorrst`
    * :ref:`pandasiteratorcorrectionrst`
* Algorithme, ACP :
    * :ref:`knnhighdimensionrst`
    * :ref:`knnhighdimensioncorrectionrst`
* Pratique logicielle :
    * :ref:`td1aunittestcirst`
    * :ref:`td1aunittestcicorrectionrst`

.. _l-route2017-eco3:

Séance 3 Eco
^^^^^^^^^^^^

* Manipulation de données
    * :ref:`td2aecoexercicesdemanipulationdedonneesrst`
    * :ref:`td2aecoexercicesdemanipulationdedonneescorrectionarst`
    * :ref:`td2aecoexercicesdemanipulationdedonneescorrectionbrst`
    * :ref:`td2aecoexercicesdemanipulationdedonneescorrectioncrst`
* Machine Learning (Gaël Varoquaux)
    * `scikit-learn: machine learning in Python <http://gael-varoquaux.info/scipy-lecture-notes/packages/scikit-learn/index.html>`_
      (:ref:`copie sur ce site <l-sklearn-ensae-course-2a>`)

.. _l-route2017-stat3:

Séance 3 Stat
^^^^^^^^^^^^^

* C/C++ avec Python :
    * :ref:`cffilinearregressionrst`
    * :ref:`td1acythoneditrst`
    * :ref:`td1acythoneditcorrectionrst`
* Sérialisation
    * :ref:`td2acenoncesession2erst`
    * :ref:`td2acorrectionsession2erst`
* Profiling
    * `profiling <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/completion_profiling.html>`_
* Machine Learning (Gaël Varoquaux)
    * `scikit-learn: machine learning in Python <http://gael-varoquaux.info/scipy-lecture-notes/packages/scikit-learn/index.html>`_,
      (:ref:`copie sur ce site <l-sklearn-ensae-course-2a>`)

.. _l-route2017-eco4:

Séance 4 Eco
^^^^^^^^^^^^

* webscrapping
    * :ref:`TD2AEcoWebScrapingrst`
* version alternatives des notebooks
    * `GitHub/ensae <https://github.com/Atheane/ensae>`_
    * :ref:`td2aecoAPIpocketetWebscrapingrst`
    * :ref:`td2AecoAPIpocketetWebscrapingcorrectionrst`
* texte et expression régulière
    * :ref:`td2aTD5TraitementautomatiquedeslanguesenPythonrst`

.. _l-route2017-stat4:

Séance 4 Maths
^^^^^^^^^^^^^^

* word embedding
    * :ref:`td2asomenlprst`
* machine learning classique
    * :ref:`l-machine-learning-tips`
    * :ref:`td2amltextfeaturesrst`
* clustering
    * `Découvrir les habitudes des cyclistes à Chicago <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/challenges/city_bike.html>`_

.. _l-route2017-eco5:

Séance 5 Eco
^^^^^^^^^^^^

* webscrapping
    * :ref:`TD2AEcoWebScrapingrst`
* texte et expression régulière
    * :ref:`td2aTD5TraitementautomatiquedeslanguesenPythonrst`
    * :ref:`td2aeco5dTravaillerdutextelesexpressionsregulieresrst`
    * :ref:`td2aeco5dTravaillerdutextelesexpressionsregulierescorrectionrst`

.. _l-route2017-stat5:

Séance 5 Maths
^^^^^^^^^^^^^^

* machine learning classique
    * :ref:`td2amltextfeaturesrst`
    * :ref:`td2amltextfeaturescorrectionrst`
* Courbe ROC
    * :epkg:`ml_basic_plot_roc`
* machine learning crypté
    * :ref:`mlcrypteddatarst`
    * :ref:`mlcrypteddatacorrectionrst`
* Grid Search
    * :epkg:`ml_basic_plot_grid_search`

.. _l-route2017-eco6:

Séance 6 Eco
^^^^^^^^^^^^

* NLP, scrapping
    * :ref:`td2aNLPpocketrst`
    * :ref:`td2aNLPpocketcorrectionrst`

.. _l-route2017-stat6:

Séance 6 Maths
^^^^^^^^^^^^^^

* deep learning :
  `Notebook, deep learning avec pytorch <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/index.html>`_,
  `Transfer Learning <https://github.com/sdpython/2017_deeplearning_demo/blob/master/Fine_Tuning_Deep_CNNs_with_GPU_rendered.ipynb>`_ (Olivier Grisel)
* deep learning : présentations
    * `Introduction au Deep Learning <https://github.com/sdpython/ensae_teaching_cs/blob/master/_doc/sphinxdoc/source/specials/DEEP%20LEARNING%20FOR%20ENSAE.pdf>`_
    * :ref:`l-nolabel`
    * `Deep Learning 2017 <http://www.xavierdupre.fr/exposes/deeplearning/>`_ (avec Olivier Grisel)

*Lectures*

* :ref:`Cours de deep learning appliqués au NLP <blog-stanford-nlp-deep>`

.. _l-route2017-eco7:

Séance 7 Eco
^^^^^^^^^^^^

* TF-IDF, LDA, expressions régulières
    * :ref:`td2aSeance7Analysedetextesrst`
    * :ref:`td2aSeance7Analysedetextescorrectionrst`

.. _l-route2017-stat7:

Séance 7 Maths
^^^^^^^^^^^^^^

* séries temporelles
    * :ref:`mltimeseriesbaserst`
    * `Séries temporelles et map reduce <http://www.xavierdupre.fr/app/sparkouille/helpsphinx/notebooks/map_reduce_timeseries.html>`_
    * :ref:`td2atimeseriesrst`
    * :ref:`td2atimeseriescorrectionrst`
* Machine Learning éthique
    * :ref:`td2aethicsrst`
    * :ref:`td2aethicscorrectionrst`

.. _l-route2017-eco8:

.. _l-route2017-stat8:

Séance 8
^^^^^^^^

* premiers suivis de projects
* données mal balancées
    * :ref:`mlbimbalancedrst`
* algorithmes de streaming
    * :ref:`BJKSTenoncerst`
    * :ref:`BJKSTrst`
* revue de compétitions Kaggle
    * `revue 2016 <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/ensae201611.html>`_
    * `revue 2017 <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2017/ensae_2a_201711.html>`_
* visualisation
    * :ref:`l-py2a-cartes`
    * `10 plotting libraries <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_
* interprétabilité
    * :ref:`l-interpretabilite-ml`
* conclusion
    * :ref:`l-td2a-notions`
* projets
    * :ref:`l-projinfo2a`
    * `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
    * :ref:`l-debutermlprojet`
    * :ref:`l-question-projet-2A-ml`
