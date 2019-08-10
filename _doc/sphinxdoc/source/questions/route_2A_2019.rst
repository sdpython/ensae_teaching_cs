
.. _l-feuille-de-route-2019-2A:

Feuille de route 2019 (2A)
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

Séance 1 - 10/9 - amphi - régression et classification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Précision sur le cours, évaluation, exposés, ressources, TD, amphi,
* `Rappels de mathématiques <http://www.xavierdupre.fr/app/papierstat/helpsphinx/rappel.html>`_
* :ref:`td2ecorappels1arst`, :ref:`mlcmachinelearningproblemsrst`
* Support de cours, ce site,
  `Lectures sur le machine learning <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/index.html>`_,
  github: :epkg:`sdpython`
* `Un exemple simple de régression linéaire <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/2019-01-25_linreg.html>`_
* `Base d'apprentissage et de test <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_knn_split.html>`_
* `Classifications et courbes ROC <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_color_roc.html>`_
* `Validation croisée <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_knn_cross_val.html>`_
* **A faire pour la prochaine fois** : exécuter trois notebooks,
  :ref:`structuresdonneesconversionrst`, :ref:`histogrammerapiderst`,
  :ref:`mlfeaturesmodelrst`
  
Séance 2 - 17/9 - TD - régression et classification par la pratique
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Organisée comme une compétition, choisir un jeu de données 
sur `UCI <https://archive.ics.uci.edu/ml/datasets.php>`_
et enregister les performances. La séance commencera
par le requêtage d'une API REST car la soumission se fera via une
API et non via un site.

**prévoir deux jeux d'apprentissage et de tests**

Aborder les prétraitement comme la
`normalisation <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_normalisation.html>`_,
la :epkg:`dimensionsreductionrst`.

Séance 3 - 24/9 - TD - prétraitement et catégories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `normalisation <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_normalisation.html>`_,
* :epkg:`dimensionsreductionrst`
* traitement des catégories avec le jeu de données tiré de l'exemple
  `Investigating dirty categories
  <https://dirty-cat.github.io/stable/auto_examples/01_investigating_dirty_categories.html>`_
* comparaison de modèles, régression logistique, plus proche voisin, random forest,
  gradient boosting classifier, xgboost, lightgbm, catboost, Lasso, Ridge,
  toujours sous la forme d'une compétition

Séance 4 - 1/10 - amphi - ranking et compagnie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Ranking, détection d'anomalies, clustering, valeurs manquantes,
  recommandations, imbalanced classification

Séance 5 - 8/10 - TD - séries temporelles - gestion du texte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toujours sous la forme d'une compétition

* `Variables textuelles <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/preprocessing.html>`_
* `tokenisation <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_tokenize.html>`_
* `de la tokenisation aux features <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_tokenize_features.html>`_
* `word2vec <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/text_sentiment_wordvec.html>`_
* :ref:`l-ml2a-text-features`

Séance 6 - 15/10 - TD - amphi - modèles mathématiques - éthique
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Propriétés des modèles mathématiques, modèles linéaires, modèles ensemblistes, modèles,
  dérivables, gradient, feature importance, parallélisme, boosting
* Ethique, machine learning éthique (Frédéric Bardolle)

Séance 7 - 22/10 - TD - sérialisation, webscrapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* API SNCF
* webscrapping
* écriture de code rapide
* traitement de gros volumes de données (base de données open food facts)

Séance 8 - 5/11 - amphi/TD - datascience agile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Notion de pipeline
* Mise en production de modèles de machine learning avec
  :epkg:`docker`, :epkg:`kubernetes`...

Séance 9 - 12/10 - amphi - sérialisation, webscrapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* discussion sur les projets
* créer son propre modèle de machine learning
  en utilisant l'API de :epkg:`scikit-learn`,
  `Prédicteur pour chaque catégorie
  <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/wines_color_linear.html>`_,
  :ref:`2019-09-18sklearnapirst`,
  `Contributing <http://scikit-learn.org/stable/developers/contributing.html#contributing-code>`_,
  `sklearn.base <http://scikit-learn.org/stable/modules/classes.html#module-sklearn.base>`_
* `Understanding and diagnosing your machine-learning models
  <http://gael-varoquaux.info/interpreting_ml_tuto/>`_
* Les cours de Gaël Varoquaux :ref:`l-ml-skgael`,
  les notebooks d'exercices associées à ces lectures.


Prérequis
+++++++++

