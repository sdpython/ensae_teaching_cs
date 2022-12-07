
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

Notes
=====

La grande majorité des exemples et des notebooks
proposés sur ce site sont testés une fois par mois.
La distribution utilisée varie mais s'appuie sur les dernières
versions des modules. Une part moins importante est également testée
à chaque modification sur :epkg:`github/sdpython` sur Windows,
Linux (Ubuntu) et Linux (Debian).

.. _l-auto-2018-2019:

2020-2021
+++++++++

Les tests sont dorénavant effectués sur
*Linux Debian 10* et la distribution standard *Python 3.9.1*.
Les traces d'installation ont été conservées dans cet article
`2021-01-09 Install Python 3.9 and many packages on Linux Debian 10
<http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/2021/2021-01-09_debian.html>`_.

2018-2020
+++++++++

Pour l'année 2017, les tests sont dorénavant effectués sur
*Linux Debian 9* et la distribution standard *Python 3.7.0*.
L'installation de cette machine est assez fastidieuse. Les traces
de l'installation sont conservées sur cet article de blog :
`Install Python 3.7 and many packages on Linux Debian 9 <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/2018/2018-08-19_python37.html>`_.
Il reste quelques problèmes comme :epkg:`TensorFlow` qui n'est pas
encore compatible avec *Python 3.7* (août 2018) mais
cette `pull request <https://github.com/tensorflow/tensorflow/pull/21202>`_
devrait résoudre le problème.

2017-2018
+++++++++

Toutes les modules étaient testées sur
*Windows 10* et une distribtion standard
*Python 3.6.4* puis *Python 3.6.5* 64 bits.

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
:epkg:`Anaconda` fournit la plupart d'entre eux.
Et Les plus utilisés sont de plus en plus disponibles sur
`pypi <https://pypi.org/>`_. Pour les autres, la plupart des
modules sont disponibles sur `PyPi <https://pypi.org/>`_.
Sinon il faudra passer par WSL (voir blog post du 
:ref:`7 décembre 2022 <blog-cartopy-2022>`).
Certains modules n'existent pas sous forme précompilée à
moins de le faire soi-même. Il faut qu'un compilateur
soit installée sur la machine et sans doute d'autres
dépendances. Il est possible aussi de suivre les instructions
exécutées à chaque changement :
`appveyor.yml
<https://github.com/sdpython/ensae_teaching_cs/blob/master/appveyor.yml>`_.

Linux en ligne de commande / MacOS
++++++++++++++++++++++++++++++++++

La page `Anaconda Documentation Installation
<https://docs.anaconda.com/anaconda/install/>`_ est assez
précise quant à la démarche à suivre pour installer
`Anaconda <https://www.anaconda.com/>`_ ou
`Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_.
Vous pouvez aussi suivre les instructions utilisées à chaque
changement `config.yml
<https://github.com/sdpython/ensae_teaching_cs/blob/master/.circleci/config.yml>`_.

Il existe des différences sur MacOs. Mais vous pouvez suivre
les instructions contenus dans ce fichier `azure-pipelines.yml
<https://github.com/sdpython/mlprodict/blob/master/azure-pipelines.yml#L63>`_.

.. _l-gs-ide:

IDE
+++

Un IDE est un `environnement de développement <https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement>`_.
Et comme on ne fait pas tout depuis un notebook, il faut en choisir un un.

* `Visual Studio Code <https://code.visualstudio.com/>`_
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

Le language :epkg:`python` s'est doté d'un système de distribution de modules (ou *packages*)
qui est aisément accessible depuis la `ligne de commande <http://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande>`_.
Sous :epkg:`Windows`, on peut lancer la ligne de commande par la commande ``cmd``.
Sous :epkg:`Linux` ou :epkg:`OS/X`, c'est une fenêtre terminal (:epkg:`Linux`, :epkg:`OS/X`).
Il suffit alors de se déplacer dans le répertoire d'installation de :epkg:`Python` ::

    cd c:\Python391_x64\Scripts

Ou encore :

::

    cd c:\Anaconda3\Scripts

Puis d'écrire :

::

    pip install <module>

