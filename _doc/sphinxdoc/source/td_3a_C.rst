

Données antipathiques et algorithmes Map/Reduce
===============================================

Séances dirigées
++++++++++++++++

.. toctree::
    :maxdepth: 2
    
    notebooks/_gs3a_hadoop_complexe
    
Lectures conseillées
++++++++++++++++++++

**particularité de map/reduce**

* analogie avec les itérateurs (langage fonctionnels)
* non conservation de l'ordre des lignes lors d'un traitement
* algorithmes des graphes contre-indiqués, cas des composantes connexes
* synchroniser l'heure des machines est un problème difficile
* limite du Monte Carlo sur map reduce (pseudo aléatoire distribué est compliqué,
  qu'en est-il de la fusion de deux séquences pseudo aléatoires ayant commencé avec la même seed ?, 
  lorsqu'on distribue, on crée de nombreux processus qui commence avec la même seed si on n'y prend pas garde,
  impossibilité de reproduire les résultats)

**problèmes récurrents de map/reduce**

* pas mal d'écriture sur disque, 
* éviter les sort, 
* possible explosion des stream intermédiaires, 
* gestion de la mémoire au niveau des mapper/reducer, 
* difficulté avec les algorithmes itératifs

**skewed streams**





