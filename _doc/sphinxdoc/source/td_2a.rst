
.. _l-td2a:

==========================================
Python pour un Data Scientist / Economiste
==========================================

.. index:: 2A

`ENSAE - OMI2F2 <http://www.ensae.fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/2me-anne-formationsdiplome-95.html?id=101352>`_

Cours animé par :
`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_  (ENSAE 1999) [#fwrite1]_,
Anne Muller (ENSAE 2012) [#fwrite1]_,
Elodie Royant (ENSAE 2008) [#fwrite2]_,
Antoine Thabault (ENSAE 2012) [#fwrite2]_,
Jérémie Jakubowicz (ENSAE 2002) [#fwrite2]_,
Nicolas Rousset [#fwrite2]_,
Antoine Ly (ENSAE 2015),
Benjamin Donnot (ENSAE 2015),
Gaël Varoquaux [#fwrite2]_

Ce cours s'étale sur 6 séances de cours/TD d'une durée de 4h.
Les outils proposés sont en langage `Python <https://www.python.org/>`_.
Ils sont tous `open source <http://fr.wikipedia.org/wiki/Open_source>`_,
pour la plupart disponibles sur `GitHub <https://github.com/>`_ et en développement actif.
Python est récemment devenu une alternative plus que probante
pour les scientifiques et comme c'est un langage générique, il est
possible de gérer l'ensemble des traitements appliqués aux données, depuis
le traitements des sources de données jusqu'à leur visualisation sans changer de langage.

Le cours est prévu pour des profils plutôt statistiques |pystatpng|
ou plutôt économiques |pyecopng|. Ces images reviendront pour indiquer
si les contenus s'adressent plutôt aux uns ou aux autres.
La présentation
`ENSAE 2A - Données, Machine Learning et Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html>`_ |slideslogo|
donne un aperçu des thèmes abordés.

* :ref:`feuille de route 2016 <l-feuille-de-route-2016-2A>`
* :ref:`compétitions <td2A-competition-ml>`
* :ref:`projet informatique <l-projinfo2a>`.

**Thèmes :**

.. contents::
    :local:
    :depth: 2

.. |slideslogo| image:: _static/slides_logo.png
             :height: 20
             :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html

.. |pyecopng| image:: _static/pyeco.png
            :alt: Economie

.. |pystatpng| image:: _static/pystat.png
            :alt: Statistique

------------

Rappels de programmation
========================

|pyecopng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/td2_eco_rappels_1a

.. index:: sérialisation, index, dataframe

------------

Matrices et DataFrames - numpy pandas SQL
=========================================

Import/export de données dans un DataFrame,
manipulation selon une logique SQL,
utilité des index,
`lambda function <http://www.diveintopython.net/power_of_introspection/lambda_functions.html>`_,
premiers graphiques,
commandes magiques.

.. contents::
    :local:
    :depth: 1

DataFrame
+++++++++

|pyecopng| |pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_dataframe

*Modules*

* `pandas <http://pandas.pydata.org/>`_

Array, Matrix
+++++++++++++

|pyecopng| |pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_dnumpy

*Modules*

* `numpy <http://www.numpy.org/>`_
* `scipy <https://www.scipy.org/>`_

SQL
+++

|pyecopng| |pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    ext2a/sql_doc
    notebooks/_gs2a_sql

.. _l-visualisation-td2a:

------------

Visualisation
=============

.. contents::
    :local:
    :depth: 1

Graphes
+++++++

|pyecopng| |pystatpng|

Plan

* Présenter `10 plotting libraries at PyData 2016 <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_.
* Grouper les étudiants par deux
* Considérer un jeu de données
* Chaque groupe essaye une librairie différente
* Insister sur la visualisation de gros jeu de données

Il existe de nombreuses librairies de visualisation réparties en deux grandes familles.
La première produit des images
(`matplotlib <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_matplotlib.html#immatplotlibrst>`_,
`seaborn <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_seaborn.html#imseabornrst>`_,
`networkx <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_networkx.html#imnetworkxrst>`_),
la seconde produit des graphes animés à l'aide de Javascript
(`bokeh <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/js_bokeh.html#jsbokehrst>`_,
`bqplot <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_networkx.html#imnetworkxrst>`_).
Les librairies les plus récentes implémentent les deux modes en cherchant toujours plus
de simplicité. A ce sujet, il faut jeter un coup d'oeil à
`flexx <https://flexx.readthedocs.io/en/stable/>`_. Elles explorent aussi
la visualisation animée de gros jeux de données telle que
`datashader <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/big_datashader.html#bigdatashaderrst>`_.

*Notebook sur matplotlib*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_visu

* `Graphes classiques métriques pour des modèles de machine learning <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_ml_enonce.html>`_
* `Graphes classiques métriques pour des modèles de machine learning - correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_ml_correction.html>`_

*Notebook sur Javascript*

.. toctree::
    :maxdepth: 2

    ext2a/javascript_doc

* Lire :ref:`Javascript et traitement de données <blog-js-data>`

*Modules*

* `matplotlib <http://matplotlib.org/>`_
* `seaborn <https://github.com/mwaskom/seaborn>`_
* `bokeh <http://bokeh.pydata.org/en/latest/>`_
* `bqplot <https://github.com/bloomberg/bqplot>`_
* :ref:`l-visualisation`

Cartes
++++++

|pyecopng| |pystatpng|

*Notebooks*

* :ref:`td1acenoncesession12rst`
* :ref:`td1acorrectionsession12rst`
* `Evolution d'une population <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance4_projection_population_enonce.html>`_
* `Evolution d'une population - correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_correction.html>`_

*Formats de données*

* :ref:`Système de coordonnées <blog-donnees-carroyees-2016>` (et données carroyées)
* format de cartes
  `shapefiles <https://en.wikipedia.org/wiki/Shapefile>`_,
  `topoJSON <https://en.wikipedia.org/wiki/GeoJSON#TopoJSON>`_,
  `geoJSON <https://en.wikipedia.org/wiki/GeoJSON>`_,
* `Projections sphériques et conversion <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/notebooks/chsh_geo.html>`_
* conversion de coordonnées en longitude / latitude
* librairies
  `basemap <http://matplotlib.org/basemap/>`_, ...
* sources :
  `DataMaps <http://datamaps.github.io/>`_,
  `Find Data <https://bost.ocks.org/mike/map/#finding-data>`_

*Modules*

* `basemap <http://matplotlib.org/basemap/>`_
* `cartopy <http://scitools.org.uk/cartopy/>`_
* `pyshp <https://pypi.python.org/pypi/pyshp>`_
* `shapely <https://pypi.python.org/pypi/Shapely>`_
* `pyproj <https://pypi.python.org/pypi/pyproj>`_
* `geopy <https://pypi.python.org/pypi/geopy>`_

------------

Transformations des données
===========================

.. contents::
    :local:
    :depth: 1

Projections, réduction des dimensions
+++++++++++++++++++++++++++++++++++++

|pyecopng| |pystatpng|

(à venir)

*Lectures*

* `PCA <http://scikit-learn.org/stable/modules/decomposition.html>`_
* `Johnson–Lindenstrauss lemma <https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma>`_,
  `Random projection <http://scikit-learn.org/stable/modules/random_projection.html>`_,
  `Concentration of measure <https://en.wikipedia.org/wiki/Concentration_of_measure>`_,
  `Experiments with Random Projection <http://cseweb.ucsd.edu/~dasgupta/papers/randomf.pdf>`_
* `Compressed Sensing <https://en.wikipedia.org/wiki/Compressed_sensing>`_
* `Locality-sensitive hashing <https://en.wikipedia.org/wiki/Locality-sensitive_hashing>`_
* `Manifold learning <http://scikit-learn.org/stable/modules/manifold.html>`_
* `Cartes de Kohonen <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_clus/kohonen.html>`_
* `Dynamic Self-Organising Map <http://www.labri.fr/perso/nrougier/coding/article/article.html>`_
* `Fast Randomized SVD <https://research.fb.com/fast-randomized-svd/>`_
* `Neural Autoregressive Distribution Estimation <http://www.jmlr.org/papers/volume17/16-272/16-272.pdf>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/>`_
* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `fbpca <http://fbpca.readthedocs.io/en/latest/>`_ : ACP
* `prince <https://github.com/MaxHalford/Prince>`_ : ACM

*Animations*

* `How to Use t-SNE Effectively <http://distill.pub/2016/misread-tsne/>`_

