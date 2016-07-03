


.. _finance_strategie_automatique:

Stratégie automatique de trading en finance
===========================================

.. index:: finance, strading, stratégie


Une `stratégie automatique de trading <https://en.wikipedia.org/wiki/Algorithmic_trading>`_
désigne un algorithme qui 
propose voire prend des décisions de trading. Le rôle du trader consiste 
alors à concevoir et améliorer constamment son algorithme. Ce scénario 
est rendu possible grâce à l'évolution rapide des moyens informatiques 
qui vont jusqu'à utiliser des connexions internet ultra rapide 
(lire `Verizon Creates High-Speed Direct Trading Route From Aurora to New York Metro Financial Markets for CME Group <http://www.verizon.com/about/news/verizon-creates-high-speed-direct-trading-route-aurora-new-york-metro-financial-markets-cme/>`_).
Ces techniques étaient plutôt la spécialité de certains *Hedge Funds*
(c'est le cas de `Renaissance <https://en.wikipedia.org/wiki/Renaissance_Technologies>`_).
mais elles sont de plus en plus répandues.
Il va de soi qu'un tel système de trading automatique doit être réalisé 
avec le plus grand soin car les erreurs de conception ou les bugs 
ont un impact immédiat en terme financier. Cet automatisme extrême est 
impératif dans le cas de stratégie de type 
`High Frequency Trading <https://en.wikipedia.org/wiki/High-frequency_trading>`_
qui réagissent en temps réel à la moindre variation des cours. 
Pour des stratégies à plus long terme, les algorithmes ne sont pas 
toujours directement reliés aux marchés, ils génèrent des listes d'ordres 
qui sont effectués manuellement par un trader ou servent d'outils 
d'aide à la décision. Plus la fréquence des opérations est élevée, 
plus l'investissement nécessaire à leur mise en place est important. 

Quelques références
+++++++++++++++++++

En pratique, l'efficacité d'une stratégie est souvent limitée dans 
le temps, il faut sans cesse améliorer les stratégies 
existantes et en imaginer d'autres. Les paragraphes qui suivent 
donne une première idée de ce en quoi consiste la construction 
d'un tel algorithme. Il existe un grand nombre de livres décrivant 
le monde de la finance, cette partie succinte ne prétend pas en donner 
un reflet exhaustif, elle s'intéresse à un aspect en particulier qui 
est celui du trading automatique. Un livre est considéré comme la bible en 
finance, il s'agit de 
`Options Futures et autres actifs dérivés <http://www.pearson.fr/livre/?GCOI=27440100620090>`_ de 
John Hull ([Hull2011]_). 
Le livre 
`La finance quantitative en 50 questions <http://www.lgdj.fr/la-finance-quantitative-en-50-questions-9782212538977.html>`_ 
de Paul Wilmott ([Wilmott2008]_) aborde cinquante thèmes ou questions récurrentes 
en finance. Ce second livre se conclut par des conseils concernant 
la rédaction d'un CV ou des questions types utilisées lors des 
entretiens pour tester la vivacité d'esprit des candidats. Un 
autre livre autour des Hedge Funds intitulé 
`Hedge funds, private equity, marchés financiers les frères ennemis ? <http://www.alternatives-economiques.fr/hedge-funds--private-equity--marches-financiers---les-freres-ennemis--par-bertrand-jacquillat_fr_art_690_35793.html>`_
par Bertrand Jacquillat ([Jacquillat2008]_), c'est un recueil d'articles autour de l'utilité 
des Hedge Funds au sein du système économique et financier mondial, l'un d'eux se penche 
sur des moyens de mieux réguler leur activité pour l'instant peu contrainte. 
Un tiers des Hedge Fund en 2007 était établi dans les Iles Caymans. 
Je citerai également deux autres livres concernant les Hedge Funds. 
Le premier [RocchiChristiaens2007]_ décrit les différents 
style de gestion des Hedge Funds, il revient également sur les personnalités 
qui ont marqué l'histoire des Hedge Funds. Le second [Henry2008]_
aborde les mêmes thèmes mais est mieux structuré.

Ayant quitté la finance en 2007, je connais peu de références récentes 
qui auraient pu aborder la crise des subprimes. La démarche décrite 
ici est toujours valable mais des livres récents seraient plus 
précis à propos des évolutions informatiques et des 
indicateurs intéressants à surveiller en temps de crise.
Ce qui a changé : la part croissante de l'informatique et 
des algorithmes de trading, la vitesse des communication.


Vocabulaire financier
+++++++++++++++++++++

Marchés liquides
^^^^^^^^^^^^^^^^

Les algorithmes de trading sont de préférence utilisés sur des 
marchers financiers liquides et sur des produits standards tels que les actions, 
les Futures, les devises ou encore les taux d'intéret.
Des produits simples et liquides limitent considérablement les contraintes associées à 
leur trading. L'algorithme en sera d'autant moins compliqué à concevoir et à surveiller.

Les Futures sont des produits financiers reliés à un sous-jacent 
qui ne sera échangé entre le vendeur et l'acheteur 
qu'à une date ultérieure qu'on appelle *maturité*. 
Lorsqu'on achète un produit Future sur du pétrole par exemple, 
on s'engage en fait à acheter ce dit pétrole à une date fixée par 
le contrat. Au moment de la transaction, il n'est pas nécessaire 
d'avoir effectivement l'argent, on pourra toujours clore ce contract 
avant d'avoir à acheter réellement le pétrole. A cause de la spéculation 
financière, il y a bien plus de contrats ouverts que de pétrole disponible.

Parier sur une devise, c'est parier son évolution par rapport à une autre devise, par exemple, le cours Euro/Dollars.
Les taux d'intérêt ne sont pas les mêmes d'un pays à l'autre, ces taux ne sont pas non plus constants dans le temps.

La liquidité est une caractéristique essentielle, elle détermine 
la facilité avec laquelle on peut vendre et acheter un produit financier. 
On fait souvent la distinction entre `big cap <https://fr.wikipedia.org/wiki/Big_cap>`_, 
`mid cap <https://fr.wikipedia.org/wiki/Mid_cap>`_, 
`small cap <https://fr.wikipedia.org/wiki/Small_cap>`_., 
c'est-à-dire les grandes capitalisations boursières, les moyennes et les petites.
Sur le  secteur des *small cap*, il n'est pas toujours possible de trouver 
un acheteur ou un vendeur pour une action donnée. Cela ne 
veut pas dire que le prix de cette action est momentanément nul, 
cela signifie que, momentanément, il n'existe personne sur 
le marché pour échanger. La liquidité n'est pas une caractéristique constante, 
il peut arriver qu'un marché soit liquide la plupart du temps 
et qu'il ne le soit plus en temps de crise.

Description d'une série financière
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Une série financière ne se résume pas à une série de prix. 
Pour une série quotidienne, on dispose d'autres informations 
comme le premier prix de la journée 
`Open <https://en.wikipedia.org/wiki/Open-high-low-close_chart>`_, 
le dernier prix `Close <https://en.wikipedia.org/wiki/Open-high-low-close_chart>`_, 
le plus haut prix `High <https://en.wikipedia.org/wiki/Open-high-low-close_chart>`_ et le plus bas 
`Low <https://en.wikipedia.org/wiki/Open-high-low-close_chart>`_. 
Une autre information importante est le volume de transactions. 
La figure suivante représente toutes ces informations 
sur un seul graphique pour une vingtaine de jours.

.. mathdef::
    :title: Open-High-Low-Close-Volume
    :lid: finance_graph_ohlc_figure0
    :tag: Figure
    
    .. image:: finimg/ohlc.png

    Graphe *Open-High-Low-Close-Volume* d'une série financière. 
    Les histogrammes représentant les les volumes, vert pour 
    journée positive, rouge pour une journée négative. Chaque barre verticale
    relie les prix Low et High d'une même journée, les barres horizontales sont les prix Open à gauche et 
    Close à droite.
    		

Cette représentation est valable quelque soit la période de la série, 
que ce soit un jour, cinq minutes, il existe toujours 
quatre prix, Open High Low Close. Ces mêmes données sur des périodes 
de cinq minutes peuvent être utilisées pour faire du 
`trading intraday <https://fr.wikipedia.org/wiki/Day-trading>`_ : 
le trader quitte toutes ses positions chaque soir et ne 
s'intéresse qu'aux variations des prix au sein d'une même journée. 
La figure suivante représente deux jours d'une telle série. 
Ce graphe montre que le volume de transactions n'est pas constant, 
il est souvent élevé lorsque marchés européens et américains sont ouverts ensemble, 
il est également très élevé lorsque les acteurs du marchés attendent une 
information financière comme l'annonce d'une baisse des taux ou l'indice de 
satisfaction des ménages américains.

Il faut prendre le temps de regarder plusieurs séries financières,
de comprendre un peu mieux ce qu'est l'analyse technique d'uen série via
`Leçons d'analyse technique <http://www.abcbourse.com/apprendre/11_lecons_at_intro.html>`_.
Après seulement, on peut envisager les algorithmes de trading.

.. mathdef::
    :title: OHLC Intraday
    :tag: Figure
    :lid: finance_graph_ohlc_figure_intraday

    .. image:: finimg/intraday.png

    Graphe *Open-High-Low-Close-Volume* d'une série financière intraday. 
    Les volumes représentés ici sont ceux d'une série européenne, 
    il y a une première vague avant midi, juste avant la 
    pause déjeuner, il y a une seconde vague qui correspond à l'ouverture des marchés américains. Certaines 
    statistiques américaines tombe parfois à 13h30 heure française et ont un fort impact 
    très localisé dans le temps sur les séries financières les plus traitées.}
    		
