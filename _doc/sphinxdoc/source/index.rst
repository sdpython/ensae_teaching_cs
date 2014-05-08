

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
de départ. La correction est délivré également sous forme de notebook.

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
Je recommande la version `64bit, v3.3 <https://www.python.org/downloads/release/python-335/>`_.


Contenu des enseignements
-------------------------

    * :ref:`ENSAE, 1A, initiation à la programmation et l'algorithmie <l-td1a>`
    * :ref:`Exposé divers non abordés en cours <l-extra>`
    * :ref:`Exercices d'algorithmie <l-exoalgo>`

Quelques références
-------------------

    * `Programmation avec le langage Python <http://www.xavierdupre.fr/site2013/documents/python/initiation_via_python_ellipse_mai_2010.pdf>`_
    * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_
    * `Exercices de programmation <http://www.xavierdupre.fr/blog/2014-03-22_nojs.html>`_
    * `Python avec la Khan Academy <http://www.xavierdupre.fr/blog/2013-11-29_nojs.html>`_
    * `Python Tutor <http://www.pythontutor.com/>`_
    * `version PDF de ce site <http://www.xavierdupre.fr/app/ensae_teaching_cs/latex/ensae_teaching_cs_doc.pdf>`_
    
Python
------

    * `Questions Fréquentes <https://docs.python.org/3.4/faq/index.html>`_
    * `Modules standards <https://docs.python.org/3.4/library/>`_
    * `Installation de modules sous Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
    
Articles de blog
----------------

    * `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
    * `Travailler avec IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_
    * `Résoudre un sudoku avec Excel et VBA <http://www.xavierdupre.fr/blog/2014-02-08_nojs.html>`_
    * `Fusionner deux tableaux <http://www.xavierdupre.fr/blog/2013-11-21_nojs.html>`_
    * `De l'idée au programme informatique <http://www.xavierdupre.fr/blog/2013-11-08_nojs.html>`_
    * `Compter les pièces de monnaie pour obtenir un montant <http://www.xavierdupre.fr/blog/2013-11-09_nojs.html>`_
    * `Désactiver les logs de cvxopt <http://www.xavierdupre.fr/blog/2014-04-16_nojs.html>`_
    * `Machine Learning with Python <http://www.xavierdupre.fr/blog/2013-08-10_nojs.html>`_
    * `Quelques astuces pour accélérer un programme <http://www.xavierdupre.fr/blog/2014-04-12_nojs.html>`_
    * `Quelques précisions sur les projets informatiques (finance) <http://www.xavierdupre.fr/blog/2014-04-05_nojs.html>`_
    * `A small video on sorting algorithm <http://www.xavierdupre.fr/blog/2014-04-04_nojs.html>`_
    
Des petits details
------------------

    * `Why Lists Can't Be Dictionary Keys <https://wiki.python.org/moin/DictionaryKeys>`_
    * `Time Complexity <https://wiki.python.org/moin/TimeComplexity>`_
    * `List of data structures <http://en.wikipedia.org/wiki/List_of_data_structures>`_


.. toctree::
    :maxdepth: 1
    :hidden:

    td_1a
    expose_divers
    exercices
    examples
    all_example
    FAQ
    glossary
    filechanges
    README
    indexes
    