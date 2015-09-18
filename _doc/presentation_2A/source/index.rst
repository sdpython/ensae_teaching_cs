
ENSAE 2A - Programmation
========================

.. revealjs:: ENSAE 2A - Python pour un Data Scientist

    .. image:: _static/project_ico.png

    Antoine Thabault -
    Nicolas Rousset -
    Jérémie Jakubowicz -
    `Xavier Dupré <http://www.xavierdupre.fr/>`_ 

    **Assistant à l'ENSAE**
    
    `Romain Lesauvage <mailto: romain.lesauvage AT ensae.fr>`_
    
.. revealjs:: 
    
    .. revealjs:: Intervenants

            **site, cours** `Xavier Dupré <http://www.xavierdupre.fr/>`_

        * `Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_  (ENSAE 1999)
        * Elodie Royant (ENSAE 2008)
        * Antoine Thabault (ENSAE 2012)
        * Jérémie Jakubowicz (ENSAE 2002)
        * Nicolas Pousset
        * Antoine Ly (ENSAE 2015)
        * Dominique Poudevigne
        * Gaël Varoquaux
        
    .. revealjs:: Bio 1/3
    
        **Elodie Royant** a travaillé 6 ans chez `MAPP <http://www.mapp-economics.com/fr/>`_, 
        un cabinet d’expertise en économie de la concurrence. Elle est actuellement Data Scientist chez `Oscaro.com <http://www.oscaro.com/>`_,
        un e-commerçant spécialisé dans la ventes de pièces détachées pour voiture. 
        Elle est en charge de l'optimisation de l'acquisition de trafic sur le site (payant et gratuit) 
        et de la mesure des actions marketing.
    
        **Antoine Thabault** a travaillé pendant 3 ans en finance, en particulier sur des problématiques 
        de trading algorithmique et de trading haute fréquence. Il est actuellement Data Scientist chez 
        `AlephD <https://www.alephd.com/>`_, 
        une start-up française qui aide les éditeurs de contenu en ligne à vendre efficacement leurs espaces 
        publicitaires dans le cadre d'enchères en temps réel.
        
    .. revealjs:: Bio 2/3
    
        **Jérémie Jakubowicz** est chercheur et professeur à l'ENSAE et à Télécom SudParis.
        Il publie dans le domaine des statistiques, du traitement du signal et des images.
        
        **Xavier Dupré** est ingénieur chez Microsoft et professeur à l'ENSAE.
        
        ** Nicolas Pousset** 
    
    .. revealjs:: Bio 3/3
    
        **Anoine Ly**
        
        ** Dominique Poudevigne**
        
        **Gaël Varoquaux**
    
    
        
        
.. revealjs:: 

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
    
        Le cours utilise les `notebooks <https://jupyter.org/>`_.
        
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
            * `actuariat_python <https://github.com/sdpython/actuariat_python/>`_
            
        Vous pouvez participer.
        
.. revealjs:: 

    .. revealjs:: Python à l'ENSAE

        * Le système d'exploitation est Windows.
        * L'environnement est installé pour vous.
        * Vous pouvez appliquer le même `setup <http://www.xavierdupre.fr/enseignement/>`_ 
          chez vous.
        
    .. revealjs:: Python chez vous

        * Le système d'exploitation est celui que vous choisissez (Windows, Linux, Mac).
        
            * Windows : `setup <http://www.xavierdupre.fr/enseignement/>`_ fourni
            * Linux/Mac : Anaconda + une liste de modules à Installer

        * Lire `Getting started <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html#getting-started>`_.
        * Vous devriez avoir installé Python dès les premières séances.
        
    .. revealjs:: Version de Python
    
        * Le cours est construit pour la version 3.4+.
        * Les exemples ne marcheront pas tous sur la version 2.7.
        * Il faut choisir la version *amd64*. C'est la seule capable de tirer parti d'une mémoire de plus de 4 Go.
        
    .. revealjs:: Utiliser Internet
    
        Quand on ne sait pas, il suffit d'utiliser un moteur de recherche et de chercher :
        
            python + question
            
        *en anglais de préférence*
            
        Example :  `python pandas dataframe merge <https://duckduckgo.com/?q=python+pandas+dataframe+merge&ia=qa>`_
        
    .. revealjs:: Notebook
    
            * Ils mélangent code, texte, formules, tableaux, graphiques.
            * Ils sont convertibles au format HTML, Latex.
            
            * Ils sont pratiques pour garder la trace d'une série de petites étapes pour une étude scientifique.
            * Ils ne sont pas pratiques pour écrire de longs programmes.

    .. revealjs:: Notebook example
    
        `Jupyter <https://jupyter.org/>`_
    
        .. image:: _static/notsnap.png        
        
    .. revealjs:: Editeur 
    
        On n'écrit pas de modules ou de grands programmes dans un notebook. Il faut un éditeur.
        Il existe de nombreuses options :
            
            * `éditeurs, outils <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/devtools.html#l-devtools>`_
        
        La version gratuite de `PyCharm <http://www.jetbrains.com/pycharm/>`_ contient tout ce qu'il faut.
        Il détecte quelques erreurs avant l'exécution.
        Le débuggeur de `PyTools (Visual Studio) <https://pytools.codeplex.com/>`_ est très efficace.
        
    .. revealjs:: Scite
    
        `Scite <http://www.scintilla.org/SciTE.html>`_
        
        .. image:: _static/scite.png
        
    .. revealjs:: Spyder
    
        `Spyder <https://pythonhosted.org/spyder/>`_
        
        .. image:: _static/spyder.png
        
    .. revealjs:: Rodeo
    
        `Rodeo <http://blog.yhathq.com/posts/introducing-rodeo.html>`_
        
        .. image:: _static/rodeo.png
        
        

.. revealjs:: Contenu
    
    * Manipuler les données
    * Calcul matriciel
    * Calcul distribué
    * Visualisation
    * Machine learning
    * Algorithmie
    
.. revealjs:: 

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
    
    .. revealjs:: Deep Learning
    
        * Vision, apprentissage
    
        ...
    
        **Module de référence**
    
        * `theano <http://deeplearning.net/software/theano/>`_
        
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
        
.. revealjs:: 
        
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
    
.. revealjs::    

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
    
        `Séance 1 : données et graphes en quelques lignes <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/td2a_cenonce_session_1.html>`_
        
        DataFrame, Matplotlib
        
        A vous.

        
    

