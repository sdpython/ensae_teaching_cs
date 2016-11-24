

.. _l-td3a:


==========================================================
Eléments logiciels pour le traitement des données massives
==========================================================

.. index:: 3A


`ENSAE - OMI309 <http://www.ensae.fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/3me-anne-voies-de-spcialisation-formationsdiplome-96/data-science-cours-3a.html?id=100729>`_

Cours animé par :
Matthieu Durut [#f3write1]_,
Xavier Dupré [#f3write1]_,
Antoine Ly [#f3write1]_

Le cours est évalué avec un :ref:`projet informatique <l-projinfo3a>`.


.. contents::
    :local:


Eléments techniques
===================


Anatomie et histoire d'un ordinateur
++++++++++++++++++++++++++++++++++++

* mémoire, cache, northbridge, southbridge
* CPU, GPU, FGPA, ASICS
* 2004 - espace entre deux circuits intégrés de 32 ns, passage à 24 ns ? effet quantique, passage d'électron
* optimisation des calculs, parallélisation, notion de cache et de latence

*Lectures*

* `Memory Latency over the years <https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html>`_
* `What every computer scientist should know about floating point <http://faculty.tarleton.edu/agapie/documents/cs_343_arch/papers/1991_Goldberg_FloatingPoint.pdf>`_
* `What every programmer should know about memory <https://www.akkadia.org/drepper/cpumemory.pdf>`_
* `Introduction to High Performance Scientific Computing <http://pages.tacc.utexas.edu/~eijkhout/istc/istc.html>`_
* `Zoologie des réseaux de neurones <http://www.asimovinstitute.org/neural-network-zoo/>`_
* `Teaching a machine how to play Mario <http://www.cs.cmu.edu/~tom7/mario/mario.pdf>`_
* `Introduction au système de recommandation par facteurs latents <https://datajobs.com/data-science-repo/Recommender-Systems-%5bNetflix%5d.pdf>`_
* `The Unreasonable Effectiveness of Data <http://static.googleusercontent.com/media/research.google.com/fr//pubs/archive/35179.pdf>`_


GPU
+++

* `Convolution <https://fr.wikipedia.org/wiki/Produit_de_convolution>`_
* `Introduction to CUDA C <http://www.nvidia.com/content/gtc-2010/pdfs/2131_gtc2010.pdf>`_
* Notion de block, threads
* Echange d'information entre CPU et GPU
* `index de thread <http://www.martinpeniak.com/index.php?option=com_content&view=article&catid=17:updates&id=288:cuda-thread-indexing-explained>`_
* `syncthread <http://stackoverflow.com/questions/15240432/does-syncthreads-synchronize-all-threads-in-the-grid>`_
* `shared array <http://supercomputingblog.com/cuda/cuda-tutorial-3-thread-communication/>`_

*Lectures sur le GPU*

* `Comment apprendre aux ordinateurs à comprendre des images <https://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures?language=fr>`_
* `Scaling-up Machine Learning Chapitre 16 et 17 <http://www.cambridge.org/catalogue/catalogue.asp?isbn=1139210408>`_
* `Quelques exemples graphiques de kernel 3x3 de convolution <>`_
* `Introduction aux réseaux convolutifs <http://matlabtricks.com/post-5/3x3-convolution-kernels-with-online-demo#demo>`_,
  `Canny edge detector <https://en.wikipedia.org/wiki/Canny_edge_detector>`_
* `Understanding Convolution in Deep Learning <http://timdettmers.com/2015/03/26/convolution-deep-learning/>`_
* `Pycuda <https://mathema.tician.de/software/pycuda/>`_,
  `theano <http://deeplearning.net/software/theano/>`_
* `Introduction au GPGPU <https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units>`_
* `Quelques éléments de consommation électrique sur les GPU et CPU <http://blog.octo.com/la-technologie-gpgpu-1ere-partie-le-cote-obscur-de-la-geforce/>`_
* `Inter-Block GPU Communication via Fast Barrier Synchronization <http://eprints.cs.vt.edu/archive/00001087/01/TR_GPU_synchronization.pdf>`_
* `CUDA C Programming Guide <https://docs.nvidia.com/cuda/cuda-c-programming-guide/>`_
* `Demystifying GPU Microarchitecture through Microbenchmarking <http://www.stuffedcow.net/files/gpuarch-ispass2010.pdf>`_

*Lectures sur le C++*

* `Thinking in C++ <http://mindview.net/Books/TICPP/ThinkingInCPP2e.html>`_, Bruce Eckel
* `Effective C++ <http://www.aristeia.com/books.html>`_, Scott Meyers
* `What Every Programmer Should Know About Memory <http://www.akkadia.org/drepper/cpumemory.pdf>`_, Ulrich Drepper
* `The Art of Multiprocessor Programming <http://edc.tversu.ru/elib/inf/0189.pdf>`_, Maurice Herlihy, Nir Shavit
* `An Introduction to GPGPU Programming - CUDA Architecture <http://www.diva-portal.org/smash/get/diva2:447977/FULLTEXT01.pdf>`_, Rafia Inam

Eléments théoriques
===================


Crypographie, block chain
+++++++++++++++++++++++++

* commitment et signature (RSA)
* Tiers de confiance et distributed consensus (PAXOS), `RAFT <https://raft.github.io/>`_
* Block chain, Bitcoin, Attque (Incentive, long term consensus, la probabilité qu'on soit en désaccord
  décroît avec le temps, monnaie stable, sûre, anonyme ?)
* `Ethereum <https://en.wikipedia.org/wiki/Ethereum>`_

*Lectures*

* The art of multiprocessor programming, *Nit Shavit*
* `CS176: Multiprocessor Synchronization <http://cs.brown.edu/courses/cs176/course_information.shtml>`_
* `Bitcoin and Cryptocurrency Technologies <https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf?a=1>`_
* `Delivery versus payment <http://www.multichain.com/blog/2015/09/delivery-versus-payment-blockchain/>`_
* `Ethereum official website <https://www.ethereum.org/>`_
* `Hello World in Ethereum <https://www.ethereum.org/greeter>`_
* `Introduction to Smart Contracts <http://solidity.readthedocs.io/en/develop/introduction-to-smart-contracts.html>`_
* `Monnaie, finance et économie réelle <http://www.editionsladecouverte.fr/catalogue/index-Monnaie__finance_et___conomie_r__elle-9782707185822.html>`_




Eléments logiciels
==================

Structures de données
+++++++++++++++++++++

.. toctree::

    :ref:`Séance 1 :  <td3acenoncesession1rst>`  (:ref:`correction <td3acorrectionsession1rst>`)

* `liste chaînées <http://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e>`_, 
  `stack <http://fr.wikipedia.org/wiki/Pile_(informatique)>`_, 
  `queue <http://en.wikipedia.org/wiki/Queue_(abstract_data_type)>`_, 
  `dictionnaire <http://en.wikipedia.org/wiki/Associative_array>`_,
  `hashtable <https://fr.wikipedia.org/wiki/Table_de_hachage>`_
* graphe `BFS <http://en.wikipedia.org/wiki/Breadth-first_search>`_, 
  `DFS <http://en.wikipedia.org/wiki/Depth-first_search>`_,
  `Red Black Tree <https://fr.wikipedia.org/wiki/Arbre_bicolore>`_
* `merge sort <http://en.wikipedia.org/wiki/Merge_sort>`_, 
  `quicksort <http://en.wikipedia.org/wiki/Quicksort>`_, 
  `heapsort <http://en.wikipedia.org/wiki/Heapsort>`_, 
  `max heap <http://en.wikipedia.org/wiki/Min-max_heap>`_
* String matching, Rabin-Karp, automates finis
* Notions de coût algorithme, `NP Complet <https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-complet>`_


*Lectures*

* `Introduction to Algorithms, 2nd Edition <http://is.ptithcm.edu.vn/~tdhuy/Programming/Introduction.to.Algorithms.pdf>`_, Cormen, Leiserson, Rivest, Stein.
* `Cracking the Coding Interview <http://www.valleytalk.org/wp-content/uploads/2012/10/CrackCode.pdf>`_

Threads et synchronisation
++++++++++++++++++++++++++

* threads, application multi-threadées
* variables globales, synchronisation

*Lectures*

* `TIL: clock skew exists (distributed system) <http://jvns.ca/blog/2016/02/10/til-clock-skew-exists/>`_ *(2016/06)*


Distribution des calculs, stratégies de stockage, SQL NoSQL
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. toctree::
    :maxdepth: 2

    td_3a_s5_synthese
    notebooks/hash_distribution
    notebooks/map_reduce_timeseries
    
*Lectures*

* `What Every Data Scientist Needs to Know about SQL <http://joshualande.com/data-science-sql>`_



Map Reduce en pratique
++++++++++++++++++++++

* Itérateurs, lien avec le SQL (voir :ref:`mapreducetimeseriesrst`)
* Distribution à base de hash (voir :ref:`hashdistributionrst`)
* `Mapper, Reducer, Combiner, Partitionner <https://developer.yahoo.com/hadoop/tutorial/module4.html>`_
* Graphe d'exécution, synchronisation - *Map Reduce Flow Chart*
* Exemple : moyennes par groupes
* Pas d'ordre des observations, tri sur l'ensemble des données à éviter
* Produit matriciel, représentation d'une matrice en trois colonnes, matrice sparse
* Graphe : pas facile en map/reduce, exemple avec l'algorithme des 
  :ref:`random walk with restarts <exposerwrrecommandationrst>`
* Problème des skewed datasets --> clés très mal distribués (voir :ref:`hashdistributionrst`)
* Descente du gradient : itératif
* Stratégie de parallélisation, propriétés mathématiques
  optimisation d'une fonction convexe
* Exemple de :ref:`k-means distribué <2015kmeansrst>`
* Le hasard en distribué, :ref:`Réservoir sampling <td3aenoncereservoirsamplingrst>` (:ref:`correction <td3acorrectionreservoirsamplingrst>`)
* Schéma des langages de map/reduce : 
  `lazy evaluation <https://en.wikipedia.org/wiki/Lazy_evaluation>`_ (évalusation presseuse, dask, Spark, PIG)



Map Reduce avec PIG sur Azure et Cloudera
=========================================


Les trois séances suivantes sont plus appliquées et dédiées à la découverte
de `Hadoop <http://fr.wikipedia.org/wiki/Hadoop>`_, un environnement
qui permet d'exécuter des tâches 
`Map/Reduce <http://fr.wikipedia.org/wiki/MapReduce>`_. 
Plusieurs angles d'approche sont possibles. Celle retenue est l'utilisation
du langage `PIG-latin <http://en.wikipedia.org/wiki/Pig_Latin>`_ dont la logique
ressemble beaucoup à celle du `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_.
Les outils Python [#fp1]_ simplifient la communication avec le cluster.

.. toctree::
    :maxdepth: 2
    
    specials/azure
    td_3a_A
    td_3a_B
    td_3a_C
    
.. index:: PageRank, k-means, factorisation de matrice
    
Trois projets réalisés par les élèves lors de l'année 2014-2015 :

.. toctree::
    :maxdepth: 1

    notebooks/2015_page_rank
    notebooks/2015_kmeans
    notebooks/2015_factorisation_matrice    

*Lectures*

* `PIG tutorial <https://developer.yahoo.com/hadoop/tutorial/pigtutorial.html>`_
* `PIG <http://pig.apache.org/>`_, `PIG syntax <http://pig.apache.org/docs/r0.14.0/basic.html>`_
* `commandes HDFS <http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html>`_
* `commandes linux <http://doc.ubuntu-fr.org/tutoriel/console_commandes_de_base>`_
* `azure (python) <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/index.html>`_
* `WebHCat <http://docs.hortonworks.com/HDPDocuments/HDP1/HDP-1.2.1/bk_dataintegration/content/ch_using_hcatalog_1.html>`_
* `command pig <http://pig.apache.org/docs/r0.12.1/start.html#run>`_
* `HIVE <https://hive.apache.org/>`_
* `CUBE and ROLLUP: Two Apache Pig Functions That Every Data Scientist Should Know <http://joshualande.com/cube-rollup-pig-data-science/>`_
* `How to Read and Write JSON-formatted Data With Apache Pig <http://joshualande.com/read-write-json-apache-pig/>`_
* `Programming Pig <http://chimera.labs.oreilly.com/books/1234000001811/index.html>`_, Alan Gates (accessible en ligne)
* `Programming Hive <http://shop.oreilly.com/product/0636920023555.do>`_, Edward Capriolo, Dean Wampler, Jason Rutherglen
* `Hadoop: The Definitive Guide, 2nd Edition <http://shop.oreilly.com/product/0636920010388.do>`_, Tom White  (voir aussi `GitHub <https://github.com/tomwhite/hadoop-book/>`_)
* `Hadoop in Practice <http://it-ebooks.info/book/1028/>`_, Alex Holmes
* `Data-Intensive Text Processing with MapReduce <http://lintool.github.io/MapReduceAlgorithms/>`_, Jimmy Lin, Chris Dyer
* `Introducing Microsoft Azure HDInsight <http://blogs.msdn.com/b/microsoft_press/archive/2014/05/27/free-ebook-introducing-microsoft-azure-hdinsight.aspx>`_, Avkash Chauhan, Valentine Fontama, Michele Hart, Wee Hyong Tok, Buck Woody
* `Introduction to Apache Pig <http://www.cloudera.com/content/cloudera/en/resources/library/training/introduction-to-apache-pig.html>`_ (MOOC)


    
Map Reduce avec Spark SQL
=========================

(*à venir*)


*Lectures*

* `Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing <http://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf>`_,
  Matei Zaharia, Mosharaf Chowdhury, Tathagata Das, Ankur Dave, Justin Ma, Murphy McCauley, Michael J. Franklin, Scott Shenker, Ion Stoica
* `From scikit-learn to Spark ML <http://blog.xebia.fr/2015/10/08/from-scikit-learn-to-spark-ml/>`_ *(2016/06)*




.. _l-td3a-start:

Getting started
===============

**PIG**

Ces enseignements vous sont proposés via des notebooks. 
Ils requièrent une surcouche apporté par le module 
`pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_.
Le python n'est pas l'objet de ce cours, les notebooks sont utilisés
pour pouvoir regrouper dans un même document toutes les opérations 
effectuées dans un langage Map/Reduce.
La page :ref:`l-installation-courte` décrit comment installer 
ces outils sur les trois OS principaux 
`Windows <http://www.microsoft.com/fr-fr/windows>`_, 
`OS X <http://www.apple.com/osx/>`_, 
`Linux <https://en.wikipedia.org/wiki/Linux>`_.

**SPARK**

.. toctree::
    
    td_3a_spark




.. _l-td3a-biblio:


Bibliographie
=============


**Articles**

* `Large Scale Distributed Deep Networks <http://www.cs.toronto.edu/~ranzato/publications/DistBeliefNIPS2012_withAppendix.pdf>`_, Jeffrey Dean, Greg S. Corrado, Rajat Monga, Kai Chen, Matthieu Devin, Quoc V. Le, Mark Z. Mao, Marc'Aurelio Ranzato, Andrew Senior, Paul Tucker, Ke Yang, Andrew Y. Ng
* `Stochastic Gradient Descent Tricks <http://research.microsoft.com/pubs/192769/tricks-2012.pdf>`_, Léon Bottou
* `A Fast Distributed Stochastic Gradient Descent Algorithm for Matrix Factorization <http://jmlr.org/proceedings/papers/v36/li14.pdf>`_, Fanglin Li, Bin Wu, Liutong Xu, Chuan Shi, Jing Shi
* `Parallelized Stochastic Gradient Descent <http://martin.zinkevich.org/publications/nips2010.pdf>`_, Martin A. Zinkevich, Markus Weimer, Alex Smola, Lihong Li
* `Topic Similarity Networks: Visual Analytics for Large Document Sets <http://arxiv.org/pdf/1409.7591v1.pdf>`_, Arun S. Maiya, Robert M. Rolfe
* `Low-dimensional Embeddings for Interpretable Anchor-based Topic Inference <http://mimno.infosci.cornell.edu/papers/EMNLP2014138.pdf>`_, Moontae Lee, David Mimno
* `K-means on Azure <http://apiacoa.org/publications/2010/durutrossi2010k-means-on.pdf>`_, Matthieu Durut, Fabrice Rossi
* `Confidence intervals for AB-test <http://arxiv.org/abs/1501.07768>`_, Cyrille Dubarry  

**Liens**

* `HackerRank <https://www.hackerrank.com/>`_
* `15+ Great Books for Hadoop <http://blog.matthewrathbone.com/2013/05/31/hadoop-resources---books.html>`_
* `A Roundup of Recent Text Analytics and Vis Work <http://blogger.ghostweather.com/2014/10/a-roundup-of-recent-text-analytics-and.html>`_
* `Don't use Hadoop - your data isn't that big <http://www.chrisstucchio.com/blog/2013/hadoop_hatred.html>`_
* `Remote Notebook with Azure <http://www.xavierdupre.fr/blog/2014-11-09_nojs.html>`_
* `Mahout 1.0 Features by Engine <https://mahout.apache.org/users/basics/algorithms.html>`_
* `Pig Advantages and Disadvantages <http://bugra.github.io/work/notes/2014-02-08/pig-advantages-and-disadvantages/>`_
* `Pig Not So Foreign Language Paper Notes <http://bugra.github.io/work/notes/2014-02-09/pig-not-so-foreign-language-paper-notes/>`_
* `Tutorial: Spark-GPU Cluster Dev in a Notebook <https://iamtrask.github.io/2014/11/22/spark-gpu/>`_
* `How CPU load averages work (and using them to triage webserver performance!) <http://jvns.ca/blog/2016/02/07/cpu-load-averages/>`_ *(2016/06)*

*Librairies / outils*

* `amazon-dsstne <https://github.com/amznlabs/amazon-dsstne>`_ : moteur de recommandation d'Amazon
* `Elastic Search <https://github.com/elastic/elasticsearch>`_ : moteur de recherche
* `Giraph <http://giraph.apache.org/>`_ : Large-scale graph processing on Hadoop 
* `Hadoop <http://hadoop.apache.org/>`_ : système de fichier distribué + Map Reduce simple
* `Kafka <http://kafka.apache.org/>`_ : distributed streaming platform, conçu pour stocker et récupérer en temps réel
   des événements de sites web
* `Mesos <http://mesos.apache.org/>`_ : Apache Mesos abstracts CPU, memory, storage, and other compute resources away from machines (physical or virtual)
  `Elixi <https://github.com/ceteri/exelixi/wiki>`_
* `MLlib <https://spark.apache.org/mllib/>`_ : distributed machine learning for Spark
* `Parquet <http://parquet.apache.org/>`_ : Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem.
* `Presto <https://prestodb.io/>`_ : Distributed SQL Query Engine for Big Data (Facebook)
* `pyCUDA <https://developer.nvidia.com/pycuda>`_ (`A Monte Carlo Option Pricer <http://nbviewer.jupyter.org/gist/harrism/835a8ca39ced77fe751d>`_ 
   avec `numbapro <http://docs.continuum.io/numbapro/>`_)
* `Spark <https://spark.apache.org/>`_ :  Map Reduce, minimise les accès disques,
  (`DPark <https://github.com/douban/dpark>`_ clone Python de Spark)
* `Spark SQL <https://spark.apache.org/sql/>`_ : SQL distribué, sur couche de Spark
* `Storm <https://storm.apache.org/>`_ : Apache Storm is a free and open source distributed realtime computation system,
  conçu pour distribuer des pipelines de traitements de données
* `YARN <https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/YARN.html>`_ : Ressource negociator

    
.. rubric:: Footnotes

.. [#fp1] C'est l'objet du paragraphe :ref:`l-td3a-start`.
        
.. [#f3write1] Contributeur et coordinateur du cours.

.. [#f3write2] Contributeur, encadrant.
          