Variables catégorielles
+++++++++++++++++++++++

|pyecopng| |pystatpng|

(à venir)

* Corrélation entre des variables catégorielles

*Lectures*

* :ref:`Tranformer les variables catégorielles et contrastes <encoding-categorie-id>`
* :ref:`Corrélations entre des variables catégorielles <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/correlation_non_lineaire.html>`_
* `Enoncé d'examan autour des variables catégorielles <http://www.xavierdupre.fr/site2013/enseignements/tdnoteseul/td_note_2017.pdf>`_
  et sa :ref:`corection <tdnote2017rs>`

Distances
+++++++++

(à venir)

|pystatpng|

*Lectures*

* `Learning Hierarchical Similarity Metrics <http://www.cs.toronto.edu/~vnair/cvpr12.pdf>`_
* `From Word Embeddings To Document Distances <http://jmlr.org/proceedings/papers/v37/kusnerb15.pdf>`_

Clustering
++++++++++

|pyecopng| |pystatpng|

(à venir)

* scopre silhouette
* clustering de variables catégorielles

*Lectures*

* `A New Algorithm and Theory for Penalized Regression-based Clustering <http://www.jmlr.org/papers/volume17/15-553/15-553.pdf>`_ :
  méthode de sélection de variables pour des méthodes non supervisés de clustering, voir aussi
  `Penalized Model-Based Clustering with Application to Variable Selection <http://www.jmlr.org/papers/volume8/pan07a/pan07a.pdf>`_
* `K-means <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_clus/kmeans.html>`_
* `Cartes de Kohonen <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_clus/kohonen.html>`_
* `Clustering by Passing Messages Between Data Points <http://www.icmla-conference.org/icmla07/FreyDueckScience07.pdf>`_
* `Map/Reduce Affinity Propagation Clustering Algorithm <http://www.ijeee.net/uploadfile/2014/0807/20140807114023665.pdf>`_
* `Parallel Hierarchical Affinity Propagation with MapReduce <https://arxiv.org/abs/1403.7394>`_
* `Cats & Co: Categorical Time Series Coclustering <https://arxiv.org/abs/1505.01300v1>`_
* `Comparing Python Clustering Algorithms <https://github.com/scikit-learn-contrib/hdbscan/blob/master/docs/comparing_clustering_algorithms.rst>`_
* `Fast and Provably Good Seedings for k-Means <https://papers.nips.cc/paper/6478-fast-and-provably-good-seedings-for-k-means.pdf>`_
* `Clustering with Same-Cluster Queries <https://papers.nips.cc/paper/6449-clustering-with-same-cluster-queries.pdf>`_
* `The K-Modes Algorithm for Clustering <https://arxiv.org/pdf/1304.6478v1.pdf>`_
* `Clustering of Categorical variables <http://eric.univ-lyon2.fr/~ricco/cours/slides/en/classif_variables_quali.pdf>`_
* `Classification d'un ensemble de variables qualitatives <http://archive.numdam.org/ARCHIVE/RSA/RSA_1998__46_4/RSA_1998__46_4_5_0/RSA_1998__46_4_5_0.pdf>`_
* `Yinyang K-Means: A Drop-In Replacement of the Classic K-Means with Consistent Speedup <https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ding15.pdf>`_
* `Online Clustering with Experts <http://www.jmlr.org/proceedings/papers/v26/choromanska12a/choromanska12a.pdf>`_
* `Kernel K-means and Spectral Clustering <https://pdfs.semanticscholar.org/6be9/e527f94e88fef82e2270e94162d31a2dbfbc.pdf>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/>`_
* `hdbscan <https://github.com/scikit-learn-contrib/hdbscan>`_

Détection d'anomalies
+++++++++++++++++++++

*(à venir)*

*Lectures*

* `A Classification Framework for Anomaly Detection <http://www.jmlr.org/papers/volume6/steinwart05a/steinwart05a.pdf>`_
* `Security Analysis of Online Centroid Anomaly Detection <http://www.jmlr.org/papers/volume13/kloft12b/kloft12b.pdf>`_
* `Robust Random Cut Forest Based Anomaly Detection On Streams <http://jmlr.org/proceedings/papers/v48/guha16.pdf>`_
* `Network Traffic Decomposition for Anomaly Detection <https://arxiv.org/abs/1403.0157v1>`_
* `Network Volume Anomaly Detection and Identification in Large-scale Networks based on Online Time-structured Traffic Tensor Tracking <https://arxiv.org/abs/1608.05493v1>`_

*Vidéos*

* `Anomaly Detection vs. Supervised Learning <https://www.coursera.org/learn/machine-learning/lecture/Rkc5x/anomaly-detection-vs-supervised-learning>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/modules/outlier_detection.html>`_
* `pyculiarity <https://github.com/nicolasmiller/pyculiarity>`_
* `lsanomaly <https://github.com/lsanomaly/lsanomaly>`_

------------

Machine Learning - Formalisation
================================

.. contents::
    :local:
    :depth: 1

.. _l-ml-skgael:

Machine learning, cours de Gaël Varoquaux
+++++++++++++++++++++++++++++++++++++++++

|pyecopng| |pystatpng|

Gaël est un des concepteurs de `scikit-learn <http://scikit-learn.org/stable/>`_.

* `notes de lectures <https://github.com/GaelVaroquaux/sklearn_ensae_course>`_ (`Gaël Varoquaux <http://gael-varoquaux.info/>`_)
* machine learning et `scikit-learn <http://scikit-learn.org/stable/>`_
  (`tutoriels sur scikit-learn <http://nbviewer.jupyter.org/github/GaelVaroquaux/sklearn_pandas_tutorial/tree/master/rendered_notebooks/>`_),
* *Quelques extraits.* Par définition les plus proches voisins ne font pas d'erreur sur la base d'apprentissage,
  l'apprentissage consiste à forcer le modèle à faire des erreurs. `Overfitting <http://en.wikipedia.org/wiki/Overfitting>`_ et
  `régularisation <http://en.wikipedia.org/wiki/Regularization_(mathematics)>`_.
  Erreur `L2 <http://en.wikipedia.org/wiki/Lp_space>`_ et pénalisation `L1 <http://fr.wikipedia.org/wiki/Espace_L1>`_.
  `RandomizedPCA <http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.RandomizedPCA.html>`_,
  `GridSearch <http://scikit-learn.org/stable/modules/grid_search.html>`_,
  `LassoCV <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html>`_.
  `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_.

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_statdes
    notebooks/_gs2a_ml_base

*Lectures*

* `A Visual Introduction to Machine Learning <http://www.r2d3.us/visual-intro-to-machine-learning-part-1/>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `A Tour of Machine Learning Algorithms <http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/>`_
* `12 Algorithms Every Data Scientist Should Know <https://datafloq.com/read/12-algorithms-every-data-scientist-should-know/2024>`_ *(2016/06)*
* `10+2 Data Science Methods that Every Data Scientist Should Know in 2016 <http://tjo-en.hatenablog.com/entry/2016/04/18/190000>`_ *(2016/06)*
* `Complete Guide to Parameter Tuning in XGBoost (with codes in Python) <https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/>`_ *(2016/08)*
* `XGBoost: A Scalable Tree Boosting System <http://arxiv.org/pdf/1603.02754v1.pdf>`_, Tianqi Chen, Carlos Guestrin

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/>`_

.. _l-td2a-ml-extensions:

Pratique du machine learning, problème de données
+++++++++++++++++++++++++++++++++++++++++++++++++

|pyecopng| |pystatpng|

.. toctree::
    :maxdepth: 2

    questions/some_ml

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_ml

*Lectures*

* :ref:`Travailleur les features ou changer de modèle <mlfeaturesmodelrst>`
* :ref:`Bien démarrer un projet de machine learning <l-debutermlprojet>`
* :ref:`question_projet_2014`
* `MA 2823 Foundations of Machine Learning (Fall 2016) <http://cazencott.info/index.php/pages/MA-2823-Foundations-of-Machine-Learning-%28Fall-2016%29>`_
* `A Random Forest Guided Tour <http://www.lsta.upmc.fr/BIAU/bs.pdf>`_, Gérard Biau, Erwan Scornet
* `Courbe ROC <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html>`_
* `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_
* `A Unified Approach to Learning Task-Specific Bit Vector Representations for Fast Nearest Neighbor Search <http://www.cs.toronto.edu/~vnair/www12.pdf>`_

*Recherche*