Sous :epkg:`Linux` ou :epkg:`OS/X` (Apple), la ligne de commande
s'appelle le `terminal <http://doc.ubuntu-fr.org/terminal>`_.
Comme :epkg:`Python` est déjà installé en version 2.7, je recommande
l'installation de la distribution :epkg:`Anaconda` en version 3.8
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
S'il ne l'est pas, l'installation du module est
réservée aux experts qui ne fuit pas les messages d'erreur
d'un compilation C++.

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

.. _l-desinstallation-modules:

Désinstallation des modules implémentés pour ce cours
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Il est possible de désinstaller simplement les modules installés pour
ces enseignements :

.. runpython::

    from ensae_teaching_cs.automation.teaching_modules import get_teaching_modules
    for mod in sorted(get_teaching_modules(branch=False)):
        print('pip uninstall -y {}'.format(mod))

Configuration pour ces cours
++++++++++++++++++++++++++++

Certains notebooks requièrent des outils supplémentaires :

* :epkg:`GraphViz`

.. index:: pip, ligne de commande

Compiler un module
++++++++++++++++++

* `Compiler les librairies Python sous Windows
  <https://makina-corpus.com/blog/metier/2016/compile_python_wheels_windows/
  compiler-les-librairies-python-sous-windows>`_

Distributions
=============

.. index:: anaconda, winpython, miniconda

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

Voir `10 plotting libraries at PyData 06/14/2016 in Paris
<http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_
ou :ref:`l-visualisation`.

*Jeux*

* :epkg:`pygame` + :epkg:`thorpy`
* `kivy <http://kivy.org/#home>`_ : pour faire des jeux ou des applications pour tablettes, téléphones

*Pour les TD et projets à l'ENSAE*

* :epkg:`pyensae` : outils pour les élèves de l'ENSAE
* :epkg:`pyquickhelper` : outils d'automatisation

*Pour faire du machine learning sans programmer*

* `Orange <https://orangedatamining.com/>`_

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

* `Git <http://git-scm.com/>`_ + `GitHub <https://github.com/>`_ :
  pour suivre ses projets avec Git
* `TortoiseGit <https://code.google.com/p/tortoisegit/>`_ (Windows)

**Archivage distant**

* `hubiC <https://hubic.com/fr/>`_  (25 Go gratuit)
* `OneDrive <https://onedrive.live.com/about/fr-fr/>`_
* `Google Drive <https://www.google.com/intl/en_jm/drive/>`_
* `DropBox <https://www.dropbox.com/>`_
* ...

Ce ne sont pas les seuls, vous trouverez d'autres options ici :
`cloud-gratuit <https://www.cloud-gratuit.com/>`_. Toutefois, **il est recommandé de faire attention
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
* `Slack <https://slack.com/intl/fr-fr/>`_
* `Google Docs <https://docs.google.com/>`_

*Editeur de texte*

* `Visual Studio Code <https://code.visualstudio.com/>`_ :
  il marche partout, il est gratuit, léger et il a été adopté pas beaucoup de monde
* :epkg:`SciTE` : le plus simple, pas d'explorateur de fichier, pas d'installeur, autocomplétion perturbante
* `TextWrangler <http://www.barebones.com/products/textwrangler/>`_ (seulement sur iOS - Apple)
* `SublimeText <http://www.sublimetext.com/>`_ : configuration nécessaire avant d'exécuter un script python
* :epkg:`Notepad++` : configuration nécessaire avant d'exécuter un script python

*IDE*

* `Visual Studio Code <https://code.visualstudio.com/>`_ :
  il marche partout, il est gratuit, léger et il a été adopté pas beaucoup de monde
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

Pour être compilée, la documentation requiert également :

* :epkg:`GraphViz` : représenter des graphes
* :epkg:`InkScape`
* :epkg:`MiKTeX` (Windows seulement)
* :epkg:`pandoc`

*Continuous build*