Certains organismes financiers bâtissent des stratégies qui nécessitent 
des données encore plus précises qu'on appelle données `tick by tick <https://en.wikipedia.org/wiki/Tick_size>`_.
Un tick est un ordre exécuté, il correspond à une quantité et un prix, ce prix est la valeur de l'action 
jusqu'au prochain tick. Ainsi les quatre prix Open High Low Close sur une période sont calculés à partir 
des données tick by tick. Ces données sont très volumineuses et nécessitent des systèmes informatiques 
spécialisés. Elles sont aussi bruitées, il arrive parfois qu'un ordre passé à un temps :math:`t`
ne soit répercuté dans la série que plus tard.

On associe souvent aux données tick by tick les carnets d'ordres : 
ce sont les intentions de chaque acteur du marché, elles sont classées 
par prix croissants pour les intentions de vente et décroissants 
pour les intentions d'achat. Une donnée souvent mesurée est l'écart 
entre le prix de vente le plus bas et le prix d'achat le plus haut qu'on 
appelle `bid-offer spread <https://en.wikipedia.org/wiki/Bid%E2%80%93ask_spread>`_.
Cette différence est positive. Le prix d'une action n'évolue pas de manière continue, 
il ne peut augmenter ou diminuer que d'un nombre entier de ticks. 
Fournir des données financières nettoyées est un service qui se vend 
assez cher et qui sert principalement à l'`hyper trading <https://fr.wikipedia.org/wiki/Transactions_%C3%A0_haute_fr%C3%A9quence>`_. 
En agissant suffisamment vite (100~millisecondes pour aller retour bourse-banque-bourse), 
il est possible de placer un ordre à un prix qui assure son exécution.
    		
.. mathdef::
    :title: Exemple de carnet d'ordres, tous les ordres ne sont pas représentés.
    :tag: Figure
    :lid: finance_graph_ohlc_figure_carnet

    .. image:: finimg/carnet.png
    		    	    
.. _finance_rendemnt_annee:

Rendements, Volatilité, Corrélation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Le `CAC 40 <https://fr.wikipedia.org/wiki/CAC_40>`_ 
a perdu 0,2% aujourd'hui, -0,2% est le rendement du CAC 40 sur 
cette journée. Si on définit une série ou quotidienne ou daily par :math:`(X_t)_t`, 
le rendement journalier est défini par :

.. math::
    :nowrap:

    \begin{eqnarray*}
    r_t &=& \ln \frac{X_t}{X_{t-1}} \sim \frac{X_t - X_{t-1}}{X_{t-1}} \\
    \ln \frac{X_t}{X_{t-2}} &=& \ln \frac{X_t X_{t-1}}{X_{t-1} X_{t-2}} = \ln \frac{X_t}{X_{t-1}} + \ln \frac{X_{t-1}}{X_{t-2}}
                            = r_t + r_{t-1} 
    \end{eqnarray*}

