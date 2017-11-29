
.. _l-getting_started_full:

===============
Getting started
===============

.. contents::
    :local:
    :depth: 2

.. index:: R, Julia, WinPython, Anaconda, pyminstall, getting started

Lorsqu'on fait des statistiques, le language :epkg:`Python` est loin d'être
aussi complet que `R <https://www.r-project.org/>`_
qui a été pensé dans ce but. Il faut lui ajouter plusieurs dizaines
de modules. C'est à ce moment qu'on découvrir les subtilités dans les différents
systèmes d'exploitations, les compilateurs, les dépendances, la ligne de commande.
Ce paragraphe décrit un moyen d'installation :epkg:`Python` sur les trois
systèmes principaux
`Windows <http://www.microsoft.com/fr-fr/windows>`_,
`OS X <http://www.apple.com/osx/>`_,
`Linux <https://en.wikipedia.org/wiki/Linux>`_
avec les modules nécessaires présentés dans ce cours.
Le premier paragraphe explique comment installer rapidement :epkg:`Python`,
il faudra lire les suivants si vos besoins vont au delà.

.. _l-installation-courte:

En résumé : Anaconda
====================

En résumé, le conseil le plus fréquent qu'on donne à ceux qui souhaitent
installer :epkg:`Python` est d'utiliser la distribution :epkg:`Anaconda`.
C'est l'équivalent de :epkg:`R`.
Sans autre étape supplémentaire, elle permet de faire du calcul matriciel
:epkg:`numpy`, de tracer des graphiques avec :epkg:`matplotlib`,
de manipuler les données `pandas <http://pandas.pydata.org/>`_
et de faire du machine du machine learning
:epkg:`scikit-learn`.
La plupart des exercices proposés sur ce site n'utilisent pas plus que ce qui est proposé
dans cette distribution standard. Pour les autres,
les instructions mentionnées ci-dessous fonctionnent sous Windows, Linux et Mac.

* Installation :epkg:`Anaconda` (python 64 bit)
* Mise à jour de la distribution avec ``conda update --all`` (en ligne de commande).

Pour installer le module implémenté pour ce cours :

* ``pip install ensae_teaching_cs``

Windows
=======

Certains modules nécessitent une compilation C++.
:epkg:`Anaconda` fournit la plupart d'entre eux. Pour les autres, il faut allez à
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
Certains modules n'existent pas sous forme précompilée à moins de le faire soi-même.
Et c'est ce que j'ai fait pour certains modules
comme :epkg:`dlib`.

::

    pip install pymyinstall
    pymy_install xgboost

Linux en ligne de commande / MacOS
++++++++++++++++++++++++++++++++++

Voir `Install Miniconda through SSH connection <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2015/2015-11-01_anaconda_ssh.html>`_.
Cela fonctionne avec les distributions `Ubuntu 14.04 <http://releases.ubuntu.com/14.04/>`_
et `Ubuntu 16.04 <http://releases.ubuntu.com/16.04/>`_. Vous pouvez par exemple
suivre les instructions utilisées pour tester et compiler ce site disponibles dans le fichier
`config.yml <https://github.com/sdpython/ensae_teaching_cs/blob/master/.circleci/config.yml>`_.
Les sorties disponibles sur le site
`CircleCI <https://circleci.com/gh/sdpython/ensae_teaching_cs/>`_
peuvent vous aider à comprendre les erreurs si vous en avez.

Les mêmes instructions devraient fonctionner sous MacOS depuis
une fenêtre `terminal <https://en.wikipedia.org/wiki/Terminal_(macOS)>`_
car ce système s'appuie sur une distribution Linux.

.. _l-gs-ide:

IDE
+++

Un IDE est un `environnement de développement <https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement>`_.
Et comme on ne fait pas tout depuis un notebook, il faut en choisir un un.

