
.. _l-td3a:


3A
==

`Eléments logiciels pour le traitement des données massives - OMI309 <http://www.ensae.fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/3me-anne-voies-de-spcialisation-formationsdiplome-96/data-science-cours-3a.html?id=100729>`_


En cours de rédaction

Cours animé par :

* Matthieu Durut
* Xavier Dupré


    
- :ref:`Séance 1 :  <td3acenoncesession1rst>`  (:ref:`correction <td3acorrectionsession1rst>`)
    * `liste chaînées <http://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e>`_, `stack <http://fr.wikipedia.org/wiki/Pile_(informatique)>`_, `queue <http://en.wikipedia.org/wiki/Queue_(abstract_data_type)>`_, `dictionnaire <http://en.wikipedia.org/wiki/Associative_array>`_
    * graphe `BFS <http://en.wikipedia.org/wiki/Breadth-first_search>`_, `DFS <http://en.wikipedia.org/wiki/Depth-first_search>`_
    * `merge sort <http://en.wikipedia.org/wiki/Merge_sort>`_, `quicksort <http://en.wikipedia.org/wiki/Quicksort>`_, `heapsort <http://en.wikipedia.org/wiki/Heapsort>`_, `max heap <http://en.wikipedia.org/wiki/Min-max_heap>`_
- Séance 2
    * threads, application multi-threadées
    * variables globales, synchronisation
- Séance 3
    * Stockage de données, consistence, persistence, impossibilité de faire des rollbacks, corruption, 
      absence de garanties sur la manière dont sont stockés les champs (exemple formats de date), pas d'index, etc.
    * Introduction du SQL, type de requêtes, 
      Notion de transaction, d'atomicité, capacité de rollback, garanties ACID, 
      difficultés dans un SQL réparti (atomicité des transactions, double commit protocol)
    * Systèmes NoSQL, Key-Value Pair Storage, transactionnalité multi-entités dans un Key-Value pair, 
      écriture optimiste avec des timestamps.
    * Base de données orientées Document, Bases de données orientées Graph
    * Map/Reduce. Notions de mappers, de reducers, de calculs embarassingly parallel. 
      problèmes des machines mortes, des stragglers, tradeof calcul/transfert des données,
      exemples d'applications de MapReduce,
      exemples d'algos difficilement parallélisables,
    * Hadoop, Azure
    * Queues distribuées.
- Séance 4
    * distribuer un traitement de données à différent niveaux
        * avec un langage haut niveau (comme PIG)
        * utilisation du java pour distribuer un job de façon plus optimisée
        * distribution personnalisée d'un traitement avec des librairies bas niveau (type MPI)
- Séance 5
    * algorithme distribué, descente de gradient distributé
    * exemple des `k-means <http://fr.wikipedia.org/wiki/Algorithme_des_k-moyennes>`_ distribué
    * `GPU <http://fr.wikipedia.org/wiki/Processeur_graphique>`_

