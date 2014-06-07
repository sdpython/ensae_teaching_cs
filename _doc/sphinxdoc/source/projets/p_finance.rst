
.. _l-proj_finance:

Algorithmes de trading
======================

Le projet consiste à construire un algorithme qui proposent des décisions d'achats et de vente.


Voici quelques types de stratégies :

- Optimisation de porte-feuille
- Trend Following
- Pair-trading

Les statégies en détail
-----------------------

Trend following
+++++++++++++++

On cherche à écrire un algorithme de trading automatique sur des produits produits financiers en
s'inspirant d'une stratégie `trend following <http://en.wikipedia.org/wiki/Trend_following>`_ :
on compare la moyenne mobile à 10 jours avec la moyenne mobile à 100 jours. 
Deux cas sont à considérer :

- si la moyenne à court terme est plus élevée que la moyenne à long terme, nous sommes sur une tendance haussière :math:`\rightarrow` on achète
- si la moyenne à court terme est inférieure à la moyenne à long terme, la tendance est baissière :math:`\rightarrow` on vend

L'objectif du projet est de construire une stratégie avec quelques paramètres, de les optimiser sur la
période d’apprentissage (ou back test) puis de les tester sur la période de test. Vous trouverez plus
d'information dans ce document : `finance_autostrat.pdf <http://www.xavierdupre.fr/enseignement/initiation/finance_autostrat.pdf>`_.


Optimisation de porte-feuille
+++++++++++++++++++++++++++++

Pair trading
++++++++++++




Travail attendu
---------------

- le rapport doit résumer ce que votre projet vous a appris, vous devez désigner 
  une meilleure stratégie avec les meilleurs paramètres et la façon de les obtenir.



Erreurs à éviter
----------------

Nombre de paramètres et nombre de contraintes
+++++++++++++++++++++++++++++++++++++++++++++

Lorsqu'on optimise un porte-feuille, le problème qu'on résoud est un problème
d'optimisation sous contraintes. Chaque contrainte d'égalité enlève un degré de liberté au problème.
Chaque contrainte d'inégalité également si celle-ci est saturée. 
Le nombre d'actions dans le porte-feuille doit donc être plus grand que le nombre de contraintes
afin que cela reste un problème d'optimisation.



