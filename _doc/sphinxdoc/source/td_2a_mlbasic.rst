
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

.. |pyecopng| image:: _static/pyeco.png
            :height: 20
            :alt: Economie
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: _static/pystat.png
            :height: 20
            :alt: Statistique
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

-----------------------

Statistiques Descriptives
=========================

.. contents::
    :local:
    :depth: 1

ACP, ACM, ANOVA
+++++++++++++++

(*à venir*)

*Lectures*

* `Probabilités, analyse des données et statistique <http://www.editionstechnip.com/fr/catalogue-detail/149/probabilites-analyse-des-donnees-et-statistique.html>`_ (Gilbert Saporta)

*Modules*

* `scipy <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html>`_ (ANOVA)
  `scipy.stats.mstats <https://docs.scipy.org/doc/scipy/reference/stats.mstats.html>`_
* `scikit-learn <http://scikit-learn.org/>`_
* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `fbpca <http://fbpca.readthedocs.io/en/latest/>`_ : ACP
* `prince <https://github.com/MaxHalford/Prince>`_ : ACM
* `scikit-gof <https://github.com/wrwrwr/scikit-gof>`_

Intervalles de confiance
++++++++++++++++++++++++

(*à venir*)

*Modules*

* `bootstrap_contrast <https://github.com/josesho/bootstrap_contrast>`_,
  propose des graphes montrant ces intervalles de confiance

----------------------

Transformations des données, Embedding
======================================

.. contents::
    :local:
    :depth: 1

Construire un `embedding <https://en.wikipedia.org/wiki/Embedding>`_ consiste le plus
souvent à construire une fonction qui convertit un entier, un graphe, un texte en
un vecteur réel de dimension fixe exploitable par un modèle de machine learning.
Cette partie s'intéresse à construire de meilleures variables que celles issues
du problème initiale.

|pyecopng| |pystatpng|

Projections, Réduction des dimensions
+++++++++++++++++++++++++++++++++++++

(à venir)

* PCA, Sparse PCA, Kernel PCA
* SOM
* LSH

*Lectures*

* `PCA <http://scikit-learn.org/stable/modules/decomposition.html>`_
* `Johnson–Lindenstrauss lemma <https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma>`_,
  `Random projection <http://scikit-learn.org/stable/modules/random_projection.html>`_,
  `Concentration of measure <https://en.wikipedia.org/wiki/Concentration_of_measure>`_,
  `Experiments with Random Projection <http://cseweb.ucsd.edu/~dasgupta/papers/randomf.pdf>`_
* `Compressed sensing and single-pixel cameras <https://terrytao.wordpress.com/2007/04/13/compressed-sensing-and-single-pixel-cameras/>`_
  (wikipedia : `Compressed Sensing <https://en.wikipedia.org/wiki/Compressed_sensing>`_)
* `Locality-sensitive hashing <https://en.wikipedia.org/wiki/Locality-sensitive_hashing>`_,
  `LSH Forest: Self-Tuning Indexes for Similarity Search <http://infolab.stanford.edu/~bawa/Pub/similarity.pdf>`_
* `Manifold learning <http://scikit-learn.org/stable/modules/manifold.html>`_
* `Cartes de Kohonen <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_clus/kohonen.html>`_
* `Dynamic Self-Organising Map <http://www.labri.fr/perso/nrougier/coding/article/article.html>`_
* `Fast Randomized SVD <https://research.fb.com/fast-randomized-svd/>`_
* `Neural Autoregressive Distribution Estimation <http://www.jmlr.org/papers/volume17/16-272/16-272.pdf>`_
* `How to Use t-SNE Effectively <http://distill.pub/2016/misread-tsne/>`_
* `Practical and Optimal LSH for Angular Distance <https://arxiv.org/abs/1509.02897>`_
* `Optimal Data-Dependent Hashing for Approximate Near Neighbors <https://arxiv.org/abs/1501.01062>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/>`_
* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `fbpca <http://fbpca.readthedocs.io/en/latest/>`_ : ACP
* `prince <https://github.com/MaxHalford/Prince>`_ : ACM
* `Parametric-t-SNE <https://github.com/kylemcdonald/Parametric-t-SNE/blob/master/Parametric%20t-SNE%20(Keras).ipynb>`_
* `datasketch <https://github.com/ekzhu/datasketch>`_ (LSH)
* `NearPy <https://github.com/pixelogik/NearPy>`_ (LSH)

