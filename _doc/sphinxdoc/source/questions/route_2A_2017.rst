
.. _l-feuille-de-route-2017-2A:

Feuille de route 2017
=====================

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td2a>`

Plan
++++

Les cours et séances se déroulent sur 8 séances de 3h
lundi matin. Le cours est divisé en deux pistes
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
        Featurisation, Etique dans les modèles,
        :ref:`l-route2017-eco7`
      - Interprétabilité des modèles, problèmes de classification binaire,
        Etique dans les modèles,
        :ref:`l-route2017-stat7`
    * - 14/11 (8)
      - Algorithme de streaming, Interprétabilité des modèles,
        sequence learning, présentation des projets,
        Revue de compétition Kaggle
      - Construction d'un site web, retour sur la compétition,
        présentation des projets

Intervenants
++++++++++++

`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_,
Anne Muller, Elodie Royant, Antoine Thabault,
Antoine Ly, Benjamin Donnot, Eliot Barril,
Gaël Varoquaux.

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
* Compétation : :ref:`solution2016creditclementrst`

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
    * :ref:`td1acenoncesession12rst`
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

* Panoplie de graphes et cartes : :ref:`td1acenoncesession12rst`
* ROC pour un modèle logit :ref:`sphx_glr_antiseches_ml_basic_plot_binary_classification.py`
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

.. _l-route2017-exo3:

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
    * :ref:`sphx_glr_ml_basic_plot_roc.py`
* machine learning crypté
    * :ref:`mlcrypteddatarst`
    * :ref:`mlcrypteddatacorrectionrst`
* Grid Search
    * :ref:`sphx_glr_ml_basic_plot_grid_search.py`

.. _l-route2017-eco6:

Séance 6 Eco
^^^^^^^^^^^^

* NLP, scrapping
    * :ref:`td2aNLPpocketrst`
    * :ref:`td2aNLPpocketcorrectionrst`

.. _l-route2017-stat6:

Séance 6 Maths
^^^^^^^^^^^^^^

* deep learning : notebooks
    * :ref:`100LogisticIRISrst`
    * :ref:`110PerceptronIrisrst`
    * :ref:`200PerceptronMNISTrst`
    * :ref:`210ConvolutionMNISTrst`
    * :ref:`300ConvolutionCIFAR10rst`
    * :ref:`mldeeppythonrst`
    * `Transfer Learning <https://github.com/sdpython/2017_deeplearning_demo/blob/master/Fine_Tuning_Deep_CNNs_with_GPU_rendered.ipynb>`_ (Olivier Grisel)
* deep learning : présentations
    * `Introduction au Deep Learning <https://github.com/sdpython/ensae_teaching_cs/blob/master/_doc/sphinxdoc/source/specials/DEEP%20LEARNING%20FOR%20ENSAE.pdf>`_
    * :ref:`l-nolabel`
    * `Deep Learning 2017 <http://www.xavierdupre.fr/exposes/deeplearning/>`_ (avec Olivier Grisel)

.. _l-route2017-eco7:

Séance 7 Eco
^^^^^^^^^^^^

.. _l-route2017-stat7:

Séance 7 Maths
^^^^^^^^^^^^^^

* séries temporelles
    * :ref:`mltimeseriesbaserst`
    * :ref:`mapreducetimeseriesrst`
    * :ref:`td2atimeseriesrst`
    * :ref:`td2atimeseriescorrectionrst`
