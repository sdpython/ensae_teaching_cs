

ENSAE - Programmation - Xavier Dupré
====================================

:ref:`l-README`, :ref:`blog <ap-main-0>`


Cette page donne accès au contenu des séances de travaux pratiques en programmation
que je dispense à l'`ENSAE <http://www.ensae.fr/>`_. Ils s'appuient principalement sur 
le langage Python. Le contenu est librement disponible sur `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_
et permet à quiconque de contribuer à ce cours disponible sous trois formats différents : 
`mobile/PC <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_,
`compact/blanc <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/index.html>`_,
`compact/mobile/PC <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_.

Avant-propos
------------

On programme nécessairement avec un **langage** de `programmation <http://fr.wikipedia.org/wiki/Langage_de_programmation>`_.
Ce langage a une grammaire et un vocabulaire. Il n'est pas d'une poésie
irréprochable mais il permet d'exprimer des idées avec une précision tâtillonne.
Comme toute langue qu'on apprend ou toute séance de solfège, 
les premiers pas sont rebutants et on y prend peu de plaisir.
Cela devient plus facile avec une pratique régulière. On passe alors plus de temps
sur son idée et moins sur son programme. Le langage Python est un de ceux
qui demande le moins d'effort. Il est de plus en plus populaire comme en témoignent les 
nombreux exemples sur Internet 
(`Python is Now the Most Popular Introductory Teaching Language at Top U.S. Universities <http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext>`_).



**3 niveaux**

Les cours proposés sont de difficultés croissantes et orientés pour un statisticien ou data scientist.
La pratique est un élément essentiel de l'apprentissage de la programmation.
Quoi qu'on en dise, il faut aussi être créatif.


* **1A :** syntaxe de langage, premiers algorithmes, programmation dynamique, Data Frame, premiers graphes
* **2A :** python pour un statisticien, Data Frames, calcul matriciel, machine learning, 
  exercices d'algorithmie
* **3A :** calculs distribués, Map/Reduce depuis un notebook

Le :ref:`blog <ap-main-0>` associé à ce site publie des liens vers des vidéos,
des données, met en valeur certaines mise à jour, aborde des sujets qui 
seront plus tard, peut-être intégrées au contenu des enseignements. 


Contenu des enseignements
-------------------------

* 3 niveaux
    * :ref:`1A, Initiation à la programmation et l'algorithmie <l-td1a>`
    * :ref:`2A, Données, Machine Learning et Programmation <l-td2a>`
    * :ref:`3A, Eléments logiciels pour le traitement des données massives <l-td3a>`    
* Présentations
    * `Présentation ENSAE 1A - Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx/index.html>`_
    * `Présentation ENSAE 2A - Données et machine learning <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html>`_
    * `Présentation ENSAE 3A - Map/Reduce <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_3A/index.html>`_
* Projets informatiques
    * :ref:`projet informatique 1A <l-projinfo1a>`
    * :ref:`projet informatique 2A <l-projinfo2a>`
    * :ref:`projet informatique 3A <l-projinfo3a>`
* :ref:`Exemples de toutes sortes <l-examplesindex>` dont :
    * :ref:`Exercices d'algorithmie <l-exoalgo>`
    * :ref:`Exposés divers non abordés en cours <l-extra>`
* Questions, termes, FAQ
    * :ref:`FAQ <l-FAQs>`
    * :ref:`Glossaire <l-glossaire>`
    * :ref:`question`
    * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_ (PDF)
* Autres documents
    * :ref:`Articles, Références, Blog <l-biblio>`
    * :ref:`Modules <modulesi>`
    * :ref:`Outils, ressources pour développer <l-devtools>`
    * :ref:`Examens passés <l-examens>` (1A)
    * :ref:`Coding Party <l-codingparty>`
    

    

Prérequis et Installation
-------------------------

**Notebooks**

Les séances utilisent les `notebooks IPython <http://ipython.org/notebook.html>`_.
Au début de chaque séance, il vous suffit de télécharger le notebook qui sert de point
de départ. La correction est également rédigée sous forme de notebook.
Les prérequis sont bien sûr `Python <https://www.python.org/>`_ et les modules qui l'ont rendu
populaire :
`IPython <http://ipython.org/>`_ mais aussi leurs dépendances
`pandas <http://fr.wikipedia.org/wiki/Panda>`_, 
`numpy <http://www.numpy.org/>`_, 
`matplotlib <http://matplotlib.org/>`_. 
Sous Windows, ces modules
sont accessibles depuis le site 
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
En outre, quatre modules ont été développés pour ces enseignements :

* `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/>`_ : génère la documentation de ce module
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_ : code nécessaires aux TDs, aux projets informatiques, Big Data, PIG
* `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_ : installe facilement des modules
* `ensae_teaching_cs <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_ : ces enseignements compilés sous forme de modules

Il peuvent tous être installés avec l'instruction ::

    pip install <module>