Les logarithmes se manipulent assez bien puisque un rendement 
annuel devient la somme des rendements quotidiens. Ce dernier 
n'est souvent pas très représentatif, on préfère un rendement 
annualisé. Comme il y a environ :math:`N=220` jours de trading 
par an, le rendement annualisé devient :

.. math::
    :nowrap:
    
    \begin{eqnarray}
    R^{year} &=& N R^{day}  \Longleftrightarrow R^{day} = \frac{R^{year}}{N}
    \end{eqnarray}

Un rendement annuel de 10\% correspondant à un rendement journalier 
moyen de 0,045%. Un rendement de 10% par an est un excellent rendement mais il 
est intéressant de savoir si ce résultat a été obtenu de façon graduelle 
tout au long de l'année ou si c'était plutôt par à coup. C'est ce que 
tente de mesurer la volatilité d'une série : c'est l'écart-type des rendements.

.. math::
    :nowrap:

    \begin{eqnarray*}
    V^{day} &=& \sqrt{ \frac{1}{N} \sum_{t=1}^{N} \pa{r_t^{day} - \overline{r^{day}}}^2 } \\
    \text{avec }\overline{r^{day}} &=& \frac{1}{N} \sum_{t=1}^{N} r_t^{day} 
    \end{eqnarray*}

Cette volatilité est quotidienne ou daily, là encore, on préfère parler de volatilité 
annualisée. Le rendement annuel est la somme des rendements quotidiens, 
on suppose que ceux-ci sont tous indépendants les uns des autres 
et identiquement distribués, par conséquent : 

.. math::

    \sigma^{year} = \sqrt{\esp{(R^{year})^2}} = \sqrt{ \esp{\sum_1^N (R_i^{day})^2}} = \sqrt{ \esp{N(R^{day})^2}} = \sqrt{N} \sigma^{day}


Un dernier indicateur souvent utilisée est l'indice de corrélation 
entre deux séries. Lorsqu'on compare deux séries financières 
issues du même secteur (Société Générale et BNP par exemple), 
il est fort probable que ces deux séries réagissent de manière 
similaire à des événements économiques relatifs au secteur bancaire. 
Pour mesurer la proximité entre ces deux séries, 
on utilise la corrélation entre rendements :

.. math::
    :nowrap:
    
    \begin{eqnarray*}
    \rho(R_1,R_2) &=& \frac{1}{N \sigma_1^{day} \sigma_2^{day}} 
                    \sum_{i=1}^{N} \pa{ r_{1t}^{day} - \overline{r_{1}^{day}} }
                                                 \pa{ r_{1}^{day} - \overline{r_{2}^{day}} }
    \end{eqnarray*}

Cet indicateur est compris dans l'intervalle :math:`\cro{-1,1}`. 
Il est souvent calculé sur la dernière année écoulée, il exprime 
la proximité de deux séries financières. Investir sur deux 
actions fortement corrélées revient à investir le 
double sur une seule des deux puisque les rendements sont sensiblement 
les mêmes.

Ces indicateurs sont des moyennes, ils peuvent être estimés 
sur des périodes plus ou moins longues, sur des périodes 
glissantes mais de par leur nature, ils 
sont peu sensibles aux variations courtes.


Moyenne mobile, bandes de Bollinger
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La moyenne mobile est un indicateur couramment utilisé 
car il permet de mieux visualiser la tendance d'une 
courbe financière en gommant les variations quotidiennes. 
Cette moyenne est simplement la moyenne des dernières 
valeurs passées. On définit l'indicateur :math:`MM(n,t)` 
(MA pour `Moving Average <https://en.wikipedia.org/wiki/Moving_average>`_ en anglais)
à la  date :math:`t` la moyenne mobile :math:`n` 
par :

.. math::
    :nowrap:

    \begin{eqnarray}
    MM(n,t) = \frac{1}{n}  \sum_{i=0}^{n-1} X_{t-i}
    \end{eqnarray}

Cette moyenne est décentrée car elle ne tient compte que des 
valeurs passées, on dit souvent que la moyenne est en 
retard par rapport à la série elle-même. Cet indicateur 
permet de dégager une tendance mais prévoit toujours avec 
retard un changement de tendance. 

La figure :ref:`moyenne mobile <finance_graph_ohlc_figure_trend>` 
représente le cours d'une action 
à côté de sa moyenne mobile. Cet indicateur est couramment accompagnée 
des `bandes de Bollinger <https://fr.wikipedia.org/wiki/Bandes_de_Bollinger>`_ 
qui enserrent la série financière 
dans une sorte de tube. On définit tout d'abord la distance 
moyenne entre la série et sa moyenne :

.. math::
    :nowrap:

    \begin{eqnarray*}
    dist(n,t) = \sqrt{\frac{1}{n} \summy{i=0}{n-1} \pa{X_{t-i} - MM(n,i)}^2}
    \end{eqnarray*}

Les bandes de Bollinger sont définies par l'intervale 
:math:`\cro{ MM(n,t) - \alpha dist(n,t), \; MM(n,t) + \alpha dist(n,t)}` où 
:math:`\alpha` est un paramètre qui détermine la largeur du couloir. 
Le fait que la série sorte de ce couloir indique un jour de plus forte variation.

De nombreux autres indicateurs sont utilisés par les traders au cours de 
leur analyse technique. Le tableau suivant en reprend quelques-uns. 
On note par :math:`\pa{O_t, H_t, L_t, C_t}` les quatre prix Open High Low Close 
pour la période :math:`t`. 

----------------------------------  ---------------------------------------------------------------------------------------------- 
Indicateur                          Description
==================================  ==============================================================================================
moyenne mobile exponentielle        C'est une moyenne mobile qui accorde plus de poids aux valeurs récentes. 
                                    Elle est définie par un paramètre.
                                    :math:`\alpha` : :math:`MME_{\alpha}(t) = \alpha X_t + (1-\alpha) MME_{\alpha}(t-1)`. 
                                    Le paramètre :math:`\alpha` est souvent défini
                                    comme étant :math:`\alpha = \frac{2}{d+1}` où :math:`d` 
                                    est un nombre de périodes.
                                    MME = EMA pour Exponential Moving Average en anglais.
                                    `wikipedia <https://fr.wikipedia.org/wiki/Moyenne_glissante#Moyenne_mobile_exponentielle>`_
