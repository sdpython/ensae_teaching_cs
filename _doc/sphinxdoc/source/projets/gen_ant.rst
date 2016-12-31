
.. _l-gen_ant:

Algorithmes génétiques, Fourmis
===============================

Les algorithmes génétiques ne sont pas ou peu enseignés à l'ENSAE. Chaque sujet
est l'occasion de découvrir des algorithmes. Chaque sujet considère un problème
simple et un algorithme d'optimisation génétique décrit par un document.

.. _l-gen-optim:

Optimisation à partir d'algorithmes génétiques
----------------------------------------------

La plupart des algorithmes d'optimisation reposent sur le gradient. La plus classique est de se promener le long
de la courbe à optimisation dans le long de la pente la plus forte : dans le sens du gradient s'il faut maximier,
dans le sens opposé s'il faut minimiser. Lorsque celui-ci n'est pas nul, la direction de cette pente est indiquée par le gradient.
Mais cela suppose évidemment que la fonction à optimiser soit dérivable.
Il arrive que la fonction ne soit pas dérivable où tout simplement que le problème d'optimisation soit
`combinatoire <http://fr.wikipedia.org/wiki/Optimisation_combinatoire>`_.

L'objectif de ce projet est de comparer un algorithme d'optimisation linéaire sous contrainte et un algorithme génétique
appliqué à des problèmes au même problème. On s'intéressera à la convergence des deux algorithmes lorsque la dimension
de l'espace des observations croît.

* `Algorithmes Génétiques <http://perso.limsi.fr/jps/enseignement/tutoriels/pcd/3.genetique/>`_
* `Ant Colony Optimization applications in Portfolio Construction and Algorithmic Trading <http://www.stuartreid.co.za/ant-colony-optimization-finance/>`_

.. _l-gen-bag:

Problème du sac-à-dos et algorithmes génétiques
-----------------------------------------------

.. index:: sac-à-dis, Knapsack

Le `problème du sac-à-dos <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos>`_ est un
problème d'optimisation discrète linéaire avec contrainte.
Il peut être vu comme un problème d'`optimisation combinatoire <http://fr.wikipedia.org/wiki/Optimisation_combinatoire>`_.
Comment remplir un sac-à-dos avec des objets de volumes différents en perdant le moins d'espace possible ?
L'objectif de ce projet est d'implémentation un algorithme de résolution de tels problèmes
à partir d'algorithme génétiques.

* `Optimisation par colonies de fourmis pour le problème du sac à dos multidimensionnel <http://liris.cnrs.fr/Documents/Liris-2310.pdf>`_
  (`autre accès <http://www.xavierdupre.fr/enseignement/projet_data/fourmi_sac_a_dos_Liris-2310.pdf>`_)

On étudiera la convergence et le coût des algorithmes en fonction de la dimension du problème.

.. _l-gen-tsp:

Problème du voyageur de commerce et algorithme génétique
--------------------------------------------------------

.. index:: TSP

Le `problème du voyageur de commerce <http://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce>`_ est un
problème d'optimisation discrète très connu. Il consiste à parcourir tous les sommets d'un graphe en minimisant
la distance pour les parcourir. Ici encore, il s'agit de résoudre ce problème à l'aide d'algorithme génétique.

* `Méthodes pour l'optimisation discrète <http://www.dil.univ-mrs.fr/~vancan/m111/documents/cours1r.pdf>`_
    (`autre accès <http://www.xavierdupre.fr/enseignement/projet_data/cours1rag.pdf>`_)

On étudiera la convergence et le coût des algorithmes en fonction de la dimension du problème.

.. _l-gen-ant:

Colonie de fourmis et plus court chemin
---------------------------------------

.. index:: fourmi

On dispose un trésor dans une pièce contenant de nombreux obstacles, à l'autre bout, une colonie
de fourmis. Au gré de leurs explorations, ces fourmis vont trouver puis raccourcir le plus court
chemin de leurs fourmilières au trésor.

* `Agents Réactifs <http://perso.limsi.fr/jps/enseignement/tutoriels/sma/doc/A.reactif.pdf>`_
  (`autre accès <http://www.xavierdupre.fr/enseignement/projet_data/A.reactif.pdf>`_)

L'aspect visuel est souvent utile lorsqu'on veut vérifier que l'algorithme fonctionne et converge
convenablement. Toutefois, il est rarement possible d'implémenter cette interface et d'étudier en détail les
algorithmes. Le ou les élèves devront faire un choix entre ces deux directions.

* Direction 1 : les fourmis, une colonie, un trésor, des phéromones et une interface visuelle.
* Direction 2 : un problème plus classique d'optimisation du plus court chemin dans un graphe,
                on comparera avec un algortihme de Djisktra, puis on s'intéressera aux propriétés de
                l'algorithme lorsque le nombre de sommets augmentent (le réseau routier belge, français, américain, européen...)

.. _l-gen-motif:

Recherche de motifs
-------------------

Pas encore bien défini mais inspiré de :

* `Stochastic Local Search for Pattern Set Mining <http://arxiv.org/pdf/1412.5984v1.pdf>`_

Lectures complémentaires
------------------------

* 2009 - `Optimisation multi-objectif par colonies de fourmis, Cas des problèmes de sac à dos <http://tel.archives-ouvertes.fr/docs/00/60/37/80/PDF/TH2009_Alaya_-_Ines.pdf>`_ (thèse) (`autre accès <http://www.xavierdupre.fr/enseignement/projet_data/TH2009_Alaya_-_Ines.pdf>`_)
* 2000 - `Algorithmes de fourmis artificielles : applications à la classification et à l'optimisation <http://www.hant.li.univ-tours.fr/webhant/pub/Mon00a.phd.pdf>`_  (thèse) (`autre accès <http://www.xavierdupre.fr/enseignement/projet_data/fourmi_Mon00a.phd.pdf>`_)
* 2014 - `Modeling Creativity: Case Studies in Python <http://arxiv.org/abs/1410.0281>`_
