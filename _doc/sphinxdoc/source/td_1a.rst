


.. _l-td1a:



Algorithmes et programmation
============================

.. index:: 1A

`ENSAE - OMI1C4 <http://www.ensae.fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/1re-anne-formationsdiplome-94.html?id=100115>`_,
`ENSAE - OMI1C9 <http://www.ensae.fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/1re-anne-formationsdiplome-94.html?id=100332>`_

Cours animé par :

* Xavier Dupré

Intervenants 2015-2016 :

* Xavier Dupré, `Microsoft France <https://www.microsoft.com/fr-fr/>`_
* Emmanuel Guérin, `TalendSoft <http://www.talentsoft.com/>`_
* Arthur Renaud, `Etaonis <http://www.etaonis.fr/>`_
* Mehdi Seddar, `Artfact <http://www.artefact.is/>`_
* Yves Gerey, `A2iA <http://www.a2ia.com/en>`_
* Marc-Antoine Weisser, `Supélec <http://www.supelec.fr/>`_
* Charles de Ravel d'Esclapon, `Etaonis <http://www.etaonis.fr/>`_
* Félix Revert, `CapGemini Consulting <https://www.capgemini-consulting.com/>`_



TD - les bases
--------------

Ce cours s'étale sur 12 séances de travaux dirigés (TD) d'une durée de 2h. Le cours est décrit plus 
en détail dans cette présentation : `ENSAE 1A - Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx/index.html>`_.
Les six premières séances font découvrir le langage Python. 

- :ref:`TD 1 : Premiers pas en Python <td1acenoncesession1rst>`  (:ref:`correction <td1acorrectionsession1rst>`)
- :ref:`TD 2 : Variables, boucles, corrections <td1acenoncesession2rst>`  (:ref:`correction <td1acorrectionsession2rst>`)
- :ref:`TD 3 : Dictionnaires, fonctions <td1acenoncesession3rst>`  (:ref:`correction <td1acorrectionsession3rst>`)
- :ref:`TD 4 : Fichiers, modules, expressions régulières <td1acenoncesession4rst>`  (:ref:`correction <td1acorrectionsession4rst>`)
- :ref:`TD 5 : Classes et carrés magiques <td1acenoncesession5rst>`  (:ref:`correction <td1acorrectionsession5rst>`)
- :ref:`TD 6 : Classes et héritage <td1acenoncesession6rst>`  (:ref:`correction <td1acorrectionsession6rst>`)

Sessions alternatives :

- :ref:`TD 3-4 : Tests unitaires, suivi de source, profiling, design <l-production>` (2016)
- :ref:`TD 4-5 : distance de Jaccard <td1acenoncesession45jaccardrst>` (:ref:`correction <td1acorrectionsession45jaccardrst>`) (2016)

Au terme de ces six séances, si la programmation est nouvelle pour vous ou
si le langage vous paraît encore peu naturel, je vous encourage à faire d':ref:`autres exercices <l-examplesindex>`,
à piocher dans les anciens :ref:`l-examens`, à regarder la liste des exercices
proposées à `Quelques exercices du Project Euler <http://mathprepa.fr/python-project-euler-mpsi/>`_.
La plupart de ces notions font déjà partie du programme des classes préparatoires
scientifiques.



TD - algorithmes
----------------

