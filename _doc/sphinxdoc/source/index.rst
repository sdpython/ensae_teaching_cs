
:tocdepth: 4

ENSAE - Programmation - Xavier Dupré
====================================

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


Contenu des enseignements
-------------------------

* 3 niveaux
    * :ref:`ENSAE, 1A, Initiation à la programmation et l'algorithmie <l-td1a>`
    * :ref:`ENSAE, 2A, Données, Machine Learning et Programmation <l-td2a>`
    * :ref:`ENSAE, 3A, Eléments logiciels pour le traitement des données massives <l-td3a>`
* Présentations
    * `Présentation ENSAE 1A - Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx/index.html>`_
    * `Présentation ENSAE 2A - Données et machine learning <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html>`_
    * `Présentation ENSAE 3A - Map/Reduce <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_3A/index.html>`_
* Projets informatiques
    * :ref:`projet informatique 1A <l-projinfo>`
    * :ref:`projet informatique 2A <l-projinfo2a>`
    * :ref:`projet informatique 3A <l-projinfo3a>`
* :ref:`Exemples de toutes sortes <l-examplesindex>` dont :
    * :ref:`Exercices d'algorithmie <l-exoalgo>`
    * :ref:`Exposés divers non abordés en cours <l-extra>`
    * :ref:`Jeux autour des données <l-jdonnees>`
* Questions, termes, FAQ
    * :ref:`FAQ <l-FAQs>`
    * :ref:`Glossaire <l-glossaire>`
    * :ref:`questions`
    * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_ (PDF)
* Autres documents
    * :ref:`Articles, Références, Blog <l-biblio>`
    * :ref:`Modules <modulesi>`
    * :ref:`Outils, ressources pour développer <l-devtools>`
    * :ref:`Examens passés <l-examens>` (1A)
    * :ref:`Coding Party <l-codingparty>`
    

    
.. _l-install:

Prérequis et Installation
-------------------------

**Notebooks**

Les séances utilisent les `notebooks IPython <http://ipython.org/notebook.html>`_.
Au début de chaque séance, il vous suffit de télécharger le notebook qui sert de point
de départ. La correction est également rédigée sous forme de notebook.
Les prérequis sont bien sûr `Python <https://www.python.org/>`_ et
`IPython <http://ipython.org/>`_ mais aussi leurs dépendances
`pandas <http://fr.wikipedia.org/wiki/Panda>`_, 
`numpy <http://www.numpy.org/>`_, 
`openpyxl <http://pythonhosted.org/openpyxl/>`_. 
Sous Windows, ces modules
sont accessibles depuis le site 
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
En outre, quatre modules ont été développés pour ces enseignements :


* `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/>`_ : génère la documentation de ce module
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_ : code nécessaires aux TDs, aux projets informatiques, Big Data, PIG
* `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_ : installe facilement des modules
* `ensae_teaching_cs <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_ : ces enseignements compilés sous forme de modules

Si des modules supplémentaires sont nécessaires, ils seront spécifiés sur la page
de chaque cours : :ref:`l-td3a-start`.

**Installation de Python**

Lors de l'installation, il faut faire attention à installer le langage
Python et ses modules en prenant soin d'utiliser la même version pour chaque composant.
Je recommande la version `64bit, v3.4.1 <https://www.python.org/downloads/release/python-341/>`_.
La distribution `Anaconda <http://continuum.io/downloads#py34>`_ contient 
tous les modules importants pour les deux premières années. 
Le cours de troisième année utilise d'autres modules plus facilement installables
sous Windows via cette distribution.



**Ouvrir un notebooks**

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
* `Trouver chaussure à ses stats <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/notebooks/td1a_cenonce_session_10.html#intro>`_
* :ref:`Python pour Data Scientist <l-data2a>`
* :ref:`l-ressources`
* :ref:`l-devtools`
* :ref:`modulesi`



.. toctree::
    :hidden:

    td_1a
    td_2a
    td_3a
    data2a
    exemple_index
    exams
    projet_info
    coding_party
    manytools
    biblio
    ressources
    FAQ
    glossary
    questions/questions
    filechanges
    README
    indexes
    