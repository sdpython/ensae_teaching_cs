
.. _l-expoinfo2a:

Exposés 2018 (2A)
=================

*en préparation*

.. contents::
    :local:
    :depth: 1

:ref:`Page principale du cours <l-td2a>`

Principe
++++++++

Un cours ne suffit pas pour aborder les nombreux
aspects du machine learning, tous ne sont pas utiles
tous les jours dans la vie d'un datascientiste,
la recherche est également très active dans ce domaine,
c'est un voeu pieux que d'écrire un cours à jour.
Il est important d'entretenir sa curiosité et
de se former seul. L'objectif de cet exposé est de présenter
pendant 10 à 15 minutes un thème ou un problème
non abordé en cours. Il est fait à plusieurs et
s'appuiera sur la lecture d'articles ou de documentation
de librairies. L'exposé devra inclure :

* Une synthèse ce que vous avez lu.
* Le problème auquel la méthode présentée répond.
* Existe-t-il des librairies qui implémentent la méthode ?
  Si oui, sont-elles simples d'utilisation,
  si non, l'algorithme est-il simple à implémenter ?
* Avez-vous des critiques quant à la méthode ?

L'exposé pourra porter sur un des thèmes suivants
ou un autre de votre choix après validation.
Lors de la présentation, chaque personne du groupe
devra s'exprimer.

Thèmes
++++++

* Méthode `LIME <https://eli5.readthedocs.io/en/latest/blackbox/lime.html>`_

    * `"Why Should I Trust You?": Explaining the Predictions of Any Classifier <https://arxiv.org/abs/1602.04938>`_
    * `Defining Locality for Surrogates in Post-hoc Interpretablity <https://128.84.21.199/abs/1806.07498v1>`_
    * module `eli5 <https://eli5.readthedocs.io/en/latest/index.html>`_

* Classification multi-label

    * `Multiclass-Multilabel Classification with More Classes than Examples <http://proceedings.mlr.press/v9/dekel10a/dekel10a.pdf>`_
    * `A Ranking-based KNN Approach for Multi-Label Classification <http://proceedings.mlr.press/v25/chiang12/chiang12.pdf>`_

* Factorization Machines

    * `Factorization Machines <https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf>`_
    * `Field-aware Factorization Machines in a Real-world Online Advertising System <https://arxiv.org/abs/1701.04099>`_
    * `Contextual and Position-Aware Factorization Machines for Sentiment Classification <https://arxiv.org/abs/1801.06172>`_

* Imputation de valeurs manquantes

    * `Imputation de données manquantes <https://www.math.univ-toulouse.fr/~besse/Wikistat/pdf/st-m-app-idm.pdf>`_
    * `Scalable Tensor Factorizations for Incomplete Data <https://arxiv.org/pdf/1005.2197.pdf>`_
    * `Much ado about nothing: A comparison of missing data methods and software to fit incomplete data regression models <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1839993/>`_

* Régression linéaire et sélection de variables

    * `Sélection bayésienne de variables en régression linéaire <https://www.ceremade.dauphine.fr/~xian/cmr06.pdf>`_
    * `Régression linéaire bayésienne <https://en.wikipedia.org/wiki/Bayesian_linear_regression>`_
    * `bayesian_linear_regression.py <https://github.com/wiseodd/probabilistic-models/blob/master/models/bayesian/bayesian_linear_regression.py>`_

* Bandits

    * `Learning to Interact <http://hunch.net/~jl/interact.pdf>`_
    * `Thompson Sampling with the Online Bootstrap <https://arxiv.org/pdf/1410.4009.pdf>`_

* Descente de gradient

    * `Dual Principal Component Pursuit <http://www.jmlr.org/papers/v19/17-436.html>`_
    * `Adam: A Method for Stochastic Optimization <https://arxiv.org/abs/1412.6980>`_
    * `HOGWILD!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent <https://arxiv.org/abs/1106.5730>`_
    * `Sparse Online Learning via Truncated Gradient <http://www.jmlr.org/papers/volume10/langford09a/langford09a.pdf>`_

* Clustering

    * `Consensus Clustering <https://en.wikipedia.org/wiki/Consensus_clustering>`_
    * `A Survey of Clustering Ensemble Algotihm <https://pdfs.semanticscholar.org/0d1b/7d01fb2634b6160a96bbdd73f918ed3859cb.pdf>`_

* Privacy

    * `k-anonymity <https://en.wikipedia.org/wiki/K-anonymity>`_
    * `A General Survey of Privacy-Preserving Data Mining Models and Algorithms <http://charuaggarwal.net/generalsurvey.pdf>`_
    * `Privacy Preserving Data Mining <http://web.stanford.edu/group/mmds/slides/mcsherry-mmds.pdf>`_

* Random Forest améliorées

    * `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_
    * `Extremely randomized trees <http://www.montefiore.ulg.ac.be/~ernst/uploads/news/id63/extremely-randomized-trees.pdf>`_
    * `Learning to rank with extremely randomized trees <http://proceedings.mlr.press/v14/geurts11a/geurts11a.pdf>`_
    * `Mondrian Forests: Efficient Online Random Forests <https://arxiv.org/abs/1406.2673>`_

