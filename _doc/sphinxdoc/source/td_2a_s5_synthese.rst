


.. _l-td25asynthese:

Distribution des calculs, stratégies de stockage, SQL NoSQL
===========================================================

Vue d'ensemble
++++++++++++++

* Stockage de données, consistence, persistence, impossibilité de faire des rollbacks, corruption, 
  absence de garanties sur la manière dont sont stockés les champs (exemple formats de date), pas d'index, etc.
* Introduction du SQL, type de requêtes, 
  Notion de transaction, d'atomicité, capacité de rollback, garanties ACID, 
  difficultés dans un SQL réparti (atomicité des transactions, double commit protocol)
* Systèmes NoSQL, Key-Value Pair Storage, transactionnalité multi-entités dans un Key-Value pair, 
  écriture optimiste avec des timestamps.
* Base de données orientées Document, Bases de données orientées Graph
* Map/Reduce. Notions de mappers, de reducers, de calculs embarassingly parallel. 
  problèmes des machines mortes, des stragglers, tradeof calcul/transfert des données,
  exemples d'applications de MapReduce,
  exemples d'algos difficilement parallélisables,
* Hadoop, Azure
* Queues distribuées.

SQL, NoSQL
++++++++++

* SQL / NoSQL / clé-valeur / document
    * Description d'un document (notion de structures, format json, xml)
    * SQL : 
        * notion d'index
        * Ne scale pas pour la parallélisation d'un grande nombre de recherches sur des données modifiées en permanence (mais à une moindre fréquence)
            * Cohérences des données
            * ACID
        * Traduction d'une base de documents en un schéma relationnel parfois complexe lorsque les documents ont une structure arborescente (plein de tables)
        * Récupérer un document entier nécessite plein de lookups
    * NoSQL
        * Clé/valeur --> simple et recherche très simple
        * Valeur = donnée simple comme document complexe
        * Recherche rapide sur les clés
        * Lente sur la plupart du reste
        * Efficace lorsqu'on veut récupérer la totalité d'un document
    * Autre type d'indexation
        * Trie
* Montée en charge, Stratégie de répartition de charges sur plusieurs machines
    * Dépend des données
    * Dépend des usages
    * Exemple
        * Cas d'un système de auto-complétion (usage standard sur un site internet)
        * Division en n machine --> comment faire
    * Notion de hash --> distribution uniforme
    * Transformée de Burrows-Wheeler (BWT) 
    * Cache
* Maintenance des données
    * Lecture et écriture simultanée
    * Conflit dans les mises à jour
    * Parler Section critiques --> très lent
    * Timestamp (Lamport) : vision optimiste
        * Récupération de données (données + timestamp)
        * Écriture si timestamp identique
        * Impossibilité d'une heure commune dans un cluster
    * Exemple : index d'un moteur de recherche
        * Données réparties sur plusieurs machines (résistante à la charge)
        * Même données répliquées sur plusieurs machines (résistance aux pannes)
        * Mise à jour d'un document ? Qui a la version la plus récente ? --> timestamp
        
NoSQL distribué
+++++++++++++++

* Hadoop
    * Distribution des calculs
    * Notion de mapper, reducer
    * Avantage
        * Répartition efficace si calculs indépendant d'une ligne à l'autre
    * Inconvénient
        * Grosses consommations réseau, I/O
        * Pas de communication entre machine
        * Peu de mémoire pour chaque traitement
    * Java, langage évolué, PIG, HIVE, logique proche du SQL
    * Distinguer le système de fichiers distribué (HDFS) du moteur de distribution de job
    * Pas de communication entre machine --> algorithme sur les graphes pas efficaces
    * Mahout
    * Accès très lent aux données --> pas d'index
    * Ordre des lignes dans une table imprévisible
    * Langage fonctionnels très adaptés
    * YARN
* Spark/Graphlab
    * RDD --> effectuer plus de calculs en mémoire
    * Dataframe --> SFrame
    * Cours de Jérémie
    * MLlib
    * Langage evolué --> compilation / optimisation / allocation de machines
