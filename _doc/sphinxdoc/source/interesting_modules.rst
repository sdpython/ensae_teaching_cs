

.. _modulesi:


Modules intéressants (pour un ENSAE)
====================================


Les modules indispensables sont intégrés à la distribution 
`Anaconda <http://continuum.io/downloads#py34>`_ ou `WinPython <http://winpython.sourceforge.net/>`_.
Une autre solution est d'utiliser le module
`pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_ ::

    from pymyinstall import datascientist
    datascientist ("install")
        
Cela suppose que `pip <http://pip.readthedocs.org/en/latest/>`_ est installé 
(c'est le cas à partir de la version Python 3.4).
Tous ces modules ont quelques dépendances optionnelles 
qui ne sont pas incluses dans cette liste mais dont l'usage est rare.

Parmi ces trois options, `Anaconda <http://continuum.io/downloads#py34>`_ est la plus à jour
et la plus réactive. `pymyinstall <https://github.com/sdpython/pymyinstall/blob/master/src/pymyinstall/packaged/packaged_config.py>`_ 
contient la liste de tous les modules utilisés pour ces enseignements ::

    from pymyinstall import datascientist
    datascientist ("install", azure = True)
        

Les indispensables
------------------

* `ipython <http://ipython.org/index.html>`_ : gestion des notebooks (des pages blanches mélangeant code, équations, graphiques)
* `matplotlib <http://matplotlib.org/>`_ : graphes scientifiques
* `numpy <http://www.numpy.org/>`_ : calcul matriciel
* `pandas <http://pandas.pydata.org/>`_ : gestion de `DataFrame <http://en.wikipedia.org/wiki/Data_frame>`_
* `scikit-learn <http://scikit-learn.org/stable/>`_ : machine learning, statistique descriptive

Autres dépendances
------------------

**ipython :**

* `python-dateutil <https://labix.org/python-dateutil>`_ : boîte à outils pour les dates
* `jinja2 <http://jinja.pocoo.org/>`_ : moteur de rendu HTML
* `pyzmq <http://zeromq.github.io/pyzmq/>`_ : connecteur pour `ØMQ <http://zeromq.org/>`_ (librairie de sockets, communication entre plusieurs machines)
* `six <https://pythonhosted.org/six/>`_ : librairie de conversion entre Python 2 et 3
* `tornado <http://www.tornadoweb.org/en/stable/>`_ : server web
    
**plugin ipython :**

* `ipyD3 <https://github.com/z-m-k/ipyD3>`_ : plugin pour utiliser `d3.js <http://d3js.org/>`_ dans iPython
* `mpld3 <http://mpld3.github.io/>`_ : pour afficher un graph Matplotlib sous forme de graphe `d3.js <http://d3js.org/>`_
    
Visualisation
-------------

*Visualisation des données :*

* `matplotlib <http://matplotlib.org/>`_ : graphes scientifiques
* `seaborn <http://stanford.edu/~mwaskom/software/seaborn/>`_ (nécessite matplotlib)
* `networkx <http://networkx.github.io/>`_ : dessin de graphes (simple)
    
*Jeux :*

* `pygame <http://www.pygame.org/>`_ 
* `kivy <http://kivy.org/#home>`_ : pour faire des jeux ou des applications pour tablettes, téléphones

Extensions
----------

* `cvxopt <http://cvxopt.org/>`_ : optimisation quadratique sous contraintes 
  (lire `Install cvxopt on Ubuntu <http://www.xavierdupre.fr/blog/2014-11-23_nojs.html>`_, sous Windows,
  il faut aller à `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_)
* `openpyxl <http://pythonhosted.org/openpyxl/>`_ : conversion de DataFrame en feuille Excel, 
  il est préférable d'installer la version 1.6.2 (``pip install openpyxl==1.6.2``) car la version 2.0.3
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

* `liblinear <http://www.csie.ntu.edu.tw/~cjlin/liblinear/>`_ : calcul matriciel en grande dimension
* `opencv <http://opencv.org/>`_ : traitement d'image, reconnaissance des formes
* `PyQt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_ : interfaces graphiques
* `simplecv <http://simplecv.org/>`_ : Python et Kinect, vision
* `sphinx <http://sphinx-doc.org/>`_ : génération de documentation (dont celle-ci)
    
Python et autres langages
-------------------------

* `Cython <http://www.cython.org/>`_ : Python et C++
* `pythonnet <http://pythonnet.sourceforge.net/>`_ : Python et C# (pour Windows, utiliser `sdpython/pythonnet <https://github.com/sdpython/pythonnet>`_)
* `rpy2 <https://bitbucket.org/lgautier/rpy2>`_ : Python et R
    
Internet / SSH
--------------

* `requests <http://docs.python-requests.org/>`_ : pratique pour se débrouiller avec internet (`exemples <http://docs.python-requests.org/en/latest/user/quickstart/#redirection-and-history>`_)
* `paramiko <http://www.paramiko.org/>`_ : utile pour créer une connexion SSH
* `ecdsa <https://pypi.python.org/pypi/pycrypto/>`_ : dépendance de paramiko
* `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_ : dépendance de paramiko
* `ansiconv <http://pythonhosted.org/ansiconv/>`_ : conversion de texte ANSI en unicode (sortie linux)
* `ansi2html <https://github.com/ralphbean/ansi2html/>`_ : conversion de texte ANSI en HTML (sortie linux)
          

Pour faire du machine learning sans programmer
----------------------------------------------

* `Orange <http://orange.biolab.si/>`_
* :ref:`Trouver chaussure à ses stats <td1acenoncesession10rst>`
    