*Animations*

* `How to Use t-SNE Effectively <http://distill.pub/2016/misread-tsne/>`_

|pyecopng| |pystatpng|

Variables catégorielles
+++++++++++++++++++++++

(à venir)

* Corrélation entre des variables catégorielles

*Lectures*

* :ref:`Tranformer les variables catégorielles et contrastes <encoding-categorie-id>`
* `Corrélations entre des variables catégorielles <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/correlation_non_lineaire.html>`_
* `Exemple de traitement d'une variable catégorielle <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/solution_2017.html#solution2017rst>`_
* `Enoncé d'examan autour des variables catégorielles <http://www.xavierdupre.fr/site2013/enseignements/tdnoteseul/td_note_2017.pdf>`_
  et sa :ref:`corection <tdnote2017rs>`
* `Visiting: Categorical Features and Encoding in Decision Trees <https://medium.com/data-design/visiting-categorical-features-and-encoding-in-decision-trees-53400fa65931>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/>`_
* `category_encoders <http://contrib.scikit-learn.org/categorical-encoding/>`_

Distances
+++++++++

(à venir)

|pystatpng|

*Lectures*

* `Learning Hierarchical Similarity Metrics <http://www.cs.toronto.edu/~vnair/cvpr12.pdf>`_
* `From Word Embeddings To Document Distances <http://jmlr.org/proceedings/papers/v37/kusnerb15.pdf>`_
* `Detecting Near-Duplicates for Web Crawling <http://www.wwwconference.org/www2007/papers/paper215.pdf>`_
* `Deep metric learning using Triplet network <https://arxiv.org/abs/1412.6622>`_

|pyecopng| |pystatpng|

Clustering
++++++++++

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_clustering

(à venir)

* score silhouette
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
* `Scalable Density-Based Clustering with Quality Guarantees using Random Projections <http://alumni.cs.ucr.edu/~mvlachos/erc/projects/density-based/paper.pdf>`_
* `Clustering Via Decision Tree Construction <http://web.cs.ucla.edu/~wwc/course/cs245a/CLTrees.pdf>`_
  (implémentation en python `dimitrs/CLTree <https://github.com/dimitrs/CLTree>`_)
* `Spectral Clustering Based on Local PCA <http://www.jmlr.org/papers/volume18/14-318/14-318.pdf>`_
* `Brown clustering <https://en.wikipedia.org/wiki/Brown_clustering>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/>`_
* `hdbscan <https://github.com/scikit-learn-contrib/hdbscan>`_
* `pyclustering <https://pypi.python.org/pypi/pyclustering>`_
* `pycluster <https://pypi.python.org/pypi/pycluster>`_

|pyecopng| |pystatpng|

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

|pyecopng| |pystatpng|

Graphe et embedding
+++++++++++++++++++

*(à venir)*

*Lectures*

* `Graph Convolutional Networks <https://tkipf.github.io/graph-convolutional-networks/>`_
* `Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering <https://arxiv.org/abs/1606.09375>`_
* `Deep Convolutional Networks on Graph-Structured Data <https://arxiv.org/abs/1506.05163>`_

|pyecopng| |pystatpng|

Text embedding
++++++++++++++

Voir :ref:`l-td2a-nlp`.

|pyecopng| |pystatpng|

Valeurs manquantes
++++++++++++++++++

.. index:: valeurs manquantes

Les valeurs manquantes sont rarement l'objectif final
d'un système de prédiction mais elles sont souvent sur le chemin.
Pourquoi leur consacrer un chapitre alors qu'il paraît si facile
de les remplacer par la moyenne ? Pourquoi ne pas chercher à
les prédire puisqu'il s'agit d'utiliser une valeur appropriée à la
place de quelque chose qu'on ne connaît ? Les mots-clés importants :
*imputation*, *MICE*, *Amelia*.

*(à venir)*

*Lectures*

