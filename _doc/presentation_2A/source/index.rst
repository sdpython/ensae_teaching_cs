
ENSAE 2A - Programmation
========================

.. revealjs:: ENSAE 2A - Données, Machine Learning et Programmation
    :data-background: #DDDDDD

    .. image:: _static/project_ico.png

    Antoine Thabault -
    Nicolas Rousset -
    Jérémie Jakubowicz -
    `Xavier Dupré <http://www.xavierdupre.fr/>`_ 

    **Assistant à l'ENSAE**
    
    `Romain Lesauvage <mailto: romain.lesauvage AT ensae.fr>`_
        
        
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Déroulement du cours 
    
            * 6 séances de 4h
            * 1 projet

        **Plan complet**
        
        `séances <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a.html>`_
        
        De lundi 21 septembre au lundi 2 novembre 
        (excepté le 26 Octobre) de 8h30 à 13h.
        
        Deux suivis de projets sont prévus en fin de semestre.

    .. revealjs:: Objectifs du cours
    
        * Passer moins de temps à manipuler les données
        * Passer plus de temps à les modéliser
        * Connaître les outils pour être agile
        * Savoir faire rapidement une étude statistique simple
        * Avoir les moyens de se débrouiller en toute circonstance
        
    .. revealjs:: Notebooks
    
        Le cours utilise les `notebooks <http://ipython.org/notebook.html>`_.
        
        .. image:: _static/notsnap.png       

        La plupart des exemples sur Internet sont disponibles sous cette forme.
        
    .. revealjs:: Le langage Python et Machine Learning
    
        Pourquoi ?

        * Le langage est open source et donc gratuit.
        * Il fonctionne sur tous les OS (Windows, Linux, Mac, bientôt `IPad <http://computableapp.com/>`_).
        * Il dispose de nombreuses extensions, il peut tout faire.
        * Il est devenu une alternative intéressante pour un statisticien depuis 2013 et quelques modules :
            * `pandas <http://pandas.pydata.org/>`_, `ipython <http://ipython.org/>`_, `matplotlib <http://matplotlib.org/>`_
            * `numpy <http://www.numpy.org/>`_, `scikit-learn <http://scikit-learn.org/stable/>`_, `statsmodels <http://statsmodels.sourceforge.net/devel/index.html>`_
        * Les notebooks se répandent à grande vitesse : `A gallery of interesting IPython Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_.
        
    .. revealjs:: Liens

        * `Contenu du cours <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a.html>`_
        * `Blog <http://www.xavierdupre.fr/blog/xd_blog_nojs.html>`_
        * `Bibliographie <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/biblio.html>`_
        * `Installer Python pour faire des statistiques <http://www.xavierdupre.fr/blog/2014-02-26_nojs.html>`_
        * `Python pour un Data Scientist <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/data2a.html>`_
        * `Modules et outils pour développer <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/manytools.html>`_
        * `Coding Party à l'ENSAE <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/coding_party.html>`_
        * `Evénements, ressources <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/ressources.html>`_

    .. revealjs:: Contributions

        Le contenu est disponible sur `GitHub <https://github.com/>`_ :
        
            * `ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs/>`_
            
        Autres modules :
        
            * `pyensae <https://github.com/sdpython/pyensae/>`_
            * `pyquickhelper <https://github.com/sdpython/pyquickhelper/>`_
            * `pymyinstall <https://github.com/sdpython/pymyinstall/>`_        
            
        Vous pouvez participer.
        
.. revealjs:: Environnement de travail
    :data-background: #DDDDFF    
    
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Python à l'ENSAE

        * Le système d'exploitation est Windows.
        * L'environnement est installé pour vous (`WinPython <http://winpython.sourceforge.net/>`_)
        * Vous pouvez le recopier tel quel chez vous (avec un clé USB).
        
    .. revealjs:: Python chez vous

        * Le système d'exploitation est celui que vous choisissez (Windows, Linux, Mac).
            * Windows : l'école vous fournit un setup
            * Linux/Mac : Anaconda + une liste de modules à Installer
        * Lire `Prérequis et installation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html#prerequis-et-installation>`_.
        * Vous devriez avoir installé Python dès les premières séances.
        
    .. revealjs:: Version de Python
    
        * Le cours est construit pour la version 3.4+.
        * Les exemples ne marcheront pas tous sur la version 2.7.
        * Il faut choisir la version *amd64*. C'est la seule capable de tirer parti d'une mémoire de plus de 4 Go.
        
    .. revealjs:: Notebook
    
            * Ils mélangent code, texte, formules, tableaux, graphiques.
            * Ils sont convertibles au format HTML, Latex.
            * Ils sont pratiques pour garder la trace d'une série de petites étapes pour une étude scientifique.
            * Ils ne sont pas pratiques pour écrire de longs programmes.
            * Ils sont très utilisés, plein d'exemples sur Internet
        
    .. revealjs:: Editeur 
    
        On n'écrit pas de modules ou de grands programmes dans un notebook. Il faut un éditeur.
        Il existe de nombreuses options :
            
            * `éditeurs, outils <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/devtools.html#l-devtools>`_
        
        La version gratuite de `PyCharm <http://www.jetbrains.com/pycharm/>`_ contient tout ce qu'il faut.
        Il détecte quelques erreurs avant l'exécution.
        Il existe aussi `WingIDE <https://wingware.com/>`_.
        
    .. revealjs:: Environnement scientifique

        * `Spyder <http://pythonhosted.org//spyder/>`_ (`Python <https://www.python.org/>`_) équivalent de `RStudio <http://www.rstudio.com/>`_ (`R <http://www.r-project.org/>`_)
        * 4 fenêtres
            * script
            * command line
            * explorateur de données
            * graphiques
        
    .. revealjs:: Démo
    
        * Editeur de texte : **Scite**
        * Environnement mathématique : **Spyder**
        * Notebooks : **IPython/Notebooks**
        
        Et des éditeurs plus complets :
        
        * `PyCharm <http://www.jetbrains.com/pycharm/>`_
        * `PyTools <http://pytools.codeplex.com/>`_ 
        
