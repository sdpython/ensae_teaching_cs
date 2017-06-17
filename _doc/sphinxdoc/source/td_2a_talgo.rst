
.. _l-td2a-algo:

================================
Le coin du programmeur astucieux
================================

Agilité, rapidité, inventivité.

.. contents::
    :local:

.. |pyecopng| image:: _static/pyeco.png
            :alt: Economie

.. |pystatpng| image:: _static/pystat.png
            :alt: Statistique

---------------

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

*Modules*

* `dask <http://dask.pydata.org/en/latest/>`_
* `cytoolz <https://github.com/pytoolz/cytoolz>`_

Tensor, tableaux multidimensionnel
++++++++++++++++++++++++++++++++++

|pystatpng|

(à venir)

*Modules*

* `xarray <http://xarray.pydata.org/en/stable/>`_
* `xtensor-array <https://github.com/QuantStack/xtensor-python>`_
* `cubes <http://cubes.databrewery.org/>`_

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

*Modules*

* `cython <http://cython.org/>`_
* `ctypes <https://docs.python.org/3/library/ctypes.html>`_
* `boost_python <http://www.boost.org/doc/libs/1_63_0/libs/python/doc/html/index.html>`_
* `pybind11 <https://github.com/pybind/pybind11/>`_

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

* `Répartir train / test en streaming <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/split_train_test.html#streaming-splitting>`_

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_streaming

*Lectures*

* Algorithme `BJKST <http://info.prelert.com/blog/hashing-and-approximate-distinct-value-counts>`_
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
