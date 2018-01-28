
.. blogpost::
    :title: Calcul distribué en Python (CPU)
    :keywords: calcul distribué, parallel computing
    :date: 2018-01-28
    :categories: parallel computing
    :lid: blog-parallel-computing-2018

    Le langage :epkg:`Python` est très lent.
    C'est pourquoi la plupart les calculs scientifiques
    sont implémentés en :epkg:`C++` ou tout autre
    alternative à mi-chemin comme :epkg:`Cython`
    qui est presque un langage à part entière.
    La connaissance du :epkg:`C++` n'est pas indispensable
    mais elle facilite énormément la période d'apprentissage.

    Il est toujours possible de parallèle les calculs en utilisant
    des threads mais le langage :epkg:`Python`, pour éviter
    les erreurs d'exécution et garder le langage simple,
    protège tous les objects qu'il manipule contre les accès
    concurrentiels via une unique porte qu'on appelle
    le :epkg:`GIL`. Il faut concevoir ce :epkg:`GIL` comme
    une fil d'attente par laquelle le programme passe lors de
    son exécution pour lire ou modifier tout objet, toute classe,
    liste ou dictionnaire. Comme on y accède fréquemment,
    les programmes multithreads sont fortement ralentis au point
    de ne pas aller plus vite qu'un programme à un seul thread.
    Le :epkg:`GIL` peut être désactivé mais il faut recourir à
    des outils comme :epkg:`Cython` ou au :epkg:`C++`.
    Sans :epkg:`C++`, des technologies comme
    :epkg:`OpenMP` sont difficilement accessibles.

    Une autre façon de paralléliser consiste à utiliser plusieurs
    processus, autrement dit, plusieurs interpréteurs :epkg:`Python`
    tournent en même temps. L'inconvénient de cette méthode est
    que la mémoire n'est pas partagée : les processus peuvent travailler
    sur les mêmes données mais il faut qu'elles soient recopiées dans
    la mémoire de chacun. De même, les processus doivent communiquer
    entre eux pour partager le résultat de leurs calculs. Ce n'est pas
    compliqué en soi mais cela complique un peu l'écriture des programmes
    et cela les ralentit. Il faut communiquer le minimum d'information.

    Des librairies ont été implémentées pour simplifier l'écriture
    de telles programmes comme `joblib <https://github.com/joblib/joblib>`_
    qui est la solution adoptée par :epkg:`scikit-learn`. La première librairie
    sur le sujet fut :epkg:`MPI` portée sous :epkg:`Python`
    avec `mpi4p <https://github.com/mpi4py/mpi4py>`_.
    D'autres options existent comme
    `dispy <https://github.com/pgiri/dispy>`_. Il vaut mieux
    vérifier la fréquence des mises à jour et le nombre de contributeurs
    avant d'utiliser une librairie.

    `pymp <https://github.com/classner/pymp>`_ est une librairie à part
    car elle permet d'utiliser :epkg:`OpenMP` en utilisant une
    particularité du système d'exploitation :epkg:`linux`.

    Une dernière option consiste à utiliser des modules
    qui convertissent des programmes :epkg:`Python` en :epkg:`C++`
    comme :epkg:`numba`. A l'exécution, :epkg:`numba` détecte
    les types des variables manipulées et en déduit un code :epkg:`C++`
    équivalent, le compile et remplace la fonction :epkg:`Python`
    par une version plus rapide. Ce faisant, il est possible
    de désactiver le :epkg:`GIL` :
    `nogil <http://numba.pydata.org/numba-doc/dev/user/jit.html#nogil>`_.
    La connaissance du :epkg:`C++` aide à comprendre comment écrire
    des bouts de code qui peuvent se passer du :epkg:`GIL`. Néanmoins,
    la fonction ne crée aucun containeur, aucun tableau mais reçoit
    en paramètre tous ceux qu'elles doit modifier - ils sont
    donc créés au préalable -, le programme devrait tourner sans erreur
    d'exécution.
