

Python dans tous ses états
==========================


Contenu des séances de travaux pratiques en programmation
que je dispense à l'`ENSAE <http://www.ensae.fr/>`_. 
Ces cours s'appuient principalement sur 
le langage `Python <https://www.python.org/>`_. 
Le contenu est librement disponible sur `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_ |gitlogo|
et permet à quiconque de contribuer à ce cours. 
Il existe trois formats disponibles :
`mobile/PC <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_,
`blanc <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/index.html>`_,
`bleu <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_.
Les changements importants sont notés sur le :ref:`blog <ap-main-0>` 
associé à ce cours, les autres :ref:`l-completed-todolist`, les améliorations envisagées
:ref:`l-issues-todolis`.

.. |gitlogo| image:: _static/git_logo.png
             :height: 20
             
.. |slideslogo| image:: _static/slides_logo.png
             :height: 20


Avant-propos
------------

Les langages `R <https://www.r-project.org/>`_ et 
`Python <https://www.python.org/>`_ sont devenus 
incontournables dans le domaine des statistiques.
Ils sont simples, open source, s'apprennent rapidement, sont utilisés
par beaucoup et dispose de nombreuses pages, blogs, listes
de diffusions qui leur sont dédiées.
`R <https://www.r-project.org/>`_ est le terrain de jeu préféré des chercheurs
mais il est peu pratique pour développer un site web ou un jeu.
`Python <https://www.python.org/>`_ est beaucoup plus polyvalent
et de plus en plus populaire. Il est enseigné à l'ENSAE depuis 2004.
Les premiers pas sont parfois rebutants mais on arrive vite à 
quelque chose à condition d'y passer un peu de temps au démarrage.
Passer les premiers jeux (voir `lesenfantscodaient.fr <http://lesenfantscodaient.fr/>`_),
la programmation se révèle assez pratique pour traiter les données,
les visualiser, automatiser les tâches les plus répétitives, et
s'amuser.




**3 niveaux**

Les cours proposés sont de difficultés croissantes et orientés pour un statisticien ou data scientist.
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
-------------------------

.. toctree::
    :maxdepth: 1

    1. Algorithmes et programmation <td_1a>
    2. Python pour un Data Scientist <td_2a>
    3. Eléments logiciels pour le traitement des données massives <td_3a>
    4. Projets informatiques <projet_info>
    5. Examens <i_exams>
    6. Découvrir <i_decouvrir>
    7. Visualisation <i_visualisation>
    8. Modules, Bibliographie, Articles, FAQ... <i_informations>
    9. Getting started <i_getting_started>
    10. Index <i_index>



Getting started
---------------

.. index: notebook, installation, prérequis

Notebooks
^^^^^^^^^

Les séances utilisent les `notebooks Jupyter <http://jupyter.org/>`_.
Ils sont de plus en plus fréquent lors des conférences scientifiques et offre
un espace de travail réactif, agréable et très pratique quant il s'agit de 
partager son travail.
Chaque séance mélanage notions et exerices qu'on peut faire directement dans le notebook 
une fois téléchargé. La correction est également rédigée sous forme de notebook afin de
pouvoir aisément *jouer* avec la solution.


.. _l-getting-started-main:
.. _l-install:


Démarrage
^^^^^^^^^

Voir :ref:`l-installation-courte`.


Le langage est devenu populaire aussi parmi les data scientists grâce à un ensemble 
de librairies qui ont offert un service équivalent à ce que propose `R <https://www.r-project.org/>`_,
`pandas <http://fr.wikipedia.org/wiki/Panda>`_, 
`numpy <http://www.numpy.org/>`_, 
`matplotlib <http://matplotlib.org/>`_,
`scikit-learn <http://scikit-learn.org/stable/>`_ 
et qu'il a su réinventer la façon de travailler avec les 
notebooks et `Jupyter <http://jupyter.org/>`_.
Sous Windows, ces modules
sont accessibles depuis le site 
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
et ne peuvent pas être installés avec l'instruction ``pip install <module>`` car ils
nécessitent un compilateur C++.

    

Dépendences et automatisation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ces cours représentent plus de 60 heures de cours et travaux pratiques suivis
par plus de 200 élèves de l'ENSAE répartis sur trois années, la réception d'une centaine
de projets. Cela nécessite un peu d'automatisation implémentée en Python
mise à disposition sous forme de modules :ref:`listes des dépendances <ci-status>`.



En diagonal
-----------

* Questions, termes, FAQ
    * :ref:`FAQ <l-FAQs>` (Foire aux Questions ou Frequently Asked Questions)
    * :ref:`Glossaire <l-glossaire>`
    * :ref:`question`
    * :ref:`l-EX2`
    * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_ (PDF)
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
    
.. image:: https://ci.appveyor.com/api/projects/status/4chpamq95rh5h245?svg=true
    :target: https://ci.appveyor.com/project/sdpython/ensae-teaching-cs
    :alt: Build Status Windows    
    
.. image:: https://badge.fury.io/py/ensae_teaching_cs.svg
    :target: http://badge.fury.io/py/ensae_teaching_cs
      
.. image:: http://img.shields.io/pypi/dm/ensae_teaching_cs.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/ensae_teaching_cs  
    
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
