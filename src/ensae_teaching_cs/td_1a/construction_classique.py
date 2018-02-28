# -*- coding: utf-8 -*-
"""
@file
@brief Quelques constructions classiques pour éviter de recoder des variantes d'algorithmes.
classiques.
"""

from functools import reduce


def recherche(li, c):
    """
    Retourne l'index d'un élément ou -1 si non trouvé

    @param      li      liste
    @param      c       élément à trouver
    @return             position

    .. exref::
        :tag: Base
        :title: recherche avec index

        Lorsqu'on cherche un élément dans un tableau, on cherche plus souvent
        sa position que le fait que le tableau contient cet élément.

        .. runpython::
            :showcode:

            def recherche (li, c) :
                for i,v in enumerate (li) :
                    if v == c:
                        return i
                return -1
            li = [45, 32, 43, 56]
            print (recherche(li, 43))  # affiche 2

        En python, il existe un fonction simple qui permet de faire ça :

        ::

            print(li.index (43))  # affiche 2

        Lorsque l'élément n'y est pas, on retourne souvent la position ``-1``
        qui ne peut être prise par aucun élément :

        ::

            if c in li: return li.index(c)
            else: return -1

        Même si ce bout de code parcourt deux fois le tableau (une fois déterminer
        sa présence, une seconde fois pour sa position), ce code est souvent plus rapide
        que la première version et la probabilité d'y faire une erreur plus faible.
    """
    if c in li:
        return li.index(c)
    else:
        return -1


def minindex(li):
    """
    Retourne l'index du minimum et le minimum.

    @param  li      liste
    @return         tuple (minimum,position)


    .. exref::
        :tag: Base
        :title: minimum avec position

        La fonction `min <https://docs.python.org/3/library/functions.html#min>`_
        retourne le minium d'un tableau mais pas sa position.
        Le premier réflexe est alors de recoder le parcours de la liste
        tout en conservant la position du minimum.

        .. runpython::
            :showcode:

            li = [ 0, 434, 43, 6436, 5 ]
            m  = 0
            for i in range (0, len (li)):
                if li [m] < li [i]:
                    m = i
            print(m)

        Mais il existe une astuce pour obtenir la position sans avoir à le reprogrammer.

        .. runpython::
            :showcode:

            k = [(v,i) for i,v in enumerate (li)]
            m = min(k)
            print(m)

        La fonction ``min`` choisit l'élément minimum d'un tableau dont les éléments sont des
        couples (élément du premier tableau, sa position).
        Le minimum est choisi en comparant les éléments, et la position
        départegera les exaequo.
    """
    return min((v, i) for i, v in enumerate(li))


def recherche_dichotomique(li, c):
    """
    Effectue une recherche dichotomique.

    @param  li      tableau
    @param  c       élément à chercher
    @return         position

    .. exref::
        :tag: Base
        :title: recherche dichotomique

        La `recherche dichotomique <http://fr.wikipedia.org/wiki/Dichotomie>`_
        est plus rapide qu'une recherche classique mais elle
        suppose que celle-ci s'effectue dans un ensemble trié.
        L'idée est de couper en deux l'intervalle de recherche à chaque itération.
        Comme l'ensemble est trié, en comparant l'élément cherché à l'élément central,
        on peut éliminer une partie de l'ensemble : la moitié inférieure ou supérieure.

        .. runpython::
            :showcode:

            def recherche_dichotomique(li, c) :
                a,b = 0, len (li)-1
                while a <= b :
                    m = (a+b)/2
                    if   c == li [m] : return m
                    elif c <  li [m] : b = m-1   # partie supérieure éliminée
                    else             : a = m+1   # partie inférieure éliminée
                return -1  # élément non trouvé

            print(recherche_dichotomique([0, 2, 5, 7, 8], 7)
    """
    a, b = 0, len(li) - 1
    while a <= b:
        m = (a + b) // 2
        if c == li[m]:
            return m
        elif c < li[m]:
            b = m - 1   # partie supérieure éliminée
        else:
            a = m + 1   # partie inférieure éliminée
    return -1  # élément non trouvé


