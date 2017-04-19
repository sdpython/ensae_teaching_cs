
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
- `zipline <https://github.com/quantopian/zipline>`_ (module de trading algorithmique)

`quandl <http://www.quandl.com/>`_ est un aggrégateur de source données. Il
est possible de récupérer facilement de nombreuses séries financières, des séries économiques
comme le PIB des pays.
Vous trouvez plein de références sur de sources de données
ou de modules sur 
`awesome-quant <https://github.com/wilsonfreitas/awesome-quant>`_.
Un exemple de graphique avec matplotlib :
`candlestick_ohlc <https://matplotlib.org/examples/pylab_examples/finance_demo.html>`_.


Le module `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_
permet de récupérer facilement des données depuis
`Yahoo Finance <https://fr.finance.yahoo.com/>`_::

    from pyensae import StockPrices
    prices = StockPrices(tick="BNP.PA")
    print (prices.dataframe.head())

Pour ces deux sites, les données récupérées sont *daily* et pas *intraday*.
Les algorithmes fonctionnent tous à peu près de la même manière : chaque soir,
l'algorithme donne les décisions à prendre le lendemain.
Les stratégies dépendent de paramètres qu'on optimise en utilisant des données passées,
2004-2010 par example. On teste ensuite la stratégie sur la période suivante 2010-2014.
Il faut toujours faire attention à utiliser les données jusqu'à la date *t* pour
prédire les actions pour la date *t+1*.

Notebook conseillés :

* `An Introduction to Stock Market Data Analysis with Python (Part 1) <http://blog.yhat.com/posts/stock-data-python.html>`_
* `An Introduction to Stock Market Data Analysis with Python (Part 2) <http://blog.yhat.com/posts/stock-data-python-pt2.html>`_

D'autres idées avec d'autres lectures :

* `Random walks down Wall Street - Stochastic Processes in Python  <http://www.stuartreid.co.za/random-walks-down-wall-street-stochastic-processes-in-python/>`_,
* `10 Common Misconceptions about Neural Networks <http://www.stuartreid.co.za/misconceptions-about-neural-networks/>`_
* `Algorithmic trading system requirements <http://www.stuartreid.co.za/algorithmic-trading-system-requirements-post/>`_
* `et d'autres articles de Stuart Reid <http://www.stuartreid.co.za/one-year-later-metapost-computational-finance-blog/>`_
* `OLPS:AToolboxforOn-LinePortfolioSelection <http://www.jmlr.org/papers/volume17/15-317/15-317.pdf>`_ *(2016/08)*

.. _l-fi-trend:

Trend following
---------------

Le `trend following <http://en.wikipedia.org/wiki/Trend_following>`_ est un algorithme
qui fonctionne bien sur les `futures <http://fr.wikipedia.org/wiki/Contrat_%C3%A0_terme>`_.
Il existe de nombreuses variantes. En voici une :

    On compare la moyenne mobile à 10 jours avec la moyenne mobile à 100 jours.
    Deux cas sont à considérer :

        - si la moyenne à court terme est plus élevée que la moyenne à long terme, nous sommes sur une tendance haussière :math:`\rightarrow` on achète
        - si la moyenne à court terme est inférieure à la moyenne à long terme, la tendance est baissière :math:`\rightarrow` on vend

Vous trouverez plus à cette page :
:ref:`_finance_strategie_automatique`.

.. _l-fi-port:

Optimisation de portefeuille
----------------------------

Optimiser un portefeuille d'action consiste à construire une moyenne pondéré d'action
qui soit optimise le rendement à risque bornée soit minimise le risque à
rendement borné également. La page
:ref:`finance_strategie_automatique`
(`ancienne version pdf <http://www.xavierdupre.fr/enseignement/projet_data/Gestion%20de%20Portefeuille.pdf>`_)
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
Quelques liens :

* `Currency Portfolio Optimization Using ScienceOps <http://blog.yhathq.com/posts/currency-portfolio-optimization-using-scienceops.html>`_
* :ref:`finance_strategie_automatique`
* `Bayes à la rescousse de Markowitz <http://www.finaltis.com/downloads/finaltisefficientbetaeuro/lettrerecherche/201602LettreDeRecherche.pdf>`_
  (plutôt, à lire en cas de performances décevantes)

.. _l-fi-pair:

Pair trading
------------

Le `pair trading <http://en.wikipedia.org/wiki/Pairs_trade>`_ n'est pas vraiment une
stratégie. La différence vient ici du fait qu'on considère une paire d'action
comme produit financier plutôt qu'une action seule.
Le trader achète un action pendant qu'il vend l'autre.

.. _l-fi-ml:

Machine learning et trading
---------------------------

Ce projet demande un peu de travail. La première étape consiste à choisir des actions puis à déterminer manuellement ou à l'aide d'une règle
les dates à laquelle il aurait fallu acheter ou vendre cette action pour obtenir un bon rendement. Lors de cett étape,
on utilise le futur de l'action pour déterminer l'action idéale. On appelle cette série :math:`Y_t`.
Ensuite, on constitue une base de features :math:`(X_t)` : à chaque temps :math:`t`, on construit
des indicateurs comme la volatilité, la distance à différentes moyennes mobiles, la corrélation avec un indice ou
une autre action, le `RSI <http://fr.wikipedia.org/wiki/Relative_strength_index>`_... Ces indicateurs ne dépendent que du passé de la série.
L'objectif est de construire une fonction qui prédit la bonne décision :math:`Y_t = f(X_t) + \epsilon_t`. On utilise
des techniques issues du machine learning et des modules tels que `scikit-learn <http://scikit-learn.org/stable/>`_.

Travail attendu
---------------

Le rapport doit résumer ce que votre projet vous a appris, vous devez désigner
une meilleure stratégie avec les meilleurs paramètres et la façon de les obtenir.
Et comme c'est un projet de finance, on s'attend sans doute à ce que vous pariez
sur votre propre stratégie à moins que...

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