----------------------------------  ---------------------------------------------------------------------------------------------- 
True Range 					        Il est défini par :math:`TR_t = \max\acc{C_{t-1}, H_t} - \min\acc{L_t, C_{t-1}}`. 
                                    Il donne une estimation différente des variations
                                    opérées par une série financière durant la période. L'indicateur $TR_t$ permet
                                    de prendre en compte la variabilité intra-période (intraday si les périodes sont des jours).
                                    Rapporté à la série elle-même, c'est une mesure semblable à la volatilité mais beaucoup plus 
                                    réactive puisque ce n'est pas une moyenne.
                                    `wikipedia <https://en.wikipedia.org/wiki/Average_true_range>`_
----------------------------------  ---------------------------------------------------------------------------------------------- 
MACD 								Cet indicateur sert à détecter les changements de tendance 
                                    en calculant la différence entre deux moyennes 
                                    mobiles d'horizons différents :math:`n > m` : 
                                    :math:`MACD_{m,n}(t) = EMA_m(t) - EMA_n(t)`. Un changement de signe indique 
                                    un changement de tendance. Pour un trading daily, les 
                                    horizons sont souvent choisis dans l'ensemble
                                    :math:`(n,m) \in \acc{9,12,26}^2`. En pratique, l'indicateur 
                                    utilisé n'est pas directement le MACD mais une 
                                    moyenne mobile de celui-ci.
                                    `wikipedia <https://fr.wikipedia.org/wiki/MACD>`_
----------------------------------  ---------------------------------------------------------------------------------------------- 
Parabolic SAR (Stop And Reverse)    Cet indicateur cherche à détecter les tendances, il est défini par~:
                                    :math:`SAR(t) = SAR(t-1) + \alpha \pa{ EP(t) - SAR(t-1)}`. 
                                    :math:`\alpha` est un paramètre en général fixé à 0,02.
                                    et qui croît de 0,02 à chaque changement de tendance jusqu'à la valeur 0,2. 
                                    :math:`EP(t)` désigne le prix extrême observé
                                    au cours de la tendance en cours, il correspond à un prix maximal 
                                    pour un trend haussier et un prix minimal
                                    pour un trend baissier. Le $SAR$ détermine si le trend est 
                                    haussier s'il se situe en-dessous du prix actuel, 
                                    le trend est baissier s'il se situe au-dessus du prix actuel.
                                    `wikipedia <https://en.wikipedia.org/wiki/Parabolic_SAR>`_
----------------------------------  ---------------------------------------------------------------------------------------------- 
RSI (Relative Strength Indicator)   Cet indicateur sert à comparer les forces des mouvements 
                                    baissiers et haussiers. On définit tout
                                    d'abord les deux séries :math:`U_t = \max\acc{0,C_t - C_{t-1}}` et 
                                    :math:`D_t = \max\acc{0,C_{t-1} - C_t}`. 
                                    On définit ensuite
                                    :math:`EMU_n(t)` et :math:`EMD_n(t)` comme étant les moyennes mobiles 
                                    exponentielles des séries :math:`(U_t)` et :math:`(D_t)`. 
                                    On définit l'indicateur 
                                    :math:`RS_n(t) = \frac{EMU_n(t)}{EMD_n(t)}`. 
                                    Enfin, l'indicateur :math:`RSI_n(t) = 100 - \frac{100}{1+RS_n(t)}`.
                                    `wikipedia <https://fr.wikipedia.org/wiki/Relative_strength_index>`_
----------------------------------  ---------------------------------------------------------------------------------------------- 


Achats, ventes, levier
^^^^^^^^^^^^^^^^^^^^^^

