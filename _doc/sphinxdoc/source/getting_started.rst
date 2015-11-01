


Getting started
---------------

.. index:: R, Julia, WinPython, Anaconda, pyminstall, getting started

Résumé
++++++

Les instructions mentionnées ci-dessous fonctionnent sous Windows, Linux et Mac.
Des différences peuvent apparaître mais elles seront explicitées.


**Recommandations**

* Linux/Mac OS : distribution `Anaconda <http://continuum.io/downloads#py34>`_ (python 3.4, 64 bit)
* Windows : une `distribution customisée <http://www.xavierdupre.fr/enseignement/>`_ [#fpm1]_ 
  ou la distribution  `WinPython <https://winpython.github.io/>`_

**Installer un module soi-même**

Il faut ouvrir une fenêtre ligne de commande (Windows) ou une fenêtre terminal (Linux, OS/X) et se placer dans le répertoire de la distribution.

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

Par défaut, l'installation d'un module implique celle de ses dépendances
ce qu'il est possible d'éviter : ::

    pip install <module> --no-deps


**Installer un module avec pymy_install**

Le module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_ 
recherche la meilleure façon d'installer un module quelque soit votre installation. 
Pour l'installer ou le mettre à jour : ::

    pip install pymyinstall --upgrade

L'installation du module crée deux scripts,
``pymy_install3`` pour installer un module,
``pymy_update3`` pour mettre à jour.
Le module permet d'installer un ensemble de modules ::

    pymy_install3 --set=pyensae



Data Scientist
++++++++++++++

La version recommandée est Python 3.4, 64 bit. Par défaut, les modules 
s'installent avec ``pip install <module>`` ou avec ``conda install <module>``
pour les modules distribués par Anaconda. 
Le plus simple est sans doute d'utiliser une distribution qui inclut
les modules les plus usités. Deux options possibles :

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


Configuration
+++++++++++++

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

pip, python et ligne de commande
++++++++++++++++++++++++++++++++


Le language python s'est doté d'un système de distribution de modules (ou *packages*)
qui est aisément accessible depuis la `ligne de commande <http://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande>`_.
Sous Windows, on peut lancer la ligne de commande par la commande ``cmd``. On obtient une fenêtre noire.
Il suffit alors de se déplacer dans le répertoire d'installation de Python ::

    cd c:\Python34_x64\Scripts
    
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
    
    
pymyinstall
+++++++++++
    
Le module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_    
est conçu pour installer la plupart des modules en choisissant le moyen le plus
approprié selon votre distribution. Pour l'installer ::

    pip install pymyinstall
    
Puis ::

    pymy_install3 <module_name>
    
Ou pour le mettre à jour ::

    pymy_update3 <module_name>
    
Le module référence des lises de modules conseillés ::

    pymy_install3 --set=pyensae
    
Ou ::    

    pymy_install3 --set=ensae_teaching_cs

    
Désinstallation
+++++++++++++++

Il est possible de désinstaller simplement les modules installés pour
ces enseignements::

::

    pip uninstall pyquickhelper pyensae pymmails pyrsslocal pysqllike 
    pip uninstall ensae_teachings_cs
    pip uninstall code_beatrix actuariat_python 

    
    
Editeur de texte et navigateur
++++++++++++++++++++++++++++++

.. index:: éditeur, IDE

* `SciTe <http://www.scintilla.org/SciTE.html>`_, le plus simple et le plus léger,
  lire cet article pour le configurer
  `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_.
* `PyCharm <https://www.jetbrains.com/pycharm/>`_, c'est un environnement complet de développement,
  très pratique pour débugger, repérer des erreurs avant l'exécution (nom de variable inconnus...)
  
.. index:: navigateur, notebook  

Les navigateur sont importants pour l'utilisation des notebooks. Je recommande soit
`Firefox <https://www.mozilla.org/fr/firefox/new/>`_, 
soit `Chrome <http://www.google.com/chrome/>`_. Internet Explorer pose quelques problèmes
avec l'utilisateur du Javascript. Ces deux navigateurs sont indispensables si vous insérez du javascript
dans nos notebooks.
        
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

* `PyTools <http://pytools.codeplex.com/>`_ (Windows uniquement)
* `PyCharm <https://www.jetbrains.com/pycharm/>`_
    

Les outils pour développer
++++++++++++++++++++++++++

Impératif :

* `Python 3.4 64 bit <https://www.python.org/downloads/>`_
* `R <http://www.r-project.org/>`_
* `Scite <http://www.scintilla.org/SciTE.html>`_ : éditeur de texte très léger
* `7zip <http://www.7-zip.org/>`_ : pour compresser, décompresser tous les formats
* `Firefox <https://www.mozilla.org/fr-FR/firefox/new/>`_, `Chrome <http://www.google.com/chrome/>`_ : navigateurs 
  (il faut éviter Internet Explorer pour les notebooks IPython)
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

Optionnel :

* `Visual Studio Community <https://www.visualstudio.com/>`_ : C++, C#, F#, Python avec `PythonTools <https://pytools.codeplex.com/>`_
* `MinGW <http://www.mingw.org/>`_ : compilateur C++
* `iTunes <https://www.apple.com/itunes/>`_ (+ de la musique)


.. rubric:: Footnotes

.. index:: pymyinstall, distribution

.. [#fpm1] Cette distribution est construite grâce à la fonction 
           `win_python_setup <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/pymyinstall/win_installer/win_setup_main.html#pymyinstall.win_installer.win_setup_main.win_python_setup>`_
           du module
           `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/pymyinstall/>`_.
           La construction du setup prend quelques heures et inclut les modules
           listés répertoriés par :ref:`l-data2a`.