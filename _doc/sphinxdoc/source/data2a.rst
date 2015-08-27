

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
b. Environnements
    - `IDLE <https://docs.python.org/3.4/library/idle.html>`_
    - `ligne de commande IPython <http://ipython.org/ipython-doc/2/interactive/reference.html>`_
    - `Spyder <http://pythonhosted.org//spyder/>`_  (environnement de type `RStudio <http://www.rstudio.com/>`_)
    - `Rodeo <https://pypi.python.org/pypi/rodeo>`_  (Spyder version web et épurée)
    - `Notebooks <http://ipython.org/notebook.html>`_
c. Editeur de texte (pour des projets plus ambitieux, SciTE, PyCharm, PyTools, WingIDE)
    - `Scite <http://www.scintilla.org/SciTE.html>`_
    - `Notepad++ <https://notepad-plus-plus.org/>`_
    - `SublimeText <http://www.sublimetext.com/>`_
    - `PyCharm <http://www.jetbrains.com/pycharm/>`_
    - `PyTools <http://pytools.codeplex.com/>`_
    - `WingIDE <https://wingware.com/>`_ (version académique `Wing IDE 101 <https://wingware.com/downloads/wingide-101>`_)
        

.. index:: wheel

Modules Python
++++++++++++++

Les modules suivant font partie du setup proposés aux étudiants.

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



Quelques articles
+++++++++++++++++

* `Gradient Boosted Regression Trees <http://orbi.ulg.ac.be/bitstream/2268/163521/1/slides.pdf>`_
* `A Reliable Effective Terascale Linear Learning System <http://arxiv.org/pdf/1110.4198v3.pdf>`_
* `Understanding Random Forest <http://orbi.ulg.ac.be/handle/2268/170309>`_
* `scikit lectures <http://scipy-lectures.github.io/>`_
* `Formation à Python scientifique - ENS Paris <http://python-prepa.github.io/index.html>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `Python Tools for Machine Learning <http://www.cbinsights.com/blog/python-tools-machine-learning/>`_
* `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
* `22 outils gratuits pour visualiser et analyser les données (1ère partie) <http://www.lemondeinformatique.fr/actualites/lire-22-outils-gratuits-pour-visualiser-et-analyser-les-donnees-1ere-partie-47241-page-3.html>`_


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
    - `Probabilistic Programming and Bayesian Methods for Hackers <http://nbviewer.ipython.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Prologue/Prologue.ipynb>`_,
      (`second version <http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/>`_)
- Vidéo
    - `Scikit-Learn: Machine Learning en Python <http://www.microsoft.com/france/mstechdays/programmes/2014/fiche-session.aspx?ID=295be946-2c69-458a-8545-bcebe7970fd8>`_
    - `PyVideo <http://www.pyvideo.org/>`_
    - `PyData TV <https://www.youtube.com/user/PyDataTV>`_