* `Atom <https://atom.io/>`_
* `Ninja IDE <http://ninja-ide.org/home/>`_
* `PTVS <http://microsoft.github.io/PTVS/>`_ (Python Tools for Visual Studop)
* `PyCharm <http://www.jetbrains.com/pycharm/>`_
* `PyDev <http://pydev.org/>`_ (fonctionne avec `Eclipse <http://www.eclipse.org/>`_)
* `Pyzo <http://www.pyzo.org/>`_ : ressemble à Matlab  (anciennement `IEP <http://www.iep-project.org/index.html>`_)
* `WingIDE <https://wingware.com/>`_

Editeur de texte
++++++++++++++++

Si vous êtes dans le train et que vous n'avez pas beaucoup de batterie,
il faut revenir à l'essentiel : un `éditeur de texte <https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte>`_.

* `Emacs <https://www.gnu.org/software/emacs/>`_
* `nano <https://www.nano-editor.org/>`_ (linux)
* :epkg:`Notepad++`
* :epkg:`SciTE`, le plus simple et le plus léger,
  lire cet article pour le configurer
  `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_.

Installer un module
===================

pip, python et ligne de commande
++++++++++++++++++++++++++++++++

Le language python s'est doté d'un système de distribution de modules (ou *packages*)
qui est aisément accessible depuis la `ligne de commande <http://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande>`_.
Sous :epkg:`Windows`, on peut lancer la ligne de commande par la commande ``cmd``.
Sous :epkg:`Linux` ou :epkg:`OS/X`, c'est une fenêtre terminal (:epkg:`Linux`, :epkg:`OS/X`).
Il suffit alors de se déplacer dans le répertoire d'installation de :epkg:`Python` ::

    cd c:\Python36_x64\Scripts

Ou encore :

::

    cd c:\Anaconda3\Scripts

Puis d'écrire :

::

    pip install <module>

Sous :epkg:`Linux` ou :epkg:`OS/X` (Apple), la ligne de commande
s'appelle le `terminal <http://doc.ubuntu-fr.org/terminal>`_.
Comme :epkg:`Python` est déjà installé en version 2.7, je recommande
l'installation de la distribution :epkg:`Anaconda` en version 3.6
qui facilite la coexistence de plusieurs versions de :epkg:`Python`.
On procède de la même manière ::

    cd /home/<alias>/anaconda3/bin

Puis ::

    pip install <module>

Pour vous assurer que cela correspond bien à la version de :epkg:`Python`
souhaitée, il suffit de demander la version installée ::

    pip --version

Sous :epkg:`Windows`, pour l'ajout d'un module ponctuel,
si l'instruction ``pip install <module>`` ne fonctionne pas,
c'est vraisemblablement parce que ce module contient une partie en C++.
Dans ce cas, il faut aller voir sur ce site
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
s'il est disponible. S'il ne l'est pas, l'installation du module est
réservée aux experts.

conda ou pip
++++++++++++

:epkg:`Anaconda` maintient des versions de librairies :epkg:`Python`.
Pour tous les modules de cette liste,
`Anaconda Package List <https://docs.continuum.io/anaconda/packages/pkg-docs>`_,
il faut utiliser ``conda install <module>``.
Pour les autres, ``pip install <module>``.
Cela ne fonctionne qu'avec la distribution
:epkg:`Anaconda`.

L'instruction ``pip install`` ne fonctionne pas sous :epkg:`Windows`
lorsque le module est implémenté en :epkg:`Python` et :epkg:`C++`.
C'est pourquoi il est préférable d'installer
une version précompilée.

Dépendances
+++++++++++

Par défaut, l'installation d'un module implique celle de ses dépendances
ce qu'il est possible d'éviter :

::

    pip install <module> --no-deps

Installer un module avec pymy_install
+++++++++++++++++++++++++++++++++++++

Le module :epkg:`pymyinstall`
recherche la meilleure façon d'installer un module quelque soit votre installation.
Pour l'installer ou le mettre à jour :

::

    pip install pymyinstall --upgrade

L'installation du module crée deux scripts,
``pymy_install3`` pour installer un module,
``pymy_update3`` pour mettre à jour.
Le module permet aussi d'installer un ensemble de modules.
La ligne suivante installe un module développé pour ce cours
et ses dépendances :

