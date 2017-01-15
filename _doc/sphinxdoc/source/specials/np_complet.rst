
.. index:: NP-complet

.. _l-np-complets:

Problèmes NP-complets
=====================

.. contents::
    :local:

Quelques définitions
++++++++++++++++++++

On distingue trois classes de problèmes
*P*, *NP*, *NP-complet*.

**coût**

**P**

Un problème appartient à la
`classe P <https://fr.wikipedia.org/wiki/P_(complexit%C3%A9)>`_
s'il peut être décidé en temps polynomial.

**NP**

Un problème de décision est dans
`NP <https://fr.wikipedia.org/wiki/NP_(complexit%C3%A9)>`_
s'il est décidé par une
`machine de Turing non déterministe <https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe>`_
en temps polynomial par rapport à la taille de l'entrée.
Cela implique que pour un problème *A*, il est possible
de vérifier qu'un *mot m* est solution de *A* en temps polynomial.

**NP-complet**

Un problème `NP-complet <https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-complet>`_
est un problème qui n'admet pas d'algorithmes capables de trouver une solution
en un temps polynomial. Plus précisément, pour deux problèmes *A* et *B* de cette classe,
il existe une transformation (ou *réduction*) *f* qui transforme
le problème *A* en *B*.

**BPP**

La classe `BPP <https://fr.wikipedia.org/wiki/BPP_(complexit%C3%A9)>`_
est un objet de la théorie de la complexité, en informatique théorique.
C'est une classe de problèmes de décision qui peut être définie avec des
`machines de Turing probabilistes <https://fr.wikipedia.org/wiki/Machine_de_Turing_probabiliste>`_.
L'acronyme BPP vient de Bounded-error Probabilistic Polynomial time.

**P=NP ?**

C'est un problème encore irrésolu :
`Problème P = NP <https://fr.wikipedia.org/wiki/Probl%C3%A8me_P_%3D_NP>`_.

Idée pour démonstration qu'un problème est NP-complet
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Une preuve complète est donnée dans le cours
`Logique, modèles, calculs (INF 423) <http://www.enseignement.polytechnique.fr/informatique/INF423/i.php?n=Main.Poly>`_.

**1**

L'idée est toujours la même : il faut partir d'un problème NP-complet connu
et le réduire de façon polynomial au problème *P* dont on cherche à démontrer qu'il
est NP-complet. La *réduction* est une transformation d'un problème
*A* en *P* de telle sorte qu'une solution problème *A*
puisse être transformé en une solution du problème *P* et réciproquement.

**2**

Il faut un premier problème NP-complet pour lequel il faut démontrer la NP-complétude.
C'est le théorème de `Stephen Cook <https://fr.wikipedia.org/wiki/Stephen_Cook>`_ :
le problème `SAT <https://fr.wikipedia.org/wiki/Probl%C3%A8me_SAT>`_ est NP-complet.
On peut montrer que les problème SAT et
`3-SAT <https://fr.wikipedia.org/wiki/Probl%C3%A8me_SAT#3-SAT>`_ sont équivalents.

**3**

Beaucoup de problèmes se présentent sous la forme d'une optimisation.
Or *SAT* est un problème de décision : existe-t-il un point de
:math:`\acc{0,1}^N` qui vérifie une clause logique :
:math:`\vee_k  ( y_{1k} \wedge ... \wedge y_{n_k k} )`
avec :math:`y_{ik}` est soit :math:`x_i` soit :math:`\neg x_i` ?
Pour passer de l'un à l'autre, on transforme le problème d'optimisation
en un problème de décision : existe-t-il une solution dont l'évaluation
est inférieure ou supérieur à un certain seuil ?

Liste de problèmes NP-complets
++++++++++++++++++++++++++++++

* `21 problèmes NP-complet de Karp <https://fr.wikipedia.org/wiki/21_probl%C3%A8mes_NP-complets_de_Karp>`_
* `Liste de problèmes NP complets <https://fr.wikipedia.org/wiki/Liste_de_probl%C3%A8mes_NP-complets>`_
  (`en <https://en.wikipedia.org/wiki/List_of_NP-complete_problems>`_)
