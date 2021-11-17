
.. _l-td3a:

==========================================================
Eléments logiciels pour le traitement des données massives
==========================================================

`Eléments logiciels pour le traitement des données massives
<https://www.ensae.fr/courses/elements-logiciels-pour-le-traitement-des-donnees-massives/>`_
(ENSAE)

Cours animé par :
Matthieu Durut,
Xavier Dupré.

Le cours est évalué avec un :ref:`projet informatique <l-projinfo3a>`.
Programme de l'année 2021 : :ref:`l-feuille-de-route-2021-3A`.

.. contents::
    :local:

------------

Eléments techniques
===================

.. _l-anatomie-ordi:

Anatomie et histoire d'un ordinateur
++++++++++++++++++++++++++++++++++++

* mémoire, cache, northbridge, southbridge
* CPU, GPU, FGPA, ASICS
* 2004 - espace entre deux circuits intégrés de 32 ns, passage à 24 ns ? effet quantique, passage d'électron
* optimisation des calculs, parallélisation, notion de cache et de latence

*Lectures*

* `Memory Latency over the years <https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html>`_
* `What every computer scientist should know about floating point
  <http://faculty.tarleton.edu/agapie/documents/cs_343_arch/papers/1991_Goldberg_FloatingPoint.pdf>`_
* `What every programmer should know about memory <https://www.akkadia.org/drepper/cpumemory.pdf>`_
* `Introduction to High Performance Scientific Computing <http://pages.tacc.utexas.edu/~eijkhout/istc/istc.html>`_
* `Zoologie des réseaux de neurones <http://www.asimovinstitute.org/neural-network-zoo/>`_
* `Teaching a machine how to play Mario
  <http://www.cs.cmu.edu/~tom7/mario/mario.pdf>`_
* `Introduction au système de recommandation par facteurs latents
  <https://datajobs.com/data-science-repo/Recommender-Systems-%5bNetflix%5d.pdf>`_
* `The Unreasonable Effectiveness of Data
  <http://static.googleusercontent.com/media/research.google.com/fr//pubs/archive/35179.pdf>`_
* :ref:`Après l'architecture Von Neumann <l-archi-vonneum-memory>`
* `Learning Efficient Algorithms with Hierarchical Attentive Memory <https://arxiv.org/pdf/1602.03218.pdf>`_
* `GotoBLAS <https://en.wikipedia.org/wiki/GotoBLAS>`_ (écrit par
  `Kazushige Gotō <https://en.wikipedia.org/wiki/Kazushige_Goto>`_)
* `Judy Arrays <https://en.wikipedia.org/wiki/Judy_array>`_,
  `site <http://judy.sourceforge.net/>`_, cette structure
  implémente un mapping int/int plus efficace que
  l'implémentation traditionnelle avec une table de hashage,
  la structure utilise les propriétés des caches dans les
  processeurs

*Machine Learning*

* `Infrastructure for Usable Machine Learning: The Stanford DAWN Project
  <https://arxiv.org/pdf/1705.07538.pdf>`_

CPU
+++

*Notebooks*

Le notebook suivant montre comment écrire du code C++ tout en
l'utilisant depuis Python pour mesurer une optimisation que
proposent les processeurs CPU : le :epkg:`branching`.

* `Measures branching in C++ from python
  <http://www.xavierdupre.fr/app/cpyquickhelper/helpsphinx/notebooks/
  cbenchmark_branching.html#cbenchmarkbranchingrst>`_

*Code*

* `ENH: Improves speed of one hot encoding
  <https://github.com/scikit-learn/scikit-learn/pull/15762>`_,
  cette pull request (PR) modifie un code très court pour réduire
  le nombre d'allocations mémoire avec :epkg:`numpy`
* `New K-means implementation for improved performances
  <https://github.com/scikit-learn/scikit-learn/pull/11950>`_,
  cette pull request (PR) étudie une nouvelle implémentation
  de l'algorithme des k-means, il n'est pas évident de se plonger
  dans le code mais il faut lire les commentaires qui illustrent
  les différences de performances selon que la machine utilise
  ses caches L2, L3.

*Lectures*

* `Weld: A Multithreading Technique Towards Latencytolerant VLIW Processors
  <http://tinker.cc.gatech.edu/symposia/hipc01.pdf>`_
* `Stackless Python <https://bitbucket.org/stackless-dev/stackless>`_ :
  implémentation de l'interpréteur de Python
  spécialisée dans le micro threading.
* `Why is it faster to process a sorted array than an unsorted array?
  <https://stackoverflow.com/questions/11227809/
  why-is-it-faster-to-process-a-sorted-array-than-an-unsorted-array/11227902#11227902>`_
* `How to optimize C and C++ code in 2018
  <https://medium.com/@aka.rider/how-to-optimize-c-and-c-code-in-2018-bd4f90a72c2b>`_
* `C++ Concurrency in Action (second edition, published 2019 by Manning Publications)
  <http://www.cplusplusconcurrencyinaction.com/>`_
* `Embarrassingly parallel for loops <https://joblib.readthedocs.io/en/latest/parallel.html>`_
* `ZeRO: Memory Optimizations Toward Training Trillion Parameter Models <https://arxiv.org/abs/1910.02054>`_
* `SLIDE : In Defense of Smart Algorithms over Hardware Acceleration for Large-Scale Deep Learning Systems <https://arxiv.org/abs/1903.03129>`_

*Vidéos*

* `C++ and Beyond 2012: Herb Sutter - atomic<> Weapons, 1 of 2
  <https://channel9.msdn.com/Shows/Going+Deep/
  Cpp-and-Beyond-2012-Herb-Sutter-atomic-Weapons-1-of-2>`_

