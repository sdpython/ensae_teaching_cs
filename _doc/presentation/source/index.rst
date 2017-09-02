
ENSAE 1A - Programmation
========================

.. revealjs:: ENSAE 1A - Programmation

    .. image:: _static/project_ico.png

    `Xavier Dupré <http://www.xavierdupre.fr/>`_ (1999)

    `Python <https://www.python.org/>`_ a été choisi comme langage en 2005 à l'ENSAE.

.. revealjs:: Algorithme ?

.. revealjs::

    .. revealjs:: Trois concepts en algorithmie

        * la séquence
        * le test
        * la boucle

    .. revealjs:: Une bille tombe où va-t-elle ?

        .. image:: _static/bille.png

    .. revealjs:: Décrire le chemin de la bille ?

        .. image:: _static/bille.png
            :width: 200px

        * avec les trois concepts
        * le plus succintement possible

.. revealjs::

    .. revealjs:: Objectifs du cours

        Deux profils

        * Interpréter les données - data scientist / analyste
        * Optimiser avec les données - data scientist / ingénieur

    .. revealjs:: data scientist / analyste

        Les données servent à comprendre. Les calculs sont moins
        importants qu'une bonne représentation d'un phénomène
        qu'on cherche à expliquer.

        * Les bases du langage *Python*
        * Expressions régulières
        * Quelques algorithmes classiques
        * Les dataframes, les graphes.

    .. revealjs:: data scientist / ingénieur

        Les données servent à améliorer un processus de décision
        quitte à ne plus comprendre comment les variables sont assemblées
        pour prendre cette décision.

        * Culture algorithmique, pratique régulière
        * Notion de graphes.
        * Le calcul matriciel, les dataframes, les graphes.

    .. revealjs:: Semestre 1

        Cours / TD : `apprendre <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_1a.html>`_

        Organisés par groupes de TD, contenu en fonction de votre objectif
        et de vos connaissances.

    .. revealjs:: Semestre 2

        Projet informatique : devenir autonome

        * `base de sujets <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/projet_info_1A.html>`_
          à adapter selon vos envies
        * votre sujet est le bienvenu
        * ingéniérie logicielle

