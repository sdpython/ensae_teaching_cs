
==========================
Python dans tous ses états
==========================

Contenu des séances de travaux pratiques en programmation
que je dispense à l':epkg:`ENSAE`.
Ces cours s'appuient principalement sur
le langage :epkg:`Python`.
Le contenu est librement disponible sur `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_ |gitlogo|
et permet à quiconque de contribuer à ce cours.
Il existe deux formats disponibles :
`mobile/PC <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_ ou
`plus large <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_.
Les changements importants sont notés sur le :ref:`blog <ap-main-0>`
associé à ce cours, certains modifications prévues
sont notés sur `Waffle/ensae_teaching_cs <https://waffle.io/sdpython/ensae_teaching_cs>`_.

.. |gitlogo| image:: _static/git_logo.png
             :height: 20

.. |slideslogo| image:: _static/slides_logo.png
             :height: 20

.. contents::
    :depth: 1
    :local:

Ce site est principalement un site d'exercices. D'autres contenus sont disponibles
sur des `éléments de machine learning <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/index.html#mlstatpy>`_,
`la programmation avec Python <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/index.html>`_,
des `jeux autour d'algorithmes <http://lesenfantscodaient.fr/>`_,
des `présentations, conférences <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/index.html>`_,
ou encore des `sujets de compétitions, hackathons <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/index.html>`_.

Avant-propos
============

Les langages `R <https://www.r-project.org/>`_ et
`Python <https://www.python.org/>`_ sont devenus
incontournables dans le domaine des statistiques.
Ils sont simples,
`open source <https://fr.wikipedia.org/wiki/Open_source>`_,
s'apprennent rapidement, sont utilisés
par beaucoup et disposent de nombreuses pages, blogs, listes
de diffusions qui leur sont dédiées.
`R <https://www.r-project.org/>`_ est le terrain de jeu préféré des chercheurs
mais il est peu pratique pour développer un site web ou un jeu.
`Python <https://www.python.org/>`_ est beaucoup plus polyvalent
et de plus en plus populaire. Il est enseigné à l':epkg:`ENSAE` depuis 2004.
Les premiers pas sont parfois rebutants mais on arrive vite à
quelque chose à condition d'y passer un peu de temps au démarrage.
La programmation est indispensable pour traiter les données,
les visualiser, automatiser les tâches les plus répétitives, et
s'amuser (voir `lesenfantscodaient.fr <http://lesenfantscodaient.fr/>`_).

**3 niveaux**

Les cours proposés sont de difficultés croissantes et orientés pour un statisticien ou un data scientist.
La pratique est un élément essentiel de l'apprentissage de la programmation.
Quoi qu'on en dise, il faut aussi être créatif.

* **1A :** syntaxe de langage, premiers algorithmes, programmation dynamique, Data Frame, premiers graphes
* **2A :** python pour un statisticien, Data Frames, calcul matriciel, machine learning,
  exercices d'algorithmie
* **3A :** calculs distribués, Map/Reduce, Hadoop, PIG, Spark, depuis un notebook

Le :ref:`blog <ap-main-0>` associé à ce site publie des liens vers des vidéos,
des données, met en valeur certaines mises à jour, aborde des sujets connexes
aux enseignements proposés.
Chaque cours est validé par un projet et c'est principalement durant cet exercice
qu'on apprend et qu'on exprime ses idées. Dire qu'on sait programmer simplement
parce qu'on a réussi les exercices du cours serait un peu comme prétendre
savoir jouer aux échecs après avoir pris connaissance des règles et sans avoir jamais
joué une partie.

Contenu des enseignements
=========================

.. toctree::
    :maxdepth: 1

    1. Algorithmes et programmation <td_1a>
    2. Python pour un Data Scientist / Economiste <td_2a>
    3. Eléments logiciels pour le traitement des données massives <td_3a>
    4. Projets informatiques <projet_info>
    5. Examens / Compétitions <i_exams>
    6. Découvrir <i_decouvrir>
    7. Visualisation <i_visualisation>
    8. Modules, Bibliographie, Articles, FAQ... <i_informations>
    9. Getting started <i_getting_started>
    10. Galleries d'exemples <i_galleries>
    11. Index <i_index>

Getting Started - Démarrer
==========================

.. index: notebook, installation, prérequis

L'immense majorité des langages de programmation est de langue anglaise.
La documentation de tous les logiciels partagés est en anglais.
Certains paragraphes y sont souvent présents comme
`Getting Started <https://www.python.org/about/gettingstarted/>`_.
Les résultats des recherches sur internet sont très souvent
plus intéressants lorsqu'elles sont libellées en anglais.

Notebooks
+++++++++

Les séances utilisent les `notebooks Jupyter <http://jupyter.org/>`_.
C'est le support privilégiés des chercheurs lors des conférences scientifiques.
Il offre un espace de travail réactif, agréable et très pratique quand il s'agit de
partager son travail.
Chaque séance mélange notions et exerices qu'on peut faire directement dans le notebook
une fois téléchargé. La correction est également rédigée sous forme de notebook afin de
pouvoir aisément *jouer* avec la solution mais elle fonctionnera dans n'importe quel
autre environnement.

