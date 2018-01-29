
.. _l-td2a-algo:

========================================
Algorithmes, Optimisation, Programmation
========================================

Agilité, rapidité, inventivité.

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

---------------

Scrapping, API, Site Web, Notebooks
===================================

.. contents::
    :local:
    :depth: 2

|pyecopng| |pystatpng|

.. _l-2a-scraping:

Webscrapping et API
+++++++++++++++++++

.. toctree::
    :maxdepth: 1

    notebooks/TD2A_eco_les_API

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

|pyecopng| |pystatpng|

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

|pystatpng|

Jupyter et les commandes magiques
+++++++++++++++++++++++++++++++++

.. toctree::
    :maxdepth: 1

    notebooks/jupyter_custom_magics
    notebooks/notebook_convert

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_magic_commands

---------------

Traiter les données rapidement pour de plus grands volumes
==========================================================

.. contents::
    :local:
    :depth: 2

|pystatpng|

.. _l-cluster-non-struct-2a:

Big data sans cluster, structures de données
++++++++++++++++++++++++++++++++++++++++++++

.. index:: itérateur

Beaucoup de jeux de données tiennent en mémoire mais les temps de calcul ou de chargement
même pour des choses simples sont parfois rédhibitoires. Parfois, on ne peut simplement pas
copier plus d'une fois le jeu de données sous peine de dépasser les capacités de la mémoire.
Face à ces obstacles, différentes stratégies sont possibles. Un échantillon aléatoire
conserve les propriétés statistiques mais réduit la taille mémoire. Les itérateurs
réduisent le temps le laps de temps entre le début de lecture des données et le début des
calculs. Ils ont aussi le mérité de n'utiliser que les données nécessaires lors des calculs :
les données défilent en mémoire. D'autres modules font en sorte qu'on puisse écrire des calculs
de la même manière alors que les données sont toujours sur le disque dur. D'autres compressent
les données et ne les décompressent que si besoin. Dans tous les cas, il s'agit de contourner
de façon intelligente la contrainte de volume. Et s'il n'y avait qu'une idée
à retenir, ce serait le concept d'ìtérateur <https://fr.wikipedia.org/wiki/It%C3%A9rateur>`_.

* `présentation données structurées <http://www.xavierdupre.fr/enseignement/complements/cours_structure_donnee.pdf>`_

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_no_sql_exo
    notebooks/dataframe_matrix_speed
    notebooks/ml_huge_datasets
    notebooks/ml_table_mortalite

*Notebooks*

.. toctree::
    :maxdepth: 2

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

*Modules*

* `dask <http://dask.pydata.org/en/latest/>`_
* `cytoolz <https://github.com/pytoolz/cytoolz>`_

|pystatpng|

Tensor, tableaux multidimensionnel
++++++++++++++++++++++++++++++++++

.. toctree::
    :maxdepth: 1

    notebooks/ml_table_mortalite

(à venir)

*Modules*

* `xarray <http://xarray.pydata.org/en/stable/>`_
* `xtensor-array <https://github.com/QuantStack/xtensor-python>`_
* `cubes <http://cubes.databrewery.org/>`_

|pystatpng|

.. _l-2a-cplusplus-para-serie:
.. _l-acc-code-llvm:

C++, Accélération de code
+++++++++++++++++++++++++

.. toctree::
    :maxdepth: 1

    notebooks/python_r
    notebooks/python_csharp
    notebooks/cffi_linear_regression

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_langages

*Lectures*

* :ref:`l-python_cplusplus`
* `sklearn-compiledtrees <https://github.com/ajtulloch/sklearn-compiledtrees/>`_ :
  création d'une implémentation C++ de la fonction de décision d'un arbre de décision entraîné avec
  scikit-learn
* `Just-in-time compilation <https://en.wikipedia.org/wiki/Just-in-time_compilation>`_

*Vidéos*

* `Making your code faster: Cython and parallel processing in the Jupyter Notebook <https://www.youtube.com/watch?v=MiHddLYZ6cQ>`_

*Modules*