.. revealjs::

    .. revealjs:: Le langage Python

        Pourquoi ?

        * Open source
        * Windows, Linux, Mac...
        * Tout terrain (calcul scientifique, programmation, web, jeux).
        * Simple, utilisé partout
        * Obligatoire pour un data scientist

    .. revealjs:: Startup et programmation

        De plus en plus nombreux chaque année.

        Toujours un site web, souvent des traitements de données...

    .. revealjs:: Les difficultés de l'apprentissage

        * La programmation est **abstraite**.
          Il n'existe pas de façon évidente de représenter un algorithme ou un raisonnement.
        * Les programmes sont un **long empilement de choses simples**.
          L'objectif est souvent simple à résumer, la méthode moins.
        * Il existe beaucoup de bonnes pratiques qu'on adopte souvent après avoir fait le contraire.
          On ne programme pas de la même façon après le projet informatique.
          **Faire des erreurs, c'est apprendre.**

    .. revealjs:: L'image d'un bug

        .. image:: _static/bug.png

    .. revealjs:: Utiliser Internet

        Quand on ne sait pas, il suffit d'utiliser un moteur de recherche et de chercher :

            python + question

        *en anglais de préférence*

        Example :  `python syntax loop <https://duckduckgo.com/?q=python+syntax+loop>`_

    .. revealjs:: Notebooks

        Le cours utilise principalement les `notebooks <http://jupyter.org/notebook.html>`_.

        .. image:: _static/notsnap.png

        Plutôt fun. Retours positifs des années précédentes.
        La plupart des exposés utilisent ce support lors des conférences.

    .. revealjs:: Autre option : Scite

        `Scite <http://www.scintilla.org/SciTE.html>`_

        .. image:: _static/scite.png

    .. revealjs:: Autre option : Spyder

        `Spyder <https://pythonhosted.org/spyder/>`_

        .. image:: _static/spyder.png

    .. revealjs:: Autre option : IDE

        `PTVS <https://github.com/Microsoft/PTVS>`_, `PyCharm <https://www.jetbrains.com/pycharm/>`_

        .. image:: https://msdnshared.blob.core.windows.net/media/MSDNBlogsFS/prod.evol.blogs.msdn.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/01/29/92/metablogapi/7840.Startertemplatestobuildwebsitesusingpopularframeworks_44FA9070.png

    .. revealjs:: Autres langages

        Le langage informatique majoritaire est différent selon  la filière.

        * `C++ <http://fr.wikipedia.org/wiki/C%2B%2B>`_, `C <http://fr.wikipedia.org/wiki/C_(langage)>`_ : finance (2A)
        * `C# <http://fr.wikipedia.org/wiki/C_sharp>`_ : finance, actuariat, les nouveaux projets démarrent plus souvent en C# qu'en C++ (3A)
        * `java <http://fr.wikipedia.org/wiki/Java_(langage)>`_ : Big Data, calcul distribué poussé (3A)
        * `Python <https://www.python.org/>`_ : web, startup, machine learning, ... (1A, 2A, 3A)
        * `javascript <http://fr.wikipedia.org/wiki/JavaScript>`_ : application web, internet
        * `R <http://www.r-project.org/>`_ : recherche, actuariat, statistiques... (1A)
        * `Spark SQL <http://spark.apache.org/sql/>`_ : bientôt partout (3A)
        * `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_ : partout (1A)

    .. revealjs:: D'autres langages

        Liste non exhaustive :

        * `Clojure <http://fr.wikipedia.org/wiki/Clojure>`_ : langage fonctionnel
        * `Erlang <http://fr.wikipedia.org/wiki/Erlang_(langage)>`_ : message facebook, service internet ne pouvant pas s'arrêter
        * `Go <https://golang.org/>`_ : Google
        * `HTML <http://fr.wikipedia.org/wiki/Hypertext_Markup_Language>`_ : internet (pas vraiment un langage)
        * `Objective-C <http://fr.wikipedia.org/wiki/Objective-C>`_ : application iPhone
        * `Scala <http://fr.wikipedia.org/wiki/Scala_(langage)>`_ : langage fonctionnel, voir `Spark <https://spark.apache.org/>`_ (3A)
        * `Ruby <https://www.ruby-lang.org/fr/>`_ : site web
        * `SAS <http://www.sas.com/offices/europe/france/>`_ : actuariat, grosses entreprises (1A)
        * `VBA <http://fr.wikipedia.org/wiki/Visual_Basic_for_Applications>`_ : Excel (et quand on n'a pas le choix) (2A)

.. revealjs::

    .. revealjs:: Support / Matériel

        * `Python dans tous ses états <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_
        * `Apprendre la programmation avec Python <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/index.html>`_
        * `Les maths d'abord, la programmation ensuite <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/index.html>`_
        * `Jeux algorithmiques pour petits et grands <http://lesenfantscodaient.fr/>`_

    .. revealjs:: Contributions

        Le contenu est disponible sur `GitHub <https://github.com/sdpython>`_ :

        * `ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs/>`_
        * `autres modules <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/ci_status.html>`_

        .. image:: _static/fork.png

        .. image:: _static/edit.png

    .. revealjs:: Jeux algorithmes

        Dans un certain pays, il existe un parti politique pétri d'inimitiés tenaces.
        Est-il possible de scinder le parti en deux pour que chaque paire d'ennemis
        intangibles se retrouve de part et d'autres du fossé ?

        Cette devinette algorithmique est tirée d'une compétition
        `google code jam <https://code.google.com/codejam/contest/6234486/dashboard#s=p0>`_.

        .. image:: http://static.fnac-static.com/multimedia/FR/Images_Produits/FR/fnac.com/Visual_Principal_340/2/0/0/9782864970002.jpg
            :width: 200

    .. revealjs:: Hackathon

        `Hackathon EY/ENSAE 2016 <https://www.youtube.com/watch?v=vSchPGmtikI>`_

        avec `La Croix-Rouge <http://www.croix-rouge.fr/>`_
        et `Crésus <https://www.cresus-iledefrance.org/>`_.

        C'est un hackathon pour **apprendre**.

    .. revealjs:: Trois questions

        * Quel est votre objectif ?  (analyste / ingénieur)
        * Avez-vous déjà programmé ? (Non, Oui)
        * Choisissez un groupe : A1, A2, I1, I2.

    .. revealjs:: Exercices

        Récupérer les données vélib et prédire l'affluence des vélos à une station ?

        Comment feriez-vous ?

.. revealjs:: Plan fin de séance

    * `Installation de Python sur vos machines <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/i_getting_started.html#l-installation-courte>`_
    * `Outils spécifiques à ce cours <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/ci_status.html>`_
    * Organisation des séances et contenus proposés
    * Algorithme et créativité
    * Pas de par coeur
    * Rappel de syntaxe : décoder un programme simple
