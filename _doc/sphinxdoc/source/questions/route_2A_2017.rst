
.. _l-feuille-de-route-2017-2A:

Feuille de route 2017
=====================

.. contents::
    :local:

:ref:`Page principale du cours <l-td2a>`_

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
      - clustering, ACP, t-SNE, projection, Python et C++,
        revue de code de scikit-learn
        cours de Gaël Varoquaux
      - Clustering, application aux vélos de Chicago,
        revue des différentes types de variables (numérique, entier, texte, date...)
        cours de Gaël Varoquaux
    * - 10/10 (4)
      - Revue de problèmes de machine learning formalisés,
        Données textuelles, variables catégorielles, word embedding
      - Revue de problèmes de machine learning formalisés,
        Données textuelles, variables catégorielles
    * - 17/10 (5)
      - Deep learning, Keras
      - Web scrapping, API
    * - 24/10 (6)
      - Exercice sur un problèm de ranking, moteur de recherche,
        machine learning données cryptées
      - Etique dans les données, anonimisation des données,
        séries temporelles
    * - 7/11 (7)
      - Revue de compétition Kaggle, deep learning, itérateurs, algorithme streaming
      - Interprétabilité des modèles, problèmes de classification binaire
    * - 14/11 (8)
      - Transfer Learning, Présentation des projets
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
* Manipulation des données : :ref:`td2acenoncesession2arst`,
  :ref:`td2acorrectionsession2arst`, :ref:`td2acenoncesession1rst`,
  :ref:`td2acorrectionsession1rst`

*Notebooks*

* `try.jupyter.org <https://try.jupyter.org/>`_
* `Notebook <http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb>`_

*Compléments*

* Rappels sur des bases du langage :epkg:`Python` : :ref:`td1acenoncesession1rst`,
  :ref:`td1acenoncesession2rst`, :ref:`td1acenoncesession3rst`, :ref:`codelistetuplerst`,
  :ref:`structuresdonneesconversionrst`
* Notebook : :ref:`td2acenoncesession2crst`
* Compétation : :ref:`solution2016creditclementrst`

.. _l-route2017-stat1:

Séance 1 Stat
^^^^^^^^^^^^^

* Manipulation des données : :ref:`td2acenoncesession1rst`,
  :ref:`td2acorrectionsession1rst`, :ref:`td2acenoncesession2arst`,
  :ref:`td2acorrectionsession2arst`
* Graphes : :ref:`td2avisualisationrst`,
  `10 plotting libraries <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_
* Cartes : :ref:`td1acenoncesession12rst`, :ref:`td1acorrectionsession12rst`
* SQL : :ref:`sqldocrst`, :ref:`td2aecosqlrst`, :ref:`td2aecosqlcorrectionrst`
* Sérialisation : :ref:`td2acenoncesession2erst`

.. _l-route2017-eco2:

Séance 2 Eco
^^^^^^^^^^^^

* Cartes : :ref:`td1acenoncesession12rst`, :ref:`td1acorrectionsession12rst`
* SQL : :ref:`sqldocrst`, :ref:`td2aecosqlrst`, :ref:`td2aecosqlcorrectionrst`

.. _l-route2017-stat2:

Séance 2 Stat
^^^^^^^^^^^^^

* Itérateur, parallélisation : :ref:`td2acenoncesession5donneesnonstructureesetprogrammationfonctionnellerst`,
  :ref:`seance5daskrst`, :ref:`td2acorrectionsession5donneesnonstructureesetprogrammationfonctionnellecorrigerst`
* Algorithme : :ref:`knnhighdimensionrst`, :ref:`knnhighdimensionrst`
* Pratique logicielle : :ref:`td1aunittestcirst`, :ref:`td1aunittestcicorrectionrst`
