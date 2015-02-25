
ENSAE 1A - Projets informatiques
================================

.. revealjs:: ENSAE 1A - Projets informatiques
    :data-background: #DDDDDD

    .. image:: _static/project_ico.png

    Encadrants : `Xavier Dupré <http://www.xavierdupre.fr/>`_ ,
    Emmanuel Guérin, Arthur Renaud

    **Assistant à l'ENSAE**
    
    `Romain Lesauvage <mailto: romain.lesauvage AT ensae.fr>`_
        
        
.. revealjs:: Vos choix de projets
    :data-background: #DDDDFF

            * Finance
            * Machine Learning
            * Jeux de Cartes
            * Mathématiques
            * Nuages de mots
            * Jeux de plates-formes, smartphone
            
            ...
            
            La présentation contient des extraits de projets réalisés par des élévèes de l'ENSAE.
            Année 2012-2014.
            
.. revealjs:: Programmer, oui mais encore !
    :data-background: #DDDDFF
    
    
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Quelques dangers
    
        `The Code <http://en.wikipedia.org/wiki/The_Code_%282014_TV_series%29>`_
        
        .. raw:: html
        
            <div id='blogvision'><iframe src='http://www.allocine.fr/_video/iblogvision.aspx?cmedia=19550886' style='width:480px; height:270px'></iframe>
            <br /><a href='http://www.allocine.fr/_video/iblogvision.aspx?cmedia=19550886'>link</a>
            </div>

            
    .. revealjs:: Trouver le geek qui est en vous
    
        .. raw:: html

            <div id='blogvision2'><iframe width="420" height="315" src="https://www.youtube.com/embed/0ZgiVicpZGk" frameborder="0" allowfullscreen></iframe>
            <br /><a href="https://www.youtube.com/watch?v=hk-c5jlk48s">link</a>
            </div>
            
    .. revealjs:: THE Geek
    
        .. image:: images/gourou.png
        
        THE gourou: I don't code, I invent coding.
    
.. revealjs:: Un peu plus en détail
    :data-background: #DDDDFF

    * quelques caricatures
            
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Finance
    
            * Trend Following ou propre stratégie
            * Optimisation de porte-feuille : 
                * `cvxopt <http://cvxopt.org/>`_
                * fonction `qp <http://cvxopt.org/userguide/coneprog.html#quadratic-programming>`_
            * Machine Learning : 
                * `scikit-learn <http://scikit-learn.org/stable/>`_
            * Données
                * `pyensae.StockPrices <http://www.xavierdupre.fr/app/pyensae/helpsphinx/all_example.html#retrieve-stock-prices-from-the-yahoo-source>`_
                * `quandl <https://www.quandl.com/>`_, `quandl/futures <https://www.quandl.com/c/futures>`_
            
    .. revealjs:: Graphe de mauvais poil
    
        Que manque-t-il ?
    
        .. image:: images/f1.png
    
    .. revealjs:: Graphe toujours de mauvais poil
    
        Et le meilleur, à l'oeil je dirais...
    
        .. image:: images/f2.png
    
    .. revealjs:: Tableau récapitulatif
    
        Performance... unité ?
    
        .. image:: images/f3.png
        
    .. revealjs:: Courbe réaliste ?
        
        .. image:: images/f4.png
        
    .. revealjs:: Volatilité
        
        * :math:`\sqrt{\frac{1}{n} \sum \left(R_i - \bar{R}\right)^2}`
        * `Volatilité annualisée <http://en.wikipedia.org/wiki/Volatility_%28finance%29>`_
        
    .. revealjs:: Courbe lisible
        
        .. image:: images/f5.png
        
        