::

    pymy_install3 --set=pyensae

.. _l-desinstallation-modules:

Désinstallation des modules implémentés pour ce cours
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Il est possible de désinstaller simplement les modules installés pour
ces enseignements ::

.. runpython::

    from ensae_teaching_cs.automation.teaching_modules import get_teaching_modules
    for mod in sorted(get_teaching_modules()):
        print('pip uninstall -y {}'.format(mod))

Configuration pour ces cours
++++++++++++++++++++++++++++

Les notebooks utilisent le module :epkg:`pyensae`
développé pour ces enseignements. Pour installer ses dépendances,
il faut utiliser le module :epkg:`pymyinstall`. Les dépendances
s'installent comme suit :

    pymy_install3 --set=ensae_teaching_cs
    pip install ensae_teaching_cs

Certains notebooks requièrent des outils supplémentaires :

* :epkg:`GraphViz`

.. index:: pip, ligne de commande

Compiler un module
++++++++++++++++++

* `Compiler les librairies Python sous Windows <https://makina-corpus.com/blog/metier/2016/compile_python_wheels_windows/compiler-les-librairies-python-sous-windows>`_

Distributions
=============

.. index:: anaconda, winpython

* :epkg:`Anaconda` (Windows, Linux, Mac).
  Sous :epkg:`Linux` ou :epkg:`OS/X`, la distribution n'interfère pas
  avec la distribution existante souvent différente. C'est un point très
  appréciable. Les modules de la distribution ne sont
  pas tous à jour. Il faut penser à mettre à jour avec la commande
  ``conda install <module>`` depuis le répertoire ``Anaconda3/Scripts``
  (``conda install cvxopt`` par exemple). Il existe une version différente :
  :epkg:`miniconda`. La liste des packages manquant sera probablement différente.
  Il suffit d'écrire sur la ligne de commande ``conda update --all``
  pour mettre à jour tous les modules.

* `WinPython <https://winpython.github.io/>`_ (:epkg:`Windows`).
  Sous :epkg:`Windows`, elle inclut parfois :epkg:`R` ou
  :epkg:`Julia` (ces version ne sont pas aussi à jour que la
  version principale). On passe alors facilement de python à :epkg:`R`
  ou :epkg:`Julia` depuis le même notebooks. Uniquement disponible
  sous :epkg:`Windows`, cette installation a l'avantage de ne pas
  nécessiter les droits administrateur pour être installée. Elle
  ne modifie pas les registres et on peut la recopier telle quelle sur une clé USB
  pour la recopier sur un autre ordinateur. On peut également préparer sa propre version
  `How To Make WinPython <https://github.com/winpython/winpython/wiki/How-To-Make-WinPython>`_.

* Distribution officielle de :epkg:`Python`, il faut ensuite
  installer de nombreux modules (voir :ref:`l-data2amod`) pour obtenir
  une distribution équivalente aux deux précédentes.

* :epkg:`miniconda` est une version light de :epkg:`Anaconda`
  sans tous ces packages. Elle peut être installée depuis une ligne de commande, via
  une connexion SSH.
  Voir `Install Anaconda through SSH connection <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2015/2015-11-01_anaconda_ssh.html>`_.

La liste des packages de `WinPython <https://winpython.github.io/>`_ ou
`Anaconda <https://docs.continuum.io/anaconda/pkg-docs>`_
sont d'excellents moyens de découvrir de nouveaux modules intéressants.

Modules incournables pour un data scientist
===========================================

Les modules indispensables sont intégrés à la distribution
`Anaconda <https://www.continuum.io/downloads>`_, `WinPython <https://winpython.github.io/>`_.

*Les indispensables*

* :epkg:`dask` : dataframe distribué et capables de gérer des gros volumes de données (> 5Go)
* :epkg:`Jupyter` :
  gestion des notebooks (des pages blanches mélangeant code, équations, graphiques)
