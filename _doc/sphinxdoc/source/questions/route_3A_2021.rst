
.. _l-feuille-de-route-2021-3A:

Feuille de route 2021-2022 (3A)
===============================

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td3a>`

Plan
++++

Les cours et séances se déroulent sur 6 séances de 3h
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

* `Introduction to Algorithms
  <https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf>`_
* `Latency Numbers Every Programmer Should Know
  <https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html>`_
* `What Every Computer Scientist Should Know About Floating-Point Arithmetic
  <https://faculty.tarleton.edu/agapie/documents/cs_343_arch/papers/1991_Goldberg_FloatingPoint.pdf>`_
* `What Every Programmer Should Know About Memory
  <https://www.akkadia.org/drepper/cpumemory.pdf>`_
* `Introduction to High Performance Scientific Computing
  <https://www.amazon.fr/Introduction-High-Performance-Scientific-Computing/dp/1257992546/ref=sr_1_1?ie=UTF8&qid=1476379218&sr=8-1&keywords=introduction+to+high+performance+scientific+computing+Victor+eijkhout>`_

Séance 2
^^^^^^^^

Les modèles de deep learning dépassent maintenant le milliards de coefficients.
Le premier modèle `BERT <https://arxiv.org/abs/1810.04805>`_ en avait
340 millions. Comment estime-t-on les coefficients de ces mastodontes ?
1 milliards de coefficients, c'est plus de dix ans de calculs sur une seule
carte GPU.

* Tour d'horizon
    * IA, machine learning, deep learning
    * Apprentissage de modèle, déploiement de modèles
    * Langage interprété, bas niveaux
    * CPU, GPU, ...
    * Course logicielle matérielle (`A100 <https://www.nvidia.com/en-us/data-center/a100/>`_)
* Machine learning open source ?
* Le graal : concevoir un modèle avec un outil simple et faisant des calculs rapides.
    * Ecrire des calculs rapides exige une connaissance des processeurs
    * Ecrire un modèle performant exige des connaissances mathématiques
    * Mécanicien et pilote sont des métiers devenus différents
* La simplicité, documentation
    * `API scikit-learn <https://scikit-learn.org/stable/modules/classes.html>`_
    * `pytorch tutorial <https://pytorch.org/tutorials/beginner/basics/intro.html>`_
* Illustrations
    * Calcul : produit matriciel de 3 matrices ?
      `Associativity and matrix multiplication
      <http://www.xavierdupre.fr/app/td3a_cpp/helpsphinx/auto_examples/plot_benchmark_associative.html>`_,
      (`opt-einsum <https://optimized-einsum.readthedocs.io/en/stable/>`_)
    * Fonction einsum : `Einsum decomposition
      <http://www.xavierdupre.fr/app/mlprodict/helpsphinx/notebooks/einsum_decomposition.html>`_,
      `bsnh,ctnh->nts <http://www.xavierdupre.fr/app/mlprodict/helpsphinx/notebooks/einsum_decomposition.html#decomposition-of-bsnh-ctnh-nts>`_
      `bsnh,btnh->bnts <http://www.xavierdupre.fr/app/mlprodict/helpsphinx/notebooks/onnx_profile_ort.html#einsum-bsnh-btnh-bnts>`_
* Python et C++
    * Un atout pour une thèse
    * Un exemple : `td3a_cpp <http://www.xavierdupre.fr/app/td3a_cpp/helpsphinx/index.html>`_
* Optimiser les calculs sur CPU
    * Parallélisation
        * `Threads <https://realpython.com/intro-to-python-threading/>`_
        * `Processus <https://docs.python.org/fr/3.9/library/subprocess.html>`_
        * Cloud
        * `sérialisation <https://python-guide-pt-br.readthedocs.io/fr/latest/scenarios/serialization.html>`_
    * `AVX <https://fr.wikipedia.org/wiki/Advanced_Vector_Extensions>`_
    * `Cache <https://en.wikipedia.org/wiki/CPU_cache>`_
    * Synchronisation et `GIL <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/notebooks/gil_example.html>`_
      (voir aussi `GIL <https://www.codeflow.site/fr/article/python-gil>`_)
    * Garbage Collector
    * :epkg:`Cython`, :epkg:`pybind11`