Si des modules supplémentaires sont nécessaires, ils seront spécifiés sur la page
de chaque cours (voir :ref:`Getting Started 3A <l-td3a-start>`). La section :ref:`l-install` 
précise comment installer Python et les différentes options à disposition.



**Ouvrir un notebook**

L'ensemble des TDs a lieu sur les notebooks. Le plus simple pour écourter le plus possible
la mise en route est de suivre ces deux étapes :

1. Créer un répertoire vide pour vos notebooks désigné par ``<dirnb>``.
2. Ajouter un raccourci sur votre bureau qui contient la ligne suivante::

    set path=%path%;c:\Python34;c:\Python34\Scripts&ipython3 notebook --notebook-dir=<dirnb>
    
Il suffit ensuite de double cliquer sur ce lien pour ouvrir un notebook. Pour récupérer un notebook, il suffit
de le télécharger puis de le copier dans le répertoire ``<dirnb>`` ou de le glisser dans le navigateur.
Le seul raccourci à connaître est **SHIFT + ENTREE** qui lance l'exécution de la zone de code sélectionné.
L'article `Travailler avec IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_ décrit
d'autres paramètres par défaut.



Environnement de développement
------------------------------

* `Installation de modules sous Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_  (**modules sous Windows**)
* `Travailler avec IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_
* `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
* `Remote Notebook with Azure <http://www.xavierdupre.fr/blog/2014-11-09_nojs.html>`_
* `Trouver chaussure à ses stats <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/notebooks/td1a_cenonce_session_10.html#intro>`_
* :ref:`Python pour Data Scientist <l-data2a>`
* :ref:`l-ressources`
* :ref:`l-devtools`
* :ref:`modulesi`
* `(Très) Grand listing des libs tierce partie les plus utiles en Python <http://sametmax.com/tres-grand-listing-des-libs-tierce-partie-les-plus-utiles-en-python/>`_


.. _l-getting-started-main:
.. _l-install:


Getting started
---------------

.. index:: R, Julia, WinPython, Anaconda, pyminstall


La version recommandée est Python 3.4, 64 bit. Par défaut, les modules 
s'installe avec ``pip install <module>``. Le plus simple est d'utiliser la 
distribution `Anaconda <https://store.continuum.io/cshop/anaconda/>`_ :

* `Anaconda <http://continuum.io/downloads#py34>`_ (Windows, Linux, Mac). 
  Sous Linux ou Mac, la distribution n'interfère pas avec la distribution existante
  souvent différente. C'est un point très appréciable. Les modules de la distribution ne sont 
  pas tous à jour. Il faut penser à mettre à jour avec la commande ``conda install <module>``
  depuis le répertoire ``Anaconda3/Scripts`` (``conda install pandas`` par exemple).
  Pour suivre ces cours il faut ajouter :

    * `cvxopt <http://cvxopt.org/>`_ (`Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/#cvxopt>`_)
    * `goslate <http://pythonhosted.org/goslate/>`_
    * `dbfread <http://dbfread.readthedocs.org/en/latest/>`_
    * `rpy2 <http://rpy.sourceforge.net/>`_ (`Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2>`_)
    * `mpld3 <http://mpld3.github.io/>`_ (`Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_)
    * `folium <https://github.com/python-visualization/folium>`_
    * `graphviz <https://github.com/xflr6/graphviz>`_
    * `numexpr <https://github.com/pydata/numexpr>`_
    
   Il existe une version différente : `miniconda <http://conda.pydata.org/miniconda.html>`_.
   La liste des packages manquant sera probablement différente.
   Il suffit d'écrire sur la ligne de commande ``conda update --all`` 
   pour mettre à jour tous les modules.

    
Il faut également un éditeur de texte :

.. index:: éditeur, IDE

* `SciTe <http://www.scintilla.org/SciTE.html>`_, le plus simple et le plus léger,
  lire cet article pour le configurer
  `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_.
* `PyCharm <https://www.jetbrains.com/pycharm/>`_, c'est un environnement complet de développement,
  très pratique pour débugger, repérer des erreurs avant l'exécution (nom de variable inconnus...)
  
Pour les développeurs chevronnés, il faut un environnement plus complet :

.. toctree::

    getting_started

Table des matières
------------------

.. toctree::
    :maxdepth: 1

    td_1a
    td_2a
    td_3a
    blog/blogindex
    projet_info
    informations
    exemple_index
    exams
    coding_party
    README
    index_apropos
    glossary
    FAQ
    license
    indexmenu

Index
-----

* :ref:`l-notebooks`
* :ref:`l-modules`
* :ref:`l-classes`
* :ref:`l-functions`
* :ref:`l-changes`


.. image:: https://badge.fury.io/py/ensae_teaching_cs.svg
    :target: http://badge.fury.io/py/ensae_teaching_cs
      
.. image:: http://img.shields.io/pypi/dm/ensae_teaching_cs.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/ensae_teaching_cs  
    
