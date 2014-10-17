
:tocdepth: 4

ENSAE - Programmation - Xavier Dupré
====================================

Cette page donne accès au contenu des séances de travaux pratiques en programmation
que je dispense à l'`ENSAE <http://www.ensae.fr/>`_. Ils s'appuient principalement sur 
le langage Python. Le contenu est librement disponible sur `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_
et permet à quiconque de contribuer à ce cours disponible sous trois formats différents : 
`mobile/PC <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_,
`compact/blanc <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/index.html>`_,
`compact/noir <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_.
La page :ref:`l-README` résume l'historique des modifications.
    

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
nombreux exemples sur Internet.

Il faut bien entendu installer Python une première fois. Comme ce cours requiert de nombreux modules,
les étapes ont été simplifiées le plus possibles. Il faudra néanmoins y consacrer une bonne demi-heure :
:ref:`l-install`.


Contenu des enseignements
-------------------------

    * :ref:`ENSAE, 1A, Initiation à la programmation et l'algorithmie <l-td1a>`
    * :ref:`ENSAE, 2A, Données, Machine Learning et Programmation <l-td2a>`
    * :ref:`ENSAE, 3A, Eléments logiciels pour le traitement des données massives <l-td3a>`
    * :ref:`Exemples de toutes sortes <l-examplesindex>` dont :
        * :ref:`Exercices d'algorithmie <l-exoalgo>`
        * :ref:`Exposés divers non abordés en cours <l-extra>`
        * :ref:`Jeux autour des données <l-jdonnees>`
    * Autres documents
        * `Présentation ENSAE 1A - Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx/index.html>`_
        * `Présentation ENSAE 2A - Données et machine learning <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html>`_
        * :ref:`Articles, Références, Blog <l-biblio>`
        * :ref:`Modules <modulesi>`
        * :ref:`Outils, ressources pour développer <l-devtools>`
        * :ref:`Examens passés <l-examens>`
        * :ref:`Projets informatiques <l-projinfo>`
        * :ref:`Coding Party <l-codingparty>`
    * Projets informatiques
        * :ref:`projet informatique 1A <l-projinfo>`
        * :ref:`projet informatique 2A <l-projinfo2a>`
    * :ref:`Python pour Data Scientist <l-data2a>`
    * :ref:`l-ressources`
    
Et, j'ajoute parfois les questions qu'on me pose :

    * :ref:`FAQ <l-FAQs>`
    * :ref:`Glossaire <l-glossaire>`
    

    
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
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_ : code nécessaires aux TDs et aux projets informatiques
* `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_ : installe facilement des modules
* `ensae_teaching_cs <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_ : ces enseignements compilés sous forme de module


**Installation de Python**

Lors de l'installation, il faut faire attention à installer le langage
Python et ses modules en prenant soin d'utiliser la même version pour chaque composant.
Je recommande la version `64bit, v3.4.1 <https://www.python.org/downloads/release/python-341/>`_.
Le module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/>`_ propose une 
façon simple d'installer tous les modules nécessaires en faisant attention à la version choisie
à la première étape:


    1. Installer `python <https://www.python.org/>`_
    2. Ouvrir une ligne de commande et aller dans le répertoire ``<python>/Scripts``
    3. Ecrire ``pip install pymyinstall``
    4. Utiliser le code suivant pour installer les modules supplémentaires ::

        from pymyinstall import datascientist
        datascientist("install", full = False)

L'article `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
donne plus de détails et d'options. La liste complète des modules est celle de la fonction
`complete_installation <https://github.com/sdpython/pymyinstall/blob/master/src/pymyinstall/packaged/packaged_config.py>`_.
Pour tout module supplémentaire, vous pouvez lire 
`Three ways to install a module <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/notebooks/install_module.html>`_.


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


Quelques références
-------------------

    * `Programmation avec le langage Python <http://www.xavierdupre.fr/site2013/documents/python/initiation_via_python_ellipse_mai_2010.pdf>`_ (PDF, ou version `Ellipse <http://www.editions-ellipses.fr/product_info.php?products_id=6891>`_)
    * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_ (PDF)
    * `Exercices de programmation <http://www.xavierdupre.fr/blog/2014-03-22_nojs.html>`_
    * `Python avec la Khan Academy <http://www.xavierdupre.fr/blog/2013-11-29_nojs.html>`_
    * `Python Tutor <http://www.pythontutor.com/>`_
    * `version PDF de ce site <http://www.xavierdupre.fr/app/ensae_teaching_cs/latex/ensae_teaching_cs_doc.pdf>`_
    * `De l'idée au programme informatique <http://www.xavierdupre.fr/blog/2013-11-08_nojs.html>`_
    * `A gallery of interesting IPython Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_
    * `pyvideo.org <http://pyvideo.org/>`_
    
Python
------

    * `Questions Fréquentes <https://docs.python.org/3.4/faq/index.html>`_
    * `Modules standards <https://docs.python.org/3.4/library/>`_
    * :ref:`modulesi`
    * `Installation de modules sous Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_  (**modules sous Windows**)
    * `Python is Now the Most Popular Introductory Teaching Language at Top U.S. Universities <http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext>`_
    
Trucs et astuces en Python
--------------------------

    * `Vérification de types <http://www.xavierdupre.fr/blog/2014-08-20_nojs.html>`_
    * `Configurer IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_
    * `Test unitaires <http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-1/>`_, `partie 2 <http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-2/>`_

Environnement de développement
------------------------------

    * `Travailler avec IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_
    * `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
    * `Débugger en Python <http://www.xavierdupre.fr/blog/2014-06-02_nojs.html>`_
    * :ref:`l-devtools`
    * `Trouver chaussure à ses stats <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/notebooks/td1a_cenonce_session_10.html#intro>`_

Vieilles versions
-----------------

    * `année 2004-2011 <http://www.xavierdupre.fr/enseignement/td_python/python_td_simple/index.html>`_
    * `année 2011-2013 <http://www.xavierdupre.fr/enseignement/td_python/python_td_minute/index.html>`_
    * `année 2013-2014 <http://www.xavierdupre.fr/site2013/enseignements/index.html>`_



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
    filechanges
    README
    indexes
    