* `Buildbot <https://buildbot.net/>`_
* `Java <http://www.java.com/fr/download/>`_ : nécessaire pour Jenkins et `Antlr <http://www.antlr.org/>`_
* :epkg:`Jenkins` (plus les plugins pour
  `GitHub <https://wiki.jenkins-ci.org/display/JENKINS/GitHub+Plugin>`_,
  `git <https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin>`_,
  `python <https://wiki.jenkins-ci.org/display/JENKINS/Python+Plugin>`_,
  `pipeline <https://wiki.jenkins-ci.org/display/JENKINS/Build+Pipeline+Plugin>`_,
  `Build timeout plugin <https://wiki.jenkins-ci.org/display/JENKINS/Build-timeout+Plugin>`_,
  `Console column plugin <https://wiki.jenkins-ci.org/display/JENKINS/Console+Column+Plugin>`_,
  `Next executions <https://wiki.jenkins-ci.org/display/JENKINS/Next+Executions>`_,
  `Collapsing Console Sections Plugin <https://wiki.jenkins-ci.org/display/JENKINS/Collapsing+Console+Sections+Plugin>`_,
  `Exclusive Execution <https://plugins.jenkins.io/exclusive-execution/>`_)
* :epkg:`Visual Studio Community Edition 2015` : C++, C#, F#, Python
  avec `PTVS <https://microsoft.github.io/PTVS/>`_

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

Personnellement, j'ai acheté des livres de Python, le premier pour apprendre
le langage, il m'a servi pour préparer mes premiers cours il y a 5 ou 6 ans,
les autres pour voir ce qu'on pouvait écrire sur le sujet mais ils ne m'ont
jamais vraiment servi. Le machine learning va si vite aujourd'hui que la plupart
des livres d'informatique sont obsolètes en peu de temps. Pour apprendre, un livre
ou un prof fera l'affaire. Ensuite, des livres de mathématiques, des articles...

*Listes de modules*

* `data-science-ipython-notebooks <https://github.com/donnemartin/data-science-ipython-notebooks>`_
* `Awesome Python <https://github.com/vinta/awesome-python#environment-management>`_,
  répertoire de librairies :epkg:`Python` populaires (donc à regarder en premier)
* `Trending Python <https://github.com/trending?l=python>`_
* `Trending Python <https://github.com/trending?l=python&since=monthly>`_ (mensuel)
* conférence `pydata <http://pydata.org/>`_

*Quelques articles*

* `scikit lectures <http://scipy-lectures.github.io/>`_
* `Formation à Python scientifique - ENS Paris <http://python-prepa.github.io/index.html>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `Python Tools for Machine Learning <http://www.cbinsights.com/blog/python-tools-machine-learning/>`_
* `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
* `22 outils gratuits pour visualiser et analyser les données (1ère partie)
  <http://www.lemondeinformatique.fr/actualites/lire-22-outils-gratuits-pour-visualiser-et-analyser-les-donnees-1ere-partie-47241-page-3.html>`_
* `Gradient Boosted Regression Trees <http://orbi.ulg.ac.be/bitstream/2268/163521/1/slides.pdf>`_
* `A Reliable Effective Terascale Linear Learning System <http://arxiv.org/pdf/1110.4198v3.pdf>`_
* `Understanding Random Forest <http://orbi.ulg.ac.be/handle/2268/170309>`_
* `6 Best Python Books for Data Science and Machine Learning in 2021
  <https://medium.com/javarevisited/6-best-python-books-for-data-science-and-machine-learning-in-2021-2f41d9fbf8be>`_
* `20 Best Machine Learning Books for Beginner & Experts in 2021
  <https://hackr.io/blog/best-machine-learning-books>`_

*Liens, blogs à suivre*

- `FastML <https://fastml.com/>`_
- `no free hunch (Kaggle Blog) <https://blog.kaggle.com/>`_
- `NumFOCUS Foundation <https://numfocus.org/sponsored-projects>`_

*Articles Livres, Vidéos*

- `Scikit-learn: Machine Learning in Python
   <https://jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf>`_ (avec les auteurs de scikit-learn)
- `Building Machine Learning Systems with Python
   <https://github.com/luispedro/BuildingMachineLearningSystemsWithPython>`_
  by Willi Richert, Luis Pedro Coelho published by PACKT PUBLISHING (2013) 
- `Machine Learning <https://github.com/pbharrin/machinelearninginaction>`_
  in Action by Peter Harrington
- `Probabilistic Programming and Bayesian Methods for Hackers
  <http://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Prologue/Prologue.ipynb>`_,
  (`second version <http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/>`_)
- `PyVideo <https://www.pyvideo.org/>`_
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
  que le module inclut une partie C++ qu'il est préférable de récupérer déjà compilée,
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
