
ENSAE 1A - Programmation
========================

.. revealjs:: ENSAE 1A - Programmation
    :data-background: #DDDDDD

    .. image:: _static/project_ico.png
        
    `Xavier Dupré <http://www.xavierdupre.fr/>`_ (1999)
    
    Python a été choisi comme langage en 2005 à l'ENSAE.
    
    **Assistant à l'ENSAE**
    
    `Romain Lesauvage <mailto: romain.lesauvage AT ensae.fr>`_
        
.. revealjs:: Intervenants
    :data-background: #DDDDDD

    **Professeur**
    
        * **site :** `Xavier Dupré <http://www.xavierdupre.fr/>`_ 
        * **mail :** `xavier.dupre AT ensae.fr <mailto:xavier.dupre AT ensae.fr>`_

    **Chargés de TD**

        +-------------------------------------------------------+-----------------------------------------------------------------------------------+
        | Xavier Dupré                                          | `xavier.dupre AT ensae.fr <mailto:xavier.dupre AT ensae.fr>`_                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------+
        | Emmanuel Guérin                                       | `emmanuel AT guerin.fr.eu.org <mailto:emmanuel AT guerin.fr.eu.org>`_             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------+
        | Arnaud de Myttenaere                                  | `arnaud.de.myttenaere AT ensae.fr <mailto:Arnaud.De.Myttenaere AT ensae.fr>`_     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------+
        | Edwin Grappin                                         | `edwin.grappin AT ensae.fr <mailto:edwin.grappin AT ensae.fr>`_                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------+
        | Yves Gerey                                            | `ggereyy AT gmail.com <mailto:ggereyy@gmail.com>`_                                |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------+
        | ...                                                   | ...                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------+
        
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Semestre 1 
    
        Cette partie est obligatoire.
    
            * 6 séances d'initiation à la programmation
            * 3 séances sur 3 algorithmes classiques
            * 3 séances sur des outils pour manipuler des données
            * 1 séance notée

        **Plan complet**
        
        `séance <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_1a.html#l-td1a>`_
        
        Du vendredi 4 septembre au vendredi 5 décembre excepté le 19/09 et le 31/10, 16h30.

    .. revealjs:: Semestre 2
    
        - Cette partie est facultative.
    
            * `sujets <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/projet_info.html#l-projinfo>`_
            * votre sujet est le bienvenu.
            
        - Le projet permet de découvrir :
        
            * le travail de façon plus autonome
            * le travail collectif
            
        - C'est l'occasion de s'exercer sur un sujet qui vous plaît.


    .. revealjs:: Evaluation
    
        * Semetre 1 (obligatoire)
            * 3 interrogations écrites de 20 minutes sur 5 points
            * 1 séance notée sur 20 points
        * Semestre 2 (facultatif)
            * 1 projet informatique de 1 ou 2 élèves évalué avec :
                * un programme
                * un rapport
                * une soutenance
            * Le projet doit inclure une partie mathématique, statistique ou économique
            * `Barême indicatif <http://www.xavierdupre.fr/site2013/enseignements/bareme-2014.html>`_
    
    .. revealjs:: Notebooks
    
        Le cours utilise les `notebooks <http://ipython.org/notebook.html>`_.
        
        .. image:: _static/notsnap.png        
        
        Plutôt fun. A vous de me dire.
        
    .. revealjs:: Liens

        * `Contenu du cours <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_ (rendu `2 <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx2/index.html>`_ et `3 <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_)
        * `Blog <http://www.xavierdupre.fr/blog/xd_blog_nojs.html>`_
        * `Bibliographie <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/biblio.html>`_
        * `Apprentissage de la programmation <http://inforef.be/swi/python.htm>`_ de Gérard Swinnen
        * `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
        * `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_
        * `xavierdupre.fr <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_

.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Le langage Python
    
        Pourquoi ?

        * Le langage est open source et donc gratuit.
        * Il fonctionne sur toutes les OS (Windows, Linux, Mac).
        * Il dispose de nombreuses extensions.
        * Il permet de nombreux usages (calcul scientifique, programmation, web, jeux).
        * Sa syntaxe est l'une des plus simples.
        * Il est en pleine expansion.
        
    .. revealjs:: Data Scientist
    
        `Data Science en exemples <http://datascience.net/fr/challenge>`_ 

        * `R <http://www.r-project.org/>`_ est le langage des chercheurs.
        * `Python <https://www.python.org/>`_ a rattrapé une bonne partie de son retard depuis 2012.
        * Python est très actif.
        * voir `Python pour un Data Scientist <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/data2a.html>`_
        
    .. revealjs:: Les difficultés de l'apprentissage
    
        * La programmation est abstraite. 
        * Il n'existe pas de façon évidente de représenter un algorithme ou un raisonnement.
        * Les programmes sont un long empilement de choses simples. 
        * L'objectif est souvent simple à résumer, la méthode moins.
        * Il existe beaucoup de bonnes pratiques qu'on adopte souvent après avoir fait le contraire.
        * On ne programme pas de la même façon après le projet informatique.
        
    .. revealjs:: Les supports de cours
    
        * `Les énoncés des séances <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_1a.html>`_
        * `Examples de code <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/exemple_index.html>`_
        * `Résumé de la syntaxe Python <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_
        * `FAQ <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/all_FAQ.html>`_
        * `Examens passés <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/exams.html>`_
        
    .. revealjs:: Pour aller plus loin
    
        * `Coding Party à l'ENSAE <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/coding_party.html>`_
        * `Modules et outils pour développer <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/manytools.html>`_
        * `Articles, Références, Blogs <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/biblio.html>`_
        * `Données, Machine Learning et Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a.html>`_ (2A)