.. revealjs:: 
    :data-background: #DDDDDD
    
    .. revealjs:: Machine Learning 1 (ou projet 2A)
    
            * Machine Learning : `scikit-learn <http://scikit-learn.org/stable/>`_
            * `source de données et problèmes <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/ressources.html?highlight=donn%C3%A9es#source-de-donnees>`_
            
    .. revealjs:: Machine Learning 2

            * problème de la collecte
                * `scrappy <http://scrapy.org/>`_
                * `twitter <http://nbviewer.ipython.org/github/alexhanna/hse-twitter/blob/master/docs/Collecting%20Twitter%20data%20from%20the%20API%20with%20Python.ipynb>`_
                * ...
            * Machine Learning : `scikit-learn <http://scikit-learn.org/stable/>`_
            
    .. revealjs:: Machine Learning 3
    
            * implémenter votre propre algorithme de machine learning
            * jeu de données test
            * jeu de données plus complexe s'il y a le temps
            
    .. revealjs:: Machine Learning 4 : deep learning
    
            * `Yoshua Bengio <http://www.iro.umontreal.ca/~bengioy/yoshua_en/talks.html>`_
            * `Lasagne <https://github.com/benanne/Lasagne>`_
            * `theano <http://deeplearning.net/software/theano/>`_
            * `pylearn2 <http://deeplearning.net/software/pylearn2/library/index.html>`_
            
    .. revealjs:: Autre dont système de recommandations
    
            * `Algorithms for Near-Separable Nonnegative Matrix Factorization <http://research.microsoft.com/apps/video/default.aspx?id=189333>`_ (talk)
            * `LightLDA: Big Topic Models on Modest Compute Clusters <http://arxiv.org/pdf/1412.1576.pdf>`_
            * `Comprehend DeepWalk as Matrix Factorization <http://arxiv.org/pdf/1501.00358v1.pdf>`_
            * `Distributed Nonnegative Matrix Factorization for Web-Scale Dyadic Data Analysis on MapReduce <http://research.microsoft.com/pubs/119077/DNMF.pdf>`_
            * `Random Walks on the Click Graph <http://research.microsoft.com/en-us/um/people/nickcr/pubs/craswell_sigir07.pdf>`_
            * `Image Annotation Refinement using Random Walk with Restarts <http://research.microsoft.com/en-us/um/people/leizhang/paper/acmmm06_changhu.pdf>`_
            * `Efficient Random Walk Computation, and Ranking Mechanisms on the Web <http://research.microsoft.com/apps/video/default.aspx?id=121518>`_ (talk)
            
            
.. revealjs:: 
    :data-background: #DDDDDD
    
            
    .. revealjs:: Jeux de cartes
    
            * Partie graphique : optionnelle
            * Joueur intelligent
                * calcul de probabilité
            * Poker, Belotte, ...
            
    .. revealjs:: Graphiques optionnels
        
        .. image:: images/c5.png
        
    .. revealjs:: Librairies
        
        * `tkinter <https://docs.python.org/3.4/library/tkinter.html>`_
        * `pyqt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_
        * `pygame <http://pygame.org/news.html>`_
        * `kivy <http://kivy.org/>`_ (smartphone)
        
    .. revealjs:: IA
        
        .. image:: images/c1.png
        
    .. revealjs:: Choisir un paramètre ?
        
        .. image:: images/c2.png
        
    .. revealjs:: Comparer des stratégies 1
        
        .. image:: images/c4.png
        
    .. revealjs:: Comparer des stratégies 2
        
        .. image:: images/c3.png
        
.. revealjs:: 
    :data-background: #DDDDDD
    
    .. revealjs:: Nuage de mots
    
        * rendu
            * `d3.js <http://d3js.org/>`_, `tag cloud <https://github.com/jasondavies/d3-cloud>`_, `javascript <http://jsfiddle.net/adiioo7/RUTpJ/light/>`_
            * `format HTML <http://www.w3schools.com/tags/tag_font.asp>`_
        * mathématiques
            * `TF-IDF <http://en.wikipedia.org/wiki/Tf%E2%80%93idf>`_
            * `analyse factorielle <http://fr.wikipedia.org/wiki/Analyse_factorielle_des_correspondances>`_
            
    .. revealjs:: Stop words et autres problèmes
    
        * `Stop words <http://en.wikipedia.org/wiki/Stop_words>`_
        * `encoding <https://docs.python.org/3.4/howto/unicode.html>`_
        * `enlever les accents <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/texthelper/diacritic_helper.html#pyquickhelper.texthelper.diacritic_helper.remove_diacritics>`_
        * `normalisation, stemming <http://www.nltk.org/howto/stem.html>`_ (`NTLK <http://www.nltk.org/>`_)
            
    .. revealjs:: Vectoriser les mots
    
        * `word2vec <https://github.com/danielfrg/word2vec>`_
        * `topic modelling <http://radimrehurek.com/gensim/models/word2vec.html>`_ (with `Gensim <http://radimrehurek.com/gensim/index.html>`_)
        * `auto encoders <http://en.wikipedia.org/wiki/Autoencoder>`_
        * `pylearn2 <http://deeplearning.net/software/pylearn2/library/index.html>`_
        * `Improving Word Representations Via Global Context And Multiple Word Prototypes <http://www.socher.org/index.php/Main/ImprovingWordRepresentationsViaGlobalContextAndMultipleWordPrototypes>`_
        
    .. revealjs:: Illustration
    
        .. image:: images/cl1.png
        
            