* *Voix stat* : maîtrise du langage :epkg:`Python`,
  connaissance des modules :epkg:`pandas`, :epkg:`numpy`, :epkg:`matplotlib`, voir
  `quelques rappels <http://www.xavierdupre.fr/app/papierstat/helpsphinx/rappel.html>`_
* *Voix éco* : maîtrise du langage :epkg:`Python`, :ref:`td2ecorappels1arst`

Intervenants
++++++++++++

`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_,
Anne Muller,
Eliot Barril,
Mayeul Picard,
Frédéric Bardolle,
`Gaël Varoquaux <http://gael-varoquaux.info/>`_.

Liens utiles et trop nombreux
+++++++++++++++++++++++++++++

* :ref:`td1acenoncesession12carterst`
* :ref:`td1acenoncesession12plotrst`, :ref:`td1acenoncesession12carterst`,
  :ref:`td1acenoncesession12jsrst`
* `Etude statistique <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/enonce_2017.html#enonce2017rst>`_,
  `correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/solution_2017.html>`_
* `Tracer une carte en Python <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/enedis_cartes.html>`_
* :ref:`l-mlbasic-anomaly`
* :ref:`l-ml2a-ranking`
* :ref:`l-imbalanced-classification`
* :ref:`l-td2a-missing-values`
* :ref:`td2aclusteringrst`, :ref:`td2aclusteringcorrectionrst`
* `Ranking et système de recommandations <http://www.xavierdupre.fr/app/papierstat/helpsphinx/lectures/otherml.html>`_
* :ref:`l-ml2a-testab` (ou `Test A/B sur wikipedia <https://en.wikipedia.org/wiki/A/B_testing>`_)
* `Liens entre factorisation de matrices, ACP, k-means <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/missing_values_mf.html>`_
* :ref:`l-td2a-sys-recommandation`
* Traitement des variables catégorielles et textuelles.
* :ref:`td2asentimentanalysisrst`, :ref:`td2asentimentanalysiscorrectionrst`
* Regardez différentes options disponibles pour faire les graphiques et
  passez un peu de temps sur l'exemple :ref:`td2avisualisationrst`
* :ref:`ACP <td2acenoncesession3arst>` (s'arrêter à l'exercice 1)
* :ref:`Régression linéaire <td2aecoregressionslineairesrst>`
* :ref:`Logit <td2aecocompetitionmodeleslogistiquesrst>`
* :ref:`l-td2a-ml-crypted`
* :ref:`mltimeseriesbaserst`, :ref:`timeseriesssarst`
* :ref:`l-td2a-hyperparametre` et :ref:`l-ml2a-autolearning`
* `Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising 
  <http://jmlr.org/papers/v14/bottou13a.html>`_
* `Making Contextual Decisions with Low Technical Debt <https://arxiv.org/pdf/1606.03966.pdf>`_
* deep reinforcement learning, `Alpha Go Zero <https://deepmind.com/blog/alphago-zero-learning-scratch/>`_
* :ref:`td2asentimentanalysisrst`, :ref:`td2asentimentanalysiscorrectionrst`
* :ref:`td2aenoncesession4Arst`, :ref:`correction <td2acorrectionsession4Arst>`
* :ref:`TD2AEcoWebScrapingrst` (:ref:`correction <TD2AEcoWebScrapingcorrigerst>`)
* :ref:`td2aeco5dTravaillerdutextelesexpressionsregulieresrst`
  (:ref:`correction <td2aeco5dTravaillerdutextelesexpressionsregulierescorrectionrst>`)
* :ref:`mlatreeoverfittingrst`
* :ref:`correction <knnhighdimensioncorrectionrst>`,
  `Nearest Neighbours and Sparse Features
  <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/notebooks/nearest_neighbours_sparse_features.html>`_
* `Régression linéaire par morceaux <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/regression_lineaire.html>`_
* `Corrélations non linéaires <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/correlation_non_lineaire.html>`_
* `Régression logistique, diagramme de Voronoï, k-Means <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/lr_voronoi.html>`_
* `AdaBoost <https://fr.wikipedia.org/wiki/AdaBoost>`_,
  :ref:`2019-10-09ensemblegradientboostingrst`
* :ref:`mlcccmachinelearninginterpretabiliterst` (feature importance)
* :ref:`mlccmachinelearningproblems2rst`
* :ref:`l-ml2a-selvar`
* `XGBoost: A Scalable Tree Boosting System <https://arxiv.org/pdf/1603.02754.pdf>`_,
  sparsité et valeurs manquantes
* `LightGBM: A Highly Efficient Gradient Boosting Decision Tree <https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree.pdf>`_,
  sélection des splits, combinaison de features sparses
