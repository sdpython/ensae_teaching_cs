

.. index:: examens, algorithme

.. _l-examens-1A-algo:


Etude d'un algorithme en binôme
===============================

Les algorithmes sont le plus souvent abordés hors contexte
bien qu'ils soient présents dans n'importe quelle application
smartphone. 


.. contents::
    :local:

Mise en scène
+++++++++++++

Le jeu `Pokémon Go <https://fr.wikipedia.org/wiki/Pok%C3%A9mon_Go>`_ 
est sorti début 2016. Les détails de l'implémentation en sont pas connus
mais cela n'empêche pas d'y réfléchir. 

Les élèves seront groupés par deux, un élève plutôt débutant,
un autre plutôt pas, ils tirent un algorithme ou une structure de données
au hasard et doivent déterminer où il intervient dans les petites histoires décrites
au paragraphe suivant. Les élèves devront ensuite l'implémenter,
cela ne devrait pas dépasser 20 lignes.

5 points seront attribués à cet exercice pour cinq tâches :

#. Associer l'algorithme à la bonne étape de l'histoire.
#. Implémentation en Python.
#. Résultats sur un exemple fabriqué.
#. Impact économique si l'algorithme est deux fois plus rapide.
#. Une piste d'amélioration pour l'application considérée.



Scénarios
+++++++++

Une personne sort son téléphone. Il ouvre l'application
*Trésor Caché*. L'écran lui montre ce qui l'a devant lui
comme s'il allait prendre une photo. 
Ces histoires sont fictives.

**histoire 0**

#. L'utilisateur s'authentifie.

**histoire 1**

#. Il balaye devant lui.
#. L'application cherche si un trésor est virtuellement caché
   devant lui.
#. La position d'un des trésor correspond. 
   L'application affiche ses caractéristiques.
#. L'utilisateur *swipe* et stocke le trésor dans son
   coffre fort virtuel.
#. L'application envoie l'information aux ordinateurs
   des créateurs de l'application. Elle envoie également l'image
   du paysage où le trésor a été attrapé.
#. Ces ordinateurs détermine si le joueur a gagné.
   Mais il n'a pas gagné.
   
**histoire 2**

#. Le trésor a volontairement été placé par les concepteurs 
   de l'application en hauteur au niveau de la pancarte du nom de la rue.
#. Les ordinateurs distants extraient la zone de l'image correspondant à cette pancarte.
#. Ils lancent une reconnaissance OCR pour lire le nom écrit sur cette pancarte.
#. Ils comparent à une liste de noms rues mais il ne s'y trouve pas.
#. Le moteur de reconnaissance de l'écriture fait parfois des erreurs,
   Ils lancent alors un moteur qui corrige les fautes d'orthographes
   automatiquement. Une seconde recherche est lancée.
   La rue est trouvée, elle n'a a priori pas changé de nom.
#. Une dernière validation est effectuée. Une distance est calculée
   entre le nom de rue reconnu et le nom de rue corrigé. 
   La distance n'est pas trop grande. Aucune vérification manuelle
   n'est requise.
   
**histoire 3**

#. Le joueur est impatient, il demande une suggestion pour 
   le prochain trésor.
#. L'application récupère l'information stockée pendant que le joueur
   joue. Il envoie cette information au serveur des concepteurs.
#. Ceux-ci déterminent trois trésors proches et non découverts.
#. Ils sélectionnent trois magasins autour des trésors.
#. Ils mettent aux enchères le profil de l'utilisateur.
#. 5 magasins font une offre. Le meilleur est choisi.
#. L'utilisateur reçoit le message qu'un indice se trouve dans ce magasin.
#. L'application lui indique le chemin le plus court jusqu'au magasin.
#. L'utilisateur partage l'indice avec ses amis sur l'application.
   
**histoire 4**

Le jeu marche très bien mais finit par provoquer une certaine lassitude.
Les concepteurs du jeu ont quelques idées. L'une d'elles 
est d'associer une récompense à chaque trésor comme des bons de réductions.

#. Sans le savoir certains utilisateurs bénéficient de cette option,
   d'autres pas.
#. On compare ces deux populations sur un mois en mesurant le temps de jeu
   moyen par joueur.
#. L'idée est finalement validée.


Algorithmes implémentables
++++++++++++++++++++++++++

* `Branch and Bound <https://fr.wikipedia.org/wiki/S%C3%A9paration_et_%C3%A9valuation>`_
* `Cryptographie <https://en.wikipedia.org/wiki/Message_authentication_code>`_
* `Distance d'édition <https://fr.wikipedia.org/wiki/Distance_de_Levenshtein>`_
* `Enchères de Vickrey <https://fr.wikipedia.org/wiki/Ench%C3%A8re_de_Vickrey>`_,
  `Mécanisme de Vickrey-Clarke-Groves <https://fr.wikipedia.org/wiki/M%C3%A9canisme_de_Vickrey-Clarke-Groves>`_
* `Plus court chemin <https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra>`_
* Recherche dans un `index <https://fr.wikipedia.org/wiki/Index_(base_de_donn%C3%A9es)>`_
* `Test A/B <https://fr.wikipedia.org/wiki/Test_A/B>`_ 
  plus  spécifiquement `P-Value <https://fr.wikipedia.org/wiki/Valeur_p>`_
* `Tri <https://fr.wikipedia.org/wiki/Algorithme_de_tri>`_

Machine learning
++++++++++++++++

Ces modèles sont utilisés dans l'une des histoires mais
il n'est pas demandé de les implémenter.

* `réseau de neurones <https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels>`_,
  `OCR <https://fr.wikipedia.org/wiki/Reconnaissance_optique_de_caract%C3%A8res>`_
* `Système de recommandation <https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_recommandation>`_