* Point aberrants

    * `BoostClean: Automated Error Detection and Repair for Machine Learning <https://arxiv.org/pdf/1711.01299.pdf>`_
    * `Outlier Detection Techniques <https://archive.siam.org/meetings/sdm10/tutorial3.pdf>`_
    * `RANSAC <https://fr.wikipedia.org/wiki/RANSAC>`_
    * `Scorpion: Explaining Away Outliers in Aggregate Queries <http://sirrice.github.io/files/papers/scorpion-vldb13.pdf>`_

* Régressions linéaires pas classiques

    * `Intelligible Models for Classification and Regression <http://www.cs.cornell.edu/~yinlou/papers/lou-kdd12.pdf>`_
    * `Isotonic regression <https://en.wikipedia.org/wiki/Isotonic_regression>`_
    * `Online Isotonic Regression <http://proceedings.mlr.press/v49/kotlowski16.pdf>`_
    * `Iteratively reweighted least squares <https://en.wikipedia.org/wiki/Iteratively_reweighted_least_squares>`_
    * `RANSAC <https://fr.wikipedia.org/wiki/RANSAC>`_
    * `Multivariate Convex Regression with Adaptive Partitioning <http://www.jmlr.org/papers/volume14/hannah13a/hannah13a.pdf>`_
    * `Lattice Regression <https://papers.nips.cc/paper/3694-lattice-regression.pdf>`_

* Spiking Neural Networks

    * `Spiking neural networks, an introduction <http://www.ai.jonad.eu/materialy/download/sieci_neuronowe/2003-008.pdf>`_
    * `A Minimal Spiking Neural Network to Rapidly Train and Classify Handwritten Digits in Binary and 10-Digit Tasks <https://thesai.org/Downloads/IJARAI/Volume4No7/Paper_1-A_Minimal_Spiking_Neural_Network_to_Rapidly_Train.pdf>`_
    * `Training Deep Spiking Neural Networks Using Backpropagation <https://www.frontiersin.org/articles/10.3389/fnins.2016.00508/full>`_
    * `Spiking Neural Networks: Principles and Challenges <https://homepages.cwi.nl/~sbohte/publication/es2014-13Gruning.pdf>`_
    * `Python Tutorial: How to Write a Spiking Neural Network Simulation From Scratch <http://www.mjrlab.org/2014/05/08/tutorial-how-to-write-a-spiking-neural-network-simulation-from-scratch-in-python/>`_

* Détection de communauté

    * `Fast unfolding of communities in large networks <https://arxiv.org/abs/0803.0476>`_
    * `Partitioning Well-Clustered Graphs: Spectral Clustering Works! <http://proceedings.mlr.press/v40/Peng15.pdf>`_
    * `A Spectral Algorithm with Additive Clustering for the Recovery of Overlapping Communities in Networks <https://arxiv.org/pdf/1506.04158.pdf>`_

* Détection d'anomalies

    * `Robust Random Cut Forest Based Anomaly Detection On Streams <http://proceedings.mlr.press/v48/guha16.pdf>`_

* yield management

    * `Le yield managment pour les nuls <http://veilletourisme.ca/2004/05/27/le-yield-management-pour-les-nuls/>`_
    * `Machine-learning pour la prédiction des prix dans le secteur du tourisme en ligne <https://pastel.archives-ouvertes.fr/tel-01310537/document>`_
    * `Yield Management at American Airlines <https://classes.engineering.wustl.edu/2010/fall/ese403/software/Informs%20Articles/CH18%20Yield%20Management%20at%20American%20Airlines.pdf>`_
    * `Perishability of Data: Dynamic Pricing under Varying-Coefficient Models <http://www.jmlr.org/papers/volume18/17-061/17-061.pdf>`_

* Enchères

    * `Learning Algorithms for Second-Price Auctions with Reserve <http://jmlr.org/papers/volume17/14-499/14-499.pdf>`_
    * `Learning Simple Auctions <http://proceedings.mlr.press/v49/morgenstern16.pdf>`_

* Education

    * `Multi-Armed Bandits for Intelligent Tutoring Systems <http://www.pyoudeyer.com/JEDMClementetal15.pdf>`_
    * `Object learning through active exploration <https://flowers.inria.fr/ActiveExplorationICubTAMD2013.pdf>`_

* Détection de biais

    * `On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation <http://www.jmlr.org/papers/volume11/cawley10a/cawley10a.pdf>`_
    * `Learning Theory of Distributed Regression with Bias Corrected Regularization Kernel Network <http://www.jmlr.org/papers/volume18/17-423/17-423.pdf>`_
    * `Identifying Significant Predictive Bias in Classifiers <https://arxiv.org/pdf/1611.08292.pdf>`_
    * `On the reduction of biases in Big Data sets ofr the detection of irregular power usage <https://arxiv.org/pdf/1801.05627.pdf>`_

* Robustesse

    * `Preserving Statistical Validity in Adaptive Data Analysis∗ <https://arxiv.org/pdf/1411.2664.pdf>`_
