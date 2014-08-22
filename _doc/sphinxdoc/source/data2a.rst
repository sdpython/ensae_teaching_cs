
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

1. Introduction aux différents environnements de programmation (pas très long)
    a. Installation : 
        - `WinPython <http://winpython.sourceforge.net/>`_, 
        - `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ 
        - `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_
    b. Environnements
        - `IDLE <https://docs.python.org/3.4/library/idle.html>`_
        - `ligne de commande IPython <http://ipython.org/ipython-doc/2/interactive/reference.html>`_
        - `Spyder <http://pythonhosted.org//spyder/>`_  (environnement de type `RStudio <http://www.rstudio.com/>`_)
        - `Notebooks <http://ipython.org/notebook.html>`_
    c. Editeur de texte (pour des projets plus ambitieux, SciTE, PyCharm, PyTools)
        - `Scite <http://www.scintilla.org/SciTE.html>`_
        - `PyCharm <http://www.jetbrains.com/pycharm/>`_
        - `PyTools <http://pytools.codeplex.com/>`_
    d. Liens
        - `Formation à Python scientifique - ENS Paris <http://python-prepa.github.io/index.html>`_
        
2. `Pandas <http://pandas.pydata.org/>`_
    a. Récupérer des données depuis un fichier plat
    b. Encoding
    c. Notion de dataframe
    d. Valeur manquantes
    e. Manipuler les données façon SQL (group by, join, union, filter)
    f. Manipulation customisée (avec fonction lambda)
    g. Récupération depuis d'autre sources (SQL, fichiers Excel, sqlite3)
    h. Séries temporelles
    i. Autres fonctionnalités (describe, histogram…)
    j. Données "sparse" ou creuses
    h. Grandes tables (> 250Mo) (en dessous ça tient en mémoire facilement et les calculs sont assez rapides), modules pytables, blaze, SQLAchemy, http://www.pytables.org/docs/LargeDataAnalysis.pdf, SQLiteSpy, `HDF5 <http://www.h5py.org/>`_
    
    
3. `Numpy <http://www.numpy.org/>`_, `Scipy <http://www.scipy.org/>`_, `cvxopt <http://cvxopt.org/>`_
    a. Notation avec ``:``
    b. Calcul matriciel
    c. Convertir des boucles en calcul matriciel, écrire du code rapide
    d. Distinction numpy.matrix, numpy.array, matrices creuses (sparse)
    e. Valeur propres / vecteur propres
    f. Optimisation, optimisation sous Contraintes
    g. Optimisation sous contrainte avec cvxopt
    
4. Visualisation
    a. images
        - `matplotlib <http://matplotlib.org/>`_
        - `prettyplotlib <http://olgabot.github.io/prettyplotlib/>`_
        - `ggplot <https://github.com/yhat/ggplot>`_ 
    b. cartes
        - `cartopy <http://scitools.org.uk/cartopy/>`_
        - `basemap <http://matplotlib.org/basemap/>`_
        - `shapely <https://pypi.python.org/pypi/Shapely>`_, `documentation <http://toblerity.org/shapely/index.html>`_
        - `mapnik <http://mapnik.org/>`_
        - `geos <http://trac.osgeo.org/geos/>`_
        - `GDAL <https://pypi.python.org/pypi/GDAL/>`_
        - video `Spatial data and web mapping with Python <http://www.youtube.com/watch?v=qmgh14LUOjQ&feature=youtu.be>`_
    c. interactif (javascript)
        - `plotly <https://plot.ly/python/>`_
        - `bokeh <http://bokeh.pydata.org/>`_
        - `d3js <http://d3js.org/>`_, `d3js gallery <http://christopheviau.com/d3list/>`_, `ipyD3 <http://nbviewer.ipython.org/github/z-m-k/ipyD3/blob/master/ipyD3sample.ipynb>`_, `nvd3 <http://nvd3.org/>`_
        - `python-nvd3 <https://pypi.python.org/pypi/python-nvd3/>`_
        - `vispy <http://vispy.org/index.html>`_
        - `IVisual <https://pypi.python.org/pypi/IVisual/>`_
    