* `XGBoost: A Scalable Tree Boosting System <https://arxiv.org/pdf/1603.02754.pdf>`_
* `Classification of Imbalanced Data with a Geometric Digraph Family <http://www.jmlr.org/papers/volume17/15-604/15-604.pdf>`_
* `On the Influence of Momentum Acceleration on OnlineLearning <http://www.jmlr.org/papers/volume17/16-157/16-157.pdf>`_

.. index:: multilabel

*Multilabel*

* `A Ranking-based KNN Approach for Multi-Label Classification <http://www.jmlr.org/proceedings/papers/v25/chiang12/chiang12.pdf>`_
* `Classification by Selecting Plausible Formal Concepts in a Concept Lattice <http://ceur-ws.org/Vol-977/paper5.pdf>`_
* `Large-scale Multi-label Learning with Missing Labels <http://jmlr.org/proceedings/papers/v32/yu14.pdf>`_
* `Multiclass-Multilabel Classification with More Classes than Examples <http://www.jmlr.org/proceedings/papers/v9/dekel10a/dekel10a.pdf>`_

*Digressions*

* `A Network That Learns Strassen Multiplication <http://www.jmlr.org/papers/volume17/16-074/16-074.pdf>`_
* `Learning Theory for Distribution Regression <http://www.jmlr.org/papers/volume17/14-510/14-510.pdf>`_

*Métriques*

* `Optimization of AMS using Weighted AUC optimized models <http://jmlr.org/proceedings/papers/v42/diaz14.pdf>`_

*Librairies*

`JMLR <http://www.jmlr.org/>`_
poste régulièrement des articles sur des librairies de machine learning open source.

* `fastFM: A Library for Factorization Machines <fastFM: A Library for Factorization Machines>`_

*Modules*

* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `xgboost <https://xgboost.readthedocs.io/en/latest/>`_
* `mlxtend <https://github.com/rasbt/mlxtend>`_

Ranking
+++++++

*(à venir)*

*Lectures*

* `Learning to rank (software, datasets) <http://arogozhnikov.github.io/2015/06/26/learning-to-rank-software-datasets.html>`_
* `Multiple-criteria decision analysis <https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis>`_
* `Data-driven Rank Breaking for Efficient Rank Aggregation <http://www.jmlr.org/papers/volume17/16-209/16-209.pdf>`_

*Modules*

* `xgboost <https://xgboost.readthedocs.io/en/latest/>`_
* `scikit-learn <http://scikit-learn.org/>`_
* `rankpy <https://github.com/dmitru/rankpy>`_ (standby)
* `The Lemur Project - ranklib <https://sourceforge.net/p/lemur/wiki/RankLib/>`_
* `scikit-criteria <https://github.com/leliel12/scikit-criteria>`_ (standby)

Système de recommandation
+++++++++++++++++++++++++

*(à venir)*

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/>`_

.. _l-deep-learning:

Deep Learning
+++++++++++++

|pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_deep

*Tutoriel*

* :ref:`l-deep-learning-specials`.
* `Artificial Intelligence, Revealed (1) <https://code.facebook.com/pages/1902086376686983>`_ : article de blog et vidéos
  expliquant les différents concepts du deep learning
* `colah's blog <http://colah.github.io/>`_ *(2016/08)* blog/cours sur le deep learning

*Sites*

* `Tinker With a Neural Network Right Here in Your Browser <http://playground.tensorflow.org/>`_
* `ConvNetJS <http://cs.stanford.edu/people/karpathy/convnetjs/>`_

*Modèles pré-entraînés*

* `Places CNN <http://places.csail.mit.edu/downloadCNN.html>`_,
  `Pre-release of Places365-CNNs <https://github.com/metalbubble/places365>`_
  (deep learning)
* `CNTK <https://www.microsoft.com/en-us/research/product/cognitive-toolkit/model-gallery/>`_
  (sur `github <https://github.com/Microsoft/CNTK/tree/master/Examples>`_)

*Lectures*

* `LightRNN: Memory and Computation-Efficient Recurrent Neural Networks <https://arxiv.org/abs/1610.09893>`_
* `Deep learning architecture diagrams <http://fastml.com/deep-learning-architecture-diagrams/>`_
* `Factorized Convolutional Neural Networks <https://arxiv.org/abs/1608.04337>`_
* `Deep Residual Learning for Image Recognition <https://arxiv.org/pdf/1512.03385v1.pdf>`_
* `Deep Learning <http://www-labs.iro.umontreal.ca/~bengioy/dlbook/>`_, Yoshua Bengio, Ian Goodfellow and Aaron Courville
* `LeNet5 <http://yann.lecun.com/exdb/lenet/>`_
* `mxnet <https://github.com/dmlc/mxnet>`_
* `Benchmarking State-of-the-Art Deep Learning Software Tools <http://arxiv.org/pdf/1608.07249v5.pdf>`_
* `Wide & Deep Learning: Better Together with TensorFlow <https://research.googleblog.com/2016/06/wide-deep-learning-better-together-with.html>`_,
  `Wide & Deep Learning for Recommender Systems <https://arxiv.org/pdf/1606.07792v1.pdf>`_
* `To go deep or wide in learning? <http://www.jmlr.org/proceedings/papers/v33/pandey14.pdf>`_
* `Three Classes of Deep Learning Architectures and Their Applications: A Tutorial Survey <https://www.microsoft.com/en-us/research/publication/three-classes-of-deep-learning-architectures-and-their-applications-a-tutorial-survey/>`_
* `Tutorial: Learning Deep Architectures <http://www.cs.toronto.edu/~rsalakhu/deeplearning/yoshua_icml2009.pdf>`_
* `Deep Learning <https://en.wikipedia.org/wiki/Deep_learning>`_ (wikipédia)
* `Fast R-CNN <https://arxiv.org/abs/1504.08083>`_ (voir `Object Detection using Fast R CNN <https://github.com/Microsoft/CNTK/wiki/Object-Detection-using-Fast-R-CNN>`_)
* `Evaluation of Deep Learning Toolkits <https://github.com/zer0n/deepframeworks/blob/master/README.md>`_ *(2015/12)*
* `Understanding Deep Learning Requires Rethinking Generalization <https://arxiv.org/pdf/1611.03530.pdf>`_
* `Training Deep Nets with Sublinear Memory Cost <https://arxiv.org/pdf/1604.06174.pdf>`_

*Chiffres, Textes*

* `One weird trick for parallelizing convolutional neural networks <https://arxiv.org/pdf/1404.5997v2.pdf>`_
* `ImageNet Classification with Deep Convolutional Neural Networks <https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf>`_
* `Very Deep Convolutional Networks for Large-Scale Image Recognition <https://arxiv.org/pdf/1409.1556v6.pdf>`_
* `Multi-Digit Recognition Using A Space Displacement Neural Network  <https://papers.nips.cc/paper/557-multi-digit-recognition-using-a-space-displacement-neural-network.pdf>`_
* `Space Displacement Localization Neural Networks to locate origin points of handwritten text lines in historical documents <http://liris.cnrs.fr/christian.wolf/papers/icdar-hip2015.pdf>`_
* `Neural Network Architectures <https://culurciello.github.io/tech/2016/06/04/nets.html>`_,
  `Convolutional Neural Networks (CNNs / ConvNets) <http://cs231n.github.io/convolutional-networks/#conv>`_
* `Transfer Learning <http://cs231n.github.io/transfer-learning/>`_

*Plus théoriques*

* `Why Does Unsupervized Deep Learning Work? - A perspective from group theory <https://arxiv.org/pdf/1412.6621v3.pdf>`_
* `Deep Learning of Representations: Looking Forward <https://arxiv.org/pdf/1305.0445v2.pdf>`_
* `Why Does Unsupervised Pre-training Help Deep Learning? <http://jmlr.org/papers/volume11/erhan10a/erhan10a.pdf>`_

*Lectures deep text*

* `Efficient Estimation of Word Representations in Vector Space <http://arxiv.org/abs/1301.3781>`_, Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean,
* `Distributed Representations of Words and Phrases and their Compositionality <http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf>`_, Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, Jeff Dean,
* `word2vec Parameter Learning Explained <http://arxiv.org/abs/1411.2738>`_, Xin Rong,
* `Tutorial on Auto-Encoders <http://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_, Piotr Mirowski

*Modules*

* `theano <http://deeplearning.net/software/theano/>`_
* `keras <https://keras.io/>`_
* `mxnet <https://github.com/dmlc/mxnet>`_
* `caffe <http://caffe.berkeleyvision.org/>`_ (`installation <http://caffe.berkeleyvision.org/installation.html>`_)
* `climin <http://climin.readthedocs.io/en/latest/rmsprop.html>`_ (algorithme de back propagation)
* `pytorch <http://pytorch.org/>`_ (Facebook)
* `tensorflow <https://www.tensorflow.org/>`_ (Google)

