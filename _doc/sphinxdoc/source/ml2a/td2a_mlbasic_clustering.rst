
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-basic-clustering:

Clustering
++++++++++

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_clustering

(à venir)

* score silhouette
* clustering de variables catégorielles

*Métriques*

* `Indice de Rand <https://fr.wikipedia.org/wiki/Indice_de_Rand>`_
* `Silhouette (clustering) <https://en.wikipedia.org/wiki/Silhouette_(clustering)>`_
* `The Impact of Random Models on Clustering Similarity <http://www.jmlr.org/papers/volume18/17-039/17-039.pdf>`_

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
* `Hierarchical Clustering via Spreading Metrics <http://www.jmlr.org/papers/volume18/17-081/17-081.pdf>`_

*Lectures - Constraint KMeans*

* `Same-size k-Means Variation <https://elki-project.github.io/tutorial/same-size_k_means>`_
* `Constrained K-means Clustering with Background Knowledge <http://cse.msu.edu/~cse802/notes/WagstaffCOPKmeans.pdf>`_
 (voir aussi `cop_kmeans.py <https://github.com/Behrouz-Babaki/COP-Kmeans/blob/master/copkmeans/cop_kmeans.py>`_)

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/>`_
* `hdbscan <https://github.com/scikit-learn-contrib/hdbscan>`_
* `pyclustering <https://pypi.python.org/pypi/pyclustering>`_
* `pycluster <https://pypi.python.org/pypi/pycluster>`_
