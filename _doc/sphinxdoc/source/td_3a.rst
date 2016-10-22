

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




Concepts, théorie
=================

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

Distribution des calculs, stratégies de stockage, SQL NoSQL
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. toctree::
    :maxdepth: 2

    td_2a_s5_synthese


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

Exemples de scripts PIG
=======================

Trois projets réalisés par les élèves lors de l'année 2014-2015 :

.. toctree::
    :maxdepth: 1

    notebooks/2015_page_rank
    notebooks/2015_kmeans
    notebooks/2015_factorisation_matrice


.. _l-td3a-start:

Getting started
===============

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


.. _l-td3a-biblio:


Bibliographie
=============

**Documentation**

* `PIG tutorial <https://developer.yahoo.com/hadoop/tutorial/pigtutorial.html>`_
* `PIG <http://pig.apache.org/>`_, `PIG syntax <http://pig.apache.org/docs/r0.14.0/basic.html>`_
* `commandes HDFS <http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html>`_
* `commandes linux <http://doc.ubuntu-fr.org/tutoriel/console_commandes_de_base>`_
* `azure (python) <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/index.html>`_
* `WebHCat <http://docs.hortonworks.com/HDPDocuments/HDP1/HDP-1.2.1/bk_dataintegration/content/ch_using_hcatalog_1.html>`_
* `command pig <http://pig.apache.org/docs/r0.12.1/start.html#run>`_
* `HIVE <https://hive.apache.org/>`_

**Articles**

* `CUBE and ROLLUP: Two Apache Pig Functions That Every Data Scientist Should Know <http://joshualande.com/cube-rollup-pig-data-science/>`_
* `How to Read and Write JSON-formatted Data With Apache Pig <http://joshualande.com/read-write-json-apache-pig/>`_
* `What Every Data Scientist Needs to Know about SQL <http://joshualande.com/data-science-sql/>`_
* `Large Scale Distributed Deep Networks <http://www.cs.toronto.edu/~ranzato/publications/DistBeliefNIPS2012_withAppendix.pdf>`_, Jeffrey Dean, Greg S. Corrado, Rajat Monga, Kai Chen, Matthieu Devin, Quoc V. Le, Mark Z. Mao, Marc'Aurelio Ranzato, Andrew Senior, Paul Tucker, Ke Yang, Andrew Y. Ng
* `Stochastic Gradient Descent Tricks <http://research.microsoft.com/pubs/192769/tricks-2012.pdf>`_, Léon Bottou
* `A Fast Distributed Stochastic Gradient Descent Algorithm for Matrix Factorization <http://jmlr.org/proceedings/papers/v36/li14.pdf>`_, Fanglin Li, Bin Wu, Liutong Xu, Chuan Shi, Jing Shi
* `Parallelized Stochastic Gradient Descent <http://martin.zinkevich.org/publications/nips2010.pdf>`_, Martin A. Zinkevich, Markus Weimer, Alex Smola, Lihong Li
* `Topic Similarity Networks: Visual Analytics for Large Document Sets <http://arxiv.org/pdf/1409.7591v1.pdf>`_, Arun S. Maiya, Robert M. Rolfe
* `Low-dimensional Embeddings for Interpretable Anchor-based Topic Inference <http://mimno.infosci.cornell.edu/papers/EMNLP2014138.pdf>`_, Moontae Lee, David Mimno
* `K-means on Azure <http://apiacoa.org/publications/2010/durutrossi2010k-means-on.pdf>`_, Matthieu Durut, Fabrice Rossi
* `Efficient Estimation of Word Representations in Vector Space <http://arxiv.org/abs/1301.3781>`_, Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean,
  `Distributed Representations of Words and Phrases and their Compositionality <http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf>`_, Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, Jeff Dean,
  `word2vec Parameter Learning Explained <http://arxiv.org/abs/1411.2738>`_, Xin Rong,
  `Tutorial on Auto-Encoders <http://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_, Piotr Mirowski
* `Confidence intervals for AB-test <http://arxiv.org/abs/1501.07768>`_, Cyrille Dubarry  
* `Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing <http://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf>`_,
  Matei Zaharia, Mosharaf Chowdhury, Tathagata Das, Ankur Dave, Justin Ma, Murphy McCauley, Michael J. Franklin, Scott Shenker, Ion Stoica
* `From scikit-learn to Spark ML <http://blog.xebia.fr/2015/10/08/from-scikit-learn-to-spark-ml/>`_ *(2016/06)*

**Livres Map/Reduce**

* `Programming Pig <http://chimera.labs.oreilly.com/books/1234000001811/index.html>`_, Alan Gates (accessible en ligne)
* `Programming Hive <http://shop.oreilly.com/product/0636920023555.do>`_, Edward Capriolo, Dean Wampler, Jason Rutherglen
* `Hadoop: The Definitive Guide, 2nd Edition <http://shop.oreilly.com/product/0636920010388.do>`_, Tom White  (voir aussi `GitHub <https://github.com/tomwhite/hadoop-book/>`_)
* `Hadoop in Practice <http://it-ebooks.info/book/1028/>`_, Alex Holmes
* `Data-Intensive Text Processing with MapReduce <http://lintool.github.io/MapReduceAlgorithms/>`_, Jimmy Lin, Chris Dyer
* `Introducing Microsoft Azure HDInsight <http://blogs.msdn.com/b/microsoft_press/archive/2014/05/27/free-ebook-introducing-microsoft-azure-hdinsight.aspx>`_, Avkash Chauhan, Valentine Fontama, Michele Hart, Wee Hyong Tok, Buck Woody

**Livres GPU**

* `Thinking in C++ <http://mindview.net/Books/TICPP/ThinkingInCPP2e.html>`_, Bruce Eckel
* `Effective C++ <http://www.aristeia.com/books.html>`_, Scott Meyers
* `What Every Programmer Should Know About Memory <http://www.akkadia.org/drepper/cpumemory.pdf>`_, Ulrich Drepper
* `The Art of Multiprocessor Programming <http://edc.tversu.ru/elib/inf/0189.pdf>`_, Maurice Herlihy, Nir Shavit
* `An Introduction to GPGPU Programming - CUDA Architecture <http://www.diva-portal.org/smash/get/diva2:447977/FULLTEXT01.pdf>`_, Rafia Inam

**MOOC**

* `Introduction to Apache Pig <http://www.cloudera.com/content/cloudera/en/resources/library/training/introduction-to-apache-pig.html>`_

**Liens**

* `HackerRank <https://www.hackerrank.com/>`_
* `15+ Great Books for Hadoop <http://blog.matthewrathbone.com/2013/05/31/hadoop-resources---books.html>`_
* `A Roundup of Recent Text Analytics and Vis Work <http://blogger.ghostweather.com/2014/10/a-roundup-of-recent-text-analytics-and.html>`_
* :ref:`l-azurep`
* `Don't use Hadoop - your data isn't that big <http://www.chrisstucchio.com/blog/2013/hadoop_hatred.html>`_
* `Remote Notebook with Azure <http://www.xavierdupre.fr/blog/2014-11-09_nojs.html>`_
* `Mahout 1.0 Features by Engine <https://mahout.apache.org/users/basics/algorithms.html>`_
* `Pig Advantages and Disadvantages <http://bugra.github.io/work/notes/2014-02-08/pig-advantages-and-disadvantages/>`_
* `Pig Not So Foreign Language Paper Notes <http://bugra.github.io/work/notes/2014-02-09/pig-not-so-foreign-language-paper-notes/>`_
* `Tutorial: Spark-GPU Cluster Dev in a Notebook <https://iamtrask.github.io/2014/11/22/spark-gpu/>`_
* `How CPU load averages work (and using them to triage webserver performance!) <http://jvns.ca/blog/2016/02/07/cpu-load-averages/>`_ *(2016/06)*
* `TIL: clock skew exists (distributed system) <http://jvns.ca/blog/2016/02/10/til-clock-skew-exists/>`_ *(2016/06)*

**Librairies**

* `amazon-dsstne <https://github.com/amznlabs/amazon-dsstne>`_, moteur de recommandation d'Amazon
* `Chapel <http://chapel.cray.com/>`_
* `Giraph <http://giraph.apache.org/>`_
* `Kafka <http://kafka.apache.org/>`_
* `Mesos <http://mesos.apache.org/>`_, `Elixi <https://github.com/ceteri/exelixi/wiki>`_
* `MLlib <https://spark.apache.org/mllib/>`_ (`Mahout <http://mahout.apache.org/>`_ risque de disparaître)
* `Presto <https://prestodb.io/>`_
* `pyCUDA <https://developer.nvidia.com/pycuda>`_ (`A Monte Carlo Option Pricer <http://nbviewer.jupyter.org/gist/harrism/835a8ca39ced77fe751d>`_ avec `numbapro <http://docs.continuum.io/numbapro/>`_)
* `Spark <https://spark.apache.org/>`_ (`DPark <https://github.com/douban/dpark>`_)
* `Storm <https://storm.apache.org/>`_
* `YARN <https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/YARN.html>`_

**Revue de presse**

* `Microsoft, partenaire de la filière Data Science de l'ENSAE ParisTech avec Microsoft Azure Machine <http://www.microsoft.com/france/Hub-Presse/communiques-de-presse/fiche-communique.aspx?eid=f7e7f695-fb08-4c6d-b4ec-3cde562ba429>`_


    
.. rubric:: Footnotes

.. [#fp1] C'est l'objet du paragraphe :ref:`l-td3a-start`.
        
.. [#f3write1] Contributeur et coordinateur du cours.

.. [#f3write2] Contributeur, encadrant.
          