*à suivre*

* `chainer <https://github.com/pfnet/chainer>`_
* `platoon <https://github.com/mila-udem/platoon/>`_ :
  multi-GPU pour theano
* `scikit-theano <https://github.com/sklearn-theano/sklearn-theano>`_

.. _l-td2a-reinforcement-learning:

Reinforcement Learning
++++++++++++++++++++++

ou *apprentissage par renforcement*

|pystatpng|

*(année prochaine)*

*Lectures*

* `Deep	Reinforcement Learning through Policy Optmization <http://people.eecs.berkeley.edu/~pabbeel/nips-tutorial-policy-optimization-Schulman-Abbeel.pdf>`_
  (vu dans `Highlights of NIPS 2016: Adversarial learning, Meta-learning, and more <http://sebastianruder.com/highlights-nips-2016/index.html>`_)
* `The Nuts and Bolts of Deep RL Research <http://rll.berkeley.edu/deeprlcourse/docs/nuts-and-bolts.pdf>`_
* `A Comprehensive Survey on Safe Reinforcement Learning <http://www.jmlr.org/papers/volume16/garcia15a/garcia15a.pdf>`_
* `RLPy: A Value-Function-Based Reinforcement Learning Framework for Education and Research <http://www.jmlr.org/papers/volume16/geramifard15a/geramifard15a.pdf>`_
* `UCL Course on RL <http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html>`_
* `Reinforcement Learning Part I <http://www.labri.fr/perso/nrougier/downloads/Chile-2014-Lecture-1.pdf>`_
  `Reinforcement Learning Part II <http://www.labri.fr/perso/nrougier/downloads/Chile-2014-Lecture-2.pdf>`_
* `Strategic Attentive Writer for Learning Macro-Actions <https://arxiv.org/pdf/1606.04695.pdf>`_

Bandits
+++++++

|pystatpng|

*(année prochaine)*

*Lectures*

* `Bandit theory, part I <http://blogs.princeton.edu/imabandit/2016/05/11/bandit-theory-part-i/>`_
* `Bandit theory, part II <http://blogs.princeton.edu/imabandit/2016/05/13/bandit-theory-part-ii/>`_
* `Kernel-based methods for bandit convex optimization, part 1 <http://blogs.princeton.edu/imabandit/2016/08/06/kernel-based-methods-for-bandit-convex-optimization-part-1/>`_
* `Kernel-based methods for bandit convex optimization, part 2 <http://blogs.princeton.edu/imabandit/2016/08/09/kernel-based-methods-for-convex-bandits-part-2/>`_
* `Kernel-based methods for bandit convex optimization, part 3 <http://blogs.princeton.edu/imabandit/2016/08/10/kernel-based-methods-for-convex-bandits-part-3/>`_
* `Learning to Interact <http://hunch.net/~jl/interact.pdf>`_ (John Langford)
* `Batch Learning from Logged Bandit Feedback through Counterfactual Risk Minimization <http://www.jmlr.org/papers/volume16/swaminathan15a/swaminathan15a.pdf>`_
* `Stochastic Structured Prediction under Bandit Feedback <https://papers.nips.cc/paper/6134-stochastic-structured-prediction-under-bandit-feedback.pdf>`_

Modèles bayésiens
+++++++++++++++++

|pystatpng|

*(année prochaine)*

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_bayes

*Lectures*

* `A Bayesian Approximation Method for Online Ranking <http://jmlr.csail.mit.edu/papers/volume12/weng11a/weng11a.pdf>`_
* `stan case studies <http://mc-stan.org/documentation/case-studies>`_
* `Edward: A library for probabilistic modeling, inference, and criticism <https://arxiv.org/pdf/1610.09787.pdf>`_

*Vidéo*

* `Variational Inference in Python <https://www.youtube.com/watch?v=3KGZDC3-_iY>`_
* `Bayesian Network Modeling using R and Python <https://www.youtube.com/watch?v=iRvXfx9IWM0>`_

*Modules*

* `edward <http://edwardlib.org/>`_
* `PyMC3 <https://pymc-devs.github.io/pymc3/notebooks/getting_started.html>`_
* `bayespy <http://bayespy.org/en/latest/>`_
* `kabuki <https://pypi.python.org/pypi/kabuki/>`_

Factorization Machines
++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Factorization Machines with libFM <http://www.csie.ntu.edu.tw/~b97053/paper/Factorization%20Machines%20with%20libFM.pdf>`_ *(2016/09)*
* `Stochastic Subsampling for Factorizing Huge Matrices <https://hal.archives-ouvertes.fr/hal-01431618>`_

------------

Machine Learning Avancé
=======================

.. contents::
    :local:
    :depth: 1

Régression quantile
+++++++++++++++++++

(*à venir*)

*Lectures*

* `La régression quantile en pratique <https://www.insee.fr/fr/statistiques/fichier/1381107/doc_regression_quantile.pdf>`_
* `Extensions of the Markov chain marginal bootstrap <https://www.researchgate.net/publication/23635751_Extensions_of_the_Markov_chain_marginal_bootstrap>`_
* `Iteratively reweighted least squares <https://en.wikipedia.org/wiki/Iteratively_reweighted_least_squares>`_

*Modules*

* `statsmodels <http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.quantile_regression.QuantReg.html>`_

Interprétabilité des modèles
++++++++++++++++++++++++++++

|pyecopng| |pystatpng|

*(à venir)*

*Lectures*

* `Learning to learn by gradient descent by gradient descent <https://arxiv.org/pdf/1606.04474.pdf>`_
* `Importance Weighting Without Importance Weights: An Effcient Algorithm for Combinatorial Semi-Bandits <http://jmlr.org/papers/volume17/15-091/15-091.pdf>`_
* `Making Tree Ensembles Interpretable <https://arxiv.org/pdf/1606.05390v1.pdf>`_
* `Understanding variable importances in forests of randomized trees <http://papers.nips.cc/paper/4928-understanding-variable-importances-in-forests-of-randomized-trees.pdf>`_
* `Confidence Intervals for Random Forests: The Jackknife and the Infinitesimal Jackknife <http://jmlr.csail.mit.edu/papers/volume15/wager14a/wager14a.pdf>`_
* `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_
* `Wavelet decompositions of Random Forests - smoothness analysis, sparse approximation and applications <http://www.jmlr.org/papers/volume17/15-203/15-203.pdf>`_
* `"Why Should I Trust You?" Explaining the Predictions of Any Classifier <http://arxiv.org/pdf/1602.04938v1.pdf>`_ *(2016/06)*
* `Edward: A library for probabilistic modeling, inference, and criticism <https://arxiv.org/pdf/1610.09787.pdf>`_
* `Strictly Proper Scoring Rules, Prediction, and Estimation <https://www.cs.duke.edu/courses/spring17/compsci590.2/Gneiting2007jasa.pdf>`_

*Modules*

* `edward <http://edwardlib.org/>`_

Optimisation des hyperparamètres
++++++++++++++++++++++++++++++++

(à venir)

*Lectures*

* `Algorithms for Hyper-Parameter Optimization <https://papers.nips.cc/paper/4443-algorithms-for-hyper-parameter-optimization.pdf>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/>`_
* `hyperopt <https://github.com/hyperopt/hyperopt>`_

Online training
+++++++++++++++

*(à venir)*

*Lectures*

* `Fast Rates in Statistical and Online Learning <http://www.jmlr.org/papers/volume16/vanerven15a/vanerven15a.pdf>`_

Modèles avec dépendances dans le temps
++++++++++++++++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Learning Algorithms for Second-Price Auctions with Reserve <http://www.jmlr.org/papers/volume17/14-499/14-499.pdf>`_
* `Machine Learning in an Auction Environment <http://www.jmlr.org/papers/volume17/15-109/15-109.pdf>`_

Timeseries - Séries temporelles
+++++++++++++++++++++++++++++++

|pyecopng| |pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_timeseries

*Lectures*

