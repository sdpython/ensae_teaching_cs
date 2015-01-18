

.. _l-entretiens:


Entretiens d'embauche pour le poste de Data Scientist
=====================================================

On retrouve presque les mêmes types d'exercices dans la plupart des entretiens d'embauche Big Data. 
Beaucoup d'annonces mentionnent le langage Python. Comme la plupart ds langages interprétés,
Python évite les copies inutiles pour les types mutables : :ref:`lm-Quest-cequuntypeimmuableouimmutable`.
On peut regarder cette page :ref:`l-FAQ` pour se rappeler quelques spécificités du langages.

Il faut connaître :ref:`pandas et matplotlib <td2acenoncesession1rst>`. 
En matière de machine learning, le module à connaître est 
:ref:`scikit-learn <td2acenoncesession4arst>` qu'on peut compléter par
:ref:`statsmodels <td2acenoncesession3Arst>`.

Même si ce n'est pas encore très répandu, la connaissance de Hadoop, PIG est un plus : 
:ref:`Hadoop, Streaming <td3acenoncesession7arst>` qu'on peut faire depuis une ligne de commande
ou depuis un notebook à condition d'utiliser le module `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_.


Enfin, il existe quelques algorithmes à connaître comme le calcul du plus court de chemin dans un graphe
avec la :ref:`programmation dynamique <td1acenoncesession7rst>` ou la 
`distance d'édition <http://www.xavierdupre.fr/blog/2013-12-02_nojs.html>`_.
Lorsqu'on travaille avec de gros volumes de données, il faut être astucieux dans sa manière de les traiter
et faire constamment attention au coût (:math:`O(n), O(n \ln n), O(n^2)` ... C'est pour cela qu'on 
teste votre capacité à résoudre des énigmes telles que 
ces :ref:`5 exercices <td2acenoncesession6rst>`.

*La plupart des notebooks cités sont présentés sous forme d'exercice. La correction est disponible sur ce site.*