

.. _l-production:


Génie logiciel : coder facilement, coder à plusieurs, qualité du code, gestion de projets
=========================================================================================

L'industrie logiciel a beaucoup évolué en 20 ans et plusieurs standards ont émergé
pour travailler à plusieurs et produire un logiciel avec peu d'erreurs.
Cette page est plus un guide de bonne conduite, un ensemble de pratiques
permettant d'améliorer la qualité du code. 
Ces pratiques ne sont sans doute pas utiles 
si votre code est juste une étude et n'a pas vocation à durer.
Dans ce cas, je recommande tout de même l'utilisation d'un 
:ref:`l-suivi-source-p`. Les :ref:`l-unittest-p` et la 
:ref:`l-doc-p` sont à considérer dès le début du projet
dans le cas contraire. Il est beaucoup plus difficile
de les ajouter par la suite.


.. contents::
    :local:

Robustesse du code
------------------

.. _l-unittest-p:


Tests unitaires
^^^^^^^^^^^^^^^

.. index:: test unitaire

Les fonctions d'un programme prenne part à un grand ensemble et lorsqu'une
erreur se déclare, il n'est pas toujours évident de localiser la source d'erreur.
Ce cas arrive fréquemment lorsqu'on modifie le code d'une fonction
utilisée par beaucoup d'autres.
Les `tests unitaires <https://fr.wikipedia.org/wiki/Test_unitaire>`_ ont pour 
objectif de d'assurer de la qualité du code.
Ils permettent de vérifier qu'une modification n'a pas de répercussionss
inattendues. La règle veut qu'on ajout un test unitaire pour chaque fonction
ajoutée au code et chaque bug découvert. 
Dans la pratique, si on ne le fait pas tout de suite, on le fait
rarement. Il est impensable de vendre ou écrire un projet open source
sans ces tests. La plupart des langages permettent d'écrire cela
rapidement. En Python :ref:`Qu'est-ce qu'un test unitaire ? <faq-python-tu>`
avec les modules :

* `unittest <https://docs.python.org/3/library/unittest.html>`_
* `nose <http://nose.readthedocs.io/en/latest/>`_
* `pytest <http://pytest.org/latest/>`_
* `green <https://github.com/CleanCut/green>`_

**resources distantes**

Les tests unitaires sont difficiles à mettre en place dès qu'une resource distance est impliquée.
Le test peut échouer parce qu'Internet n'est pas accessible, parce que le site web ne répond pas,
pour un problème d'identification. Ce problème est abordée au paragraphe suivant
avec le concept de `mock <https://fr.wikipedia.org/wiki/Mock_%28programmation_orient%C3%A9e_objet%29>`_.

Une des réponses est d'introduire plusieurs séries de tests :

* *tests unitaires ou fonctionnels* : teste une fonction en particulier, ces tests sont très rapides.
* *tests d'intégration* : vérifier qu'une librairie fonctionne toujours avec ses dépendances,
  surtout après une mise à jour. C'est important surtout si on écrit du code
  différencié selon la version d'une dépendance.
* *tests de non régression* : teste un algorithme et vérifie que sa réponse ne se dégrage 
  après une modification, qu'un bug fixé le reste.
* *tests système ou end to end* : teste une fonctionnalité impliquant une ressource externe
  (serveur SQL, Internet), sur un environnement précis.

**site web, serveur**

Il faut démarrer un serveur pour tester un site de bout en bout.

* :ref:`test unitaire est flask <l-flask-unittest>`
* `Testing Flask Applications <http://flask.pocoo.org/docs/testing/>`_, `Flask testing <https://pythonhosted.org/Flask-Testing/>`_
* `Writing and running tests with Django <https://docs.djangoproject.com/en/1.9/topics/testing/overview/>`_

Et cela ne suffit pas toujours car la plupart des sites utilisent
du javascript pour lesquels il faudrait simuler des événements au clavier
(touches, souris) une fois le site lancé.
Pour vérifier certains aspects du site web tels qu'ils seront par un internaute :

* `Selenium with Python <http://selenium-python.readthedocs.io/>`_ (voir aussi :ref:`Issue with Selenium and Firefox <faq-web-selenium>`)
* `Splinter <http://splinter.readthedocs.io/en/latest/>`_

**GUI**

Même si on crée de moins en moins d'application GUI (avec une interface graphique), 
il est préférable de les tester.