* `Time series analysis with pandas <http://earthpy.org/pandas-basics.html>`_
* `Consistent Algorithms for Clustering Time Series <http://www.jmlr.org/papers/volume17/khaleghi16a/khaleghi16a.pdf>`_
* `Learning Time Series Detection Models from Temporally Imprecise Labels <https://arxiv.org/abs/1611.02258>`_
* `Time Series Prediction With Deep Learning in Keras <http://machinelearningmastery.com/time-series-prediction-with-deep-learning-in-python-with-keras/>`_
* `Sequence Classification with LSTM Recurrent Neural Networks in Python with Keras <http://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/>`_
* `Time Series Classification and Clustering with Python <http://alexminnaar.com/time-series-classification-and-clustering-with-python.html>`_
* `Dynamic Time Warping <https://en.wikipedia.org/wiki/Dynamic_time_warping>`_
* `Functional responses, functional covariates and the concurrent model <http://www.ece.uvic.ca/~bctill/papers/mocap/Ramsay_Silverman_2005ao.pdf>`_

*Modules*

* `statsmodels <http://statsmodels.sourceforge.net/>`_

Auto-Learning
+++++++++++++

|pyecopng| |pystatpng|

*(à venir)*

* `Angluin Algorithm <https://web.archive.org/web/20131202232143/http://www.cse.iitk.ac.in/users/chitti/thesis/references/learningRegSetsFromQueriesAndCounterExamples.pdf>`_

*Lectures*

* `Learning to learn by gradient descent by gradient descent <https://papers.nips.cc/paper/6461-learning-to-learn-by-gradient-descent-by-gradient-descent.pdf>`_
* `Matching Networks for One Shot Learning <https://papers.nips.cc/paper/6385-matching-networks-for-one-shot-learning.pdf>`_
* `Efficient and Robust Automated Machine Learning <http://papers.nips.cc/paper/5872-efficient-and-robust-automated-machine-learning.pdf>`_
* `Learning Regular Sets from Queries and Counterexamples <https://web.archive.org/web/20131202232143/http://www.cse.iitk.ac.in/users/chitti/thesis/references/learningRegSetsFromQueriesAndCounterExamples.pdf>`_

*Modules*

* `REP <https://github.com/yandex/rep>`_
* `TPOT <https://github.com/rhiever/tpot>`_
* `auto-sklearn <https://github.com/automl/auto-sklearn/>`_

Machine Learning sur des données cryptées
+++++++++++++++++++++++++++++++++++++++++

|pystatpng|

*(à venir)*

*Lectures*

* `Privacy Preserving Data Mining <http://web.stanford.edu/group/mmds/slides/mcsherry-mmds.pdf>`_, Cynthia Dwork, Frank McSherry,
  concept de :math:`\epsilon`-differential privacy
  (`version longue <https://users.soe.ucsc.edu/~abadi/CS223_F12/mcsherry.pdf>`_,
  `Privacy Preserving Data Mining <http://www.cs.jhu.edu/~fabian/courses/CS600.624/slides/privacy-preserving.pdf>`_)
* `Differentially Private Empirical Risk Minimization <http://www.jmlr.org/papers/volume12/chaudhuri11a/chaudhuri11a.pdf>`_
* `Preserving Privacy of Continuous High-dimensional Data with Minimax Filters <http://www.jmlr.org/proceedings/papers/v38/hamm15.pdf>`_
* `Differentially Private Online Learning <http://www.jmlr.org/proceedings/papers/v23/jain12/jain12.pdf>`_
* `A Differentially Private Stochastic Gradient Descent Algorithm for Multiparty Classification <http://www.jmlr.org/proceedings/papers/v22/rajkumar12/rajkumar12.pdf>`_
* `Privacy for Free: Posterior Sampling and Stochastic Gradient Monte Carlo <http://www.jmlr.org/proceedings/papers/v37/wangg15.pdf>`_
* `Machine Learning Classification over Encrypted Data <https://eprint.iacr.org/2014/331.pdf>`_
* `CryptoNets: Applying Neural Networks to Encrypted Data with High Throughput and Accuracy <http://jmlr.org/proceedings/papers/v48/gilad-bachrach16.pdf>`_
* `Compressed Sensing <https://en.wikipedia.org/wiki/Compressed_sensing>`_

*Modules*

* `ciphermed <https://github.com/rbost/ciphermed>`_ : pas maintenu

Prédire une distribution
++++++++++++++++++++++++

|pystatpng|

*(à venir)*

*Lectures*

* `Learning with a Wasserstein Loss <https://arxiv.org/pdf/1506.05439.pdf>`_

------------

NLP - Image - Réseaux
=====================

.. contents::
    :local:
    :depth: 1

.. _l-td2a-nlp:

Traitement du langage
+++++++++++++++++++++

|pyecopng| |pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_nlp

*Lectures*

* `Système de complétion <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_nlp/completion.html>`_ :
  la complétion est utilisée par tous les sites Internet pour aider les utilisateurs
  à saisir leur recherche. N'importe quel site commercial l'utiliser
  pour guider les utilisateurs plus rapidement vers le produit qu'ils recherchent.
* `Text Understanding from Scratch <https://arxiv.org/abs/1502.01710>`_, Xiang Zhang, Yann LeCun
* `Text Generation With LSTM Recurrent Neural Networks in Python with Keras <http://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/>`_
* `Dual Learning for Machine Translation <https://papers.nips.cc/paper/6469-dual-learning-for-machine-translation.pdf>`_
* `Supervised Word Mover's Distance <https://papers.nips.cc/paper/6139-supervised-word-movers-distance.pdf>`_
* `Probabilistic Context-Free Grammars (PCFGs) <http://www.cs.columbia.edu/~mcollins/courses/nlp2011/notes/pcfgs.pdf>`_
* `A Roundup of Recent Text Analytics and Vis Work <http://blogger.ghostweather.com/2014/10/a-roundup-of-recent-text-analytics-and.html>`_

* `A Joint Model for Entity Analysis: Coreference, Typing, and Linking <http://www.cs.utexas.edu/~gdurrett/papers/durrett-klein-tacl2014.pdf>`_
* `Disfluency Detection with a Semi-Markov Model and Prosodic Features <http://www.cs.utexas.edu/~gdurrett/papers/ferguson-durrett-klein-naacl2015.pdf>`_
* `Capturing Semantic Similarity for Entity Linking with Convolutional Neural Networks <http://www.cs.utexas.edu/~gdurrett/papers/mfl-durrett-klein-naacl2016.pdf>`_
* `Neural CRF Parsing <http://www.cs.utexas.edu/~gdurrett/papers/durrett-klein-acl2015.pdf>`_
* `Less Grammar More Features <http://www.cs.utexas.edu/~gdurrett/papers/hall-durrett-klein-acl2014.pdf>`_
* `Learning-Based Single-Document Summarization with Compression and Anaphoricity Constraints <https://arxiv.org/pdf/1603.08887v1.pdf>`_

*word2vec*

* `Towards a continuous modeling of natural language domains <http://www.aclweb.org/anthology/W/W16/W16-6012.pdf>`_
* `Efficient Estimation of Word Representations in Vector Space <http://arxiv.org/abs/1301.3781>`_, Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean,
  `Distributed Representations of Words and Phrases and their Compositionality <http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf>`_, Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, Jeff Dean,
  `word2vec Parameter Learning Explained <http://arxiv.org/abs/1411.2738>`_, Xin Rong,
  `Tutorial on Auto-Encoders <http://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_, Piotr Mirowski

*Word embedding*

* `On word embeddings - Part 1 <http://sebastianruder.com/word-embeddings-1/index.html>`_
* `On word embeddings - Part 2: Approximating the Softmax <http://sebastianruder.com/word-embeddings-softmax/index.html>`_
* `On word embeddings - Part 3: The secret ingredients of word2vec <http://sebastianruder.com/secret-word2vec/index.html>`_
* `From Word Embeddings To Document Distances <http://jmlr.org/proceedings/papers/v37/kusnerb15.pdf>`_

*Vidéos*

* `Modern NLP in Python <https://www.youtube.com/watch?v=6zm9NC9uRkk>`_

*Modules*

* `nltk <http://www.nltk.org/>`_
* `gensim <https://radimrehurek.com/gensim/>`_
* `spacy <https://spacy.io/>`_

Images
++++++

|pyecopng| |pystatpng|

(à venir)

*Lectures*

* `VIGRA <https://github.com/ukoethe/vigra>`_
* `opencv <http://opencv.org/>`_

Graphes et réseaux
++++++++++++++++++

