
.. _l-projinfo3a:

.. index:: 3A

3A - Projets informatiques
==========================

.. contents::
    :local:

Travail attendu
+++++++++++++++

Le projet a pour objectif l'implémentation d'un algorithme réparti,
soit en utilisant le calcul sur GPU, soit via Map/Reduce,
soit en implémentant vous-même la répartition des calculs sur plusieurs machines (virtuelles)
via des primitives telles que `MPI <http://fr.wikipedia.org/wiki/Message_Passing_Interface>`_ ou des
`Key-Value Pair Storages <http://en.wikipedia.org/wiki/NoSQL>`_.
Les technologies proposées sont donc :

* GPU : `CUDA <http://fr.wikipedia.org/wiki/Compute_Unified_Device_Architecture>`_ et C, ou CUDA et python via
  `pyCUDA <http://mathema.tician.de/software/pycuda/>`_
* Map/Reduce : `PIG <http://en.wikipedia.org/wiki/Pig_Latin>`_,
  `Hive <http://fr.wikipedia.org/wiki/Hive>`_, Java sur un cluster Cloudera ou Azure,
  `Spark <https://spark.apache.org/>`_
* implémentation d'un calcul réparti ou distribué : `QueueStorage <http://azure.microsoft.com/fr-fr/documentation/articles/storage-dotnet-how-to-use-queues/>`_ +
  `Blobstorage <http://azure.microsoft.com/fr-fr/documentation/articles/storage-dotnet-how-to-use-blobs/>`_
  comme primitives de communication (C#, .Net) sur Azure.

Vous êtes libres de traiter l'algorithme de votre choix avec la technologie
de votre choix avec la contrainte que l'algorithme implémenté soit distribué
par votre implémentation et non par la librairie que vous utilisez.
**Dans ce cadre, un projet sur un réseau de neurones profond seul
n'est pas valide.**
Nous vous en proposons certains dans les articles ci-dessous.

**A souligner dans le rapport et le code**

* **GPU** : indiquer les parties parallélisées, les frontières entre CPU et GPU,
  une estimation du coût de l'algorithme CPU / GPU / nombre de verrous.
* **Calcul distribué** : indiquer les parties parallélisées,
  les variables partagées, si cela est fait via un thread ou un processus,
  une estimation du coût de l'algorithme communication / CPU / nombre de verrous.
* **Map/Reduce** (Spark ou autre) : préfixer le noms des colonnes par *m_* ou *d_* selon la colonne
  contient des données ou un coefficient du modèle optimisé, donner une estimation du nombre de
  lignes de chaque flux manipulé.

.. _l-suggestio-articles-projet-3A:

Suggestions d'articles
++++++++++++++++++++++

*Articles ou sujet que vous ne pouvez plus choisir*

* `Dimension Independent Matrix Square using MapReduce (DIMSUM) <http://stanford.edu/~rezab/papers/dimsum.pdf>`_
* `Map/Reduce Affinity Propagation Clustering Algorithm <http://www.ijeee.net/uploadfile/2014/0807/20140807114023665.pdf>`_ ou
  `Parallel Hierarchical Affinity Propagation with MapReduce <https://arxiv.org/abs/1403.7394>`_
* Algorithme `k-means clustering <https://en.wikipedia.org/wiki/K-means_clustering>`_

*2014-2015*

* `Parallel MCMC <http://arxiv.org/pdf/1010.1595v3.pdf>`_
* `Parallel Gradient Descent in Minibatches <http://research.microsoft.com/pubs/158712/distr_mini_batch.pdf>`_
* `FFT et convolutions sous GPU <http://cadik.posvete.cz/papers/cadikm-iv06-gpu.pdf>`_
* `Algos de PageRank <http://lintool.github.io/MapReduceAlgorithms/MapReduce-book-final.pdf>`_ (p106)
* `Recherche de valeurs propres en grande dimension <http://arxiv.org/pdf/1304.1467v3.pdf>`_
* `Algorithmes LASSO parallèles <http://arxiv.org/pdf/1411.6520v1.pdf>`_
* `Distributed Online Learning <http://arxiv.org/pdf/1308.4568v3.pdf>`_
* `Large-scale L-BFGS using MapReduce <http://papers.nips.cc/paper/5333-large-scale-l-bfgs-using-mapreduce>`_
* `LightLDA: Big Topic Models on Modest Compute Clusters <http://arxiv.org/abs/1412.1576>`_
* `A Reliable Effective Terascale Linear Learning System <http://jmlr.org/papers/volume15/agarwal14a/agarwal14a.pdf>`_

*2015-2016*

* `Multi-Block ADMM for Big Data Optimization in Modern Communication Networks <http://arxiv.org/abs/1504.01809>`_, optimisation distribuée (ADMM)
* `A scalable system for primal-dual optimization <http://arxiv.org/pdf/1507.01461v1.pdf>`_, optimisation sous contrainte avec Map/Reduce et Spark
* `Sorting and Permuting without Bank Conflicts on GPUs <http://arxiv.org/abs/1507.01391>`_
* `Building Balanced k-d Tree with MapReduce <http://arxiv.org/abs/1512.06389>`_
* `Scalable Models for Computing Hierarchies in Information Networks <http://arxiv.org/abs/1601.00626>`_,
  Distributed Random Walks with Restart
* `Optimally Pruning Decision Tree Ensembles With Feature Cost <http://arxiv.org/pdf/1601.00955v1.pdf>`_, voir section 5
* `Scalable Matrix Inversion Using MapReduce <https://cs.uwaterloo.ca/~ashraf/pubs/hpdc14matrix.pdf>`_

*2016-2017*

* `The Part-Time Parliament <http://research.microsoft.com/en-us/um/people/lamport/pubs/pubs.html#lamport-paxos>`_,
  ce papier introduit l'algorithme `Paxos <https://en.wikipedia.org/wiki/Paxos_(computer_science)>`_ qui gère les problèmes
  de consensus entre machines. Une machine souhaite déléguer un travail à une autre mais elle a le choix.
  Comment s'assurer qu'une seule et une seule machine ne fait ce travail ?
  On pourra traiter n'importe qu'elle autre variance de l'algorithme plus récente.
* `Schönhage-Strassen Algorithm with MapReduce for Multiplying Terabit Integers <http://people.apache.org/~szetszwo/ssmr20110429.pdf>`_
* `A Fast Parallel Stochastic Gradient Method for Matrix Factorization in Shared Memory Systems <http://jmlr.org/papers/v17/15-471.html>`_
* `Asynchronous Methods for Deep Reinforcement Learning <http://arxiv.org/pdf/1602.01783.pdf>`_
* `Parallelizing Word2Vec in Shared and Distributed Memory <http://arxiv.org/abs/1604.04661>`_
* `Exploiting Multiple Levels of Parallelism in Sparse Matrix-Matrix Multiplication <http://arxiv.org/abs/1510.00844>`_
* `Hogwild!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent <https://arxiv.org/pdf/1106.5730v2.pdf>`_
* `L1-Regularized Distributed Optimization: A Communication-Efficient Primal-Dual Framework <http://arxiv.org/pdf/1512.04011v2.pdf>`_
* `Local Approximation of PageRank and Reverse PageRank <https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/34455.pdf>`_
* `A Fast Parallel SGD for Matrix Factorization in Shared Memory Systems <https://www.csie.ntu.edu.tw/~cjlin/papers/libmf/libmf.pdf>`_
* `CuMF_SGD: Fast and Scalable Matrix Factorization <https://arxiv.org/pdf/1610.05838.pdf>`_

*2017-2018*

* `A Parallel Matrix Scaling Algorithm <http://amestoy.perso.enseeiht.fr/doc/adru.pdf>`_
* `Auto-Differentiating Linear Algebra <https://arxiv.org/pdf/1710.08717.pdf>`_
* `Efficient Distributed Locality Sensitive Hashing <https://arxiv.org/abs/1210.7057>`_
* `Parallel GPU Implementation of Iterative PCA Algorithms <https://arxiv.org/abs/0811.1081v1>`_
* `Large-Scale Matrix Factorization with Distributed Stochastic Gradient Descent <https://researcher.watson.ibm.com/researcher/files/us-phaas/rj10482Updated.pdf>`_
* `weighted minhash on gpu helps to find duplicate github repositories <https://blog.sourced.tech//post/minhashcuda/>`_ (article de blog)

*2018-2019*

* `Estimating Mutual Information on Data Streams <https://dbis.ipd.kit.edu/download/camera_ready_17_with_copyright.pdf>`_
* `Affinity Clustering: Hierarchical Clustering at Scale <https://papers.nips.cc/paper/7262-affinity-clustering-hierarchical-clustering-at-scale.pdf>`_
  (voir également
  `Spinner: Scalable Graph Partitioning in the Cloud <https://arxiv.org/abs/1404.3861>`_,
  `Fennel: Streaming Graph Partitioning for Massive Scale Graphs <https://www.microsoft.com/en-us/research/publication/fennel-streaming-graph-partitioning-for-massive-scale-graphs/>`_,
  `METIS - Serial Graph Partitioning and Fill-reducing Matrix Ordering <https://github.com/EmanueleCannizzaro/metis>`_,
  `Balanced Label Propagation for Partitioning Massive Graphs <https://stanford.edu/~jugander/papers/wsdm13-blp.pdf>`_)
* `DSCOVR: Randomized Primal-Dual Block Coordinate Algorithms for Asynchronous Distributed Optimization <https://www.microsoft.com/en-us/research/wp-content/uploads/2017/10/dscovr.pdf>`_
* `A Fast Parallel Stochastic Gradient Method for Matrix Factorization in Shared Memory Systems <https://www.csie.ntu.edu.tw/~cjlin/papers/libmf/libmf_journal.pdf>`_

*2019-2020*

* `Anatomy of High-Performance Many-Threaded Matrix Multiplication
  <http://www.cs.utexas.edu/users/flame/pubs/blis3_ipdps14.pdf>`_

Nous vous recommandons d'adopter la démarche suivante:

#. implémentation et débugging sur un petit jeu de données synthétiques
   où les choses sont sensées bien se passer
   et la taille du jeu de données rend le debugging plus rapide,
#. application à un vrai jeu de données que vous aurez sélectionné sur un des sites suivants
   `Stanford Large Network Dataset Collection <http://snap.stanford.edu/data/>`_,
   `UCI Machine Learning Repository <https://archive.ics.uci.edu/ml/datasets.html>`_
   ou autre (voir :ref:`l-datasources`).

Le site
`Kaggle <https://www.kaggle.com/competitions/search?SearchVisibility=AllCompetitions&ShowActive=true&ShowCompleted=true&ShowProspect=true&ShowOpenToAll=true&ShowPrivate=true&ShowLimited=true&DeadlineColumnSort=Descending>`_ `(2) <http://inclass.kaggle.com/>`_
référence de nombreuses compétitions intéressantes.
Toutefois, avant d'utiliser les données Kaggle, je vous encourage à lire les articles
`Date use for teaching after competition concludes <http://www.kaggle.com/c/decoding-the-human-brain/forums/t/8331/date-use-for-teaching-after-competition-concludes>`_
et `Using a Kaggle contest as a term project <http://www.kaggle.com/forums/t/2745/using-a-kaggle-contest-as-a-term-project>`_.
Les règles peuvent varier d'un projet à l'autre, prenez soin de les lire avant de choisir un projet
car on ne peut pas tout faire avec les données disponibles sur ce site.

.. index:: PageRank, k-means, factorisation de matrice

Exemples d'implémentation d'algorithme en PIG
+++++++++++++++++++++++++++++++++++++++++++++

Trois projets réalisés par les élèves lors de l'année 2014-2015 :

* :ref:`2015pagerankrst`
* :ref:`2015kmeansrst`
* :ref:`2015factorisationmatricerst`

Code de survie
++++++++++++++

* :ref:`blogpost_azure_file_attente`