* `cffi <https://cffi.readthedocs.io/en/latest/>`_
* `ctypes <https://docs.python.org/3/library/ctypes.html>`_
* `boost_python <http://www.boost.org/doc/libs/1_63_0/libs/python/doc/html/index.html>`_
* `pybind11 <https://github.com/pybind/pybind11/>`_
* `swig <http://www.swig.org/>`_
* `numba <https://numba.pydata.org/>`_ :
  JIT, compilation à la volée de certaines parties d'un code
* `nuitka <http://nuitka.net/>`_ :
  compilation d'un programme python ou d'un module
  (essaye de convertir un programe python en C)
* `pypy <https://pypy.org/>`_ :
  compilation d'un programme python ou d'un module
  (essaye de convertir un programe python en C)
* `cython <http://cython.org/>`_ :
  pseudo C (un mix entre C et Python), solution adoptée par scikit-learn

*Plus expérimental*

* `pythran <https://pythonhosted.org/pythran/>`_ : conversion de code python
  en C++ et compilation
* `pyston <https://github.com/dropbox/pyston>`_ (Python 2.7 seulement) :
  réécriture de l'interpréteur Python pour être plus rapide.

---------------

Meilleure efficacité avec des algorithmes
=========================================

.. contents::
    :local:
    :depth: 2

|pystatpng|

Parallélisation, sérialisation
++++++++++++++++++++++++++++++

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

|pystatpng|

.. _l-puzzlealgo2A:

Puzzles algorithmiques
++++++++++++++++++++++

.. toctree::

    td_2a_algo
    specials/nb_complet
    specials/algorithm_culture
    specials/problem_solved

*Notebooks*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_puzzle
    notebooks/_gs2a_puzzle_ml

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

*Modules*

* :ref:`Algorithmes classiques implémentés <l-blog-algo-impl>`

|pystatpng|

Algorithmes probabilistes
+++++++++++++++++++++++++

(*à venir*)

*Lectures*

* `Probabilistic Data Structures for Web Analytics and Data Mining <https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/>`_
* `HyperLogLog: the analysis of a near-optimal cardinality estimation algorithm <http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf>`_

*Modules*

* `hyperloglog <https://github.com/svpcom/hyperloglog>`_

|pystatpng|

Streaming algorithms
++++++++++++++++++++

Les algorithmes *streaming* que Wikipédia traduit par
`Algorithme de fouille de flots de données <https://fr.wikipedia.org/wiki/Algorithme_de_fouille_de_flots_de_donn%C3%A9es>`_
sont des algorithmes qui s'exécutent sans avoir connaissance de l'ensemble des données
ni même combien il y en a. Cela signifie que l'algorithme peut s'arrêter à tout moment
et qu'il est capable de retourner un résultat valide sur l'ensemble des données qu'il
a traités jusqu'à présent. L'algorithme le plus connu est sans aucun doute
`Reservoir Sampling <https://en.wikipedia.org/wiki/Reservoir_sampling>`_
qui permet de tirer un échantillon aléatoire dans un jeu de données dont la taille
est inconnue à l'avance.

* `Répartir train / test en streaming <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/split_train_test.html#streaming-splitting>`_

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_streaming

*Lectures*

* Algorithme BJKST `Counting distinct elements in a data stream <https://pdfs.semanticscholar.org/e349/7952347101a3535434bc35d378224cf87bcc.pdf>`_
* `Streaming Algorithms <http://resources.mpi-inf.mpg.de/departments/d1/teaching/ss14/gitcs/notes3.pdf>`_
* `Optimal streaming histograms <https://amplitude.com/blog/2014/08/06/optimal-streaming-histograms/>`_
* `Density Estimation Over Data Stream <http://alumni.cs.ucr.edu/~wli/publications/deosd.pdf>`_
* `Confidence Decision Trees via Online and Active Learning for Streaming (BIG) Data <https://arxiv.org/pdf/1604.03278.pdf>`_
* `Approximation and Streaming Algorithms for Histogram Construction Problems <http://www.mathcs.emory.edu/~cheung/papers/StreamDB/Histogram/2005-Guha-Histogram.pdf>`_
* `State-of-the-art on clustering data streams <https://bdataanalytics.biomedcentral.com/articles/10.1186/s41044-016-0011-3>`_
* `Parallel Computing of Kernel Density Estimates with MPI <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.102.5195&rep=rep1&type=pdf>`_
* `Density Estimation with Adaptive Sparse Grids for Large Data Sets <http://web.mit.edu/pehersto/www/preprints/sgde_siam.pdf>`_
* `Sliding HyperLogLog: Estimating cardinality in a data stream <https://hal.archives-ouvertes.fr/file/index/docid/465313/filename/sliding_HyperLogLog.pdf>`_
* `Data Streaming Algorithms 2009 <http://www.cs.dartmouth.edu/~ac/Teach/CS85-Fall09/Notes/lecnotes.pdf>`_,
  `Data Streaming Algorithms 2011 <http://www.cs.dartmouth.edu/~ac/Teach/CS49-Fall11/Notes/lecnotes.pdf>`_
* `Data Stream Management <http://web.cs.ucla.edu/classes/winter17/cs240B/notes/DataStreamMg.pdf>`_
  (collection d'articles)

*Modules*

* `StreamLib <https://github.com/jiecchen/StreamLib>`_
* `pandas_streaming <https://github.com/sdpython/pandas_streaming/>`_
* `streamparse <https://github.com/Parsely/streamparse>`_

------------

Machine Learning en environnement contraint
===========================================

Les objets connectés sont petits et ne possède pas la puissance
de calculs des ordinateurs. Il faut adapter les algorithmes de machines
learning pour ces environnements. Dans la plupart des cas, cela signifie apprendre
sur un ordinateur, exporter le modèle dans l'objet connecté et prédire sans
connexion extérieure. Dans le meilleur des cas, cela signifie aussi apprendre
dans l'objet connecté avec des contraintes assez fortes sur la mémoire et
la puissance de calculs.

|pystatpng|

Prédire en environnement contraint
++++++++++++++++++++++++++++++++++

C'est l'option la plus facile. Elle consiste à apprendre
sur un ordinateur classique puis à exporter le modèle dans un environnement
différent où seule la prédiction est disponible. On l'appelle parfois
le *runtime*. Il existe encore peu d'outils communs même s'il est fortement
probable que chacun ait développé des outils en interne adaptés à son architecture.
Il est très facile d'apprendre une régression logistique puis de réimplémenter
la fonction de prédiction partout où on en a besoin avec les coefficients
du modèle plutôt que de chercher à installer :epkg:`Python`.

*Modules*

* `Embedded Learning Library (ELL) <https://github.com/Microsoft/ELL>`_ :
  deep learning sur :epkg:`RaspberryPI`, :epkg:`Arduino`
* `onnx <https://github.com/onnx/onnx>`_
* `coremltools <https://pypi.python.org/pypi/coremltools>`_

|pystatpng|

Apprendre en environnement contraint
++++++++++++++++++++++++++++++++++++

*(à venir)*

*Lectures*

* `ProtoNN: Compressed and Accurate kNN for Resource-scarce Devices <http://manikvarma.org/pubs/gupta17.pdf>`_
* `Near-optimal sample compression for nearest neighbors <https://papers.nips.cc/paper/5528-near-optimal-sample-compression-for-nearest-neighbors.pdf>`_
* `Joint learning and pruning of decision forests <https://www.kuleuven-kulak.be/benelearn/papers/Benelearn_2016_paper_53.pdf>`_
* `Optimally Pruning Decision Tree Ensembles With Feature Cost <https://arxiv.org/abs/1601.00955>`_
* `Cost-complexity pruning of random forests <https://arxiv.org/pdf/1703.05430.pdf>`_
* `A Compression Approach to Support Vector Model Selection <http://www.jmlr.org/papers/volume5/luxburg04a/luxburg04a.pdf>`_
* `Resource-efficient Machine Learning in 2 KB RAM for the Internet of Things <http://proceedings.mlr.press/v70/kumar17a/kumar17a.pdf>`_

*Modules*

* `EdgeML <https://github.com/Microsoft/EdgeML>`_ :
  entraîner un modèle lorsqu'on a peu de mémoire.

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
