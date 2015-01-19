

.. issue.

.. _l-data2a:


Python pour un Data Scientist
=============================

Manipuler les données est différent de savoir programmer.
Si le second est nécessaire au premier, il est impensable
aujourd'hui de ne pas tenir compte ce que d'autres programmeurs
ont mis à disposition de tous en libre accès. Tous les modules proposés 
dans la suite sont utilisées par beaucoup, et sont très adaptés 
à la manipulation des données.
Ils bénéficient de ce fait
d'un développement rapide et d'une robustesse qu'il faut environ un an à un bon 
programmeur pour obtenir avec un de ses outils 
sur le même éventail de fonctionnalités (en y consacrant 10 à 20% de son temps).

J'ai cherché à regrouper les outils qui permettent à un ingénieur,
statisticiens, data scientist de manipuler aisément des données,
qui peuvent aller de quelques kilo-octets à quelques giga octets.
En tant que data scientist, je pioche très régulièrement des éléments
des sept premiers chapitres. Les sept suivants ne sont utiles que de temps en temps,
surtout si les données sont de taille supérieure à 250 Mo.

L'essentiel n'est pas de tout faire en Python, l'essentiel est d'être agile,
de passer le moins de temps sur l'implémentation et le plus de temps possible
sur les données.



Usage régulier
++++++++++++++

#. Introduction aux différents environnements de programmation (pas très long)
    a. Installation : 
        - `Anaconda <http://continuum.io/downloads#py34>`_
        - `WinPython <http://winpython.sourceforge.net/>`_ (seulement sur Windows, moins rapide au niveau des mises à jour que Anaconda)
        - `Canopy <https://www.enthought.com/products/canopy/>`_ (Python 3 n'a pas l'air disponible)
        - `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ 
        - `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_
    b. Environnements
        - `IDLE <https://docs.python.org/3.4/library/idle.html>`_
        - `ligne de commande IPython <http://ipython.org/ipython-doc/2/interactive/reference.html>`_
        - `Spyder <http://pythonhosted.org//spyder/>`_  (environnement de type `RStudio <http://www.rstudio.com/>`_)
        - `Notebooks <http://ipython.org/notebook.html>`_
    c. Editeur de texte (pour des projets plus ambitieux, SciTE, PyCharm, PyTools, WingIDE)
        - `Scite <http://www.scintilla.org/SciTE.html>`_
        - `PyCharm <http://www.jetbrains.com/pycharm/>`_
        - `PyTools <http://pytools.codeplex.com/>`_
        - `WingIDE <https://wingware.com/>`_
    d. Liens
        - `Formation à Python scientifique - ENS Paris <http://python-prepa.github.io/index.html>`_

#. `Pandas <http://pandas.pydata.org/>`_
    a. Récupérer des données depuis un fichier plat
    b. Encoding
    c. Notion de dataframe
    d. Valeur manquantes
    e. Manipuler les données façon SQL (group by, join, union, filter)
    f. Manipulation customisée (avec fonction lambda)
    g. Récupération depuis d'autre sources (SQL, fichiers Excel, sqlite3)
    h. Séries temporelles
    i. Autres fonctionnalités (describe, histogram...)
    j. Données "sparse" ou creuses
    h. Grandes tables (> 250Mo) (en dessous ça tient en mémoire facilement et les calculs sont assez rapides), modules pytables, blaze, SQLAchemy, http://www.pytables.org/docs/LargeDataAnalysis.pdf, SQLiteSpy, `h5py <http://www.h5py.org/>`_
    i. `pandas cookbook <http://pandas.pydata.org/pandas-docs/stable/cookbook.html>`_
    j. `cytoolz <https://github.com/pytoolz/cytoolz/>`_
    k. `toolz <https://github.com/pytoolz/toolz/>`_

#. `Numpy <http://www.numpy.org/>`_, `Scipy <http://www.scipy.org/>`_, `cvxopt <http://cvxopt.org/>`_
    a. Notation avec ``:``
    b. Calcul matriciel
    c. Convertir des boucles en calcul matriciel, écrire du code rapide
    d. Distinction numpy.matrix, numpy.array, matrices creuses (sparse)
    e. Valeur propres / vecteur propres
    f. Optimisation, optimisation sous Contraintes
    g. Optimisation sous contrainte avec cvxopt

