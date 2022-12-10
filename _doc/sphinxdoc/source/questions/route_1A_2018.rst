
.. _l-feuille-de-route-2018-1A:

Feuille de route 2018 (1A)
==========================

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td1a>`

Plan
++++

.. list-table::
    :widths: 2 10
    :header-rows: 1

    * - Séance
      - Notes
    * - (1) 4/9 amphi court et TD
      - Présentation/rappel du langage :epkg:`Python` sur les élements du langage,
        (type de variables, tests, fonctions),
        présentation de l'environnement à l'ENSAE,
        installation de :epkg:`Python` sur Windows, Linux, Mac,
        installation de modules, présentation des notebooks,
        :ref:`l-route2018-algo1`
    * - (2) 11/9 TD
      - Premiers algorithmes simples, intégrale de Rienmann,
        2048, deviner la langue d'un texte, pyramide bigarrée,
        :ref:`l-route2018-algo2`
    * - (3) 18/9 TD
      - Classes, expression régulières, templating, fichiers,
        :ref:`l-route2018-algo3`
    * - (4) 25/9 TD
      - Graphes et distance d'édition,
        notions de coût algorithmique,
        :ref:`l-route2018-algo4`,
        :ref:`2018-09-25distanceentremotsrst`
    * - (5) 2/10 TD
      - Création d'un module :epkg:`Python` avec
        des tests unitaires, un setup, une documentation,
        pour ceux qui veulent :
        mise en ligne sur *github*, *bitucket*, *gitlab*, ...
        et mise en place de l'intégration continue, notion
        de :epkg:`git`, outil de profilage,
        :ref:`l-route2018-algo5`
    * - (6) 9/10 TD
      - Manipuler les matrices, les données sous :epkg:`Python`,
        :epkg:`numpy`, :epkg:`pandas`, :ref:`l-route2018-algo6`
    * - (7) 16/10 TD
      - Visualisation, statique et javascript,
        module :epkg:`matplotlib`, :epkg:`bokeh`,
        :epkg:`pyecharts`, réalisation de cartes
        avec :epkg:`cartopy`, création d'un site
        web avec :epkg:`flask`,
        :ref:`l-route2018-algo7`
    * - (8) 23/10 TD
      - Module :epkg:`numba`,
        mélanger du code C++ avec :epkg:`Cython`,
        :epkg:`pybind11`, optimisation quadratique
        pour ceux que le C++ rebute, algorithme de streaming,
        :ref:`l-route2018-algo8`

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

Les exercices et notebooks sont testées sur la version :epkg:`Python` 3.9.
Ils fonctionneront également sur les versions 3.5 et 3.6. Le plus simple
pour installer :epkg:`Python` est d'utiliser la distribution :epkg:`Anaconda`.
La distribution standard fonctionne également en s'aidant ce cette page
`Archived: Unofficial Windows Binaries for Python Extension Packages
<https://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
pour *Windows* et de celle-ci pour la distribution
*Debian 9* (*Ubuntu est très similaire) :
`Install Python 3.7 and many packages on Linux Debian 9
<http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2018/2018-08-19_python37.html>`_.

Notes
+++++

Liens, notebooks prévus pour les séances pratiques.

.. contents::
    :local:

.. _l-route2018-algo1:

Séance 1
^^^^^^^^

Les premiers notebooks de cette section.

* :ref:`l-td1a-lesbases`
* :ref:`matrixdictionaryrst`

.. _l-route2018-algo2:

Séance 2
^^^^^^^^

Les notebooks correspondant aux premiers algorithmes :

* :ref:`l-td1a-lesbases`
* Recherche dichotomique, :ref:`l-td1a-algo-dicho-graphe`,
* :ref:`td1a-algo-amusement`

Autres algorithmes, résolution d'un sudoku (:ref:`l-sudoku-sol`),
d'une puzzle ou coloriage (:ref:`f-puzzlegirafe`) :

* `coloriage <http://www.xavierdupre.fr/site2013/enseignements/tdnoteseul/td_note_2013.pdf>`_,
  :ref:`tdnote2013boutdecodecoloriagerst`,
  :ref:`tdnote2013coloriagecorrectionrst`

.. _l-route2018-algo3:

Séance 3
^^^^^^^^

Notebooks sur les classes et les expressions régulièrs,
dans la section qui suit :

* :ref:`l-td1a-lesbases`

Pour le templating, il faut voir les modules
:epkg:`jinja2` ou :epkg:`mako`.
Le principe est assez simple et plutôt bien
documenté. Indispensable pour concevoir des sites
web. `TemPy <https://github.com/Hrabal/TemPy>`_
est aussi à regarder car le design est différent.

.. _l-route2018-algo4:

Séance 4
^^^^^^^^

Notion de graphes,
un algorithme sur les graphes,
un autre sur la distance d'édition,

* :ref:`l-td1a-algo-dicho-graphe`
* :ref:`2018-09-25distanceentremotsrst`

Jeter un oeil sur la liste
:ref:`l-algoculture-shortlist`.

.. _l-route2018-algo5:

Séance 5
^^^^^^^^

* :ref:`l-production`
* :ref:`gitnotebookrst`
* :ref:`profilingexamplerst`

Sur :epkg:`github` :
`td1a_unit_test_ci <https://github.com/sdpython/td1a_unit_test_ci>`_.

.. _l-route2018-algo6:

Séance 6
^^^^^^^^

Premiers notebooks sur les dataframes et les
matrices avec les modules :epkg:`numpy`
et :epkg:`pandas`.

* :ref:`l-td1a-numpy-pandas-plt`

.. _l-route2018-algo7:

Séance 7
^^^^^^^^

Derniers notebooks sur les dataframes et les
matrices avec les modules :epkg:`matplotlib`,
:epkg:`bokeh`, :epkg:`cartopy`.

* :ref:`l-td1a-numpy-pandas-plt`

Sur :epkg:`Flask` :

* Un peu de lecture : :ref:`l-td1a-ut-flask-profiling`
* :ref:`TD2Aecodebuterflaskrst`

.. _l-route2018-algo8:

Séance 8
^^^^^^^^

La connaissance du :epkg:`C++` est un plus
pour ceux qui souhaitent faire une thèse ou
qui souhaitant écrire une librairie de calcul
numérique.

* :ref:`cffilinearregressionrst`
* :ref:`td1acythoneditrst`
* :ref:`td1acythoneditcorrectionrst`
* :ref:`l-acc-code-llvm`

Voir aussi :epkg:`cpyquickhelper` qui illustre
plusieurs techniques d'optimisation.
Pour l'optimisation et les algorithmes de streaming (BJKST),
voir les notebooks reliés dans la section :

* :ref:`l-td1a-algo-dicho-graphe`
