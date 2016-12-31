
.. blogpost::
    :title: Permutations et récursivité
    :keywords: permutation, combinatoire
    :date: 2016-09-16
    :categories: TD

    Enumérer les permutations est un exercice classique.
    Voici une implémentation un peu différente mais toujours récursive :

    ::

        def permutation(L):
            n=len(L)
            if n==1:
                return [L]
            else :
                P=[]
                for i in range(n):
                    A=L[0:i]+L[i+1:n]
                    P1=permutation(A)
                    for k in range(len(P1)):
                        P.append([L[i]]+P1[k])
                return P

    La version que j'ai implémentée utilise les itérateurs
    :func:`enumerate_permutations_recursive <ensae_teaching_cs.td_1a.construction_classique.enumerate_permutations_recursive>`.
    Il existe toujours une version non récursive d'une fonction qui l'est :
    :func:`enumerate_permutations <ensae_teaching_cs.td_1a.construction_classique.enumerate_permutations>`.
    Celle-ci reproduit le fonctionnement de la première.
    C'est un exemple où le passage de l'un à l'autre n'est pas simple.