Les six séances [#f1]_ suivantes sont centrées autour de l'utilisation de la programmation
pour un usage scientifique. 
Trois séances sont centrées sur trois algorithmes.
Lorsqu'un problème paraît compliqué ou qu'un algorithme est trop long, 
il y a deux questions qu'on doit se poser en premier pour entrevoir une solution. 

#. Peut-on réécrire le problème par **récurrence** ? 
   On aboutit le plus souvent à une solution issue de la programmation dynamique. 
   Le coût est **quadratique**.
#. Peut-on **couper le problème en deux**, construire une solution sur 
   chaque moitié puis recoller les solutions ? On procède de cette façon par dichotomie. 
   Le coût est **logarithmique**.

Ces deux façons de faire sont présentées durant les trois séances.

- :ref:`TD 7 : Programmation dynamique <td1acenoncesession7rst>`  (:ref:`correction <td1acorrectionsession7rst>`)
- :ref:`TD 8 : Arbre et Trie <td1acenoncesession8rst>`  (:ref:`correction <td1acorrectionsession8rst>`)
- :ref:`TD 9 : Optimisation sous contrainte <td1acenoncesession9rst>`  (:ref:`correction <td1acorrectionsession9rst>`) 
  (relecture conseillée à ceux qui souhaitent optimiser des portefeuilles d'actions) [#f1]_

Sessions alternatives :

- :ref:`TD 7 : distance d'édition <td1acenoncesession7editionrst>` (:ref:`correction <td1acorrectionsession7editionrst>`),
  cette séance fait écho à la distance de Jaccard évoquée par :ref:`TD 4-5 : distance de Jaccard <td1acenoncesession45jaccardrst>`
- :ref:`TD 8 : Parcours dans un graphe <td1acenoncesession8wikirootrst>` (:ref:`correction <td1acorrectionsession8wikirootrst>`)  


TD - librairies numériques
--------------------------

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
- alternative `TD 12 : graphes <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_enonce.html#seance6graphesenoncerst>`_
  (`correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_correction.html#seance6graphescorrectionrst>`_)

La dernière séance est une séance notée. Tous les documents sont autorisés. Quelques questions 
peuvent requérir l'utilisation des outils présentées durant les séances 9 à 12. Toutefois,
si tel était le cas, ce serait très proche d'une solution proposée lors des TD.


Exercices supplémentaires
-------------------------

* `décomposition mosaïque d'une image <http://www.xavierdupre.fr/site2013/enseignements/tddata/am_td_11_image.pdf>`_ (Arnaud de Myttenaere)
* :ref:`l-exampleNgatifs`
* :ref:`l-exampleTD1A`
* :ref:`l-exampleConstructionsClassiques`
* :ref:`ppexodevinerunnombrerst`, :ref:`correction <ppexodevinerunnombrecorrectionrst>`
* :ref:`codelistetuplerst`
* :ref:`codemultinomialrst`


Algorithmes classiques
----------------------

Ces exercices sont proches de ceux qu'on peut poser en entretien d'embauche. Le plus souvent,
il existe une façon naïve d'arriver au résultat et il existe un algorithme plus rapide. 
Tout est question de coût d'algorithme. Il y a deux grandes astuces pour aller plus vite :

    * la programmation dynamique, son coût est en :math:`O(n^2)`,
    * la dichotomie, son coût est en :math:`O(\ln_2 n)`.
    
Le tout est d'exprimer la solution en faisant apparaître l'un ou l'autre ou une combinaison des deux pour les problèmes 
les plus complexes.
La programmation dynamique apparaît souvent quand on considère la solution sous forme récurrente.
La dichotomie consiste à résoudre à couper l'ensemble de départ en deux, à résoudre le problème pour les deux sous-ensembles, 
puis à fusionner les deux solutions.

    
.. toctree::
    :numbered:

    notebooks/exercice_xn
    notebooks/exercice_echelle
    notebooks/exercice_morse
    notebooks/exercice_lcs
    notebooks/exercice_plus_grande_somme
    
Petites Fiches
--------------

.. toctree::

    1a/graphes
    1a/siteflask
    1a/unittest_coverage_git_profling
    

Trucs et astuces avec les notebooks
-----------------------------------

    
.. toctree::
    :numbered:

    notebooks/notebook_convert
    notebooks/jupyter_custom_magics

.. _l-td1a-start:

Getting started
---------------

Il faut vous reporter à la section :ref:`l-installation-courte` pour installer python.        
Certaines séances pratiques utilisent des données depuis ce site. 
Elles sont facilement téléchargeables avec ces deux modules :

* `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_



.. _l-td1a-biblio:

Bibliographie
-------------

**Cheat Sheet**

* `Aide Mémoire Python <http://www.le-memento.fr/python.html>`_
* `Syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_

**Liens**

* `Message de service aux débutants en Python <http://sametmax.com/message-de-service-aux-debutants-en-python/>`_
* `Cours et tutos <http://sametmax.com/cours-et-tutos/>`_ 
* `Les trucmuchables en Python <http://sametmax.com/les-trucmuchables-en-python/>`_ (iterable, mutable, immutable, ...)
* `A gallery of interesting IPython Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_
* `Data Science in Python <http://blog.yhathq.com/posts/data-science-in-python-tutorial.html>`_
* `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
* `Exercices de programmation <http://www.xavierdupre.fr/blog/2014-03-22_nojs.html>`_
* `De l'idée au programme informatique <http://www.xavierdupre.fr/blog/2013-11-08_nojs.html>`_
* `Questions Fréquentes <https://docs.python.org/3.4/faq/index.html>`_
* :ref:`l-FAQ`
* :ref:`l-glossary`
* :ref:`l-questions`
* `Débugger en Python <http://www.xavierdupre.fr/blog/2014-06-02_nojs.html>`_
* `Modules standards <https://docs.python.org/3.4/library/>`_
* `8 Regular Expressions You Should Know <http://code.tutsplus.com/tutorials/8-regular-expressions-you-should-know--net-6149>`_ (2016/03)
* `Love Python <http://love-python.blogspot.fr/>`_ (2016/03)

**Livres**

* `Apprentissage de la programmation <http://inforef.be/swi/python.htm>`_, Gérald Swinnen
* `Une introduction à Python 3 <https://perso.limsi.fr/pointal/python:courspython3>`_
* `Programmation avec le langage Python <http://www.xavierdupre.fr/site2013/documents/python/initiation_via_python_ellipse_mai_2010.pdf>`_ (PDF, ou version `Ellipse <http://www.editions-ellipses.fr/product_info.php?products_id=6891>`_)
* `Teach Yourself Python in 24 Hours <http://www.pauahtun.org/TYPython/>`_, Ivan Van Laningham 
  (le site est visuellement difficile, `version PDF <http://ptgmedia.pearsoncmg.com/images/9780672336874/samplepages/0672336871.pdf>`_)
* `Précis de recherche opérationnelle <http://www.eyrolles.com/Informatique/Livre/precis-de-recherche-operationnelle-9782100706129>`_, Robert Faure, Bernard Lemaire, Christophe Picouleau
* `Problem Solving with Algorithms and Data Structures <https://www.cs.auckland.ac.nz/courses/compsci107s1c/resources/ProblemSolvingwithAlgorithmsandDataStructures.pdf>`_, Brad Miller, David Ranum (version `html <http://interactivepython.org/courselib/static/pythonds/index.html>`_)
* `Automate Boring Stuff with Python <https://automatetheboringstuff.com/>`_ (2016/03)
* `Intermediate Python Release <http://pythontips.com/2015/08/17/intermediate-python-released/#more-665>`_ (2016/03)

**Cours**

* `Apprenez à programmer en Python <http://openclassrooms.com/courses/apprenez-a-programmer-en-python>`_ (openclassrooms)
* `A gallery of interesting Jupyter Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_
* `Python Notes <http://www.thomas-cokelaer.info/tutorials/python/index.html>`_
* `Program Arcade Games With Python And Pygame <http://programarcadegames.com/>`_
* `Python cours et TPs <http://mathcpge.org/index.php?option=com_content&view=article&id=55&Itemid=146>`_ (2016/04)
* `Le Python en prépas <http://web.isen-bretagne.fr/livres/python/>`_ (2016/04)
* `Algorithmique et programmation en CPGE <http://python-liesse.enseeiht.fr/cours/index.html>`_ (2016/04)

**Exercices**

*  `Quelques exercices du Project Euler <http://mathprepa.fr/python-project-euler-mpsi/>`_ (2016/04)

**MOOC**

* `Code Academy Python <http://www.codecademy.com/tracks/python>`_ (utilise Python 2.7)
* `Un premier Mooc Inria sur Python <https://www.france-universite-numerique-mooc.fr/courses/inria/41001/Trimestre_4_2014/about>`_
* `pyvideo.org <http://pyvideo.org/>`_

**Jeux**

* `codingame <http://www.codingame.com/>`_

**Outils**

* `PythonTutor <http://pythontutor.com/>`_ : pour suivre pas à pas l'exécution d'un programme (petit)




.. toctree::
    :hidden:

    td_1a_enonce
    td_1a_correction
    questions/question_2014

.. rubric:: Footnotes

.. [#f1] Les quatre sujets importants des six dernières séances sont la programmation dynamique, la dichotomie, les dataframe, les graphiques. La séance 9, la fin de la séance 10 et la séance 11 ne sont pas indispensables.