* Etude de cas
    * dot, matmul, syntaxe
    * `prange <https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html>`_
    * `AVX <https://fr.wikipedia.org/wiki/Advanced_Vector_Extensions>`_
    * branching
    * processeur, cache et blocs de mémoire contigüs
      (`mlas <https://github.com/microsoft/onnxruntime/tree/master/onnxruntime/core/mlas/lib>`_)
* Outils du développeur
    * Outils du dévelopeur : compilateur, éditeur (Visual Studio Code)
    * git, notion d'intégration continue
        * `Fixes #13173, implements faster polynomial features for dense matrices #13290
          <https://github.com/scikit-learn/scikit-learn/pull/13290>`_
    * Profileur
        * `cProfile <https://docs.python.org/3/library/profile.html>`_
        * `py-spy <https://github.com/benfred/py-spy>`_
        * `pyinstrument <https://github.com/joerick/pyinstrument>`_
        * `Nsight <https://developer.nvidia.com/nsight-visual-studio-edition>`_ (GPU)
* Culture
    * Librairies `BLAS <https://fr.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms>`_,
      `LAPACK <https://fr.wikipedia.org/wiki/LAPACK>`_
      - des algorithmes hyper-optimisés au long des décennies de leur existence
    * `JIT <https://fr.wikipedia.org/wiki/Compilation_%C3%A0_la_vol%C3%A9e>`_
    * `Quantization <https://pytorch.org/docs/stable/quantization.html>`_
    * `Sparse <https://en.wikipedia.org/wiki/Sparse_matrix>`_
    * Streaming Algorithm: :ref:`BJKSTrst`,
      `river <https://github.com/online-ml/river>`_,
      :ref:`l-ml2a-streaming-algorithm`, :ref:`l-ml2a-streaming-ml`,
      notes de cours : `Data Stream Algorithm
      <https://www.cs.dartmouth.edu/~ac/Teach/data-streams-lecnotes.pdf>`_

Séance 3
^^^^^^^^

