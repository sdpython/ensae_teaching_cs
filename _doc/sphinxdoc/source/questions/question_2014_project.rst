

.. _question_projet_2014

Questions Projets 2014
======================

.. _question_2014_projet_1_2A

Quel type de problème pour quelles données ?
++++++++++++++++++++++++++++++++++++++++++++

Pour un problème de regréssion (linéaire ou non) ou de classification, 
on s'attend à ce que les données
apparaissent dans une table classique, des colonnes pour les variables, 
une colonne contenant la cible (ou target) : une valeur numérique pour la régression,
un label pour la classification. Dans cette configuration, les données sont supposées
indépendantes.

Un problème, c'est aussi souvent plein de données de sources différentes et reliées entre elles :

* Certaines données sont générées par les utilisateurs (données temps réels, ...), 
  d'autres sont créées manuellement (classification de livres, ...).
* Elles peuvent être liées par le temps (série temporelles), géographiques (données
  spatiables), par une structure de réseau (facebook).

On peut aussi passer d'une représentation à l'autre en ajoutant des concepts
pour passer d'une structure à l'autre. Prenons l'exemple du jeu 
`Amazon product co-purchasing network metadata <http://snap.stanford.edu/data/amazon-meta.html>`_.
Ce jeu contient des commentaires d'utilisateurs à propos de produits. On sait aussi
quand ce commentaire a été écrit. On dispose également
d'une classification des produits (DVD, livres, vidéos...). C'est une 
`taxonomie <http://fr.wikipedia.org/wiki/Taxinomie>`_.

Un problème classique est d'essayer de prévoir si un utilisateur aimera
un produit ou non. C'est un 
`système de recommandation <http://fr.wikipedia.org/wiki/Syst%C3%A8me_de_recommandation>`_.
On veut prédire une sorte de score d'un produit :math:`p` 
pour un utilisateur :math:`u` à l'instant :math:`t`.

On peut voir cela comme un problème de régression et imaginer une table dans laquelle
on regroupe des caractéristiques sur les utilisateurs et les produits pour prédire un score.
On peut voir aussi cela comme un problème de classification en changeant le score par 
la probabilité que l'utilisateur achète aime produit (classe 0 : il n'aime pas, classe 1 : il aime).

**Problème 1**

Cela dit, le jeu de données ne contient pas beaucoup de caractéristiques à part
des données agrégées : combien de produits l'utilisateur a aimé, combien de fois le 
produit a été apprécié, combien de fois il l'a été récemment. On peut ajouter des données 
agrégées par catégories. Ensuite, il suffit d'apprendre un modèle en utilisant 
les évaluations des utilisateurs dont on dispose. C'est le problème 1.

**Problème 2, 2 bis**

On peut aussi se dire qu'on n'a peu exploité le fait que les utilisateurs se ressemblent
et que ceux qui se ressemblent aiment souvent les mêmes produits. On peut essayer 
de construire un clustering (donc non supervisé) des utilisateurs. C'est le problème 2.
Ensuite, on utilise les probabilités d'appartenance des utilisateurs 
aux clusters comme caractéristiques pour le problème 1.

On peut se dire qu'on aurait pu faire de même sur les produits. C'est le problème 3, toujours
pour améliorer les performances du modèle du problème 1.

L'inconvénient de ces deux approches est que le clustering opère sur des vecteurs de très 
grandes dimensions et creux. Cela ne les rend pas toujours facile à réaliser.

**Problème 3**

Pourquoi ne pas traiter les deux en même temps en décrivant le problème
comme un système de recommandations. Les données sont structurées comme 
un `graphe biparti <http://fr.wikipedia.org/wiki/Graphe_biparti>`_. Un utilisateur
d'un côté, un produit de l'autre, une évaluation pondère la relation entre les deux.
Ce n'est pas toujours évident d'évaluer la pertinence d'un tel système. Une façon de faire
est de transformer le résultat en caractéristiques pour revenir au problème 1.

Le système de recommandations peut être vu comme une façon de déterminer 
la proximité entre deux produits ou deux utilisateurs. C'est une forme de distance.
Deux produits proches auront une distance en dessous d'un certain seuil.
On peut par exemple ajouter
comme caractéristiques le nombre de produits proches un utilisateur 
a rédigé un commentaire.


**Problème 4**

Et les catégories ? C'est souvent une information assez fiable car elle a été construite 
manuellement par ceux qui gèrent le service. Ils sont donc intéressés à ce que cette 
information soit de qualité. En comparaison, les commentaires sont parfois très bruités.
Lorsqu'on manque d'information sur un produit en particulier (peu de commentaires),
on peut regrouper les produits peu évalués par leur catégorie dans le problème 3. 
Il faut décider quels produits regrouper. On peut aussi les utiliser pour clusteriser les 
utilisateurs : le vecteur sera d'une dimension abordable.

**Problème 5**

Et le temps ? On peut rechercher si certains produits sont passés de mode ou
si les utilisateurs découvrent les produits souvent dans le même ordre. 
On peut aussi considérer que les commentaires les plus vieux ont moins de valeurs
et qu'il faut leur donner moins de poids. Comment choisir ce poids dépendant du temps ?

**Problème 6**

Une fois de retour au problème 1, on analyse les observations pour lesquelles 
on fait le plus d'erreurs. On en déduit que l'un des problème évoqués ci-dessous
pourrait apporter la solution, une nouvelle caractéristique...

**...**

C'est un peu sans fin. Si l'objectif est de suggérer des produits qui
pourraient plaire à un utilisateur, une façon de mesurer la pertinence des
suggestions est de mesurer l'évolution du nombre d'achats par utilisateur,
de calculer la moyenne des évaluations et de voir si ces deux mesures augmentent.

**Remarque**

Il est facile d'évaluer un système temps réel sur le court terme et très difficile
sur le long terme. Recommander un best seller a beaucoup de chance de fonctionner 
à court terme. A long terme, les utilisateurs peuvent se lasser de ces recommandations 
qu'ils jugent peu-être un peu trop faciles.