|pyecopng| |pystatpng|

*(année prochaine)*

*Lectures*

* `Basic models and questions in statistical network analysis <https://arxiv.org/abs/1609.03511>`_
* `Trinity: A Distributed Graph Engine on a Memory Cloud <https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Trinity-1.pdf>`_
* `Dimensionality Reduction for Spectral Clustering <http://www.jmlr.org/proceedings/papers/v15/niu11a/niu11a.pdf>`_
* `Compressive Spectral Clustering <http://jmlr.org/proceedings/papers/v48/tremblay16.pdf>`_
* `Spectral Clustering on a Budget <http://www.jmlr.org/proceedings/papers/v15/shamir11a/shamir11a.pdf>`_
* `Partitioning Well-Clustered Graphs: Spectral Clustering Works! <http://www.jmlr.org/proceedings/papers/v40/Peng15.pdf>`_
* `Bipartite Correlation Clustering: Maximizing Agreements <http://www.jmlr.org/proceedings/papers/v51/asteris16.pdf>`_
* `Correlation Clustering and Biclustering with Locally Bounded Errors <http://jmlr.org/proceedings/papers/v48/puleo16.pdf>`_
* `A Unified Framework for Model-based Clustering <http://www.jmlr.org/papers/volume4/zhong03a/zhong03a.pdf>`_
* `A Tensor Approach to Learning Mixed Membership Community Models <http://jmlr.org/papers/volume15/anandkumar14a/anandkumar14a.pdf>`_
* `Local Network Community Detection with Continuous Optimization of Conductance and Weighted Kernel K-Means <http://jmlr.org/papers/volume17/16-043/16-043.pdf>`_
* `Learning Communities in the Presence of Errors <http://www.jmlr.org/proceedings/papers/v49/makarychev16.pdf>`_
* `Fast unfolding of communities in large networks <https://arxiv.org/abs/0803.0476>`_

------------

Techniques de programmation et algorithmes
==========================================

.. contents::
    :local:
    :depth: 2

.. _l-2a-scraping:

Webscrapping et API
+++++++++++++++++++

|pyecopng| |pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_eco_scraping
    notebooks/_gs2a_eco_api

*Ressources*

* `API de geocoding <https://www.data.gouv.fr/fr/faq/reuser/>`_
* `adresse.data.gouv.fr <https://adresse.data.gouv.fr/csv/>`_

*Modules*

* `beautifulsoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_
* `ghost.py <http://jeanphix.me/Ghost.py/>`_
* `selenium <http://selenium-python.readthedocs.io/>`_
* `scrapy <https://scrapy.org/>`_
* `scrapoxy <http://scrapoxy.io/>`_, `python api <https://github.com/fabienvauchelles/scrapoxy-python-api>`_

.. _l-eco-website:

Site web
++++++++

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_eco_website

*Lectures*

* `Python's Web Framework Benchmarks <http://klen.github.io/py-frameworks-bench/>`_

*Modules*

* `bottle <http://bottlepy.org/docs/dev/>`_
* `django <https://www.djangoproject.com/>`_
* `falcon <https://falconframework.org/>`_
* `Flask <http://flask.pocoo.org/>`_
* `sanic <https://github.com/channelcat/sanic>`_ + `uvloop <https://github.com/MagicStack/uvloop>`_

Jupyter et les commandes magiques
+++++++++++++++++++++++++++++++++

|pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_magic_commands

.. _l-cluster-non-struct-2a:

Big data sans cluster, données non structurées
++++++++++++++++++++++++++++++++++++++++++++++

|pystatpng|

* `présentation données structurées <http://www.xavierdupre.fr/enseignement/complements/cours_structure_donnee.pdf>`_

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_no_sql_exo
    notebooks/_gs2a_no_sql_twitter
    notebooks/_gs2a_big_in_memory

*Lectures*

- Propriétés des base de données : `ACID <http://fr.wikipedia.org/wiki/Propri%C3%A9t%C3%A9s_ACID>`_,
  `relationnelle <http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_relationnelle>`_,
  `transactionnelle <http://fr.wikipedia.org/wiki/Transaction_informatique>`_
- Best practices, index et `foreign key <http://en.wikipedia.org/wiki/Foreign_key>`_
  (importance des `random access <http://fr.wikipedia.org/wiki/Random_Access_Memories>`_ et `accès séquentiel <http://en.wikipedia.org/wiki/Sequential_access>`_)
- Limites des structures relationnelles
  (`données arborescentes <http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_hi%C3%A9rarchique>`_,
  données hétérogènes)
- Base de données non relationnelles dont `NoSQL <http://fr.wikipedia.org/wiki/NoSQL>`_
- :ref:`l-td25asynthese`
- `Un tools d'itertour, ou l'inverse <http://sametmax.com/un-tools-ditertour-ou-linverse/>`_
- `Benchmark of Python JSON libraries <http://artem.krylysov.com/blog/2015/09/29/benchmark-python-json-libraries/>`_

*Bases de données no SQL*

* `MongoDB <https://www.mongodb.com/>`_
* `rethinkdb <https://rethinkdb.com/>`_ (python : `rethinkdb <https://pypi.python.org/pypi/rethinkdb/>`_)

.. _l-2a-cplusplus-para-serie:

C++, R
++++++

|pystatpng|

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_langages
    notebooks/_gs1a_D_calcul_dicho_cython

*Lectures*

* :ref:`l-python_cplusplus`
* `sklearn-compiledtrees <https://github.com/ajtulloch/sklearn-compiledtrees/>`_ :
  création d'une implémentation C++ de la fonction de décision d'un arbre de décision entraîné avec
  scikit-learn

*Vidéos*

* `Making your code faster: Cython and parallel processing in the Jupyter Notebook <https://www.youtube.com/watch?v=MiHddLYZ6cQ>`_

Parallélisation, sérialisation
++++++++++++++++++++++++++++++

|pystatpng|

La sérialisation est le fait de convertir n'importe quelle structure de données en un
tableau d'octets, c'est indispensable pour la communication entre deux machines, deux processus.

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_parallelisation
    notebooks/_gs2a_serialisation

*Modules*

* `dask <http://dask.pydata.org/en/latest/>`_
* `cytoolz <https://github.com/pytoolz/cytoolz>`_
* `joblib <https://pythonhosted.org/joblib/>`_

*Lectures*

* `Out-of-Core Dataframes in Python: Dask and OpenStreetMap <https://jakevdp.github.io/blog/2015/08/14/out-of-core-dataframes-in-python/>`_ *(2015/12)*
* `Combining random forest models in scikit learn <http://stackoverflow.com/questions/28489667/combining-random-forest-models-in-scikit-learn>`_
* `Better Python compressed persistence in joblib <http://gael-varoquaux.info/programming/new_low-overhead_persistence_in_joblib_for_big_data.html>`_

.. _l-puzzlealgo2A:

Puzzles algorithmiques
++++++++++++++++++++++

|pystatpng|

.. toctree::

    td_2a_algo
    specials/nb_complet
    specials/algorithm_culture
    specials/problem_solved

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_puzzle

Certains sont tirés de plusieurs sites dont
`Google Code Jam <https://code.google.com/codejam/contests.html>`_.

*Lectures*

* `Profiling avec Python <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/completion_profiling.html?highlight=profiling>`_
* types de complexité : `force brute <http://fr.wikipedia.org/wiki/Recherche_exhaustive>`_,
  `glouton <http://fr.wikipedia.org/wiki/Algorithme_glouton>`_, `dynamique <http://fr.wikipedia.org/wiki/Programmation_dynamique>`_
* :ref:`l-algoculture`
* :ref:`l-expose-explication`
* `Logique, modèles, calculs (INF 423) <http://www.enseignement.polytechnique.fr/informatique/INF423/i.php?n=Main.Poly>`_
* `Notation de Landau <https://fr.wikipedia.org/wiki/Comparaison_asymptotique#La_famille_de_notations_de_Landau_O.2C_o.2C_.CE.A9.2C_.CF.89.2C_.CE.98.2C_.7E>`_
* `Edmonds' Blossom Algorithm <https://stanford.edu/~rezab/dao/projects_reports/shoemaker_vare.pdf>`_
  (`github <https://github.com/amyshoe/CME323-Project>`_),
  `Blossom5 <http://pub.ist.ac.at/~vnk/papers/blossom5.pdf>`_,
  `Fast and Simple Algorithms for Weighted Perfect Matching <http://e-collection.library.ethz.ch/eserv/eth:4711/eth-4711-01.pdf>`_
