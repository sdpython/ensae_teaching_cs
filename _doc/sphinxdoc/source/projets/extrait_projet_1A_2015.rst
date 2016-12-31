
.. index:: 2015, projet, 1A, extrait

.. _l-extrait-projet-1A-2015:

Extraits des projets informatiques de première année à l'ENSAE en 2015
======================================================================

Les élèves ont exprimé de belle façon ce que les projets informatiques leur ont apporté.
Je reprends ici avec leur accord quelques passages.

**tâtonner**

*L'une des choses essentielles que nous avons apprises de ce projet est qu'il n'existe pas de
solution ou de justification théorique à tous les problèmes. En effet, dans de nombreux
cas, les seuls recours possibles sont notre propre imagination et les tests empiriques sur
des données réelles.*

**nom des variables**

*Tout d'abord, nous avons fait un effort sur le nom des variables.
Cela peut sembler bête, mais comme pour nous deux c'était notre premier code,
c'était loin d'être évident. Mais très vite nous nous sommes rendus compte que ce
n'était pas possible d'appeler nos fonctions* f1, f2, .. *et nos variables* x,y,z.
*Nous nous sommes donc renseignés sur ce qui se faisait dans la programmation de manière générale.
Ainsi nos noms de fonctions sont devenus bien plus compréhensibles.
Cela nous a été d'autant plus utile que nous travaillons à deux.*

**succession de détails**

*Nous avons ensuite essayé d'écrire certaines parties de notre code en moins de lignes.
En effet, pour beaucoup de fonctions nous les avions écrites une première fois. Mais au fur
et à mesure que notre programme avançait, nous devions les rallonger.*

**débugger**

*Ce projet nous a appris la patience. Parfois debugger était fastidieux mais là aussi nous avons
appris à être plus performant, à progresser pas à pas dans le problème pour identifier la provenance
du problème et il nous arrivait par la suite d'être plus rassurés par un message d'erreur que par des
sorties aberrantes. D'autant plus que lorsque l'on fait jouer 1000 parties à la machine, tous les cas
pathologiques pour des fonctions que l'on aurait éventuellement mal écris ce rencontrent et la loi
Murphy est plus que jamais vérifiée. Le stack viewer qui permet de connaître toutes les valeurs des
variables locales au moment du bug nous a été une aide précieuse.
L'erreur qui nous a fait perdre le plus de temps est sans doute les problèmes causés par
l'assignement par valeur et par référence entre autre dans la partie de programme suivante* ::

    def coup(self):
      matrice=self.début[len(self.début)-1];
      j=maxp(self.début[len(self.début)-1])
      matrice[j]=1
      self.début.append(matrice)

**choix**

*Notre grand regret est d'avoir essayé pendant trop longtemps de faire une interface graphique.
Cela nousa fait perdre beaucoup de temps et nous a empêché de faire des IA beaucoup plus
compétitives.*

**lisibilité**

*Nous voyons donc ici l'aspect peu agréable de cette méthode
comparativement à celle des dictionnaires utilisée dans le code final. Ainsi un dictionnaire vaut
mieux que 25000* if.

**évolution**

*Parmi les éléments importants dégagés tout au long de notre projet, nous avons pu
constater qu'un projet informatique était loin d'être simplement l'alignement les unes à la suite
des autres de lignes de codes, de boucles if, de tests. Il s'agit plutôt d'un projet qui évolue, qui
se construit, parfois certaines parties sont complètements éradiquées, d'autres ont plutôt un
caractère « jetable », permettant l'amélioration du code.*

**avancer**

*Ce projet m'a également permis de comprendre qu'il faut, non seulement coder l'algorithme
permettant de réaliser telle ou telle tâche, mais surtout le pousser plus loin, tester chaque étape,
illustrer chaque résultat et tenter d'optimiser au mieux le processus.*

**début**

Conseils de deux novices :

#. *Parfois il faut savoir quand faire une pause.*
#. *Les bugs les plus ennuyants sont parfois causés par une faute de frappe ou une erreur
   négligeable, Ton ami ? Les* print *partout pour localiser le ou les problèmes.*
#. *Programmer, c'est avoir un problème compliqué ou un but général à atteindre, il faut le
   décomposer en unités et essayer de les résoudre une par une. Le problème, c'est qu'on
   risque de perdre le fil de ses idées et qu'on ne peut savoir si la méthode fonctionne qu'à la
   fin du programme ou du moins la fin d'une étape majeure, on ne peut pas voir les résultats
   de ses efforts à fur et à mesure que l'on avance ce qui risque d'être bouleversant… Morale
   de l'histoire : La patience.*
#. *La programmation apprend en quelque sorte l'autonomie.*
#. *C'est en se noyant que l'on apprend finalement à nager.*

**duplication**

*Etant donné mon projet et son caractère quelque peu expérimental,
ce que j'ai le plus appris de mes erreurs est l'importance d'écrire du code
modulaire et sans duplication.*

**variables globales**

*Les modifications des paramètres du modèle doivent s'effectuer dans les différents fichiers python,
nous n'avons appris que trop tard l'utilisation de variables globales ne nous permettant pas d'en faire
une implémentation propre.*

**design**

*La nécessité de planifier méthodiquement les implémentations à l'avance : le coût d'une
modification est proportionnelle à la taille du code, avec les nombreuses interactions à modifier et
aussi un risque d'apparition d'erreurs difficilement trouvables. En effet, une petite erreur nous coûta
un temps monstrueux : en remaniant les différentes fonctions de téléchargement afin que celles-ci
prennent toutes en argument un string et non pas parfois un datetime, nous avons oublié de
modifier la fonction vérifiant que le cours est déjà dans la liste de recensement : à chaque appel les
cours étaient téléchargés et ajoutés une fois de plus au tableau de recensement. Cela rendait le
temps de calcul trop long lors de l'appel de la fonction créant les tableaux de résultats, si bien que
pendant un bon moment nous avons cherché l'erreur en faîtes de ce coté, jusqu'à nous apercevoir de
la taille du tableau de recensement.*