* `CatBoost: gradient boosting with categorical features support <http://learningsys.org/nips17/assets/papers/paper_11.pdf>`_,
  ajout de combinaisons de variables
* `Understanding and diagnosing your machine-learning models <http://gael-varoquaux.info/interpreting_ml_tuto/>`_.
* `Réseaux de neurones <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/rn/rn.html>`_
* :ref:`l-nolabel`
* `Galleries de problèmes résolus ou presque <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/dl_resolus.html>`_
* `Transfer Learning <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/deep_transfer_learning.html>`_
* `Search images with deep learning <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/notebooks/search_images.html>`_
* `GAN <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/deep_generative_adversarial_network_gan.html>`_
* `Les fossoyeurs de l’innovation <https://salon.thefamily.co/les-fossoyeurs-de-l-innovation-6a754d1e8e35>`_ par Nicolas Colin
* `Tristan Harris : «Beaucoup de ficelles invisibles dans la tech nous agitent comme des marionnettes» <http://www.lefigaro.fr/secteur/high-tech/2019/05/31/32001-20190531ARTFIG00004-tristan-harris-beaucoup-de-ficelles-invisibles-dans-la-tech-nous-agitent-comme-des-marionnettes.php>`_
* `How AI Designers will Dictate Our Civic Future  <https://vimeo.com/238221677>`_
* `AlgoTranspency <https://algotransparency.org/>`_
* `L'efficacité d'un logiciel censé prédire la récidive à nouveau critiquée <https://www.lemonde.fr/pixels/article/2019/01/17/l-efficacite-d-un-logiciel-cense-predire-la-recidive-a-nouveau-critiquee_5243218_4408996.html>`_
* Google Translate biais sexiste : *A doctor, a nurse* traduit en *un docteur, une infirmière* et non *une docteure, un infirmier*
* `Serment d'Hippocrate pour Data Scientist <https://www.hippocrate.tech/>`_
* `Un monde d'automatisation ? <https://www.editions-eres.com/ouvrage/4222/un-monde-d-automatisation>`_,
  avec entre autres Alexeï Grinbaum
* `Ethique de la vertu <https://fr.wikipedia.org/wiki/%C3%89thique_de_la_vertu>`_ (`Aristote <https://fr.wikipedia.org/wiki/Aristote>`_,
  ne fais pas à autrui ce que tu ne voudrais pas qu'on te fasse),
  `éthique utilitariste <https://fr.wikipedia.org/wiki/Utilitarisme>`_
  (`Bentham <https://fr.wikipedia.org/wiki/Jeremy_Bentham>`_,
  maximiser le plaisir, diminuer les peines en apposant une échelle de valeur,
  l'action est jugée sur la conséquence),
  `éthique déontologique <https://fr.wikipedia.org/wiki/%C3%89thique_d%C3%A9ontologique>`_
  (`Kant <https://fr.wikipedia.org/wiki/Emmanuel_Kant>`_,
  `impératif catégorique <https://fr.wikipedia.org/wiki/Imp%C3%A9ratif_cat%C3%A9gorique>`_,
  je peux faire quelque chose si
  tout le monde peut le faire sans mettre le monde en danger, action en fonction de l'intention
  quelque soit le résultat),
* `Dilemme du tramway <https://fr.wikipedia.org/wiki/Dilemme_du_tramway>`_
* `L'utilitarisme et les problèmes de tramways <https://minarchiste.wordpress.com/2013/12/06/lutilitarisme-et-les-problemes-de-tramways/>`_
* `Théorie du développement moral de Kohlberg <https://fr.wikipedia.org/wiki/Th%C3%A9orie_du_d%C3%A9veloppement_moral_de_Kohlberg>`_
* :ref:`knnhighdimensionrst`, :ref:`knnhighdimensioncorrectionrst`
* :ref:`BJKSTrst`
* :ref:`td2acenoncesession6Arst`, :ref:`td2acorrectionsession6Arst`
* :ref:`td2acenoncesession6Brst`, :ref:`td2acorrectionsession6Brst`
* :ref:`td2asentimentanalysisrst`
  (:ref:`correction <td2asentimentanalysiscorrectionrst>`),
  lien vers le jeu de données :
  `Project 1: Spooky Data Analysis <https://github.com/GU4243-ADS/spring2019-project1-ginnyqg/tree/master/data>`_
* :ref:`td2aeconlptfidfngramsldaword2vecsurdesextraitslitterairesrst`
* :ref:`td2amltextfeaturesrst`
* :ref:`td2asomenlprst`
