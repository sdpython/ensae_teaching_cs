

.. _l-projinfo3a:

.. index:: 3A

3A - Projets informatiques
==========================

Le projet aura pour objectif l'implémentation d'un algorithme réparti, 
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

Vous êtes libres de traiter l'algorithme de votre choix. Nous vous en proposons certains dans les articles ci-dessous

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
* `Multi-Block ADMM for Big Data Optimization in Modern Communication Networks <http://arxiv.org/abs/1504.01809>`_, optimisation distribuée (ADMM)


Nous vous recommandons d'adopter la démarche suivante:

#. implémentation et débugging sur un petit jeu de données synthétiques où :
    * les choses sont sensées bien se passer
    * la taille du jeu de données rend le debugging plus rapide
#. Un vrai jeu de données que vous aurez sélectionné sur un des sites suivants :
    * `Stanford Large Network Dataset Collection <http://snap.stanford.edu/data/>`_
    * `UCI Machine Learning Repository <https://archive.ics.uci.edu/ml/datasets.html>`_



Autres sources de jeux de données
+++++++++++++++++++++++++++++++++

* `Kaggle <https://www.kaggle.com/competitions/search?SearchVisibility=AllCompetitions&ShowActive=true&ShowCompleted=true&ShowProspect=true&ShowOpenToAll=true&ShowPrivate=true&ShowLimited=true&DeadlineColumnSort=Descending>`_ `(2) <http://inclass.kaggle.com/>`_,
  Toutefois, avant d'utiliser les données Kaggle, je vous encourage à lire les articles `Date use for teaching after competition concludes <http://www.kaggle.com/c/decoding-the-human-brain/forums/t/8331/date-use-for-teaching-after-competition-concludes>`_,
  et `Using a Kaggle contest as a term project <http://www.kaggle.com/forums/t/2745/using-a-kaggle-contest-as-a-term-project>`_.
  Les règles peuvent varier d'un projet à l'autre, prenez soin de les lire avant de choisir un projet.
* `Global Disease Monitoring and Forecasting with Wikipedia  <http://www.ploscompbiol.org/article/info:doi/10.1371/journal.pcbi.1003892>`_
* :ref:`Autres suggestions <l-datasources>`
* `urls, spam, ... <http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html>`_, jeux de données utilisés 
  comme benchmark pour la libraire `libsvm <http://www.csie.ntu.edu.tw/~cjlin/libsvm/>`_
* `Pascal Large Scale Learning Challenge <http://largescale.ml.tu-berlin.de/instructions/>`_
* Votre propre jeu de données (à valider avec l'encadrant).

Git
+++

* :ref:`gitnotebookrst`