.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Python à l'ENSAE

        * Le système d'exploitation est Windows.
        * L'environnement est installé pour vous (`WinPython <http://winpython.sourceforge.net/>`_)
        * Vous pouvez le recopier tel quel chez vous (avec un clé USB).
        
    .. revealjs:: Python chez vous

        * Le système d'exploitation est celui que vous choisissez (Windows, Linux, Mac).
        * Vous installez votre environement (amenez votre ordinateur portable en TD en cas de problème).
        * Lire `Prérequis et installation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html#prerequis-et-installation>`_.
        * Vous devriez avoir installé Python dès les premières séances.
        
    .. revealjs:: Version de Python
    
        * Le cours est construit pour la version 3.3+.
        * Les exemples ne marcheront pas tous sur la version 2.7.
        * Il faut choisir la version *amd64*. C'est la seule capable de tirer parti d'une mémoire de plus de 4 Go.
        
    .. revealjs:: Utiliser Internet
    
        Quand on ne sait pas, il suffit d'utiliser un moteur de recherche et de chercher :
        
            python + question
            
        *en anglais de préférence*
            
        Example :  `python syntax loop <https://duckduckgo.com/?q=python+syntax+loop>`_        
        
    .. revealjs:: Notebook
    
            * Ils mélangent code, texte, formules, tableaux, graphiques.
            * Ils sont convertibles au format HTML, Latex.
            
            * Ils sont pratiques pour garder la trace d'une série de petites étapes pour une étude scientifique.
            * Ils ne sont pas pratiques pour écrire de longs programmes.

        
    .. revealjs:: Editeur 
    
        On n'écrit pas de modules ou de grands programmes dans un notebook. Il faut un éditeur.
        Il existe de nombreuses options :
            
            * `éditeurs, outils <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/devtools.html#l-devtools>`_
        
        La version gratuite de `PyCharm <http://www.jetbrains.com/pycharm/>`_ contient tout ce qu'il faut.
        Il détecte quelques erreurs avant l'exécution.
        
    .. revealjs:: Démo
    
        * Editeur de texte : **Scite**
        * Environnement mathématique : **Spyder**
        * Notebooks : **IPython/Notebooks**
        
        Et des éditeurs plus complets :
        
        * `PyCharm <http://www.jetbrains.com/pycharm/>`_
        * `PyTools <http://pytools.codeplex.com/>`_ 
        
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Les langages à l'ENSAE
        
        Le langage informatique majoritaire est différent selon  la filière.
        
        * `C++ <http://fr.wikipedia.org/wiki/C%2B%2B>`_, `C <http://fr.wikipedia.org/wiki/C_(langage)>`_ : finance (2A)
        * `C# <http://fr.wikipedia.org/wiki/C_sharp>`_ : finance, actuariat, les nouveaux projets démarrent plus souvent en C# qu'en C++ (3A)
        * `java <http://fr.wikipedia.org/wiki/Java_(langage)>`_ : Big Data, calcul distribué poussé (3A)
        * `PIG <http://pig.apache.org/>`_ : Big Data, Map Reduce, calcul distribué (3A)
        * `R <http://www.r-project.org/>`_ : recherche, actuariat, statistiques... (1A)
        * `SAS <http://www.sas.com/offices/europe/france/>`_ : actuariat, grosses entreprises (1A)
        * `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_ : partout (1A)
        * `VBA <http://fr.wikipedia.org/wiki/Visual_Basic_for_Applications>`_ : Excel (et quand on n'a pas le choix) (2A)
        * `Python <https://www.python.org/>`_ : web, startup, machine learning, ... (1A, 2A, 3A)

    .. revealjs:: D'autres langages
    
        Liste non exhaustive :
        
        * `Clojure <http://fr.wikipedia.org/wiki/Clojure>`_ : langage fonctionnel
        * `Erlang <http://fr.wikipedia.org/wiki/Erlang_(langage)>`_ : message facebook, service internet ne pouvant pas s'arrêter
        * `HTML <http://fr.wikipedia.org/wiki/Hypertext_Markup_Language>`_ : internet (pas vraiment un langage)
        * `javascript <http://fr.wikipedia.org/wiki/JavaScript>`_ : application web, internet
        * `Objective-C <http://fr.wikipedia.org/wiki/Objective-C>`_ : application iPhone
        * `Scala <http://fr.wikipedia.org/wiki/Scala_(langage)>`_ : langage fonctionnel, voir `Spark <https://spark.apache.org/>`_ (3A)

    .. revealjs:: Contributions

        Le contenu est disponible sur `GitHub <https://github.com/>`_ :
        
            * `ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs/>`_
            
        Autres modules :
        
            * `pyensae <https://github.com/sdpython/pyensae/>`_
            * `pyquickhelper <https://github.com/sdpython/pyquickhelper/>`_
            * `pymyinstall <https://github.com/sdpython/pymyinstall/>`_        
            
        Vous pouvez participer.