* `Missing Data <https://en.wikipedia.org/wiki/Missing_data>`_
* `Imputation de données manquantes <https://www.math.univ-toulouse.fr/~besse/Wikistat/pdf/st-m-app-idm.pdf>`_
* `Missing Data & How to Deal: An overview of missing data <https://liberalarts.utexas.edu/prc/_files/cs/Missing-Data.pdf>`_
* `Additive Non-negative Matrix Factorization for Missing Data <https://arxiv.org/abs/1007.0380>`
* `Scalable Tensor Factorizations for Incomplete Data <https://arxiv.org/pdf/1005.2197.pdf>`_
* `Missing-data imputation <http://www.stat.columbia.edu/~gelman/arm/missing.pdf>`_
* `Check your missing-data imputations using cross-validation <http://andrewgelman.com/2012/03/18/check-your-missing-data-imputations-using-cross-validation/>`_
* `Multiple Imputation for Continuous and Categorical Data: Comparing Joint and Conditional Approaches <http://www.stat.columbia.edu/~gelman/research/published/MI_manuscript_RR.pdf>`_
* `Multiple Imputation by Chained Equations: What is it and how does it work? <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/>`_
* `Much ado about nothing: A comparison of missing data methods and software to fit incomplete data regression models <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1839993/>`_

*Librairies*

* `fancyimpute <https://github.com/hammerlab/fancyimpute>`_
* `knnimpute <https://github.com/hammerlab/knnimpute>`_

------------

Machine Learning - Formalisation
================================

.. contents::
    :local:
    :depth: 1

|pyecopng| |pystatpng|

.. _l-ml-skgael:

Machine learning, cours de Gaël Varoquaux
+++++++++++++++++++++++++++++++++++++++++

`Gaël Varoquaux <http://gael-varoquaux.info/>`_
est un des concepteurs de
`scikit-learn <http://scikit-learn.org/stable/>`_.

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

Les `notes de lectures <https://github.com/GaelVaroquaux/sklearn_ensae_course>`_
(`Gaël Varoquaux <http://gael-varoquaux.info/>`_) sont disponibles sur GitHub et reprise
ici :

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_ensae_sklearn
    specials/machine_learning
    notebooks/td2a_eco_regressions_lineaires

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_statdes
    notebooks/_gs2a_ml_base

*Lectures*

* `API design for machine learning software: experiences from the scikit-learn project <https://arxiv.org/pdf/1309.0238.pdf>`_
* `Économétrie & Machine Learning <https://arxiv.org/pdf/1708.06992.pdf>`_
* `A Visual Introduction to Machine Learning <http://www.r2d3.us/visual-intro-to-machine-learning-part-1/>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `A Tour of Machine Learning Algorithms <http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/>`_
* `12 Algorithms Every Data Scientist Should Know <https://datafloq.com/read/12-algorithms-every-data-scientist-should-know/2024>`_ *(2016/06)*
* `10+2 Data Science Methods that Every Data Scientist Should Know in 2016 <http://tjo-en.hatenablog.com/entry/2016/04/18/190000>`_ *(2016/06)*
* `Complete Guide to Parameter Tuning in XGBoost (with codes in Python) <https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/>`_ *(2016/08)*
* `XGBoost: A Scalable Tree Boosting System <http://arxiv.org/pdf/1603.02754v1.pdf>`_, Tianqi Chen, Carlos Guestrin
* `Round Robin Classification <http://www.jmlr.org/papers/volume2/fuernkranz02a/fuernkranz02a.pdf>`_
* `ANN-Benchmarks: A Benchmarking Tool for Approximate Nearest Neighbor Algorithms? <http://www.itu.dk/people/maau/additional/sisap2017-preprint.pdf>`_

*Livres*

* `Python Data Science Handbook <https://github.com/jakevdp/PythonDataScienceHandbook>`_
* `The Elements of Statistical Learning <https://web.stanford.edu/~hastie/ElemStatLearn/>`_ :
  la bible que tout le monde recommande :

*Comprendre*

* `Explaining the Success of AdaBoost and Random Forests as Interpolating Classifiers <http://jmlr.org/papers/volume18/15-240/15-240.pdf>`_

*Modules*

* :epkg:`scikit-learn`
* :epkg:`statsmodels`
* :epkg:`XGboost`

Et quelques autres comme :

* `annoy <https://github.com/spotify/annoy>`_

|pyecopng| |pystatpng|

