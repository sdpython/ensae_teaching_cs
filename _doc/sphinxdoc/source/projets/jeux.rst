
.. _l-proj_jeux:

Jeux de réflexion
=================

Pour chacun de ces projets, il faut permettre à un joueur de jouer contre l'ordinateur. La qualité de 
l'affichage est secondaire et l'accent doit être mis avant tout sur les stratégies utilisées par 
l'ordinateur. Le projet ne peut être validé que si : 

* Il est possible à un joueur de jouer contre l'ordinateur. 
* Il est possible de choisir parmi au moins deux stratégies ou deux niveaux de difficulté (il peut 
  s'agir de la même stratégie avec différents paramètres). 
* Il doit être possible de faire jouer l'ordinateur contre lui-même afin de permettre l'optimisation
  des paramètres de la stratégies de jeux ou le calcul de statistiques sur un grand nombre
  de parties.
  
Le plan suggéré est le suivant : 

1. Implémentation des règles du jeu et d'un affichage (graphique ou texte). L'encadrant pourra 
   aider si cet affichage n'est pas terminé avant la mi-parcours. 
2. Conception de deux stratégies 
3. Opposition de ces deux stratégies, sélection de la meilleure. 
4. Facultatif : si les deux stratégies sont conçues de la même façon mais avec des paramètres 
   différents, on pourra penser à un moyen de déterminer les meilleurs paramètres pour cette 
   famille de stratégies. 
   
Le modèle classique pour concevoir une stratégie consiste à utiliser une fonction d'évaluation qui 
donne un score à chaque coup possible. On utilise ensuite un algorithme 
`minimax <http://fr.wikipedia.org/wiki/Algorithme_minimax>`_ 
(voir aussi `Using Artificial Intelligence to solve the 2048 Game (JAVA code) <http://blog.datumbox.com/using-artificial-intelligence-to-solve-the-2048-game-java-code/>`_)
pour construire 
différents niveaux de difficulté. On pourra par exemple vérifier qu'une stratégie utilisant la même 
fonction d'évaluation qu'une autre mais avec un niveau de difficulté ou de profondeur plus élevée 
est meilleure. Avant de commencer la partie graphique, je suggère la lecture de cet article : 
`Frameworks for games in Python <http://www.xavierdupre.fr/blog/2014-01-01_nojs.html>`_.

.. _l-jeu-p4:

Puissance 4
-----------


Quelques liens : 

* `Règles du Puissance 4 <http://fr.wikipedia.org/wiki/Puissance_4>`_
* `minimax <http://fr.wikipedia.org/wiki/Algorithme_minimax>`_
* `élagage alpha-beta <http://fr.wikipedia.org/wiki/%C3%89lagage_alpha-beta>`_

Récemment, il a été prouvé qu'il existe une stratégie gagnante pour le joueur qui commence quelque 
soit son adversaire : `A Knowledge-based Approach of Connect-Four <http://www.informatik.uni-trier.de/~fernau/DSL0607/Masterthesis-Viergewinnt.pdf>`_
(`autre accès <http://www.xavierdupre.fr/enseignement/projet_data/puissance4_connect4.pdf>`_).
Quelques images regroupées par d'anciens élèves : 
`image_puissance_4.zip <http://www.xavierdupre.fr/enseignement/projet_data/image_puissance_4.zip>`_ 
pour ceux qui veulent réaliser une interface graphique. 

.. _l-jeu-oth:

Othello
-------

Quelques liens : 

* `Règles d'Othello <http://fr.wikipedia.org/wiki/Othello_(jeu)>`_
* `minimax <http://fr.wikipedia.org/wiki/Algorithme_minimax>`_
* `élagage alpha-beta <http://fr.wikipedia.org/wiki/%C3%89lagage_alpha-beta>`_

Quelques images regroupées par d'anciens élèves : 
`image_othello.zip <http://www.xavierdupre.fr/enseignement/projet_data/image_othello.zip>`_ 
pour ceux qui veulent réaliser une interface graphique.

.. _l-jeu-awa:

Awalé
-----

Quelques liens : 

* `Règles de l'Awalé <http://fr.wikipedia.org/wiki/Awal%C3%A9>`_
* `minimax <http://fr.wikipedia.org/wiki/Algorithme_minimax>`_
* `élagage alpha-beta <http://fr.wikipedia.org/wiki/%C3%89lagage_alpha-beta>`_

Quelques images regroupées par d'anciens élèves : 
`image_awale.zip <http://www.xavierdupre.fr/enseignement/projet_data/image_awale.zip>`_ 
pour ceux qui veulent réaliser une interface graphique.

.. _l-jeu-gomo:

Gomoku
------

Quelques liens : 

* `Règles du Gomoku <http://fr.wikipedia.org/wiki/Gomoku>`_
* `minimax <http://fr.wikipedia.org/wiki/Algorithme_minimax>`_
* `élagage alpha-beta <http://fr.wikipedia.org/wiki/%C3%89lagage_alpha-beta>`_

Le Gomoku peut se jouer sur des grilles de tailles diverses. Il est aussi simple de la dessiner
que d'utiliser des images.