def text2mat(s, sep_row="\n", sep_col="\t"):
    """
    convertit une chaîne de caractères en une matrice ( = liste de listes),
    réciproque de la fonction @see fn mat2text

    @param      s           texte à convertir
    @param      sep_row     séparation de ligne
    @param      sep_col     séparateur de colonnes
    @return                 liste de liste

    .. exref::
        :tag: Base
        :title: conversion d'une chaîne de caractère en matrice

        Les quelques lignes qui suivent permettent de décomposer une chaîne de caractères
        en matrice. Chaque ligne et chaque colonne sont séparées par des
        séparateurs différents. Ce procédé intervient souvent lorsqu'on récupère des
        informations depuis un fichier texte lui-même provenant d'un tableur.

        .. runpython::
            :showcode:

            s       = "case11;case12;case13|case21;case22;case23"
            # décomposition en matrice
            ligne   = s.split ("|")                     # lignes
            mat     = [ l.split (";") for l in ligne ]  # colonnes

            print(mat)

        Comme cette opération est très fréquente lorsqu'on travaille avec les données,
        on ne l'implémente plus soi-même. On préfère utiliser un module comme
        `pandas <http://pandas.pydata.org/>`_ qui est plus robuste et considère plus de cas.
        Pour écrire, utilise la méthode `to_csv <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html>`_,
        pour lire, la fonction
        `read_csv <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.parsers.read_csv.html>`_.
        On peut également directement enregistrer au format Excel
        `read_excel <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.excel.read_excel.html>`_ et écrire dans ce même format
        `to_excel <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html>`_.
    """
    ligne = s.split(sep_row)                     # lignes
    mat = [l.split(sep_col) for l in ligne]  # colonnes
    return mat


def mat2text(mat, sep_row="\n", sep_col="\t"):
    """
    convertit une matrice en une chaîne de caractères,
    réciproque de la fonction @see fn text2mat

    @param      mat         matrice à convertir (liste de listes)
    @param      sep_row     séparation de ligne
    @param      sep_col     séparateur de colonnes
    @return                 liste de liste

    .. exref::
        :tag: Base
        :title: conversion d'une matrice en chaîne de caractères

        .. runpython::
            :showcode:

            mat     = [['case11', 'case12', 'case13'], ['case21', 'case22', 'case23']]
            ligne   = [ ";".join (l) for l in mat ]     # colonnes
            s       = "|".join (ligne)                  # lignes

            print(s)
    """
    ligne = [";".join(l) for l in mat]     # colonnes
    s = "|".join(ligne)                  # lignes
    return s


def somme(li):
    """
    Calcule la somme des éléments d'un tableau.

    @param      li      tableau
    @return             somme

    .. exref::
        :tag: Base
        :title: calcul d'une somme

        Le calcul d'une somme fait toujours intervenir une boucle car le langage
        :epkg:`Python` ne peut faire des additions qu'avec deux nombres.
        Le schéma est toujours le même : initialisation et boucle.

        .. runpython::
            :showcode:

            li = [ 0, 434, 43, 6456 ]
            s  = 0                       # initialisation
            for l in li :                # boucle
                s += l                   # addition
            print(s)

        Ce code est équivalent à la fonction `sum <https://docs.python.org/3/library/functions.html#sum>`_.
        Dans ce cas où la somme intègre le résultat d'une fonction (au sens mathématique)
        et non les éléments d'une liste, il faudrait écrire :

        .. runpython::
            :showcode:

            def fonction(x):
                return x
            s  = 0
            for l in li:
                s += fonction (l)
            print(s)

        Et ces deux lignes pourraient être résumées en une seule grâce
        à l'une de ces instructions :

        .. runpython::
            :showcode:

            s1 = sum ( [fonction (l) for l in li] )
            s2 = sum ( fonction (l) for l in li )
            s3 = sum ( map (fonction, li) )
            print(s1, s2, s3)

        L'avantage des deux dernières instructions est qu'elles évitent
        la création d'une liste intermédiaire,
        c'est un point à prendre en compte si la liste sur laquelle opère la
        somme est volumineuse.
    """
    return sum(li)


