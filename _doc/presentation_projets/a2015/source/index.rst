
ENSAE 1A - Projets informatiques
================================

.. revealjs:: ENSAE 1A - Projets informatiques
    :data-background: #DDDDDD

    .. image:: _static/project_ico.png

    Encadrants : `Xavier Dupré <http://www.xavierdupre.fr/>`_ ,
    Emmanuel Guérin, Arthur Renaud

    **Assistant à l'ENSAE**
    
    `Romain Lesauvage <mailto: romain.lesauvage AT ensae.fr>`_
        
        
.. revealjs:: Quelques idées
    :data-background: #DDDDFF

            * Finance
            * Machine Learning
            * Jeux de Cartes
            * Mathématiques
            * Nuages de mots
            * Jeux de plates-formes, smartphone
            
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
            * jeu de données plus complexe si il y a le temps
            
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

    .. revealjs:: Algorithme mathématiques
    
        * optimisation
        * résolution de puzzle
        * `google jam <https://code.google.com/codejam/contest/6214486/dashboard#s=p3>`_

    .. revealjs:: Algorithme mathématiques
    
        * commencer par de petites dimensions
        * découper le problème en petites fonctions
        * vérifier que chaque petite fonction fait ce qu'on attend d'elle
        
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
    
        * Ce projet nous a permis de découvrir de multiples éléments et outils non abordés au 
          cours du premier semestre et a donc été bénéfique pour notre appréhension 
          de la programmation orientée objet en général.        

    .. revealjs:: dix pages de codes dans le rapport
    
        * Mais j'ai le programme vous savez !
        * Je préfère dix lignes bien placées que cent qui me noient.
        * Le jury sait peu de choses mais il sait qu'il y a 52 cartes.
    
    .. revealjs:: le programme
    
        * Je ne comprends pas le rapport.
        * Le programme ne marche pas.
        * Je n'ai pas les données.
        * On a laissé un commentaire ::
        
            # il 3h du mat, j'en ai marre. 
            
        * Ca m'aide pas beaucoup.
    
    .. revealjs:: 
    
        * Imaginer que le lecteur a trente rapports à lire et que voulez qu'il se souvienne de vous
          car il a compris les points essentiels de votre travail.
        * Si le projet vous a intéressé, il y a de bonne chance que le jury le soit aussi.
    
.. revealjs:: A vous
    :data-background: #DDDDFF

    Questions ?
    