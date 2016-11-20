

.. index:: glossary, glossaire


.. _l-glossaire:


.. _l-glossary:


Glossaire
=========

.. glossary::

    algorithme
        Un `algorithme <http://fr.wikipedia.org/wiki/Algorithme>`_ 
        est une suite finie et non ambigüe 
        d'opérations ou d'instructions permettant de résoudre un problème.
        
    Antlr4
        `Antlr4 <http://www.antlr.org/>`_ est un outil qui permet de construire des grammaires ou des 
        compilateurs. Cela peut servir à interpréter un code écrit dans un langage existant,
        pour le réécrire avec un meilleur format par exemple ou lui ajouter quelques fonctionnalités.
        On peut également vouloir définir rapidement un langage de script pour sa
        propre application. Dans les deux cas, cet outil permet éviter de réécrire son propre
        parseur et donc d'aller beaucoup plus vite. Il est intuitif.
        Voir `Using Antlr4 to write a grammar <http://www.xavierdupre.fr/blog/2015-07-13_nojs.html>`_.
        
    auto-encoders
        Le concept d'`auto-encoders <https://en.wikipedia.org/wiki/Autoencoder>`_ est
        associé au deep learning. C'est aussi un moyen de réduire le bruit dans les données *X*
        ou de les compresser
        en considérant la fonction :math:`X=g ( f (X ) )` où *g* est une fonction
        pseudo inverse de *f*. La fonction *f* est une sorte de projection dans un espace
        de dimension inférieur à celui de départ. La fonction *g* reconstruit *X* à partir de sa projection.
        Après cette première étape d'apprentissage,
        les données transformées :math:`f(X)` sont moins bruitées et sont souvent de meilleurs
        features que les données initiales. Cette étape est assez utile pour transformer des données
        discrètes (voire binaires) en données continues, ce que les algorithmes d'optimisation à base de gradient préfèrent.
        Voir aussi `Tutorial on auto-encoders <https://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_.
        
    bandits
        Le bandit manchot fait référence aux machines à sou dans les casinos. 
        Tout l'enjeu de cette méthode consiste à maximiser ces gains en améliorant sa stratégie au fur et 
        à mesure. Tout au long du jeu, il devient possible d'estimer la probabilité d'apparition 
        des combinaisons gagnantes avec de plus en plus de précision. 
        Voir `bandit manchot <http://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)>`_ ou 
        `multi-armed bandit <http://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)>`_ 
        en anglais. 
        
    benchmark
        `banc d'essai <http://fr.wikipedia.org/wiki/Test_de_performance>`_
    
    cache
        Mécanisme qui consiste à mémoriser un résultat coûteux à produire.
        Lorqu'il n'est pas possible de tout stocker en mémoire, il faut 
        choisir les informations les plus susceptibles d'être demandées.
        Voir `algorithme de cache <https://fr.wikipedia.org/wiki/Algorithmes_de_remplacement_des_lignes_de_cache>`_.
        
    Cheat Sheet
        Sorte d'anti-sèche. Quelques exemples pour le machine learning :
        `8 Best Machine Learning Cheat Sheets <http://designimag.com/best-machine-learning-cheat-sheets/>`_,
        `Cheat Sheets Python <http://www.xavierdupre.fr/app/ensae_projects/helpsphinx/cheat_sheets.html>`_
        Ce mot-clé fonctionne très bien quand on cherche des informations sur un language, un module...
        Essayez avec *python cheatsheet* sur n'importe quel moteur de recherche.

    coût
        Le coût d'un algorithme est le nombre d'opérations qu'il effectue lorsqu'il 
        est exécuté. Ce coût dépend des données qu'il manipule. 
        Il s'exprime en règle générale en fonction de la taille des données. 
        Le plus souvent, on ne cherche pas le nombre exact d'opérations 
        mais un nombre approché (notation en :math:`O(.)`). 
        La plupart du temps, ce coût correspond au nombre d'exécution d'une 
        instuction incluse dans la boucle la plus imbriquée.
        
    DropBox
        `DropBox <https://www.dropbox.com/>`_, stockage dans le cloud. Pour récupérer automatiquement des 
        fichiers, voir `Download a file from Dropbox with Python <http://www.xavierdupre.fr/blog/2015-01-20_nojs.html>`_.
        
    Deep Learning
        Le concept `Deep Learning <http://en.wikipedia.org/wiki/Deep_learning>`_ évoque souvent des réseaux
        de neurones à plusieurs couches dont on retrouve l'histoire et les principaux concepts dans le livre
        `Deep Learning: Methods and Applications <http://research.microsoft.com/apps/pubs/default.aspx?id=219984>`_.
        Deep learning signifie aussi des algorithmes gourmands en calculs 
        et ils sont très rarement codés en Python seul mais en C++ et Python (wrapper) :
        
        - `Deep Learning Tutorials <http://www.deeplearning.net/tutorial/>`_ (python) 
          (voir aussi `github/yaoli/GSN <https://github.com/yaoli/GSN)>`_)
        - `Vowpal Wabbit <https://github.com/JohnLangford/vowpal_wabbit/wiki>`_ (C++)
        - `Tutorial on auto-encoders <https://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_
            
        L'inventeur du deep learning est Yoshua Bengio:
        
        - `Yoshuas Bengion's talk <http://www.iro.umontreal.ca/~bengioy/yoshua_en/talks.html>`_. 
        - `LeNet 5 <http://yann.lecun.com/exdb/lenet/>`_ (probably the first known deep network)
        
        Voir aussi :
        
        - `Sequence to Sequence Learning with Neural Networks <http://arxiv.org/pdf/1409.3215.pdf>`_, Ilya Sutskever, Oriol Vinyals, Quoc V. Le
        - `Why does Deep Learning work? - A perspective from Group Theory <http://arxiv.org/abs/1412.6621>`_, Arnab Paul, Suresh Venkatasubramanian
        - `Deeply-Supervised Nets <http://arxiv.org/abs/1409.5185>`_, Chen-Yu Lee, Saining Xie, Patrick Gallagher, Zhengyou Zhang, Zhuowen Tu
        
        Quelques blogs :
        
        - `Image Scaling using Deep Convolutional Neural Networks <http://engineering.flipboard.com/2015/05/scaling-convnets/>`_
        
    Deep Q Network (DQN)    
        Deep Learning + Reinforcement Learning.
        Voir `DQN <https://en.wikipedia.org/wiki/Deep_learning#Deep_Q-networks>`_.
        Lire `Human-level control through deep reinforcement learning <https://storage.googleapis.com/deepmind-data/assets/papers/DeepMindNature14236Paper.pdf>`_,
        in Nature Volume 518, `Deep Reinforcement Learning from Self-Play in Imperfect-Information Games <https://arxiv.org/pdf/1603.01121.pdf>`_ (ArXiv)
        
    Dijkstra
        Plus connu pour l'algorithme du plus court chemin dans un graphe,
        `Edsger Dijkstra <http://fr.wikipedia.org/wiki/Edsger_Dijkstra>`_,
        il a contribué à faire ce que le programmation est aujourd'hui. Il faut lire
        `A Case against the GO TO statement <https://www.cs.utexas.edu/users/EWD/transcriptions/EWD02xx/EWD215.html>`_
        `The humble programmer <https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html>`_
        (traduction française `Le programmeur modeste <http://old.adrahon.org/le-programmeur-modeste.html>`_).
        Il est aussi l'auteur d'`aphorisme <http://fr.wikipedia.org/wiki/Edsger_Dijkstra#Aphorismes>`_
        très sensés pour la plupart des programmeurs.        
    
    ENSAE ParisTech
        Ecole Nationale de la Statistique et de l'Administration Economique (`ENSAE <http://www.ensae.fr/>`_)
        
    entretien
        Quelques révisions à faire afin de préparer un :ref:`l-entretiens`.
        
    expression régulière
        Chercher un mot dans un texte est facile, chercher un nombres réelles ou un date est plus complexe
        car toutes les séquences de chiffres ne sont pas des nombres ou des dates. Dans ce cas, il faut utiliser un
        outil plus adaptés comme les `expressions régulières <https://fr.wikipedia.org/wiki/Expression_rationnelle>`_
        qui permettent de chercher ou remplacer des motifs ce qu'illustre parfaitement l'article
        `8 Regular Expressions You Should Know <http://code.tutsplus.com/tutorials/8-regular-expressions-you-should-know--net-6149>`_.
        
    FAQ
        *Frequently Asked Questions*, titre de sections très souvent utilisés pour regroupés les
        questions envoyées par les utilisateurs d'un produit.
        
    Git
        Logiciel de suivi de source utilisé par exemple par GitHub. 
        Il est décentralisé. Chaque contributeur est libre de proposer ou d'importer
        une modification faite par un autre.

    GitHub
        `GitHub <http://fr.wikipedia.org/wiki/GitHub>`_ est un service web d'hébergement et de gestion de développement de logiciels, utilisant le 
        programme `Git <http://fr.wikipedia.org/wiki/Git>`_. 
        C'est ce service qui héberge les sources de ce tutoriel sur Python.
        Il sert essentiellement à deux choses : travailler à plusieurs
        et pouvoir facilement fusionner les modifications de chacun,
        conserver l'historique des modifications.
        Voici par exemple un changement sur la librairie
        `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_ :
        `add method plot <https://github.com/sdpython/pyensae/commit/b5c36ba7885d9d4d92c00e67c5a2d238c57d507a>`_.
        
    glouton
        Un `algorithme glouton <https://fr.wikipedia.org/wiki/Algorithme_glouton>`_
        est un algorithme qui suit le principe de faire, étape par étape, un choix optimum local (*wikipedia*).
        Ce terme est un peu trompeur parfois dans la mesure où il englobe des algorithmes rapides comme
        lents.
        
    ggplot
        `ggplot2 <http://ggplot2.org/>`_ est une librairie de graphiques sous R.
        Elle est accessible via `matplotlib <http://matplotlib.org/>`_.
        Voir `A few tricks with matplotlib <http://www.xavierdupre.fr/blog/2014-12-07_nojs.html>`_.
        
    GPU
        `GPU <https://en.wikipedia.org/wiki/Graphics_processing_unit>`_ = 
        Graphics Processing Unit. Ils sont très utilisés pour les réseaux de 
        neurones et les algorithmes de Monte Carlo.
        Voir `Building Deep Neural Networks in the Cloud with Azure GPU VMs, MXNet and Microsoft R Server <https://blogs.technet.microsoft.com/machinelearning/2016/09/15/building-deep-neural-networks-in-the-cloud-with-azure-gpu-vms-mxnet-and-microsoft-r-server/>`_.
        
    greedy
        Voir glouton.
    
    Hadoop
        Logiciel de distribution de traitement de données. 
        Voir `Hadoop <https://hadoop.apache.org/>`_.
    
    HDFS
        Hadoop File System : système de fichiers distribué propre à Hadoop : 
        `commandes HDFS <http://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html>`_.
        
    Hive
        Langage haut niveau pour implémenter des tâches Map/Reduce traitant des tables de données :
        `Hive <https://hive.apache.org/>`_.

    Immuable 
        voir Immutable
    
    Immutable
        On dit qu'un type est **immutable** s'il ne peut être modifié. Un
        tuple est **immutable**, c'est un tableau dont on ne peut pas changer les 
        éléments contrairement à une liste. Voir aussi
        :ref:`Qu'est-ce qu'un type immuable ou immutable ? <faq-py-immutable>`, 
        :ref:`question_1A_2014_1`.
        
    Internet Of Things
        Voir `Internet des Objets <https://fr.wikipedia.org/wiki/Internet_des_objets>`_.
        Les objets qui nous entourent enregistrent des données et en retour nous permettent
        de mieux interagir avec notre environnement.
        
    IoT
        Voir Internet Of Things
        
    Jenkins
        `Jenkins <http://jenkins-ci.org/>`_ est un logicial d'automatisation de build (et de tâches). 
        Voir `Build automation with Jenkins <http://www.xavierdupre.fr/blog/2014-12-06_nojs.html>`_.
        
    JIT
        Just In Time (Compilation). Some modules such as `Cython <http://cython.org/>`_ offers the possibility to speed up
        a Python programming by converting some part of it in C++. It is then compiled and executed.
        See also: `Python Just In Time Compilation <http://www.xavierdupre.fr/blog/2014-10-17_nojs.html>`_.
        
    Knuth
        `Donald Knuth <http://www-cs-faculty.stanford.edu/~uno/>`_  est l'auteur de 
        `The Art of Computer Programming <http://fr.wikipedia.org/wiki/Donald_Knuth>`_.
        C'est une des grandes figures de l'informatique. Il est 
        également l'inventeur du langage `TeX <http://fr.wikipedia.org/wiki/TeX>`_.
    
    Markdown
        Langage utilisé par les notebooks et pour cette documentation écrit en `rst <http://fr.wikipedia.org/wiki/ReStructuredText>`_.
        Sa syntaxe est décrite à `Markdown: Syntax <http://daringfireball.net/projects/markdown/syntax>`_.
        A l'instar du langage Python, il utilise l'indentation pour marquer la séparation entre les blocs.
        
    Mock
        Il est difficile de tester un programme qui lance des requêtes sur un service sans que ce 
        service soit activé comme par exemple récupérer des données financières sur Internet
        sans Internet. Lorsqu'on veut s'assuser qu'une fonction qui communique avec un service fonctionne, 
        on créé ce qu'on appelle un mock : on créé un faux service qui retourne des réponses assez courtes
        afin de tester la partie qu'on a besoin de tester. Ce genre de système permet de tester séparément le service
        et la partie qui communique avec ce service. Lire également  `Mock Object <http://en.wikipedia.org/wiki/Mock_object>`_,
        `Unit test et Mock <http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-5/>`_.
        
    Mutable
        Voir Immutable.
        
    Natural Language Processing
        Ensemble de méthodes traitent du `langage naturel <https://en.wikipedia.org/wiki/Natural_language_processing>`_.
        Les opérations les plus courantes consistent à `séparer un texte en mots <https://en.wikipedia.org/wiki/Text_segmentation>`_,
        à `normaliser <https://en.wikipedia.org/wiki/Text_normalization>`_,
        à faire du `stemming <https://en.wikipedia.org/wiki/Stemming>`_,
        à enlever les `mots de liaison <https://en.wikipedia.org/wiki/Stop_words>`_ qui n'apportent pas de sens au texte.
        Après ce nettoyage, on peut faire du `text mining <https://en.wikipedia.org/wiki/Text_mining>`_,
        de l'`analyse de sentiments <https://en.wikipedia.org/wiki/Sentiment_analysis>`_...
        
    NLP
        Voir Natural Language Processing
        
    NLTK
        *Natural Language Toolkit*. 
        La librairie `NTLK <http://www.nltk.org/>`_  est sans doute la plus connue lorsqu'il s'agit de 
        traiter le langage.
        
    optimisation
        L'`optimisation <https://fr.wikipedia.org/wiki/Optimisation_%28math%C3%A9matiques%29>`_
        se résume le plus souvent à maximiser ou minimiser une fonction réelle dépendant
        de plusieurs paramètres. Il s'agit de trouver les paramètres optimaux : ceuw qui permettent
        d'obtenir le minimum ou maximum trouvé. La plupart des problèmes de machine
        learning se résume à un problème d'optimisation.
        Parmi les différentes types de problèmes, on distingue les problèmes
        linéaire, quadratique, non linéaire, avec ou sans contraintes.
        Lire le blog :ref:`Optimisation avec contraintes, cvxopt, pulp, NLopt, ... <blog-optimisation-contrainte>`.
        
    pair programming
        Voir `pair programming <https://www.hackerschool.com/manual#sec-pairing>`_.
        
    PCFG
        *Probabilistic Context-Free Grammars*.
        Les grammaires permettent de *tagger* les mots d'un texte : en s'appuyant sur des règles de proximité, on
        arrive à reconnaître des noms, des verbes ou autre entités sémantiques.
        Voir `Probabilistic Context-Free Grammars (PCFGs) <http://www.cs.columbia.edu/~mcollins/courses/nlp2011/notes/pcfgs.pdf>`_.
        Voir aussi le module `NTLK <http://www.nltk.org/>`_.
        
    PIG
        Langage haut niveau pour implémenter des tâches avec plusieurs Map/Reduce :
        `PIG <http://pig.apache.org/>`_.
        
    PR
        voir Pull Request
        
    Pull Request
        Terme prope à `Git <http://fr.wikipedia.org/wiki/Git>`_ (`GitHub <http://fr.wikipedia.org/wiki/GitHub>`_, 
        `BitBucket <http://en.wikipedia.org/wiki/Bitbucket>`_, `GitLab <http://fr.wikipedia.org/wiki/GitLab>`_). 
        Cela veut dire que quelqu'un a forké un projet open source, l'a modifié et a demandé à son concepteur d'intégrer ses modifications. 
        Il a envoyé une `pull request <http://www.blog-nouvelles-technologies.fr/13114/comprendre-github-fork-branch-track-squash-et-pull-request/>`_.
        
    pyensae
        C'est un module que j'ai développé à l'attention des élèves de l'ENSAE
        (`documentation <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_).
        Il sert le plus souvent à télécharger des documents depuis le site 
        `www.xavierdupre.fr <http://www.xavierdupre.fr/>`_ et plus précisément des documents
        accessibles depuis ce lien `documents <http://www.xavierdupre.fr/enseignement/complements/index_documents.html>`_.
        
    PyQt
        `PyQt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_ est considéré comme le
        standard en matière d'interface grahique. C'est d'abord un concept d'interface graphique
        qu'on retrouve en Python sous deux implémentation :
        `PyQt4 <http://www.riverbankcomputing.com/software/pyqt/download>`_,
        `PyQt5 <http://www.riverbankcomputing.com/software/pyqt/download5>`_ (licence GPL),
        `PySide <http://pyside.github.io/docs/pyside/>`_ (licence LGPL).
        Il existe d'autres alternatives comme
        `Phoenix <http://wxpython.org/Phoenix/docs/html/main.html>`_
        mais moins populaires donc moins maintenus.
        
    pyquickhelper
        Ce module est utilisé par `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_.
        Il sert principalement à générer cette documentation.
        Il effectue des tâches avant et après la génération de la 
        documentation avec `Sphinx <http://sphinx-doc.org/>`_.
    
    Python
        Langage de programmation interprété. C'est le langage utilisé pour le support de ce cours.
        `Site officiel <https://www.python.org/>`_. 
        C'est un `langage impératif <http://fr.wikipedia.org/wiki/Programmation_imp%C3%A9rative>`_.
        Un tutoriel : `Python Notes <http://www.thomas-cokelaer.info/tutorials/python/index.html>`_.
        
    Recurrent Neural Network (RNN)
        `The Unreasonable Effectiveness of Recurrent Neural Networks <http://karpathy.github.io/2015/05/21/rnn-effectiveness/>`_
        
    regular expression
        Voir expression régulière.
        
    Resilient Distributed Datasets (RDD)
        Voir `Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing <http://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf>`_.
        
    reStructuredText
        Voir Sphinx.
        
    RNN
        Voir Recurrent Neural Network.
        
    Rossum
        `Guido van Rossum <http://fr.wikipedia.org/wiki/Guido_van_Rossum>`_
        est l'inventeur du langage `Python <https://www.python.org/>`_.
        
    rst
        rst = `reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`_, voir Sphinx
        
    score
        Le score n'a pas de définition théorique et il dépend de chaque modèle. 
        Prenons l'exemple d'une classification avec LDA, le résultat est un hyperplan qui sépare deux classes. 
        On détermine le meilleur hyperplan possible sur une base d'apprentissage. 
        Le score dans ce cas est la distance d'un point à cet hyperplan mais c'est une définition propre au modèle LDA. 
        D'une manière générale, un classifier réalise une partition, il permet de tracer des frontière entre 
        les classes. Le score indique si on est plus ou moins proche de cette frontière. 
        Plus on est proche, moins le classifieur est sûr de sa réponse. Voilà en résumé l'idée du score.
        Donc le score est un chiffre qui exprime la proximité d'une observation à la frontière de la classe 
        dans laquelle elle est classée. La frontière est apprise sur la base d'apprentissage, 
        l'observation provient de n'importe quelle base.  
        
    Sérialisation
        La `sérialisation <https://fr.wikipedia.org/wiki/S%C3%A9rialisation>`_ est le fait 
        de transcrire une structure de données parfois cyclique (comme un graphe) en une seule séquence
        d'octets. On s'en sert surtout pour transmettre ces données (via internet) ou les stocker.

    skewed join
        Voir :ref:`Map Reduce et Skew Join <blog-skew-join>`, :ref:`td3acenoncesession8arst`.
        
    Spark
        Couche logicielle au-dessus de Hadoop permettent de distribuer des calculs. 
        Se distingue de Hadoop grâce aux *Resilient Distributed Datasets* (RDD)
        qui sont plus efficace.
        Voir `Spark <https://spark.apache.org/>`_.
        
    sparse
        Les matrices `sparse <http://en.wikipedia.org/wiki/Sparse_matrix>`_ (ou creuses) sont des matrices 
        de grandes dimensions dont la plupart des coefficients sont nuls. En tenant compte de cette information,
        il est possible de réduire la taille de stockages et d'optimiser le calcul matriciel.
        Il n'existe pas encore de modules standard pour gérer ce cas. Quelques liens :
        `sparse et pandas <http://pandas.pydata.org/pandas-docs/dev/sparse.html>`_,
        `sparse matrix avec scipy <http://docs.scipy.org/doc/scipy-0.14.0/reference/sparse.html#module-scipy.sparse>`_,
        `Handling huge matrices in Python <http://www.philippsinger.info/?p=464>`_,
        `sparse matrix et cvxopt <http://cvxopt.org/userguide/matrices.html>`_,
        `présentation de blaze <http://fr.slideshare.net/pycontw/largescale-arrayoriented-computing-with-python>`_,
        `blaze <http://blaze.pydata.org/docs/latest/index.html>`_ (peut-être le futur de `numpy <http://blog.digital.telefonica.com/2014/03/05/python-big-data/>`_),
        `Introducing Blaze - HMDA Practice <http://continuum.io/blog/blaze-hmda>`_
        
    Sphinx
        Dans le cadre de ce cours, `Sphinx <http://sphinx-doc.org/>`_ est un module Python qui
        permet de générer la documentation de la grande majorité des modules Python incluant ce cours.
        Le langage de la documentation est `RST <https://en.wikipedia.org/wiki/ReStructuredText>`_ (reStructuredText). 
        Quelques exemples : 
        `Cheat Sheet <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_,
        `Sphinx and RST syntax guide <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_.
        
    Stemmer
        Un *stemmer* permet de réduire les différentes formes d'un mot. Les mots apparaissent au singulier, au pluriel,
        collés à une apostrophes, conjugués... Il n'est pas toujours évident de dire si un document contient un mot précis.
        C'est pourquoi on effectue une étape de nettoyage qui consite à séparer un texte en mot et à 
        les réduire à une forme canonique. Cette seconde étape est appelée le *stemming*.
        `NLP & Sentiment Analysis <http://nbviewer.jupyter.org/github/taposh/mlearning/blob/master/nlp/sentiment/bow/Sentiment.ipynb>`_
        
    Stemming
        Voir stemmer.
        
    Stroustrup
        `Bjarne Stroustrup <http://www.stroustrup.com/>`_ est l'inventeur du 
        langage `C++ <http://fr.wikipedia.org/wiki/C%2B%2B>`_.
        
    Sphinx
        `Sphinx <http://sphinx-doc.org/>`_ est un moteur qui génère de la
        documentation à partir de fichier au format `reStructuredText <http://docutils.sourceforge.net/rst.html>`_.
        Voir également `Restructured Text (reST) and Sphinx CheatSheet <http://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#images-and-figures>`_.
        
    SQL
        Le `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_ où *Structured Query Language*
        est un language dédié aux `base de données relationnelles <http://fr.wikipedia.org/wiki/Bases_de_donn%C3%A9es_relationnelles>`_.
        Sa logique est plus proche de la `programmation fonctionnelle <http://fr.wikipedia.org/wiki/Programmation_fonctionnelle>`_.
        
    SVN
        `SVN <http://fr.wikipedia.org/wiki/Apache_Subversion>`_ est un logiciel de suivi
        de source, de même que Git. Il est centralisé : une modification doit d'abord
        être appliquée à la branche centrale avant de pouvoir être propagée aux autres branches.
        
    Theano
        Librairie de calcul GPU pour Python. 
        Voir `theano <http://deeplearning.net/software/theano/>`_.
        
    Torch
        Librairie de deep learning pour Lua.
        Voir `Torch <http://torch.ch/>`_.
        Voir également `Torch vs Theano <http://fastml.com/torch-vs-theano/>`_.
        
    transport
        Théorie du transport, *m* usines, *n* entrepôts, on définit
        :math:`c(i,j)` le coût de transport d'une usine à un entrepôt,
        comment optimiser l'acheminement ? 
        Lire `Transport optimal de mesure : coup de neuf pour un très vieux problème <http://images.math.cnrs.fr/pdf2004/Villani.pdf>`_
        de Cédric Villani.
    
    warnings
        Non-blocking error but it should be read and the cause removed.
        See `Python: Use Warnings! <http://www.arruda.blog.br/programacao/python-use-warnings/>`_.
        
    Wheel
        Nouveau format pour installer des modules Python.
        Voir `Install a Python module with Wheel <http://www.xavierdupre.fr/blog/2015-01-19_nojs.html>`_.
    