.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Algorithmes mathématiques
    
        * optimisation
        * IA : `minimax <http://fr.wikipedia.org/wiki/Algorithme_minimax>`_, `alpha-beta <http://fr.wikipedia.org/wiki/%C3%89lagage_alpha-beta>`_
        * résolution de puzzle
        * `google jam <https://code.google.com/codejam/contest/6214486/dashboard#s=p3>`_

    .. revealjs:: Ca ne marchera pas mieux sur de grands problèmes
    
        * commencer par de petites dimensions
        * découper le problème en petites fonctions
        * vérifier que chaque petite fonction fait ce qu'on attend d'elle
            
    .. revealjs:: Cryptographie
    
        * `Merkle–Hellman knapsack cryptosystem <http://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem>`_
        * `Histoires des codes secrets <http://fr.wikipedia.org/wiki/Histoire_des_codes_secrets._De_l%27%C3%89gypte_des_pharaons_%C3%A0_l%27ordinateur_quantique>`_, Simon Singh
        * `Tor <https://www.torproject.org/>`_
    
        
.. revealjs:: 
    :data-background: #DDDDDD

        
    .. revealjs:: Simulation micro
    
        .. image:: images/e1.png

    .. revealjs:: Propagation
    
        .. image:: images/e2.png

    .. revealjs:: Fin
    
        .. image:: images/e3.png

    .. revealjs:: Aspect Macro
    
        .. image:: images/e4.png

.. revealjs:: 
    :data-background: #DDDDDD
    
    .. revealjs:: jeux, smartphone
    
        * `tkinter <https://docs.python.org/3.4/library/tkinter.html>`_
        * `pyqt <http://www.riverbankcomputing.co.uk/software/pyqt/intro>`_
        * `pygame <http://pygame.org/news.html>`_
        * `kivy <http://kivy.org/>`_ (smartphone)
            
                        
.. revealjs:: Déroulement
    :data-background: #DDDDFF


.. revealjs:: 
    :data-background: #DDDDDD
    
    .. revealjs:: Suivis

        * Mercredi 25 février
        * vendredi à 16h30
        
    .. revealjs:: Suivi 1
    
        * Poser le problème
        * Rester dans des limites raisonnables

    .. revealjs:: Suivi 2+
    
        * C'est vous qui voyez.

    .. revealjs:: attendu
    
        * un programme (notebook, programme, n'importe quel langage)
        * un rapport
        * une soutenance

    .. revealjs:: conclusion creuse
    
        Ce projet nous a permis de découvrir de multiples éléments et outils non abordés au 
        cours du premier semestre et a donc été bénéfique pour notre appréhension 
        de la programmation orientée objet en général.    
        
        ... 
        
        Attends je relis.

    .. revealjs:: dix pages de code dans le rapport
    
        * Mais j'ai le programme vous savez !
        * Je préfère dix lignes bien placées que cent qui me noient.
        * Le jury sait peu de choses mais il sait qu'il y a 52 cartes.
        * La belotte... c'est quoi les règles déjà ? Ok, file-moi le lien.
    
    .. revealjs:: le programme
    
        * Je ne comprends pas le rapport.
        * Le programme ne marche pas.
        * Je n'ai pas les données.
        * On a laissé un commentaire ::
        
            # il 3h du mat, j'en ai marre. 
            
        * Ca ne m'aide pas beaucoup.
    
    .. revealjs:: indications
    
        * Imaginer que le lecteur a trente rapports à lire.
        * Il se souvient de vous car il a compris les points essentiels de votre travail.
        * Si le projet vous a intéressé, il y a de bonnes chances que le jury le soit aussi.

    .. revealjs:: mi-parcours, fin avril
    
        * 200 lignes de codes
        * un `pitch <http://fr.wikipedia.org/wiki/Pitch_%28fiction%29>`_

    .. revealjs:: début juin
    
        * soutenances
        * awesome


.. revealjs:: Encadrement
    :data-background: #DDDDFF
    
    

.. revealjs:: 
    :data-background: #DDDDDD

    .. revealjs:: Encadrants
        
        * Emmanuel Guérin
        * Arthur Renaud 
        * Xavier Dupré

    .. revealjs:: Domaine d'expertise
        
        * Géniel logiciel
        * Machine Learning
        * Hacking

    .. revealjs:: Git
        
        * `Git <http://git-scm.com/>`_, `TortoiseGit <https://code.google.com/p/tortoisegit/>`_
        * `GitHub <https://github.com/sdpython/ensae_teaching_cs/>`_
        * `commit <https://github.com/sdpython/ensae_teaching_cs/commit/551380b913099b8c5a3ffd54664301da87d36812>`_

    .. revealjs:: En cas d'incertitude
    
        * essayer
        * `mail to <mailto:xavier.dupre AT gmail.com>`_
        

.. revealjs:: A vous
    :data-background: #DDDDFF
    
    Questions ?
    