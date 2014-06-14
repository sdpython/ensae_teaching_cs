
.. _l-exoalgo:


Exercices autour d'algorithmes
==============================

Ces exercices sont proches de ceux qu'on peut poser en entretien d'embauche. Le plus souvent,
il existe une façon naïve d'arriver au résultat et il existe un algorithme plus rapide. 
Tout est question de coût d'algorithme. Il y a deux grandes astuces pour aller plus vite :
    * la programmation dynamique, son coût est en :math:`O(n^2)`,
    * la dichotomie, son coût est en :math:`O(\ln_2 n)`.
    
Le tout est d'exprimer la solution en faisant apparaître l'un ou l'autre ou une combinaison des deux pour les problèmes 
les plus complexes.
La programmation dynamique apparaît souvent quand on considère la solution sous forme récurrente.
La dichotomie consiste à résoudre à couper l'ensemble de départ en deux, à résoudre le problème pour les deux sous-ensembles, 
puis à fusionner les deux solutions.

    
    
.. toctree::
    :numbered:

    notebooks/exercice_xn
    notebooks/exercice_echelle
    
    
    
    