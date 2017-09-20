
.. blogpost::
    :title: Carré magique (1A) et transformation d'une fonction
    :keywords: carré magique, list
    :date: 2017-09-19
    :categories: imagination

    On veut écrire une fonction qui calcule la somme
    des nombres sur chaque ligne d'un carré magique
    pour s'assurer qu'on a bien la même somme à chaque fois.

    ::

        1 2 3  --> 6
        4 5 6  --> 15
        7 8 9  --> 24

    La première idée est d'écrire quelque chose comme :

    .. runpython::
        :showcode:

        def est_magique(a, b, c, d, e, f, g, h, i):
            l1 = a + b + c
            l2 = d + e + f
            l3 = g + h + i
            if l1 == l2 == l3:
                return True
            else:
                return False

        print(est_magique(1, 2, 3, 4, 5, 6, 7, 8, 9))

    Plus un code est long, plus la probabilité de faire une erreur
    est grande. C'est pourquoi, on préfère toujours un code court.
    La dernière partie de la fonction retourne un booléen qui en fait
    identique à la condition du test dont il dépend. On réduit donc
    les quatre dernières lignes à une seule.

    .. runpython::
        :showcode:

        def est_magique(a, b, c, d, e, f, g, h, i):
            l1 = a + b + c
            l2 = d + e + f
            l3 = g + h + i
            return l1 == l2 == l3

        print(est_magique(1, 2, 3, 4, 5, 6, 7, 8, 9))

    Avoir neuf lettres pour désigner les coefficients est l'assurance
    de se tromper. Une lettre pour désigner l'ensemble, une liste sera
    tout de suite plus lisible.

    .. runpython::
        :showcode:

        def est_magique(coefs):
            l1 = coefs[0] + coefs[1] + coefs[2]
            l2 = coefs[3] + coefs[4] + coefs[5]
            l3 = coefs[6] + coefs[7] + coefs[8]
            return l1 == l2 == l3

        print(est_magique([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    Cela reste quand même fastidieux d'écrire les positions des coefficients.
    Réduisons encore cela avec la fonction :epkg:`*py:python:sum`.

    .. runpython::
        :showcode:

        def est_magique(coefs):
            l1 = sum(coefs[0:3])
            l2 = sum(coefs[3:6])
            l3 = sum(coefs[6:9])
            return l1 == l2 == l3

        print(est_magique([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    C'est mieux mais il reste toujours le problème du copier/coller
    pour chaque ligne. Une boucle devrait résoudre le tout. Il faut
    également adapter la condition finale.

    .. runpython::
        :showcode:

        def est_magique(coefs):
            l123 = [sum(coefs[3*i : 3*i+3]) for i in range(0, 3)]
            return l123[0] == l123[1] == l123[2]

        print(est_magique([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    La dernière condition est toujours longue, on peut la simplifier en disant
    que si le plus petit et le plus grand montant de chaque ligne sont égaux,
    alors ils sont tous égaux.

    .. runpython::
        :showcode:

        def est_magique(coefs):
            l123 = [sum(coefs[3*i : 3*i+3]) for i in range(0, 3)]
            return min(l123) == max(l123)

        print(est_magique([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    Il reste maintenant à changer la fonction pour que celle-ci soit capable
    de traiter des carrés de n'importe quelle dimension. Les nombres ``3``
    vont disparaître. On précise également la dimension du carré comme
    argument de la fonction même si on pourrait la dimension comme
    étant la racine carré de la longueur de la liste en entrée.

    .. runpython::
        :showcode:

        def est_magique(coefs, n):
            # n devrait être égal à len(coefs) ** 0.5
            ln = [sum(coefs[n*i : n*i+n]) for i in range(0, n)]
            return min(ln) == max(ln)

        print(est_magique([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
        print(est_magique([1, 2, 3, 4], 2))

    Le code final est plus concis et plus générique. En supportant plusieurs
    dimensions pour lesquelles on le teste, il est aussi plus robuste. En revanche,
    il est plus lent que la version initiale qui ne fait que les calculs nécessaires.
    La dernière version inclut des opérations implicites mais pourtant bien réelles.
    A chaque itération de boucle, on incrémente un compteur (``i`` par exemple)
    et on vérifie qu'il n'est pas plus grand que le nombre d'itérations
    souhaité. Cela signifie que le code final devrait être deux fois plus lent
    que le code initial. Ce choix lisibilité / performance revient plus
    fréquemment qu'on ne le pense.
    La dernière fonction contient ``n + 3`` boucles. Saurez-vous les identifier ?
