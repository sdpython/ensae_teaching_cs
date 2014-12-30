
.. _l-simulation:

Simulations économiques, sociales
=================================

Assez proches des algorithmes génétiques dans l'implémentation, les simulations
permettent à partir de règles simples sur le comportement des individus d'obtenir
des résultats sur l'ensemble d'une population. Le projet doit comporter les élémens suivants :

* Description du problème et des interactions entre individus
* Réalisation d'une simulation réduite pour vérifier que le programme donne des résultats numériquement fiables
  et cohérents avec l'intuition qu'on a du problème (lire `Common sense and statistics <http://andrewgelman.com/2014/12/25/common-sense-statistics/>`_)
* Réalisation de simulations plus poussées
* Analyse des résultats obtenus avec le programme, comparaison avec la réalité

.. _l-sim-segre:

Simuler la ségégation sociale
-----------------------------

L'article suivant `La ségrégation, comment ça marche ? <http://www.letemps.ch/interactive/2014/polygones/>`_ 
(version originale `Parable of the polygons <http://ncase.me/polygons/>`_) montrer comment 
une forme de ségrégation spatiale s'installe dans une ville à partir d'une règle assez simple : on préfère
avoir des voisins qui nous ressemblent.

.. _l-sim-panique:

Simulation d'une foule en panique
---------------------------------

Les trois articles abordent le comportement d'une foule pour appréhender son mouvement en
cas de panique par exemple. 

* `Self-Organized Pedestrian Crowd Dynamics <http://itp.uni-frankfurt.de/~gros/JavaApplets/PedestrianCrowdDynamics/PedestrianApplet.html>`_
* `Simulation of Pedestrian Crowds in Normal and Evacuation Situations <http://www.pmcorp.com/Portals/5/_Downloads/Simulation%20of%20Pedestrian%20Crowds%20in%20normal%20and%20evacuation.pdf>`_, Dirk Helbing, Anders Johansson
* `Pedestrian,Crowd and EvacuationDynamics <http://www.ethlife.ethz.ch/archive_articles/100727_Massenpanik_Helbing_sch/Pedestrian_Crowd_and_Evacuation_Dynamics_Helbing.pdf>`_, Dirk Helbing, Anders Johansson
* `Modélisation 2D discrète du mouvement des piétons : application à l'évacuation des structures du génie civil et à l'interaction foule-passerelle <https://tel.archives-ouvertes.fr/pastel-00674774/document>`_, thèse de Philippe Pecol
* `Modélisation mathé´matique des mouvements de foule <https://ensiwiki.ensimag.fr/images/4/40/TER_Rapport_Spanneut.pdf>`_, Aurélia Spanneut
* `Un modèle de suivi réaliste pour la simulation de foules <http://www.google.fr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CCYQFjAA&url=http%3A%2F%2Fwww.irit.fr%2FREFIG%2Findex.php%2Frefig%2Farticle%2Fdownload%2F110%2F59&ei=LBWjVKi3JciuU6SZhJgL&usg=AFQjCNHEh-_tFRxGRPaQgRMC5FbdqqUSMg&sig2=nDdDPQfu41xdBDCG_1DQGQ&bvm=bv.82001339,d.d24>`_, Samuel Lemercier et al

On pourra commencer par simuler une foule au repos dans une salle carrée avec une seule issue
puis à créer un mouvement panique (un incendie par exemple).