*Librairies*

* `OpenMP <https://www.openmp.org/>`_ :
  c'est une librairie très utilisée pour paralléliser les calculs en C++
  sur plusieurs threads
* `OpenMPI <https://www.open-mpi.org/>`_ :
  c'est une librairie utilisée pour synchroniser des calculs parallélisés
  sur plusieurs processeurs (ou machines)
* `daal4py <https://intelpython.github.io/daal4py/>`_,
  réécriture d'algorithme de machine learning optimisée
  pour les processeurs Intel

*Outils*

* `Introducing PyTorch Profiler - the new and improved performance tool
  <https://pytorch.org/blog/introducing-pytorch-profiler-the-new-and-improved-performance-tool/>`_
* `DeepSpeed <https://github.com/microsoft/DeepSpeed>`_

Intel propose une version de l'interpréteur python avec
les principaux modules compilée spécifiquement
pour ces processeurs :
`Intel Python <https://software.intel.com/en-us/distribution-for-python>`_.
L'accélération n'est pas exceptionnelle pour un processeur
avec un ou deux coeurs, mais elle l'est particulièrement
sur des machines dédiées aux calculs.

GPU
+++

* `Convolution <https://fr.wikipedia.org/wiki/Produit_de_convolution>`_
* `Introduction to CUDA C <http://www.nvidia.com/content/gtc-2010/pdfs/2131_gtc2010.pdf>`_
* Notion de block, threads
* Echange d'information entre CPU et GPU
* `index de thread <http://www.martinpeniak.com/index.php?
  option=com_content&view=article&catid=17:updates&id=288:cuda-thread-indexing-explained>`_
* `syncthread <http://stackoverflow.com/questions/15240432/
  does-syncthreads-synchronize-all-threads-in-the-grid>`_
* `shared array <http://supercomputingblog.com/cuda/cuda-tutorial-3-thread-communication/>`_

*Lectures sur le GPU*

* `Comment apprendre aux ordinateurs à comprendre des images
  <https://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures?language=fr>`_
* `Scaling-up Machine Learning Chapitre 16 et 17
  <http://www.cambridge.org/catalogue/catalogue.asp?isbn=1139210408>`_
* `Quelques exemples graphiques de kernel 3x3 de convolution
  <https://docs.gimp.org/en/plug-in-convmatrix.html>`_
* `Introduction aux réseaux convolutifs
  <http://matlabtricks.com/post-5/3x3-convolution-kernels-with-online-demo#demo>`_,
  `Canny edge detector <https://en.wikipedia.org/wiki/Canny_edge_detector>`_
* `Understanding Convolution in Deep Learning
  <http://timdettmers.com/2015/03/26/convolution-deep-learning/>`_
* `Introduction au GPGPU
  <https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units>`_
* `Quelques éléments de consommation électrique sur les GPU et CPU
  <http://blog.octo.com/la-technologie-gpgpu-1ere-partie-le-cote-obscur-de-la-geforce/>`_
* `Inter-Block GPU Communication via Fast Barrier Synchronization
  <http://eprints.cs.vt.edu/archive/00001087/01/TR_GPU_synchronization.pdf>`_
* `CUDA C Programming Guide <https://docs.nvidia.com/cuda/cuda-c-programming-guide/>`_
* `Demystifying GPU Microarchitecture through Microbenchmarking
  <http://www.stuffedcow.net/files/gpuarch-ispass2010.pdf>`_
* `Mixed-Precision Training of Deep Neural Networks
  <https://devblogs.nvidia.com/parallelforall/mixed-precision-training-deep-neural-networks/>`_
* `Computing Higher Order Derivatives of Matrix and Tensor Expressions
  <https://papers.nips.cc/paper/
  7540-computing-higher-order-derivatives-of-matrix-and-tensor-expressions.pdf>`_
* `Enclaves as accelerators: learning lessons from GPU computing for designing efficient runtimes for enclaves
  <https://marksilberstein.com/wp-content/uploads/2020/04/systex16sgx.pdf>`_
* `WarpDrive: Extremely Fast End-to-End Deep Multi-Agent Reinforcement Learning on a GPU
  <https://arxiv.org/abs/2108.13976>`_
* `A friendly introduction to machine learning compilers and optimizers
  <https://huyenchip.com/2021/09/07/a-friendly-introduction-to-machine-learning-compilers-and-optimizers.html?fbclid=IwAR3Fc1TuBmKtu886Vur4gl4bSSvJDvViKeaY1r-AuBrj51rZ8YNMvYBI1dc#next>`_
* `CUDA C/C++ Streams and Concurrency
  <https://developer.download.nvidia.com/CUDA/training/StreamsAndConcurrencyWebinar.pdf>`_

*Lectures sur le C++*

* `Thinking in C++ <http://mindview.net/Books/TICPP/ThinkingInCPP2e.html>`_,
  Bruce Eckel
* `Effective C++ <http://www.aristeia.com/books.html>`_,
  Scott Meyers
* `What Every Programmer Should Know About Memory
  <http://www.akkadia.org/drepper/cpumemory.pdf>`_, Ulrich Drepper
* `The Art of Multiprocessor Programming <http://edc.tversu.ru/elib/inf/0189.pdf>`_,
  Maurice Herlihy, Nir Shavit
* `An Introduction to GPGPU Programming - CUDA Architecture
  <http://www.diva-portal.org/smash/get/diva2:447977/FULLTEXT01.pdf>`_,
  Rafia Inam
* `SizeBench: a new tool for analyzing Windows binary size
  <https://devblogs.microsoft.com/performance-diagnostics/sizebench-a-new-tool-for-analyzing-windows-binary-size/>`_