.. _l-getting-started-main:
.. _l-install:

Démarrage / Installation
++++++++++++++++++++++++

Voir :ref:`l-installation-courte` pour des instuructions détaillées
sous Windows, Linux et MacOS.

Le langage est devenu populaire aussi parmi les data scientists grâce à un ensemble
de librairies qui ont offert un service équivalent à ce que propose `R <https://www.r-project.org/>`_.
`pandas <http://fr.wikipedia.org/wiki/Panda>`_,
`numpy <http://www.numpy.org/>`_,
`matplotlib <http://matplotlib.org/>`_,
`scikit-learn <http://scikit-learn.org/stable/>`_
ont élevé le niveau de fonctionnalités, les
`notebooks Jupyter <http://jupyter.org/>`_
ont changé la façon de travailler.
Les modules les plus utilisés sont maintenant fournis sur toutes les plate-formes
avec la distribution `Anaconda <https://www.continuum.io/downloads>`_.
Sous Windows, le site
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
proposent de nombreux modules qui nécessitent un compilateur C++. On les repère car
l'installation ``pip install <module>`` échoue à moins de savoir bidouiller sa machine.

Dépendences et automatisation
+++++++++++++++++++++++++++++

Ces cours représentent plus de 60 heures de cours et travaux pratiques suivis
par plus de 200 élèves de l':epkg:`ENSAE` répartis sur trois années, la réception d'une centaine
de projets. Cela nécessite un peu d'automatisation implémentée en :epkg:`Python`
mise à disposition sous forme de modules (voir :ref:`listes des dépendances <ci-status>`).

En diagonal
===========

* Questions, termes, FAQ
    * :ref:`FAQ <l-FAQs>` (Foire aux Questions ou Frequently Asked Questions)
    * :ref:`Glossaire <l-glossaire>`
    * :ref:`question`
    * :ref:`l-EX2`
    * `Résumé de la syntaxe Python <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_resume/python_sheet.html>`_
* Lectures
    * :ref:`Articles, Références, Blog <l-information>`
    * :ref:`l-codingparty`
    * :ref:`blog <ap-main-0>` de ce cours
    * :ref:`code associé à ce cours <modindex>`
    * :ref:`l-ressources`
    * :ref:`l-biblio`
* A propos de ce cours
    * :ref:`l-issues-todolist`
    * :ref:`l-completed-todolist`
* Autres supports
    * `Python et actuariat <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html>`_
    * `Présentations en notebooks <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/index.html>`_
    * `Machine Learning, Statistiques et Programmation <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/index.html>`_ (théorique)
    * `Apprendre la programmation avec Python <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/index.html#teachpyx>`_

Contributions
=============

Le cours est open source et disponible sur :epkg:`GitHub`.
N'hésitez pas à contribuer en m'envoyant des
`pull requests <https://github.com/sdpython/ensae_teaching_cs/pulls>`_
sans même avoir à récupérer tous les fichiers sur votre ordinateur :
`Editing files in your repository <https://help.github.com/articles/editing-files-in-your-repository/>`_.

+----------------------+---------------------+---------------------+--------------------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`     |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`               | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+----------------------+---------------------+---------------------+--------------------------------+------------------------+------------------------------------------------+
| :ref:`modindex`      |  :ref:`l-EX2`       | :ref:`search`       | :ref:`l-license`               | :ref:`l-changes`       | :ref:`l-README`                                |
+----------------------+---------------------+---------------------+--------------------------------+------------------------+------------------------------------------------+
| :ref:`genindex`      |  :ref:`l-FAQs`      | :ref:`l-notebooks`  | :ref:`l-getting_started_full`  | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+----------------------+---------------------+---------------------+--------------------------------+------------------------+------------------------------------------------+

.. image:: https://travis-ci.org/sdpython/ensae_teaching_cs.svg?branch=master
    :target: https://travis-ci.org/sdpython/ensae_teaching_cs
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/ko5g064idp5srm74?svg=true
    :target: https://ci.appveyor.com/project/sdpython/ensae-teaching-cs
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/ensae_teaching_cs/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/ensae_teaching_cs/tree/master

.. image:: https://badge.fury.io/py/ensae_teaching_cs.svg
    :target: http://badge.fury.io/py/ensae_teaching_cs

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://codecov.io/github/sdpython/ensae_teaching_cs/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/ensae_teaching_cs?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/ensae_teaching_cs.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/ensae_teaching_cs/issues

.. image:: https://badge.waffle.io/sdpython/ensae_teaching_cs.png?label=ready&title=Ready
    :alt: Waffle
    :target: https://waffle.io/sdpython/ensae_teaching_cs

.. image:: https://api.codacy.com/project/badge/Grade/80a874c0eafd4ea68f3493d73b43f0c5
    :target: https://www.codacy.com/app/sdpython/ensae_teaching_cs?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sdpython/ensae_teaching_cs&amp;utm_campaign=Badge_Grade
    :alt: Codacy Badge

.. image:: nbcov.png
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage
