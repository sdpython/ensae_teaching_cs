
.. blogpost::
    :title: Le design d'un code informatique
    :keywords: design, programmation
    :date: 2015-05-22
    :categories: programmation
    :lid: blog-design-program

    On écrit rarement un programme au hasard et même si ça
    paraît évident et logique, on fait du *design*.

    En construction par exemple, on place un tuyau qui doit traverser un mur avant
    de couler le béton (ou une forme lui ressemblant).
    Si on ne le fait pas, on doit percer un trou et ça coûte cher.

    On n'écrit pas le même programme si on sait qu'on doit faire jouer
    l'ordinateur contre lui-même. On ne peut pas mélanger le code à l'interface graphique.
    Est-il simple de transformer une constante en paramètre ?
    Souhaite-t-on en garder la possibilité ?
    Ce sont des questions qu'on se pose au début de la conception
    d'un programme afin d'éviter de trop grands changements
    plus tard.

    .. index:: variable globale

    Lorsqu'on programme un calcul numérique, le besoin de lancer
    celui-ci à grande échelle survient inévitablement. Le calcul
    est facile à lancer sur un jeu de données et il faudra le lancer
    sur des milliers de jeux de données. Presque toujours, l'utilisation
    des variables globales est un grand frein.

    Autre exemple, le même calcul numérique fonctionne
    avec des données récupérées depuis un fichier texte.
    Est-il facile de changer la source ? De les récupérer depuis
    Internet sans les enregistrer sur le disque ? Depuis des données
    stockées en mémoire ? On se pose presque toujours
    la question de la multiplicité **après** avoir commencé
    au moment où on s'aperçoit qu'il faut changer beaucoup de choses
    car on n'y avait pas pensé.

    Pour résumer, on s'intéresse au design d'un programme quand
    on souhaite anticiper sur ses besoins futurs afin d'éviter
    d'avoir à tout recoder ensuite. Il est beaucoup plus simple
    d'intégrer à son code les tests unitaires et la documentation
    dès le début plutôt que de les ajouter après coup.

    On écrit une fonction qui fait *A* et *B* puis on en a besoin
    d'un autre qui fait *A* et *C*. Deux ou trois fonctions ?
