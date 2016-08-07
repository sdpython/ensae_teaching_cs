


.. _l-td1a:


============================
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


.. contents::
    :local:


TD - les bases
==============

Ce cours s'étale sur 12 séances de travaux dirigés (TD) d'une durée de 2h. Le cours est décrit plus 
en détail dans cette présentation : 
`ENSAE 1A - Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx/index.html>`_. |slideslogo|
Les six premières séances font les éléments de syntaxe propres à 
la `programmation impérative <https://fr.wikipedia.org/wiki/Programmation_imp%C3%A9rative>`_.

.. toctree::
    :maxdepth: 2

    notebooks/_gs1a_1_premiers_pas
    notebooks/_gs1a_2_variables
    notebooks/_gs1a_3_dictionnaires_fonctions
    notebooks/_gs1a_4_fichier_module
    notebooks/_gs1a_5_classes

Les programmes sont des assemblages de petites fonctions qui font souvent 
les mêmes choses. Voici une idée de ces *mêmes choses* qu'on fait tout le temps
et qu'il est important de comprendre.

.. toctree::
    :maxdepth: 1

    all_example_ConstructionsClassiques
    notebooks/code_liste_tuple
    all_example_Ngatifs
    all_example_Impossibleretenir    
    all_example_TD1A
    all_example_science
    all_example_techniques
    
    
Le premier jeu qu'on demande d'implémenter à tous ceux qui commencent la 
programmation :
    
.. toctree::
    :maxdepth: 1

    notebooks/pp_exo_deviner_un_nombre
    notebooks/pp_exo_deviner_un_nombre_correction
    

A la fin des premières séances, on peut réfléchir à l'implémentation
d'un algorithme :

.. toctree::
    :maxdepth: 2

    notebooks/_gs1a_6_jaccard
    

Au terme de ces six séances, si la programmation est nouvelle pour vous ou
si le langage vous paraît encore peu naturel, 
je vous encourage à faire d'autres exercices comme 
piocher dans les anciens :ref:`l-examens`, à regarder la liste des exercices
proposées à `Quelques exercices du Project Euler <http://mathprepa.fr/python-project-euler-mpsi/>`_.
La plupart de ces notions font déjà partie du programme des classes préparatoires
scientifiques.



TD - Site web et pratiques logiciels
====================================   

Le langage Python est au programme des classes préparatoires scientifique
(`Prise en main du logiciel Python <https://www.ac-paris.fr/portail/jcms/p1_742307/prise-en-main-du-logiciel-python>`_)
et les étudiants ont déjà vu ou parcouru des exercices algorithmiques
(voir `MathPrepas, Programmation en Python <http://mathprepa.fr/python-project-euler-mpsi/>`_).
**Cette partie s'adesse essentiellement à ceux qui ont déjà programmé.**
On peut se pencher sur d'autres aspects logiciels tels que les 
tests unitaires, le templating, les sites Web, le scraping, encoding, les notebooks...

.. toctree::
    :maxdepth: 1

    specials/graphes
    specials/siteflask
    specials/unittest_coverage_git_profling
    notebooks/notebook_convert
    notebooks/jupyter_custom_magics

Deux exercices sont suggérés pour une séance de deux heures à choisir parmi :

#. Constuire un site web avec `Flask <http://flask.pocoo.org/>`_, 
   `Django <https://www.djangoproject.com/>`_ ou 
   `Falcon <https://falconframework.org/>`_
#. Ecrire un test unitaire pour un exercice d'une séance précédente
#. Appliquer une des méthodes décrites dans `Profiling <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/completion_profiling.html#completionprofilingrst>`_
   à un exercice d'une séance précédente
#. Constuire la documentation d'un module avec `Sphinx <http://www.sphinx-doc.org/en/stable/>`_
#. Implémenter une nouvelle commande magique sur Jupyter
#. Concevoir une campagne publicataire avec `Mako <http://www.makotemplates.org/>`_
   ou `Jinja2 <http://jinja.pocoo.org/docs/dev/>`_

.. todoext::
    :title: Ajouter un exercice sur le templating (jinja2, mako)
    :issue:
    :tag: plus

    Le templating fonction comme la fonction ``format`` et permet
    en plus de faire des répétitions. C'est très utiliser
    dans le domaine du web, notamment par `django <https://www.djangoproject.com/>`_.





