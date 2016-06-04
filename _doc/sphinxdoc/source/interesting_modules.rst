

.. _modulesi:


Modules intéressants (pour un ENSAE)
====================================


Les modules indispensables sont intégrés à la distribution 
`Anaconda <https://www.continuum.io/downloads>`_, `WinPython <https://winpython.github.io/>`_
ou le setup préparée pour l'école `Windows Setup <http://www.xavierdupre.fr/enseignement/>`_
construit avec le module
`pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
puis d'exécuter la commande depuis de répertoire *Scripts* ::

    pymy_install
    
Pour les mettre à jour ::

    pymy_update

        
Parmi ces trois options, `Anaconda <http://continuum.io/downloads#py34>`_ est la plus à jour
et la plus réactive. `pymyinstall <https://github.com/sdpython/pymyinstall/>`_ 
est développé pour ces cours et contient la liste de tous les modules utilisés pour ces enseignements
        

Les indispensables
------------------

* `dask <http://dask.pydata.org/en/latest/>`_ : dataframe distribué et capables de gérer des gros volumes de données (> 5Go)
* `Jupyter <http://jupyter.org/>`_ : gestion des notebooks (des pages blanches mélangeant code, équations, graphiques)
* `matplotlib <http://matplotlib.org/>`_ : graphes scientifiques
* `numpy <http://www.numpy.org/>`_ : calcul matriciel
* `pandas <http://pandas.pydata.org/>`_ : gestion de `DataFrame <http://en.wikipedia.org/wiki/Data_frame>`_
* `scikit-learn <http://scikit-learn.org/stable/>`_ : machine learning, statistique descriptive

Autres dépendances
------------------

**jupyter**

* `jinja2 <http://jinja.pocoo.org/>`_ : moteur de rendu HTML
* `python-dateutil <https://labix.org/python-dateutil>`_ : boîte à outils pour les dates
* `pyzmq <http://zeromq.github.io/pyzmq/>`_ : connecteur pour `ØMQ <http://zeromq.org/>`_ (librairie de sockets, communication entre plusieurs machines)
* `six <https://pythonhosted.org/six/>`_ : librairie de conversion entre Python 2 et 3
* `tornado <http://www.tornadoweb.org/en/stable/>`_ : server web
    
**plugin jupyter**

* `mpld3 <http://mpld3.github.io/>`_ : pour afficher un graph Matplotlib sous forme de graphe `d3.js <http://d3js.org/>`_
* `qgrid <https://pypi.python.org/pypi/qgrid>`_ : pour afficher des dataframe interactifs
    
Visualisation
-------------

*Visualisation des données*

* `matplotlib <http://matplotlib.org/>`_ : graphes scientifiques
* `networkx <http://networkx.github.io/>`_ : dessin de graphes (simple)
* `seaborn <http://stanford.edu/~mwaskom/software/seaborn/>`_ (nécessite matplotlib)
* voir aussi :ref:`l-visualisation`
    
*Jeux*

* `pygame <http://www.pygame.org/>`_ 
* `kivy <http://kivy.org/#home>`_ : pour faire des jeux ou des applications pour tablettes, téléphones

Extensions
----------

* `cvxopt <http://cvxopt.org/>`_ : optimisation quadratique sous contraintes 
  (lire `Install cvxopt on Ubuntu <http://www.xavierdupre.fr/blog/2014-11-23_nojs.html>`_, sous Windows,
  il faut aller à `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_)
* `Flask <http://flask.pocoo.org/>`_ : outils pour produire un server web en Python (plus simple que `django <http://www.django-fr.org/>`_)
* `openpyxl <http://pythonhosted.org/openpyxl/>`_ : conversion de DataFrame en feuille Excel, 
* `Pillow <https://github.com/python-imaging/Pillow>`_ : traitement d'image
* `Scipy <http://www.scipy.org/>`_ : calcul scientifiques
* `statsmodels <http://statsmodels.sourceforge.net/>`_ : modèles linéaires

Pour les TD et projets à l'ENSAE
--------------------------------

* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_ : outils pour les élèves de l'ENSAE
* `pyquickhelper <http://www.xavierdupre.fr/app/`pyquickhelper/helpsphinx/index.html>`_ : dépendences de ``pyensae``
    
Spécialistes
------------

* `liblinear <http://www.csie.ntu.edu.tw/~cjlin/liblinear/>`_ : calcul matriciel en grande dimension
* `opencv <http://opencv.org/>`_ : traitement d'image, reconnaissance des formes
* `simplecv <http://simplecv.org/>`_ : Python et Kinect, vision
* `PyQt4 <https://www.riverbankcomputing.com/software/pyqt/download>`_ : interfaces graphiques
* `sphinx <http://sphinx-doc.org/>`_ : génération de documentation (dont celle-ci)
    
Python et autres langages
-------------------------

* `Cython <http://www.cython.org/>`_ : Python et C++
* `pythonnet <https://github.com/pythonnet/pythonnet>`_ : Python et C#
* `rpy2 <https://bitbucket.org/lgautier/rpy2>`_ : Python et R
    
Internet / SSH
--------------

* `ansiconv <http://pythonhosted.org/ansiconv/>`_ : conversion de texte ANSI en unicode (sortie linux)
* `ansi2html <https://github.com/ralphbean/ansi2html/>`_ : conversion de texte ANSI en HTML (sortie linux)
* `BeautifulSoup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_ : parser du HTML
* `ecdsa <https://pypi.python.org/pypi/pycrypto/>`_ : dépendance de paramiko
* `paramiko <http://www.paramiko.org/>`_ : utile pour créer une connexion SSH
* `pycryptodomex <https://pypi.python.org/pypi/pycryptodomex/>`_ : crypographie
* `requests <http://docs.python-requests.org/>`_ : pratique pour se débrouiller avec internet (`exemples <http://docs.python-requests.org/en/latest/user/quickstart/#redirection-and-history>`_)
          

Pour faire du machine learning sans programmer
----------------------------------------------

* `Orange3 <http://orange.biolab.si/orange3/>`_
* :ref:`Trouver chaussure à ses stats <td1acenoncesession10rst>`
    