.. revealjs:: Contenu
    :data-background: #DDDDFF
    
    * Manipuler les données
    * Calcul matriciel
    * Calcul distribué
    * Visualisation
    * Machine learning
    * Algorithmie
    
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Manipuler les données
    
        * Importer/Exporter des données en différents formats
        * Fusionner, filter, grouper
        * Echantillonner
        
        ...
        
        **Module de référence**
        
        * `pandas <http://pandas.pydata.org/>`_
    
    .. revealjs:: Calcul matriciel
    
        * Plus de choses en moins de lignes et plus rapides.    
        * Python a de `bonnes performances <http://julialang.org/benchmarks/>`_
        
        ...
        
        **Module de référence**
        
        `numpy <http://www.numpy.org/>`_ 
    
    .. revealjs:: Calcul distribué
    
        * distribuer pour aller plus vite
        * CPU - sur plusieurs machines ou threads (avec IPython)
        * GPU - Monte Carlo - *non abordé cette année*
        
        ...
        
        **Module de référence**
        
        `dask <http://dask.pydata.org/en/latest/>`_
    
    .. revealjs:: Visualisation
        
        * De moins en moins de tableaux
        * De plus en plus de graphiques.    
        * De plus en plus interactifs.
        
        ...
        
        **Module de référence**
        
        * `matplotlib <http://matplotlib.org/>`_
    
    .. revealjs:: Machine Learning, Statistiques
    
        * Statistiques descriptives
        * Clustering
        * Apprentissage statistique
    
        ...
    
        **Module de référence**
    
        * `scikit-learn <http://scikit-learn.org/stable/>`_, `statsmodels <http://statsmodels.sourceforge.net/devel/index.html>`_
        
        Gaël Varoquaux (`INRIA <http://www.inria.fr/>`_) viendra présenter ce module en tant que principal contributeur le 6 Octobre à 11h.
    
    .. revealjs:: Algorithmie
    
        * Manipuler 100 millions de lignes requiert d'être astucieux
        * Cas récurrents :
            * joindre deux sources de données
            * grouper, trier dans le bon ordre sans perdre du temps
        * Porte d'entrée aux entretiens d'embauche dans les startups
    
        ...
    
        **Module de référence**
        
        Vous
    
.. revealjs:: Les données comme terrain de jeu
    :data-background: #DDDDFF
        
.. revealjs:: 
    :data-background: #DDDDDD
        
    .. revealjs:: Se cultiver, être inventif
    
        * Assembler les méthodes, modèles
        * Mélanger les genres (statistiques, recherche opérationnelle)
        * Ne pas être limité par les outils
        
        ...
        
        **Exemple :** Je ne sais jamais où mettre les accents dans un mot.
        Je veux écrire une fonction qui les corrige automatiquement ?
        
        
    .. revealjs:: Customiser son outil

        * Tout faire depuis un notebook
        * `R et notebooks <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/python_r.html>`_
        * `Custom Magics for IPython <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/ipython_custom_magics.html>`_
    
    .. revealjs:: Ordres de grandeur
    
            +--------------------+-------------------------------+--------------------------+
            | Ordre de grandeur  | Outil / Langage               | Algorithme               |
            | (observations)     | principal                     | raisonnable              |
            +====================+===============================+==========================+
            | < 50000            | Excel                         | ``O(n^a)``               |
            +--------------------+-------------------------------+--------------------------+
            | < 10 millions      | Python, R                     | ``O(n (ln n)^a)``        |
            +--------------------+-------------------------------+--------------------------+
            | < 1 milliard       | SQL, Python                   | ``O(n ln n)``            |
            +--------------------+-------------------------------+--------------------------+
            | > 200 millions     | Cluster (Map/Reduce), Python  | ``O(n ln n)`` distribué  |
            +--------------------+-------------------------------+--------------------------+
            
            ...
            
            Astucieux ou très (très) patient. A vous de choisir.
            
.. revealjs:: Légalement...
    :data-background: #DDDDFF
    
.. revealjs::    
    :data-background: #DDDDDD

    .. revealjs:: Droits et données

        * Restrictions
            * Les données sont associées à une license.
            * Elle détermine ce qu'on peut en faire.
            * L'usage est parfois limité dans le temps.        
        * Anonymisation
            * Les données sont le plus souvent anonymisées (identifiant illisible)
            * On sait beaucoup de choses sur ces anonymes (ensemble des achats, requêtes, trajets web)
    
    .. revealjs:: Fuites possibles
    
        * Technologies web : savoir quand on fait appel à un service extérieur
            * cartographie
            * formules
        * Oublis du quotidien
            * Petits échantillons qui trainent sur le disque dur
            * Résultats expérimentaux qu'on garde
            * Résilience des mails
            * Vol de portable
        

.. revealjs:: 
    :data-background: #DDDDDD
    
        `Séance 1 : données et graphes en quelques lignes <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/td2a_cenonce_session_1.html>`_
        
        DataFrame, Matplotlib
        
        A vous.

        
    