* `La recherche mathématique en mots et en images (CNRS) <http://images.math.cnrs.fr/>`_
* `The Traveling Salesperson Problem <http://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb>`_
* `Google Interview University <https://github.com/jwasham/google-interview-university#np-np-complete-and-approximation-algorithms>`_:
  *This is my multi-month study plan for going from web developer (self-taught, no CS degree) to Google software engineer.*
* `Cache replacement policies <https://en.wikipedia.org/wiki/Cache_replacement_policies>`_
* `Livres techniques en français <https://github.com/vhf/free-programming-books/blob/master/free-programming-books-fr.md>`_

Streaming algorithms
++++++++++++++++++++

(*à venir*)

* `Répartir train / test en streaming <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/split_train_test.html#streaming-splitting>`_

Plan

* Calcul d'une médiane
* Algorithme `BJKST <http://info.prelert.com/blog/hashing-and-approximate-distinct-value-counts>`_

*Lectures*

* `Streaming Algorithms <http://resources.mpi-inf.mpg.de/departments/d1/teaching/ss14/gitcs/notes3.pdf>`_
* `Data Stream Algorithms <http://www.cs.dartmouth.edu/~ac/Teach/CS85-Fall09/Notes/lecnotes.pdf>`_
* `Optimal streaming histograms <https://amplitude.com/blog/2014/08/06/optimal-streaming-histograms/>`_
* `Density Estimation Over Data Stream <http://alumni.cs.ucr.edu/~wli/publications/deosd.pdf>`_
* `Data Streaming Algorithms <http://www.cs.dartmouth.edu/~ac/Teach/CS49-Fall11/Notes/lecnotes.pdf>`_
* `Confidence Decision Trees via Online and Active Learning for Streaming (BIG) Data <https://arxiv.org/pdf/1604.03278.pdf>`_
* `Approximation and Streaming Algorithms for Histogram Construction Problems <http://www.mathcs.emory.edu/~cheung/papers/StreamDB/Histogram/2005-Guha-Histogram.pdf>`_
* `State-of-the-art on clustering data streams <https://bdataanalytics.biomedcentral.com/articles/10.1186/s41044-016-0011-3>`_
* `Parallel Computing of Kernel Density Estimates with MPI <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.102.5195&rep=rep1&type=pdf>`_
* `Density Estimation with Adaptive Sparse Grids for Large Data Sets <http://web.mit.edu/pehersto/www/preprints/sgde_siam.pdf>`_

*Modules*

* `StreamLib <https://github.com/jiecchen/StreamLib>`_

------------

Data Scientist en liberté
=========================

Contrairement à ce qu'on pense, les datascientists sont plus prévisibles que les données.

*machine learning*

* :ref:`l-debutermlprojet`
* `Sous le capot de la boîte noire <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/index.html#mlstatpy>`_
* `Quick samples on machine learning <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/mlexamples.html>`_
* `Cheat Sheets <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/cheat_sheets.html>`_
* `Gros volumes et sqllite3 <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/_gs5_sql_big_data.html>`_
* C'est quoi déjà le `True False Positive <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html>`_ ?

*quoi d'autres ?*

* `Gerry Mandering <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/_gs_gerrymandering.html>`_ (bidouillage de cartes électorales)
* `Apprendre des synonymes <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/_gs7_synonyme.html>`_
* `Revue de compétition Kaggle <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/ensae201611.html>`_

*installation*

* `Anaconda <https://www.continuum.io/downloads>`_ + ``conda update all`` + ``pip install jyquickhelper``
* `XGBoost sous Windows <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2016/2016-08-09_xgboost_again.html>`_

.. _l-td2a-biblio:

------------

Bibliographie
=============

**Livres sur le machine learning**

* `The Elements of Statistical Learning <http://statweb.stanford.edu/~tibs/ElemStatLearn/>`_, Trevor Hastie, Robert Tibshirani, Jerome Friedman
* `Python for Data Analysis <http://shop.oreilly.com/product/0636920023784.do>`_, Wes McKinney
* `Building Machine Learning Systems with Python <https://www.packtpub.com/big-data-and-business-intelligence/building-machine-learning-systems-python>`_, Willi Richert, Luis Pedro Coelho
* `Learning scikit-learn: Machine Learning in Python <https://www.packtpub.com/big-data-and-business-intelligence/learning-scikit-learn-machine-learning-python>`_, Raúl Garreta, Guillermo Moncecchi
* `Modeling Creativity: Case Studies in Python <http://arxiv.org/abs/1410.0281>`_, Tom De Smedt
* `Critical Mass: How One Thing Leads to Another <http://www.philipball.co.uk/index.php?option=com_content&view=article&id=15:critical-mass-how-one-thing-leads-to-another&catid=3:books&Itemid=4>`_, Philip Ball
* `Bugra Akyildiz <http://bugra.github.io/>`_
* `Deep Learning <http://www-labs.iro.umontreal.ca/~bengioy/dlbook/>`_, Yoshua Bengio, Ian Goodfellow and Aaron Courville
* `Artificial Intelligence: A Modern Approach <http://aima.cs.berkeley.edu/>`_, Stuart Russell, Peter Norvig *(2016/08)*
* `Speech and Language Processing <http://www.cs.colorado.edu/~martin/slp.html>`_,  Daniel Jurafsky and James H. Martin *(2016/08)*,
  see also `Draft chapters in progress <https://web.stanford.edu/~jurafsky/slp3/>`_

**Livres sur les algorithmes**

* `Introduction to Algorithms <http://mitpress.mit.edu/books/introduction-algorithms>`_, Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein
* `The Algorithm Design Manual <http://www.algorist.com/>`_, Steven S. Skiena
* `Competitive Programming <http://www.comp.nus.edu.sg/~stevenha/myteaching/competitive_programming/cp1.pdf>`_, Steven Halim

**Livres sur la programmation**

* `High Performance Python <http://shop.oreilly.com/product/0636920028963.do>`_, Micha Gorelick, Ian Ozsvald.
   Le livre est très bien conçu et les exemples sont très clairs. Si vous souhaitez accélérer un programme Python
   en utilisant le multithreading, `OpenMP <http://openmp.org/wp/>`_,
   `Numba <http://numba.pydata.org/>`_, `Cython <http://cython.org/>`_
   `PyPy <http://cython.org/>`_, ou `CPython <https://en.wikipedia.org/wiki/CPython>`_,
   je recommande d'y jeter un coup d'oeil d'abord.

**Liens sur la programmation**

* `Python Scientific Lecture Notes <http://scipy-lectures.github.io/>`_
* `Introduction to matplotlib <https://scipy-lectures.github.io/intro/matplotlib/matplotlib.html>`_
* `Introduction to Data Processing with Python <http://opentechschool.github.io/python-data-intro/>`_
* Quelques idées de livres : `Python for Data Scientists <https://www.packtpub.com/books/content/python-data-scientists>`_
* `Ultimate guide for Data Exploration in Python using NumPy, Matplotlib and Pandas <http://www.analyticsvidhya.com/blog/2015/04/comprehensive-guide-data-exploration-sas-using-python-numpy-scipy-matplotlib-pandas/#One>`_
* `Don't use Hadoop - your data isn't that big <http://www.chrisstucchio.com/blog/2013/hadoop_hatred.html>`_
* `Prédire les épidémies avec Wikipedia <http://www.lemonde.fr/sante/article/2014/11/13/predire-les-epidemies-avec-wikipedia_4523461_1651302.html>`_, Le Monde
* `FastML <http://fastml.com/>`_  (blog sur le machine learning)
* `Mathematical optimization: finding minima of functions <http://scipy-lectures.github.io/advanced/mathematical_optimization/index.html>`_
* `you can take the derivative of a regular expression?! <http://jvns.ca/blog/2016/04/25/how-regular-expressions-go-fast/>`_ *(2016/06)*
* `How to trick a neural network into thinking a panda is a vulture <https://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture>`_ *(2016/06)*
* `Matrix Factorization: A Simple Tutorial and Implementation in Python <http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/>`_ *(2016/06)*
* `Top-down learning path: Machine Learning for Software Engineers <https://github.com/ZuzooVn/machine-learning-for-software-engineers>`_

**Tutoriels**

