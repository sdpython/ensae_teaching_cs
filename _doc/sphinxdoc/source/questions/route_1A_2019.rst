
.. _l-feuille-de-route-2019-1A:

Feuille de route 2019 (1A)
==========================

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td1a>`

Evaluation
++++++++++

* :ref:`module informatique <l-examens-1A-algo>` -
  8 novembre (vendredi) - 1/3 de la note finale,
  (6/20 pour réaliser le module, 6/20 pour
  implémenter une stratégie qui fonctionne, 6/20 pour
  écrire un test unitaire, 2/20 pour fournir un exemple
  d'utilisation du module qui fonctionne, 1 point
  pour être dans les 5 premiers)
* :ref:`l-seances-notees-1A` - 22 octobre -
  2/3 de la note finale

Au second semestre, pas de TD, juste un
:ref:`projet informatique <l-projinfo1a>`,
par groupe à soutenir en juin.

Prérequis
+++++++++

La programmation fait maintenant partie
du programme des `classes préparatoires <https://info-llg.fr/>`_.
Ce cours suppose que les
`types du langage <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_lang/types.html>`_,
sa `syntaxe <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_lang/syntaxe.html>`_
sont connus tout comme quelques algorithmes de :ref:`tri <trinlndrst>` comme
le `tri bulle <https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles>`_
et le `tri fusion <https://fr.wikipedia.org/wiki/Tri_fusion>`_.

Version de Python
+++++++++++++++++

Les exercices et notebooks sont testées sur la version :epkg:`Python` 3.7.
Le plus simple pour installer :epkg:`Python` est d'utiliser la distribution
:epkg:`Anaconda`. La distribution standard fonctionne également en s'aidant de cette page
`Archived: Unofficial Windows Binaries for Python Extension Packages
<https://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
pour *Windows* et de celle-ci pour la distribution
*Debian 9* (Ubuntu est très similaire) :
`Install Python 3.7 and many packages on Linux Debian 9
<http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2018/2018-12-29_python37_2.html>`_.

Plan proposé
++++++++++++

Liens, notebooks prévus pour les séances pratiques.

.. contents::
    :local:

Séance 1 - 3/9 - introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python, choix du langage, évaluation,
modules, mise en production, algorithmes,
quelques mots sur les années prochaines...

* :ref:`coloriagecarrerst`

Séance 2 - 10/9 - parcours de solutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Suggestions :

* résolution d'un sudoku (:ref:`l-sudoku-sol`)
* `coloriage <http://www.xavierdupre.fr/site2013/enseignements/tdnoteseul/td_note_2013.pdf>`_,
  :ref:`tdnote2013boutdecodecoloriagerst`,
  :ref:`tdnote2013coloriagecorrectionrst`

Autres suggestions :

* :ref:`l-td1a-lesbases`
* Recherche dichotomique, :ref:`l-td1a-algo-dicho-graphe`,
* :ref:`td1a-algo-amusement`
* :ref:`l-puzzle_girafe`

Séance 3 - 17/9 - expressions régulières et classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :ref:`td1acenoncesession4rst` (correction : :ref:`td1acorrectionsession4rst`)
* :ref:`l-1a-classe-heritage`

Le templating est un sujet intéressant
mais facile à comprendre dès les premières
de documentation. Il faut voir les modules
:epkg:`jinja2` ou :epkg:`mako`.
Le principe est assez simple et plutôt bien
documenté. Indispensable pour concevoir des sites
web. `TemPy <https://github.com/Hrabal/TemPy>`_
est aussi à regarder car le design est différent.

Autres suggestions :

* :ref:`l-td1a-lesbases`

Séance 4 - 24/9 - graphes - distance d'édition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lectures :

* :ref:`2018-09-25distanceentremotsrst`

Notebooks : :ref:`l-td1a-algo-dicho-graphe`

* un notebook sur les graphes
* un notebook sur les distances

Jeter un oeil sur la liste
:ref:`l-algoculture-shortlist`.

Séance 5 - 1/10 - génie logiciel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :ref:`l-production`
* :ref:`gitnotebookrst`
* :ref:`profilingexamplerst`

Sur :epkg:`github` :
`td1a_unit_test_ci <https://github.com/sdpython/td1a_unit_test_ci>`_.

Séance 6 - 8/10 - dataframe - matplotlib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Premiers notebooks sur les dataframes et les
matrices avec les modules :epkg:`numpy`
et :epkg:`pandas`.

* :ref:`l-td1a-numpy-pandas-plt`

Derniers notebooks sur les dataframes et les
matrices avec les modules :epkg:`matplotlib`,
:epkg:`bokeh`.

* :ref:`l-td1a-numpy-pandas-plt`

Séance 7 - 15/10 - cartes et 2048
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notebook suggérés sur les cartes :

* :ref:`l-td1a-numpy-pandas-plt`

Notebooks : :ref:`l-td1a-algo-dicho-graphe`

* plus court chemin dans un graph

Les élèves doivent tester leur module en TD.
Rendre le module :epkg:`python` implémentant
une stratégie pour le jeu 2048,
:ref:`l-examens-1A-algo-2048`.

Séance 8 - 22/10 - révision - TD noté
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**TD noté**.