.. _l-td2a-ml-extensions:

De la théorie à la pratique
+++++++++++++++++++++++++++

Tous les modèles proposées répondent à un problème d'optimisation
et convergent avec un algorithme donnée et avec des hypothèses
précises sur les données. Dans la plupart des cas, ces hypothèses
ne sont jamais vérifiées. Malgré tout, on continue à utiliser
le machine learning parce qu'il marche plutôt bien même si les
hypothèses initiales ne sont pas vérifiées mais connaître la
façon dont sont construits ces modèles aide à construire
une liste de recettes qui améliorent leur performances et qui
accélèrent le moment où le problème devient vraiment intéressant.
Deux ou trois petits à garder à l'esprit.

Les réseaux de neurones s'apprennent avec des méthodes de d'optimisation
basées sur le **gradient**. Elles n'aiment pas les **échelles logarithmiques**.
Les variables de type fréquences (nombre de clics sur une page, nombre d'occurence
d'un mot, ...) ont des queues épaisses et quelques valeurs extrêmes,
il est conseillé de normaliser et de passer à une échelle logarithmique.
Elles n'aiment pas les **gradients élevés** : le gradient peut avoir une valeur très élevée
dan un voisinage localisée (un regression proche d'une fonction en escalier),
l'optimisation à base de gradient mettra beaucoup de temps à converger.
Elles n'aiment pas les **variables discrètes** : le calcul du gradient fonctionne beaucoup
mieux sur des variables continues plutôt que des variables discrètes
car cela limite le nombre de valeurs que peut prendre le gradient.

Les forêts aléatoires  et les arbres de décision sont des méthodes ensemblistes.
Elles n'utilisent pas de gradient. Elles ne sont pas sensibles à la
**normalisation**, comme ces modèles sont des assemblages de décisions basées sur
des seuils, ils ne sont pas sensibles aux changements d'échelle. En revanche, elles
n'aiment pas trop pas **décisions obliques**, comme un seuil s'applique sur une variable,
il ne peut approcher une droite *x + y = 1* qu'avec une fonction en escalier
(lire `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_).
Ces algorithms n'aiment pas non plus les problèmes **multi-classe**.
Pour un assemblage de fonction binaire (au dessus ou en dessous du seuil),
il est plus facile d'avoir seulement deux choix.
On compense cette lacune avec deux stratégies
`one versus rest <https://en.wikipedia.org/wiki/Multiclass_classification#One-vs.-rest>`_
ou `one versus one <https://en.wikipedia.org/wiki/Multiclass_classification#One-vs.-one>`_
(stratégie dite aussi `pair-wise <https://en.wikipedia.org/wiki/Learning_to_rank#Pairwise_approach>`_).

Le `boosting <https://en.wikipedia.org/wiki/Boosting_(machine_learning)>`_
est une technique de machine learning qui consiste à sur-pondérer
les erreurs. Pour un algorithme d'apprentissage itératif, cela consiste à donner
plus de poids à l'itération *n* aux erreurs produites par l'itération *n-1*.
L'algorithme le plus connu est `AdaBoost <https://en.wikipedia.org/wiki/AdaBoost>`_.
Le `gradient boosting <https://en.wikipedia.org/wiki/Gradient_boosting>`_ est
l'application de ce concept à un modèle et une fonction d'erreur dérivable.
A ce sujet : `The Boosting Approach to Machine Learning An Overview <https://www.cs.princeton.edu/picasso/mats/schapire02boosting_schapire.pdf>`_,
`A Theory of Multiclass Boosting <http://rob.schapire.net/papers/multiboost-journal.pdf>`_,
`weak learner <https://stats.stackexchange.com/questions/82049/what-is-meant-by-weak-learner>`_.

`XGBoost <http://xgboost.readthedocs.io/>`_
est un librairie qui a bénéficié de nombreux apports au fur et à
mesure des compétitions `Kaggle <https://www.kaggle.com/>`_
qu'elle a permis de gagner. Certains paramètres qui pilotent l'apprentissage
du modèle ne sont pas issus de la théorie mais de la pratique
et permettent de contourner un problème de données qui ferait
échouer l'apprentissage :
`paramètres de XGBoost <https://github.com/dmlc/xgboost/blob/master/doc/parameter.md>`_.
C'est le cas du paramètre *scale_pos_weight* qui permet de forcer une distribution
des labels de sortie dans le cas d'un problème de classification binaire.
C'est utile dans le cas d'un problème
de :ref:`l-imbalanced-classification`.

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
* `On the Mutual Nearest Neighbors Estimate in Regression <http://www.jmlr.org/papers/volume14/guyader13a/guyader13a.pdf>`_
* `The Boosting Approach to Machine Learning An Overview <https://www.cs.princeton.edu/picasso/mats/schapire02boosting_schapire.pdf>`_,
* `A Theory of Multiclass Boosting <http://rob.schapire.net/papers/multiboost-journal.pdf>`_

`JMLR <http://www.jmlr.org/>`_
poste régulièrement des articles sur des librairies de machine learning open source telles que
`fastFM: A Library for Factorization Machines <fastFM: A Library for Factorization Machines>`_.

*Recherche*

* `XGBoost: A Scalable Tree Boosting System <https://arxiv.org/pdf/1603.02754.pdf>`_
* `On the Influence of Momentum Acceleration on OnlineLearning <http://www.jmlr.org/papers/volume17/16-157/16-157.pdf>`_

*Digressions*

* `A Network That Learns Strassen Multiplication <http://www.jmlr.org/papers/volume17/16-074/16-074.pdf>`_
* `Learning Theory for Distribution Regression <http://www.jmlr.org/papers/volume17/14-510/14-510.pdf>`_

*Métriques*

* `Optimization of AMS using Weighted AUC optimized models <http://jmlr.org/proceedings/papers/v42/diaz14.pdf>`_

*Modules*

* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `xgboost <https://xgboost.readthedocs.io/en/latest/>`_
* `mlxtend <https://github.com/rasbt/mlxtend>`_

|pyecopng| |pystatpng|

.. _l-imbalanced-classification:

Imbalanced classification
+++++++++++++++++++++++++

.. index:: imbalanced, mal-balancé

Imbalanced, mal balancé, skewed, ce type de problème de données
est très fréquent. Il signifie qu'une classe dans un problème de classification
est sous-représentée par rapport aux autres et que le modèle de machine
learning n'est pas suffisamment pénalisé s'il n'en tient pas compte.
Le cas classique est un problème à deux classes, une majoritaire à 99%,
une minoritaire à 1%. Un modèle qui répond toujours la majorité est correct
99% du temps mais il n'a rien appris puisque sa réponse est constante.
Comment le forcer à apprendre quelque chose ? Il existe trois types approches
et la réponse est souvent un mélange des trois :

* *boosting* : le modèle pondère davantage les exemples sur lesquels il fait
  des erreurs, a fortiori, les exemples de la classe minoritaire
* *over sampling* : on multiplie les exemples de la classe minoritaire
  de façon à lui donner plus de poids
* *under sampling* : on réduit le nombre d'exemples de la classe majoritaire
  sans altérer la capacité du modèle à trouver une bonne solution, cela consiste
  à enlever des exemples loin de la frontière de classification.

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_ml_imbalanced

*Lectures*

* `Classification of Imbalanced Data with a Geometric Digraph Family <http://www.jmlr.org/papers/volume17/15-604/15-604.pdf>`_
* `RUSBoost: A Hybrid Approach to Alleviating Class Imbalance <http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=9260A5C92AC5F8FA3B8590A53A06248D?doi=10.1.1.309.2305&rep=rep1&type=pdf>`_
* `RAMOBoost: Ranked Minority Oversampling in Boosting <https://ai2-s2-pdfs.s3.amazonaws.com/9640/1540d5d8c4d5d956ae5fa487590dd8682507.pdf>`_
* `ND DIAL: Imbalanced Algorithms <https://github.com/dialnd/imbalanced-algorithms>`_
* `rusboost.py <https://github.com/harusametime/RUSBoost>`_ (plutôt un bout de code)
* `xgboost <https://xgboost.readthedocs.io/en/latest/>`_
* `Boosting and AdaBoost for Machine Learning <https://machinelearningmastery.com/boosting-and-adaboost-for-machine-learning/>`_,
  `A Gentle Introduction to the Gradient Boosting Algorithm for Machine Learning <https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/>`_,
  `Thoughts on Hypothesis Boosting <https://www.cis.upenn.edu/~mkearns/papers/boostnote.pdf>`_,
  `Predictions Games and Arcing Algorithms <https://www.stat.berkeley.edu/~breiman/games.pdf>`_

*Modules*

* `imbalanced-learn <https://github.com/scikit-learn-contrib/imbalanced-learn>`_
  (la documentation est intéressante)

|pyecopng| |pystatpng|

.. index:: multilabel

Classification Multi-label
++++++++++++++++++++++++++

*à venir*

*Lectures*

* `A Ranking-based KNN Approach for Multi-Label Classification <http://www.jmlr.org/proceedings/papers/v25/chiang12/chiang12.pdf>`_
* `Classification by Selecting Plausible Formal Concepts in a Concept Lattice <http://ceur-ws.org/Vol-977/paper5.pdf>`_
* `Large-scale Multi-label Learning with Missing Labels <http://jmlr.org/proceedings/papers/v32/yu14.pdf>`_
* `Multiclass-Multilabel Classification with More Classes than Examples <http://www.jmlr.org/proceedings/papers/v9/dekel10a/dekel10a.pdf>`_

|pyecopng| |pystatpng|

Ranking
+++++++

*(à venir)*

*Lectures*

* `Learning to rank (software, datasets) <http://arogozhnikov.github.io/2015/06/26/learning-to-rank-software-datasets.html>`_
* `Multiple-criteria decision analysis <https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis>`_
* `Data-driven Rank Breaking for Efficient Rank Aggregation <http://www.jmlr.org/papers/volume17/16-209/16-209.pdf>`_
* `BPR: Bayesian Personalized Ranking from Implicit Feedback <https://arxiv.org/abs/1205.2618>`_
  (applicable également aux systèmes de recommandation)

*Modules*

* `xgboost <https://xgboost.readthedocs.io/en/latest/>`_
* `scikit-learn <http://scikit-learn.org/>`_
* `pyltr <https://github.com/jma127/pyltr>`_
* `lightfm <https://github.com/lyst/lightfm>`_
* `rankpy <https://github.com/dmitru/rankpy>`_ (standby)
* `The Lemur Project - ranklib <https://sourceforge.net/p/lemur/wiki/RankLib/>`_
* `scikit-criteria <https://github.com/leliel12/scikit-criteria>`_ (standby)

|pystatpng|

Système de recommandation
+++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Recommendations in Keras using triplet loss <https://github.com/maciejkula/triplet_recommendations_keras>`_
* `AutoRec: Autoencoders Meet Collaborative Filtering <http://users.cecs.anu.edu.au/~akmenon/papers/autorec/autorec-paper.pdf>`_,
  `Hybrid Recommender System based on Autoencoders <https://hal.inria.fr/hal-01336912/file/AutoEnc.pdf>`_
* `ACP et factorisation de matrices <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/missing_values_mf.html>`_
* `The Why and How of Nonnegative Matrix Factorization <https://arxiv.org/abs/1401.5226>`_
* `A tutorial on Non-Negative Matrix Factorisation with Applications to Audiovisual Content Analysis <http://perso.telecom-paristech.fr/~essid/teach/NMF_tutorial_ICME-2014.pdf>`_
* `Large-Scale Matrix Factorization with Missing Data under Additional Constraints <http://www.cfar.umd.edu/~rama/Publications/mitra_nips_2010.pdf>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/>`_
* `NonnegMFPy <https://github.com/guangtunbenzhu/NonnegMFPy>`_ : implémentation de
  l'algorithme décrit dans l'article
  `Large-Scale Matrix Factorization with Missing Data under Additional Constraints <http://www.cfar.umd.edu/~rama/Publications/mitra_nips_2010.pdf>`_
* `scikit-surprise <http://surpriselib.com/>`_ (`documentation <http://surprise.readthedocs.io/en/stable/>`_)

|pystatpng|

.. _l-td2a-reinforcement-learning:

Reinforcement Learning
++++++++++++++++++++++

ou *apprentissage par renforcement*

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
* `Temporal difference learning <https://en.wikipedia.org/wiki/Temporal_difference_learning>`_

|pystatpng|

Bandits
+++++++

*(à venir)*

*Lectures*

* `Bandit theory, part I <http://blogs.princeton.edu/imabandit/2016/05/11/bandit-theory-part-i/>`_
* `Bandit theory, part II <http://blogs.princeton.edu/imabandit/2016/05/13/bandit-theory-part-ii/>`_
* `Kernel-based methods for bandit convex optimization, part 1 <http://blogs.princeton.edu/imabandit/2016/08/06/kernel-based-methods-for-bandit-convex-optimization-part-1/>`_
* `Kernel-based methods for bandit convex optimization, part 2 <http://blogs.princeton.edu/imabandit/2016/08/09/kernel-based-methods-for-convex-bandits-part-2/>`_
* `Kernel-based methods for bandit convex optimization, part 3 <http://blogs.princeton.edu/imabandit/2016/08/10/kernel-based-methods-for-convex-bandits-part-3/>`_
* `Learning to Interact <http://hunch.net/~jl/interact.pdf>`_ (John Langford)
* `Batch Learning from Logged Bandit Feedback through Counterfactual Risk Minimization <http://www.jmlr.org/papers/volume16/swaminathan15a/swaminathan15a.pdf>`_
* `Stochastic Structured Prediction under Bandit Feedback <https://papers.nips.cc/paper/6134-stochastic-structured-prediction-under-bandit-feedback.pdf>`_
* `Thompson sampling with the online bootstrap <https://arxiv.org/abs/1410.4009>`_ (à lire)
* `Trial without Error: Towards Safe Reinforcement Learning via Human Intervention <https://arxiv.org/abs/1707.05173>`_

|pystatpng|

Modèles bayésiens
+++++++++++++++++

*(à venir)*

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_bayes

*Lectures*

* `A Bayesian Approximation Method for Online Ranking <http://jmlr.csail.mit.edu/papers/volume12/weng11a/weng11a.pdf>`_
* `stan case studies <http://mc-stan.org/documentation/case-studies>`_
* `Edward: A library for probabilistic modeling, inference, and criticism <https://arxiv.org/pdf/1610.09787.pdf>`_
* `Auto-Encoding Variational Bayes <https://arxiv.org/pdf/1312.6114.pdf>`_

*Vidéo*

* `Variational Inference in Python <https://www.youtube.com/watch?v=3KGZDC3-_iY>`_
* `Bayesian Network Modeling using R and Python <https://www.youtube.com/watch?v=iRvXfx9IWM0>`_

*Modules*

* `edward <http://edwardlib.org/>`_
* `PyMC3 <https://pymc-devs.github.io/pymc3/notebooks/getting_started.html>`_
* `bayespy <http://bayespy.org/en/latest/>`_
* `kabuki <https://pypi.python.org/pypi/kabuki/>`_
* `bnpy <https://github.com/bnpy/bnpy>`_
* `pyro <http://pyro.ai/>`_ : modèle bayèsiens et deep learning

*Exemples de code*

* `Probabilistic Models <https://github.com/wiseodd/probabilistic-models>`_ :
  sont implémentés entre autres, LDA, Chinese Restaurant Process, Indian Restaurant Process,
  GMM...

|pystatpng|

Factorization Machines
++++++++++++++++++++++

*(à venir)*

*Lectures*

* `Factorization Machines with libFM <http://www.csie.ntu.edu.tw/~b97053/paper/Factorization%20Machines%20with%20libFM.pdf>`_ *(2016/09)*
* `Stochastic Subsampling for Factorizing Huge Matrices <https://hal.archives-ouvertes.fr/hal-01431618>`_
* `Field-aware Factorization Machines in a Real-world Online Advertising System <https://arxiv.org/abs/1701.04099>`_
* `fastFM: A Library for Factorization Machines <fastFM: A Library for Factorization Machines>`_

*Librairies*

* `libffm <http://www.csie.ntu.edu.tw/~r01922136/libffm/>`_ (C++)
* `fastFM <https://github.com/ibayer/fastFM>`_

------------

Méthodes Statistiques
=====================

.. contents::
    :local:
    :depth: 1

|pyecopng| |pystatpng|

Données de panels
+++++++++++++++++

*(à venir)*

*Modules*

* `linearmodels <https://bashtage.github.io/linearmodels/doc/>`_