* `PyData Seattle 2015 Scikit-learn Tutorial <https://github.com/jakevdp/sklearn_pydata2015>`_ *(2015/12)*
* `Pythonic Perambulations <https://jakevdp.github.io/>`_ *(2015/12)*
* `Python Scripts posted on Kaggle <https://www.kaggle.com/scripts?language=Python>`_ *(2016/02)*
* `Pandas cookbook <https://github.com/jvns/pandas-cookbook>`_ *(2016/06)*
* `Machine Learning & Deep Learning Tutorials <https://github.com/ujjwalkarn/Machine-Learning-Tutorials>`_ *(2016/06)* :
  lien vers une liste assez longue de tutoriels, on y trouve aussi des *cheat sheets* comme
  `Probability Cheatsheet <http://static1.squarespace.com/static/54bf3241e4b0f0d81bf7ff36/t/55e9494fe4b011aed10e48e5/1441352015658/probability_cheatsheet.pdf>`_

**MOOC**

* `Machine Learning par Andrew Y. Ng <https://www.class-central.com/mooc/835/coursera-machine-learning>`_
  (les chapitres X et XI de la semaine 6 aborde la construction d'un système de machine learning).
* `Coursera Machine Learning <https://www.coursera.org/course/ml>`_
* `Coursera Machine Algorithm <https://www.coursera.org/course/algo>`_
* `CSE373 - Analysis of Algorithms - 2007 SBU <https://www.youtube.com/playlist?list=PL5F43156F3F22C349>`_
* `CS109 Data Science (Harvard) <http://cs109.github.io/2014/>`_ (la liste des vidéos disponibles est en bas)

**Autres cours, notebooks**

* `CS109 Data Science (Harvard) <http://cs109.github.io/2014/>`_ -
  `TD <https://github.com/cs109/content>`_ -
  `Talks <http://cm.dce.harvard.edu/2015/01/14328/publicationListing.shtml>`_
* `Notes and assignments for Stanford CS class CS231n <https://github.com/cs231n/cs231n.github.io>`_
  `Convolutional Neural Networks for Visual Recognition <http://vision.stanford.edu/teaching/cs231n/>`_
* `Advanced Statistical Computing, Chris Fonnesbeck (Vanderbilt University) <http://nbviewer.jupyter.org/github/fonnesbeck/Bios366/tree/master/notebooks/>`_
* `CS 188: Artificial Intelligence (Berkeley) <http://inst.eecs.berkeley.edu/~cs188/fa10/lectures.html>`_
* `IAPR: Teaching materials for machine learning <http://homepages.inf.ed.ac.uk/rbf/IAPR/researchers/MLPAGES/mlteach.htm>`_
* machine learning et musique `Audio Content Analysis, teachings <http://www.audiocontentanalysis.org/teaching/>`_
* `ogrisel's notebook <https://github.com/ogrisel/notebooks>`_ (2016/04)
* `L'apprentissage profond <https://www.college-de-france.fr/site/yann-lecun/course-2015-2016.htm>`_, Yann LeCun au Collège de France *(2016/06)*
* `MA 2823 Foundations of Machine Learning (Fall 2016) <http://cazencott.info/index.php/pages/MA-2823-Foundations-of-Machine-Learning-%28Fall-2016%29>`_ *(2016/10)*

**Articles d'auteurs très connus**

* `Latent Dirichlet Allocation <http://ai.stanford.edu/~ang/papers/jair03-lda.pdf>`_, David M. Blei, Andrew Y. Ng, Michael I. Jordan
* `Analysis of a Random Forests Model <http://www.jmlr.org/papers/volume13/biau12a/biau12a.pdf>`_, Gerard Biau
* `Adaptivity of Averaged Stochastic Gradient Descent to Local Strong Convexity for Logistic Regression <http://jmlr.csail.mit.edu/papers/volume15/bach14a/bach14a.pdf>`_, Francis Bach
* `Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising <http://jmlr.csail.mit.edu/papers/volume14/bottou13a/bottou13a.pdf>`_, Léon Bottou, Jonas Peter et Al.
* `Tutorial on Practical Prediction Theory for Classification <http://www.jmlr.org/papers/volume6/langford05a/langford05a.pdf>`_, John Langford
* `Sparse Online Learning via Truncated Gradient <http://jmlr.org/papers/volume10/langford09a/langford09a.pdf>`_, John Langford, Lihong Li, Tong Zhang
* `Low-dimensional Embeddings for Interpretable Anchor-based Topic Inference <http://mimno.infosci.cornell.edu/papers/EMNLP2014138.pdf>`_, Moontae Lee, David Mimno
* `ABC model choice via random forests <http://arxiv.org/abs/1406.6288>`_, Pierre Pudlo, Jean-Michel Marin, Arnaud Estoup, Jean-Marie Cornuet, Mathieu Gautier, Christian P. Robert
* `Mondrian Forests: Efficient Online Random Forests <http://arxiv.org/pdf/1406.2673v1.pdf>`_, Balaji Lakshminarayanan, Daniel M. Roy, Yee Whye Teh
* `Stochastic Gradient Tricks <http://leon.bottou.org/papers/bottou-tricks-2012>`_
* `SiGMa: Simple Greedy Matching for Aligning Large Knowledge Bases <http://arxiv.org/abs/1207.4525>`_, Simon Lacoste-Julien, Konstantina Palla, Alex Davies, Gjergji Kasneci, Thore Graepel, Zoubin Ghahramani
* `Learning from Partial Labels <http://www.seas.upenn.edu/~taskar/pubs/partial_labels_jmlr11.pdf>`_, Timothee Cour, Benjamin Sapp, Ben Taskar
* `Word Alignment via Quadratic Assignment <http://www.seas.upenn.edu/~taskar/pubs/naacl06_qap.pdf>`_, Simon Lacoste-Julien, Ben Taskar, Dan Klein, Michael I. Jordan
* `Contextual Bandit Learning with Predictable Rewards <http://arxiv.org/abs/1202.1334>`_, Alekh Agarwal, Miroslav Dudík, Satyen Kale, John Langford, Robert E. Schapire
* `Learning from Logged Implicit Exploration Data <http://papers.nips.cc/paper/3977-learning-from-logged-implicit-exploration-data>`_, Alex Strehl, John Langford, Lihong LiSham, M. Kakade
* `The Metropolis-Hastings algorithm <http://arxiv.org/abs/1504.01896>`_, Christian P. Robert
* `From RankNet to LambdaRank to LambdaMART: An Overview <http://research.microsoft.com/pubs/132652/MSR-TR-2010-82.pdf>`_, Christopher J.C. Burges

**Compétition de code**

* `Google Hash Code <https://hashcode.withgoogle.com/>`_, a lieu chaque année en deux tours, le second tour a lieu chez Google à Paris.
* `Google Code Jam <https://code.google.com/codejam>`_
* `TopCoder <http://www.topcoder.com/>`_
* `UVa Online Judge <http://uva.onlinejudge.org/>`_
* `Le problème des huit reines <http://zanotti.univ-tln.fr/algo/REINES.html>`_
* `Projet Euler <https://projecteuler.net/>`_

Pour finir, `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_ :

.. image:: http://scikit-learn.org/stable/_static/ml_map.png
    :width: 500

**Librairies Python**

* `Simple/limited/incomplete benchmark for scalability, speed and accuracy of machine learning libraries for classification <https://github.com/szilard/benchm-ml>`_
* `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
* `Related Projects (of machine learning) <http://scikit-learn.org/stable/related_projects.html>`_ (2016/03)

**Librairies de machine learning**

* `Awesome Machine Learning <https://github.com/josephmisiti/awesome-machine-learning#python>`_
* `CNTK <https://github.com/Microsoft/CNTK>`_ (2016/04)
* `Keras <http://keras.io/>`_
* `scikit-learn <http://scikit-learn.org/stable/index.html>`_
* `TensorFlow <https://github.com/tensorflow/tensorflow>`_
* `theano <http://deeplearning.net/software/theano/>`_
* `Vowpal Wabbit <https://github.com/JohnLangford/vowpal_wabbit/wiki>`_
* `xgboost <https://github.com/dmlc/xgboost>`_

**Vidéos**

* `Beyond Bag of Words A Practitioner’s Guide to Advanced NLP <https://www.youtube.com/watch?v=YWzFxRZPEyU>`_
* `Building Continuous Learning Systems <https://www.youtube.com/watch?v=VtBvmrmMJaI>`_

.. [#fwrite1] Contributeur, encadrant et coordinateur du cours.

.. [#fwrite2] Contributeur, encadrant.