* Modèle de mémoire (
* Description de la stack, pile d'appel, stackoverflow
* Threads
* GPU, bloc, threads, synchronisation

Séance 4
^^^^^^^^

**Paralléliser des calculs avec pytorch**

:epkg:`pytorch` est une librairie qui a su séduire beaucoup de développeurs
grâce à un design intuitif et à une documentation de bonne qualité.
Aujourd'hui se pose la question de créer un code rapide en dehors d'un système
existant ou d'étendre une librairie qui offre déjà beaucoup de fonctionnalités.
L'option qui est proposée ici est celle d'étendre *pytorch* dans la mesure
où les dernières versions de la librairies ont été pensées pour faciliter
ce scénario.

On peut utilier du code C++ depuis python ou utiliser du code
Python depuis C++. C'est le premier scénario qui est illustré.

torch

* `Custom C++ and CUDA Extensions
  <https://pytorch.org/tutorials/advanced/cpp_extension.html>`_
* `Pytorch C++ API <https://pytorch.org/cppdocs/>`_
* `td3a_cpp_deep <http://www.xavierdupre.fr/app/td3a_cpp_deep/helpsphinx/index.html>`_

CUDA

* `CUDA C/C++ Basics <https://www.nvidia.com/docs/IO/116711/sc11-cuda-c-basics.pdf>`_
* `CUDA Thread Indexing Cheatsheet
  <https://cs.calvin.edu/courses/cs/374/CUDA/CUDA-Thread-Indexing-Cheatsheet.pdf>`_
* `CUDA Thread Basics
  <http://users.wfu.edu/choss/CUDA/docs/Lecture%205.pdf>`_
* `CUDA 11 Features Revealed
  <https://developer.nvidia.com/blog/cuda-11-features-revealed/>`_

CUDA streams

* `CUDA Streams And Concurrency
  <https://developer.download.nvidia.com/CUDA/training/StreamsAndConcurrencyWebinar.pdf>`_

Visual Studio

* `NVIDIA Nsight Integration
  <https://developer.nvidia.com/nsight-tools-visual-studio-integration>`_

**Combiner pytorch avec autre chose**

La librairie pytorch utilise une structure de données appelée *Tensor*
pour représenter un vecteur, une matrice... Elle est décrite par :

* un vecteur *shape* (les dimensions)
* un vecteur *strides* (sous ensemble)
* un emplacement, une adresse
* un type (float32, float64, double, int64, ...)
* un device (CPU, GPU, ...)
* un numéro de device (s'il y a plusieus GPU)
* un destructeur permettant de détruire la structure (pas les données)

S'échanger fes informations d'une librairie à une autre, dans le plus simple
des cas veut dire les copier. Mais ça prend trop de temps d'où l'introduction
d'une structure commune d'échange (API).
Elle a été récemment introduite dans les dernières versions de torch.
Elle est encore en projets dans numpy.

* `DLPack <https://github.com/dmlc/dlpack>`_
* `torch.dlpack <https://pytorch.org/docs/stable/dlpack.html>`_
* about numpy `ENH: Implement the DLPack Array API protocols for ndarray.
  <https://github.com/numpy/numpy/pull/19083>`_
* Notion de `capsule en python <https://docs.python.org/3/c-api/capsule.html>`_

**Traiter un jeu gros de données**

La base `Open DAMIR : base complète sur les dépenses d'assurance maladie inter régimes
<https://www.data.gouv.fr/en/datasets/open-damir-base-complete-sur-les-depenses-dassurance-maladie-inter-regimes/>`_
est sans doute une base très intéressante mais aussi un défi quand on
souhaite s'y attaquer.

Streaming local

* `sqlite3 <https://www.sqlite.org/index.html>`_,
  `python.sqlite3 <https://docs.python.org/3/library/sqlite3.html>`_
* :epkg:`pandas_streaming` : surcouche autour des itérateur
  `pandas.read_csv
  <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html>`_
* serveur :epkg:`SQL` (PostGreSQL

Streaming distant

* `dask <https://dask.org/>`_, s'interface avec scikit-learm
* `spark <https://spark.apache.org/>`_

Voir également `awesome-streaming <https://project-awesome.org/manuzhang/awesome-streaming#streaming-library>`_.

**Histoires, problèmes résolus**

* nom des quarties de paris
* fusion d'annuaire, géocoding
* tournée du camion poubelle
* streaming, :epkg:`pandas_streaming`
* `complétion
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_nlp/completion_formalisation.html>`_
* `Distance entre deux graphes
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_algo/graph_distance.html>`_
* `arbre de décision et réseau de neurones
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/lr_trees.html>`_,
  `Un arbre de décision en réseaux de neurones
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/neural_tree.html>`_
* `régression quantile
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/regression_quantile.html>`_
* `plus proche voisins
  <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_ml/kppv.html>`_
* parallélisation
* einsum
    * `Compares implementations of Einsum
      <http://www.xavierdupre.fr/app/mlprodict/helpsphinx/gyexamples/plot_op_einsum.html?highlight=einsum>`_
    * `Einsum decomposition
      <http://www.xavierdupre.fr/app/mlprodict/helpsphinx/notebooks/einsum_decomposition.html?highlight=einsum>`_
    * `Decompose einsum into numpy operators
      <http://www.xavierdupre.fr/app/mlprodict/helpsphinx/blog/2021/2021-08-11_einsum.html?highlight=einsum>`_

Séance 5
^^^^^^^^

Séance 6
^^^^^^^^
