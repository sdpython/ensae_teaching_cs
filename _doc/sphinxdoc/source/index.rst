
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
    

Avant-propos
------------

On programme nécessairement avec un **langage** de `programmation <http://fr.wikipedia.org/wiki/Langage_de_programmation>`_.
Ce langage a une grammaire et un vocabulaire. Il permet d'exprimer des idées sous la forme d'algorithmes.
Comme toute langue qu'on apprend, les premiers pas sont rebutants et on y prend peu de plaisir.
Mais cela devient plus facile avec une pratique régulière et le langage s'efface devant le problème à résoudre.
    


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
Je recommande la version `64bit, v3.4.1 <https://www.python.org/downloads/release/python-341/>`_.


Contenu des enseignements
-------------------------

    * :ref:`ENSAE, 1A, initiation à la programmation et l'algorithmie <l-td1a>`
    * :ref:`Exemples de toutes sortes <l-examplesindex>` dont :
    
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
    * `De l'idée au programme informatique <http://www.xavierdupre.fr/blog/2013-11-08_nojs.html>`_
    * `A gallery of interesting IPython Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_
    * `pyvideo.org <http://pyvideo.org/>`_
    
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
    * `Trouver chaussure à ses stats <file:///C:/xadupre/__home_/_data/GitHub/ensae_teaching_cs/dist/html/notebooks/td1a_cenonce_session_10.html#intro>`_

Vieilles versions
-----------------

    * `année 2004-2011 <http://www.xavierdupre.fr/enseignement/td_python/python_td_simple/index.html>`_
    * `année 2011-2013 <http://www.xavierdupre.fr/enseignement/td_python/python_td_minute/index.html>`_
    * `année 2013-2014 <http://www.xavierdupre.fr/site2013/enseignements/index.html>`_



.. toctree::
    :hidden:

    td_1a
    exemple_index
    exams
    projet_info
    coding_party
    manytools
    biblio
    FAQ
    glossary
    filechanges
    README
    indexes
    