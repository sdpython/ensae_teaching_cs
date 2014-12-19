
.. _l-ml:

Machine Learning
================



Apprentissage par renforcement
++++++++++++++++++++++++++++++


Un problème souvent évoqué lorsqu'on parle d'apprentissage par renforcement est celui du 
`bandit manchot <http://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)>`_ ou 
`multi-armed bandit <http://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)>`_ 
en anglais. L'objectif de ce projet est de résoudre 
ce problème en utilisant l'apprentissage par renforcement. Quelques liens :

* `Rémi Munos, part 1 <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part1.pdf>`_
* `Rémi Munos, part 2 <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part2.pdf>`_
* `Rémi Munos, part 3, parlant spécifiquement du bandit manchot <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_part3.pdf>`_
* `Un livre sur l'apprentissage par renforcement <http://www.xavierdupre.fr/enseignement/projet_data/apprentissage_renforcement_RL-3.pdf>`_

Le bandit manchot fait référence aux machines à sou dans les casinos. 
Tout l'enjeu de cette méthode consiste à maximiser ces gains en améliorant sa stratégie au fur et 
à mesure. Tout au long du jeu, il devient possible d'estimer la probabilité d'apparition 
des combinaisons gagnantes avec de plus en plus de précision. 
L'apprentissage par renforcement est une façon d'optimiser ses gains tout en apprenant cette distribution.


Algorithme de Chow-Liu
++++++++++++++++++++++

Cet algorithme `Chow Liu <http://en.wikipedia.org/wiki/Chow%E2%80%93Liu_tree>`_. 
Il sert à construire des relations entre des variables aléatoires. On pourra procéder en deux étapes :

* implémentation de l'algorithme et vérification sur un jeux de données synthétiques
* application sur un jeu de données plus conséquent


**Ressources**

* `MOOC: Learning Tree Structured Networks <https://class.coursera.org/pgm/lecture/97>`_,  Daphne Koller
  (pour aller plus loin `Probabilistic Graphical Models <https://class.coursera.org/pgm/lecture/preview>`_)
* `http://pgm.stanford.edu/ <Probabilistic Graphical Models>`_, Daphne Koller, Nir Friedman
* `Learning with Mixtures of Trees <http://www.jmlr.org/papers/volume1/meila00a/meila00a.pdf>`_, Marina Meila, Michael I. Jordan

