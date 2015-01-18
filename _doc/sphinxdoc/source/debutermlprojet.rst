

.. _l-debutermlprojet:

Bien démarrer un projet de machine learning
===========================================


Un projet de machine learning commence généralement avec un jeu de données et un problème à résoudre.
Une fois qu'on a cela, les premières étapes débutent avec presque toujours les mêmes questions :

Etape 1 : quel est le type de problème ?
++++++++++++++++++++++++++++++++++++++++

* supervisé 
    * régression : :math:`Y = f(X) + \epsilon`
    * classification : :math:`(c_1,...,c_k) = f(X)` pour un problème à :math:`k` classes
    * ranking
* non supervisé
    * clustering
    * réduction du nombre de dimension
    * système de recommandations
        
Etape 2 : quelles sont les données ?
++++++++++++++++++++++++++++++++++++

* Est-ce une table classique ou un graphe ?
* Y a-t-il une dimension temporelle ?
* Nombre d'observations ?
* Nombre de variables (ou features) ?
* Quelles sont les variables connues, les variables à prédire ?
* Valeurs manquantes ?
* Variables catégorielles, discrètes ou continues ?
    
La plupart des algorithmes d'apprentissages utilisent des données numériques,
il faut convertir les variables catégorielles au format numérique.

Si une variable catégorielle est à choix unique et qu'elle contient :math:`C` catégories, 
celle-ci sera multipliée en :math:`n` colonnes, une pour chaque modalité. Comme la somme de
ces colonnes est le vecteur colonne :math:`J=(1,...,1)`, la matrice :math:`X` modifiée sera corrélée.
    
Etape 3 : séparation train/test
+++++++++++++++++++++++++++++++

Il faut faire attention à deux ou trois détails. Par exemple, si le problème est un de problème 
de classification, il faut faire attention que toutes les classes à prédire sont bien représentées
dans les deux bases. C'est particulièrement important si l'une d'elles comportent peu d'exemples.

Etape 4 : apprentissage d'un modèle
+++++++++++++++++++++++++++++++++++

On cale un ou plusieurs modèles sur les données d'apprentissage.

Etape 5 : mesure de la performance
++++++++++++++++++++++++++++++++++

On mesure la performance du modèle sur la base de test. Il existe certaines façons standard de le faire en
fonction des types de problèmes :

* classification
    * matrice de confusion
    * courbe ROC
    * précision / rappel
* régression
    * erreur de prédiction
* ranking
    * `DCG <http://en.wikipedia.org/wiki/Discounted_cumulative_gain>`_
    * `corrélation de rang <http://en.wikipedia.org/wiki/Rank_correlation>`_
* clustering
    * variance intra classe, inter classe
    * nombre d'arc coupés
* système de recommandation
    * corrélation de rang

Si la performance globale convient, on s'arrête souvent ici. Dans le cas contraire, il faut retourner à l'étape 4 :

* La base d'apprentissage contient peut-être des points aberrants.
* La distribution d'un variable n'est pas homogène dans les bases d'apprentissage et des tests.
* Le modèle a besoin de plus de variables :
    * combinaison non linéaires des variables existantes (polynômes, fonctions en escalier, ...),
    * recoupement de la base de données avec une autre base.
* Les valeurs manquantes empêchent le modèle d'apprendre.
* Une variables continues ne l'est pas vraiment : distribution selon deux modes par exemple.
* ...
    
Voir également `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_.

Etape 6 : validation du modèle
++++++++++++++++++++++++++++++

On regarde sur quelques exemples bien choisi que le modèle proposent une réponse acceptables.
On applique des méthodes du type validation croisée.

