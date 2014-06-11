
:tocdepth: 4

ENSAE - Programmation - Xavier Dupré
====================================

Cette page donne accès au contenu des séances de travaux pratiques en programmation
que je dispense à l'`ENSAE <http://www.ensae.fr/>`_. Ils s'appuient sur 
le langage Python.

    * `documentation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_
    * `Windows Setup <http://www.xavierdupre.fr/site2013/index_code.html#ensae_teaching_cs>`_
    * :ref:`l-README`
    
Pour contribuer, il suffit d'utiliser GitHub qui héberge les sources de ce document :

    * `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_


Prérequis
---------

Les séances utilisent les `notebooks IPython <http://ipython.org/notebook.html>`_.
Au début de chaque séance, il vous suffit de télécharger le notebook qui sert de point
de départ. La correction est également rédigée sous forme de notebook.

Les prérequis sont bien sûr `Python <https://www.python.org/>`_ et
`IPython <http://ipython.org/>`_ mais 
les modules `pandas <http://fr.wikipedia.org/wiki/Panda>`_, 
`numpy <http://www.numpy.org/>`_, 
`openpyxl <http://pythonhosted.org/openpyxl/>`_. Sous Windows, ces modules
sont accessibles depuis le site 
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
Les étapes nécessaires à l'installation sont décrites ici :
`Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_.
A ces modules, il faut ajouter deux autres conçus pour ces enseignements : 
`pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/>`_,
`pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_.

Lors de l'installation, il faut faire attention à installer le langage
Python et ses modules en prenant soin d'utiliser la même version pour chaque composant.
Je recommande la version `64bit, v3.3.5 <https://www.python.org/downloads/release/python-335/>`_.
La version `64bit, v3.4.1 <https://www.python.org/downloads/release/python-341/>`_ a encore quelques bugs.


Contenu des enseignements
-------------------------

    * :ref:`ENSAE, 1A, initiation à la programmation et l'algorithmie <l-td1a>`
    * :ref:`Quelques exemples très courts <l-example-main>`
    * :ref:`Quelques problématiques récurrentes <l-elcode>`
    * :ref:`Exercices d'algorithmie <l-exoalgo>`
    * :ref:`Exposés divers non abordés en cours <l-extra>`

Quelques références
-------------------

    * `Programmation avec le langage Python <http://www.xavierdupre.fr/site2013/documents/python/initiation_via_python_ellipse_mai_2010.pdf>`_ (PDF, ou version `Ellipse <http://www.editions-ellipses.fr/product_info.php?products_id=6891>`_)
    * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_ (PDF)
    * `Exercices de programmation <http://www.xavierdupre.fr/blog/2014-03-22_nojs.html>`_
    * `Python avec la Khan Academy <http://www.xavierdupre.fr/blog/2013-11-29_nojs.html>`_
    * `Python Tutor <http://www.pythontutor.com/>`_
    * `version PDF de ce site <http://www.xavierdupre.fr/app/ensae_teaching_cs/latex/ensae_teaching_cs_doc.pdf>`_ (PDF)
    
Python
------

    * `Questions Fréquentes <https://docs.python.org/3.4/faq/index.html>`_
    * `Modules standards <https://docs.python.org/3.4/library/>`_
    * :ref:`modulesi`
    * `Installation de modules sous Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_  (**modules sous Windows**)
    
Environnement de développement
------------------------------

    * `Travailler avec IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_
    * `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
    * `Débugger en Python <http://www.xavierdupre.fr/blog/2014-06-02_nojs.html>`_
    * :ref:`l-devtools`

Articles de blog
----------------

    * `Résoudre un sudoku avec Excel et VBA <http://www.xavierdupre.fr/blog/2014-02-08_nojs.html>`_
    * `Fusionner deux tableaux <http://www.xavierdupre.fr/blog/2013-11-21_nojs.html>`_
    * `De l'idée au programme informatique <http://www.xavierdupre.fr/blog/2013-11-08_nojs.html>`_
    * `Compter les pièces de monnaie pour obtenir un montant <http://www.xavierdupre.fr/blog/2013-11-09_nojs.html>`_
    * `Désactiver les logs de cvxopt <http://www.xavierdupre.fr/blog/2014-04-16_nojs.html>`_
    * `Machine Learning with Python <http://www.xavierdupre.fr/blog/2013-08-10_nojs.html>`_
    * `Quelques astuces pour accélérer un programme <http://www.xavierdupre.fr/blog/2014-04-12_nojs.html>`_
    * `Quelques précisions sur les projets informatiques (finance) <http://www.xavierdupre.fr/blog/2014-04-05_nojs.html>`_
    * `A small video on sorting algorithm <http://www.xavierdupre.fr/blog/2014-04-04_nojs.html>`_
    
   
Python dans le détail
---------------------

    * `La boîte à outils Python 2014 <http://www.hautefeuille.eu/python-tools-2014.html>`_
    * `Les recettes Python de Tyrtamos <http://python.jpvweb.com/mesrecettespython/doku.php?id=Sommaire>`_
    * `Why Lists Can't Be Dictionary Keys <https://wiki.python.org/moin/DictionaryKeys>`_
    * `Time Complexity <https://wiki.python.org/moin/TimeComplexity>`_
    * `List of data structures <http://en.wikipedia.org/wiki/List_of_data_structures>`_
    * `Advanced Data Structures in Python <http://pypix.com/python/advanced-data-structures-python/>`_
    * `Useful Python Functions and Features You Need to Know <http://pypix.com/tools-and-tips/python-functions/?utm_content=buffer2e408&utm_source=buffer&utm_medium=twitter&utm_campaign=Buffer>`_
    * `Essential SQLAlchemy Tips and Techniques <http://pypix.com/tools-and-tips/essential-sqlalchemy/>`_
    * `Parallélisation des traitements en Python <http://www.hautefeuille.eu/python-parallelism-multiprocessing.html>`_
    * `Why Python is Slow: Looking Under the Hood <http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/>`_


.. toctree::
    :hidden:

    td_1a
    examples
    element_code
    exercices
    expose_divers
    projet_info
    coding_party
    manytools
    FAQ
    glossary
    filechanges
    README
    indexes
    