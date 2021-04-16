
.. _l-feuille-de-route-2020-3A:

Feuille de route 2020-2021 (3A)
===============================

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

* `Introduction to CUDA C
  <https://www.nvidia.com/content/gtc-2010/pdfs/2131_gtc2010.pdf>`_
* `Comment apprendre aux ordinateurs à comprendre les images
  <https://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures?language=fr>`_
  (TED)
* `Scaling up Machine Learning: Parallel and Distributed Approaches
  <https://www.amazon.com/Scaling-Machine-Learning-Distributed-Approaches/dp/0521192242>`_
  Chapitre 16 et 17
* `Understanding Convolution in Deep Learning
  <http://timdettmers.com/2015/03/26/convolution-deep-learning/>`_
* `General-purpose computing on graphics processing units
  <https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units>`_
* `La technologie GPGPU – 1ère partie : Le côté obscur de la (Ge)Force
  <https://blog.octo.com/la-technologie-gpgpu-1ere-partie-le-cote-obscur-de-la-geforce/>`_
* `NVIDIA Ampere Architecture In-Depth
  <https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/>`_

Séance 3
^^^^^^^^

* `Bitcoin and Cryptocurrency Technologies
  <https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf?a=1>`_
* `Delivery versus payment on a blockchain
  <https://www.multichain.com/blog/2015/09/delivery-versus-payment-blockchain/>`_
* `ETHEREUM DEVELOPER RESOURCES
  <https://www.ethereum.org/greeter>`_
* `Monnaie, finance et économie réelle
  <http://www.editionsladecouverte.fr/catalogue/index-Monnaie__finance_et___conomie_r__elle-9782707185822.html>`_

Séance 4
^^^^^^^^

Séance 5
^^^^^^^^

Parallelisation CPU
* `Threads <https://realpython.com/intro-to-python-threading/>`_
* `Processus <https://docs.python.org/fr/3.9/library/subprocess.html>`_
* `sérialisation <https://python-guide-pt-br.readthedocs.io/fr/latest/scenarios/serialization.html>`_
* Plusieurs machines
* `AVX <https://fr.wikipedia.org/wiki/Advanced_Vector_Extensions>`_
* `Cache https://en.wikipedia.org/wiki/CPU_cache>`_

Cython
* `Presentation <https://cython.org/>`_
* Compilateur (`Windows <https://visualstudio.microsoft.com/fr/vs/community/>`_ (VS),
  `Linux <https://doc.ubuntu-fr.org/gcc>`_ (gcc),
  `MacOs <https://developer.apple.com/xcode/>`_ (xcode))
* `manylinux <https://www.python.org/dev/peps/pep-0513/>`_ sur pypi
* `C et Cython <https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html>`_
* Fichier `pyx <https://cython.readthedocs.io/en/latest/src/quickstart/build.html>`_
  et `setup.py <https://cython.readthedocs.io/en/latest/src/quickstart/build.html#building-a-cython-module-using-setuptools>`_
* `GIL <http://www.xavierdupre.fr/app/teachpyx/helpsphinx/notebooks/gil_example.html>`_
  (voir aussi `GIL <https://www.codeflow.site/fr/article/python-gil>`_)

Example
* `td3a_cpp <https://github.com/sdpython/td3a_cpp>`_ - multiplication de matrices
  `PR TD 2021/01 <https://github.com/sdpython/td3a_cpp/pull/2>`_
* `git <https://git-scm.com/>`_ (Windows)
* Fonction c, fonction pythons dans un pyx
* `prange <https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html>`_

Profiling
* `py-spy <https://github.com/benfred/py-spy>`_
* `pyinstrument <https://github.com/joerick/pyinstrument>`_
* Fonctionnement

Libraires pour aller plus vite sur CPU
* Librairies `BLAS <https://fr.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms>`_,
  `LAPACK <https://fr.wikipedia.org/wiki/LAPACK>`_
  - des algorithmes hyper-optimisés au long des décennies de leur existence
* `Pybind11 <https://github.com/pybind/pybind11>`_
* `Cffi <https://cffi.readthedocs.io/en/latest/>`_
* `Numba <https://numba.pydata.org/>`_
  (`JIT <https://fr.wikipedia.org/wiki/Compilation_%C3%A0_la_vol%C3%A9e>`_)
* `Torch <https://pytorch.org/docs/stable/torch.html>`_ = numpy + numba + pybind11

Stratégies d'optimisation
* Composer à partir de librairies implémentant des calculs standards (matriciel)
* Fusionner deux opérations en une seule (transposition + multiplication A B' ->
  `gemm <https://en.wikipedia.org/wiki/GEMM>`_),
  `opt_einsum <https://github.com/dgasmith/opt_einsum>`_
  = recomposition des calculs, nombre accru d'opérations,
  `MLPRegressor <http://www.xavierdupre.fr/app/mlprodict/helpsphinx/
  skl_converters/visual-neural_network-004.html>`_
