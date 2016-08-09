

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
  `Hive <http://fr.wikipedia.org/wiki/Hive>`_ ou Java sur un cluster Cloudera ou Azure
* implémentation d'un calcul réparti : `QueueStorage <http://azure.microsoft.com/fr-fr/documentation/articles/storage-dotnet-how-to-use-queues/>`_ + 
  `Blobstorage <http://azure.microsoft.com/fr-fr/documentation/articles/storage-dotnet-how-to-use-blobs/>`_ 
  comme primitives de communication (C#, .Net) sur Azure.

Vous êtes libres de traiter l'algorithme de votre choix.
Nous vous en proposons certains dans les articles ci-dessous.

Suggestions d'articles
++++++++++++++++++++++

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
  On pourra traiter n'importe qu'elle autre variance de l'algorithme plus récene.
* `Schönhage-Strassen Algorithm with MapReduce for Multiplying Terabit Integers <http://people.apache.org/~szetszwo/ssmr20110429.pdf>`_
* `Dimension Independent Matrix Square using MapReduce (DIMSUM) <http://stanford.edu/~rezab/papers/dimsum.pdf>`_
* `A Fast Parallel Stochastic Gradient Method for Matrix Factorization in Shared Memory Systems <http://jmlr.org/papers/v17/15-471.html>`_
* `Asynchronous Methods for Deep Reinforcement Learning <http://arxiv.org/pdf/1602.01783.pdf>`_
* `Parallelizing Word2Vec in Shared and Distributed Memory <http://arxiv.org/abs/1604.04661>`_
* `Exploiting Multiple Levels of Parallelism in Sparse Matrix-Matrix Multiplication <http://arxiv.org/abs/1510.00844>`_


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


