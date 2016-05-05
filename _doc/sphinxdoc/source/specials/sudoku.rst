



.. _l-sudoku-sol:


Résolution d'un sudoku
======================

Le `sudoku <https://fr.wikipedia.org/wiki/Sudoku>`_ est assez simple à résoudre si
on se contente de ne trouver que la première solution qui fonctionne :
la fonction :func:`resolution_sudoku <ensae_teaching_cs.special.sudoku.resolution_sudoku>`.

.. todoext::
    :title: construire un sudoku
    :tag: special
    
    Une grille de sudoku est plus ou moins difficile. Il faut d'abord s'assurer 
    que la grille n'aboutit qu'à une seule solution. La difficulté provient du nombre 
    de choix qu'on doit lors de la résolution.
