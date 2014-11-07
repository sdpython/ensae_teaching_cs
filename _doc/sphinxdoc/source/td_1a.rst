
.. _l-td1a:


1A
==

`Algorithmes et programmation - OMI1C4 <http://www.ensae.fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/1re-anne-formationsdiplome-94.html?id=100115>`_

Ce cours s'étale sur 12 séances de travaux dirigés (TD) d'une durée de 2h. Le cours est décrit plus 
en détail dans cette présentation : `ENSAE 1A - Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx/index.html>`_.
Les six premières séances font découvrir le langage Python. 

- :ref:`TD 1 : Premiers pas en Python <td1acenoncesession1rst>`  (:ref:`correction <td1acorrectionsession1rst>`)
- :ref:`TD 2 : Variables, boucles, corrections <td1acenoncesession2rst>`  (:ref:`correction <td1acorrectionsession2rst>`)
- :ref:`TD 3 : Dictionnaires, fonctions <td1acenoncesession3rst>`  (:ref:`correction <td1acorrectionsession3rst>`)
- :ref:`TD 4 : Fichiers, modules, expressions régulières <td1acenoncesession4rst>`  (:ref:`correction <td1acorrectionsession4rst>`)
- :ref:`TD 5 : Classes et carrés magiques <td1acenoncesession5rst>`  (:ref:`correction <td1acorrectionsession5rst>`)
- :ref:`TD 6 : Classes et héritage <td1acenoncesession6rst>`  (:ref:`correction <td1acorrectionsession6rst>`)

Les six séances [#f1]_ suivantes sont centrées autour de l'utilisation de la programmation
pour un usage scientifique. 
Trois séances sont centrées sur trois algorithmes.
Lorsqu'un problème paraît compliqué ou qu'un algorithme est trop long, 
il y a deux questions qu'on doit se poser en premier pour entrevoir une solution. 

1. Peut-on réécrire le problème par **récurrence** ? On aboutit le plus souvent à une solution issue de la programmation dynamique. Le coût est **quadratique**.
2. Peut-on **couper le problème en deux**, construire une solution sur chaque moitié puis recoller les solutions ? On procède de cette façon par dichotomie. Le coût est **logarithmique**.

Ces deux façons de faire sont présentées durant les trois séances.

- :ref:`TD 7 : Programmation dynamique <td1acenoncesession7rst>`  (:ref:`correction <td1acorrectionsession7rst>`)
- :ref:`TD 8 : Arbre et Trie <td1acenoncesession8rst>`  (:ref:`correction <td1acorrectionsession8rst>`)
- :ref:`TD 9 : Optimisation sous contrainte <td1acenoncesession9rst>`  (:ref:`correction <td1acorrectionsession9rst>`) (relecture conseillée à ceux qui souhaite optimiser des portefeuilles d'actions) [#f1]_

Trois séances sont centrées sur les outils indispensables pour manipuler facilement les données et faire des calculs.
Ces outils sont similaires à ceux qu'on trouve dans de nombreux languages à usage scientifique
(`R <http://www.r-project.org/>`_, `SciLab <http://www.scilab.org/fr>`_, 
`Julia <http://julialang.org/>`_, `Octave <http://www.gnu.org/software/octave/>`_, ...).
Ces trois séances peuvent paraître plus longues car elles s'appuient sur des modules qu'il faut découvrir 
puis utiliser pour résoudre des exercices. Toutefois, les modules 
`numpy <http://www.numpy.org/>`_, `pandas <http://pandas.pydata.org/>`_, `matplotlib <http://matplotlib.org/>`_
sont incontournables pour manipuler les données en Python.

- :ref:`TD 10 : DataFrame et Matrice <td1acenoncesession10rst>`  (:ref:`correction <td1acorrectionsession10rst>`) [#f1]_ 
- :ref:`TD 11 : Calcul numérique, dichotomie et Cython <td1acenoncesession11rst>`  (:ref:`correction <td1acorrectionsession11rst>`) [#f1]_ 
- :ref:`TD 12 : Visualisation des données <td1acenoncesession12rst>`  (:ref:`correction <td1acorrectionsession12rst>`) 

La dernière séance est une séance notée. Tous les documents sont autorisés. Quelques questions 
peuvent requérir l'utilisation des outils présentées durant les séances 9 à 12. Toutefois,
si tel était le cas, ce serait très proche d'une solution proposée lors des TD.

.. _l-td1a-biblio:

Bibliographie
-------------

**Liens**

* `A gallery of interesting IPython Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_
* `Data Science in Python <http://blog.yhathq.com/posts/data-science-in-python-tutorial.html>`_
* `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_

**Livres**

* `Apprentissage de la programmation <http://inforef.be/swi/python.htm>`_, Gérald Swinnen
* `Précis de recherche opérationnelle <http://www.eyrolles.com/Informatique/Livre/precis-de-recherche-operationnelle-9782100706129>`_, Robert Faure, Bernard Lemaire, Christophe Picouleau
* `Problem Solving with Algorithms and Data Structures <https://www.cs.auckland.ac.nz/courses/compsci107s1c/resources/ProblemSolvingwithAlgorithmsandDataStructures.pdf>`_, Brad Miller, David Ranum (version `html <http://interactivepython.org/courselib/static/pythonds/index.html>`_)


.. toctree::
    :hidden:
    
    td_1a_enonce
    td_1a_correction
    questions/question_2014
    
.. rubric:: Footnotes

.. [#f1] Les quatre sujets importants des six dernières séances sont la programmation dynamique, la dichotomie, les dataframe, les graphiques. La séance 9, la fin de la séance 10 et la séance 11 ne sont pas indispensables. 
    