

.. issue.

.. _l-glossaire:


.. _l-glossary:


Glossaire
=========

.. glossary::

    algorithme
        Un `algorithme <http://fr.wikipedia.org/wiki/Algorithme>`_ 
        est une suite finie et non ambigüe 
        d'opérations ou d'instructions permettant de résoudre un problème.
        
    benchmark
        `banc d'essai <http://fr.wikipedia.org/wiki/Test_de_performance>`_

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
        Le concept `Deep Learning <http://en.wikipedia.org/wiki/Deep_learning>`_ évoque a commencé avec cet article
        `Deep Learning: Methods and Applications <http://research.microsoft.com/apps/pubs/default.aspx?id=219984>`_
        Deep learning signifie aussi des algorithmes gourmands en calculs 
        et il sont très rarement codés en Python seul mais en C++ et Python (wrapper) :
            - `Deep Learning Tutorials <http://www.deeplearning.net/tutorial/>`_ (python) 
              (voir aussi `github/yaoli/GSN <https://github.com/yaoli/GSN)>`_)
            - `Vowpal Wabbit <https://github.com/JohnLangford/vowpal_wabbit/wiki>`_ (C++)
        L'inventeur du deep learning est Yoshua Bengio:
            - `Yoshuas Bengion's talk <http://www.iro.umontreal.ca/~bengioy/yoshua_en/talks.html>`_. 
            - `LeNet 5 <http://yann.lecun.com/exdb/lenet/>`_ (probably the first known deep network)
        Voir aussi :
            - `Sequence to Sequence Learning with Neural Networks <http://arxiv.org/pdf/1409.3215.pdf>`_, Ilya Sutskever, Oriol Vinyals, Quoc V. Le
            - `Why does Deep Learning work? - A perspective from Group Theory <http://arxiv.org/abs/1412.6621>`_, Arnab Paul, Suresh Venkatasubramanian
            - `Deeply-Supervised Nets <http://arxiv.org/abs/1409.5185>`_, Chen-Yu Lee, Saining Xie, Patrick Gallagher, Zhengyou Zhang, Zhuowen Tu
        Quelques blogs :
            - `Image Scaling using Deep Convolutional Neural Networks <http://engineering.flipboard.com/2015/05/scaling-convnets/>`_
        
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
        
    ggplot
        `ggplot2 <http://ggplot2.org/>`_ est une librairie de graphiques sous R.
        Elle est accessible via `matplotlib <http://matplotlib.org/>`_.
        Voir `A few tricks with matplotlib <http://www.xavierdupre.fr/blog/2014-12-07_nojs.html>`_.
    
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
        :ref:`lm-Quest-cequuntypeimmuableouimmutable`, 
        :ref:`question_1A_2014_1`.
        
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
        
    pyquickhelper
        Ce module est utilisé par `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_.
        Il sert principalement à générer cette documentation.
        Il effectue des tâches avant et après la génération de la 
        documentation avec `Sphinx <http://sphinx-doc.org/>`_.
    
    Python
        Langage de programmation interprété. C'est le langage utilisé pour le support de ce cours.
        `Site officiel <https://www.python.org/>`_. 
        C'est un `langage impératif <http://fr.wikipedia.org/wiki/Programmation_imp%C3%A9rative>`_.
        
    reStructuredText
        Voir Sphinx.
        
    Rossum
        `Guido van Rossum <http://fr.wikipedia.org/wiki/Guido_van_Rossum>`_
        est l'inventeur du langage `Python <https://www.python.org/>`_.
        
    rst
        rst = reStructuredText
        
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
        
    Stroustrup
        `Bjarne Stroustrup <http://www.stroustrup.com/>`_ est l'inventeur du 
        langage `C++ <http://fr.wikipedia.org/wiki/C%2B%2B>`_.
        
    Sphinx
        `Sphinx <http://sphinx-doc.org/>`_ est un moteur qui génère de la
        documentation à partir de fichier au format `reStructuredText <http://docutils.sourceforge.net/rst.html>`_.
        
    SQL
        Le `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_ où *Structured Query Language*
        est un language dédié aux `base de données relationnelles <http://fr.wikipedia.org/wiki/Bases_de_donn%C3%A9es_relationnelles>`_.
        Sa logique est plus proche de la `programmation fonctionnelle <http://fr.wikipedia.org/wiki/Programmation_fonctionnelle>`_.
        
    SVN
        `SVN <http://fr.wikipedia.org/wiki/Apache_Subversion>`_ est un logiciel de suivi
        de source, de même que Git. Il est centralisé : une modification doit d'abord
        être appliquée à la branche centrale avant de pouvoir être propagée aux autres branches.
        
    warnings
        Non-blocking error but it should be read and the cause removed.
        See `Python: Use Warnings! <http://www.arruda.blog.br/programacao/python-use-warnings/>`_.
        
    Wheel
        Nouveau format pour installer des modules Python.
        Voir `Install a Python module with Wheel <http://www.xavierdupre.fr/blog/2015-01-19_nojs.html>`_.
    
