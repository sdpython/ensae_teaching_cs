
ENSAE 3A - Map/Reduce en pratique
=================================

.. revealjs:: ENSAE 3A - The Hitchhiker Guide...
    :data-background: #DDDDDD

    .. image:: _static/project_ico.png

    Matthieu Durut
    `Xavier Dupré <http://www.xavierdupre.fr/>`_ 

    **Assistant à l'ENSAE**
    
    `Romain Lesauvage <mailto: romain.lesauvage AT ensae.fr>`_
        
        
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Déroulement du cours 
    
            * 8 séances de 2h
            * 1 projet

        **Plan complet**
        
        `séances <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_3a.html>`_
        
    .. revealjs:: Objectifs du cours
    
        * Initiation au calcul distribué
        * Exercices pratiques avec Map / Reduce
        
    .. revealjs:: Notebooks
    
        Les exercices utilisent les `notebooks <http://ipython.org/notebook.html>`_.
        
        .. image:: _static/notsnap.png       

        La plupart des exemples sur Internet sont disponibles sous cette forme.
        
    .. revealjs:: Le langage Python
    
        Pourquoi ?

        * Le langage est open source et donc gratuit.
        * Il fonctionne sur tous les OS (Windows, Linux, Mac, bientôt `IPad <http://computableapp.com/>`_).
        * Il dispose de nombreuses extensions, il peut tout faire.
        * Les notebooks se répandent à grande vitesse : `A gallery of interesting IPython Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_.
        * Même si les calculs distribués ne se font pas en Python, le langage sert de télécommande programmable.
        
    .. revealjs:: Liens

        * `Contenu du cours <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_3a.html>`_
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
            * `azure <https://github.com/Azure/azure-sdk-for-python>`_
            
        Vous pouvez participer.
        
.. revealjs:: Environnement de travail
    :data-background: #DDDDFF    
    
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Python à l'ENSAE

        * Le système d'exploitation est Windows.
        * L'environnement est installé pour vous (`WinPython <http://winpython.sourceforge.net/>`_)
        * Vous pouvez le recopier tel quel chez vous (avec un clé USB).
        * `Anaconda <http://continuum.io/downloads#py34>`_ est plus complet et plus réactif
        
    .. revealjs:: Python chez vous

        * Le système d'exploitation est celui que vous choisissez (Windows, Linux, Mac).
        * Vous installez votre environnement (amenez votre ordinateur portable en TD en cas de problème).
        * Lire `Prérequis et installation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html#prerequis-et-installation>`_.
        * Vous devriez avoir installé Python dès les premières séances.
        
    .. revealjs:: Version de Python
    
        * Le cours est construit pour la version 3.3+.
        * Les exemples ne marcheront pas sur la version 2.7.
        * Il faut choisir la version *amd64*. C'est la seule capable de tirer parti d'une mémoire de plus de 4 Go.
        
    .. revealjs:: Notebook
    
            * Ils mélangent code, texte, formules, tableaux, graphiques.
            * Ils sont convertibles au format HTML, Latex.
            * Ils sont pratiques pour garder la trace d'une série de petites étapes pour une étude scientifique.
            * Ils ne sont pas pratiques pour écrire de longs programmes.
            * Ils sont très utilisés, plein d'exemples sur Internet
        
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
    
            +--------------------+-----------------------+--------------------------+
            | Ordre de grandeur  | Outil / Langage       | Algorithme               |
            | (observations)     | principal             | raisonnable              |
            +====================+=======================+==========================+
            | < 50000            | Excel                 | ``O(n^a)``               |
            +--------------------+-----------------------+--------------------------+
            | < 10 millions      | Python, R             | ``O(n (ln n)^a)``        |
            +--------------------+-----------------------+--------------------------+
            | < 1 milliard       | SQL                   | ``O(n ln n)``            |
            +--------------------+-----------------------+--------------------------+
            | > 200 millions     | Cluster (Map/Reduce)  | ``O(n ln n)`` distribué  |
            +--------------------+-----------------------+--------------------------+
            
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
            * Les mots de passe qu'on laisse dans les notebooks
        

.. revealjs:: Contenu
    :data-background: #DDDDFF
    
    * Séances 1-5 : éléments théoriques et logiciels
    * Séances 6-8 : Map / Reduce sur un vrai cluster
    
.. revealjs::    
    :data-background: #DDDDDD

    .. revealjs:: Map / Reduce

        * C'est une sorte de SQL distribué.
        * Pratique pour toutes sortes d'aggrégation.
        * A utiliser avec précaution pour des calculs sur des graphes.
        
    .. revealjs:: Cluster
    
        * Deux solutions
            * Azure HD Insight : `Microsoft, partenaire de la filière Data Science de l'ENSAE ParisTech avec Microsoft Azure Machine <http://www.microsoft.com/france/Hub-Presse/communiques-de-presse/fiche-communique.aspx?eid=f7e7f695-fb08-4c6d-b4ec-3cde562ba429>`_
            * Cloudera : distribution de Hadoop sur Linux
        * Un seul langage PIG et presque les mêmes TDs
            * Les mêmes scripts fonctionneront sur les deux systèmes
            * Différence minimes au niveau des commandes et des chemins des données
        
    .. revealjs:: Accès
    
        * Azure : deux clusters
            * un petit pour tester : disponible en permanence
            * un plus gros : ouvert pendant les projets
            * des identifiants unique pour tous les élèves
        * Cloudera
            * un cluster disponible en permanence (sauf notification)
            * un identifiant différent pour chaque utilisateur
        
    .. revealjs:: Approche du cours

        * forte culture informatique
            * interfaces graphiques limitées
            * fichiers texte et ligne de commande plus efficaces
        * `notebook <http://ipython.org/notebook.html>`_ + `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_
            * accès via des commandes magiques
            * accès depuis le notebook
            * python est une sorte de télécommande programmation

    .. revealjs:: Choix de langage

        * `PIG <http://en.wikipedia.org/wiki/Pig_Latin>`_ très proche du SQL sans index
            * langage haut niveau, programme concis
            * plus riche que `Hive <https://hive.apache.org/>`_
        * Python
            * notebook
            * `streaming <http://hadoop.apache.org/docs/r1.2.1/streaming.html>`_

    .. revealjs:: Objectif
    
        * introduire et pratiquer Map / Reduce
        * réduire le coût d'entrée technique

    .. revealjs:: Séances 6-8
    
        * S6 : introduction à PIG, parallèle avec SQL
        * S7 : streaming, PIG + python
        * S8 : coût selon la configuration des données et comment y remédier
    
.. reveals:: Notebooks et pyensae
    :data-background: #DDDDFF
    
    * `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_
        * un `wrapper <http://fr.wikipedia.org/wiki/Adaptateur_(patron_de_conception)>`_
        * des `commandes magiques <http://nbviewer.ipython.org/github/ipython/ipython/blob/1.x/examples/notebooks/Cell%20Magics.ipynb>`_ pour gommer un peu l'aspect geek
        * sans l'effacer complètement
        * pour pouvoir s'adapter à des habitudes différentes en entreprise
    * contribuer `github/pyensae <https://github.com/sdpython/pyensae/>`_
    
.. revealjs:: Hadoop
    :data-background: #DDDDFF
    
    `Notebook et PIG <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_3a.html>`_
    
    Dernier détail, sur Hadoop tout fichier texte
    est encodé en `UTF-8 <http://fr.wikipedia.org/wiki/UTF-8>`_.
    
    