TD - algorithmes
================

Ces séances sont centrées autour de l'utilisation de la programmation
pour un usage scientifique. On commence par les algorithmes et à la façon
d'écrire un algorithme efficace car le principal défaut des algorithmes
est leur lenteur. On a souvent des idées pour énumérer les solutions d'un problème 
et décrire les premières étapes avec les mains. Et puis, on se pose rapidement
la question : **Comment le faire rapidement ?**
Il y a deux questions qu'on doit se poser en premier pour entrevoir une solution. 

#. Peut-on réécrire le problème par **récurrence** ? 
   On aboutit le plus souvent à une solution issue de la programmation dynamique. 
   Le coût est **quadratique**.
#. Peut-on **couper le problème en deux**, construire une solution sur 
   chaque moitié puis recoller les solutions ? On procède de cette façon par dichotomie. 
   Le coût est **logarithmique**.

Ces deux façons de faire sont présentées durant trois séances à choisir parmi :

.. toctree::
    :maxdepth: 2
    
    notebooks/_gs1a_A_programmation_dynamique
    notebooks/_gs1a_A_arbre_trie
    notebooks/_gs1a_A_optimisation_contrainte
    notebooks/_gs1a_A_edit_distance
    notebooks/_gs1a_A_parcours_graphe
    
**Notes**    

La relecture du TD sur l'optimisation sous contrainte est conseillée 
à ceux qui souhaitent optimiser des portefeuilles d'actions.
Il est préférable d'avoir fait la séance sur la distance de Jaccard
avant de faire celle sur la distance d'édition. 
L'efficacité d'un algorithme est étroitement liée à la représentation des 
données choisies. Le `trie <https://fr.wikipedia.org/wiki/Trie_(informatique)>`_
en est l'illustration. 

.. toctree:: 
    :maxdepth: 2

    questions/question_2014

.. _l-entretiens:

**Entretiens d'embauche**

Les recruteurs testent de plus en plus votre capacité à programmer avec des exercices
où ils vérifient que vous savez écrire du code et comparer la vitesse de deux
algorithmes. Le plus souvent,
il existe une façon naïve d'arriver au résultat et il existe un algorithme plus rapide. 
Il y a deux grandes astuces pour aller plus vite :

* la programmation dynamique, son coût est en :math:`O(n^2)`,
* la dichotomie, son coût est en :math:`O(\ln_2 n)`.
    
Le tout est d'exprimer la solution en faisant apparaître l'un ou l'autre ou une 
combinaison des deux pour les problèmes 
les plus complexes.
La programmation dynamique apparaît souvent quand on considère la solution sous forme récurrente.
La dichotomie consiste à résoudre à couper l'ensemble de départ en deux, 
à résoudre le problème pour les deux sous-ensembles, 
puis à fusionner les deux solutions. Ce cela ne dépend pas du langage Python.
Pour vous exercer :

    
.. toctree::
    :maxdepth: 1

    notebooks/exercice_xn
    notebooks/exercice_echelle
    notebooks/exercice_morse
    notebooks/exercice_lcs
    notebooks/exercice_plus_grande_somme


TD - calcul matriciel, graphes, données
=======================================

Les quatre sujets importants des six dernières séances sont la programmation dynamique,
la dichotomie, les dataframe, les graphiques. La séance 9, la fin de la séance 
10 et la séance 11 ne sont pas indispensables et seront vus plus en détail l'année prochaine.
Toutefois, **la séance sur les dataframes propose des outils de manipulation et visualisation 
des données utiles pour tous les projets réalisés à l'école**.


Ces séances sont centrées sur les outils indispensables pour manipuler 
facilement les données et faire des calculs rapides.
Ces outils sont similaires à ceux qu'on trouve dans de nombreux languages à usage scientifique
(`R <http://www.r-project.org/>`_, `SciLab <http://www.scilab.org/fr>`_, 
`Julia <http://julialang.org/>`_, `Octave <http://www.gnu.org/software/octave/>`_, ...).
Ces trois séances peuvent paraître plus longues car elles s'appuient sur des modules qu'il faut découvrir 
puis utiliser pour résoudre des exercices. Toutefois, les modules 
`numpy <http://www.numpy.org/>`_, `pandas <http://pandas.pydata.org/>`_, `matplotlib <http://matplotlib.org/>`_
sont incontournables pour manipuler les données en Python.