5. `Scikit-learn <http://scikit-learn.org/stable/>`_
    a. ADD avec Python (ACP, CAH, clustering)
    b. Machine learning (régression, modèles prédictifs)
    c. `autres modules <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
    d. `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
    e. `DataFrame et SQLite3 <http://www.xavierdupre.fr/app/pyensae/helpsphinx/notebooks/pyensae_flat2db3.html>`_
    
6. Représentation de graphes
    a. `Graphviz <https://github.com/xflr6/graphviz>`_
    b. `Networkx <https://networkx.github.io/>`_
    c. `neo4j <http://www.neo4j.org/develop/python>`_
    
7. Représentation de données structurées, NoSQL
    a. différences avec les bases de données traditionnelles (tables)
    b. format `JSON <http://fr.wikipedia.org/wiki/JavaScript_Object_Notation>`_, `XML <http://fr.wikipedia.org/wiki/Extensible_Markup_Language>`_ pour les `données structurées <http://en.wikipedia.org/wiki/Semi-structured_data>`_
    c. `NoSQL <http://fr.wikipedia.org/wiki/NoSQL>`_ définition
    d. `unqlitepy <https://github.com/nobonobo/unqlitepy>`_ (`unqlite <http://unqlite.org/>`_), `cassandra-driver <https://github.com/datastax/python-driver>`_ (`Cassandra <http://cassandra.apache.org/>`_)
    e. `pymongo <http://docs.mongodb.org/ecosystem/drivers/python/>`_ (installation depuis `pymongo pipy <https://pypi.python.org/pypi/pymongo/>`_, `MongoDB <http://www.mongodb.org/>`_), `py-couchdb <https://py-couchdb.readthedocs.org/en/latest/>`_ (`CouchDB <http://couchdb.apache.org/>`_)
    
8. Calcul distribué  
    a. Multithreading (local)
    b. `GPU <http://fr.wikipedia.org/wiki/Processeur_graphique>`_ : `pycuda <http://mathema.tician.de/software/pycuda/>`_, `theano <http://deeplearning.net/software/theano/>`_
    c. Plusieurs machines ou plusieurs coeurs (ipython, lzmq, ...)
    d. Workflow (`luigi <http://luigi.readthedocs.org/en/latest/>`_, `papy <http://arxiv.org/ftp/arxiv/papers/1407/1407.4378.pdf>`_)
    e. calcul en grande précision `gmpy2 <http://gmpy2.readthedocs.org/en/latest/>`_
    
9. Python et autres langages (C++, Cypthon, C#, R) 
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

3. Outils pour mieux développer
    a. Tests unitaires
    b. `Vérification de types <http://www.xavierdupre.fr/blog/2014-08-20_nojs.html>`_
    c. Profiling (cprofile, yappi)
    d. debugger (avec pytools)
    e. Github, bitbucket, Tortoisegit, tortoisesvn
    f. Génération d'une documentation avec sphinx
    g. Créer un setup pour un module
    h. Créer un exécutable cx_Freeze
    
4. Traitement d'images
    a. Pillow
    b. Opencv
    
5. Un siteweb en python
    a. Flask
    b. Django
    c. `brython <http://www.brython.info/>`_
    d. `pyjs <http://pyjs.org/>`_
    
6. Python sur tablette, téléphone
    a. kivy
    
7. Traitement du langage
    a. Nltk
    
8. Statistiques bayésiennes
    a. pymc (je fais rarement du bayésien,)


Liens
+++++

- Blog: 
    - http://sebastianraschka.com/articles.html
    - http://blog.yhathq.com/
- Sites
    - http://numfocus.org/projects/index.html
    - http://www.pythonworks.org/home (références de livres)
- Articles
    - http://jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf (avec les auteurs de scikit-learn)
- Livres
    - Building Machine Learning Systems with Python by Willi Richert, Luis Pedro Coelho published by PACKT PUBLISHING (2013) 
    - Machine Learning in Action by Peter Harrington
    - `Probabilistic Programming and Bayesian Methods for Hackers <http://nbviewer.ipython.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Prologue/Prologue.ipynb>`_
- Vidéo
    - http://www.microsoft.com/france/mstechdays/programmes/2014/fiche-session.aspx?ID=295be946-2c69-458a-8545-bcebe7970fd8
    - http://www.microsoft.com/france/mstechdays/programmes/2013/fiche-session.aspx?ID=bb6cbb87-c370-477e-8fd4-b46f9ca292d0