* distribuer un traitement de données à différent niveaux
    * avec un langage haut niveau (comme PIG)
    * utilisation du java pour distribuer un job de façon plus optimisée
    * distribution personnalisée d'un traitement avec des librairies bas niveau (type MPI)
* algorithme distribué, descente de gradient distributé
    * exemple des `k-means <http://fr.wikipedia.org/wiki/Algorithme_des_k-moyennes>`_ distribué
    * `GPU <http://fr.wikipedia.org/wiki/Processeur_graphique>`_
        

Structurer les données
++++++++++++++++++++++


**Index**

* Pourquoi indexer ?
    * rechercher une information plus rapidement ( ``SELECT * WHERE <condition>`` )
    * il est possible de créer des index multiples
    * `B-tree <http://en.wikipedia.org/wiki/B-tree>`_ est une structure courante pour représenter un index
* Effets secondaires
    * plus il y a d'index, plus l'insertion et la suppression sont coûteuses
    * parfois il vaut mieux, supprimer l'index, insérer toutes les données à insérer, recréer l'index
* Index sur de grosses bases de données depuis un fichier
    * si deux `accès aléatoire <http://en.wikipedia.org/wiki/Random_access>`_ au même fichier à des données 
      :math:`\rightarrow` il vaut mieux parfois lire toutes les bases (aussi rapide, la tête de lecture fera le même chemin)
    * `Disque SSD <http://fr.wikipedia.org/wiki/Solid-state_drive>`_ - accès lecture réduit, il n'y a plus d'usure physique
    
**Données structurées / non structurées** (`NoSQL <http://fr.wikipedia.org/wiki/NoSQL>`_)

* `schéma de données <http://fr.wikipedia.org/wiki/Sch%C3%A9ma_conceptuel>`_
    * conçu pour éviter la réplication des données
    * une colonne avec des données à choix multiple (départements dans l'exemple) :math:`\rightarrow` 
      replacement par un entier et création d'une table avec départements
    * plus facile de vérifier la validité de données (mauvais départements)
* sans schéma de données
    * on ne s'intéresse plus trop à bien structurer les données
    * un peu plus de duplication d'information, un document est décrit sans table supplémentaire (*self-contained*), 
      gère mieux le bruit lors de la saisie de données
    * on s'intéresse surtout aux recherches qu'on va faire dessus
    * `JSON <http://fr.wikipedia.org/wiki/JavaScript_Object_Notation>`_, `XML <http://fr.wikipedia.org/wiki/Extensible_Markup_Language>`_ : 
      moyen fréquemment utilisé de décrire des structures de données
    * technologie `MongoDB <http://fr.wikipedia.org/wiki/MongoDB>`_
 
**Cohérence** (`wikipedia <http://fr.wikipedia.org/wiki/Coh%C3%A9rence_(donn%C3%A9es)>`_)

* `ACID <http://fr.wikipedia.org/wiki/Propri%C3%A9t%C3%A9s_ACID>`_
    * `relationnelle <http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_relationnelle>`_ - éviter la duplication d'information
    * `transactionnelle <http://fr.wikipedia.org/wiki/Transaction_informatique>`_ - la base n'est pas modifiée tant que la transaction n'est pas terminée
* Cohérence / non cohérence
    * cohérence :math:`\rightarrow` la base n'est pas modifiée en cours de calcul
    * non cohérence :math:`\rightarrow` la base peut être modifiée en cours de calcul mais l'impact est souvent petit
* Coût
    * plus le volume de données est gros, plus c'est coûteux
    * lorsqu'il y a beaucoup de données, la non-cohérence a souvent moins d'impact sur les grandeurs mesurées 
      (exemple : calculer le nombre d'utilisateurs de facebook à t, pas toujours facile à faire car le nombre d'utilisateur
      peut changer en cours de calcul)
      
**Taille des données / représentation des données**

* plus la taille des données est grande, plus la solution choisie doit être adaptée à l'usage qu'on en a, moins il est
  possible de la tordre pour d'autres usages
* exemples :
    * on préfère parfois stocker une chaîne de caractères dans une colonne même si elle représente une liste 
      plutôt que d'ajouter une nouvelle table (pour des questions de performances)


