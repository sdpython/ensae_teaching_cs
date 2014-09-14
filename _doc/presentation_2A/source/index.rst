
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
        
        De lundi 22 septembre au lundi 3 novembre (excepté 27 Octobre)

    .. revealjs:: Objectifs du cours
    
        * Passer moins de temps à manipuler les données
        * Passer plus de temps à les modéliser
        * Connaître les outils pour être agile
        * Savoir faire rapidement une étude statistique simple
        
    .. revealjs:: Notebooks
    
        Le cours utilise les `notebooks <http://ipython.org/notebook.html>`_.
        
        .. image:: _static/notsnap.png        
        
    .. revealjs:: Le langage Python et Machine Learning
    
        Pourquoi ?

        * Le langage est open source et donc gratuit.
        * Il fonctionne sur toutes les OS (Windows, Linux, Mac).
        * Il dispose de nombreuses extensions.
        * Il peut tout faire.
        * Il est devenu une alternative intéressante pour un statisticien depuis 2013 et quelques modules :
            * `pandas <http://pandas.pydata.org/>`_, `ipython <http://ipython.org/>`_, `numpy <http://www.numpy.org/>`_, `matplotlib <http://matplotlib.org/>`_
            * `scikit-learn <http://scikit-learn.org/stable/>`_
        
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

    .. revealjs:: Thèmes abordés
    
        * Manipuler les données
        * Calcul matriciel
        * Calcul distribué
        * Visualisation
        * Machine learning
        * Algorithmie
        
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
        * GPU - Monte Carlo - _non abordé cette année_
        
        ...
        
        **Module de référence**
        
        `ipython <http://ipython.org/>`_
    
    .. revealjs:: Visualisation
        
        * De moins en moins de tableaux
        * De plus en plus de graphiques.    
        * De plus en plus intéractifs.
        
        ...
        
        **Module de référence**
        
        * `matplotlib <http://matplotlib.org/>`_
    
    .. revealjs:: Machine Learning
    
        * Statistiques descriptives
        * Clustering
        * Apprentissage statistiques
    
        ...
    
        **Module de référence**
    
        * `scikit-learn <http://scikit-learn.org/stable/>`_
        
        Gaël Varoquaux (INIRIA) viendra présenter ce module en tant que premier contributeur.
    
    .. revealjs:: Algorithmie
    
        * Manipuler 100 millions de lignes requiert d'être astucieux
        * Cas récurrents :
            * joindre deux sources de données
            * grouper, trier dans le bon ordre sans perdre du temps
    
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Inventif
    
        * Assembler les méthodes, modèles
        * Sans être limité par les outils
        
    .. revealjs:: Customiser son outil

        * Tout faire depuis un notebook
        * `R et notebooks <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/python_r.html>`_
        * `Custom Magics for IPython <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/ipython_custom_magics.html>`_
    
    .. revealjs:: ...
    
        A vous.

        
    