* :epkg:`matplotlib` : graphes scientifiques
* :epkg:`numpy` : calcul matriciel
* :epkg:`pandas` : gestion de `DataFrame <http://en.wikipedia.org/wiki/Data_frame>`_
* :epkg:`Scipy` : calcul scientifique
* :epkg:`scikit-learn` : machine learning, statistique descriptive
* :epkg:`statsmodels` : séries temporelles

*Visualisation*

Voir `10 plotting libraries at PyData 06/14/2016 in Paris <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_.

*Jeux*

* `pygame <http://www.pygame.org/>`_
* `kivy <http://kivy.org/#home>`_ : pour faire des jeux ou des applications pour tablettes, téléphones

*Pour les TD et projets à l'ENSAE*

* :epkg:`pyensae` : outils pour les élèves de l'ENSAE
* :epkg:`pyquickhelper` : outils d'automatisation

*Pour faire du machine learning sans programmer*

* `Orange3 <http://orange.biolab.si/orange3/>`_

Outils, ressources pour développer
==================================

Développer un programme informatique prend du temps et il est important d'être à l'aise.
Une grande difficulté lorsqu'on programme c'est de travailler à plusieurs sur le même projet.
Il faut se sychroniser. Fort heureusement, le problème est connu depuis longtemps et il existe beaucoup
d'outils open source dont on aurait tort de se passer ou des services gratuits sous certains conditions
qui facilitent l'archivage.

En vrac
+++++++

*Suivi de sources distant*

* `GitHub <https://github.com/>`_ : c'est le site par référence pour tous les projets
  open source.
* `GitLab <https://about.gitlab.com/>`_
* `BitBucket <https://bitbucket.org/>`_

*Git*

*git* est un logiciel de suivi de source. Il a supplanté tous les autres
et il est indispensable aujourd'hui de le connaître. On ne retient pas toujours
les commandes mais un moteur de recherche fournit rapidement la réponse.
Voir aussi
`Cheat Sheet <http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf>`_.

* `Git <http://git-scm.com/>`_ + `GitHub <https://github.com/>`_ : pour suivre ses projets avec Git
* `TortoiseGit <https://code.google.com/p/tortoisegit/>`_ (Windows)

**Archivage distant**

* `hubiC <https://hubic.com/fr/>`_  (25 Go gratuit - août 2015)
* `OneDrive <https://onedrive.live.com/about/fr-fr/>`_ (15 Go gratuit - août 2015)

Ce ne sont pas les seuls, vous trouverez d'autres options ici :
`cloud-gratuit <http://www.cloud-gratuit.com/>`_. Toutefois, **il est recommandé de faire attention
avec les données personnelles sensibles**. Il n'est pas toujours possible de choisir
le lieu de stockage et chaque pays a une législation différente.
Même si vos données sont protégées par un mot de passe et ne sont pas publiques,
il arrive que certains mots de passe soient interceptés.

*Comparaison de fichiers*

* `kdiff3 <http://kdiff3.sourceforge.net/>`_
* `Beyond and Compare <http://www.scootersoftware.com/>`_ :
  il est gratuit pendant un mois, c'est le plus convivial.

*Partager des notes, des idées*

* `OneNote <http://office.microsoft.com/fr-fr/onenote/>`_
* `Evernote <https://evernote.com/intl/fr/>`_
* `Google Docs <https://docs.google.com/>`_

*Editeur de texte*

* :epkg:`SciTE` : le plus simple, pas d'explorateur de fichier, pas d'installeur, autocomplétion perturbante
* `TextWrangler <http://www.barebones.com/products/textwrangler/>`_ (seulement sur iOS - Apple)
* `SublimeText <http://www.sublimetext.com/>`_ : configuration nécessaire avant d'exécuter un script python
* :epkg:`Notepad++` : configuration nécessaire avant d'exécuter un script python

*IDE*

