
.. _l-feuille-de-route-2023-3A:

Feuille de route 2022-2023 (3A)
===============================

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td3a>`

Plan
++++

Les cours et séances se déroulent sur 6 séances de 3h au second semeste.

Intervenants
++++++++++++

Xavier Dupré, Matthieu Durut.

Notes
+++++

Liens, notebooks prévus pour les séances pratiques.

.. contents::
    :local:

Séance 1
^^^^^^^^

1.

* hardware
* ordinateur
* mémoire partagée
* ordre de grandeur vitesse CPU, communication

2.

* algorithmes répartis
* multithread
* `race condition <https://en.wikipedia.org/wiki/Race_condition>`_
* verrou

Séance 2
^^^^^^^^

Séance pratique sur CPU.

**Plan : parallélisation avec CPU**

1.

* Setup SSP Cloud, présentation d'un package, C++
* Outils de développement : cmake, git, pull request
* Python : setup.py, sphinx, pybind11, cython
* style : `black <https://github.com/psf/black>`_,
  `ruff <https://github.com/charliermarsh/ruff>`_

2.

* Somme des éléments d'une matrice
* en ligne, en colonne, notion de cache, `std::vector`, numpy array, benchmark
* éléments de C++, pybind11, cython
* AVX
* parallélisation avec des threads, processus

3.

* Exercice : somme de deux vecteurs
* parallélisation d'une multiplication de matrices
* applications aux random forest

4.

* `blas <https://netlib.org/lapack/lug/node145.html>`_,
  `lapack <https://netlib.org/lapack/>`_,
  `Eigen <https://eigen.tuxfamily.org/index.php?title=Main_Page>`_,
  `blis <https://github.com/flame/blis>`_
* `Triton <https://github.com/JonathanSalwan/Triton>`_, `TVM <https://github.com/apache/tvm>`_,
  `AITemplate <https://github.com/facebookincubator/AITemplate>`_,
  `treelite <https://treelite.readthedocs.io/en/latest/>`_

**Instructions pour démarrer**

* Aller sur la plate-forme `SSPCloud de l'ENSAE <https://datalab.sspcloud.fr/home>`_.
* Se connecter avec son adresse ENSAE
* Ouvrir une instance `vscode-python`

Il ensuite exécuter les instuctions suivantes en ligne de commande.

:: 

    git clone https://github.com/sdpython/onnx-extended.git
    cd onnx-extended
    python setup.py build_ext --inplace

Si ça ne marche, installer cmake: ``conda install cmake``.
Puis :

::

    export PYTHONPATH=<this folder>
    python _doc/examples/plot_bench_cpu_vector_sum.py

Séance 3
^^^^^^^^

Séance pratique sur Spark.

1.

* Présentation de spark, objectif
* HDFS, premiers pas avec Spark, `java <https://en.wikipedia.org/wiki/Java_(programming_language)>`_
* Notion de spark dataframes
* `parquet <https://parquet.apache.org/>`_

2.

* Lien avec SQL, group by, join
* Importance de collect
* `Spark SQL <https://spark.apache.org/sql/>`_
* Lecture, écriture

3.

* Distribution : :ref:`hashdistributionrst`
* Notion de skewed datasets
* group by + count, group by + mediane
* Exercice

On veut calculer pour chaque français le nombre de points de vente alimentaires (~44.000)
situé à moins de trois kilomètres du domicile. Comment faire ? On dispose que deux jeux
de données :

* la géolocalisation des points de vente alimentaires et leur taille
* la géolocalisation des français (toutes les adresses connues dans les pages blanches)

4.

* `mllib <https://spark.apache.org/mllib/>`_
* notion d'algorithmes de streaming, BJKST,
  `Reservoir Sampling
  <http://www.xavierdupre.fr/app/sparkouille/helpsphinx/notebooks/reservoir_sampling.html>`_

Séance 4
^^^^^^^^

Séance 5
^^^^^^^^

Séance pratique sur CUDA.

Séance 6
^^^^^^^^
