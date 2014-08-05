
.. _modulesi:


Modules intéressants (pour un ENSAE)
====================================


Les modules indispensables sont intégrés à la distribution 
`WinPython <http://winpython.sourceforge.net/>`_. 
L'autre solution est d'utiliser le module
`pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_::

    from pymyinstall import datascientist
    datascientist ("install")
        
Cela suppose que `pip <http://pip.readthedocs.org/en/latest/>`_ est installé 
(c'est le cas à partir de la version Python 3.4).
Tous ces modules ont quelques dépendances optionnelles 
qui ne sont pas incluses dans cette liste mais dont l'usage est rare.


Les indispensables
------------------

    * `ipython <http://ipython.org/index.html>`_ : gestion des notebooks (des pages blanches mélangeant code, équations, graphiques)
    * `matplotlib <http://matplotlib.org/>`_ : graphes scientifiques
    * `numpy <http://www.numpy.org/>`_ : calcul matriciel
    * `pandas <http://pandas.pydata.org/>`_ : gestion de `DataFrame <http://en.wikipedia.org/wiki/Data_frame>`_
    * `scikit-learn <http://scikit-learn.org/stable/>`_ : machine learning, statistique descriptive

Autres dépendances
------------------

*ipython :*

    * `python-dateutils <https://labix.org/python-dateutil>`_ : boîte à outils pour les dates
    * `jinja2 <http://jinja.pocoo.org/>`_ : moteur de rendu HTML
    * `markupsafe <http://www.pocoo.org/projects/markupsafe/>`_
    * `pygments <http://pygments.org/>`_ : meilleur rendu de la ligne de commande
    * `pyzmq <http://zeromq.github.io/pyzmq/>`_ : connecteur pour `ØMQ <http://zeromq.org/>`_ (librairie de sockets, communication entre plusieurs machines)
    * `six <https://pythonhosted.org/six/>`_ : librairie de conversion entre Python 2 et 3
    * `tornado <http://www.tornadoweb.org/en/stable/>`_ : server web
    
*plugin ipython :*

    * `ipyD3 <https://github.com/z-m-k/ipyD3>`_ : plugin pour utiliser `d3.js <http://d3js.org/>`_ dans iPython
    * `mpld3 <http://mpld3.github.io/>`_ : pour afficher un graph Matplotlib sous forme de graphe `d3.js <http://d3js.org/>`_
    
*matplotlib :*

    * `pyparsing <http://pyparsing.wikispaces.com/>`_ : pour définir une gramme et interpréter un langage

*plugin matplotlib :*

    * `prettyplotlib <http://olgabot.github.io/prettyplotlib/>`_
    
Visualisation
-------------

*Visualisation des données :*


    * `matplotlib <http://matplotlib.org/>`_ : graphes scientifiques
    * `prettyplotlib <http://olgabot.github.io/prettyplotlib/>`_ (nécessite matplotlib)
    * `ggplot <http://ggplot.yhathq.com/>`_ : extension très populaire sur *R* et portée sur Python
    * `plotly <https://plot.ly/python/>`_ : graphes élaborés
    * `networkx <http://networkx.github.io/>`_ : dessin de graphes (simple)
    
*Jeux :*

    * `pygame <http://www.pygame.org/>`_ 
    * `kivy <http://kivy.org/#home>`_ : pour faire des jeux ou des applications pour tablettes, téléphones

Extensions
----------

    * `cvxopt <http://cvxopt.org/>`_ : optimisation quadratique sous contraintes
    * `openpyxl <http://pythonhosted.org/openpyxl/>`_ : conversion de DataFrame en feuille Excel, 
      il est préférable d'installer la version 1.62 (``pip install openpyxl==1.6.2``) car la version 2.0.3
      ne marche pas encore avec pandas.
    * `Pillow <https://github.com/python-imaging/Pillow>`_ : traitement d'image
    * `Scipy <http://www.scipy.org/>`_ : calcul scientifiques
    * `statsmodels <http://statsmodels.sourceforge.net/>`_ : modèles linéaires
    * `Flask <http://flask.pocoo.org/>`_ : outils pour produire un server web en Python (plus simple que `django <http://www.django-fr.org/>`_)

Pour les TD et projets à l'ENSAE
--------------------------------

    * `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_ : outils pour les élèves de l'ENSAE
    * `pyquickhelper <http://www.xavierdupre.fr/app/`pyquickhelper/helpsphinx/index.html>`_ : dépendences de ``pyensae``
    
Spécialistes
------------

    * `Blosc <https://github.com/Blosc/python-blosc>`_
    * `CGAL Python <http://cgal-python.gforge.inria.fr/>`_ : Voronoï, Delaunay, ...
    * `GMPY <https://code.google.com/p/gmpy/>`_ : calcul en grande précision
    * `liblinear <http://www.csie.ntu.edu.tw/~cjlin/liblinear/>`_ : calcul matriciel en grande dimension
    * `libsvm <http://www.csie.ntu.edu.tw/~cjlin/libsvm/>`_ : SVM
    * `opencv <http://opencv.org/>`_ : traitement d'image, reconnaissance des formes
    * `pygraphviz <http://pygraphviz.github.io/>`_ : dessin de graphes
    * `pyqt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_ : interfaces graphiques
    * `pytables <http://www.pytables.org/moin>`_ : manipuler de grands jeux de données
    * `pywavelets <http://www.pybytes.com/pywavelets/>`_ : ondelettes
    * `simplecv <http://simplecv.org/>`_ : Python et Kinect, vision
    * `sphinx <http://sphinx-doc.org/>`_ : génération de documentation (dont celle-ci)
    * `twisted <http://twistedmatrix.com/trac/>`_ : application client-serveur
    
Python et autres langages
-------------------------

    * `boost.python <http://www.boost.org/libs/python/doc>`_ : Python et C++
    * `Cython <http://www.cython.org/>`_ : Python et C++
    * `pythonnet <http://pythonnet.sourceforge.net/>`_ : Python et C# (pour Windows, utiliser `sdpython/pythonnet <https://github.com/sdpython/pythonnet>`_)
    * `rpy2 <https://bitbucket.org/lgautier/rpy2>`_ : Python et R
    * `shapely <https://github.com/Toblerity/Shapely>`_ : Python et `GEOS <http://trac.osgeo.org/geos/>`_
    
Boîte à outils
--------------

    * `requests <http://docs.python-requests.org/>`_ : pratique pour se débrouiller avec internet (`exemples <http://docs.python-requests.org/en/latest/user/quickstart/#redirection-and-history>`_)
    
Pour faire du machine learning sans programmer
----------------------------------------------

    * `Orange <http://orange.biolab.si/>`_
    * `Trouver chaussure à ses stats <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/notebooks/td1a_cenonce_session_10.html#intro>`_
    
Génération d'une documentation et thème Sphinx
----------------------------------------------

    * `Sphinx <http://sphinx-doc.org/>`_ : génération de documentation HTML/Javascript à partir du langage `reStructuredText <http://docutils.sourceforge.net/rst.html>`_
    * `sphinxcontrib.fancybox <http://spinus.github.io/sphinxcontrib-fancybox/>`_ : pour traite les images
    * `sphinx_rtd_theme <https://github.com/snide/sphinx_rtd_theme>`_ : thème de ce document
    * `sphinxjp.themes.basicstrap <http://pythonhosted.org/sphinxjp.themes.basicstrap/>`_ : thème (voir `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_)
    * `solar_theme <http://2vkvn.com/solar-theme/>`_ : voir `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_    
    * `cloud_sptheme <http://pythonhosted.org/cloud_sptheme/>`_: voir `pysqllike <http://www.xavierdupre.fr/app/pysqllike/helpsphinx/index.html>`_
    * `sphinx_readable_theme <https://sphinx-readable-theme.readthedocs.org/en/latest/>`_: voir `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
    * `sphinxjp.themes.sphinxjp <https://pythonhosted.org/sphinxjp.themes.sphinxjp/>`_ : voir `pymmails <http://www.xavierdupre.fr/app/pymmails/helpsphinx/>`_
    * `hachibee_sphinx_theme <http://hachibeedi.github.io/Sphinx-hachibee-theme/index.html>`_ : voir `pyrsslocal <http://www.xavierdupre.fr/app/pyrsslocal/helpsphinx/>`_
    