.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Evaluer votre niveau (1)
    
        * Avez-vous un ordinateur portable ?
        * Avez-vous essayé de résoudre les énigmes mathématiques proposées par Cédric Villani dans Le Monde ?
        * Votre grand-mère souhaite avoir une liste de montants en livres convertis en anciens francs (1£, 2£, 5£, 10£, ...). Elle a peur de trop dépenser.
            a. Vous prenez une feuille blanche, une calculatrice et un stylo.
            b. Vous ouvrez Excel.
            c. Vous codez un programme qui le fait pour toutes les devises.
            d. Vous montez une startup pour fabriquer des tie-shirt avec le cours du jour pour toutes les grand-mères du monde.
            
    .. revealjs:: Evaluer votre niveau (2)

        * Pensez-vous que la programmation requiert de l'imagination ?
        * Avez-vous déjà programmé ? 
            * Si oui, en quel langage ? (compilé, interprêté, fonctionnel)
            * Si non, seriez-vous prêt à participer à un `coding goûter <http://codinggouter.org/>`_ ?
        * Préférez-vous le clavier AZERTY ou QWERTY ?
        
        *Répartition...*

    .. revealjs:: Lectures

        * `Résumé de la syntaxe Python en 27 pages <http://www.xavierdupre.fr/site2013/documents/python/resume_utile.pdf>`_ (PDF)
        * `Apprentissage de la programmation <http://inforef.be/swi/python.htm>`_ (*Gérard Swinnen*) Le livre est mis à jour de façon régulière au gré des évolutions du langages, c'est un des rares livres à survivre d'années en années.
        * `Théorème vivant <http://grasset.fr/theoreme-vivant-9782246798828>`_ de Cédric Villani 
        
    .. revealjs:: Demain
        
        * On sera connecté en permanence.
        * On sera entouré de capteurs (voir `HealthKit <https://developer.apple.com/healthkit/>`_)
        * Les données n'attendent que vous.
        * `Evénements, ressources <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/ressources.html>`_
    
        ...

        * `Quelle France dans dix ans ? Les chantiers de la décennie <http://www.strategie.gouv.fr/sites/strategie.gouv.fr/files/archives/F10_Rapport_FINAL_23062014.pdf>`_
        * `Quel sera le paysage Média en 2020 ? <http://www.udecam.fr/docs_paysagemedia/Paysage%20Media%202020%20-%203eme%20edition%20-UDECAM%202014.pdf>`_

    .. revealjs:: Et pour finir: The Bug
        
        Un `bug <http://fr.wikipedia.org/wiki/Bug_(informatique)>`_, c'est tout ce qui sépare
        votre idée de votre programme. 
        
        La première est parfaite, le second l'est moins.
        
        **Que faire ?**
        
        * fuire
        * demander de l'aide au prof
        * réciter une incantation magique
        * chercher la cause ?
        
    .. revealjs:: L'image d'un bug
                
        .. image:: _static/bug.png