* Implémentation spécifiques (graphes, arbres)
* `Quantization <https://pytorch.org/docs/stable/quantization.html>`_
* `Sparse <https://en.wikipedia.org/wiki/Sparse_matrix>`_
* Train / Predict, `ONNX <https://onnx.ai/>`_
* Sur plusieurs machines : `dask <https://dask.org/>`_,
  `spark <https://en.wikipedia.org/wiki/Apache_Spark>`_,
  `mpi <https://www.open-mpi.org/>`_
  (https://pytorch.org/docs/stable/distributed.html)

Demain
* CPU, GPU (Nvidia, `A100 <https://www.nvidia.com/en-us/data-center/a100/>`_), ARM
* `cupy <https://github.com/cupy/cupy>`_,
  `minpy <https://minpy.readthedocs.io/en/latest/index.html>`_,
  `numpy + GPU? <https://github.com/scikit-learn/scikit-learn/pull/16574>`_
* Librairies de calculs :
    * paralléliser efficacement nécessite une bonne connaissance des processeurs
    * Calculs matriciel sur CPU GPU
* Des gagnants et des perdants
    * `Trends pytorch,tensorflow,numpy <https://trends.google.com/trends/explore?date=all&geo=US&q=pytorch,tensorflow,numpy>`_
    * `NVidia Stock <https://www.google.com/search?q=nvidia+stock&oq=nvidia+stock&aqs=chrome..69i57.2676j0j4&sourceid=chrome&ie=UTF-8>`_
    * `Intel Stock <https://www.google.com/search?ei=T6kGYIP3FInYaIbNvbAC&q=intel+stock&oq=intel+stock&gs_lcp=CgZwc3ktYWIQAzIFCAAQkQIyBggAEAcQHjIGCAAQBxAeMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECAAQR1DhY1jFZ2D5aGgAcAN4AIABVYgBlAOSAQE2mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjD2tun2qfuAhUJLBoKHYZmDyYQ4dUDCA0&uact=5>`_

Liens `pytorch <https://pytorch.org/>`_:
* `CUSTOM C++ AND CUDA EXTENSIONS <https://pytorch.org/tutorials/advanced/cpp_extension.html?highlight=thread>`_
* `Convert Torch Tensor to flattened C++ array <https://discuss.pytorch.org/t/convert-torch-tensor-to-flattened-c-array/94341>`_
* `TORCH.FROM_NUMPY <https://pytorch.org/docs/stable/generated/torch.from_numpy.html>`_

**Notes en vrac**

Mémoire --> L3 --> L2 --> L1 --> 256o de registres - CPU1, CPU2, CPU3, CPU4 calcul --> L1 --> L2 --> L3 Mémoire

Program --> Thread principal  int A = 1 --> Thread principal
                                                                      --> thread secondaire

Processus

--> Traitement de texte --> 1 processus
--> Python --> 1 processus
--> Python --> 1 autre processus

Serialisation
Données --> d'une machine à une autre
Les machines ne communiquent que par réseau : une séquence d'octets.

Objet en python --> sérialise (pickle) --> zip --> communique --> dézippe --> désérialise

Produit --> 10 multiplication + 9 additions --> instructions AVX

Paralléliser avec : Thread + AVX

Paralléliser avec des processus:
    * Calculs compliqués sur des données séquentielles (indépendantes)
    * 4, 5 processus
Paralléliser avec les threads:
    * Petits calculs répétés plein de fois et pas nécessairement de manière séquentielle
    * AVX
    * Cache  --> C, C++, Python --> invisible (assembleur)
    * 7, 8 threads (nombre de cœurs)
Paralléliser avec les GPU
    * GPU
    * 128 threads GPU

Cython prérequis
    * Interpréteur python (3.7+)
    * Compilateur (gcc sur linux (clang), Visual Studio Windows (Community Edition), gcc MacOs

Programme
    * 1 fichier python
    * 1 fichier cython --> cython le convertit en C ou C++ --> compilé (DLL, .pyd, .so)  --> prêt à l'emploi

On veut paralléliser sous linux avec une librairie openmp sous Linux:
    * "Error: je ne trouve libomp" --> sudo apt-get install libomp (dépendance)

Plus rapide:
Matrice:
Langage sécurisé
	Liste = [1, 4, 5, 6]
	Liste[3] = 4  --> remplace un élément
        * Est-ce que 3 est un index admissible ?  (vérification)
        * Faire une copie ? Object mutable, immutable ?
Interprétable = portable
    * Python interprète le code python --> fichier .pyc créé
    * Liste[3] = 4  --> appelle une fonction python qui modifie l'objet liste
    * Le Code peut évoluer dynamiquement -->
        * Les erreurs de syntaxe ne sont pas toujours découvertes avant l'exécution
Mémoire
    * Jamais accès en python à la mémoire directement
    * Deux fonctions qui font des calculs :
        * Transmission d'objet python
        * En python, on ne manipule que des objets pythons
        * Objet en C --> créé son double en python pour le manipuler
Matrice numpy:
    * Structure en C + Objet python qui le contient
GIL --> obstacle
    * GIL = Global Interpreter Lock
    * C++ = 1 verrou pour protéger une zone de la mémoire, 2 zones = 2 verrous, 1 thread qui visite une zone, 1 autre thread qui visite l'autre zone,
        * Verrou: incrémente
    * GIL = 1 verrou pour toutes les zones mémoires
	
GIT
    * Outils de suivi de source
    * Historique des modifications (utile comme documentation)
    * Revenir en arrière
    * Faire le programme de deux façons différentes
        * Branch / fork

Utilisateur --> ajouter l'extension dot1.pyx
Utilisateur --> ajouter l'extension dot2.pyx

Deux versions --> dot1.pyx une autre avec dot2.pyx
Git --> va fusionner les deux pour avoir une unique avec dot1.pyx + dot2.pyx

Intégration continue :
    * S'assurer qu'à chaque modification, aucun bug n'a été créé ailleurs que dans le code modifié

Cython
    * Python setup.py build_ext --inplace
        * Convertit cython en C/C++
        * Compiler le code C/C++
        * Link --> .pyd (Windows) ou .so sous MacOs

M3 est modifiée par deux threads en même temps mais pas au même endroit --> donc pas besoin de verrou

A B C  -> (A B ) C ou A (B C)