def triindex(li):
    """
    trie une liste, retourne la liste triée et les positions initiales

    @param      li      tableau
    @return             liste triée

    .. exref::
        :tag: Base
        :title: tri, garder les positions initiales

        Le tri est une opération fréquente. On n'a pas toujours le temps de programmer
        le tri le plus efficace comme un tri `quicksort <http://fr.wikipedia.org/wiki/Tri_rapide>`_
        et un tri plus simple suffit la plupart du temps.
        Le tri suivant consiste à recherche le plus petit élément puis à
        échanger sa place avec le premier élément du tableau du tableau.
        On recommence la même procédure à partir de la seconde position,
        puis la troisième et ainsi de suite jusqu'à la fin du tableau.

        .. runpython::
            :showcode:

            li = [5, 6, 4, 3, 8, 2]

            for i in range (0, len (li)) :
                # recherche du minimum entre i et len (li) exclu
                pos = i
                for j in range (i+1, len (li)) :
                    if li [j] < li [pos] : pos = j
                # échange
                ech      = li [pos]
                li [pos] = li [i]
                li [i]   = ech

            print(li)

        La fonction `sorted <https://docs.python.org/3/library/functions.html#sorted>`_
        trie également une liste mais selon un algorithme plus efficace
        que celui-ci (voir `Timsort <http://en.wikipedia.org/wiki/Timsort>`_).
        On est parfois amené à reprogrammer un tri parce qu'on veut conserver la position des éléments
        dans le tableau non trié.
        Cela arrive quand on souhaite trier un tableau et appliquer la même transformation à un second
        tableau.
        Il est toujours préférable de ne pas reprogrammer un tri (moins d'erreur).
        Il suffit d'applicer la même idée que pour la fonction @see fn minindex.

        .. runpython::
            :showcode:

            tab = ["zero", "un", "deux"]                       # tableau à trier
            pos = sorted(  (t,i) for i,t in enumerate(tab)  )  # tableau de couples
            print (pos)                # affiche [('deux', 2), ('un', 1), ('zero', 0)]

        Si cette écriture est trop succincte, on peut la décomposer en :

        .. runpython::
            :showcode:

            tab = ["zero", "un", "deux"]
            tab_position = [ (t,i) for i,t in enumerate(tab) ]
            tab_position.sort()
            print(tab_position)
    """
    return sorted((t, i) for i, t in enumerate(li))


def compte(li):
    """
    compte le nombre d'occurrences de chaque élément d'une liste

    @param  li      tableau
    @return         dictionnaire

    .. exref::
        :tag: Base
        :title: comptage

        On souhaite ici compter le nombre d'occurrences de chaque élément d'un tableau.
        Par exemple, on pourrait connaître par ce moyen la popularité d'un mot dans un discours
        politique ou l'étendue du vocabulaire utilisé.
        L'exemple suivant compte les mots d'une liste de mots.

        .. runpython::
            :showcode:

            li = ["un", "deux", "un", "trois"]
            d  = { }
            for l in li:
                if l not in d:
                    d [l] = 1
                else:
                    d [l] += 1
            print(d)   # affiche {'un': 2, 'trois': 1, 'deux': 1}

        La structure la plus appropriée ici est un dictionnaire puisqu'on cherche
        à associer une valeur à un élément d'une liste qui peut être de tout type.
        Si la liste contient des éléments de type modifiable comme une liste,
        il faudrait convertir ceux-ci en un type immuable comme une chaîne de caractères.
        L'exemple suivant illustre ce cas en comptant les occurrences des lignes d'une matrice.

        .. runpython::
            :showcode:

            mat = [ [1,1,1], [2,2,2], [1,1,1]]
            d  = { }
            for l in mat:
                k = str (l)    # k = tuple (l) lorsque cela est possible
                if k not in d:
                    d [k] = 1
                else:
                    d [k] += 1
            print(d)   # affiche {'[1, 1, 1]': 2, '[2, 2, 2]': 1}

        Les listes ne peuvent pas être les clés du dictionnaire :
        `Why Lists Can't Be Dictionary Keys <https://wiki.python.org/moin/DictionaryKeys>`_.

        On peut également vouloir non pas compter le nombre d'occurrence mais mémoriser les
        positions des éléments tous identiques. On doit utiliser un dictionnaire de listes :

        .. runpython::
            :showcode:

            li = ["un", "deux", "un", "trois"]
            d  = { }
            for i,v in enumerate(li):
                if v not in d:
                    d [v] = [ i ]
                else:
                    d [v].append (i)
            print(d)   # affiche {'un': [0, 2], 'trois': [3], 'deux': [1]}

        S'il suffit juste compter, l'écriture la plus simple est :

        .. runpython::
            :showcode:

            li = ["un", "deux", "un", "trois"]
            for x in li:
                r[x] = r.get(x,0)+1
            print(r)
    """
    r = {}
    for x in li:
        r[x] = r.get(x, 0) + 1
    return r


def mat2vect(mat):
    """
    convertit une matrice en un tableau à une seule dimension,
    réciproque de la fonction @see fn vect2mat

    @param  mat     matrice
    @return         liste

    .. exref::
        :tag: Base
        :title: conversion d'une matrice en un vecteur

        Dans un langage comme le *C++*, il arrive fréquemment qu'une matrice ne soit pas
        représentée par une liste de listes mais par une seule liste car cette représentation
        est plus efficace. Il faut donc convertir un indice en deux indices ligne et colonne.
        Il faut bien sûr que le nombre de colonnes sur chaque ligne soit constant.
        Le premier programme convertit une liste de listes en une seule liste.

        .. runpython::
            :showcode:

            mat = [[0,1,2],[3,4,5]]
            lin = [ i * len (mat [i]) + j \\
                        for i in range (0, len (mat)) \\
                        for j in range (0, len (mat [i])) ]
            print(lin)

        Vous pouvez aussi utiliser des fonctions telles `reduce <https://docs.python.org/3/library/functools.html?highlight=reduce#module-functools>`_.

        .. runpython::
            :showcode:

            mat = [[0,1,2],[3,4,5]]
            lin = reduce ( lambda x,y: x+y, mat )
            print(lin)
    """
    return reduce(lambda x, y: x + y, mat)