Il n'est pas nécessaire de posséder une action pour la vendre. 
Au sein d'une banque ou d'un Hedge Fund, il est possible de vendre 
une action puis la racheter (on peut emprunter l'action au `broker <http://www.fimarkets.com/pages/brokers.php>`_). 
Néanmoins, la régulation de certains pays interdit la 
`vente à découvert <https://fr.wikipedia.org/wiki/Vente_%C3%A0_d%C3%A9couvert>`_.
Ce système permet d'"attraper" les tendances baissières. 
Il suffit de vendre au moment où la baisse commence puis d'acheter lorsque celle-ci s'arrête.

Un terme revient fréquement lorsqu'on parle de finance, 
il s'agit du `levier <https://fr.wikipedia.org/wiki/Effet_de_levier>`_. 
A priori, avec un fond de 100, 
il est possible d'acheter pour 100 d'actions. En empruntant 
100 de plus, il est alors possible d'acheter pour 200 d'actions. 
On dit que le levier est de 200% ou que la stratégie est 
*leveragée* deux fois. C'est un anglicisme couramment utilisé pour désigner un fort levier. 
Cette pratique est particulièrement intéressante lorsque la performance du 
Hedge Fund est bien supérieure au taux de l'emprunt. 
Ces sociétés ont pris beaucoup d'essort entre 2001 et 2007, favorisés par la politique 
de taux bas (< 2%) pratiqués par Banque Fédérale Américaine.
Le danger apparaît en temps de crise, un fort levier implique des 
pertes possibles beaucoup plus grandes. Le livre [Jacquillat2008]_ ouvre une discussion 
quant à la responsabilité des Hedge Funds durant la crise des subprimes.

Hedge Funds
^^^^^^^^^^^

Les Hedge Funds proposent ce qu'on appelle une gestion alternative de fonds. 
Ils proposent des rendements en moyenne de 10% par an avec une part de 
risque un peu plus importante. en 2007, ils étaient majoritairement basés aux Iles Cayman 
et aux Etats-Unis (voir ci-dessous), ils favorisent des placements à 
très courts termes (quelques mois) et sont fortement leveragés. 

.. mathdef::
    :title: Implantation des Hedge Funds en 2007
    :tag: Table

    Implantation des Hedge Funds de par le monde et 
    répartition selon les différentes stratégies de trading. 
    Source *Lipper* Mars 2007, extrait de [Jacquillat2008]_.


    Lieu                    Répartition
    ----------------------  -----------
    Iles Cayman             34 % 
    USA 				    20 % 
    British Virgin Islands  14 % 
    Bermudes                5 % 
    Luxembourg              5 % 
    France                  4 % 
    Irlande                 3 % 
    Bahamas                 3 % 
    Guernsey                2 % 
    Antilles Néerlandaises  2 % 


    Stratégie                           Répartition
    ----------------------------------  -----------
    Multi-stratégie                     31%
    Long / Short Equity                 23%
    Event Driven                        13%
    Commodity Trading Advisor (CTA)     6%
    Fixed Income Arbitrage              5%
    Emerging Markets                    4%
    Global Macro                        4%
    Equity Market Neutral               4%



La description des autres stratégies s'appuie sur le livre [RocchiChristiaens2007]_.
Un fond peut éventuellement investir dans d'autres fonds.

La stratégie `Long / Short Equity <https://en.wikipedia.org/wiki/Long/short_equity>`_ 
regroupe les stratégies qui prennent 
des positions à la fois vendeuses et acheteuses sur des actions. 
Le :ref:`pair trading <pair_trading_paragraph>` est d'ailleurs l'une 
d'entre elles. Les prises de positions peuvent 
s'étendre sur différents secteurs économiques. 
Pour éviter une trop grande exposition et réduire les risques de pertes, 
les gérants font parfois en sorte que la somme des positions acheteuses 
soit équivalente à celle des positions vendeuses pour chaque secteur. 
Ce cas particulier s'appelle `Equity Market Neutral <https://en.wikipedia.org/wiki/Market_neutral>`_.

La stratégie `Event Driven <https://en.wikipedia.org/wiki/Event-driven_investing>`_
se focalise sur les sociétés dont l'actualité est mouvementée avec un fort impact 
sur le cours de ses actions. Les gérants de ce type de fonds essayent 
d'anticiper des événements ayant trait à une société particulière comme une 
fusion ou une acquisition, une offre publique d'achat (OPA). L'annonce des 
retards de livraison de l'avion A380 rentre dans cette catégorie. 
La réussite nécessite une bonne connaissance de l'histoire des sociétés 
dont on souhaite acheter ou vendre les actions, de se pencher sur leur bilan financier.

La stratégie `Commodity Trading Advisor <https://en.wikipedia.org/wiki/Commodity_trading_advisor>`_ 
ou tout simplement *CTA* s'applique à des produits Futures comme les 
Futures sur les matières premières ou Commodities.
C'est le domaine de prédilection des fonds systématiques qui utilisent des algorithmes 
de trading automatique (voir paragraphe :ref:`parar_strat_auto_famille`). 
Les Futures sont des produits très liquides qui concernent aussi bien le 
pétrole que le blé ou l'or, les indices comme le CAC40. Un Future est 
la promesse d'échanger un produit à une date donnée appelée *maturité*.
Par exemple, le `Brent Crude Oil <https://en.wikipedia.org/wiki/Brent_Crude>`_  
côté sur le `New-York Merchantile Exchange (NYMEX) <https://fr.wikipedia.org/wiki/New_York_Mercantile_Exchange>`_
est un produit Future dont il existe une maturité par mois. Le café n'est échangé que tous 
les trois mois. Lorsqu'un Hedge Fund achète un Future Brent Crude Oil Aug08, 
il prend l'engagement d'acheter du pétrole à la fin du mois d'août 2008, 
il ne paiera qu'à cette date. Cette affirmation n'est pas complètement vraie, 
pour éviter qu'un investisseur ne fasse défaut, il est tenu de verser une somme forfaitaire (un appel de marge) 
à la chambre des compensations, il doit compléter cette somme dès que 
le prix du Future s'écarte par paliers du prix initial. Les Hedge Funds n'achètent bien entendu 
jamais de pétrole, lorsque la fin du mois d'août arrive, ils vendent 
ce produit pour acheter celui correspondant à la maturité suivante 
(en anglais `roll over <http://www.investopedia.com/university/intermediate-guide-to-trading-e-mini-futures/rollover-dates-and-expiration.asp>`_).
Avec ce système, il n'y a pas besoin d'emprunter, une position vendeuse est 
aussi facile à prendre qu'une position acheteuse puisque rien n'est échangé avant la date de maturité.

La stratégie `Fixed Income Arbitrage <https://en.wikipedia.org/wiki/Fixed_income_arbitrage>`_
concerne les taux d'intérêt. Lorsque l'argent est prêté, le taux d'intérêt 
dépend de la durée. Cette stratégie consiste à jouer avec ces taux, à parier sur leur évolution.

La stratégie `Global Macro <https://en.wikipedia.org/wiki/Global_macro>`_
nécessite d'excellentes connaissances en économie car il s'agit de prendre des paris sur 
l'évolution à court terme de l'économie mondiale. Anticiper la hausse 
du prix du pétrole en fait partie, comme parier sur l'évolution des 
taux d'intérêts américains et européens ou prévoir 
la croissance de l'ensemble d'un secteur économique.

Le terme `Hedge <https://en.wikipedia.org/wiki/Hedge_(finance)>`_ 
signifie se couvrir, se couvrir contre un pari trop risqué comme 
prendre des positions inversées sur des produits similaires, 
acheter ou vendre des options.

Une option est un produit financier qui permet d'assurer 
l'acheteur de cette option contre une variation des prix. 
L'acheteur d'une option achète le droit d'acheter ou de vendre 
une action à un prix donné et à une date donnée. L'acheteur 
peut ou non exercer son droit d'acheter ou de vendre. Par exemple, 
un acteur achète une option qui lui confère le droit d'acheter 
dans un mois une action à 110 euros sachant qu'elle est à 100 aujourd'hui. 
Si au bout d'un mois, l'action est à 120, l'acheteur exercera son 
option, son bénéfice sera de 10 moins le prix de l'option, dans le cas 
contraire, il n'exercera pas son option, il ne paiera que le 
prix de l'option. Les termes `call <https://fr.wikipedia.org/wiki/Option#Le_call>`_ et 
`put <https://fr.wikipedia.org/wiki/Option#Le_put>`_
sont couramment utilisés pour désigner les options.
Un call est le droit d'acheter, un put est le droit de vendre.

Les investisseurs qui souhaitent investir dans un Hedge Funds 
regardent son *track record* 
qui désigne sa performance passée, sa capacité à afficher 
des rendements positifs chaque année, synonyme d'une bonne gestion. 
L'investisseur regarde aussi la volatilité de la performance, 
lorsqu'elle est élevée, l'incertitude sur la performance est plus grande. 
L'investisseur regarde également la corrélation avec le marché, 
le Hedge Fund est un placement risqué, une bonne gestion signifie 
aussi une volatilité contenue et une absence de corrélation 
avec le marché afin d'être moins sensible aux crises du marché.

.. _parar_strat_auto_famille:

Familles de stratégies
++++++++++++++++++++++

Les paragraphes qui suivent présentent différentes stratégies 
qui cherchent à capter chacune un aspect particulier d'une 
série financière. Ces stratégies s'appuient principalement sur 
des informations numériques calculées à partir des données numériques 
elles-mêmes (Open High Low Close Volume). Une exception pourtant : 
les stratégies de type *style* s'appliquent aux actions et utilisent 
d'autres informations relatives à la société émettrice de ses 
actions comme le chiffre d'affaire et tout autre chiffre 
extrait de leur bilan financier. 

Il n'existe pas de meilleures stratégies, il est rare qu'une 
stratégie soit efficace sur tous les secteurs économique ou 
sur tous les types de produits, action, pétrole, indices, taux, ... 
Il est rare qu'une stratégie soit tout le temps performante, 
il est toujours préférable de constuire un système en utilisant 
plusieurs, la volatilité est moins élevée.

Il n'est pas simple d'intégrer dans des systèmes automatiques des 
informations quantitatives relatives aux informations économiques comme 
l'annonce d'un plan de licenciement, des retards dans les livraisons d'avions, 
une nouvelle dépréciations d'actifs. Outre la complexité qu'entraînerait 
la prise en compte des telles informations, un argument qui justifie la seule 
utilisation de l'analyse technique est l'efficience des marchés : 
les nouvelles économiques sont prises en compte par les prix eux-mêmes 
qui sont la résultante des ordres passés sur le marché. 
Les marchés financiers corrigent d'eux-mêmes les prix 
car ils intègrent toute l'information connue.

Une stratégie s'intéresse avant tout à un comportement moyen. Une 
moyenne mobile ne peut pas prendre en compte un jour de trading 
aberrant, une journée de crise, une stratégie cherche avant tout à profiter 
d'un comportement récurrent d'une série telle qu'une tendance et doit 
faire l'impasse sur des comportements erratiques et passagers. Ces derniers 
ne sont pas assez fréquents pour être étudiés, ils sont à chaque 
fois différents et leur compréhension dépasse 
le cadre de l'analyse technique.

.. _section_trend_following_s:

Trend Following
^^^^^^^^^^^^^^^

Le `Trend Following <https://en.wikipedia.org/wiki/Trend_following>`_ 
consiste à suivre une tendance qu'elle soit haussière ou baissière. 
Une simple stratégie de Trend Following est illustrée par la figure qui suit. 
Ce type de stratégie parie sur le long terme, le temps nécessaire 
pour qu'une tendance se forme et dure. On parle parfois d'attraper 
une tendance : la stratégie prend plusieurs fois de mauvaises 
décisions et décide de couper sa position
peu de temps après, de temps en temps, la décision est bonne et 
la pose est gardée le plus longtemps possible, jusqu'à ce que la tendance prenne fin.

On parle de position ou pose pour une quantité négative ou positive d'actions. 
Couper sa pose consiste à annuler sa position : tout vendre si on 
possédait des actions ou tout acheter si la position était négative. 
Après avoir coupé sa position, le portefeuille n'est plus constitué que d'argent. 

.. mathdef::
    :title: Action BNP et Trend Following
    :tag: Figure
    :lid: finance_graph_ohlc_figure_trend
    
    .. image:: finimg/trend.png
    
    Cours de l'action \textit{BNP} accompagné par sa moyenne mobile 50 et ses bandes de Bollinger. Une stratégie simple de 
    trend following consiste à acheter lorsque le cours dépasse sa bande 
    supérieure de Bollinger (point~A) et à revendre lorsque
    le cours passe sa bande inférieure (point~B). 
    Le gain est alors la différence des cours d'achat et de vente. Lorsque la tendance 
    est baissière, il suffit de vendre d'abord puis d'acheter ensuite.

Cette stratégie prend une position acheteuse ou *long* lorsque la tendance est haussière 
et vendeuse ou *short* lorsque la tendance est baissière.
Ce type de stratégie est averse au changement de tendance qu'elle 
détecte avec retard, car cette stratégie ne s'appuie que sur 
des moyennes mobiles. Plus généralement, lorsque la volatilité est grande, 
ce type de stratégie est déconseillée, 
il est préférable d'utiliser le *Mean Reversing*.    

Concevoir un indicateur de tendance n'est pas chose facile. 
Même si l'oeil humain est habitué à analyser des courbes 
financières, il n'en est pas de même pour un algorithme 
qui fait face aux effets de seuil. La stratégie décrite par 
la figure :ref:`BNP <finance_graph_ohlc_figure_trend>` 
prend des décisions lorsque sa courbe touche une de ses 
bandes de Bollinger. Un expert humain pourra prendre une décision 
si la distance entre la courbe et la bande est petite 
visuellement, un ordinateur a besoin de seuils constants 
pour prendre sa décision qui est binaire. On pourrait modifier 
la largeur de la bande de Bollinger mais la stratégie est 
souvent très sensible à cette largeur. Ce point sera évoqué 
plus loin au paragraphe :ref:`analyse_finace_strategie`.

Un autre facteur est la longueur de la tendance. La stratégie toujours 
décrite par la table sur les :ref:`statistiques classiques <analyse_finace_strategie>`
s'appuie sur une moyenne mobile de 50 jours. 
Elle détecte bien les tendances dont la longueur se 
situe autour de cette valeur mais elle est susceptible 
de prendre de mauvaises valeurs si la tendance est plus 
courte ou si une trentaine de jours assez volatiles 
s'immiscent au sein d'une tendance longue de plusieurs mois.

En pratique, la stratégie est munie de quelques mécanismes qui 
permettent de limiter les pertes. Lorsque la stratégie achète une action 
à un prix :math:`p` si le prix descend en dessous d'un seuil 
égal à :math:`p (1-\epsilon)` alors la position est coupée. La position est 
coupée si le prix passe au-dessus du seuil :math:`p(1+\epsilon)` 
dans le cas d'une position vendeuse. Ce système permet de limiter 
les pertes de la stratégie, il est souvent présent dans 
les stratégies qui suivent avec le même objectif : 
réduire le risque. Les marchés ont d'ailleurs intégrer 
ces mécanismes avec les `stop order <https://en.wikipedia.org/wiki/Order_(exchange)#Stop_orders>`_.
Ce n'est plus le trader qui coupe sa pose mais la bourse elle-même.s

Cette règle peut encore être améliorée lorsque la stratégie 
est gagnante depuis un certain temps, cette règle propose 
de stopper la stratégie à un niveau loin de son niveau actuel. 
Dans ce cas, on rapproche de temps en temps le niveau auquel 
la position est coupée pour éviter des pertes trop importantes. 
On rapproche le niveau de stop. Dans le même ordre d'idée, 
on peut décider de couper sa pose parfois lorsque la courbe 
s'éloigne beaucoup de sa moyenne mobile et que la position 
est gagnante : c'est prendre ses profits avant que ceux-ci ne diminuent.
    		

Mean Reversing ou Mean Reversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le `mean reversing <https://en.wikipedia.org/wiki/Mean_reversion_(finance)>`_
stratégie s'intéresse aux périodes durant lesquelles 
la volatilité est élevée et où aucune tendance ne se dégage. 
Cela suppose que le cours de l'action va osciller autour 
d'une position d'équilibre et que la meilleure stratégie à 
suivre est d'acheter lorsque le cours vient 
de baisser et de vendre lorsque le cours vient de monter.

En terme de décision, cette stratégie prend beaucoup de poses, 
les garde peu de temps et celles-ci sont souvent gagnantes. 
La stratégie commence à perdre lorsque la période de haute 
volatilité laisse place à une nouvelle tendance. Cette situation 
est mal gérée par cette stratégie qui se retrouve avec une 
position inverse à celle qu'elle aurait dû prendre.

.. mathdef::
    :title: Action BNP et Mean Reversing
    :lid: finance_graph_ohlc_figure_meanr
    :tag: Figure
    
    .. image:: finimg/meanr.png

    Cours de l'action \textit{BNP} accompagné par sa moyenne mobile 50 et ses bandes de Bollinger. 
    Une stratégie simple de 
    mean reversing consiste à acheter lorsque le cours dépasse sa bande inférieure de Bollinger (point~A) 
    et à revendre lorsque
    le cours revient vers sa borne supérieure (point~B). 
    Le gain est alors la différence des cours d'achat et de vente.
    		

Le terme `Contrarian <https://en.wikipedia.org/wiki/Contrarian>`_ 
apparaît parfois pour désigner cette stratégie. Ce terme désigne 
une stratégie dont les positions prises sont inverses au 
consensus suivi par le marché. Toutefois, la stratégie est 
souvent munie d'un mécanisme limitant les pertes 
tel que celui décrit au paragraphe :ref:`section_trend_following_s`.

.. _pair_trading_paragraph:


Pair Trading
^^^^^^^^^^^^ 


Le `pair trading <https://en.wikipedia.org/wiki/Pairs_trade>`_ consiste à 
construire un portefeuille de deux actions. On étudie dans ce cas 
la série du rapport des prix des deux actions. On choisit le plus souvent 
deux actions appartenant au même secteur économique (BNP, Société Générale par 
exemple) de façon à obtenir une série moins sensible aux événements 
économiques. En cas de crise ou de rebond du secteur, les deux 
actions sont toutes deux susceptibles d'être atteintes, le rapport 
des prix ne dépend plus que des différences des deux sociétés. 
Ce procédé permet de construire une série moins sensible aux tendances 
qui s'appliquent à un secteur dans son ensemble.

Les stratégies appliquées à ce rapport de prix sont plutôt de type 
mean reversing, on s'attend à ce que temporairement le rapport 
des prix s'écarte de sa moyenne puis y reviennent. La différence 
intervient lors de la prise de décision, au lieu d'acheter ou de 
vendre une action, prendre une position consiste à acheter une 
action et vendre l'autre, quitter la position revient à 
effectuer la manipulation inverse.

.. mathdef::
    :title: Action BNP et pair trading
    :lid: finance_graph_ohlc_figure_pair
    :tag: Figure

    .. image:: finimg/pair.png

    Rapport entre l'action Société Générale et l'action BNP. 
    On observe une croissance supérieure pour la Société Générale jusqu'en 
    août 2007 date du début de la crise des subprimes puis une nette dégradation 
    depuis l'affaire Kerviel en janvier 2008. Auparavant,
    la série du rapport paraît plus stable et 
    il semble plus judicieux de faire du mean reversing.



Styles, Value, Growth
^^^^^^^^^^^^^^^^^^^^^


Le pair trading permet de prendre des paris sur une paires d'actions, 
une stratégie construite à partir de style propose une façon de jouer simultanément 
avec beaucoup d'actions. Elle utilise des indicateurs qui décrivent la santé 
financière d'une entreprise, ils sont généralement calculés à partir 
des bilans financiers que les sociétés cotées sont obligées de produire 
régulièrement. On distingue souvent deux classes de stratégies, 
les `growth <https://en.wikipedia.org/wiki/Growth_capital>`_ et les 
*value*. Les indicateurs servent à estimer si pour une compagnie, il est préférable de suivre une stratégie plutôt \textit{growth} ou plutôt \textit{value}.

Une société *growth* affiche un fort taux de croissance. 
Le prix de l'action est élevé mais les perspectives de croissance 
suggère une hausse. Il est intéressant dans ce cas d'acheter 
le stock. Une société *value* est plutôt estimée à son juste prix 
et les perspectives de hausse de cours de l'action sont faibles, 
il dans ce cas préférable d'attendre une baisse du cours avant d'acheter.

La liste suivante regroupe quelques indicateurs très utilisés pour 
étudier les sociétés cotées en bourse. Il existe plus d'une 
centaine d'indicateurs que les acteurs des marchés financiers suivent. 
Pour chacun d'entre eux, il faut savoir ce qu'est une bonne valeur, 
une mauvaise, quelle décision (acheter ou vendre) il 
faut prendre lorsque l'indicateur est élevé.

* Earnings before Interest, Taxes, Depreciation, and Amortization 
  (`EBITDA <https://fr.wikipedia.org/wiki/Earnings_before_interest,_taxes,_depreciation,_and_amortization>`_), 
  revenus avant Intérêts, impôts (Taxes), Dotations aux Amortissements et provisions
* Earnings Per Share (`EPS <https://en.wikipedia.org/wiki/Earnings_per_share>`_) : 
  :math:`\frac{\mbox{Net Earnings}}{\mbox{Outstanding Shares}}`,
  c'est le bénéfice d'une entreprise rapporté aux nombres de parts ou d'action,
* Price to Sales (`P/S <https://en.wikipedia.org/wiki/Price%E2%80%93sales_ratio>`_) : 
  :math:`\frac{\mbox{Market Cap}}{\mbox{Revenues}}`,
  Capitalisation boursière rapportée au chiffre d'affaires
* Dividend Payout Ratio (`DPR <https://en.wikipedia.org/wiki/Dividend_payout_ratio>`_) : 
  :math:`\frac{\mbox{Dividends Per Share}}{\mbox{EPS}}`,
  Dividende d'une action divisé par EPS
* Price to Earnings Ratio (`P/E <https://en.wikipedia.org/wiki/Price%E2%80%93earnings_ratio>`_) : 
  :math:`\frac{\mbox{Stock Price}}{\mbox{EPS}}`
  ou :math:`\frac{\mbox{Price per Share}}{\mbox{Annual Earnings per Share}}`,
  Prix d'une action divisé par EPS ou aussi le prix d'une action divisé par le dividende
  
  
Un indice P/E élevé indique un petit dividende comparé 
au prix de l'action, il est donc préférable de ne pas acheter. 
Il n'est pas toujours facile de savoir ce qu'est une valeur intéressante pour un indicateur mais on peut supposer que pour un secteur économique donné, il existe au moins une société dont l'indicateur est intéressant. A la date $t$, en classant par ordre croissant tous les indicateurs d'un même secteur économique, on peut supposer que les indicateurs extrêmes correspondent à des sociétés intéressantes.

Par exemple, supposons qu'au début de chaque mois, c'est à dire à la 
date :math:`t`, on dispose d'une nouvelle valeur de l'indicateur :math:`I_t^i` 
pour la société :math:`i`. 
On les trie par ordre croissant :  :math:`I_t^{\sigma(1)} \infegal I_t^{\sigma(2)} \infegal ... \infegal I_t^{\sigma(N)}`. 
Pour cet indicateur, une petite valeur suggère une position 
acheteuse. Par conséquent, on va prendre une position acheteuse 
pour les premiers 10% et une position vendeuse pour les derniers 10%.

société                 position
----------------------  ---------------------
:math:`\sigma(1)`   	acheteuse
...  			   		acheteuse
:math:`\sigma(10)`  	acheteuse
:math:`\sigma(11)`  	-
...					  	-
:math:`\sigma(N-11)`    -
:math:`\sigma(N-10)`    vendeuse
...		  			    vendeuse
:math:`\sigma(N)`       vendeuse

Le mois d'après, le classement a changé, quatre cas sont possibles :

* La société reçoit un classement équivalent et sa position ne change pas.
* La société n'apparaît plus dans les extrémités du classement, sa position est coupée.
* La société apparaît dans les extrémités du classement, on prend une position.
* La société passe d'une extrémité à une autre, on retourne la position.

Cette étape qui consiste tous les mois à conserver, couper, 
prendre ou retourner une position est souvent appelée 
`rebalancing <https://en.wikipedia.org/wiki/Rebalancing_investments>`_.
Il est préférable de n'utiliser cette méthode que sur des 
sociétés appartenant au même secteur économique, 
dans le cas contraire, classer les indicateurs par 
ordre croissant peut ne pas être pertinent.

Ce type de stratégie suppose le choix d'un indicateur 
ou d'une combinaison d'indicateurs. Le choix est souvent 
guidé par des raisons économiques et aussi l'utilisation de 
`backtest <https://fr.wikipedia.org/wiki/Backtesting>`_

Ce n'est pas toujours facile de combiner les sources.
Il faut faire attention au sens de chaque 
indicateur : un P/E faible suggère une position acheteuse, 
un DPR élevé suggère aussi une position acheteuse. 
Il est aussi difficile de combiner linéairement des indicateurs 
qui ont des ordres de grandeur différents. Une combinaison simple 
qui contourne ce problème est de combiner le rang des sociétés 
obtenus en les classant selon chaque indicateur de la combinaison. 
Par exemple, on classe les sociétés selon :math:`-P/E` et :math:`DPR`, 
les rangs obtenus sont additionnés et c'est le rang 
final qui servira à sélectionner les sociétés.


.. [Henry2008] Hedge Funds (2008),
   Gérard-Marie Henry, *Eyrolles*

.. [Hull2011] Options futures et autres actifs dérivés,
   John Hull, *Pearson Education*

.. [Jacquillat2008] Hedge funds, private equity, marchés financiers les frères ennemis ? (2008)
   Bertrand Jacquillat, *PUF*

.. [Wilmott2008] La finance quantitative en 50 questions (2008)
   Paul Willmott, *Edition d'Organisation*

.. [RocchiChristiaens2007] Hedge Funds, tome 1, Histoire de la gestion alternative et de ses techniques (2007)
   Jean-Michel Rocchi, Arnaud Christiaens, *Séfi Editions*