#. Visualisation
    a. images
        - `matplotlib <http://matplotlib.org/>`_
        - `seaborn <http://stanford.edu/~mwaskom/software/seaborn/installing.html>`_
        - `matplotlib et pandas <http://pandas.pydata.org/pandas-docs/stable/visualization.html>`_
        - `prettyplotlib <http://olgabot.github.io/prettyplotlib/>`_
        - `ggplot <https://github.com/yhat/ggplot>`_ 
        - `vincent <http://vincent.readthedocs.org/>`_
    b. cartes
        - `cartopy <http://scitools.org.uk/cartopy/>`_
        - `basemap <http://matplotlib.org/basemap/>`_
        - `shapely <https://pypi.python.org/pypi/Shapely>`_, `documentation <http://toblerity.org/shapely/index.html>`_
        - `mapnik <http://mapnik.org/>`_
        - `geos <http://trac.osgeo.org/geos/>`_
        - `GDAL <https://pypi.python.org/pypi/GDAL/>`_
        - video `Spatial data and web mapping with Python <http://www.youtube.com/watch?v=qmgh14LUOjQ&feature=youtu.be>`_
    c. interactif (javascript)
        - `mpld3 <http://mpld3.github.io/>`_
        - `bokeh <http://bokeh.pydata.org/>`_
        - `d3js <http://d3js.org/>`_, `d3js gallery <http://christopheviau.com/d3list/>`_, `ipyD3 <http://nbviewer.ipython.org/github/z-m-k/ipyD3/blob/master/ipyD3sample.ipynb>`_, `nvd3 <http://nvd3.org/>`_
        - `python-nvd3 <https://pypi.python.org/pypi/python-nvd3/>`_
        - `vispy <http://vispy.org/index.html>`_
        - `IVisual <https://pypi.python.org/pypi/IVisual/>`_
    d. others directions (pas facile à mettre en place)
        - `tessera <https://github.com/urbanairship/tessera>`_
        - `graphite <https://github.com/graphite-project>`_
    e. services (il faut d'identifier)
        - `plotly <https://plot.ly/python/>`_
        - `datawrapper <https://datawrapper.de/>`_ (utiliser par le journal l'Equipe)    

#. machine learning `Scikit-learn <http://scikit-learn.org/stable/>`_
    a. `scikit lectures <http://scipy-lectures.github.io/>`_
    b. ADD avec Python (ACP, CAH, clustering)
    c. Machine learning (régression, modèles prédictifs)
    d. `autres modules <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
    e. `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
    f. `DataFrame et SQLite3 <http://www.xavierdupre.fr/app/pyensae/helpsphinx/notebooks/pyensae_flat2db3.html>`_
    g. `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html>`_
    h. `statsmodels <http://statsmodels.sourceforge.net/>`_
    i. `fastcluster <https://pypi.python.org/pypi/fastcluster>`_
    j. `lda <https://github.com/ariddell/lda>`_ (`LDA <http://en.wikipedia.org/wiki/Latent_Dirichlet_allocation>`_)
    k. `NLTK <http://www.nltk.org/install.html>`_ (natural language processing)
    l. `glove-python <https://github.com/maciejkula/glove-python>`_
    m. `patsy <http://patsy.readthedocs.org/en/latest/index.html>`_
    n. `sqlite_bro <https://github.com/stonebig/sqlite_bro>`_

#. Représentation de graphes
    a. `Graphviz <https://github.com/xflr6/graphviz>`_
    b. `Networkx <https://networkx.github.io/>`_
    c. `neo4j <http://www.neo4j.org/develop/python>`_
    d. `python-igraph <http://igraph.org/python/>`_

#. Représentation de données structurées, NoSQL
    a. différences avec les bases de données traditionnelles (tables)
    b. format `JSON <http://fr.wikipedia.org/wiki/JavaScript_Object_Notation>`_, `XML <http://fr.wikipedia.org/wiki/Extensible_Markup_Language>`_ pour les `données structurées <http://en.wikipedia.org/wiki/Semi-structured_data>`_
    c. `NoSQL <http://fr.wikipedia.org/wiki/NoSQL>`_ définition
    d. `unqlitepy <https://github.com/nobonobo/unqlitepy>`_ (`unqlite <http://unqlite.org/>`_), `cassandra-driver <https://github.com/datastax/python-driver>`_ (`Cassandra <http://cassandra.apache.org/>`_)
    e. `pymongo <http://docs.mongodb.org/ecosystem/drivers/python/>`_ (installation depuis `pymongo pipy <https://pypi.python.org/pypi/pymongo/>`_, `MongoDB <http://www.mongodb.org/>`_), `py-couchdb <https://py-couchdb.readthedocs.org/en/latest/>`_ (`CouchDB <http://couchdb.apache.org/>`_)

#. Calcul distribué  
    a. Multithreading (local)
    b. `GPU <http://fr.wikipedia.org/wiki/Processeur_graphique>`_ : `pycuda <http://mathema.tician.de/software/pycuda/>`_, `theano <http://deeplearning.net/software/theano/>`_
    c. Plusieurs machines ou plusieurs coeurs (ipython, lzmq, ...)
    d. Workflow (`luigi <http://luigi.readthedocs.org/en/latest/>`_, `papy <http://arxiv.org/ftp/arxiv/papers/1407/1407.4378.pdf>`_)
    e. `joblib <https://pythonhosted.org/joblib/>`_

#. Python et autres langages (C++, Cypthon, C#, R) 
    a. `Cython <http://cython.org/>`_ (voir aussi `cffi <https://cffi.readthedocs.org/>`_)
    b. autres langages
        - C# avec `pythonnet <https://github.com/renshawbay/pythonnet>`_
        - R avec `rpy2 <http://rpy.sourceforge.net/>`_
        - Java avec `py4j <http://py4j.sourceforge.net/>`_, `JPype <http://jpype.sourceforge.net/>`_, `pyjnius <http://pyjnius.readthedocs.org/en/latest/>`_
        - Octave avec `IPython <http://nbviewer.ipython.org/github/blink1073/oct2py/blob/master/example/octavemagic_extension.ipynb>`_, IPython reconnaît la syntaxe (Octave = équivalent gratuit de Matlab)
        - Scilab avec `sciscipy <https://www.scilab.org/fr/scilab/interoperability/calculation_engine/python>`_
        - Matlab avec `pymatbridge <https://github.com/jaderberg/python-matlab-bridge>`_, `mlab <https://github.com/ewiger/mlab>`_, néanmoins ces modules ne semblent pas très aboutis
        - Julia voir `IJulia <https://github.com/JuliaLang/IJulia.jl>`_
    c. `PyPy <http://pypy.org/>`_, `nuitka <http://nuitka.net/>`_, `mypy <http://www.mypy-lang.org/>`_
    d. Écriture de librairies en C++
        - `boost.python <http://www.boost.org/doc/libs/1_55_0/libs/python/doc/>`_
        - `SWIG <http://www.swig.org/>`_



Usage irrégulier
++++++++++++++++

1. Outils pour mieux développer
    a. Tests unitaires
    b. `Vérification de types <http://www.xavierdupre.fr/blog/2014-08-20_nojs.html>`_
    c. Profiling (`cprofile <https://docs.python.org/3.4/library/profile.html>`_, `yappi <https://pypi.python.org/pypi/yappi/>`_)
    d. debugger (avec `pytools <http://pytools.codeplex.com/>`_)
    e. Github, bitbucket, Tortoisegit, tortoisesvn
    f. Génération d'une documentation avec sphinx
    g. Créer un setup pour un module
    h. Créer un exécutable cx_Freeze
    
2. Traitement d'images
    a. `Pillow <http://pillow.readthedocs.org/en/latest/>`_
    b. `Opencv <http://docs.opencv.org/master/doc/py_tutorials/py_tutorials.html>`_
    
3. Un siteweb en python
    a. `Flask <http://flask.pocoo.org/>`_
    b. `Django <http://www.django-fr.org/>`_
    c. `pyjs <http://pyjs.org/>`_
    d. `brython <http://www.brython.info/index.html>`_  (pour remplacer le javascript par du python)
    e. `autobahn/python <http://autobahn.ws/python/>`_ (programmation événementielle pour un site web)
    
4. Python sur tablette, téléphone
    a. `kivy <http://kivy.org/#home>`_
    
5. Statistiques bayésiennes
    a. `pymc <https://github.com/pymc-devs/pymc>`_
    b. `pystan <http://pystan.readthedocs.org/en/latest/index.html>`_
    
6. `Data Cube <http://en.wikipedia.org/wiki/Data_cube>`_ (Wikipédia)
    * modules plutôt expérimentaux
        * `cubes <https://github.com/Stiivi/cubes>`_
        * `cubesviewer <https://github.com/jjmontesl/cubesviewer>`_
        * `cube-client <https://github.com/tsileo/cube-client>`_
        
7. Algorithmie        
    * `Woodbury matrix identity <http://en.wikipedia.org/wiki/Woodbury_matrix_identity>`_
    * `Blockwise inversion <http://en.wikipedia.org/wiki/Invertible_matrix#Blockwise_inversion>`_
    
8. Mining en tout genre
    * `scrapy <http://scrapy.org/>`_ : scraping
    * `whoosh <http://pythonhosted.org//Whoosh/>`_ (moteur de recherche)
    * `elastic search <http://www.elasticsearch.org/guide/en/elasticsearch/client/python-api/current/>`_ 
    * `pattern <http://www.clips.ua.ac.be/pattern>`_
    
9. Calcul en grande dimension
    a. calcul en grande précision `gmpy2 <http://gmpy2.readthedocs.org/en/latest/>`_



Articles
++++++++
    * `Gradient Boosted Regression Trees <http://orbi.ulg.ac.be/bitstream/2268/163521/1/slides.pdf>`_
    * `A Reliable Effective Terascale Linear Learning System <http://arxiv.org/pdf/1110.4198v3.pdf>`_
    * `Understanding Random Forest <http://orbi.ulg.ac.be/handle/2268/170309>`_
    * `scikit lectures <http://scipy-lectures.github.io/>`_
    * `Formation à Python scientifique - ENS Paris <http://python-prepa.github.io/index.html>`_
    * `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
    * `Python Tools for Machine Learning <http://www.cbinsights.com/blog/python-tools-machine-learning/>`_
    * `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
    * `22 outils gratuits pour visualiser et analyser les données (1ère partie) <http://www.lemondeinformatique.fr/actualites/lire-22-outils-gratuits-pour-visualiser-et-analyser-les-donnees-1ere-partie-47241-page-3.html>`_


Liens
+++++

- Blog: 
    - `Sebastian Raschka <http://sebastianraschka.com/articles.html>`_
    - `yhat <http://blog.yhathq.com/>`_
- Sites
    - `NumFOCUS Foundation <http://numfocus.org/projects/index.html>`_
    - `pythonworks.org <http://www.pythonworks.org/home>`_ (références de livres)
- Articles
    - `Scikit-learn: Machine Learning in Python <http://jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf>`_ (avec les auteurs de scikit-learn)
- Livres
    - Building Machine Learning Systems with Python by Willi Richert, Luis Pedro Coelho published by PACKT PUBLISHING (2013) 
    - Machine Learning in Action by Peter Harrington
    - `Probabilistic Programming and Bayesian Methods for Hackers <http://nbviewer.ipython.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Prologue/Prologue.ipynb>`_
- Vidéo
    - `Scikit-Learn: Machine Learning en Python <http://www.microsoft.com/france/mstechdays/programmes/2014/fiche-session.aspx?ID=295be946-2c69-458a-8545-bcebe7970fd8>`_
    - `HDInsight : Hadoop en environnement Microsoft <http://www.microsoft.com/france/mstechdays/programmes/2013/fiche-session.aspx?ID=bb6cbb87-c370-477e-8fd4-b46f9ca292d0>`_