* `Atom <https://atom.io/>`_
* `Ninja IDE <http://ninja-ide.org/home/>`_
* `PyCharm <http://www.jetbrains.com/pycharm/>`_
* `PyDev <http://pydev.org/>`_ (fonctionne avec `Eclipse <http://www.eclipse.org/>`_)
* `PTVS <https://microsoft.github.io/PTVS/>`_ (fonctionne avec `Visual Studio <http://www.visualstudio.com/>`_)
* `Pyzo <http://www.pyzo.org/>`_ : ressemble à Matlab  (anciennement `IEP <http://www.iep-project.org/index.html>`_)
* `WingIDE <https://wingware.com/>`_

*Python et Domotique*

* `Micro Python Project <https://github.com/micropython/micropython>`_
* `Python et Arduino <http://playground.arduino.cc/Interfacing/Python>`_
* `Python et RaspberryPI <http://www.raspberrypi.org/documentation/usage/python/README.md>`_

*Navigateur*

.. index:: navigateur, notebook

Les navigateur sont importants pour l'utilisation des notebooks. Je recommande soit
`Firefox <https://www.mozilla.org/fr/firefox/new/>`_,
soit `Chrome <http://www.google.com/chrome/>`_.
Ces deux navigateurs sont indispensables si vous insérez du javascript
dans nos notebooks. Le débuggeur de Chrome est le plus pratique à utiliser quand il s'agit d'aller
fouiller dans les feuilles de styles ou de voir l'exécution du javascript.

.. index:: développeur

*Documentation*

La documentation et les tests unitaires les modules
classés dans les catégories *SPHINX*, *TEACH* (voir table ci-dessous).
Certaines séances pratiques utilisent des données depuis ce site.
Elles sont facilement téléchargeables avec ces deux modules :

* :epkg:`pyquickhelper` : ce module compile ce cours
* :epkg:`pyensae` : outils variés pour les élèves de l'ENSAE
* :epkg:`pymyinstall` : installer facilement des modules sous Windows

Pour être compilée, la documentation requiert également :

* :epkg:`GraphViz` : représenter des graphes
* :epkg:`InkScape`
* :epkg:`MiKTeX` (Windows seulement)
* :epkg:`pandoc`

*Continuous build*

* `Buildbot <http://buildbot.net/>`_
* `Java <http://www.java.com/fr/download/>`_ : nécessaire pour Jenkins et `Antlr <http://www.antlr.org/>`_
* :epkg:`Jenkins` (plus les plugins pour
  `GitHub <https://wiki.jenkins-ci.org/display/JENKINS/GitHub+Plugin>`_,
  `git <https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin>`_,
  `python <https://wiki.jenkins-ci.org/display/JENKINS/Python+Plugin>`_,
  `pipeline <https://wiki.jenkins-ci.org/display/JENKINS/Build+Pipeline+Plugin>`_,
  `Build timeout plugin <https://wiki.jenkins-ci.org/display/JENKINS/Build-timeout+Plugin>`_,
  `Console column plugin <https://wiki.jenkins-ci.org/display/JENKINS/Console+Column+Plugin>`_,
  `Next executions <https://wiki.jenkins-ci.org/display/JENKINS/Next+Executions>`_,
  `Collapsing Console Sections Plugin <https://wiki.jenkins-ci.org/display/JENKINS/Collapsing+Console+Sections+Plugin>`_)
* :epkg:`Visual Studio Community Edition 2015` : C++, C#, F#, Python
  avec `PTVS <https://microsoft.github.io/PTVS/>`_
* :epkg:`MinGW` : compilateur C++

*Compression*

* `7zip <http://www.7-zip.org/>`_ : pour compresser, décompresser tous les formats

*Ressources*

* `Developpez.com <http://www.developpez.com/>`_ : beaucoup de choses autour de la programmation et en français
* `stackoverflow <http://stackoverflow.com/>`_ : énorme forum de discussion sur tout ce qui touche à la programmation
* `Jardin Zen Css <http://www.csszengarden.com/>`_ (la même page avec une multitude de styles différents)
* `Le blog univers domotique <http://blog.univers-domotique.com/>`_
* `Tutoriel sur GIT <http://sixrevisions.com/resources/git-tutorials-beginners/>`_