def vect2mat(vect, ncol):
    """
    Convertit un tableau à une dimension en une matrice,
    réciproque de la fonction @see fn mat2vect.

    @param  vect    vecteur
    @param  ncol    nombre de colonnes
    @return         matrice

    .. exref::
        :tag: Base
        :title: conversion d'un vecteur en une matrice

        Dans un langage comme le *C++*, il arrive fréquemment qu'une matrice ne soit pas
        représentée par une liste de listes mais par une seule liste car cette représentation
        est plus efficace. Il faut donc convertir un indice en deux indices ligne et colonne.
        Il faut bien sûr que le nombre de colonnes sur chaque ligne soit constant.
        Le premier programme convertit une liste de listes en une seule liste.

        .. runpython::
            :showcode:

            vect = [0, 1, 2, 3, 4, 5]
            mat = [ vect[i*ncol: (i+1)*ncol] for i in range(0,len(vect)//ncol) ]
            print(mat)

    """
    return [vect[i * ncol: (i + 1) * ncol]
            for i in range(0, len(vect) // ncol)]


def integrale(fonction, a, b, n):
    """
    calcule l'intégrale d'une fonction avec la méthode de Rienmann

    @param  fonction        fonction
    @param  a               borne inférieure de l'intervalle
    @param  b               borne supérieure de l'intervalle
    @param  n               nombre de division de l'intervalle
    @return                 valeur

    .. exref::
        :tag: Base
        :title: fonction comme paramètre

        Une fonction peut aussi recevoir en paramètre une autre fonction.
        L'exemple suivant inclut la fonction ``calcul_n_valeur``
        qui prend comme paramètres ``l`` et ``f``.
        Cette fonction calcule pour toutes les valeurs ``x`` de la liste
        ``l`` la valeur ``f(x)``.
        ``fonction_carre`` ou ``fonction_cube`` sont passées en paramètres à la fonction
        ``calcul_n_valeur`` qui les exécute.

        .. runpython::
            :showcode:

            def fonction_carre(x):
                return x*x

            def fonction_cube(x):
                return x*x*x

            def calcul_n_valeur(l,f):
                res = [f(i) for i in l]
                return res

            l = [0,1,2,3]
            print(l)   # affiche [0, 1, 2, 3]

            l1 = calcul_n_valeur(l, fonction_carre)
            print(l1)  # affiche [0, 1, 4, 9]

            l2 = calcul_n_valeur(l, fonction_cube)
            print(l2)  # affiche [0, 1, 8, 27]
    """
    h = (b - a) / n
    return sum(fonction(a + h / 2 + h * i) for i in range(0, n)) * h


def construit_matrice_carree(n):
    """
    cette construit une matrice carrée remplie de zéro
    sous la forme d'une liste de listes

    @param      n       dimension de la matrice carrée
    """
    return [[0 for i in range(n)] for j in range(n)]


def enumerate_permutations_recursive(ensemble):
    """
    énumère les permutations d'un ensemble de façon récursive

    @param      ensemble        ensemble à permuter
    @return                     itérateur sur les permutations
    """

    if len(ensemble) == 1:
        yield ensemble
    else:
        for i in range(0, len(ensemble)):
            ensemble[0], ensemble[i] = ensemble[i], ensemble[0]
            per = enumerate_permutations_recursive(ensemble[1:])
            for p in per:
                yield [ensemble[0]] + p
            ensemble[0], ensemble[i] = ensemble[i], ensemble[0]


def enumerate_permutations(ensemble):
    """
    énumère les permutations d'un ensemble de façon non récursive

    @param      ensemble        ensemble à permuter
    @return                     itérateur sur les permutations
    """
    if len(ensemble) == 1:
        yield ensemble
    else:
        position = list(range(len(ensemble)))
        while position[0] < len(ensemble):

            memo = []
            for i, p in enumerate(position):
                ensemble[i], ensemble[p] = ensemble[p], ensemble[i]
                memo.append((i, p))
            yield ensemble.copy()
            for i, p in reversed(memo):
                ensemble[i], ensemble[p] = ensemble[p], ensemble[i]

            last = len(position) - 1
            position[last] += 1
            while last > 0 and position[last] >= len(position):
                position[last - 1] += 1
                position[last] = last
                last -= 1
