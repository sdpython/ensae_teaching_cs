
.. _l-proj_finance:

Algorithmes de trading
======================

Le projet consiste à construire un algorithme qui proposent des décisions d'achats et de vente
sur des actions, futures... Voici quelques types de stratégies :

- Optimisation de portefeuille
- Trend Following
- Pair-trading


La première étapes pour les sujets financiers est la récupération des données. 
Il existe de nombreux sites. Pour les besoins de ce projet, 
les deux sources suivantes suffiront :

- `Yahoo Finance <https://fr.finance.yahoo.com/>`_
- `quandl <http://www.quandl.com/>`_

`quandl <http://www.quandl.com/>`_ est un aggrégateur de source données. Il
est possible de récupérer facilement de nombreuses séries financières, des séries économiques
comme le PIB des pays.

Le module `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_
permet de récupérer facilement des données depuis 
`Yahoo Finance <https://fr.finance.yahoo.com/>`_::

    from pyensae import StockPrices
    prices = StockPrices(tick = "BNP.PA")
    print (prices.dataframe.head())

Pour ces deux sites, les données récupérées sont *daily* et pas *intraday*.
Les algorithmes fonctionnent tous à peu près de la même manière : chaque soir,
l'algorithme donne les décisions à prendre le lendemain.
Les stratégies dépendent de paramètres qu'on optimise en utilisant des données passées, 
2004-2010 par example. On teste ensuite la stratégie sur la période suivante 2010-2014.
Il faut toujours faire attention à utiliser les données jusqu'à la date *t* pour
prédire les actions pour la date *t+1*.



Les statégies en détail
-----------------------

Trend following
+++++++++++++++

Le `trend following <http://en.wikipedia.org/wiki/Trend_following>`_ est un algorithme
qui fonctionne bien sur les `futures <http://fr.wikipedia.org/wiki/Contrat_%C3%A0_terme>`_.
Il existe de nombreuses variantes. En voici une :

    On compare la moyenne mobile à 10 jours avec la moyenne mobile à 100 jours. 
    Deux cas sont à considérer :

        - si la moyenne à court terme est plus élevée que la moyenne à long terme, nous sommes sur une tendance haussière :math:`\rightarrow` on achète
        - si la moyenne à court terme est inférieure à la moyenne à long terme, la tendance est baissière :math:`\rightarrow` on vend

Vous trouverez plus
d'information dans ce document : `finance_autostrat.pdf <http://www.xavierdupre.fr/enseignement/initiation/finance_autostrat.pdf>`_.


Optimisation de portefeuille
++++++++++++++++++++++++++++

Optimiser un portefeuille d'action consiste à construire une moyenne pondéré d'action 
qui soit optimise le rendement à risque bornée soit minimise le risque à 
rendement borné également. La présentation suivante 
`Gestion de Portefeuille.pdf <http://www.xavierdupre.fr/enseignement/projet_data/Gestion%20de%20Portefeuille.pdf>`_
explique 
cela de façon sommaire. Le premier à avoir formalisé ce domaine est 
`Harry Markowitz <http://en.wikipedia.org/wiki/Harry_Markowitz>`_ 
(voir également `ici <http://fr.wikipedia.org/wiki/Th%C3%A9orie_moderne_du_portefeuille>`_). 
L'optimisation est `quadratique <http://fr.wikipedia.org/wiki/Optimisation_quadratique>`_ ;  
lorsque le portefeuille est constitué de deux ou trois actions, il se résout en utilisant 
la méthode des multiplicateurs de Lagrange. Lorsqu'il inclut plus d'actions, 
il faut utiliser d'autres méthodes d'optimisation telles que 
le `Lagrangien augmenté <http://en.wikipedia.org/wiki/Augmented_Lagrangian_method>`_. 
L'objectif est ici de choisir une façon de construire un portefeuille, 
de l'optimiser sur la période d'apprentissage et de la tester sur la période de test. 
Il est fortement recommandé de relire le TD qui concerne l'optimisation sous contraine.

Pair trading
++++++++++++

Le `pair trading <http://en.wikipedia.org/wiki/Pairs_trade>`_ n'est pas vraiment une 
stratégie. La différence vient ici du fait qu'on considère une paire d'action 
comme produit financier plutôt qu'une action seule.
Le trader achète un action pendant qu'il vend l'autre.



Travail attendu
---------------

- le rapport doit résumer ce que votre projet vous a appris, vous devez désigner 
  une meilleure stratégie avec les meilleurs paramètres et la façon de les obtenir.



Erreurs à éviter
----------------

Aucun résultats d'optimisation
++++++++++++++++++++++++++++++

L'optimisation d'un portefeuille mène parfois à un protefeuille où tous les coefficients
sont nuls sauf un. Il important certains résultats d'optimisation soient insérés dans le rapport.


Nombre de paramètres et nombre de contraintes
+++++++++++++++++++++++++++++++++++++++++++++

Lorsqu'on optimise un portefeuille, le problème qu'on résoud est un problème
d'optimisation sous contraintes. Chaque contrainte d'égalité enlève un degré de liberté au problème.
Chaque contrainte d'inégalité également si celle-ci est saturée. 
Le nombre d'actions dans le portefeuille doit donc être plus grand que le nombre de contraintes
afin que cela reste un problème d'optimisation.

Conclusions hâtives
+++++++++++++++++++

Une stratégie doit être validée sur plusieurs actions ou produits, plusieurs périodes différentes.
On ne peut pas conclure parce qu'on a obtenu un résultat positif
pour une action et une période précises.