**idées**

*L'avantage de l'informatique est que tant qu'il y a des idées il y a des choses à programmer.*

**fiabilité**

*Nous retenons de cette expérience la nécessité de bien tester et réfléchir le code
implémenté, finalement la mise en place des algorithmes n'occupe qu'une faible partie du temps
face à la réflexion pour bien les comprendre et les tester.*

**avancer, mémoriser, avancer, ...**

*J'ai commencé
à tracer directement des graphiques à partir de cet algorithme, et petit à petit
je me suis rendue compte qu'il serait intéressant de tester aussi quel serait le
résultat avec des probabilités de croisement différentes, et en choisissant le lieu
de ces croisements de manière aléatoire. Résultat : il fallait refaire tous les graphiques
(ce qui peut mettre pas mal de temps dès qu'on fait des mesures jusqu'à
n = 100... ). J'ai donc commencé à enregistrer les données au fur et à mesure
pour ne pas perdre de temps à les refaire si je voulais changer mes graphiques.*

**design**

*Ce projet nous a permis d'apprendre de nombreuses choses dans la façon de procéder
lorsque l'on souhaite réaliser des programmes plus complexes que ce que nous avions fait
jusque là. Nous nous étions dès le début obligés à travailler de façon claire et modulaire,
de sorte que le code qui était réalisé par l'un des membres du groupe puisse être compris
facilement et réutilisé par l'autre. Nous avons donc choisi de nous répartir le travail et
d'écrire de nombreuses petites fonctions qui réalisent de petites taches au sein de notre
projet. De sorte que chacun puisse réaliser de nombreux tests dans plusieurs fichiers différents,
nous avons limité le nombre de variables globales définies en dehors de nos fonctions.*

**répétitions des calculs**

*Il s'est donc avéré que nous devions réaliser en début de plusieurs fonctions la même
tâche (par exemple, essayer de récupérer les cours des actifs sur Internet et sélectionner la
liste de ceux qui ont pu effectivement être récupérés). De plus, nos fonctions qui tracent
nos graphiques finaux (objectif principal de notre projet) réutilisent toutes ces petites
fonctions au cours de leur execution. Au moment de les utiliser, nous avons donc réalisé
que les temps d'exécution étaient incroyablement longs : il a donc fallu réfléchir à la façon
d'optimiser les calculs en supprimant les calculs qui sont effectués plusieurs fois par des
fonctions différentes.*

**apprentissage**

*Etant donné que ce programme est mon premier projet informatique, il a été assez
laborieux. Au delà d'une erreur en particulier, c'est d'abord l'ensemble du programme
qui m'a permis de gagner en aisance et en autonomie dans le langage python.*

**documentation**

*Ma seconde erreur a sous doute été la frugalité de mon programme en terme de
documentation. Quand j'ai recommencé à travailler sur mon code après deux mois de
pause, je me suis rendu compte de l'intérêt d'une documentation précise, surtout quand
mon programme passe fréquemment des listes de tuplets aux listes, en passant par les
tuplets. Les dépendances d'une fonction à une autre sont bien mieux maitrisées.*

**idées**

*La leçon une est : Pour se lancer dans un projet de programmation, il ne faut pas attendre qu'une idée de
génie nous tombe du ciel, il vaudrait mieux commencer par le plus simple, la progression vient toute seule.*

**design**

*Lorsque la simulation était réussie, j'ai transformé le fichier en fonction pour la
mettre dans une boucle afin de générer plusieurs expériences pour tracer les courbes. Or, les variables globales
(précisément la liste des personnes) était une variable globale qui n'était pas initialisée d'une simulation à
l'autre au sein de la boucle. Ceci engendrait un programme qui ne répondait pas après quelques simulations.
La solution était donc de créer une classe qui définit toutes les variables globales et de les utiliser en définissant
une instance de cette classe. Ceci dit, il m'a fallu deux semaines de pause et un suivi pour me relancer !*

*Leçon : Toujours toujours éviter les variables globales ! Pour ce genre de projet où il faut impérativement
les utiliser (taille de la fenêtre pygame, constantes tels que la taille des objets etc ...), créer une classe pour
les définir : l'objet, ça peut vous sauver !*

**tabulations**

*Une autre erreur dont nous n'oublierons pas de tirer de bonnes habitudes concerne la rédaction :
utiliser les espaces et non les tab pour l'indentation du code. En effet nous avons
perdu énormément de temps à nous débattre avec l'indentation du fait de la différence de compilateurs.*

**travailler à plusieurs**

*Plusieurs fois nous nous sommes
retrouvé à avoir codé de deux manières différentes des parties de programme
qui faisaient la même chose parce que nous n'avions pas assez segmenté notre
travail. Ce travail nous a montré qu'il n'est pas facile de programmer à plusieurs
sur un même projet. Nous regrettons d'ailleurs de ne pas avoir réussi à
plus nous familiariser avec des outils de programmation en équipe.*

**les classes**

*Au premier abord, après le sentiment
de lassitude à l'idée de tout recoder depuis le début, nous n'avons pas vu l'intérêt des classes.
Néanmoins, avec le recul, nous avons compris l'importance de celles-ci. En effet, nous avons
découvert que les classes ont plusieurs utilités.
En un mot, nous avons compris toute l'importance d'utiliser des classes !*

**imagination**

*La principale leçon tirée de nos erreurs est le fait de ne pas se poser de limites en
travaillant.*
