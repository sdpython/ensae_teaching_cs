

Projets informatiques
=====================

**Cette page est en cours de rédaction.**


Sujets proposés année 2014-2015
-------------------------------

Les sujets proposés abordent différents domaines connexes aux enseignements proposés à l'ENSAE
(finance, statistique, économie) et quelques jeux.
Tous les projets proposés sont des suggestions, les élèves sont libres d'élaborer un sujet de leur choix
ou de s'inspirer des énoncés ci-dessous à la condition de le faire valider par un encadrant.
L'encadrant se réserve le droit de proposer des modifications si le même sujet est 
choisi par un trop grand nombre d'élèves. Afin d'avoir un premier suivi productif, 
il est conseillé de parcourir les références bibliographiques suggérées. 


.. toctree::
    :maxdepth: 1

    projets/p_finance
    projets/p_data_folie



Travail attendu
---------------

Le projet dure quatre mois au second semestre (de février à mai). Il se conclut par un programme
et un rapport. Une soutenance suit mi-juin. 
Le rapport doit souligner la contribution originale des élèves, 
illuster les résultats numériques obtenus et la 
façon dont ils ont été obtenus. On suppose que le rapport s'adresse à un public expert.
La soutenance doit reprendre les points principaux, 
décrire brièvement la façon dont le travail a été réparti
au sein de l'équipe. On suppose que la soutenance s'adresse à un public non-expert.

Chaque projet, quelque soit le sujet, devra comporter une **composante numérique** 
(statistique, économique, financière, ...), que ce soit une stratégie de trading,
l'optimisation d'une intelligence artificielle pour un jeu, une simulation économique.
Cet aspect devra ressortir lors de la rédaction du rapport final qui devra exposer les résultats
numériques obtenus et faire au moins une ou deux allusions à la façon dont ces calculs ont 
été implémentés. Le rapport doit contenir les éléments suivants :

    - le coût de votre ou de vos algorithmes
    - un ou plusieurs résultats numériques (pour une optimisation de porte-feuille, on
      s'attend à voir un porte-feuille)
    - 1 page ou plus qui détaille un aspect technique de votre projet
      
    
Chaque sujet précisera d'autres éléments (code, résultats) attendus
lors du rendu final. Vous trouverez également quelques erreurs à éviter.







Références
----------

**Articles de blogs**

    * `Deux ou trois choses à vérifier avant de rendre un projet informatique <http://www.xavierdupre.fr/blog/2014-05-14_nojs.html>`_
    * `Récupérer des données financières <http://www.xavierdupre.fr/blog/2014-05-04_nojs.html>`_
    * `Travailler à plusieurs sur le même projet informatique <http://www.xavierdupre.fr/blog/2014-02-12_nojs.html>`_
    * `Quelques précisions sur les projets informatiques <http://www.xavierdupre.fr/blog/2013-02-03_nojs.html>`_
    * `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_ 
    * `Frameworks for games in Python <http://www.xavierdupre.fr/blog/2014-01-01_nojs.html>`_
    
**Resources**

    * `données <http://www.xavierdupre.fr/site2013/enseignements/projets/donnees/>`_
    * `bibliographie <http://www.xavierdupre.fr/site2013/enseignements/projets/biblio/>`_     
    * `Barème indicatif des projets informatiques (année 2012-2013) <http://www.xavierdupre.fr/site2013/enseignements/bareme.html>`_
    * `Barème indicatif des projets informatiques (année 2013-2014) <http://www.xavierdupre.fr/site2013/enseignements/bareme-2014.html>`_
    



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


3 oublis dans le rapport
------------------------

Le code qu'on a jeté
++++++++++++++++++++

Lorsqu'on fait un projet de la sorte, il arrive souvent qu'on jette du code qu'on a écrit.
On découvre parfois que le programme tel qu'il est conçu ne permet pas de faire
tel ou tel chose, il faut en réécrire une partie. On écrit parfois du code jetable
lorsqu'on a besoin d'un résultat numérique. Une fois celui-ci obtenu, on l'intègre
au programme et on jette le code qui a permis de l'obtenu.

C'est parfois utile dans votre rapport de décrire ces codes jetés. Dans le premier cas,
le code jeté sert de justification au nouveau. Dans le second cas, cela rassure de voir 
que certains résultats ne sortent pas de nulle part.

Qu'avez-vous appris ?
+++++++++++++++++++++

Certaines conclusions mentionnent le fait qu'on apprend beaucoup à faire un projet informatique,
seul, sans aide extérieure. On apprend autant que durant des séances de travaux pratiques.
C'est un des objectifs de l'exercice : apprendre à maîtriser cet outil qu'est la programmation.


Mais ce projet demande aussi une part d'imagination, que ce soit pour concevoir une fonction d'évaluation
pour une intelligence artificielle, une simulation économique réaliste, une stratégie financière...
Tout au long de la mise en place de ses idées, on s'aperçoit que les premiers jets sont parfois
un peu naïf, que les premiers résultats numériques ne sont pas aussi bons qu'escomptés.
Il faut retravailler l'idée initiale. Cette partie doit ressortir dans votre rapport et elle
doit bien ressortir. 

Qu'est-ce que le lecteur va retenir ?
+++++++++++++++++++++++++++++++++++++

Expliquer les choses, les illustrer, choisir le bon graphique, le bon tableau,
pour défendre une idée n'est pas toujours simple. Il faut parfois imaginer qu'un rapport
sera lu deux fois, une fois en diagonale, une autre plus sérieusement. 

Il faut se poser la question de savoir ce que vous voulez que le lecteur
retienne.

Un programme informatique est d'autant
plus difficile à cerner qu'il est long. Le rapport est la version la plus accessible de votre
travail. C'est le point de départ. A partir de là, on navigue plus aisément dans votre programme.



**Un example :**

La phrase suivante est tirée d'un rapport à propos d'un jeu :


    *Au niveau 2 de difficulté, on choisit à nouveau notre propre intelligence 
    artificielle mais en choisissant cette fois-ci de bons paramètres.*


De cette phrase, je comprends que certains paramètres ont été optimisés mais 
le rapport ne revient jamais sur cet aspect. Donc :

    * Je dois deviner quelle partie du programme a servi à cela, si toutefois le code est encore là.
      Je vois bien un fichier qui correspond mais il ne marche pas (ou plus). Je ne suis pas sûr
      d'avoir envie de le débugger.
    * Je ne sais pas quels sont ces paramètres, je n'ai aucune idée des résultats obtenus,  
      ni même que la différence de niveau entre les bons paramètres et les mauvais.
    * Je comprends qu'un travail d'optimisation a été effectué mais je n'ai aucune idée
      de l'importance qu'il revêt. Si le rapport n'en fait pas mention, c'est sans doute
      que cela n'est qu'une contribution minime.