Générer une documentation comme ce cours
++++++++++++++++++++++++++++++++++++++++

Lire `List of tools needed to build the documentation <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/blog/2017/2017-04-27_setup.html>`_.

Setup pour déveloper ce cours (Windows)
+++++++++++++++++++++++++++++++++++++++

* `7zip <http://www.7-zip.org/>`_
* `Anaconda <https://www.continuum.io/downloads>`_
  2 et 3 (à installer sur le même disque que le répertoire
  utilisé pour Jenkins)
* `Chrome <https://www.google.fr/chrome/browser/desktop/>`_
* `CMake <https://cmake.org/>`_ (pour compiler XGBoost)
* `Graphviz <http://www.graphviz.org/>`_
* `Git <https://git-scm.com/>`_
* `GitHub <https://desktop.github.com/>`_
* `Java 64 bit <https://www.java.com/fr/download/manual.jsp>`_
* `Jenkins <https://jenkins.io/>`_
* `Miktex basic installer 64 bit <https://miktex.org/download>`_
  (lors de l'installation, il faut cocher l'installation automatique de nouveaux packages)
* `Pandoc <http://pandoc.org/>`_
* `Python <https://www.python.org/>`_ 3.5, 3.6, 2.7 64 bit
  (il ne faut pas ajouter les interpréteur au PATH par défaut)
* `R 3.2.2 <https://cran.r-project.org/bin/windows/base/old/3.2.2/>`_
* :epkg:`SciTE`
* `mingw-w64 <https://mingw-w64.org/doku.php>`_ (:epkg:`theano`)
  (voir :ref:`Installer theano et un compilateur C++ <blog-install-theno-keras>`)
