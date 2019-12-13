
.. _l-feuille-de-route-2019-3A:

Feuille de route 2019 (3A)
==========================

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td3a>`

Plan
++++

Les cours et séances se déroulent sur 5 séances de 3h
mardi après-midi.

Intervenants
++++++++++++

`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_,
Matthieu Durut.

Notes
+++++

Liens, notebooks prévus pour les séances pratiques.

.. contents::
    :local:

Séance 1
^^^^^^^^

* processeur, GPU, CPU
* `heapsort <http://en.wikipedia.org/wiki/Heapsort>`_

Séance 2
^^^^^^^^

Python est devenu le langage de référence pour le machine learning
bien qu'il soit très lent. Il doit bien exister quelques tours
de magie derrière cet incroyable destin. Cette séance en explique
certains en s'intéressant à trois aspects : l'utilisation
de C++ via :epkg:`cython`, la notion de :epkg:`branching`
et la parallélisation avec :epkg:`openmp`. La séance s'appuie
sur le projet :epkg:`td3a_cpp` qui peut servir de modèle pour utiliser
python et cython pour paralléliser les calculs. Le module
fonctionne sur Windows, Linux, Mac OSX et est disponible
sur :epkg:`pypi` (voir aussi :ref:`l-cython-python`).

:epkg:`cython` n'est pas la seule option pour accélérer un programme,
:epkg:`pythran`. L'article `Pythran: Python at C++ speed !
<https://medium.com/@olivier.borderies/pythran-python-at-c-speed-518f26af60e8>`_
utilise :epkg:`pythran` pour accélérer l'algorithme du :ref:`TSP <exposeTSPrst>`.
Il essaye de convertir un code python en C++. Le projet `TSP Simulated Annealing
<https://gitlab.com/oscar6echo/tsp-pythran/tree/master/>`_ est une bonne base
pour construire un projet utilisant :epkg:`pythran` et :epkg:`openmp`.

Le GPU sous Python est plus facile d'accès avec une librairie
de deep learning déjà compilée. :epkg:`pytorch` est populaire parmi
les chercheurs, :epkg:`tensorflow` est le pionnier et de ce fait le 
plus utilisé, notamment avec :epkg:`keras`. Une librairie jeune mais
qui s'attaque au machine learning standard sous GPU est :epkg:`rapids`
(lire `RAPIDS cuGraph — The vision and journey to version 1.0 and beyond
<https://towardsdatascience.com/rapids-cugraph-the-vision-and-journey-to-version-1-0-and-beyond-88eff2ce3e76>`_)
et implémente une version GPU des dataframes avec :epkg:`cudf` et des algorithmes
de machine learning les plus populaires avec :epkg:`cuml`.

Séance 3
^^^^^^^^

Séance 4
^^^^^^^^

Séance 5
^^^^^^^^
