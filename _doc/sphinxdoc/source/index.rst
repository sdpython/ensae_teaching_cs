

ENSAE - Programmation - Xavier Dupré
====================================

:ref:`l-README`, :ref:`blog <ap-main-0>`

Contenu des séances de travaux pratiques en programmation
que je dispense à l'`ENSAE <http://www.ensae.fr/>`_. 

Avant-propos
------------

Ces cours s'appuient principalement sur 
le langage `Python <https://www.python.org/>`_. 
Le contenu est librement disponible sur `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_
et permet à quiconque de contribuer à ce cours disponible sous trois formats différents : 
`mobile/PC <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_,
`compact/blanc <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/index.html>`_,
`compact/mobile/PC <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_.

On programme nécessairement avec un **langage** de 
`programmation <http://fr.wikipedia.org/wiki/Langage_de_programmation>`_.
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
* **3A :** calculs distribués, Map/Reduce, Hadoop, PIG, Spark, depuis un notebook

Le :ref:`blog <ap-main-0>` associé à ce site publie des liens vers des vidéos,
des données, met en valeur certaines mises à jour, aborde des sujets qui 
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
    * :ref:`FAQ <l-FAQs>` (Foire aux Questions ou Frequently Asked Questions)
    * :ref:`Glossaire <l-glossaire>`
    * :ref:`question`
    * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_ (PDF)
* Lectures
    * :ref:`Examens passés <l-examens>` (1A)
    * :ref:`l-data2a` ou sa version allégée avec les modules qu'il faut connaître :ref:`modulesi`
    * :ref:`Outils, ressources pour développer <l-devtools>`
    * :ref:`Articles, Références, Blog <l-information>`
    * :ref:`Coding Party <l-codingparty>`
    * :ref:`l-algoculture`
    * :ref:`blog <ap-main-0>` de ce cours
    * :ref:`code associé à ce cours <modindex>`
    * :ref:`l-ressources`
    * :ref:`l-biblio`

    

.. index: notebook, installation, prérequis

Notebooks
---------

Les séances utilisent les `notebooks IPython <http://ipython.org/notebook.html>`_.
Au début de chaque séance, il vous suffit de télécharger le notebook qui sert de point
de départ. La correction est également rédigée sous forme de notebook.
Les prérequis sont bien sûr `Python <https://www.python.org/>`_ et les modules qui l'ont rendu
populaire :
`IPython <http://ipython.org/>`_ mais aussi leurs dépendances
`pandas <http://fr.wikipedia.org/wiki/Panda>`_, 
`numpy <http://www.numpy.org/>`_, 
`matplotlib <http://matplotlib.org/>`_,
`scikit-learn <http://scikit-learn.org/stable/>`_.
Sous Windows, ces modules
sont accessibles depuis le site 
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
et ne peuvent pas être installés avec l'instruction ``pip install <module>`` car ils
nécessitent un compilateur C++.
Des modules développés pour ces enseignements viennent compléter cet ensemble :

* `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/>`_ : génère la documentation de ce module
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_ : code nécessaires aux TDs, aux projets informatiques, Big Data, PIG
* `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_ : installe facilement des modules
* `pyrsslocal <http://www.xavierdupre.fr/app/pyrsslocal/helpsphinx/>`_ : lecteur de flux RSS
* `ensae_teaching_cs <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_ : ces enseignements compilés sous forme de modules
* `actuariat_python <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html>`_ : contient d'autres notebooks
  et des exercices orientés un peu plus actuariat
* `code_beatrix <http://lesenfantscodaient.fr/>`_ : pour découvrir les algorithmes et `Scratch <https://scratch.mit.edu/>`_


.. _l-getting-started-main:
.. _l-install:


Getting started
---------------

En résumé :


**Windows**

Le plus simple est d'utiliser la distribution préparée pour ces enseignements
`ENSAE Python Setup <http://www.xavierdupre.fr/enseignement/>`_
et de la compléter si besoin. 
La page :ref:`l-data2a` décrit tous les modules qu'elle contient.
Les modules peuvent être mis à jour avec l'instruction ``Scripts/pymy_update`` qui vient 
avec l'installation du module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_.
Sinon, la distribution `Anaconda <http://continuum.io/downloads#py34>`_ est le choix le plus répandu.

Pour l'ajout d'un module ponctuel, si l'instruction ``pip install <module>`` ne fonctionne pas,
c'est vraisemblablement parce que ce module contient une partie en C++. 
Dans ce cas, il faut aller voir sur ce site `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
s'il est disponible. S'il ne l'est pas, l'installation du module est réservée aux experts.

**Linux / Mac**

La distribution `Anaconda <https://www.continuum.io/downloads>`_ (python 3.4, 64 bit)
est la plus répandue.


**Environnement de travail**

.. index:: éditeur, IDE, rodeo, spyder, pycharm, r, r studio, scite

* `SciTe <http://www.scintilla.org/SciTE.html>`_, le plus simple et le plus léger,
  lire cet article pour le configurer
  `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_.
* `PyCharm <https://www.jetbrains.com/pycharm/>`_, c'est un environnement complet de développement,
  très pratique pour débugger, repérer des erreurs avant l'exécution (nom de variable inconnus...)
* `Spyder <https://pythonhosted.org/spyder/>`_, ressemble beaucoup à `R Studio <http://www.rstudio.com/>`_
* `Rodeo <http://blog.yhathq.com/posts/introducing-rodeo.html>`_, une sorte de Spyder très épuré
* `Visual Studio Community <https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx>`_
  
Pour les développeurs chevronnés, il faut un environnement plus complet :

.. toctree::
    :maxdepth: 1

    getting_started
    

Contenu
-------

.. toctree::
    :maxdepth: 1

    td_1a
    td_2a
    td_3a
    blog/main_0000
    projet_info
    informations
    biblio
    exemple_index
    all_notebooks
    exams
    coding_party
    glossary
    FAQ
    Notebooks, Exemples, Code <indexmenu>
    genindex




+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`     |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`   | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`modindex`      |  :ref:`l-example`   | :ref:`search`       | :ref:`l-license`   | :ref:`l-changes`       | :ref:`l-README`                                |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`genindex`      |  :ref:`l-FAQs`      | :ref:`l-notebooks`  |                    | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+




.. image:: https://travis-ci.org/sdpython/ensae_teaching_cs.svg?branch=master
    :target: https://travis-ci.org/sdpython/ensae_teaching_cs
    :alt: Build status
    
.. image:: https://badge.fury.io/py/ensae_teaching_cs.svg
    :target: http://badge.fury.io/py/ensae_teaching_cs
      
.. image:: http://img.shields.io/pypi/dm/ensae_teaching_cs.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/ensae_teaching_cs  
    
.. image:: http://img.shields.io/github/issues/sdpython/ensae_teaching_cs.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/ensae_teaching_cs/issues
    
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT