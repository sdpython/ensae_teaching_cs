

ENSAE - Programmation - Xavier Dupré
====================================

Contenu des séances de travaux pratiques en programmation
que je dispense à l'`ENSAE <http://www.ensae.fr/>`_. 
Ces cours s'appuient principalement sur 
le langage `Python <https://www.python.org/>`_. 
Le contenu est librement disponible sur `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_
et permet à quiconque de contribuer à ce cours. 
Il existe trois formats disponibles :
`mobile/PC <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_,
`blanc <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/index.html>`_,
`bleu <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_.
Les changements importants sont notés sur le :ref:`blog <ap-main-0>` 
associé à ce cours.



Avant-propos
------------

Les langages `R <https://www.r-project.org/>`_ et 
`Python <https://www.python.org/>`_ sont devenus 
incontournables dans le domaine des statistiques.
Ils sont simples, open source, s'apprennent rapidement, sont utilisés
par beaucoup et dispose de nombreuses pages, blogs, listes
de diffusions qui leur sont dédiées.
`R <https://www.r-project.org/>`_ est le terrain de jeu préféré des chercheurs
mais il est peu pratique pour développer un site web ou un jeu.
`Python <https://www.python.org/>`_ est beaucoup plus polyvalent
et de plus en plus populaire. Il est enseigné à l'ENSAE depuis 2004.
Les premiers pas sont parfois rebutants mais on arrive vite à 
quelque chose à condition d'y passer un peu de temps au démarrage.
Passer les premiers jeux (voir `lesenfantscodaient.fr <http://lesenfantscodaient.fr/>`_),
la programmation se révèle assez pratique pour traiter les données,
les visualiser, automatiser les tâches les plus répétitives, et
s'amuser.




**3 niveaux**

Les cours proposés sont de difficultés croissantes et orientés pour un statisticien ou data scientist.
La pratique est un élément essentiel de l'apprentissage de la programmation.
Quoi qu'on en dise, il faut aussi être créatif.


* **1A :** syntaxe de langage, premiers algorithmes, programmation dynamique, Data Frame, premiers graphes
* **2A :** python pour un statisticien, Data Frames, calcul matriciel, machine learning, 
  exercices d'algorithmie
* **3A :** calculs distribués, Map/Reduce, Hadoop, PIG, Spark, depuis un notebook

Le :ref:`blog <ap-main-0>` associé à ce site publie des liens vers des vidéos,
des données, met en valeur certaines mises à jour, aborde des sujets connexes
aux enseignements proposés.

Chaque cours est validé par un projet et c'est principalement durant cet exercice
qu'on apprend et qu'on exprime ses idées. Dire qu'on sait programmer simplement
parce qu'on a réussi les exercices du cours serait un peu comme prétendre
savoir jouer aux échecs après avoir pris connaissance des règles et sans avoir jamais
joué une partie.



Contenu des enseignements
-------------------------


+--------+---------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Niveau | **Contenu**   | Projet                                       | Présentation - Mise en perspective                                                                                                |
+--------+---------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| 1A     | :ref:`l-td1a` | :ref:`projet informatique 1A <l-projinfo1a>` | `Présentation ENSAE 1A - Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx/index.html>`_                  |
+--------+---------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| 2A     | :ref:`l-td2a` | :ref:`projet informatique 2A <l-projinfo2a>` | `Présentation ENSAE 2A - Données et machine learning <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html>`_ |
+--------+---------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| 3A     | :ref:`l-td3a` | :ref:`projet informatique 3A <l-projinfo3a>` | `Présentation ENSAE 3A - Map/Reduce <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_3A/index.html>`_                  |
+--------+---------------+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

Autres liens, exercices, algorithmes, jeux de données, démonstrations...

* Questions, termes, FAQ
    * :ref:`FAQ <l-FAQs>` (Foire aux Questions ou Frequently Asked Questions)
    * :ref:`Glossaire <l-glossaire>`
    * :ref:`question`
    * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_ (PDF)
* :ref:`Exemples de toutes sortes <l-examplesindex>` dont :
    * :ref:`Exercices d'algorithmie <l-exoalgo>`
    * :ref:`Exposés divers non abordés en cours <l-extra>`
    * :ref:`l-expose-explication`
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
    * :ref:`l-visualisation`

    




Getting started
---------------

.. index: notebook, installation, prérequis

Notebooks
^^^^^^^^^

Les séances utilisent les `notebooks Jupyter <http://jupyter.org/>`_.
Ils sont de plus en plus fréquent lors des conférences scientifiques et offre
un espace de travail réactif, agréable et très pratique quant il s'agit de 
partager son travail.
Chaque séance mélanage notions et exerices qu'on peut faire directement dans le notebook 
une fois téléchargé. La correction est également rédigée sous forme de notebook afin de
pouvoir aisément *jouer* avec la solution.


.. _l-getting-started-main:
.. _l-install:


Démarrage
^^^^^^^^^



**Windows**

Le plus simple est d'utiliser la distribution préparée pour ces enseignements
`ENSAE Python Setup <http://www.xavierdupre.fr/enseignement/>`_
et de la compléter si besoin. Elle inclut également le langage `R <https://www.r-project.org/>`_.
La page :ref:`l-data2a` décrit tous les modules qu'elle contient.
Les modules peuvent être mis à jour avec l'instruction ``Scripts/pymy_update`` qui vient 
avec l'installation du module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_.
Sinon, la distribution `Anaconda <http://continuum.io/downloads#py34>`_ est le choix le plus répandu.

Pour l'ajout d'un module ponctuel, si l'instruction ``pip install <module>`` ne fonctionne pas,
c'est vraisemblablement parce que ce module contient une partie en C++. 
Dans ce cas, il faut aller voir sur ce site `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
s'il est disponible. S'il ne l'est pas, l'installation du module est réservée aux experts.

**Linux / Mac**

La distribution `Anaconda <https://www.continuum.io/downloads>`_ (python 3.5, 64 bit)
est la plus répandue. Voir également
`Install Anaconda through SSH connection <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/main_0001.html#hblog-2015-11-01-install-anaconda-through-ssh-connection>`_.


**Environnement de travail**

.. index:: éditeur, IDE, rodeo, spyder, pycharm, R, R studio, scite

* `SciTe <http://www.scintilla.org/SciTE.html>`_, le plus simple et le plus léger,
  lire cet article pour le configurer
  `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_.
* `PyCharm <https://www.jetbrains.com/pycharm/>`_, c'est un environnement complet de développement,
  très pratique pour débugger, repérer des erreurs avant l'exécution (nom de variable inconnus...)
* `Spyder <https://pythonhosted.org/spyder/>`_, ressemble beaucoup à `R Studio <http://www.rstudio.com/>`_
* `Rodeo <http://blog.yhathq.com/posts/introducing-rodeo.html>`_, une sorte de Spyder très épuré
* `Visual Studio Community <https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx>`_
* `Pyzo <http://www.pyzo.org/>`_ : ressemble à Matlab


Librairies clé
^^^^^^^^^^^^^^

Le langage est devenu populaire aussi parmi les data scientists grâce à un ensemble 
de librairies qui ont offert un service équivalent à ce que propose `R <https://www.r-project.org/>`_,
`pandas <http://fr.wikipedia.org/wiki/Panda>`_, 
`numpy <http://www.numpy.org/>`_, 
`matplotlib <http://matplotlib.org/>`_,
`scikit-learn <http://scikit-learn.org/stable/>`_ 
et qu'il a su réinventer la façon de travailler avec les 
notebooks et `Jupyter <http://jupyter.org/>`_.
Sous Windows, ces modules
sont accessibles depuis le site 
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
et ne peuvent pas être installés avec l'instruction ``pip install <module>`` car ils
nécessitent un compilateur C++.


  
Développeurs chevronnés
^^^^^^^^^^^^^^^^^^^^^^^

:ref:`l-getting_started_full`
    

Autres extensions
^^^^^^^^^^^^^^^^^

Ces cours représentent plus de 60 heures de cours et travaux pratiques suivis
par plus de 200 élèves de l'ENSAE répartis sur trois années, la réception d'une centaine
de projets. Cela nécessite un peu d'automatisation implémentée en Python
car il est facile de créer et de partager ses propres librairies.
`pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/>`_  automatise la création de ce site web,
`pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_ offre des fonctions développées pour les 
travaux pratiques et aux projets informatiques. 
`pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_ facilite la mise à jour des modules
et la création d'un setup dédié. 
`pyrsslocal <http://www.xavierdupre.fr/app/pyrsslocal/helpsphinx/>`_ est un lecteur très léger de flux RSS pour s'abonner
aux blogs du cours.
`ensae_teaching_cs <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_ contient ces enseignements 
compilés aussi sous forme de module. 
`ensae_projects <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/index.html>`_ fut démarré à l'occasion d'un hackathon
et cherche encore son chemin. 
`actuariat_python <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html>`_ contient d'autres notebooks
proposés dans la formation `Data Science <http://www.institutdesactuaires.com/gene/main.php?base=943>`_ à la 
maison des actuaires.
Et `code_beatrix <http://lesenfantscodaient.fr/>`_ pour découvrir les algorithmes et la programmation.




Table des matières
------------------

**Contenu**

.. toctree::
    :maxdepth: 1
    :numbered: 1
    
    1. Algorithmes et programmation <td_1a>
    2. Python pour un Data Scientist <td_2a>
    3. Eléments logiciels pour le traitement des données massives <td_3a>
    4. blog site <blog/main_0000>
    5. Projets informatiques <projet_info>
    6. Examens <exams>
    7. Modules, Bibliographie, Articles... <informations>
    
**Index**
    
.. toctree::
    :maxdepth: 1

    visualisation
    getting_started
    exemple_index
    all_notebooks
    coding_party
    Notebooks, Exemples, Code <indexmenu>
    genindex




+----------------------+---------------------+---------------------+--------------------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`     |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`               | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+----------------------+---------------------+---------------------+--------------------------------+------------------------+------------------------------------------------+
| :ref:`modindex`      |  :ref:`l-example`   | :ref:`search`       | :ref:`l-license`               | :ref:`l-changes`       | :ref:`l-README`                                |
+----------------------+---------------------+---------------------+--------------------------------+------------------------+------------------------------------------------+
| :ref:`genindex`      |  :ref:`l-FAQs`      | :ref:`l-notebooks`  | :ref:`l-getting_started_full`  | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+----------------------+---------------------+---------------------+--------------------------------+------------------------+------------------------------------------------+




.. image:: https://travis-ci.org/sdpython/ensae_teaching_cs.svg?branch=master
    :target: https://travis-ci.org/sdpython/ensae_teaching_cs
    :alt: Build status
    
.. image:: https://ci.appveyor.com/api/projects/status/4chpamq95rh5h245?svg=true
    :target: https://ci.appveyor.com/project/sdpython/ensae-teaching-cs
    :alt: Build Status Windows    
    
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
    
.. image:: https://codecov.io/github/sdpython/ensae_teaching_cs/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/ensae_teaching_cs?branch=master
    