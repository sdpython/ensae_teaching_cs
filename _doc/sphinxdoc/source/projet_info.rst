

Projets informatiques
=====================

**Cette page est en cours de rédaction.**


Sujets proposés année 2014-2015
-------------------------------

Les sujets proposés abordent différents domaines connexes aux enseignements proposés à l'ENSAE
(finance, statistique, économie) et quelques jeux : :ref:`l-projetsinformatiques`.

N'oubliez pas de lire la suite cette page qui donne quelques informations utiles
afin de réaliser un bon projet.


Contraintes
-----------

Chaque projet, quelque soit le sujet, devra comporter une **composante numérique** 
(statistique, économique, financière, ...), que ce soit une stratégie de trading,
l'optimisation d'une intelligence artificielle pour un jeu, une simulation économique.
Cet aspect devra ressortir lors de la rédaction du rapport final qui devra exposer les résultats
numériques obtenus et faire au moins une ou deux allusions à la façon dont ces calculs ont 
été implémentés.

Le rapport doit contenir les éléments suivants :
    - le coût de votre ou de vos algorithmes
    - un ou plusieurs résultats numériques (pour une optimisation de porte-feuille, on
      s'attend à voir un porte-feuille)

Rendu
-----

Le projet dure quatre mois au second semestre (de février à mai). Il se conclut par un programme
et un rapport. Une soutenance suit mi-juin. 



Article de blogs
----------------

    * `Deux ou trois choses à vérifier avant de rendre un projet informatique <http://www.xavierdupre.fr/blog/2014-05-14_nojs.html>`_
    * `Récupérer des données financières <http://www.xavierdupre.fr/blog/2014-05-04_nojs.html>`_
    * `Travailler à plusieurs sur le même projet informatique <http://www.xavierdupre.fr/blog/2014-02-12_nojs.html>`_
    * `Quelques précisions sur les projets informatiques <http://www.xavierdupre.fr/blog/2013-02-03_nojs.html>`_
    * `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_ 
    * `Frameworks for games in Python <http://www.xavierdupre.fr/blog/2014-01-01_nojs.html>`_
    
Resources
---------

    * `données <http://www.xavierdupre.fr/site2013/enseignements/projets/donnees/>`_
    * `bibliographie <http://www.xavierdupre.fr/site2013/enseignements/projets/biblio/>`_     
    * `Barème indicatif des projets informatiques (année 2012-2013) <http://www.xavierdupre.fr/site2013/enseignements/bareme.html>`_
    * `Barème indicatif des projets informatiques (année 2013-2014) <http://www.xavierdupre.fr/site2013/enseignements/bareme-2014.html>`_
    
Rapport / Programme / Soutenance
--------------------------------

Chaque projet doit inclure une composante numérique telles que celles enseignées à l'ENSAE 
(statistique, économique, financière). 
Le rapport doit souligner la contribution originale des élèves, illuster les résultats numériques obtenus et la 
façon dont ils ont été obtenus. On suppose que le rapport s'adresse à un public expert.
La soutenance doit reprendre les points principaux, décrire brièvement la façon dont le travail a été réparti
au sein de l'équipe. On suppose que la soutenance s'adresse à un public non-expert.



3 erreurs de design fréquentes
------------------------------

Ce ne sont pas à proprement parler des erreurs car elles n'altèrent pas l'exécution du programme.
Toutefois elles le rendent plus difficile à lire et à corriger en cas d'une *vraie* erreur.
La plupart des développeurs les font lorsqu'ils apprennent à programmer et ne les font plus par la suite.


Un seul gros fichier
++++++++++++++++++++

Chaque année, je vois plusieurs projets informatiques implémenter en un seul gros fichier. 
C'est sans doute dû au fait que, lorsqu'on travaille à deux ou trois, il est plus facile de s'échanger un 
seul fichier que plusieurs. Je remarque d'ailleurs que les "groupes" d'un élève font créent plus souvent 
plusieurs fichiers. 

Lorsqu'on développe un jeu, il est préférable de séparer la partie affiche de la partie
intelligence artificielle, il est encore mieux de les mettre dans deux fichiers séparés. La partie
IA sera considéré comme un module et la partie affichage comme le programme principal.

Pour éviter l'envoi continu de mail entre deux membres du même groupe, le meilleur recours est
l'emploi d'un logiciel de suivi de source. `GitHub <https://github.com/>`_ est une possibilité.
C'est celle que j'utilise pour développer ce cours : `sdpython/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs>`_.
Cela permet de suivre les modifications (`un commit <https://github.com/sdpython/ensae_teaching_cs/commit/796dcc695006f9bba44b649cb256f80c91f3a72b>`_),
ou de revenir en arrière.

Le copier/coller de plus de 10 lignes pour changer un caractère
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Je schématise un peu. Concrètement, lorsqu'on programme un jeu à deux joueurs, on
fait des choses pour le premier joueur dans un bloc de code qu'on recopie pour l'autre
joueur avec quelques modifications subtiles ::

    if joueur == 1 :
        next_joueur = 2
        proba_1[eta_succ[U-1]]=1
        proba_2[eta_succ[U-1]]=0
        proba_2[eta_succ[U-2]]=0
        proba_1[sym(eta_succ[U-1])]=1
        proba_2[sym(eta_succ[U-1])]=0
        proba_2[sym(eta_succ[U-2])]=0
    else :        
        next_joueur = 1
        proba_2[eta_succ[U-1]]=1
        proba_1[eta_succ[U-1]]=0
        proba_1[eta_succ[U-2]]=0
        proba_2[sym(eta_succ[U-1])]=1
        proba_1[sym(eta_succ[U-1])]=0
        proba_1[sym(eta_succ[U-2])]=0
    
Ceci est à éviter le plus possible. Cela allonge inutilement les programmes mais surtout cela 
oblige développeur à répercuter une modification sur tous les blocs recopiés. Et on se trompe souvent.
Dans ce cas précis, il est facile d'écrire ::

    if joueur == 1 :
        pr1,pr2 = proba_1,proba_2
    else :
        pr1,pr2 = proba_2,proba_1
            
    next_joueur = 3 - next_joueur
    pr1[eta_succ[U-1]]=1
    pr2[eta_succ[U-1]]=0
    pr2[eta_succ[U-2]]=0
    pr1[sym(eta_succ[U-1])]=1
    pr2[sym(eta_succ[U-1])]=0
    pr2[sym(eta_succ[U-2])]=0

Et si on est vraiment pointilleux ::

    pr1,pr2 = proba_1,proba_2 if joueur == 1 else proba_2,proba_1
            
    next_joueur = 3 - next_joueur
    eu_1 = eta_succ[U-1]
    seu_1 = sym(eta_succ[U-1])
    
    pr1[eu_1]=1
    pr2[eu_1]=0
    pr2[eta_succ[U-2]]=0
    pr1[seu_1]=1
    pr2[seu_1]=0
    pr2[sym(eta_succ[U-2])]=0


Les variables globales
++++++++++++++++++++++

Elles sont pratiques :

    * On y met les paramètres d'une simulation ou l'état d'un jeu de poker.
    * On n'a pas besoin de les transmettre comme paramètres à chaque fonction.
    
Ce choix simple peut devenir ennuyeux par la suite lorsqu'on souhaite faire 
tourner plusieurs le même programme en changeant ces variables globales.
Pour éviter cela, le plus simple est de créer une classes qui les contient toutes et
de passer une instance de cette classe à chaque fonction qui en a besoin ::

    class VariablesGlobales :
        def __init__(self):
            self.epsilon = 0.01
            self.alpha = 0.5
            self.iter = 1000
            # ...
            
    variable = VariablesGlobales ()
    
    def fonction_qui_en_a_besoin( varglob) :
        s = varglob.alpha
        for i in range(0,varglob.iter):
            # ...


.. toctree::

    projets/listesp