* `Visual Studio 2015 Community Edition <https://www.visualstudio.com/fr/vs/community/>`_
  (cocher C++, C#, Python comme langage + CLang comme compilateur)

Pour chaque version de :epkg:`Python`, il faut installer
`pymyinstall <https://pypi.python.org/pypi/pymyinstall/>`_
puis écrire ``pymy_install`` puis supprimer les modules qu'on
souhaite compiler et tester (voir :ref:`l-desinstallation-modules`).

Quelques modules particuliers : plus trop maintenus mais parfois utiles et parfois modifiés

::

    pip install https://github.com/sdpython/pyPdf/archive/trunk.zip

En plus :

* `Cygwin <https://www.cygwin.com/>`_
* `FileZilla <https://filezilla-project.org/>`_
* `InnoSetup <http://www.jrsoftware.org/isdl.php>`_ (version unicode)

Pour :epkg:`Jenkins`, quelques extensions :

* `Build timeout plugin <https://wiki.jenkins-ci.org/display/JENKINS/Build-timeout+Plugin>`_
* `Collapsing Console Sections Plugin <https://wiki.jenkins-ci.org/display/JENKINS/Collapsing+Console+Sections+Plugin>`_
* `Console column plugin <https://wiki.jenkins-ci.org/display/JENKINS/Console+Column+Plugin>`_
* `Extra Columns Plugin <https://wiki.jenkins-ci.org/display/JENKINS/Extra+Columns+Plugin>`_
* `Next Executions <https://wiki.jenkins-ci.org/display/JENKINS/Next+Executions>`_
* `Text File <https://wiki.jenkins-ci.org/display/JENKINS/Text+File+Operations+Plugin>`_
* `Startup Trigger <https://wiki.jenkins.io/display/JENKINS/Startup+Trigger>`_ : automatisation de build

Pour :epkg:`Jupyter` :

::

    pip install widgetsnbextension
    jupyter nbextension enable --py --sys-prefix widgetsnbextension

Un serveur en local doit être démarré, la ligne de commande ressemble à ceci :

::

    c:\Python36_x64\Scripts\pypi-server.exe -u -p 8067 --disable-fallback ..\..\local_pypi\local_pypi_server

Si le serveur :epkg:`Jenkins` utilise des mots-clés via :epkg:`keyring`,
ce qui est le cas pour plusieurs modules utilisés pour ces enseignements,
il est nécessaire de créer un serveur un serveur :epkg:`Jenkins` authentifié.
Sous :epkg:`Windows` , il faut chercher ``services.msc`` et renseigner
les identifiants.
Pour certains projets (comme la compilation de :epkg:`pywin32`), il faut
installer `Windows SDK <https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk>`_.

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

L'essentiel n'est pas de tout faire en :epkg:`Python`, l'essentiel est d'être agile,
de passer le moins de temps sur l'implémentation et le plus de temps possible
sur les données.

*Listes de modules*

* `data-science-ipython-notebooks <https://github.com/donnemartin/data-science-ipython-notebooks>`_
* `Awesome Python <https://github.com/vinta/awesome-python#environment-management>`_,
  répertoire de librairies :epkg:`Python` populaires (donc à regarder en premier)
* `Trending Python <https://github.com/trending?l=python>`_
* `Trending Python <https://github.com/trending?l=python&since=monthly>`_ (mensuel)
* `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
* conférence `pydata <http://pydata.org/>`_

*Quelques articles*

* `scikit lectures <http://scipy-lectures.github.io/>`_
* `Formation à Python scientifique - ENS Paris <http://python-prepa.github.io/index.html>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `Python Tools for Machine Learning <http://www.cbinsights.com/blog/python-tools-machine-learning/>`_
* `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
* `22 outils gratuits pour visualiser et analyser les données (1ère partie) <http://www.lemondeinformatique.fr/actualites/lire-22-outils-gratuits-pour-visualiser-et-analyser-les-donnees-1ere-partie-47241-page-3.html>`_
* `Gradient Boosted Regression Trees <http://orbi.ulg.ac.be/bitstream/2268/163521/1/slides.pdf>`_
* `A Reliable Effective Terascale Linear Learning System <http://arxiv.org/pdf/1110.4198v3.pdf>`_
* `Understanding Random Forest <http://orbi.ulg.ac.be/handle/2268/170309>`_

*Liens, blogs à suivre*

- `FastML <http://fastml.com/>`_
- `no free hunch (Kaggle Blog) <http://blog.kaggle.com/>`_
- `Sebastian Raschka <http://sebastianraschka.com/articles.html>`_
- `yhat <http://blog.yhathq.com/>`_
- `NumFOCUS Foundation <http://numfocus.org/projects/index.html>`_
- `pythonworks.org <http://www.pythonworks.org/home>`_ (références de livres)

*Articles Livres, Vidéos*

- `Scikit-learn: Machine Learning in Python <http://jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf>`_ (avec les auteurs de scikit-learn)
- `Deep Learning <http://www-labs.iro.umontreal.ca/~bengioy/dlbook/>`_
  by Yoshua Bengio, Ian Goodfellow and Aaron Courville
- `Building Machine Learning Systems with Python <https://github.com/luispedro/BuildingMachineLearningSystemsWithPython>`_
  by Willi Richert, Luis Pedro Coelho published by PACKT PUBLISHING (2013) 
- `Machine Learning <https://github.com/pbharrin/machinelearninginaction>`_
  in Action by Peter Harrington
- `Probabilistic Programming and Bayesian Methods for Hackers <http://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Prologue/Prologue.ipynb>`_,
  (`second version <http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/>`_)
- `Scikit-Learn: Machine Learning en Python <http://www.microsoft.com/france/mstechdays/programmes/2014/fiche-session.aspx?ID=295be946-2c69-458a-8545-bcebe7970fd8>`_
- `PyVideo <http://www.pyvideo.org/>`_
- `PyData TV <https://www.youtube.com/user/PyDataTV>`_
- `dotconference.com <https://www.dotconferences.com/>`_

.. _l-data2amod:

Liste exhaustive de modules Python
==================================

.. index:: wheel

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

.. rubric:: Footnotes

.. index:: pymyinstall, distribution
