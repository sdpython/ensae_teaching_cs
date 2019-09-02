
.. _l-feuille-de-route-2019-1A:

Feuille de route 2019 (1A)
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
    * - (1) 3/9 amphi
      - Présentation/rappel du langage :epkg:`Python` sur les élements du langage,
        (type de variables, tests, fonctions),
        présentation de l'environnement à l'ENSAE,
        installation de :epkg:`Python` sur Windows, Linux, Mac,
        installation de modules, présentation des notebooks,
        :ref:`l-route2018-algo1`
    * - (2) 10/9 TD
      - Premiers algorithmes simples, intégrale de Rienmann,
        2048, deviner la langue d'un texte, pyramide bigarrée,
        :ref:`l-route2018-algo2`
    * - (3) 17/9 TD
      - Classes, expression régulières, templating, fichiers,
        :ref:`l-route2018-algo3`
    * - (4) 24/9 TD
      - Graphes et distance d'édition,
        notions de coût algorithmique,
        :ref:`l-route2018-algo4`,
        :ref:`2018-09-25distanceentremotsrst`
    * - (5) 1/10 TD
      - Création d'un module :epkg:`Python` avec
        des tests unitaires, un setup, une documentation,
        pour ceux qui veulent :
        mise en ligne sur *github*, *bitucket*, *gitlab*, ...
        et mise en place de l'intégration continue, notion
        de :epkg:`git`, outil de profilage,
        :ref:`l-route2018-algo5`
    * - (6) 8/10 TD
      - Manipuler les matrices, les données sous :epkg:`Python`,
        :epkg:`numpy`, :epkg:`pandas`, :ref:`l-route2018-algo6`
    * - (7) 15/10 TD
      - Visualisation, statique et javascript,
        module :epkg:`matplotlib`, :epkg:`bokeh`,
        :epkg:`pyecharts`, réalisation de cartes
        avec :epkg:`cartopy`, rendu du module

        :ref:`l-route2018-algo7`
    * - (8) 22/10 TD noté

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
Ils fonctionneront également sur les versions 3.5 et 3.6. Le plus simple
pour installer :epkg:`Python` est d'utiliser la distribution :epkg:`Anaconda`.
La distribution standard fonctionne également en s'aidant ce cette page
`Unofficial Windows Binaries for Python Extension Packages <https://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
pour *Windows* et de celle-ci pour la distribution
*Debian 9* (*Ubuntu est très similaire) :
`Install Python 3.7 and many packages on Linux Debian 9 <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/2018/2018-08-19_python37.html>`_.

Intervenants
++++++++++++

`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_,
Lucie Neirac, Benoît Choffin.

Notes
+++++

Liens, notebooks prévus pour les séances pratiques.

.. contents::
    :local:

Séance 1 - 3/9
^^^^^^^^^^^^^^

Python, choix du langage, évaluation,
modules, mise en production, algorithmes,
quelques mots sur les années prochaines...

* :ref:`coloriagecarrerst`

Séance 2 - 10/9
^^^^^^^^^^^^^^^

Les notebooks correspondant aux premiers algorithmes :

* :ref:`l-td1a-lesbases`
* Recherche dichotomique, :ref:`l-td1a-algo-dicho-graphe`,
* :ref:`td1a-algo-amusement`

Autres algorithmes, résolution d'un sudoku (:ref:`l-sudoku-sol`),
d'une puzzle ou coloriage (:ref:`f-puzzlegirafe`) :

* `coloriage <http://www.xavierdupre.fr/site2013/enseignements/tdnoteseul/td_note_2013.pdf>`_,
  :ref:`tdnote2013boutdecodecoloriagerst`,
  :ref:`tdnote2013coloriagecorrectionrst`

Séance 3 - 17/9
^^^^^^^^^^^^^^^

Notebooks sur les classes et les expressions régulièrs,
dans la section qui suit :

* :ref:`l-td1a-lesbases`

Pour le templating, il faut voir les modules
:epkg:`jinja2` ou :epkg:`mako`.
Le principe est assez simple et plutôt bien
documenté. Indispensable pour concevoir des sites
web. `TemPy <https://github.com/Hrabal/TemPy>`_
est aussi à regarder car le design est différent.

Séance 4 - 24/9
^^^^^^^^^^^^^^^

Notion de graphes,
un algorithme sur les graphes,
un autre sur la distance d'édition,

* :ref:`l-td1a-algo-dicho-graphe`
* :ref:`2018-09-25distanceentremotsrst`

Jeter un oeil sur la liste
:ref:`l-algoculture-shortlist`.

Séance 5 - 1/10
^^^^^^^^^^^^^^^

* :ref:`l-production`
* :ref:`gitnotebookrst`
* :ref:`profilingexamplerst`

Sur :epkg:`github` :
`td1a_unit_test_ci <https://github.com/sdpython/td1a_unit_test_ci>`_.

Séance 6 - 8/10
^^^^^^^^^^^^^^^

Premiers notebooks sur les dataframes et les
matrices avec les modules :epkg:`numpy`
et :epkg:`pandas`.

* :ref:`l-td1a-numpy-pandas-plt`

Séance 7 - 15/10
^^^^^^^^^^^^^^^^

Derniers notebooks sur les dataframes et les
matrices avec les modules :epkg:`matplotlib`,
:epkg:`bokeh`, :epkg:`cartopy`.

* :ref:`l-td1a-numpy-pandas-plt`

Rendre le module :epkg:`python` implémentant une stratégie pour le jeu 2048,
:ref:`l-examens-1A-algo-2048`.

Séance 8 - 22/10
^^^^^^^^^^^^^^^^

**TD noté**.
