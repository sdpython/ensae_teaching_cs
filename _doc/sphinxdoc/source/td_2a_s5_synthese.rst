
.. _l-td25asynthese:

Quelques notes de la séance 5
=============================

* Index
    * Pourquoi indexer ?
        * rechercher une information plus rapidement ( ``SELECT * WHERE <condition>`` )
        * il est possible de créer des index multiples
        * `B-tree <http://en.wikipedia.org/wiki/B-tree>`_ est une structure courante pour représenter un index
    * Effets secondaires
        * plus il y a d'index, plus l'insertion et la suppression sont coûteuses
        * parfois il vaut mieux, supprimer l'index, insérer toutes les données à insérer, recréer l'index
    * Index sur de grosses bases de données depuis un fichier
        * si deux `accès aléatoire <http://en.wikipedia.org/wiki/Random_access>`_ au même fichier à des données 
          :math:`rightarrow` il vaut mieux parfois lire toutes les bases (aussi rapide, la tête de lecture fera le même chemin)
        * `Disque SSD <http://fr.wikipedia.org/wiki/Solid-state_drive>`_ - accès lecture réduit, il n'y a plus d'usure physique
* Données structurées / non structurées (`NoSQL <http://fr.wikipedia.org/wiki/NoSQL>`_)
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
* `Cohérence <http://fr.wikipedia.org/wiki/Coh%C3%A9rence_(donn%C3%A9es)>`_
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
* Taille des données / représentation des données
    * plus la taille des données est grande, plus la solution choisie doit être adaptée à l'usage qu'on en a, moins il est
      possible de la tordre pour d'autres usages
    * exemples :
        * on préfère parfois stocker une chaîne de caractères dans une colonne même si elle représente une liste 
          plutôt que d'ajouter une nouvelle table (pour des questions de performances)