* `pyautogui <https://github.com/asweigart/pyautogui>`_
* `pywinauto <https://github.com/pywinauto/pywinauto>`_
* `autopy3 <https://pypi.python.org/pypi/autopy3/>`_ (buggé la dernière fois que je l'ai essayé - 2016/08)

A ce sujet, lire `Automate the boring stuff with Python <https://automatetheboringstuff.com/#toc>`_.


Mock
^^^^

.. index:: mock

`Mocking <https://en.wikipedia.org/wiki/Mock_object>`_ désigne une astuce uilisée
pour écrire un test unitaire pour une fonctionnalité utilisant une ressource externe
comme internet. Par exemple, on souhaite tester une fonction qui 
vérifie que son adresse est la bonne sur un site internet. Cela inclut :

* télécharger le contenu de la page
* parser le contenu pour extraire l'adresse
* vérifier que l'adresse est la bonne

Le problème survient souvent lorsqu'un internet n'est pas accessible.
Le test échoue mais pas pour la bonne raison. On construit alors
un objet qui retourne toujours le même contenu qu'on aura enregistré.
On peut alors tester séparément le fait de télécharger une page
et celui d'extraire une adresse et de la comparer avec une autre.
En Python, on fait cela avec le module :

* `unittest.mock <https://docs.python.org/3/library/unittest.mock.html>`_

Profiling
^^^^^^^^^

.. index:: profiling

Si un programme lent ou gros consommateur de mémoire,
on veut savoir où le programme perd du temps ou 
occasionne des pics de mémoire. Le profiling permet de 
mesurer la vitesse d'exécution et la consommation de chaque fonction ou chaque ligne.
Voir `Exemples de profiling <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/completion_profiling.html#completionprofilingrst>`_

Couverture des tests unitaires
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: coverage

La `couverture d'un code informatique <https://en.wikipedia.org/wiki/Code_coverage>`_
mesure le nombre de lignes de code effectivement executée lors de l'exécution
des tests unitaires. Une couverture de 80\% est souvent un bon gage de qualité.
En deça, il faut généralement s'attendre à quelques surprises. Pour mesurer
cette couverture, un module `coverage <http://coverage.readthedocs.io/>`_.
Il est plus facile d'augmenter la couverture pour des fonctions de calculs numériques
et c'est plus difficile pour un processus d'automatisation qui requiert l'accès à une ressource
externe. On s'aperçoit aussi que les exceptions ne sont pas souvent couvertes
par les tests unitaires.

Déploiement
^^^^^^^^^^^

Une application web fonctionne rarement sur une seule machine, l'application
est déployée sur plusieurs machines. Une entreprise dispose en générale de plusieurs environnements
de test afin de pouvoir tester une application ou un service en grandeur réelle sans l'exposer
aux utilisateurs. Cela requiert pas mal d'automatisation afin que cela soit facile
et rapide. Voir `ansible <http://docs.ansible.com/ansible/index.html>`_.

Tests logiques et preuve formelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tous les tests présentés ci-dessus ne font que tester un cas particulier.
La fonction marche avec ce jeu de données dans ce cas précis.
Le test ne vérifie pas que la fonction est valide dans tous les cas.
Cela ne peut passer que part une preuve formelle que le code
fonctionne. Dans certains cas, cette preuve formelle est nécessaire 
car toute erreur a un coût prohibitif. Les logiciels de calculs 
utilisée par Ariane Espace le sont. On rentre dans le domaine des mathématiques.

* `Méthode B <http://www.methode-b.com/>`_, 
  `Un grand succès pour la preuve informatique <http://www.inria.fr/centre/saclay/actualites/un-grand-succes-pour-la-preuve-informatique>`_
* `Logique de Coq <https://fr.wikipedia.org/wiki/Coq_(logiciel)>`_
* `Introduction à la preuve de programmme <https://www.irif.univ-paris-diderot.fr/~tasson/doc/cours/cours_pp.pdf>`_, Christine Tasson
* `Mechanized Formal Semantics and Verified Compilation for C++ Objects <http://gallium.inria.fr/~tramanan/cxx/>`_, Tahina Ramananandro
* `Frama-C <http://frama-c.com/index.html>`_
* `Static Source Code Analysis Tools for C <http://www.spinroot.com/static/>`_

Ces outils ne s'appliquent pas aux langages faiblement typés.
Ils s'intéressent entre autres aux erreurs d'arrondis.
Il est difficile de prévoir la valeur d'un résultat si le type
change au cours des calculs.


Pratiques utiles
----------------

Logging
^^^^^^^

.. index:: logging

`Logger <https://en.wikipedia.org/wiki/Logfile>`_ consiste à enregister des événements,
des opérations effectués par un programme dans le but de les analyser plus tard en cas d'erreur.
Les logiciels sont maintenus conçus pour ne plus s'arrêter en cas d'erreur, 
celle-ci est donc *loggée* ainsi que la séquence d'événements qui a débouché sur cette erreur
en espérant que cette information sera suffisante pour comprendre et corriger l'erreur.
Dans le cas de site web, l'information est utilisée pour mesurer l'audience
de pages internet, la fréquence d'événements, leur enchaînements.
Pour éviter de ralentir le programme, l'information est stockée dans un fichier texte plat.
En Python, cela se fait avec le module `logging <https://docs.python.org/3.5/library/logging.html>`_
(voir aussi `logbook <http://logbook.readthedocs.io/en/stable/>`_).

Logger n'est pas aussi simple qu'il y paraît. Il faut choisir un format de fichier qui facilite
l'analyse. Le plus souvent :

::

    <data> <niveau> <message>
    
Le niveau de logging (souvent INFO, TRACE, WARNING, ERROR) détermine la quantité d'information
que le programme enregistre. Plus il y en a, plus c'est lent. Quand on développe, on logge tout,
en production, on se restreint aux avertissements et erreurs
(voir `Good logging practice in Python <http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python>`_,
`Python 101: An Intro to logging <http://www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging/>`_).

La difficulté majeure quand on logge survient quand le programme s'exécute en parallèle.
En règle générale, la fonction qui permet de logger une information ne fait pas
partie des arguments qu'elle reçoit : c'est une variable statique.
De cette façon, le programme est plus clair mais il arrive que la même fonction
s'exécute plusieurs fois en parallèle. Il devient alors difficile de reconstituer 
une séquence d'événement appartenant au même fil d'exécution. Les outils de logging 
sont capables de reconnaître différents contextes (le thread) mais cela a un 
coût en terme de performance. Il faut éviter de logger trop d'information, 
âs plus d'une dizaine par secondes.




.. _l-doc-p:

Documentation
^^^^^^^^^^^^^

.. index:: documentation

L'outil standard en Python est `Sphinx <http://www.sphinx-doc.org/en/stable/>`_.
Il aboutit à une documentation statique comme ce site web. Il faut
suivre un unique format comme `RST <http://docutils.sourceforge.net/rst.html>`_ ou 
MD (`markdown <https://daringfireball.net/projects/markdown/>`_) pour écrire
la documentation et il faut commencer dès les premières fonctions.

Les principaux écueils sont une documentation obsolète
car une modification n'a pas été reportée dans la documentation
et des exemples qui ne fonctionne pas ou plus. Le plus simple est de s'inspirer de 
la documentation d'un module qui vous plaît. On y retrouve presque toujours les 
sections :

* Un exemple de bienvenue
* Installation
* Tutorial
* Documentation

Il faut également faire attention au choix des noms de classes
et fonctions. La documentation est parfois superflue lorsque ceux-ci
sont bien choisis.


Style
-----


Annotations
^^^^^^^^^^^

.. index:: annotation

Le langage Python est faiblement typé. On précise parfois le type
attendu dans la documentation d'une fonction ou d'une classe.
Les annotations sont un moyen formel de le faire. Même si elle
n'a aucune incidence, cette information peut être utilisée :

* dans la documentation
* pour vérifier les types à l'exécution (`typecheck-decorator <https://pypi.python.org/pypi/typecheck-decorator>`_)
* améliorer les performaces des `JIT <https://en.wikipedia.org/wiki/Just-in-time_compilation>`_ 
  (lire `Would type annotations help PyPy’s performance? <http://doc.pypy.org/en/latest/faq.html?highlight=annotation#would-type-annotations-help-pypy-s-performance>`_)

Ce concept a été introduit par la version 3.5.

* `typing <https://docs.python.org/3/library/typing.html>`_
* `Tutorial <http://code.tutsplus.com/tutorials/python-3-function-annotations--cms-25689>`_
* `pep-484 <https://www.python.org/dev/peps/pep-0484/>`_, `pep-3107 <https://www.python.org/dev/peps/pep-3107/>`_
* `mypy <http://www.mypy-lang.org/>`_

PEP8
^^^^

.. index:: pep8

Il est plus facile de lire un code qui suit toujours les mêmes règles d'écriture.
En Python, on les appelles `PEP8 <https://pypi.python.org/pypi/pep8>`_. 
Ce ne sont pas des règles à suivre à la lettre mais la plupart
des développeurs python les suivent. 

* `pep8 <https://pypi.python.org/pypi/pep8>`_
* `flake8 <https://pypi.python.org/pypi/flake8>`_, `flake8 <https://pypi.python.org/pypi/flake8/>`_
* `pylint <https://www.pylint.org/>`_

A vous de voir.
A l'école, cela n'a pas d'incidence. Dans une compagnie, c'est très variable.

Design
^^^^^^

En terme de design, `scikit-learn <http://scikit-learn.org/>`_ est un modèle du genre.
La librairie propose des algorithmes de machine learning - ce n'est pas nouveau - mais
son adoption rapide est due à la simplicité de son interface, de son design.

* petites fonctions
* séparation GUI / web / algorithme
* long process : prévoir une interruption, logging, processus asynchrone
* GUI réactive : asynchrone
* éviter les variables statiques




Outils
------

.. _l-suivi-source-p:

Logiciel de suivi de source
^^^^^^^^^^^^^^^^^^^^^^^^^^^

C'est devenu un outil incontournable pour garder la trace des modifications apporter
à un programme. La première tâche est la possiblité de revenir en arrière.
C'est un outil qui permet d'accéder rapidement à la partie de code modifiée.
Aujourd'hui, la plupart des nouveaux projets commencent sur `git <https://git-scm.com/>`_.
Et vous devriez connaître les trois sites suivants qui hébergent gratuitement 
les projets open source :

* `GitHub <https://github.com/>`_
* `GitLab <https://gitlab.com/>`_
* `Bitbucket <https://bitbucket.org/>`_

Ces sites sont payants pour tout projet privé.
`GitHub <https://github.com/>`_ hébergent la grande majorité des projets open source.
Il est aussi une extension du CV.


Gestion de projet
^^^^^^^^^^^^^^^^^

.. index:: KanBan

Le terme consacré est `KanBan <https://en.wikipedia.org/wiki/Kanban>`_.
Il est issu des `méthodes agiles <https://fr.wikipedia.org/wiki/M%C3%A9thode_agile>`_.
Concrètement, plus on en nombreux à travailler sur le même projet, 
plus il est difficile de garder la trace de ce que chacun fait.
Cette approche a été en quelque sorte validée par la pratique.
 
* `5 open source alternatives to Trello <https://opensource.com/business/15/8/5-open-source-alternatives-trello>`_
* `Waffle <https://waffle.io/>`_
* `Top Agile Tools – Best Kanban Tools <http://agilescout.com/best-kanban-tools/>`_
* `Portable Kanban <https://dmitryivanov.net/>`_
* `Kanboard <https://kanboard.net/>`_
* `Restyaboard <http://restya.com/board>`_
* `Taiga <https://taiga.io/>`_


Revue de code
^^^^^^^^^^^^^

Une `revue de code <https://fr.wikipedia.org/wiki/Revue_de_code>`_  
intervient avant la mise à jour du code d'un logiciel.
C'est l'occasion pour un dévelopeur de partager ses modifications avec le reste de son équipe
qui commentent les parties du code qui leur déplaisent ou qu'ils approuvent 
si la mise à jour leur convient. La règle est souvent qu'une modification ne peut 
être prise en compte dans le code de l'application que si un ou deux autres dévelopeurs
la valide.

Poussé à l'extrême, cela devient le 
`pair programming <https://en.wikipedia.org/wiki/Pair_programming>`_ qui
consiste à programmer à deux devant le même écran.
C'est assez cauchemardesque si c'est permanent.

Continuous integration
^^^^^^^^^^^^^^^^^^^^^^

On devrait faire tourner l'ensemble des tests unitaires à chaque modification.
En pratique, on le fait pas toujours voire rarement car cela prend trop de temps.
On délègue cette tâche à une machine distante. Toute cette machinerie
fait partie des systèmes d'intégration continue :

* un dévelopeur ajoute une modification au code source
* l'application est compilé
* les tests unitaires sont validés
* l'application est déployée

Ce circuit est effectué à chaque modification ou chaque nuit.
C'est ce type de service que propose gratuitement pour les projets open source
`travis <https://travis-ci.org/>`_ sur Linux,
`appveyor <https://www.appveyor.com/>`_ sur Windows.
Il existe d'autres alternatives comme
`Circle CI <https://circleci.com/>`_ (payant). 
Ces trois solutions s'exécutent à distance. Localement,
on peut utiliser `Jenkins <https://jenkins.io/>`_ qui est 
très simple d'utilisation ou `BuildBot <http://buildbot.net/>`_
Ce site est construit avec `Jenkins <https://jenkins.io/>`_.




.. todoext::
    :title: terminer la page dédiée aux outils et pratiques dans l'industrie logicielle
    :issue: 7
    :hidden:
    :tag: plus
    :date: 2016-08-03
    
    Chaque année, les étudiants poussent de plus en plus loin leur réflexion
    sur les différents moyens de travailler à plusieurs sur un projet.
    Il s'agit d'exposer les pratiques actuelles liées à la gestion
    d'un projet informatique.