Les trois séances suivantes sont plus appliquées et dédiées à la découverte
de `Hadoop <http://fr.wikipedia.org/wiki/Hadoop>`_, un environnement
qui permet d'exécuter des tâches 
`Map/Reduce <http://fr.wikipedia.org/wiki/MapReduce>`_. 
Plusieurs angles d'approche sont possibles. Celle retenue est l'utilisation
du langage `PIG-latin <http://en.wikipedia.org/wiki/Pig_Latin>`_ dont la logique
ressemble beaucoup à celle du `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_.
Les outils Python [#fp1]_ simplifient la communication avec le cluster.

- Séance 6 : premier job Map/Reduce
    * `ENSAE 3A - Map/Reduce en pratique <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_3A/index.html>`_
    * Exercice recommandé : `SQL Magic Commands with SQLite in a Notebook <http://www.xavierdupre.fr/app/pyensae/helpsphinx/notebooks/pyensae_sql_magic.html>`_
    * Travaux pratiques
        * Cloudera - :ref:`Séance 6 : <td3acenoncesession6rst>`  (:ref:`correction <td3acorrectionsession6rst>`)
        * Azure HDInsight - :ref:`Séance 6 : <td3acenoncesession6brst>`  (:ref:`correction <td3acorrectionsession6brst>`)
    * Contenu
        * manipulation de fichiers avec `HDFS <http://hadoop.apache.org/docs/r1.2.1/hdfs_design.html>`_
        * premier job avec `PIG-latin <https://pig.apache.org/docs/r0.7.0/piglatin_ref2.html>`_ [#fp2]_
        * parallèle entre la syntaxe `PIG <http://pig.apache.org/docs/r0.12.1/basic.html>`_ et `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_

- Séance 7 : PIG, JSON, streaming
    * :ref:`PIG et JSON <td3acenoncesession7arst>`  (:ref:`correction <td3acorrectionsession7arst>`) (avec Azure)

Le cours sera évalué avec un :ref:`projet informatique <l-projinfo3a>`.


.. _l-td3a-start:

Getting started
+++++++++++++++

La plupart des modules requis sont inclus dans la distribution
`Anaconda <http://continuum.io/downloads#py34>`_ de Python. A ceux-ci, il faut ajouter :

* `ansiconv <http://pythonhosted.org/ansiconv/>`_,
* `ansi2html <https://github.com/ralphbean/ansi2html/>`_.
* `azure <https://github.com/Azure/azure-sdk-for-python>`_ (pour Azure uniquement)

Les deux modules suivantes introduisent les commandes magiques utilisées dans les notebooks :

* `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_ (version >= 1.0)

Il faudra également installer (pour Cloudera uniquement) :

* `paramiko <http://www.paramiko.org/>`_
* `ecdsa <https://pypi.python.org/pypi/pycrypto/>`_
* `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_

Ces modules sont plus faciles à installer avec `Anaconda <http://continuum.io/downloads#py34>`_ 
(commande ``conda install paramiko``, lire `install extra packages <http://docs.continuum.io/anaconda/faq.html#install-packages>`_).
Le module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_
(voir :ref:`l-install`), il suffit d'exécuter ::

    from pymyinstall import datascientist
    datascientist("install", azure = True)

Liens :

* `Remote Notebook with Azure <http://www.xavierdupre.fr/blog/2014-11-09_nojs.html>`_

.. _l-td3a-biblio:


Bibliographie
+++++++++++++

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

**Livres**

* `Thinking in C++ <http://mindview.net/Books/TICPP/ThinkingInCPP2e.html>`_, Bruce Eckel
* `Effective C++ <http://www.aristeia.com/books.html>`_, Scott Meyers
* `What Every Programmer Should Know About Memory <http://www.akkadia.org/drepper/cpumemory.pdf>`_, Ulrich Drepper
* `The Art of Multiprocessor Programming <http://edc.tversu.ru/elib/inf/0189.pdf>`_, Maurice Herlihy, Nir Shavit
* `Hadoop: The Definitive Guide, 2nd Edition <http://shop.oreilly.com/product/0636920010388.do>`_, Tom White  (voir aussi `GitHub <https://github.com/tomwhite/hadoop-book/>`_)
* `Hadoop in Practice <http://it-ebooks.info/book/1028/>`_, Alex Holmes
* `Data-Intensive Text Processing with MapReduce <http://lintool.github.io/MapReduceAlgorithms/>`_, Jimmy Lin, Chris Dyer
* `Introducing Microsoft Azure HDInsight <http://blogs.msdn.com/b/microsoft_press/archive/2014/05/27/free-ebook-introducing-microsoft-azure-hdinsight.aspx>`_, Avkash Chauhan, Valentine Fontama, Michele Hart, Wee Hyong Tok, Buck Woody
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

**Revue de presse**

* `Microsoft, partenaire de la filière Data Science de l'ENSAE ParisTech avec Microsoft Azure Machine <http://www.microsoft.com/france/Hub-Presse/communiques-de-presse/fiche-communique.aspx?eid=f7e7f695-fb08-4c6d-b4ec-3cde562ba429>`_

.. toctree::
    :hidden:
    
    td_3a_enonce
    td_3a_correction
    specials/azure
    
.. rubric:: Footnotes

.. [#fp1] C'est l'objet du paragraphe :ref:`l-td3a-start`.

.. [#fp2] Les exercices des notebooks s'appuient sur le langage `PIG-latin <http://en.wikipedia.org/wiki/Pig_Latin>`_ qui est un langage
          haut niveau permettant d'écrire des tâches Map Reduce complexes. Le script est ensuite converti en un ensemble de 
          `mapper / reducer <http://hadooptutorial.wikispaces.com/MapReduce>`_. 
          Ce langage suffit dans la plupart des cas
          et le temps de développement est très réduit par rapport à un langage plus bas niveau.
          L'autre langage haut niveau est `Hive <https://hive.apache.org/>`_. Sa syntaxe est très proche de celle
          du `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_. 
          `PIG <http://en.wikipedia.org/wiki/Pig_Latin>`_ a été choisi
          car `Hive <https://hive.apache.org/>`_ est plus un moyen de lancer rapidement de petites
          tâches, PIG permet des tâches plus conséquentes pour un coût d'apprentissage
          très raisonnable.
          