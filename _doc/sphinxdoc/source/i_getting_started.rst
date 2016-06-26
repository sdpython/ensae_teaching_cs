

.. _l-getting_started_full:


===============
Getting started
===============

.. index:: R, Julia, WinPython, Anaconda, pyminstall, getting started

Lorsqu'on fait des statistiques, le language Python est loin d'être
aussi complet que `R <https://www.r-project.org/>`_ 
qui a été pensé dans ce but. Il faut lui ajouter plusieurs dizaine
de modules. C'est à ce moment qu'on découvrir les subtilités dans les différents
systèmes d'exploitations, les compilateurs, les dépendances, la ligne de commande.
Ce paragraphe décrit un moyen d'installation Python sur les trois
systèmes principaux 
`Windows <http://www.microsoft.com/fr-fr/windows>`_, 
`OS X <http://www.apple.com/osx/>`_, 
`Linux <https://en.wikipedia.org/wiki/Linux>`_
avec les modules nécessaires présentés dans ce cours.
Le premier paragraphe explique comment installer rapidement Python, 
il faudra lire les suivants si vos besoins vont au delà.


.. _l-installation-courte:

En résumé : Anaconda
====================

En résumé, le conseil le plus fréquent qu'on donne à ceux qui souhaitent 
installer Python est d'utiliser la distribution `Anaconda <https://www.continuum.io/downloads>`_.
C'est l'équivalent de `R <https://www.r-project.org/>`_.
Sans autre étape supplémentaires, elle permet de faire du calcul matriciel
`numpy <http://www.numpy.org/>`_, de tracer des graphiques avec `matplotlib <http://matplotlib.org/>`_,
de manipuler les données `pandas <http://pandas.pydata.org/>`_
et de faire du machine du machine learning
`scikit-learn <http://scikit-learn.org/>`_.

La plupart des exercices proposés sur ce site n'utilisent pas plus que ce qui est proposé
dans cette distribution standard. Pour les autres, 
les instructions mentionnées ci-dessous fonctionnent sous Windows, Linux et Mac.

Windows
+++++++

Pour tous les modules nécessaires une compilation C++,
allez à `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.

* distribution `Anaconda <https://www.continuum.io/downloads>`_ (python 64 bit)

**ou**