*Python*

* `GPU and pycuda or pyopencl on Windows
  <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/2017/2017-01-14_cuda.html>`_
* `Pycuda <https://mathema.tician.de/software/pycuda/>`_ ou
  `pyopencl <https://documen.tician.de/pyopencl/>`_
  pour ceux qui n'ont pas de carte
  `NVidia <http://www.nvidia.com/content/global/global.php>`_
* `theano <http://deeplearning.net/software/theano/>`_ (n'est plus maintenu)
* Tous les modules de deep learning.

*Bas niveau*

* `Low-Level Programming University
  <https://github.com/gurugio/lowlevelprogramming-university>`_

*Sécurité et bas niveau*

* `'Kernel memory leaking' Intel processor design flaw forces Linux, Windows redesign
  <http://www.theregister.co.uk/2018/01/02/intel_cpu_design_flaw/>`_
* `KASLR is Dead: Long Live KASLR <https://gruss.cc/files/kaiser.pdf>`_
* `Meltdown and Spectre <https://meltdownattack.com/>`_ :
  Bugs in modern computers leak passwords and sensitive data.
* `Meltdown <https://meltdownattack.com/meltdown.pdf>`_
* `Spectre Attacks: Exploiting Speculative Execution∗ <https://spectreattack.com/spectre.pdf>`_

*Optimisation*

* `No Bits Left Behind <http://sirrice.github.io/files/papers/bits-cidr11.pdf>`_ :
  l'article quelques stratégies bas-niveau pour optimiser les programmes

*Modules*

* `scikit-cuda <http://scikit-cuda.readthedocs.io/en/latest/index.html>`_
* `pycuda <https://developer.nvidia.com/pycuda>`_
* `numbapro <http://docs.continuum.io/numbapro/>`_
  (voir `A Monte Carlo Option Pricer
  <http://nbviewer.jupyter.org/gist/harrism/835a8ca39ced77fe751d>`_)

TPU, IPU, FGPA, ...
+++++++++++++++++++

* `Tensor Processor Unit (TPU)
  <https://en.wikipedia.org/wiki/Tensor_Processing_Unit>`_
* `How different is a TPU from GPU?
  <https://www.quora.com/How-different-is-a-TPU-from-GPU>`_
* `Using the Graphcore IPU for traditional HPC applications
  <http://workshops.inf.ed.ac.uk/accml/papers/2021/3rd_AccML_paper_5.pdf>`_
* `A List of Chip/IP for Deep Learning
  <https://medium.com/@shan.tang.g/a-list-of-chip-ip-for-deep-learning-48d05f1759ae>`_
* `FPGA vs GPU for Machine Learning Applications: Which one is better?
  <https://www.aldec.com/en/company/blog/167--fpgas-vs-gpus-for-machine-learning-applications-which-one-is-better>`_

BLAS, LAPACK, calcul matriciel
++++++++++++++++++++++++++++++

*Notebook*

Pas vraiment un notebook, un exemple d'utilisation
d'une fonction LAPACK dans un code python / cython :
`Résoudre une régression linéaire avec BLAS
<http://www.xavierdupre.fr/app/mlinsights/helpsphinx/mlinsights/mlmodel/direct_blas_lapack.cpython-37m-x86_64-linux-gnu.html?highlight=lapack#module-mlinsights.mlmodel.direct_blas_lapack>`_
(et le code associé `direct_blas_lapack.pyx
<https://github.com/sdpython/mlinsights/blob/master/mlinsights/mlmodel/direct_blas_lapack.pyx>`_).

*Lectures*

* `Fonctions LAPACK <http://www.netlib.org/lapack95/L90index/>`_
* `Introducing TensorNetwork, an Open Source Library for Efficient Tensor Calculations
  <https://ai.googleblog.com/2019/06/introducing-tensornetwork-open-source.html>`_,
  `Tensor in a Nutshell <https://arxiv.org/abs/1708.00006>`_
  (`github <https://github.com/google/tensornetwork>`_)
* `Anatomy of High-Performance Many-Threaded Matrix Multiplication
  <http://www.cs.utexas.edu/users/flame/pubs/blis3_ipdps14.pdf>`_
* `Computing the vector norm
  <http://fa.bianp.net/blog/2011/computing-the-vector-norm/>`_
* `Faster identification of optimal contraction sequences for tensor networks
  <https://arxiv.org/pdf/1304.6112.pdf>`_, cet article s'intéresse à
  l'implémentation optimale de réaliser une opération de type `einsum
  <https://numpy.org/devdocs/reference/generated/numpy.einsum.html>`_,
  les découvertes de l'article sont implémentées dans le module
  `opt-einsum <https://github.com/dgasmith/opt_einsum>`_.

*Modules*

* :epkg:`Cython`
* `BLAS <http://www.netlib.org/blas/>`_
* `LAPACK <http://www.netlib.org/lapack/>`_
* `OpenBLAS <http://www.openblas.net/>`_
* `cython-blis <https://github.com/explosion/cython-blis>`_

Optimisations logicielles
+++++++++++++++++++++++++

* `Compiling ONNX Neural Network Models Using MLIR
   <https://arxiv.org/pdf/2008.08272.pdf>`_
* `Compiling Classical ML Pipelines into Tensor Computations for One-size-fits-all Prediction Serving
  <http://learningsys.org/neurips19/assets/papers/27_CameraReadySubmission_Hummingbird%20(5).pdf>`_,
  `Taming Model Serving Complexity, Performance and Cost: A Compilation to Tensor Computations Approach
  <https://scnakandala.github.io/papers/TR_2020_Hummingbird.pdf>`_

Calcul matriciel
++++++++++++++++

* `How to optimize GEMM on CPU
  <https://tvm.apache.org/docs/tutorials/optimize/opt_gemm.html#sphx-glr-tutorials-optimize-opt-gemm-py>`_
* `HIGH PERFORMANCE CODE GENERATION IN MLIR: AN EARLY CASE STUDY WITH GEMM
  <https://arxiv.org/pdf/2003.00532v1.pdf>`_
* `Fireiron: A Data-Movement-Aware Scheduling Language for GPUs
  <https://dl.acm.org/doi/pdf/10.1145/3410463.3414632>`_
* `Linalg Dialect Rationale: The Case For Compiler-Friendly Custom Operations
  <https://mlir.llvm.org/docs/Rationale/RationaleLinalgDialect/>`_

Autres que CPU, GPU
+++++++++++++++++++

*Lectures*

* `Plasticine: A Reconfigurable Architecture For Parallel Patterns
  <http://csl.stanford.edu/~christos/publications/2017.plasticine.isca.pdf>`_
* `Introduction to CGRA
  <http://aces.snu.ac.kr/~bernhard/teaching/4541.775/lecture/4541.775.9.CGRA.Introduction.pdf>`_
  (`Coarse-Grained Reconfigurable Architecture <http://cccp.eecs.umich.edu/research/cgra.php>`_)
* `Tensor Processor Unit (TPU) <https://en.wikipedia.org/wiki/Tensor_processing_unit>`_
* `Application-specific integrated circuit (ASIC)
  <https://en.wikipedia.org/wiki/Application-specific_integrated_circuit>`_
* `Field-programmable gate array (FGPA)
  <https://en.wikipedia.org/wiki/Field-programmable_gate_array>`_
* `Ethereum: a Secure Decentralised Generalized Transaction Ledger EIP-150 Revision
  <http://gavwood.com/paper.pdf>`_

------------

Eléments théoriques
===================

Crypographie, block chain
+++++++++++++++++++++++++

* commitment et signature (RSA)
* Tiers de confiance et distributed consensus (PAXOS), `RAFT <https://raft.github.io/>`_
* Block chain, Bitcoin, Attque (Incentive, long term consensus, la probabilité qu'on soit en désaccord
  décroît avec le temps, monnaie stable, sûre, anonyme ?)
* `Ethereum <https://en.wikipedia.org/wiki/Ethereum>`_
* `Trustless Machine Learning Contracts; Evaluating and Exchanging Machine Learning Models on the Ethereum Blockchain
  <https://algorithmia.com/research/ml-models-on-blockchain>`_

*Lectures*

* The art of multiprocessor programming, *Nit Shavit*
* `CS176: Multiprocessor Synchronization <http://cs.brown.edu/courses/cs176/course_information.shtml>`_
* `Bitcoin and Cryptocurrency Technologies
  <https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf?a=1>`_
* `Delivery versus payment <http://www.multichain.com/blog/2015/09/delivery-versus-payment-blockchain/>`_
* `Ethereum official website <https://www.ethereum.org/>`_
* `Hello World in Ethereum <https://www.ethereum.org/greeter>`_
* `Introduction to Smart Contracts <http://solidity.readthedocs.io/en/develop/introduction-to-smart-contracts.html>`_
* `Monnaie, finance et économie réelle
  <http://www.editionsladecouverte.fr/catalogue/index-Monnaie__finance_et___conomie_r__elle-9782707185822.html>`_

.. _l-algo3A-distri:

Algorithmes Distribués
++++++++++++++++++++++

(à venir)

*Lectures*

* `Optimization Methods for Large-Scale Machine Learning <https://arxiv.org/abs/1606.04838>`_
* `Diagonal Rescaling For Neural Networks <https://arxiv.org/abs/1705.09319>`_
* `Communication Complexity of Distributed Convex Learning and Optimization
  <https://arxiv.org/pdf/1506.01900.pdf>`_
* `Fast Distributed Gradient Methods <https://arxiv.org/pdf/1112.2972.pdf>`_
* `A Generalized Accelerated Composite Gradient Method: Uniting Nesterov's Fast Gradient Method and FISTA
  <https://arxiv.org/abs/1705.10266>`_
* `Demystifying Parallel and Distributed Deep Learning: An In-Depth Concurrency Analysis
  <https://arxiv.org/pdf/1802.09941.pdf>`_
* `Measuring the Effects of Data Parallelismon Neural Network Training
  <http://jmlr.org/papers/volume20/18-789/18-789.pdf>`_
* `Scaling Distributed Training with Adaptive Summation
  <https://arxiv.org/abs/2006.02924>`_
* `ZeRO: Memory Optimizations Toward Training Trillion Parameter Models
  <https://arxiv.org/abs/1910.02054>`_

*Vidéo*

* `CS231n Winter 2016 Lecture 4 Backpropagation, Neural Networks 1
  <https://www.youtube.com/watch?v=GZTvxoSHZIo&feature=youtu.be>`_
* :ref:`Algorithmes classiques implémentés <l-blog-algo-impl>`
* `Fast Interesection of Sorted Lists Using SSE Instructions
  <https://highlyscalable.wordpress.com/2012/06/05/fast-intersection-sorted-lists-sse/>`_
* `Hogwild for Machine Learning on Multicore <https://www.youtube.com/watch?v=l5JqUvTdZts>`_

Compilateur, compilation à la volée, JIT
++++++++++++++++++++++++++++++++++++++++

La compilation à la volée ou
`JIT <https://en.wikipedia.org/wiki/Just-in-time_compilation>`_
pour Just in Time est utilisé pour optimiser une partie du code
après que l'exécution du programme ait démarrée. :epkg:`numba`
permet de demander à un compilateur *JIT* de remplacer le code
python par un code optimisé en C++ souvent beaucoup plus rapide
si ce code est purement numérique.

*Lectures*

à venir

*Modules*

* `ast <https://docs.python.org/3/library/ast.html>`_
* `ply <https://www.dabeaz.com/ply/ply.html>`_ (`Lex Yacc <http://dinosaur.compilertools.net/>`_)
* `llvmlite <https://github.com/numba/llvmlite>`_
* :epkg:`numba`
* `cffi <https://cffi.readthedocs.io/en/latest/>`_
* `jax <https://github.com/google/jax/>`_ : module pour calculer automatique
  la dérivée d'une fonction écrité avec :epkg:`numpy`
* `tensornetwork <https://github.com/google/TensorNetwork>`_
* `clang <https://clang.llvm.org/>`_

------------

Eléments logiciels
==================

Structures de données
+++++++++++++++++++++

* :ref:`codelistetuplerst`
* `liste chaînées <http://fr.wikipedia.org/wiki/Liste_cha%C3%AEn%C3%A9e>`_,
  `stack <http://fr.wikipedia.org/wiki/Pile_(informatique)>`_,
  `queue <http://en.wikipedia.org/wiki/Queue_(abstract_data_type)>`_,
  `dictionnaire <http://en.wikipedia.org/wiki/Associative_array>`_,
  `hashtable <https://fr.wikipedia.org/wiki/Table_de_hachage>`_
* graphe `BFS <http://en.wikipedia.org/wiki/Breadth-first_search>`_,
  `DFS <http://en.wikipedia.org/wiki/Depth-first_search>`_,
  `Red Black Tree <https://fr.wikipedia.org/wiki/Arbre_bicolore>`_
* `merge sort <http://en.wikipedia.org/wiki/Merge_sort>`_,
  `quicksort <http://en.wikipedia.org/wiki/Quicksort>`_,
  `heapsort <http://en.wikipedia.org/wiki/Heapsort>`_,
  `max heap <http://en.wikipedia.org/wiki/Min-max_heap>`_
* String matching, Rabin-Karp, automates finis
* Notions de coût algorithme, `NP Complet <https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-complet>`_

*Lectures*

* `Introduction to Algorithms, 3rd Edition
  <https://mcdtu.files.wordpress.com/2017/03/introduction-to-algorithms-3rd-edition-sep-2010.pdf>`_,
  Cormen, Leiserson, Rivest, Stein.
* `Cracking the Coding Interview <http://www.valleytalk.org/wp-content/uploads/2012/10/CrackCode.pdf>`_
* :ref:`Ecrire du code rapide <blog-post-optim-code-2018-08>` (article de blog)
* `The NumPy array: a structure for efficient numerical computation
  <https://hal.inria.fr/inria-00564007/document>`_

Threads et synchronisation
++++++++++++++++++++++++++

* threads, application multi-threadées
* variables globales, synchronisation
* threads et processus

*Lectures*

* `TIL: clock skew exists (distributed system) <http://jvns.ca/blog/2016/02/10/til-clock-skew-exists/>`_
* `Le dîner des philosophes <https://fr.wikipedia.org/wiki/D%C3%AEner_des_philosophes>`_,
  `The Part-Time Parliament <http://lamport.azurewebsites.net/pubs/lamport-paxos.pdf>`_
* `Is Parallel Programming Hard, And, If So, What Can You Do About It?
  <https://www.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html>`_
* `Time, Clocks, and the Ordering of Events in a Distributed System
  <http://lamport.azurewebsites.net/pubs/time-clocks.pdf>`_
* `Paxos Made Simple <http://lamport.azurewebsites.net/pubs/paxos-simple.pdf>`_
* `Linearizability: A Correctness Condition for Concurrent Objects
  <https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf>`_
* :ref:`Calcul distribué en Python (CPU) <blog-parallel-computing-2018>`

Plus proches voisins en grandes dimensions
++++++++++++++++++++++++++++++++++++++++++

* `Efficient Distributed Locality Sensitive Hashing <https://arxiv.org/abs/1210.7057>`_
* `Scalable Locality-Sensitive Hashing for Similarity Search in High-Dimensional, Large-Scale Multimedia Datasets
  <https://arxiv.org/abs/1310.4136>`_
* `Streaming Similarity Search over one Billion Tweets using Parallel Locality-Sensitive Hashing
  <http://istc-bigdata.org/plsh/docs/plsh_paper.pdf>`_

.. _l-algo-distribues-3a:

Distribution des calculs, stratégies de stockage, SQL NoSQL
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. toctree::
    :maxdepth: 2

    td_3a_s5_synthese
    notebooks/hash_distribution

*Lectures*

* `What Every Data Scientist Needs to Know about SQL <http://joshualande.com/data-science-sql>`_
* `Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services
  <https://users.ece.cmu.edu/~adrian/731-sp04/readings/GL-cap.pdf>`_
* `Distributed Algorithms in NoSQL Databases
  <https://highlyscalable.wordpress.com/2012/09/18/distributed-algorithms-in-nosql-databases/>`_
* `No SQL Data Modeling Techniques
  <https://highlyscalable.wordpress.com/2012/03/01/nosql-data-modeling-techniques/>`_
* `Distributed Systems and Parallel Computing
  <http://research.google.com/pubs/DistributedSystemsandParallelComputing.html>`_
* `Faster: A Concurrent Key-Value Store with In-Place Updates
  <https://www.microsoft.com/en-us/research/uploads/prod/2018/03/faster-sigmod18.pdf>`_

*Logiciels*

* `MongoDB <https://www.mongodb.com/>`_
* `rethinkdb <https://rethinkdb.com/>`_
  (python : `rethinkdb <https://pypi.python.org/pypi/rethinkdb/>`_)
* `FASTER <https://github.com/Microsoft/FASTER>`_

*Distribution des calculs en Python*

* :epkg:`dask`
* :epkg:`mars`
* :epkg:`h2o`
* :epkg:`joblib`

Compression des données
+++++++++++++++++++++++

Lorsque les données sont volumineuses. Une solution consiste à les compresser.

*Lectures*

* `Compressed sparse row (CSR, CRS or Yale format)
  <https://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_row_.28CSR.2C_CRS_or_Yale_format.29>`_
* `Moving away from HDF5 <http://cyrille.rossant.net/moving-away-hdf5/>`_

*Modules*

* `ASDF <http://asdf-standard.readthedocs.io/en/latest/>`_
* `blosc <http://blosc.org/>`_
* `h5py <http://www.h5py.org/>`_
* `Zarr <https://github.com/alimanfoo/zarr>`_

Workflow de données
+++++++++++++++++++

*Lectures*

* `Composable Multi-Threading for Python Libraries
  <http://conference.scipy.org/proceedings/scipy2016/pdfs/anton_malakhov.pdf>`_

*Modules*

* `Luigi <https://github.com/spotify/luigi>`_ (Python)
* `Threading Building Blocks <https://www.threadingbuildingblocks.org/>`_ (C++, Python)
* `Oozie <http://oozie.apache.org/>`_ (Hadoop, Spark)
* `Azkaban <https://azkaban.github.io/>`_ (Hadoop, Spark)

.. _l-deep-learning-3A:

Deep Learning
+++++++++++++

* deep learning : notebooks (Matthieu Bizien):
    * `Réseaux de neurones et Deep Learning
      <http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/chapters/deep_reseaux_de_neurones_et_deep_learning.html>`_.
    * `Transfer Learning
      <https://github.com/sdpython/2017_deeplearning_demo/blob/master/Fine_Tuning_Deep_CNNs_with_GPU_rendered.ipynb>`_
      (Olivier Grisel)
    * `Search images with deep learning
      <http://www.xavierdupre.fr/app/mlinsights/helpsphinx/notebooks/search_images.html#searchimagesrst>`_

* deep learning : présentations
    * `Introduction au Deep Learning
      <https://github.com/sdpython/ensae_teaching_cs/blob/master/_doc/sphinxdoc/source/specials/DEEP%20LEARNING%20FOR%20ENSAE.pdf>`_
    * :ref:`l-nolabel`
    * `Deep Learning 2017 <http://www.xavierdupre.fr/exposes/deeplearning/>`_ (avec Olivier Grisel)

*Vidéos*
    * `PyTorch in 5 Minutes <https://www.youtube.com/watch?v=nbJ-2G2GXL0>`_
    * `PyTorch Demystified, Why Did I Switch <https://www.youtube.com/watch?v=VMcRWYEKmhw>`_

*Cours*
    * :ref:`Cours de deep learning appliqués au NLP <blog-stanford-nlp-deep>`
    * `Companion Jupyter notebooks for the book "Deep Learning with Python"
      <https://github.com/fchollet/deep-learning-with-python-notebooks>`_
      (avec :epkg:`keras`, :epkg:`auto-keras`)

Framework de deep learning
++++++++++++++++++++++++++

* `TensorFlow <https://www.tensorflow.org/>`_ : GPU (Deep Learning Google)
* `Ray <https://github.com/ray-project/ray>`_ : (MPI, Berkeley),
  `Meet Ray, the Real-Time Machine-Learning Replacement for Spark
  <https://www.datanami.com/2017/03/28/meet-ray-real-time-machine-learning-replacement-spark/>`_
* `CUDA <https://developer.nvidia.com/how-to-cuda-c-cpp>`_ : GPU for NVidia
* `OpenCL <https://fr.wikipedia.org/wiki/OpenCL>`_
  (`Intel <https://software.intel.com/en-us/articles/opencl-drivers>`_,
  `NVidia Open CL <https://developer.nvidia.com/opencl>`_, ...)
* `pytorch <http://pytorch.org/>`_
* `caffe <http://caffe.berkeleyvision.org/>`_
* `mxnet <http://mxnet.incubator.apache.org/>`_
* `paddlepaddle <https://github.com/PaddlePaddle/Paddle>`_
* `chainer <https://chainer.org/>`_
* `gluon <https://mxnet.incubator.apache.org/api/python/gluon.html>`_

Quelques modules spécialisé dans le calcul GPU:

* `cupy <https://cupy.chainer.org/>`_
* `rapids <https://rapids.ai/>`_ (NVidia),
  en embryon de :epkg:`scikit-learn` pour GPU
* `tensorly <https://github.com/tensorly/tensorly>`_

Les ingénieurs cherchent sans arrêt à créer le bon outil, celui qui leur fait gagner
du temps lors de la conception de programmes complexes. Voici quelques outils
qui vont dans ce sens. Il faut toujours regarder la date de création de l'outil,
s'il est toujours maintenu, s'il est utilisé...

* `Zephyr <https://www.zephyrproject.org/>`_: real-time operating system
  (`RTOS <https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation_temps_r%C3%A9el>`_)
* `Rust <https://www.rust-lang.org/en-US/>`_ : langage de programmation dont la syntaxe est proche du C.
  C'est un langage plus sûr que C lorsque des threads sont utilisées car sa syntaxe
  interdit des constructions qui ne sont pas
  `thread safe <https://fr.wikipedia.org/wiki/Thread_safety>`_.
  Firefox est réécrit avec le langage RUST :
  `Firefox 48 : le navigateur va embarquer ses premiers composants en Rust
  <https://www.developpez.com/actu/101222/
  Firefox-48-le-navigateur-va-embarquer-ses-premiers-composants-en-Rust-le-langage-de-programmation-de-Mozilla-maintenant-disponible-en-version-1-10/>`_.

Données massives avec python
++++++++++++++++++++++++++++

Voir :ref:`l-td2A-massive-data`.

------------

Map Reduce
==========

Map Reduce en pratique
++++++++++++++++++++++

* Itérateurs, lien avec le SQL
  (voir `Séries temporelles et map reduce
  <http://www.xavierdupre.fr/app/sparkouille/helpsphinx/notebooks/map_reduce_timeseries.html>`_)
* Distribution à base de hash (voir :ref:`hashdistributionrst`)
* `Mapper, Reducer, Combiner, Partitionner <https://developer.yahoo.com/hadoop/tutorial/module4.html>`_
* Graphe d'exécution, synchronisation - *Map Reduce Flow Chart*
* Exemple : moyennes par groupes
* Pas d'ordre des observations, tri sur l'ensemble des données à éviter
* Produit matriciel, représentation d'une matrice en trois colonnes, matrice sparse
* Graphe : pas facile en map/reduce, exemple avec l'algorithme des
  :ref:`random walk with restarts <exposerwrrecommandationrst>`
* Problème des skewed datasets --> clés très mal distribués (voir :ref:`hashdistributionrst`)
* Descente du gradient : itératif
* Stratégie de parallélisation, propriétés mathématiques
  optimisation d'une fonction convexe
* Schéma des langages de map/reduce :
  `lazy evaluation <https://en.wikipedia.org/wiki/Lazy_evaluation>`_
   (évalusation presseuse, :epkg:`dask`, :epkg:`Spark`,
   :epkg:`mars`)

*Lectures*

* `Computer Systems for Big Data <https://columbia.github.io/systems-bigdata-class/2-lectures/>`_ (cours à Columbia)
* `Map-Reduce Patterns, Algorithms, and Use Cases <https://highlyscalable.wordpress.com/2012/02/01/mapreduce-patterns/>`_
* `MapReduce: Simplified Data Processing on Large Clusters
  <https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf>`_
* `Speeding up Hadoop Builds using Distributed Unit tests
  <https://highlyscalable.wordpress.com/2012/08/14/speeding-up-hadoop-builds-distributed-parallel-unit-tests-on-jenkins/>`_

*Vidéos*

* `Calculer sur des données massives <https://interstices.info/jcms/p_83082/calculer-sur-des-donnees-massives>`_
* `Le hachage <https://interstices.info/jcms/c_45523/le-hachage>`_

.. _l-spark-3a:

avec Spark et Spark SQL
+++++++++++++++++++++++

Les notebooks ont été déplacés sur
`Introduction à Spark <http://www.xavierdupre.fr/app/sparkouille/helpsphinx/lectures/index_spark.html>`_.

*Lectures*

* `Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing
  <http://www.cs.berkeley.edu/~matei/papers/2012/nsdi_spark.pdf>`_,
  Matei Zaharia, Mosharaf Chowdhury, Tathagata Das, Ankur Dave, Justin Ma, Murphy McCauley,
  Michael J. Franklin, Scott Shenker, Ion Stoica
* `From scikit-learn to Spark ML
  <http://blog.xebia.fr/2015/10/08/from-scikit-learn-to-spark-ml/>`_
* `Deep Dive into Catalyst <https://spark-summit.org/2016/events/deep-dive-into-catalyst-apache-spark-20s-optimizer/>`_,
  `Catalyst — Tree Manipulation Framework
  <https://jaceklaskowski.gitbooks.io/mastering-apache-spark/content/spark-sql-catalyst.html>`_
* `What is Tungsten for Apache Spark?
  <https://community.hortonworks.com/articles/72502/what-is-tungsten-for-apache-spark.html>`_,
  `Project Tungsten: Bringing Apache Spark Closer to Bare Metal
  <https://databricks.com/blog/2015/04/28/project-tungsten-bringing-spark-closer-to-bare-metal.html>`_
* `Spark SQL: Another 16x times faster after Tungsten
  <https://spark-summit.org/east-2017/events/spark-sql-another-16x-faster-after-tungsten/>`_
* `Databricks <https://docs.databricks.com/index.html#>`_

*FAQ*

* `Avoid GroupByKey
  <https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html>`_
* `What is the difference between cache and persist?
  <https://stackoverflow.com/questions/26870537/what-is-the-difference-between-cache-and-persist>`_

*Modules*

* `spark-sklearn <https://databricks.com/blog/2016/02/08/auto-scaling-scikit-learn-with-apache-spark.html>`_ :
  implémentation d'un grid search distribué pour `scikit-learn <http://scikit-learn.org/>`_.
* `turicreate <https://github.com/apple/turicreate>`_ : mélange de deep learning
  et de *spark*

.. _l-td3a-start:

Getting started, installation, setup
====================================

SPARK
+++++

Voir `Spark approximatif <http://www.xavierdupre.fr/app/sparkouille/helpsphinx/index.html>`_.

.. _l-td3a-biblio:

------------

Bibliographie
=============

**Cours**

* `Distributed Systems Fundamentals <https://columbia.github.io/ds1-class/>`_
* `Advanced Distributed Systems <https://columbia.github.io/ds2-class/>`_

**Articles**

* `Large Scale Distributed Deep Networks
  <http://www.cs.toronto.edu/~ranzato/publications/DistBeliefNIPS2012_withAppendix.pdf>`_,
  Jeffrey Dean, Greg S. Corrado, Rajat Monga, Kai Chen, Matthieu Devin, Quoc V. Le,
  Mark Z. Mao, Marc'Aurelio Ranzato, Andrew Senior, Paul Tucker, Ke Yang, Andrew Y. Ng
* `Stochastic Gradient Descent Tricks <http://research.microsoft.com/pubs/192769/tricks-2012.pdf>`_,
  Léon Bottou
* `A Fast Distributed Stochastic Gradient Descent Algorithm for Matrix Factorization
  <http://jmlr.org/proceedings/papers/v36/li14.pdf>`_,
  Fanglin Li, Bin Wu, Liutong Xu, Chuan Shi, Jing Shi
* `Parallelized Stochastic Gradient Descent <http://martin.zinkevich.org/publications/nips2010.pdf>`_,
  Martin A. Zinkevich, Markus Weimer, Alex Smola, Lihong Li
* `Topic Similarity Networks: Visual Analytics for Large Document Sets <http://arxiv.org/pdf/1409.7591v1.pdf>`_,
  Arun S. Maiya, Robert M. Rolfe
* `Low-dimensional Embeddings for Interpretable Anchor-based Topic Inference
  <http://mimno.infosci.cornell.edu/papers/EMNLP2014138.pdf>`_,
  Moontae Lee, David Mimno
* `K-means on Azure <http://apiacoa.org/publications/2010/durutrossi2010k-means-on.pdf>`_,
  Matthieu Durut, Fabrice Rossi
* `Confidence intervals for AB-test <http://arxiv.org/abs/1501.07768>`_,
  Cyrille Dubarry
* `Convergence Properties of the KMeans Algorithm
  <http://www.iro.umontreal.ca/~lisa/pointeurs/kmeans-nips7.pdf>`_

**Liens**

* `HackerRank <https://www.hackerrank.com/>`_
* `15+ Great Books for Hadoop <http://blog.matthewrathbone.com/2013/05/31/hadoop-resources---books.html>`_
* `A Roundup of Recent Text Analytics and Vis Work
  <http://blogger.ghostweather.com/2014/10/a-roundup-of-recent-text-analytics-and.html>`_
* `Don't use Hadoop - your data isn't that big <http://www.chrisstucchio.com/blog/2013/hadoop_hatred.html>`_
* `Remote Notebook with Azure <http://www.xavierdupre.fr/blog/2014-11-09_nojs.html>`_
* `Mahout 1.0 Features by Engine <https://mahout.apache.org/users/basics/algorithms.html>`_
* `Tutorial: Spark-GPU Cluster Dev in a Notebook <https://iamtrask.github.io/2014/11/22/spark-gpu/>`_
* `How CPU load averages work (and using them to triage webserver performance!)
  <http://jvns.ca/blog/2016/02/07/cpu-load-averages/>`_ *(2016/06)*

**Librairies / outils**

* `amazon-dsstne <https://github.com/amznlabs/amazon-dsstne>`_ : moteur de recommandation d'Amazon
* `Elastic Search <https://github.com/elastic/elasticsearch>`_ : moteur de recherche
* `Giraph <http://giraph.apache.org/>`_ : Large-scale graph processing on Hadoop
* `Hadoop <http://hadoop.apache.org/>`_ : système de fichier distribué + Map Reduce simple
* `Kafka <http://kafka.apache.org/>`_ :
  distributed streaming platform, conçu pour stocker et récupérer en temps réel des événements de sites web
* `Mesos <http://mesos.apache.org/>`_ :
  Apache Mesos abstracts CPU, memory, storage, and other compute resources away from machines
  (physical or virtual), `Elixi <https://github.com/ceteri/exelixi/wiki>`_
* `MLlib <https://spark.apache.org/mllib/>`_ :
  distributed machine learning for Spark
* `Parquet <http://parquet.apache.org/>`_ :
  Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem.
* `Presto <https://prestodb.io/>`_ : Distributed SQL Query Engine for Big Data (Facebook)
* `Spark <https://spark.apache.org/>`_ :
  Map Reduce, minimise les accès disques,
  (`DPark <https://github.com/douban/dpark>`_ clone Python de Spark, pas vraiment maintenu)
* `Spark SQL <https://spark.apache.org/sql/>`_ : SQL distribué, sur couche de Spark
* `Storm <https://storm.apache.org/>`_ :
  Apache Storm is a free and open source distributed realtime computation system,
  conçu pour distribuer des pipelines de traitements de données
* `YARN <https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/YARN.html>`_ : Ressource negociator
* `rapids <https://rapids.ai/>`_ : :epkg:`numpy`, :epkg:`pandas` version GPU
* `kubernetes <https://kubernetes.io/>`_ : automatisation de déploiement
  d'applications dans des containers (type `docker <https://www.docker.com/>`_)

*Librairies à suivre*

* `multiverso <https://github.com/microsoft/multiverso>`_ : framework de parallélisation
* `lightLDA <https://github.com/Microsoft/lightlda>`_ : Latent Dirichlet Application parallélisée
* `lightGBM <https://github.com/Microsoft/lightGBM>`_ :
  A fast, distributed, high performance gradient boosting (GBDT, GBRT, GBM or MART)
  framework based on decision tree algorithms.

Feuilles de routes des années passées
=====================================

.. toctree::
    :maxdepth: 1

    questions/route_3A_2017
    questions/cython_python
    questions/route_3A_2019
    questions/route_3A_2020
    questions/route_3A_2021