.. toctree::
    :maxdepth: 2
    
    notebooks/_gs1a_D_dataframe_matrice
    notebooks/_gs1a_D_calcul_dicho_cython
    notebooks/_gs1a_D_visualisation
    
Il existe de nombreuses libraires de visualisation des données en Python et
elles se sont multipliées depuis l'avènement des notebooks :
`10 plotting libraries at PyData 2016 <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_.
La simulation du hasard est revient fréquemment pour éviter qu'un programme retourne toujours
les mêmes résultats. Voici quelques exemples :
    
.. toctree::
    :maxdepth: 1

    notebooks/code_multinomial
    


La dernière séance est une séance notée. Tous les documents sont autorisés. Quelques questions 
peuvent requérir l'utilisation des outils présentées durant les séances 9 à 12. Toutefois,
si tel était le cas, ce serait très proche d'une solution proposée lors des TD.


.. todoext::
    :title: ajouter un notebook sur flexx
    :issue: 13
    :tag: plus
    :date: 2016-08-04
    
    Voir blog post sur :ref:`Flexx <blog-post-flexx>`.
    



.. _l-td1a-start:

Getting started
===============

Il faut vous reporter à la section :ref:`l-installation-courte` pour installer python.        
Certaines séances pratiques utilisent des données depuis ce site. 
Elles sont facilement téléchargeables avec ces deux modules :

* `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_



.. _l-td1a-biblio:

Bibliographie
=============

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
* `Questions Fréquentes <https://docs.python.org/3/faq/index.html>`_
* :ref:`l-FAQs`
* :ref:`l-glossary`
* :ref:`l-questions`
* `Débugger en Python <http://www.xavierdupre.fr/blog/2014-06-02_nojs.html>`_
* `Modules standards <https://docs.python.org/3/library/>`_
* `8 Regular Expressions You Should Know <http://code.tutsplus.com/tutorials/8-regular-expressions-you-should-know--net-6149>`_ *(2016/03)*
* `Love Python <http://love-python.blogspot.fr/>`_ *(2016/03)*
* `The Hitchhiker's Guide to Python! <http://docs.python-guide.org/en/latest/>`_ *(2016/06)*

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
* `Python cours et TPs <http://mathcpge.org/index.php?option=com_content&view=article&id=55&Itemid=146>`_ *(2016/04)*
* `Le Python en prépas <http://web.isen-bretagne.fr/livres/python/>`_ (2016/04)
* `Algorithmique et programmation en CPGE <http://python-liesse.enseeiht.fr/cours/index.html>`_ *(2016/04)*

**Exercices et jeux**

* `codingame <http://www.codingame.com/>`_
* `Quelques exercices du Project Euler <http://mathprepa.fr/python-project-euler-mpsi/>`_ *(2016/04)*
* `Countdown to 2016 <http://nbviewer.jupyter.org/url/norvig.com/ipython/Countdown.ipynb>`_ *(2016/08)*
* `The Convex Hull Problem <http://nbviewer.jupyter.org/url/norvig.com/ipython/Convex%20Hull.ipynb>`_ *(2016/08)*

**MOOC**

* `Code Academy Python <http://www.codecademy.com/tracks/python>`_ (utilise Python 2.7)
* `Un premier Mooc Inria sur Python <https://www.france-universite-numerique-mooc.fr/courses/inria/41001/Trimestre_4_2014/about>`_
* `pyvideo.org <http://pyvideo.org/>`_

**Outils**

* `PythonTutor <http://pythontutor.com/>`_ : pour suivre pas à pas l'exécution d'un programme (petit)


.. todoext::
    :title: insister plus sur les algorithmes numériques pour les 1A écos
    :issue: 8
    :tag: plus
    :date: 2016-06-24
    
    Les étudiants souhaiteraient passer plus de temps au premier semestre sur 
    la partie dédiées aux algorithmes pour être mieux préparés au second semestre
    lors de la réalisation des projets.
    




    