* `distribution customisée <http://www.xavierdupre.fr/enseignement/>`_ [#fpm1]_ ou
  distribution standard de `Python <https://www.python.org/downloads/>`_
* puis la mise à jour depuis le répertoire ``python`` en ligne de commande ::

    Scripts\pip install pymyinstall --upgrade
    Scripts\pymy_install3 --set=ensae_teaching_cs
    Scripts\pymy_update3 --set=ensae_teaching_cs
    
Linux / Mac
+++++++++++

* distribution `Anaconda <https://www.continuum.io/downloads>`_ (python 64 bit)
* puis la mise à jour depuis le répetoire ``Scripts`` en ligne de commande ::

    ./conda update --all
    ./pip install pymyinstall --upgrade
    ./pymy_install3 --set=ensae_teaching_cs
    ./pymy_update3 --set=ensae_teaching_cs
        
    
Linux en ligne de commande, connexion SSH
+++++++++++++++++++++++++++++++++++++++++

Voir `Install Miniconda through SSH connection <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2015/2015-11-01_anaconda_ssh.html>`_.
La distribution testée est une distribution `Ubuntu 14.04 <http://releases.ubuntu.com/14.04/>`_.


IDE
+++

Un IDE est un `environnement de développemen <Environnement de développement>`_.
Et comme on ne fait pas tout depuis un notebook, il faut en choisir un un.

* `Atom <https://atom.io/>`_
* `Ninja IDE <http://ninja-ide.org/home/>`_
* `PTVS <http://microsoft.github.io/PTVS/>`_ (Python Tools for Visual Studop) (** debug, notebook **)
* `PyCharm <http://www.jetbrains.com/pycharm/>`_ (** * **)
* `PyDev <http://pydev.org/>`_ (fonctionne avec `Eclipse <http://www.eclipse.org/>`_)
* `Pyzo <http://www.pyzo.org/>`_ : ressemble à Matlab  (anciennement `IEP <http://www.iep-project.org/index.html>`_)
* `WingIDE <https://wingware.com/>`_

Editeur de texte
++++++++++++++++

Si vous êtes dans le train et que vous n'avez pas beaucoup de batterie,
il faut revenir à l'essentiel : un `éditeur de texte <https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte>`_.

* `Emacs <https://www.gnu.org/software/emacs/>`_
* `nano <https://www.nano-editor.org/>`_ (linux)
* `Notepad++ <https://notepad-plus-plus.org/>`_
* `SciTe <http://www.scintilla.org/SciTE.html>`_, le plus simple et le plus léger,
  lire cet article pour le configurer
  `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_.
  (** * **)



Installer un module
===================

Il faut ouvrir une fenêtre ligne de commande (Windows) 
ou une fenêtre terminal (Linux, OS/X) et se placer dans le répertoire de la distribution.
L'installation dépend ensuite dy système d'exploitation et de la 
distribution choisie. Dans tous les cas, il faut se place

* Anaconda: 

    * module standard : ``conda install <module>``
    * module rare : ``pip install <module>``
    
* WinPython (Python sur Windows)

    * module standard : télécharger le module sur le site `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ 
      et l'installer avec la commande ``pip install <local_module.whl>``
    * module rare : ``pip install <module>`` (à condition que celui-ci n'inclut pas de code C/C++) qui requiert un compilateur C/C++
    
L'instruction ``pip install`` ne fonctionne pas sous Windows lorsque le module
est implémenté en Python et C++. C'est pourquoi il est préférable d'installer
une version précompilée. 

**dépendances**

Par défaut, l'installation d'un module implique celle de ses dépendances
ce qu'il est possible d'éviter : ::

    pip install <module> --no-deps


pip, python et ligne de commande
================================

La base
+++++++


Le language python s'est doté d'un système de distribution de modules (ou *packages*)
qui est aisément accessible depuis la `ligne de commande <http://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande>`_.
Sous Windows, on peut lancer la ligne de commande par la commande ``cmd``. On obtient une fenêtre noire.
Il suffit alors de se déplacer dans le répertoire d'installation de Python ::

    cd c:\Python35_x64\Scripts
    
Ou encore ::

    cd c:\Anaconda3\Scripts
    
Puis d'écrire ::

    pip install <module>
    
Sous Linux ou OS X (Apple), la ligne de commande s'appelle le `terminal <http://doc.ubuntu-fr.org/terminal>`_.
Comme Python est déjà installé en version 2.7, je recommande l'installation de la distribution
Anaconda en version 3.4 qui facilite la coexistence de plusieurs versions de Python. On procède de la même manière ::

    cd /home/<alias>/anaconda3/bin
    
Puis ::

    pip install <module>

Pour vous assurer que cela correspond bien à la version de Python souhaitée,
il suffit de demander la version installée ::

    pip --version
    
Sous Windows, pour l'ajout d'un module ponctuel, 
si l'instruction ``pip install <module>`` ne fonctionne pas,
c'est vraisemblablement parce que ce module contient une partie en C++. 
Dans ce cas, il faut aller voir sur ce site 
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
s'il est disponible. S'il ne l'est pas, l'installation du module est réservée aux experts.
    
    
Installer un module avec pymy_install
+++++++++++++++++++++++++++++++++++++

Le module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_ 
recherche la meilleure façon d'installer un module quelque soit votre installation. 
Pour l'installer ou le mettre à jour : ::

    pip install pymyinstall --upgrade

L'installation du module crée deux scripts,
``pymy_install3`` pour installer un module,
``pymy_update3`` pour mettre à jour.
Le module permet d'installer un ensemble de modules ::

    pymy_install3 --set=pyensae


Désinstallation
+++++++++++++++

Il est possible de désinstaller simplement les modules installés pour
ces enseignements ::

    pip uninstall pyquickhelper pyensae pymmails pyrsslocal pysqllike 
    pip uninstall ensae_teachings_cs
    pip uninstall code_beatrix actuariat_python
    pip uninstall ensae_projects
    

Configuration pour ces cours
++++++++++++++++++++++++++++

Les notebooks utilise le module `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_ 
développé pour ces enseignements. Pour installer ses dépendances, il faut utiliser le module
`pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_

  
Certains notebooks s'appuient sur des fonctions qui donnent accès
à des données ou qui facilitent leur récupération. Elles sont disponibles
via le module  ::

    pip install pyensae
    
Ce module requiert des dépendances qu'on peut installer comme
suit ::

    pymy_install3 --set=pyensae

    
La page :ref:`l-data2a` propose une liste exhaustive
de modules qu'il faut ajouter pour reproduire la distribution
proposée par l'école.
  
  
Certains notebooks requièrent des outils supplémentaires :

* `graphviz <http://www.graphviz.org/>`_


.. index:: pip, ligne de commande
    

Distributions
=============

.. index:: anaconda, winpython


* `Anaconda <http://continuum.io/downloads#py34>`_ (Windows, Linux, Mac). 
  Sous Linux ou Mac, la distribution n'interfère pas avec la distribution existante
  souvent différente. C'est un point très appréciable. Les modules de la distribution ne sont 
  pas tous à jour. Il faut penser à mettre à jour avec la commande ``conda install <module>``
  depuis le répertoire ``Anaconda3/Scripts`` (``conda install cvxopt`` par exemple).
  Il existe une version différente : `miniconda <http://conda.pydata.org/miniconda.html>`_.
  La liste des packages manquant sera probablement différente.
  Il suffit d'écrire sur la ligne de commande ``conda update --all`` 
  pour mettre à jour tous les modules.

* `WinPython <https://winpython.github.io/>`_ (Windows). Sous Windows, elle inclut 
  parfois `R <http://www.r-project.org/>`_ ou `Julia <http://julialang.org/>`_ (ces version ne sont 
  pas aussi à jour que la version principale). On passe alors
  facilement de python à R ou Julia depuis le même notebooks.    
  Uniquement disponible sous Windows, cette installation a l'avantage de ne pas 
  nécessiter les droits administrateur pour être installée. Elle
  ne modifie pas les registres et on peut la recopier telle quelle sur une clé USB
  pour la recopier sur un autre ordinateur. On peut également préparer sa propre version
  `How To Make WinPython <https://github.com/winpython/winpython/wiki/How-To-Make-WinPython>`_.
  
* Distribution officielle de `python <https://www.python.org/>`_, il faut ensuite 
  installer de nombreux modules (voir :ref:`l-data2a`) pour obtenir
  une distribution équivalente aux deux précédentes.
  
* `Miniconda <http://conda.pydata.org/miniconda.html>`_ est une version light de Anaconda
  sans tous ces packages. Elle peut être installée depuis une ligne de commande, via
  une connexion SSH. 
  Voir `Install Anaconda through SSH connection <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2015/2015-11-01_anaconda_ssh.html>`_.

    
    
Outils adaptés aux projets de long terme
========================================

Navigateur
++++++++++

.. index:: navigateur, notebook  

Les navigateur sont importants pour l'utilisation des notebooks. Je recommande soit
`Firefox <https://www.mozilla.org/fr/firefox/new/>`_, 
soit `Chrome <http://www.google.com/chrome/>`_. Internet Explorer pose quelques problèmes
avec l'utilisateur du Javascript. Ces deux navigateurs sont indispensables si vous insérez du javascript
dans nos notebooks. Le débuggeur de Chrome est le plus pratique à utiliser quand il s'agit d'aller
fouiller dans les feuilles de styles ou de voir l'exécution du javascript.
        
.. index:: développeur
        
Développeur
+++++++++++
        
La documentation et les tests unitaires les modules
classés dans les catégories *SPHINX*, *TEACH*
et répertorié par :ref:`l-data2a`.
Certaines séances pratiques utilisent des données depuis ce site. 
Elles sont facilement téléchargeables avec ces deux modules :

* `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_ : ce module compile ce cours
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_ : outils variés pour les élèves de l'ENSAE
* `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_ : installer facilement des modules sous Windows

Pour être compilée, la documentation requiert également :

* `miktex <http://miktex.org/>`_ (Windows seulement)
* `pandoc <http://pandoc.org/>`_
* `InkScape <https://inkscape.org/fr/>`_
    
Il est très utile d'avoir un éditeur de texte léger, quelques options :

* `Scite <http://www.scintilla.org/SciTE.html>`_
* `Notepad++ <http://notepad-plus-plus.org/>`_
    
Et un `IDE <http://en.wikipedia.org/wiki/Integrated_development_environment>`_ :

* `PTVS <https://microsoft.github.io/PTVS/>`_ (Windows uniquement)
* `PyCharm <https://www.jetbrains.com/pycharm/>`_
    

Les outils pour développer
++++++++++++++++++++++++++

**Impératif**

* `Python 3.4 64 bit <https://www.python.org/downloads/>`_
* `R <http://www.r-project.org/>`_
* `Scite <http://www.scintilla.org/SciTE.html>`_ : éditeur de texte très léger
* `7zip <http://www.7-zip.org/>`_ : pour compresser, décompresser tous les formats
* `Firefox <https://www.mozilla.org/fr-FR/firefox/new/>`_, `Chrome <http://www.google.com/chrome/>`_ : navigateurs 
  (il faut éviter Internet Explorer pour les notebooks Jupyter)
* `Miktex <http://miktex.org/>`_, `TexnicCenter <http://www.texniccenter.org/>`_ : compiler du latex (et obtenir des PDF)
* `Java <http://www.java.com/fr/download/>`_ : nécessaire pour Jenkins et `Antlr <http://www.antlr.org/>`_
* `Jenkins <https://jenkins-ci.org/>`_ (plus les plugins pour `GitHub <https://wiki.jenkins-ci.org/display/JENKINS/GitHub+Plugin>`_, 
  `git <https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin>`_, 
  `python <https://wiki.jenkins-ci.org/display/JENKINS/Python+Plugin>`_, 
  `pipeline <https://wiki.jenkins-ci.org/display/JENKINS/Build+Pipeline+Plugin>`_) : automatisation de build
* `pandoc <http://pandoc.org/>`_ : conversion de tout type de format en tout autre (notebook --> PDF)
* `TortoiseGit <https://tortoisegit.org>`_ : sous Windows, pour éviter la ligne de commande avec Git
* `Git <http://git-scm.com/>`_ + `GitHub <https://github.com/>`_ : pour suivre ses projets avec Git
* `GraphViz <http://www.graphviz.org/>`_ : représenter des graphes

**Impératif pour le C++ sous Windows**

* `Visual Studio Community <https://www.visualstudio.com/>`_ : C++, C#, F#, Python avec `PTVS <https://microsoft.github.io/PTVS/>`_
* `MinGW <http://www.mingw.org/>`_ : compilateur C++


.. rubric:: Footnotes

.. index:: pymyinstall, distribution

.. [#fpm1] Cette distribution est construite grâce à la fonction 
           `win_python_setup <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/pymyinstall/win_installer/win_setup_main.html#pymyinstall.win_installer.win_setup_main.win_python_setup>`_
           du module
           `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/pymyinstall/>`_.
           La construction du setup prend quelques heures et inclut les modules
           listés répertoriés par :ref:`l-data2a`.
           
           




Modules incournables pour un data scientist
===========================================


Les modules indispensables sont intégrés à la distribution 
`Anaconda <https://www.continuum.io/downloads>`_, `WinPython <https://winpython.github.io/>`_
ou le setup préparée pour l'école `Windows Setup <http://www.xavierdupre.fr/enseignement/>`_
construit avec le module
`pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_.

        

Les indispensables
------------------

* `dask <http://dask.pydata.org/en/latest/>`_ : dataframe distribué et capables de gérer des gros volumes de données (> 5Go)
* `Jupyter <http://jupyter.org/>`_ : gestion des notebooks (des pages blanches mélangeant code, équations, graphiques)
* `matplotlib <http://matplotlib.org/>`_ : graphes scientifiques
* `numpy <http://www.numpy.org/>`_ : calcul matriciel
* `pandas <http://pandas.pydata.org/>`_ : gestion de `DataFrame <http://en.wikipedia.org/wiki/Data_frame>`_
* `scikit-learn <http://scikit-learn.org/stable/>`_ : machine learning, statistique descriptive
* `statsmodels <http://statsmodels.sourceforge.net/>`_ : séries temporelles

Dépendances
-----------

**jupyter**

* `jinja2 <http://jinja.pocoo.org/>`_ : moteur de rendu HTML
* `pyzmq <http://zeromq.github.io/pyzmq/>`_ : connecteur pour `ØMQ <http://zeromq.org/>`_ (librairie de sockets, communication entre plusieurs machines)
* `six <https://pythonhosted.org/six/>`_ : librairie de conversion entre Python 2 et 3
* `tornado <http://www.tornadoweb.org/en/stable/>`_ : server web

    
Visualisation
-------------

Voir `10 plotting libraries at PyData 06/14/2016 in Paris <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_.
    
Jeux
----

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

Pour les TD et projets à l'ENSAE
--------------------------------

* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_ : outils pour les élèves de l'ENSAE
* `pyquickhelper <http://www.xavierdupre.fr/app/`pyquickhelper/helpsphinx/index.html>`_ : outils d'automatisation
    
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
    




Outils, ressources pour développer
==================================

Outils
++++++

Développer un programme informatique prend du temps et il est important d'être à l'aise. 
Une grande difficulté lorsqu'on programme c'est de travailler à plusieurs sur le même projet.
Il faut se sychroniser. Fort heureusement, le problème est connu depuis longtemps et il existe beaucoup
d'outils open source dont on aurait tort de se passer ou des services gratuits sous certains conditions 
qui facilitent l'archivage. Ils sont tellement pratiques qu'on a même du mal
à s'en passer lorsqu'on travaille tout seul.

**Suivi de sources distant**

* `GitHub <https://github.com/>`_
* `BitBucket <https://bitbucket.org/>`_

**Visual pour Git**

* `TortoiseGit <https://code.google.com/p/tortoisegit/>`_ (Windows)
* `SourceTree <http://www.sourcetreeapp.com/>`_ (Windows, Mac)
* `Giggle <https://wiki.gnome.org/Apps/giggle>`_ (Linux)

**Archivage distant**

* `hubiC <https://hubic.com/fr/>`_  (25 Go gratuit - août 2015)
* `OneDrive <https://onedrive.live.com/about/fr-fr/>`_ (15 Go gratuit - août 2015)

Ce ne sont pas les seuls, vous trouverez d'autres options ici :
`cloud-gratuit <http://www.cloud-gratuit.com/>`_. Toutefois, **il est recommandé de ne pas mettre
des données personnelles sensibles**. Les compagnies qui hébergent vos données
se réservent parfois le droit de fermer votre compte sans avertissement préalable.
Même si vos données sont protégées par un mot de passe et ne sont pas publiques, 
il arrive que certains mots de passe soient interceptés.
Il est également préférable de choisir des hébergements qui proposent 
un stockage dans un pays dont la loi limite l'usage qui peut être fait de vos données.


**Comparaison de fichiers**

* `kdiff3 <http://kdiff3.sourceforge.net/>`_
* `Beyond and Compare <http://www.scootersoftware.com/>`_ : il est gratuit pendant un mois, c'est le plus convivial.

**Partager des notes, des idées**

* `OneNote <http://office.microsoft.com/fr-fr/onenote/>`_ 
* `Evernote <https://evernote.com/intl/fr/>`_

**Editeur de texte**

* `SciTE <http://www.scintilla.org/SciTE.html>`_ : le plus simple, pas d'explorateur de fichier, pas d'installeur, autocomplétion perturbante
* `TextWrangler <http://www.barebones.com/products/textwrangler/>`_ (seulement sur iOS - Apple)
* `SublimeText <http://www.sublimetext.com/>`_ : configuration nécessaire avant d'exécuter un script python
* `NotePad++ <http://notepad-plus-plus.org/fr/>`_ : configuration nécessaire avant d'exécuter un script python

**IDE**

* `Atom <https://atom.io/>`_
* `Ninja IDE <http://ninja-ide.org/home/>`_
* `PyCharm <http://www.jetbrains.com/pycharm/>`_
* `PyDev <http://pydev.org/>`_ (fonctionne avec `Eclipse <http://www.eclipse.org/>`_)
* `PTVS <https://microsoft.github.io/PTVS/>`_ (fonctionne avec `Visual Studio <http://www.visualstudio.com/>`_)
* `Pyzo <http://www.pyzo.org/>`_ : ressemble à Matlab  (anciennement `IEP <http://www.iep-project.org/index.html>`_)
* `WingIDE <https://wingware.com/>`_

**Python et Domotique**

* `Micro Python Project <https://github.com/micropython/micropython>`_
* `Python et Arduino <http://playground.arduino.cc/Interfacing/Python>`_
* `Python et RaspberryPI <http://www.raspberrypi.org/documentation/usage/python/README.md>`_

**Scheduler, automatic build**

* `Jenkins <http://jenkins-ci.org/>`_
* `Buildbot <http://buildbot.net/>`_

Ressources
++++++++++

* `Developpez.com <http://www.developpez.com/>`_ : beaucoup de choses autour de la programmation et en français
* `stackoverflow <http://stackoverflow.com/>`_ : énorme forum de discussion sur tout ce qui touche à la programmation
* `Jardin Zen Css <http://www.csszengarden.com/>`_ (la même page avec une multitude de styles différents)
* `Le blog univers domotique <http://blog.univers-domotique.com/>`_
* `Tutoriel sur GIT <http://sixrevisions.com/resources/git-tutorials-beginners/>`_




Maintenir sa distribution Python à jour
=======================================




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

Autres sources d'inspiration :

* `data-science-ipython-notebooks <https://github.com/donnemartin/data-science-ipython-notebooks>`_
* `Awesome Python <https://github.com/vinta/awesome-python#environment-management>`_, répertoire de librairiees Python populaires (donc à regarder en premier)
* `Trending Python <https://github.com/trending?l=python>`_
* `Trending Python <https://github.com/trending?l=python&since=monthly>`_ (mensuel)
* `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
* conférence `pydata <http://pydata.org/>`_


Installation
++++++++++++

a. Installation : 
    - `Anaconda <http://continuum.io/downloads#py34>`_
    - `WinPython <http://winpython.sourceforge.net/>`_ (seulement sur Windows, moins rapide au niveau des mises à jour que Anaconda)
    - `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ 
    - `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_
      (utilisé pour construire ce `setup <http://www.xavierdupre.fr/enseignement/>`_)
    - `Instructions pour installer ces modules sous Linux/Mac <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2015/2015-08-30_install_linux.html>`_
b. Environnements
    - `IDLE <https://docs.python.org/3.4/library/idle.html>`_
    - `ligne de commande Jupyter <http://jupyter-notebook.readthedocs.io/en/latest/config.html>`_
    - `Spyder <http://pythonhosted.org//spyder/>`_  (environnement de type `RStudio <http://www.rstudio.com/>`_)
    - `Rodeo <https://pypi.python.org/pypi/rodeo>`_  (Spyder version web et épurée)
    - `Notebooks <http://jupyter.org/notebook.html>`_
c. Editeur de texte (pour des projets plus ambitieux, SciTE, PyCharm, PTVS, WingIDE)
    - `Scite <http://www.scintilla.org/SciTE.html>`_
    - `Notepad++ <https://notepad-plus-plus.org/>`_
    - `SublimeText <http://www.sublimetext.com/>`_
    - `Atom <https://atom.io/>`_
    - `PyCharm <http://www.jetbrains.com/pycharm/>`_
    - `PTVS <http://microsoft.github.io/PTVS/>`_ (Python Tools for Visual Studop)
    - `WingIDE <https://wingware.com/>`_ (version académique `Wing IDE 101 <https://wingware.com/downloads/wingide-101>`_)
        


Quelques articles
+++++++++++++++++

* `scikit lectures <http://scipy-lectures.github.io/>`_
* `Formation à Python scientifique - ENS Paris <http://python-prepa.github.io/index.html>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `Python Tools for Machine Learning <http://www.cbinsights.com/blog/python-tools-machine-learning/>`_
* `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
* `22 outils gratuits pour visualiser et analyser les données (1ère partie) <http://www.lemondeinformatique.fr/actualites/lire-22-outils-gratuits-pour-visualiser-et-analyser-les-donnees-1ere-partie-47241-page-3.html>`_
* `Gradient Boosted Regression Trees <http://orbi.ulg.ac.be/bitstream/2268/163521/1/slides.pdf>`_
* `A Reliable Effective Terascale Linear Learning System <http://arxiv.org/pdf/1110.4198v3.pdf>`_
* `Understanding Random Forest <http://orbi.ulg.ac.be/handle/2268/170309>`_


Quelques liens
++++++++++++++

- Blog
    - `FastML <http://fastml.com/>`_
    - `no free hunch (Kaggle Blog) <http://blog.kaggle.com/>`_
    - `Sebastian Raschka <http://sebastianraschka.com/articles.html>`_
    - `yhat <http://blog.yhathq.com/>`_
- Sites
    - `NumFOCUS Foundation <http://numfocus.org/projects/index.html>`_
    - `pythonworks.org <http://www.pythonworks.org/home>`_ (références de livres)
- Articles
    - `Scikit-learn: Machine Learning in Python <http://jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf>`_ (avec les auteurs de scikit-learn)
- Livres
    - `Deep Learning <http://www-labs.iro.umontreal.ca/~bengioy/dlbook/>`_
      by Yoshua Bengio, Ian Goodfellow and Aaron Courville
    - `Building Machine Learning Systems with Python <https://github.com/luispedro/BuildingMachineLearningSystemsWithPython>`_
      by Willi Richert, Luis Pedro Coelho published by PACKT PUBLISHING (2013) 
    - `Machine Learning <https://github.com/pbharrin/machinelearninginaction>`_
      in Action by Peter Harrington
    - `Probabilistic Programming and Bayesian Methods for Hackers <http://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Prologue/Prologue.ipynb>`_,
      (`second version <http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/>`_)
- Vidéo
    - `Scikit-Learn: Machine Learning en Python <http://www.microsoft.com/france/mstechdays/programmes/2014/fiche-session.aspx?ID=295be946-2c69-458a-8545-bcebe7970fd8>`_
    - `PyVideo <http://www.pyvideo.org/>`_
    - `PyData TV <https://www.youtube.com/user/PyDataTV>`_


.. index:: wheel

Modules Python
++++++++++++++

Les modules suivant font partie du setup proposé aux étudiants (voir plus bas).

* **usage** : classification, la plus importante *DATA/ML* regroupe les modules les plus importantes
  pour faire du machine learning
* **name** : nom du module
* **kind** : façon d'installer le module sous Windows, si c'est *wheel*, cela signifie
  que le module inclut une partie C++ qu'il est préférable de récupérer déjà compilée
  via le site `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
* **version** : la version à installer car d'autres peuvent provoquer des conflits
* **license** : license du module, toutes ne permettent pas un usage commercial,
  voir `choose a license <http://choosealicense.com/licenses/>`_, 
  `licences commentées <http://www.gnu.org/licenses/license-list.fr.html>`_
* **purpose** : description plus détaillée


.. runpython::
    :showcode:
    :rst:
    
    from ensae_teaching_cs.automation import rst_table_modules
    print(rst_table_modules())


